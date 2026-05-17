"""
Vector Database Manager using in-memory store + HuggingFace Inference API
for semantic code search.

Replaces local sentence-transformers + chromadb to stay within Vercel's
500 MB serverless bundle limit.
"""

import os
import json
import requests
import numpy as np
from pathlib import Path
from typing import List, Optional, Dict, Any
from src.models.data_models import FunctionNode, SearchResult, EmbeddingMetadata
from src.utils.logger import get_logger

logger = get_logger(__name__)

# ---------------------------------------------------------------------------
# Lightweight Embedding Client — calls HuggingFace Inference API
# ---------------------------------------------------------------------------

class HFEmbeddingClient:
    """Generate embeddings via the HuggingFace Inference API."""

    API_URL = "https://api-inference.huggingface.co/pipeline/feature-extraction/{model}"

    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model_name = model_name
        self.api_url = self.API_URL.format(model=model_name)
        self.token = os.getenv("HUGGINGFACE_API_TOKEN", "")
        self.headers = {}
        if self.token:
            self.headers["Authorization"] = f"Bearer {self.token}"

    def encode(self, texts, show_progress_bar: bool = False):
        """
        Encode one or more texts into embeddings.

        Args:
            texts: A string or list of strings.
            show_progress_bar: Ignored (kept for API compat).

        Returns:
            numpy array of shape (n, dim).
        """
        if isinstance(texts, str):
            texts = [texts]

        # HF Inference API accepts a list of strings
        payload = {"inputs": texts, "options": {"wait_for_model": True}}
        response = requests.post(
            self.api_url,
            headers=self.headers,
            json=payload,
            timeout=120,
        )

        if response.status_code != 200:
            raise RuntimeError(
                f"HF Inference API error {response.status_code}: {response.text}"
            )

        embeddings = response.json()
        return np.array(embeddings, dtype=np.float32)


# ---------------------------------------------------------------------------
# In-memory Vector Store — replaces ChromaDB
# ---------------------------------------------------------------------------

class InMemoryVectorStore:
    """Simple in-memory vector store with cosine-similarity search."""

    def __init__(self):
        self._ids: List[str] = []
        self._embeddings: List[np.ndarray] = []
        self._documents: List[str] = []
        self._metadatas: List[Dict[str, Any]] = []

    # -- mutation ----------------------------------------------------------

    def upsert(
        self,
        ids: List[str],
        embeddings: List[List[float]],
        documents: List[str],
        metadatas: List[Dict[str, Any]],
    ):
        for i, uid in enumerate(ids):
            emb = np.array(embeddings[i], dtype=np.float32)
            if uid in self._ids:
                idx = self._ids.index(uid)
                self._embeddings[idx] = emb
                self._documents[idx] = documents[i]
                self._metadatas[idx] = metadatas[i]
            else:
                self._ids.append(uid)
                self._embeddings.append(emb)
                self._documents.append(documents[i])
                self._metadatas.append(metadatas[i])

    def add(self, ids, embeddings, documents, metadatas):
        self.upsert(ids, embeddings, documents, metadatas)

    def delete(self, ids: Optional[List[str]] = None, where: Optional[Dict] = None):
        if ids:
            for uid in ids:
                if uid in self._ids:
                    idx = self._ids.index(uid)
                    self._ids.pop(idx)
                    self._embeddings.pop(idx)
                    self._documents.pop(idx)
                    self._metadatas.pop(idx)
        elif where:
            to_remove = []
            for idx, meta in enumerate(self._metadatas):
                if all(meta.get(k) == v for k, v in where.items()):
                    to_remove.append(idx)
            for idx in reversed(to_remove):
                self._ids.pop(idx)
                self._embeddings.pop(idx)
                self._documents.pop(idx)
                self._metadatas.pop(idx)

    # -- query -------------------------------------------------------------

    def query(
        self,
        query_embeddings: List[List[float]],
        n_results: int = 10,
        where: Optional[Dict] = None,
    ) -> Dict[str, Any]:
        if not self._embeddings:
            return {"ids": [[]], "distances": [[]], "metadatas": [[]], "documents": [[]]}

        q = np.array(query_embeddings[0], dtype=np.float32)
        q_norm = q / (np.linalg.norm(q) + 1e-10)

        scores = []
        for idx, emb in enumerate(self._embeddings):
            if where:
                meta = self._metadatas[idx]
                if not all(meta.get(k) == v for k, v in where.items()):
                    continue
            e_norm = emb / (np.linalg.norm(emb) + 1e-10)
            sim = float(np.dot(q_norm, e_norm))
            distance = 1.0 - sim  # cosine distance
            scores.append((idx, distance))

        scores.sort(key=lambda x: x[1])
        top = scores[:n_results]

        result_ids = [self._ids[i] for i, _ in top]
        result_distances = [d for _, d in top]
        result_metadatas = [self._metadatas[i] for i, _ in top]
        result_documents = [self._documents[i] for i, _ in top]

        return {
            "ids": [result_ids],
            "distances": [result_distances],
            "metadatas": [result_metadatas],
            "documents": [result_documents],
        }

    def get(self, where: Optional[Dict] = None) -> Dict[str, Any]:
        if where:
            indices = [
                i
                for i, m in enumerate(self._metadatas)
                if all(m.get(k) == v for k, v in where.items())
            ]
        else:
            indices = list(range(len(self._ids)))

        return {
            "ids": [self._ids[i] for i in indices],
            "metadatas": [self._metadatas[i] for i in indices],
            "documents": [self._documents[i] for i in indices],
        }

    def count(self) -> int:
        return len(self._ids)


# ---------------------------------------------------------------------------
# VectorDBManager — public API unchanged
# ---------------------------------------------------------------------------

class VectorDBManager:
    """Manage vector embeddings and similarity search for code functions."""
    
    def __init__(
        self,
        persist_directory: str = "./chroma_db",
        collection_name: str = "code_functions",
        model_name: str = "all-MiniLM-L6-v2",
        dimension: int = 384
    ):
        """
        Initialize Vector DB Manager.
        
        Args:
            persist_directory: Directory to persist ChromaDB
            collection_name: Name of the collection
            model_name: Embedding model name
            dimension: Embedding dimension
        """
        self.persist_directory = persist_directory
        self.collection_name = collection_name
        self.model_name = model_name
        self.dimension = dimension
        
        # Initialize embedding client (HF Inference API)
        hf_model = f"sentence-transformers/{model_name}" if "/" not in model_name else model_name
        logger.info(f"Using HF Inference API for embeddings: {hf_model}")
        self.embedder = HFEmbeddingClient(model_name=hf_model)
        
        # Initialize in-memory vector store
        self.collection = InMemoryVectorStore()
        logger.info(f"Initialized in-memory vector store: {collection_name}")
    
    def add_functions(self, functions: List[FunctionNode], batch_size: int = 32):
        """
        Add functions to vector database.
        
        Args:
            functions: List of FunctionNode objects
            batch_size: Batch size for embedding generation
        """
        if not functions:
            logger.warning("No functions to add")
            return
        
        logger.info(f"Adding {len(functions)} functions to vector DB...")
        
        # Prepare data
        ids = []
        documents = []
        metadatas = []
        
        for func in functions:
            # Create unique ID
            func_id = f"{func.file_path}::{func.name}"
            ids.append(func_id)
            
            # Get textified representation for embedding
            documents.append(func.get_textified())
            
            # Store metadata (convert lists to strings for compatibility)
            metadata = {
                "function_name": func.name,
                "file_path": func.file_path,
                "signature": func.signature,
                "parameters": ",".join(func.parameters) if func.parameters else "",  # Convert list to comma-separated string
                "return_type": func.return_type or "",
                "docstring": func.docstring or "",
                "full_code": "",  # We don't store full code in metadata to save space
                "line_start": func.line_start,
                "line_end": func.line_end,
                "textified": func.get_textified()
            }
            metadatas.append(metadata)
        
        # Generate embeddings in batches
        all_embeddings = []
        for i in range(0, len(documents), batch_size):
            batch = documents[i:i + batch_size]
            embeddings = self.embedder.encode(batch, show_progress_bar=False)
            all_embeddings.extend(embeddings.tolist())
        
        # Add to in-memory store
        try:
            self.collection.upsert(
                ids=ids,
                embeddings=all_embeddings,
                documents=documents,
                metadatas=metadatas
            )
            logger.info(f"Successfully added {len(functions)} functions to vector DB")
        except Exception as e:
            # Fallback to add if upsert not available
            logger.debug(f"Upsert failed, using add: {e}")
            self.collection.add(
                ids=ids,
                embeddings=all_embeddings,
                documents=documents,
                metadatas=metadatas
            )
            logger.info(f"Successfully added {len(functions)} functions to vector DB")
    
    def search_similar(
        self,
        query: str,
        top_k: int = 10,
        min_similarity: float = 0.7,
        max_k: int = 5,
        dynamic_k: bool = True,
        filter_dict: Optional[Dict[str, Any]] = None
    ) -> List[SearchResult]:
        """
        Search for similar functions using semantic similarity.
        
        Args:
            query: Query string (function description or code snippet)
            top_k: Initial number of results to retrieve
            min_similarity: Minimum similarity threshold
            max_k: Maximum number of results to return
            dynamic_k: Whether to use dynamic k-retrieval
            filter_dict: Optional metadata filters
            
        Returns:
            List of SearchResult objects
        """
        # Generate query embedding
        query_embedding = self.embedder.encode(query, show_progress_bar=False).tolist()
        
        # Search in vector store
        results = self.collection.query(
            query_embeddings=[query_embedding[0] if isinstance(query_embedding[0], list) else query_embedding],
            n_results=top_k,
            where=filter_dict
        )
        
        # Process results
        search_results = []
        
        if not results['ids'] or not results['ids'][0]:
            logger.info("No results found")
            return search_results
        
        for i, func_id in enumerate(results['ids'][0]):
            # Calculate similarity score (distances are cosine distances)
            distance = results['distances'][0][i]
            similarity = 1 - distance  # Cosine distance to similarity
            
            # Apply similarity threshold
            if dynamic_k and similarity < min_similarity:
                continue
            
            # Reconstruct FunctionNode from metadata
            metadata = results['metadatas'][0][i]
            
            # Convert comma-separated string back to list
            parameters = metadata['parameters'].split(',') if metadata['parameters'] else []
            
            function = FunctionNode(
                name=metadata['function_name'],
                file_path=metadata['file_path'],
                signature=metadata['signature'],
                parameters=parameters,
                return_type=metadata.get('return_type') or None,
                docstring=metadata.get('docstring') or None,
                body_preview=metadata['textified'],
                line_start=metadata['line_start'],
                line_end=metadata['line_end'],
                calls=[],
                imports_used=[]
            )
            
            search_results.append(SearchResult(
                function=function,
                similarity_score=similarity,
                rank=i + 1
            ))
            
            # Apply max_k limit
            if dynamic_k and len(search_results) >= max_k:
                break
        
        logger.info(f"Found {len(search_results)} similar functions (threshold: {min_similarity})")
        return search_results
    
    def search_by_function_name(self, function_name: str) -> Optional[FunctionNode]:
        """
        Search for a function by exact name.
        
        Args:
            function_name: Name of the function
            
        Returns:
            FunctionNode if found, None otherwise
        """
        results = self.collection.get(
            where={"function_name": function_name}
        )
        
        if not results['ids']:
            return None
        
        # Return first match
        metadata = results['metadatas'][0]
        
        # Convert comma-separated string back to list
        parameters = metadata['parameters'].split(',') if metadata['parameters'] else []
        
        return FunctionNode(
            name=metadata['function_name'],
            file_path=metadata['file_path'],
            signature=metadata['signature'],
            parameters=parameters,
            return_type=metadata.get('return_type') or None,
            docstring=metadata.get('docstring') or None,
            body_preview=metadata['textified'],
            line_start=metadata['line_start'],
            line_end=metadata['line_end'],
            calls=[],
            imports_used=[]
        )
    
    def update_function(self, function: FunctionNode):
        """
        Update a function in the vector database.
        
        Args:
            function: Updated FunctionNode
        """
        func_id = f"{function.file_path}::{function.name}"
        
        # Delete old entry
        try:
            self.collection.delete(ids=[func_id])
        except Exception:
            pass
        
        # Add new entry
        self.add_functions([function])
        logger.info(f"Updated function: {func_id}")
    
    def delete_function(self, file_path: str, function_name: str):
        """
        Delete a function from the vector database.
        
        Args:
            file_path: File path
            function_name: Function name
        """
        func_id = f"{file_path}::{function_name}"
        
        try:
            self.collection.delete(ids=[func_id])
            logger.info(f"Deleted function: {func_id}")
        except Exception as e:
            logger.warning(f"Failed to delete function {func_id}: {e}")
    
    def delete_file_functions(self, file_path: str):
        """
        Delete all functions from a specific file.
        
        Args:
            file_path: File path
        """
        try:
            self.collection.delete(
                where={"file_path": file_path}
            )
            logger.info(f"Deleted all functions from: {file_path}")
        except Exception as e:
            logger.warning(f"Failed to delete functions from {file_path}: {e}")
    
    def get_all_functions(self) -> List[FunctionNode]:
        """
        Get all functions from the vector database.
        
        Returns:
            List of all FunctionNode objects
        """
        results = self.collection.get()
        
        functions = []
        for metadata in results['metadatas']:
            # Convert comma-separated string back to list
            parameters = metadata['parameters'].split(',') if metadata['parameters'] else []
            
            function = FunctionNode(
                name=metadata['function_name'],
                file_path=metadata['file_path'],
                signature=metadata['signature'],
                parameters=parameters,
                return_type=metadata.get('return_type') or None,
                docstring=metadata.get('docstring') or None,
                body_preview=metadata['textified'],
                line_start=metadata['line_start'],
                line_end=metadata['line_end'],
                calls=[],
                imports_used=[]
            )
            functions.append(function)
        
        return functions
    
    def get_stats(self) -> Dict[str, Any]:
        """
        Get statistics about the vector database.
        
        Returns:
            Dict with statistics
        """
        count = self.collection.count()
        
        return {
            'total_functions': count,
            'collection_name': self.collection_name,
            'model_name': self.model_name,
            'dimension': self.dimension
        }
    
    def reset(self):
        """Reset the vector database (delete all data)."""
        self.collection = InMemoryVectorStore()
        logger.info("Vector database reset")

# Made with Bob
