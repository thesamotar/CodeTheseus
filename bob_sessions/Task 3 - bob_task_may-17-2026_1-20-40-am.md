**User:**

<task>
refer to the 'ARCHITECTURE.md' (see below for file content) and start building as mentioned
</task>

<file_content path="ARCHITECTURE.md">
  1 | agent/context_builder.py`)
  2 |    - Build global and local context
  3 |    - Implement cumulative subtask memory
  4 |    - Implement dynamic k-retrieval
  5 | 
  6 | 10. **Implement agent orchestrator** (`agent/agent.py`)
  7 |     - Coordinate subtask execution
  8 |     - Integrate with LLM
  9 |     - Handle mode switching
 10 | 
 11 | ### Phase 4: Metric System (Week 4)
 12 | 
 13 | 11. **Implement namespace checker** (`metrics/namespace_checker.py`)
 14 |     - Parse generated code
 15 |     - Extract function calls
 16 |     - Calculate reuse score
 17 | 
 18 | 12. **Implement structural matcher** (`metrics/structural_matcher.py`)
 19 |     - Extract structural tokens
 20 |     - Calculate Jaccard similarity
 21 |     - Detect violations
 22 | 
 23 | 13. **Implement dependency validator** (`metrics/dependency_validator.py`)
 24 |     - Check call site compatibility
 25 |     - Validate imports
 26 |     - Detect breaking changes
 27 | 
 28 | 14. **Implement explanation generator** (`metrics/explanation_generator.py`)
 29 |     - Generate failure explanations
 30 |     - Suggest fixes
 31 |     - Provide examples
 32 | 
 33 | 15. **Implement metric orchestrator** (`metrics/metric.py`)
 34 |     - Coordinate all validators
 35 |     - Implement retry logic
 36 |     - Generate final results
 37 | 
 38 | ### Phase 5: Integration & Testing (Week 5)
 39 | 
 40 | 16. **End-to-end integration**
 41 |     - Connect all components
 42 |     - Implement CLI interface
 43 |     - Add configuration loading
 44 | 
 45 | 17. **Comprehensive testing**
 46 |     - Unit tests for each component
 47 |     - Integration tests for workflows
 48 |     - Test on real repositories
 49 | 
 50 | 18. **Documentation & Examples**
 51 |     - API documentation
 52 |     - Usage examples
 53 |     - Troubleshooting guide
 54 | 
 55 | ---
 56 | 
 57 | ## Testing Strategy
 58 | 
 59 | ### Unit Tests
 60 | 
 61 | **Test Coverage Requirements**: 80% minimum
 62 | 
 63 | **Key Test Cases**:
 64 | 
 65 | 1. **AST Parser Tests**
 66 |    - Parse valid Python files
 67 |    - Handle syntax errors gracefully
 68 |    - Extract imports correctly (including aliases)
 69 |    - Extract function signatures with type hints
 70 |    - Extract function calls (simple, nested, method calls)
 71 | 
 72 | 2. **Dependency Graph Tests**
 73 |    - Build import graph correctly
 74 |    - Build call graph correctly
 75 |    - Detect circular dependencies
 76 |    - Traverse graph (BFS, DFS)
 77 |    - Handle missing imports
 78 | 
 79 | 3. **Vector DB Tests**
 80 |    - Store and retrieve embeddings
 81 |    - Search with similarity threshold
 82 |    - Handle batch operations
 83 |    - Update existing embeddings
 84 |    - Persist and load from disk
 85 | 
 86 | 4. **Namespace Checker Tests**
 87 |    - Detect function calls correctly
 88 |    - Resolve qualified names
 89 |    - Handle import aliases
 90 |    - Calculate reuse score accurately
 91 |    - Handle edge cases (no calls, all new calls)
 92 | 
 93 | 5. **Structural Matcher Tests**
 94 |    - Extract structural tokens correctly
 95 |    - Calculate Jaccard similarity accurately
 96 |    - Detect plagiarism (high similarity + no reuse)
 97 |    - Avoid false positives (common patterns)
 98 |    - Handle different code styles
 99 | 
100 | 6. **Dependency Validator Tests**
101 |    - Detect breaking changes
102 |    - Validate signature compatibility
103 |    - Check import resolution
104 |    - Handle transitive dependencies
105 | 
106 | ### Integration Tests
107 | 
108 | **Test Scenarios**:
109 | 
110 | 1. **Full Indexing Workflow**
111 |    - Index sample repository
112 |    - Verify all functions indexed
113 |    - Verify dependency graph complete
114 |    - Verify search returns relevant results
115 | 
116 | 2. **Code Generation Workflow (Legacy Mode)**
117 |    - Submit task request
118 |    - Verify subtask decomposition
119 |    - Verify context building
120 |    - Verify code generation
121 |    - Verify metric validation
122 |    - Verify final code quality
123 | 
124 | 3. **Code Generation Workflow (Greenfield Mode)**
125 |    - Submit task request
126 |    - Verify basic validation only
127 |    - Verify no metric enforcement
128 | 
129 | 4. **Retry Logic**
130 |    - Submit task that initially fails validation
131 |    - Verify explanation generation
132 |    - Verify retry with explanation
133 |    - Verify eventual success or max retries
134 | 
135 | 5. **Incremental Index Update**
136 |    - Modify file in repository
137 |    - Update index
138 |    - Verify changes reflected
139 |    - Verify dependent files updated
140 | 
141 | ### Test Repositories
142 | 
143 | **Create 3 test repositories**:
144 | 
145 | 1. **Simple Repository** (10 files, 50 functions)
146 |    - Basic utilities (math, string, file operations)
147 |    - Clear dependencies
148 |    - No circular imports
149 | 
150 | 2. **Medium Repository** (50 files, 200 functions)
151 |    - Multiple modules
152 |    - Some circular dependencies
153 |    - Mix of simple and complex functions
154 | 
155 | 3. **Complex Repository** (100+ files, 500+ functions)
156 |    - Real-world structure
157 |    - Deep dependency chains
158 |    - Various coding patterns
159 | 
160 | ---
161 | 
162 | ## Deployment Guide
163 | 
164 | ### Prerequisites
165 | 
166 | ```bash
167 | # Python 3.9+
168 | python --version
169 | 
170 | # Install dependencies
171 | pip install -r requirements.txt
172 | ```
173 | 
174 | ### Installation
175 | 
176 | ```bash
177 | # Clone repository
178 | git clone https://github.com/yourusername/context-aware-agent.git
179 | cd context-aware-agent
180 | 
181 | # Install package
182 | pip install -e .
183 | 
184 | # Verify installation
185 | context-agent --version
186 | ```
187 | 
188 | ### Configuration
189 | 
190 | ```bash
191 | # Create config file
192 | cp config.example.yaml config.yaml
193 | 
194 | # Edit configuration
195 | vim config.yaml
196 | ```
197 | 
198 | ### Usage
199 | 
200 | **1. Index a repository**:
201 | ```bash
202 | context-agent index /path/to/repository
203 | ```
204 | 
205 | **2. Generate code (Legacy Mode)**:
206 | ```bash
207 | context-agent generate \
208 |   --request "Add email validation to user_service.py" \
209 |   --target-file src/services/user_service.py \
210 |   --mode legacy
211 | ```
212 | 
213 | **3. Generate code (Greenfield Mode)**:
214 | ```bash
215 | context-agent generate \
216 |   --request "Create new payment processing module" \
217 |   --target-file src/services/payment_service.py \
218 |   --mode greenfield
219 | ```
220 | 
221 | **4. Update index after changes**:
222 | ```bash
223 | context-agent update-index \
224 |   --files src/services/user_service.py src/utils/validators.py
225 | ```
226 | 
227 | **5. Query similar functions**:
228 | ```bash
229 | context-agent search \
230 |   --query "email validation" \
231 |   --top-k 5
232 | ```
233 | 
234 | ---
235 | 
236 | ## Performance Considerations
237 | 
238 | ### Indexing Performance
239 | 
240 | **Expected Performance**:
241 | - Small repo (10 files): ~5 seconds
242 | - Medium repo (50 files): ~30 seconds
243 | - Large repo (500 files): ~5 minutes
244 | 
245 | **Optimization Strategies**:
246 | 1. **Parallel processing**: Parse files in parallel using multiprocessing
247 | 2. **Batch embedding**: Embed functions in batches of 32
248 | 3. **Incremental updates**: Only re-index modified files
249 | 4. **Caching**: Cache parsed ASTs for unchanged files
250 | 
251 | ### Query Performance
252 | 
253 | **Expected Performance**:
254 | - Vector search: <100ms for top-5 results
255 | - Dependency graph traversal: <50ms
256 | - Full validation: <500ms
257 | 
258 | **Optimization Strategies**:
259 | 1. **Index optimization**: Use HNSW index in ChromaDB
260 | 2. **Lazy loading**: Load full function code only when needed
261 | 3. **Result caching**: Cache frequent queries
262 | 
263 | ### Memory Usage
264 | 
265 | **Expected Memory**:
266 | - Small repo: ~100MB
267 | - Medium repo: ~500MB
268 | - Large repo: ~2GB
269 | 
270 | **Optimization Strategies**:
271 | 1. **Streaming**: Process files in streaming fashion
272 | 2. **Disk-backed storage**: Use ChromaDB persistence
273 | 3. **Garbage collection**: Explicitly free memory after processing
274 | 
275 | ---
276 | 
277 | ## Extensibility Points
278 | 
279 | ### 1. Custom Embedders
280 | 
281 | ```python
282 | # Implement custom embedder interface
283 | class CustomEmbedder:
284 |     def embed(self, texts: List[str]) -> np.ndarray:
285 |         """Generate embeddings for texts."""
286 |         pass
287 |         
288 | # Register in config
289 | config["indexing"]["embedder"]["custom_class"] = "path.to.CustomEmbedder"
290 | ```
291 | 
292 | ### 2. Custom Validators
293 | 
294 | ```python
295 | # Add custom validation logic
296 | class CustomValidator:
297 |     def validate(self, generated_code: str) -> ValidationResult:
298 |         """Custom validation logic."""
299 |         pass
300 |         
301 | # Register in metric system
302 | metric_validator.add_validator(CustomValidator())
303 | ```
304 | 
305 | ### 3. Custom LLM Providers
306 | 
307 | ```python
308 | # Implement LLM provider interface
309 | class CustomLLMProvider:
310 |     def generate(self, prompt: str, **kwargs) -> str:
311 |         """Generate code using custom LLM."""
312 |         pass
313 |         
314 | # Register in config
315 | config["agent"]["llm"]["custom_provider"] = "path.to.CustomLLMProvider"
316 | ```
317 | 
318 | ### 4. Custom Metrics
319 | 
320 | ```python
321 | # Define custom metric
322 | class CustomMetric:
323 |     def calculate(self, generated_code: str, context: Dict) -> float:
324 |         """Calculate custom metric score."""
325 |         pass
326 |         
327 | # Register in metric system
328 | metric_validator.add_metric("custom_metric", CustomMetric())
329 | ```
330 | 
331 | ---
332 | 
333 | ## Troubleshooting
334 | 
335 | ### Common Issues
336 | 
337 | **1. Indexing fails with "Module not found"**
338 | - **Cause**: Repository has missing dependencies
339 | - **Solution**: Install repository dependencies or exclude problematic files
340 | 
341 | **2. Vector search returns irrelevant results**
342 | - **Cause**: Embeddings not capturing semantic meaning
343 | - **Solution**: Try different embedding model or adjust similarity threshold
344 | 
345 | **3. Validation always fails**
346 | - **Cause**: Thresholds too strict
347 | - **Solution**: Adjust thresholds in config.yaml
348 | 
349 | **4. High memory usage during indexing**
350 | - **Cause**: Large repository with many functions
351 | - **Solution**: Enable streaming mode or increase system memory
352 | 
353 | **5. Slow code generation**
354 | - **Cause**: LLM API rate limits or slow model
355 | - **Solution**: Use faster model or implement caching
356 | 
357 | ---
358 | 
359 | ## Future Enhancements
360 | 
361 | ### Short-term (Next 3 months)
362 | 
363 | 1. **Multi-language support**: Add JavaScript, TypeScript, Java
364 | 2. **IDE integration**: VS Code extension
365 | 3. **Web UI**: Browser-based interface
366 | 4. **Batch processing**: Process multiple files simultaneously
367 | 5. **Performance profiling**: Built-in profiler for optimization
368 | 
369 | ### Medium-term (6 months)
370 | 
371 | 1. **Cross-repository search**: Search across multiple repositories
372 | 2. **Semantic code search**: Natural language queries
373 | 3. **Automated refactoring**: Suggest refactoring opportunities
374 | 4. **Code quality metrics**: Track code quality over time
375 | 5. **Team collaboration**: Multi-user support
376 | 
377 | ### Long-term (1 year)
378 | 
379 | 1. **AI-powered architecture analysis**: Suggest architectural improvements
380 | 2. **Automated testing**: Generate tests for new code
381 | 3. **Documentation generation**: Auto-generate documentation
382 | 4. **Code review automation**: Automated code review comments
383 | 5. **Learning from feedback**: Improve based on user corrections
384 | 
385 | ---
386 | 
387 | ## Appendix
388 | 
389 | ### A. Mathematical Formulas
390 | 
391 | **Reuse Score**:
392 | $$\text{Reuse Score} = \frac{|\text{Called Functions} \cap \text{Repo Functions}|}{|\text{Called Functions}|}$$
393 | 
394 | **Jaccard Similarity**:
395 | $$J(A, B) = \frac{|A \cap B|}{|A \cup B|}$$
396 | 
397 | **Structural Plagiarism Detection**:
398 | $$\text{Plagiarism} = (\text{Structural Sim} \geq 0.85) \land (\text{Namespace Reuse} = 0) \land (\text{Semantic Sim} \geq 0.75)$$
399 | 
400 | ### B. Example Prompts
401 | 
402 | **Subtask Decomposition Prompt**:
403 | ```
404 | You are a task planner. Break down this request into 3-5 isolated subtasks.
405 | 
406 | Request: Add email validation to user registration in user_service.py
407 | 
408 | Each subtask should:
409 | - Be independently executable
410 | - Have clear input/output
411 | - Focus on single responsibility
412 | 
413 | Output format:
414 | 1. [Subtask description]
415 | 2. [Subtask description]
416 | ...
417 | ```
418 | 
419 | **Code Generation Prompt (Legacy Mode)**:
420 | ```
421 | You are a code generation agent. Generate Python code for this subtask.
422 | 
423 | IMPORTANT: Reuse existing functions from the repository whenever possible.
424 | 
425 | Global Context (Target File):
426 | {target_file_content}
427 | 
428 | Similar Functions from Repository:
429 | 1. utils.validators.validate_email(email: str) -> bool
430 |    """Validate email format using regex."""
431 |    def validate_email(email: str) -> bool:
432 |        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
433 |        return re.match(pattern, email) is not None
434 | 
435 | 2. utils.validators.check_email_format(email: str) -> Tuple[bool, str]
436 |    """Check email format and return validation result with message."""
437 |    ...
438 | 
439 | Subtask:
440 | Create a function to validate user email during registration
441 | 
442 | Requirements:
443 | - Reuse validate_email() from utils.validators
444 | - Add additional business logic if needed
445 | - Import necessary modules
446 | - Follow existing code style
447 | - Add type hints and docstrings
448 | 
449 | Generate only the code for this subtask, nothing else.
450 | ```
451 | 
452 | ### C. Sample Output
453 | 
454 | **Successful Generation (Legacy Mode)**:
455 | ```python
456 | from utils.validators import validate_email
457 | from typing import Tuple
458 | 
459 | def validate_user_email(email: str) -> Tuple[bool, str]:
460 |     """
461 |     Validate user email during registration.
462 |     
463 |     Args:
464 |         email: Email address to validate
465 |         
466 |     Returns:
467 |         Tuple of (is_valid, error_message)
468 |     """
469 |     if not email:
470 |         return False, "Email is required"
471 |     
472 |     if not validate_email(email):
473 |         return False, "Invalid email format"
474 |     
475 |     # Additional business logic
476 |     if email.endswith('@temp-mail.com'):
477 |         return False, "Temporary email addresses not allowed"
478 |     
479 |     return True, ""
480 | ```
481 | 
482 | **Validation Result**:
483 | ```
484 | ✓ Namespace Check: PASSED
485 |   - Reuse Score: 1.0 (100%)
486 |   - Called Functions: {validate_email}
487 |   - All functions from repository
488 | 
489 | ✓ Structural Check: PASSED
490 |   - No plagiarism detected
491 |   - Max Similarity: 0.32
492 | 
493 | ✓ Dependency Check: PASSED
494 |   - No breaking changes
495 |   - All imports resolve correctly
496 | 
497 | Code generation successful!
498 | ```
499 | 
500 | ---
501 | 
502 | ## Quick Reference
503 | 
504 | ### CLI Commands
505 | 
506 | ```bash
507 | # Index repository
508 | context-agent index <repo_path>
509 | 
510 | # Generate code
511 | context-agent generate --request "<request>" --target-file <file> --mode <mode>
512 | 
513 | # Update index
514 | context-agent update-index --files <file1> <file2> ...
515 | 
516 | # Search functions
517 | context-agent search --query "<query>" --top-k <k>
518 | 
519 | # Validate code
520 | context-agent validate --code-file <file> --mode <mode>
521 | 
522 | # Show stats
523 | context-agent stats
524 | 
525 | # Clear index
526 | context-agent clear-index
527 | ```
528 | 
529 | ### Configuration Keys
530 | 
531 | ```yaml
532 | repository.path                    # Repository path
533 | indexing.embedder.model           # Embedding model
534 | agent.mode                        # "legacy" or "greenfield"
535 | agent.llm.model                   # LLM model name
536 | metrics.namespace.min_reuse_score # Minimum reuse score (0.0-1.0)
537 | metrics.structural.max_similarity # Maximum structural similarity (0.0-1.0)
538 | metrics.retry.max_retries         # Maximum retry attempts
539 | context.local.max_k               # Maximum similar functions to retrieve
540 | ```
541 | 
542 | ### Key Files
543 | 
544 | ```
545 | chroma_db/                 # Vector database storage
546 | dependency_graph.json      # Dependency graph
547 | index_metadata.json        # Indexing statistics
548 | config.yaml               # Configuration file
549 | agent.log                 # Execution logs
550 | ```
551 | 
552 | ---
553 | 
554 | ## Conclusion
555 | 
556 | This architecture provides a complete blueprint for building a Context-Aware Code Generation Agent that enforces deterministic code reuse. The system combines AST analysis, vector similarity search, and structural verification to prevent code duplication while maintaining flexibility through dual-mode operation.
557 | 
558 | **Key Innovations**:
559 | 1. **Rolling subtask context**: Efficient token usage with ephemeral local context
560 | 2. **Dual-phase verification**: Namespace checking + structural similarity
561 | 3. **Call graph tracking**: Transitive dependency analysis
562 | 4. **Dynamic k-retrieval**: Adaptive context based on relevance
563 | 5. **Cumulative subtask memory**: Prevent intra-session duplication
564 | 
565 | **Next Steps**:
566 | 1. Review this architecture document
567 | 2. Set up development environment
568 | 3. Begin Phase 1 implementation (Foundation)
569 | 4. Follow the implementation order outlined above
570 | 
571 | For questions or clarifications, refer to the API contracts and data flow diagrams in this document.

</file_content>
<environment_details>
# VSCode Visible Files
ARCHITECTURE.md

# VSCode Open Tabs
ARCHITECTURE.md

# Current Time
Current time in ISO 8601 UTC format: 2026-05-16T19:50:28.656Z
User time zone: Asia/Calcutta, UTC+5:30

# Current Cost
$0.00

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>


# Current Workspace Directory (c:/Users/BIT/Desktop/ibmbob) Files
ARCHITECTURE.md
You have not created a todo list yet. Create one with `update_todo_list` if your task is complicated or involves multiple steps.
</environment_details>

---

**Assistant:**

I'll analyze the ARCHITECTURE.md file and start building the system according to the implementation plan. Let me first read the complete architecture document to understand the full scope.

<read_file>
<args>
<file>
<path>ARCHITECTURE.md</path>
</file>
</args>
</read_file>

---

**User:**

[read_file for 'ARCHITECTURE.md'. Reading multiple files at once is more efficient for the LLM. If other files are relevant to your current task, please read them simultaneously.] Result:
<files>
<file><path>ARCHITECTURE.md</path>
<content lines="1-571">
  1 | agent/context_builder.py`)
  2 |    - Build global and local context
  3 |    - Implement cumulative subtask memory
  4 |    - Implement dynamic k-retrieval
  5 | 
  6 | 10. **Implement agent orchestrator** (`agent/agent.py`)
  7 |     - Coordinate subtask execution
  8 |     - Integrate with LLM
  9 |     - Handle mode switching
 10 | 
 11 | ### Phase 4: Metric System (Week 4)
 12 | 
 13 | 11. **Implement namespace checker** (`metrics/namespace_checker.py`)
 14 |     - Parse generated code
 15 |     - Extract function calls
 16 |     - Calculate reuse score
 17 | 
 18 | 12. **Implement structural matcher** (`metrics/structural_matcher.py`)
 19 |     - Extract structural tokens
 20 |     - Calculate Jaccard similarity
 21 |     - Detect violations
 22 | 
 23 | 13. **Implement dependency validator** (`metrics/dependency_validator.py`)
 24 |     - Check call site compatibility
 25 |     - Validate imports
 26 |     - Detect breaking changes
 27 | 
 28 | 14. **Implement explanation generator** (`metrics/explanation_generator.py`)
 29 |     - Generate failure explanations
 30 |     - Suggest fixes
 31 |     - Provide examples
 32 | 
 33 | 15. **Implement metric orchestrator** (`metrics/metric.py`)
 34 |     - Coordinate all validators
 35 |     - Implement retry logic
 36 |     - Generate final results
 37 | 
 38 | ### Phase 5: Integration & Testing (Week 5)
 39 | 
 40 | 16. **End-to-end integration**
 41 |     - Connect all components
 42 |     - Implement CLI interface
 43 |     - Add configuration loading
 44 | 
 45 | 17. **Comprehensive testing**
 46 |     - Unit tests for each component
 47 |     - Integration tests for workflows
 48 |     - Test on real repositories
 49 | 
 50 | 18. **Documentation & Examples**
 51 |     - API documentation
 52 |     - Usage examples
 53 |     - Troubleshooting guide
 54 | 
 55 | ---
 56 | 
 57 | ## Testing Strategy
 58 | 
 59 | ### Unit Tests
 60 | 
 61 | **Test Coverage Requirements**: 80% minimum
 62 | 
 63 | **Key Test Cases**:
 64 | 
 65 | 1. **AST Parser Tests**
 66 |    - Parse valid Python files
 67 |    - Handle syntax errors gracefully
 68 |    - Extract imports correctly (including aliases)
 69 |    - Extract function signatures with type hints
 70 |    - Extract function calls (simple, nested, method calls)
 71 | 
 72 | 2. **Dependency Graph Tests**
 73 |    - Build import graph correctly
 74 |    - Build call graph correctly
 75 |    - Detect circular dependencies
 76 |    - Traverse graph (BFS, DFS)
 77 |    - Handle missing imports
 78 | 
 79 | 3. **Vector DB Tests**
 80 |    - Store and retrieve embeddings
 81 |    - Search with similarity threshold
 82 |    - Handle batch operations
 83 |    - Update existing embeddings
 84 |    - Persist and load from disk
 85 | 
 86 | 4. **Namespace Checker Tests**
 87 |    - Detect function calls correctly
 88 |    - Resolve qualified names
 89 |    - Handle import aliases
 90 |    - Calculate reuse score accurately
 91 |    - Handle edge cases (no calls, all new calls)
 92 | 
 93 | 5. **Structural Matcher Tests**
 94 |    - Extract structural tokens correctly
 95 |    - Calculate Jaccard similarity accurately
 96 |    - Detect plagiarism (high similarity + no reuse)
 97 |    - Avoid false positives (common patterns)
 98 |    - Handle different code styles
 99 | 
100 | 6. **Dependency Validator Tests**
101 |    - Detect breaking changes
102 |    - Validate signature compatibility
103 |    - Check import resolution
104 |    - Handle transitive dependencies
105 | 
106 | ### Integration Tests
107 | 
108 | **Test Scenarios**:
109 | 
110 | 1. **Full Indexing Workflow**
111 |    - Index sample repository
112 |    - Verify all functions indexed
113 |    - Verify dependency graph complete
114 |    - Verify search returns relevant results
115 | 
116 | 2. **Code Generation Workflow (Legacy Mode)**
117 |    - Submit task request
118 |    - Verify subtask decomposition
119 |    - Verify context building
120 |    - Verify code generation
121 |    - Verify metric validation
122 |    - Verify final code quality
123 | 
124 | 3. **Code Generation Workflow (Greenfield Mode)**
125 |    - Submit task request
126 |    - Verify basic validation only
127 |    - Verify no metric enforcement
128 | 
129 | 4. **Retry Logic**
130 |    - Submit task that initially fails validation
131 |    - Verify explanation generation
132 |    - Verify retry with explanation
133 |    - Verify eventual success or max retries
134 | 
135 | 5. **Incremental Index Update**
136 |    - Modify file in repository
137 |    - Update index
138 |    - Verify changes reflected
139 |    - Verify dependent files updated
140 | 
141 | ### Test Repositories
142 | 
143 | **Create 3 test repositories**:
144 | 
145 | 1. **Simple Repository** (10 files, 50 functions)
146 |    - Basic utilities (math, string, file operations)
147 |    - Clear dependencies
148 |    - No circular imports
149 | 
150 | 2. **Medium Repository** (50 files, 200 functions)
151 |    - Multiple modules
152 |    - Some circular dependencies
153 |    - Mix of simple and complex functions
154 | 
155 | 3. **Complex Repository** (100+ files, 500+ functions)
156 |    - Real-world structure
157 |    - Deep dependency chains
158 |    - Various coding patterns
159 | 
160 | ---
161 | 
162 | ## Deployment Guide
163 | 
164 | ### Prerequisites
165 | 
166 | ```bash
167 | # Python 3.9+
168 | python --version
169 | 
170 | # Install dependencies
171 | pip install -r requirements.txt
172 | ```
173 | 
174 | ### Installation
175 | 
176 | ```bash
177 | # Clone repository
178 | git clone https://github.com/yourusername/context-aware-agent.git
179 | cd context-aware-agent
180 | 
181 | # Install package
182 | pip install -e .
183 | 
184 | # Verify installation
185 | context-agent --version
186 | ```
187 | 
188 | ### Configuration
189 | 
190 | ```bash
191 | # Create config file
192 | cp config.example.yaml config.yaml
193 | 
194 | # Edit configuration
195 | vim config.yaml
196 | ```
197 | 
198 | ### Usage
199 | 
200 | **1. Index a repository**:
201 | ```bash
202 | context-agent index /path/to/repository
203 | ```
204 | 
205 | **2. Generate code (Legacy Mode)**:
206 | ```bash
207 | context-agent generate \
208 |   --request "Add email validation to user_service.py" \
209 |   --target-file src/services/user_service.py \
210 |   --mode legacy
211 | ```
212 | 
213 | **3. Generate code (Greenfield Mode)**:
214 | ```bash
215 | context-agent generate \
216 |   --request "Create new payment processing module" \
217 |   --target-file src/services/payment_service.py \
218 |   --mode greenfield
219 | ```
220 | 
221 | **4. Update index after changes**:
222 | ```bash
223 | context-agent update-index \
224 |   --files src/services/user_service.py src/utils/validators.py
225 | ```
226 | 
227 | **5. Query similar functions**:
228 | ```bash
229 | context-agent search \
230 |   --query "email validation" \
231 |   --top-k 5
232 | ```
233 | 
234 | ---
235 | 
236 | ## Performance Considerations
237 | 
238 | ### Indexing Performance
239 | 
240 | **Expected Performance**:
241 | - Small repo (10 files): ~5 seconds
242 | - Medium repo (50 files): ~30 seconds
243 | - Large repo (500 files): ~5 minutes
244 | 
245 | **Optimization Strategies**:
246 | 1. **Parallel processing**: Parse files in parallel using multiprocessing
247 | 2. **Batch embedding**: Embed functions in batches of 32
248 | 3. **Incremental updates**: Only re-index modified files
249 | 4. **Caching**: Cache parsed ASTs for unchanged files
250 | 
251 | ### Query Performance
252 | 
253 | **Expected Performance**:
254 | - Vector search: <100ms for top-5 results
255 | - Dependency graph traversal: <50ms
256 | - Full validation: <500ms
257 | 
258 | **Optimization Strategies**:
259 | 1. **Index optimization**: Use HNSW index in ChromaDB
260 | 2. **Lazy loading**: Load full function code only when needed
261 | 3. **Result caching**: Cache frequent queries
262 | 
263 | ### Memory Usage
264 | 
265 | **Expected Memory**:
266 | - Small repo: ~100MB
267 | - Medium repo: ~500MB
268 | - Large repo: ~2GB
269 | 
270 | **Optimization Strategies**:
271 | 1. **Streaming**: Process files in streaming fashion
272 | 2. **Disk-backed storage**: Use ChromaDB persistence
273 | 3. **Garbage collection**: Explicitly free memory after processing
274 | 
275 | ---
276 | 
277 | ## Extensibility Points
278 | 
279 | ### 1. Custom Embedders
280 | 
281 | ```python
282 | # Implement custom embedder interface
283 | class CustomEmbedder:
284 |     def embed(self, texts: List[str]) -> np.ndarray:
285 |         """Generate embeddings for texts."""
286 |         pass
287 |         
288 | # Register in config
289 | config["indexing"]["embedder"]["custom_class"] = "path.to.CustomEmbedder"
290 | ```
291 | 
292 | ### 2. Custom Validators
293 | 
294 | ```python
295 | # Add custom validation logic
296 | class CustomValidator:
297 |     def validate(self, generated_code: str) -> ValidationResult:
298 |         """Custom validation logic."""
299 |         pass
300 |         
301 | # Register in metric system
302 | metric_validator.add_validator(CustomValidator())
303 | ```
304 | 
305 | ### 3. Custom LLM Providers
306 | 
307 | ```python
308 | # Implement LLM provider interface
309 | class CustomLLMProvider:
310 |     def generate(self, prompt: str, **kwargs) -> str:
311 |         """Generate code using custom LLM."""
312 |         pass
313 |         
314 | # Register in config
315 | config["agent"]["llm"]["custom_provider"] = "path.to.CustomLLMProvider"
316 | ```
317 | 
318 | ### 4. Custom Metrics
319 | 
320 | ```python
321 | # Define custom metric
322 | class CustomMetric:
323 |     def calculate(self, generated_code: str, context: Dict) -> float:
324 |         """Calculate custom metric score."""
325 |         pass
326 |         
327 | # Register in metric system
328 | metric_validator.add_metric("custom_metric", CustomMetric())
329 | ```
330 | 
331 | ---
332 | 
333 | ## Troubleshooting
334 | 
335 | ### Common Issues
336 | 
337 | **1. Indexing fails with "Module not found"**
338 | - **Cause**: Repository has missing dependencies
339 | - **Solution**: Install repository dependencies or exclude problematic files
340 | 
341 | **2. Vector search returns irrelevant results**
342 | - **Cause**: Embeddings not capturing semantic meaning
343 | - **Solution**: Try different embedding model or adjust similarity threshold
344 | 
345 | **3. Validation always fails**
346 | - **Cause**: Thresholds too strict
347 | - **Solution**: Adjust thresholds in config.yaml
348 | 
349 | **4. High memory usage during indexing**
350 | - **Cause**: Large repository with many functions
351 | - **Solution**: Enable streaming mode or increase system memory
352 | 
353 | **5. Slow code generation**
354 | - **Cause**: LLM API rate limits or slow model
355 | - **Solution**: Use faster model or implement caching
356 | 
357 | ---
358 | 
359 | ## Future Enhancements
360 | 
361 | ### Short-term (Next 3 months)
362 | 
363 | 1. **Multi-language support**: Add JavaScript, TypeScript, Java
364 | 2. **IDE integration**: VS Code extension
365 | 3. **Web UI**: Browser-based interface
366 | 4. **Batch processing**: Process multiple files simultaneously
367 | 5. **Performance profiling**: Built-in profiler for optimization
368 | 
369 | ### Medium-term (6 months)
370 | 
371 | 1. **Cross-repository search**: Search across multiple repositories
372 | 2. **Semantic code search**: Natural language queries
373 | 3. **Automated refactoring**: Suggest refactoring opportunities
374 | 4. **Code quality metrics**: Track code quality over time
375 | 5. **Team collaboration**: Multi-user support
376 | 
377 | ### Long-term (1 year)
378 | 
379 | 1. **AI-powered architecture analysis**: Suggest architectural improvements
380 | 2. **Automated testing**: Generate tests for new code
381 | 3. **Documentation generation**: Auto-generate documentation
382 | 4. **Code review automation**: Automated code review comments
383 | 5. **Learning from feedback**: Improve based on user corrections
384 | 
385 | ---
386 | 
387 | ## Appendix
388 | 
389 | ### A. Mathematical Formulas
390 | 
391 | **Reuse Score**:
392 | $$\text{Reuse Score} = \frac{|\text{Called Functions} \cap \text{Repo Functions}|}{|\text{Called Functions}|}$$
393 | 
394 | **Jaccard Similarity**:
395 | $$J(A, B) = \frac{|A \cap B|}{|A \cup B|}$$
396 | 
397 | **Structural Plagiarism Detection**:
398 | $$\text{Plagiarism} = (\text{Structural Sim} \geq 0.85) \land (\text{Namespace Reuse} = 0) \land (\text{Semantic Sim} \geq 0.75)$$
399 | 
400 | ### B. Example Prompts
401 | 
402 | **Subtask Decomposition Prompt**:
403 | ```
404 | You are a task planner. Break down this request into 3-5 isolated subtasks.
405 | 
406 | Request: Add email validation to user registration in user_service.py
407 | 
408 | Each subtask should:
409 | - Be independently executable
410 | - Have clear input/output
411 | - Focus on single responsibility
412 | 
413 | Output format:
414 | 1. [Subtask description]
415 | 2. [Subtask description]
416 | ...
417 | ```
418 | 
419 | **Code Generation Prompt (Legacy Mode)**:
420 | ```
421 | You are a code generation agent. Generate Python code for this subtask.
422 | 
423 | IMPORTANT: Reuse existing functions from the repository whenever possible.
424 | 
425 | Global Context (Target File):
426 | {target_file_content}
427 | 
428 | Similar Functions from Repository:
429 | 1. utils.validators.validate_email(email: str) -> bool
430 |    """Validate email format using regex."""
431 |    def validate_email(email: str) -> bool:
432 |        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
433 |        return re.match(pattern, email) is not None
434 | 
435 | 2. utils.validators.check_email_format(email: str) -> Tuple[bool, str]
436 |    """Check email format and return validation result with message."""
437 |    ...
438 | 
439 | Subtask:
440 | Create a function to validate user email during registration
441 | 
442 | Requirements:
443 | - Reuse validate_email() from utils.validators
444 | - Add additional business logic if needed
445 | - Import necessary modules
446 | - Follow existing code style
447 | - Add type hints and docstrings
448 | 
449 | Generate only the code for this subtask, nothing else.
450 | ```
451 | 
452 | ### C. Sample Output
453 | 
454 | **Successful Generation (Legacy Mode)**:
455 | ```python
456 | from utils.validators import validate_email
457 | from typing import Tuple
458 | 
459 | def validate_user_email(email: str) -> Tuple[bool, str]:
460 |     """
461 |     Validate user email during registration.
462 |     
463 |     Args:
464 |         email: Email address to validate
465 |         
466 |     Returns:
467 |         Tuple of (is_valid, error_message)
468 |     """
469 |     if not email:
470 |         return False, "Email is required"
471 |     
472 |     if not validate_email(email):
473 |         return False, "Invalid email format"
474 |     
475 |     # Additional business logic
476 |     if email.endswith('@temp-mail.com'):
477 |         return False, "Temporary email addresses not allowed"
478 |     
479 |     return True, ""
480 | ```
481 | 
482 | **Validation Result**:
483 | ```
484 | ✓ Namespace Check: PASSED
485 |   - Reuse Score: 1.0 (100%)
486 |   - Called Functions: {validate_email}
487 |   - All functions from repository
488 | 
489 | ✓ Structural Check: PASSED
490 |   - No plagiarism detected
491 |   - Max Similarity: 0.32
492 | 
493 | ✓ Dependency Check: PASSED
494 |   - No breaking changes
495 |   - All imports resolve correctly
496 | 
497 | Code generation successful!
498 | ```
499 | 
500 | ---
501 | 
502 | ## Quick Reference
503 | 
504 | ### CLI Commands
505 | 
506 | ```bash
507 | # Index repository
508 | context-agent index <repo_path>
509 | 
510 | # Generate code
511 | context-agent generate --request "<request>" --target-file <file> --mode <mode>
512 | 
513 | # Update index
514 | context-agent update-index --files <file1> <file2> ...
515 | 
516 | # Search functions
517 | context-agent search --query "<query>" --top-k <k>
518 | 
519 | # Validate code
520 | context-agent validate --code-file <file> --mode <mode>
521 | 
522 | # Show stats
523 | context-agent stats
524 | 
525 | # Clear index
526 | context-agent clear-index
527 | ```
528 | 
529 | ### Configuration Keys
530 | 
531 | ```yaml
532 | repository.path                    # Repository path
533 | indexing.embedder.model           # Embedding model
534 | agent.mode                        # "legacy" or "greenfield"
535 | agent.llm.model                   # LLM model name
536 | metrics.namespace.min_reuse_score # Minimum reuse score (0.0-1.0)
537 | metrics.structural.max_similarity # Maximum structural similarity (0.0-1.0)
538 | metrics.retry.max_retries         # Maximum retry attempts
539 | context.local.max_k               # Maximum similar functions to retrieve
540 | ```
541 | 
542 | ### Key Files
543 | 
544 | ```
545 | chroma_db/                 # Vector database storage
546 | dependency_graph.json      # Dependency graph
547 | index_metadata.json        # Indexing statistics
548 | config.yaml               # Configuration file
549 | agent.log                 # Execution logs
550 | ```
551 | 
552 | ---
553 | 
554 | ## Conclusion
555 | 
556 | This architecture provides a complete blueprint for building a Context-Aware Code Generation Agent that enforces deterministic code reuse. The system combines AST analysis, vector similarity search, and structural verification to prevent code duplication while maintaining flexibility through dual-mode operation.
557 | 
558 | **Key Innovations**:
559 | 1. **Rolling subtask context**: Efficient token usage with ephemeral local context
560 | 2. **Dual-phase verification**: Namespace checking + structural similarity
561 | 3. **Call graph tracking**: Transitive dependency analysis
562 | 4. **Dynamic k-retrieval**: Adaptive context based on relevance
563 | 5. **Cumulative subtask memory**: Prevent intra-session duplication
564 | 
565 | **Next Steps**:
566 | 1. Review this architecture document
567 | 2. Set up development environment
568 | 3. Begin Phase 1 implementation (Foundation)
569 | 4. Follow the implementation order outlined above
570 | 
571 | For questions or clarifications, refer to the API contracts and data flow diagrams in this document.
</content>
</file>
</files>
<environment_details>
# VSCode Visible Files
ARCHITECTURE.md

# VSCode Open Tabs
ARCHITECTURE.md

# Current Time
Current time in ISO 8601 UTC format: 2026-05-16T19:50:36.290Z
User time zone: Asia/Calcutta, UTC+5:30

# Current Cost
$0.02

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
You have not created a todo list yet. Create one with `update_todo_list` if your task is complicated or involves multiple steps.
</environment_details>

---

**Assistant:**

I can see this is a partial ARCHITECTURE.md file (starting from line 1 which appears to be mid-sentence). Let me check if there are other related files in the workspace to get the complete picture.

<list_files>
<path>.</path>
<recursive>true</recursive>
</list_files>

