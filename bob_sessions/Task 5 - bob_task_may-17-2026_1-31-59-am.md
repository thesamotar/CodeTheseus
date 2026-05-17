**User:**

<task>
Create the complete ARCHITECTURE.md file for the Context-Aware Code Generation Agent project. The file should contain:

1. Executive Summary
2. System Architecture Overview with diagram
3. Phase 1: Offline Indexing Engine (AST Parser, Dependency Graph, Vector DB, Indexer)
4. Phase 2: Task Planner & Agent Orchestration (Subtask Decomposer, Context Builder, Agent)
5. Phase 3: Metric Validation System (Namespace Checker, Structural Matcher, Dependency Validator, Explanation Generator)
6. Mode System (Legacy vs Greenfield)
7. Data Flow Diagrams
8. API Contracts and Data Models
9. Configuration System (config.yaml example)
10. Implementation Order (5-week plan)
11. Testing Strategy
12. Deployment Guide
13. Performance Considerations
14. Extensibility Points
15. Troubleshooting
16. Future Enhancements
17. Appendix (formulas, prompts, examples)
18. Quick Reference
19. Conclusion

The current ARCHITECTURE.md file only has the second half (starting from line 1 with "agent/context_builder.py"). Delete it and create the complete file from scratch with ALL sections.

Key technical decisions to include:
- Embedding Model: Jina Code Embeddings V2
- Vector DB: ChromaDB
- Dynamic k-retrieval: min_similarity=0.7, max_k=5
- Validation thresholds: 40% reuse score, 85% structural similarity
- Cumulative subtask memory
- Call graph tracking (not just imports)
- Structural plagiarism detection with Jaccard similarity
- Explanation layer for failed validations

Make it comprehensive and production-ready - this will be the reference document for implementing the entire system.
</task>
<environment_details>
# VSCode Visible Files
ARCHITECTURE.md

# VSCode Open Tabs
ARCHITECTURE.md

# Current Time
Current time in ISO 8601 UTC format: 2026-05-16T19:56:35.324Z
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

I'll create a comprehensive ARCHITECTURE.md file for the Context-Aware Code Generation Agent project. Let me start by reading the current file to understand what exists.

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
Current time in ISO 8601 UTC format: 2026-05-16T19:56:45.417Z
User time zone: Asia/Calcutta, UTC+5:30

# Current Cost
$0.01

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

Now I'll create a comprehensive ARCHITECTURE.md file from scratch with all the required sections. Let me create a todo list first to organize this complex task.

<update_todo_list>
<todos>
[ ] Create complete ARCHITECTURE.md with all 19 sections
[ ] Include technical specifications (Jina embeddings, ChromaDB, thresholds)
[ ] Add system diagrams and data flow
[ ] Include API contracts and data models
[ ] Add configuration examples and implementation plan
[ ] Verify completeness and production-readiness
</todos>
</update_todo_list>

---

**User:**

[update_todo_list] Result:
Todo list updated successfully.
<environment_details>
# VSCode Visible Files
ARCHITECTURE.md

# VSCode Open Tabs
ARCHITECTURE.md

# Current Time
Current time in ISO 8601 UTC format: 2026-05-16T19:56:52.228Z
User time zone: Asia/Calcutta, UTC+5:30

# Current Cost
$0.03

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
====

REMINDERS

Below is your current list of reminders for this task. Keep them updated as you progress.

| # | Content | Status |
|---|---------|--------|
| 1 | Create complete ARCHITECTURE.md with all 19 sections | Pending |
| 2 | Include technical specifications (Jina embeddings, ChromaDB, thresholds) | Pending |
| 3 | Add system diagrams and data flow | Pending |
| 4 | Include API contracts and data models | Pending |
| 5 | Add configuration examples and implementation plan | Pending |
| 6 | Verify completeness and production-readiness | Pending |


IMPORTANT: When task status changes, remember to call the `update_todo_list` tool to update your progress.

</environment_details>

---

**Assistant:**

Now I'll create the complete ARCHITECTURE.md file with all 19 sections as specified.

<write_to_file>
<path>ARCHITECTURE.md</path>
<content>
# Context-Aware Code Generation Agent - Architecture Document

**Version**: 1.0  
**Last Updated**: May 16, 2026  
**Status**: Production-Ready Blueprint

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [System Architecture Overview](#2-system-architecture-overview)
3. [Phase 1: Offline Indexing Engine](#3-phase-1-offline-indexing-engine)
4. [Phase 2: Task Planner & Agent Orchestration](#4-phase-2-task-planner--agent-orchestration)
5. [Phase 3: Metric Validation System](#5-phase-3-metric-validation-system)
6. [Mode System](#6-mode-system)
7. [Data Flow Diagrams](#7-data-flow-diagrams)
8. [API Contracts and Data Models](#8-api-contracts-and-data-models)
9. [Configuration System](#9-configuration-system)
10. [Implementation Order](#10-implementation-order)
11. [Testing Strategy](#11-testing-strategy)
12. [Deployment Guide](#12-deployment-guide)
13. [Performance Considerations](#13-performance-considerations)
14. [Extensibility Points](#14-extensibility-points)
15. [Troubleshooting](#15-troubleshooting)
16. [Future Enhancements](#16-future-enhancements)
17. [Appendix](#17-appendix)
18. [Quick Reference](#18-quick-reference)
19. [Conclusion](#19-conclusion)

---

## 1. Executive Summary

### 1.1 Problem Statement

Modern code generation agents suffer from three critical issues:
1. **Code duplication**: Generated code reinvents existing functionality
2. **Context blindness**: Agents lack awareness of repository structure and dependencies
3. **Validation gaps**: No systematic verification of code reuse and structural integrity

### 1.2 Solution Overview

The **Context-Aware Code Generation Agent** is a production-ready system that enforces deterministic code reuse through:

- **Offline Indexing**: AST-based parsing, dependency graph construction, and semantic embeddings
- **Intelligent Context Building**: Dynamic retrieval of relevant functions with cumulative subtask memory
- **Multi-Metric Validation**: Namespace checking, structural similarity analysis, and dependency validation
- **Dual-Mode Operation**: Legacy mode (strict reuse) vs. Greenfield mode (flexible creation)

### 1.3 Key Innovations

1. **Rolling Subtask Context**: Ephemeral local context that resets per subtask, preventing token bloat
2. **Call Graph Tracking**: Transitive dependency analysis beyond simple imports
3. **Structural Plagiarism Detection**: Jaccard similarity to catch reimplementation patterns
4. **Dynamic k-Retrieval**: Adaptive context based on similarity thresholds (min_similarity=0.7, max_k=5)
5. **Explanation Layer**: Human-readable failure explanations with actionable suggestions

### 1.4 Technical Stack

| Component | Technology | Rationale |
|-----------|-----------|-----------|
| **Embedding Model** | Jina Code Embeddings V2 | Optimized for code semantics, 768-dim vectors |
| **Vector Database** | ChromaDB | Lightweight, persistent, HNSW indexing |
| **AST Parser** | Python `ast` module | Native, reliable, type-aware |
| **Dependency Analysis** | NetworkX | Graph algorithms, cycle detection |
| **LLM Integration** | OpenAI API (configurable) | Industry standard, extensible |

### 1.5 Success Metrics

- **Reuse Score**: ≥40% of function calls must reference existing repository functions
- **Structural Similarity**: <85% Jaccard similarity to prevent plagiarism
- **Dependency Validation**: 100% import resolution and signature compatibility
- **Performance**: <500ms validation time, <5min indexing for 500-file repos

---

## 2. System Architecture Overview

### 2.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     USER REQUEST                                 │
│  "Add email validation to user_service.py"                      │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                   TASK PLANNER                                   │
│  • Decompose into subtasks                                       │
│  • Determine execution order                                     │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                 AGENT ORCHESTRATOR                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │   Subtask 1  │→ │   Subtask 2  │→ │   Subtask 3  │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
│         │                  │                  │                  │
│         ▼                  ▼                  ▼                  │
│  ┌──────────────────────────────────────────────────┐          │
│  │          CONTEXT BUILDER                          │          │
│  │  • Global Context (target file)                   │          │
│  │  • Local Context (similar functions)              │          │
│  │  • Cumulative Memory (previous subtasks)          │          │
│  └──────────────────────────────────────────────────┘          │
│         │                                                         │
│         ▼                                                         │
│  ┌──────────────────────────────────────────────────┐          │
│  │          LLM CODE GENERATION                      │          │
│  │  • Generate code with context                     │          │
│  │  • Enforce reuse in prompt                        │          │
│  └──────────────────────────────────────────────────┘          │
│         │                                                         │
│         ▼                                                         │
│  ┌──────────────────────────────────────────────────┐          │
│  │       METRIC VALIDATION SYSTEM                    │          │
│  │  ┌────────────┐ ┌────────────┐ ┌────────────┐   │          │
│  │  │ Namespace  │ │ Structural │ │ Dependency │   │          │
│  │  │  Checker   │ │  Matcher   │ │ Validator  │   │          │
│  │  └────────────┘ └────────────┘ └────────────┘   │          │
│  └──────────────────────────────────────────────────┘          │
│         │                                                         │
│         ▼                                                         │
│  ┌──────────────────────────────────────────────────┐          │
│  │  PASS? → Accumulate → Next Subtask               │          │
│  │  FAIL? → Explain → Retry (max 3x)                │          │
│  └──────────────────────────────────────────────────┘          │
└─────────────────────────────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                   FINAL CODE OUTPUT                              │
│  • Merged subtask results                                        │
│  • Validation report                                             │
│  • Reuse statistics                                              │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│              OFFLINE INDEXING ENGINE (Pre-computed)              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │  AST Parser  │→ │ Dependency   │→ │  Vector DB   │         │
│  │              │  │    Graph     │  │  (ChromaDB)  │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
│         ↑                  ↑                  ↑                  │
│         └──────────────────┴──────────────────┘                 │
│                    Repository Files                              │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 Component Interaction Flow

```
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│   User   │────▶│  Planner │────▶│  Agent   │────▶│ Validator│
└──────────┘     └──────────┘     └──────────┘     └──────────┘
                       │                │                │
                       │                ▼                │
                       │         ┌──────────┐           │
                       │         │ Context  │           │
                       │         │ Builder  │           │
                       │         └──────────┘           │
                       │                │                │
                       │                ▼                │
                       │         ┌──────────┐           │
                       └────────▶│ Vector   │◀──────────┘
                                 │   DB     │
                                 └──────────┘
                                       │
                                       ▼
                                 ┌──────────┐
                                 │Dependency│
                                 │  Graph   │
                                 └──────────┘
```

### 2.3 Directory Structure

```
context-aware-agent/
├── indexer/
│   ├── __init__.py
│   ├── ast_parser.py          # AST parsing and extraction
│   ├── dependency_graph.py    # Import and call graph construction
│   ├── vector_db.py           # ChromaDB wrapper
│   └── indexer.py             # Main indexing orchestrator
├── planner/
│   ├── __init__.py
│   └── task_planner.py        # Subtask decomposition
├── agent/
│   ├── __init__.py
│   ├── context_builder.py     # Context assembly
│   └── agent.py               # Agent orchestration
├── metrics/
│   ├── __init__.py
│   ├── namespace_checker.py   # Function call analysis
│   ├── structural_matcher.py  # Jaccard similarity
│   ├── dependency_validator.py # Signature compatibility
│   ├── explanation_generator.py # Failure explanations
│   └── metric.py              # Validation orchestrator
├── config/
│   ├── __init__.py
│   └── config.yaml            # System configuration
├── cli/
│   ├── __init__.py
│   └── main.py                # CLI interface
├── tests/
│   ├── unit/
│   ├── integration/
│   └── fixtures/
├── docs/
│   ├── ARCHITECTURE.md        # This document
│   ├── API.md
│   └── EXAMPLES.md
├── requirements.txt
├── setup.py
└── README.md
```

---

## 3. Phase 1: Offline Indexing Engine

### 3.1 Overview

The indexing engine pre-processes the repository to create:
1. **Function metadata**: Signatures, docstrings, imports, calls
2. **Dependency graph**: Import relationships and call chains
3. **Vector embeddings**: Semantic representations for similarity search

### 3.2 AST Parser (`indexer/ast_parser.py`)

**Purpose**: Extract structured information from Python source files.

**Key Features**:
- Parse Python files into AST
- Extract function definitions with type hints
- Identify imports (including aliases: `import X as Y`, `from X import Y as Z`)
- Extract function calls (simple, nested, method calls)
- Handle decorators and class methods

**Data Extracted**:

```python
@dataclass
class FunctionMetadata:
    name: str                    # Function name
    qualified_name: str          # module.ClassName.function_name
    signature: str               # Full signature with type hints
    docstring: Optional[str]     # Docstring if present
    body: str                    # Function body code
    imports: List[str]           # Direct imports used
    calls: List[str]             # Function calls made
    line_start: int              # Starting line number
    line_end: int                # Ending line number
    file_path: str               # Source file path
    is_method: bool              # True if class method
    decorators: List[str]        # Applied decorators
```

**Implementation Details**:

```python
class ASTParser:
    def parse_file(self, file_path: str) -> List[FunctionMetadata]:
        """Parse a Python file and extract function metadata."""
        with open(file_path, 'r') as f:
            source = f.read()
        
        tree = ast.parse(source)
        functions = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                metadata = self._extract_function_metadata(node, file_path)
                functions.append(metadata)
        
        return functions
    
    def _extract_function_metadata(self, node: ast.FunctionDef, 
                                   file_path: str) -> FunctionMetadata:
        """Extract metadata from function AST node."""
        # Extract signature
        signature = self._build_signature(node)
        
        # Extract docstring
        docstring = ast.get_docstring(node)
        
        # Extract imports
        imports = self._extract_imports(node)
        
        # Extract function calls
        calls = self._extract_calls(node)
        
        # Extract body
        body = ast.unparse(node)
        
        return FunctionMetadata(
            name=node.name,
            qualified_name=self._build_qualified_name(node, file_path),
            signature=signature,
            docstring=docstring,
            body=body,
            imports=imports,
            calls=calls,
            line_start=node.lineno,
            line_end=node.end_lineno,
            file_path=file_path,
            is_method=self._is_method(node),
            decorators=[d.id for d in node.decorator_list if isinstance(d, ast.Name)]
        )
    
    def _extract_calls(self, node: ast.FunctionDef) -> List[str]:
        """Extract all function calls from function body."""
        calls = []
        for child in ast.walk(node):
            if isinstance(child, ast.Call):
                call_name = self._resolve_call_name(child)
                if call_name:
                    calls.append(call_name)
        return list(set(calls))  # Deduplicate
    
    def _resolve_call_name(self, call_node: ast.Call) -> Optional[str]:
        """Resolve function call to qualified name."""
        if isinstance(call_node.func, ast.Name):
            return call_node.func.id
        elif isinstance(call_node.func, ast.Attribute):
            # Handle method calls: obj.method()
            return self._resolve_attribute_chain(call_node.func)
        return None
```

**Edge Cases Handled**:
- Nested function definitions
- Lambda functions (excluded from indexing)
- Async functions
- Class methods and static methods
- Import aliases resolution
- Relative imports

### 3.3 Dependency Graph (`indexer/dependency_graph.py`)

**Purpose**: Build import and call graphs for dependency analysis.

**Graph Types**:

1. **Import Graph**: Module-level dependencies
   - Nodes: Python modules
   - Edges: Import relationships
   - Used for: Detecting circular imports, transitive dependencies

2. **Call Graph**: Function-level dependencies
   - Nodes: Functions (qualified names)
   - Edges: Function calls
   - Used for: Reuse validation, impact analysis

**Data Structure**:

```python
@dataclass
class DependencyGraph:
    import_graph: nx.DiGraph      # Module dependencies
    call_graph: nx.DiGraph        # Function call dependencies
    module_to_functions: Dict[str, List[str]]  # Module → Functions
    function_to_module: Dict[str, str]         # Function → Module
    
    def add_import(self, from_module: str, to_module: str):
        """Add import edge."""
        self.import_graph.add_edge(from_module, to_module)
    
    def add_call(self, caller: str, callee: str):
        """Add function call edge."""
        self.call_graph.add_edge(caller, callee)
    
    def get_transitive_dependencies(self, function: str) -> Set[str]:
        """Get all functions transitively called by this function."""
        if function not in self.call_graph:
            return set()
        return set(nx.descendants(self.call_graph, function))
    
    def detect_circular_imports(self) -> List[List[str]]:
        """Detect circular import chains."""
        try:
            cycles = list(nx.simple_cycles(self.import_graph))
            return cycles
        except nx.NetworkXNoCycle:
            return []
    
    def get_call_chain(self, from_func: str, to_func: str) -> Optional[List[str]]:
        """Find call chain between two functions."""
        try:
            path = nx.shortest_path(self.call_graph, from_func, to_func)
            return path
        except (nx.NetworkXNoPath, nx.NodeNotFound):
            return None
```

**Implementation**:

```python
class DependencyGraphBuilder:
    def build(self, functions: List[FunctionMetadata]) -> DependencyGraph:
        """Build dependency graph from function metadata."""
        graph = DependencyGraph(
            import_graph=nx.DiGraph(),
            call_graph=nx.DiGraph(),
            module_to_functions={},
            function_to_module={}
        )
        
        # Build module-to-function mappings
        for func in functions:
            module = self._extract_module(func.file_path)
            graph.module_to_functions.setdefault(module, []).append(func.qualified_name)
            graph.function_to_module[func.qualified_name] = module
        
        # Build import graph
        for func in functions:
            module = self._extract_module(func.file_path)
            for imp in func.imports:
                imported_module = self._resolve_import(imp)
                graph.add_import(module, imported_module)
        
        # Build call graph
        for func in functions:
            for call in func.calls:
                resolved_call = self._resolve_call(call, func, graph)
                if resolved_call:
                    graph.add_call(func.qualified_name, resolved_call)
        
        return graph
    
    def _resolve_call(self, call: str, caller: FunctionMetadata, 
                     graph: DependencyGraph) -> Optional[str]:
        """Resolve function call to qualified name."""
        # Check if it's a direct call to a function in the same module
        caller_module = self._extract_module(caller.file_path)
        candidate = f"{caller_module}.{call}"
        if candidate in graph.function_to_module:
            return candidate
        
        # Check imports
        for imp in caller.imports:
            if call in imp:
                # Resolve through import
                return self._resolve_through_import(call, imp, graph)
        
        return None
```

### 3.4 Vector Database (`indexer/vector_db.py`)

**Purpose**: Store and retrieve function embeddings for semantic search.

**Technology**: ChromaDB with HNSW indexing

**Configuration**:
- **Embedding Model**: Jina Code Embeddings V2 (768 dimensions)
- **Distance Metric**: Cosine similarity
- **Index Type**: HNSW (Hierarchical Navigable Small World)
- **Persistence**: Disk-backed storage

**Data Model**:

```python
@dataclass
class VectorDBEntry:
    id: str                      # Unique identifier (qualified_name)
    embedding: np.ndarray        # 768-dim vector
    metadata: Dict[str, Any]     # Function metadata
    
    # Metadata fields:
    # - qualified_name: str
    # - signature: str
    # - docstring: str
    # - file_path: str
    # - line_start: int
    # - line_end: int
    # - imports: List[str]
    # - calls: List[str]
```

**Implementation**:

```python
class VectorDB:
    def __init__(self, persist_directory: str = "./chroma_db"):
        """Initialize ChromaDB client."""
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection = self.client.get_or_create_collection(
            name="functions",
            metadata={"hnsw:space": "cosine"}
        )
        self.embedder = self._load_embedder()
    
    def _load_embedder(self):
        """Load Jina Code Embeddings V2."""
        from sentence_transformers import SentenceTransformer
        return SentenceTransformer('jinaai/jina-embeddings-v2-base-code')
    
    def add_functions(self, functions: List[FunctionMetadata]):
        """Add functions to vector database."""
        # Prepare texts for embedding
        texts = [self._prepare_text(f) for f in functions]
        
        # Generate embeddings in batches
        embeddings = self.embedder.encode(texts, batch_size=32)
        
        # Prepare metadata
        metadatas = [self._prepare_metadata(f) for f in functions]
        
        # Add to collection
        self.collection.add(
            ids=[f.qualified_name for f in functions],
            embeddings=embeddings.tolist(),
            metadatas=metadatas,
            documents=texts
        )
    
    def _prepare_text(self, func: FunctionMetadata) -> str:
        """Prepare text for embedding."""
        parts = [
            f"Function: {func.name}",
            f"Signature: {func.signature}"
        ]
        if func.docstring:
            parts.append(f"Description: {func.docstring}")
        return "\n".join(parts)
    
    def search(self, query: str, k: int = 5, 
               min_similarity: float = 0.7) -> List[Dict]:
        """Search for similar functions."""
        # Embed query
        query_embedding = self.embedder.encode([query])[0]
        
        # Search with larger k to filter by similarity
        results = self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=k * 2  # Retrieve more to filter
        )
        
        # Filter by minimum similarity
        filtered_results = []
        for i, distance in enumerate(results['distances'][0]):
            similarity = 1 - distance  # Convert distance to similarity
            if similarity >= min_similarity:
                filtered_results.append({
                    'id': results['ids'][0][i],
                    'metadata': results['metadatas'][0][i],
                    'similarity': similarity,
                    'document': results['documents'][0][i]
                })
        
        # Return top k after filtering
        return sorted(filtered_results, 
                     key=lambda x: x['similarity'], 
                     reverse=True)[:k]
    
    def get_by_id(self, function_id: str) -> Optional[Dict]:
        """Retrieve function by qualified name."""
        results = self.collection.get(ids=[function_id])
        if results['ids']:
            return {
                'id': results['ids'][0],
                'metadata': results['metadatas'][0],
                'document': results['documents'][0]
            }
        return None
```

### 3.5 Indexer Orchestrator (`indexer/indexer.py`)

**Purpose**: Coordinate the indexing pipeline.

**Workflow**:

```python
class Indexer:
    def __init__(self, config: Dict):
        self.config = config
        self.parser = ASTParser()
        self.graph_builder = DependencyGraphBuilder()
        self.vector_db = VectorDB(config['vector_db']['persist_directory'])
    
    def index_repository(self, repo_path: str) -> IndexResult:
        """Index entire repository."""
        print(f"Indexing repository: {repo_path}")
        
        # Step 1: Discover Python files
        python_files = self._discover_files(repo_path)
        print(f"Found {len(python_files)} Python files")
        
        # Step 2: Parse files (parallel)
        all_functions = []
        with multiprocessing.Pool() as pool:
            results = pool.map(self.parser.parse_file, python_files)
            for functions in results:
                all_functions.extend(functions)
        print(f"Extracted {len(all_functions)} functions")
        
        # Step 3: Build dependency graph
        dependency_graph = self.graph_builder.build(all_functions)
        print(f"Built dependency graph: {len(dependency_graph.call_graph.nodes)} nodes")
        
        # Step 4: Store in vector database
        self.vector_db.add_functions(all_functions)
        print(f"Stored embeddings in vector database")
        
        # Step 5: Persist dependency graph
        self._save_dependency_graph(dependency_graph)
        
        # Step 6: Generate statistics
        stats = self._generate_stats(all_functions, dependency_graph)
        
        return IndexResult(
            total_files=len(python_files),
            total_functions=len(all_functions),
            dependency_graph=dependency_graph,
            stats=stats
        )
    
    def update_index(self, modified_files: List[str]):
        """Incrementally update index for modified files."""
        # Parse modified files
        new_functions = []
        for file_path in modified_files:
            functions = self.parser.parse_file(file_path)
            new_functions.extend(functions)
        
        # Remove old entries
        old_ids = [f.qualified_name for f in new_functions]
        self.vector_db.collection.delete(ids=old_ids)
        
        # Add new entries
        self.vector_db.add_functions(new_functions)
        
        # Rebuild dependency graph (full rebuild for simplicity)
        # In production, implement incremental graph updates
        all_functions = self._load_all_functions()
        dependency_graph = self.graph_builder.build(all_functions)
        self._save_dependency_graph(dependency_graph)
```

---

## 4. Phase 2: Task Planner & Agent Orchestration

### 4.1 Task Planner (`planner/task_planner.py`)

**Purpose**: Decompose user requests into isolated, executable subtasks.

**Decomposition Strategy**:
- Break complex tasks into 3-5 subtasks
- Each subtask should be independently executable
- Subtasks should have clear input/output boundaries
- Maintain logical execution order

**Implementation**:

```python
class TaskPlanner:
    def __init__(self, llm_client):
        self.llm = llm_client
    
    def decompose(self, request: str, target_file: str) -> List[Subtask]:
        """Decompose request into subtasks."""
        prompt = self._build_decomposition_prompt(request, target_file)
        response = self.llm.generate(prompt)
        subtasks = self._parse_subtasks(response)
        return subtasks
    
    def _build_decomposition_prompt(self, request: str, target_file: str) -> str:
        return f"""You are a task planning expert. Break down this code generation request into 3-5 isolated subtasks.

Request: {request}
Target File: {target_file}

Requirements:
1. Each subtask must be independently executable
2. Subtasks should have clear input/output
3. Focus on single responsibility per subtask
4. Maintain logical execution order
5. Be specific about what each subtask should accomplish

Output format (one per line):
1. [Subtask description]
2. [Subtask description]
...

Subtasks:"""
    
    def _parse_subtasks(self, response: str) -> List[Subtask]:
        """Parse LLM response into subtask objects."""
        lines = response.strip().split('\n')
        subtasks = []
        for i, line in enumerate(lines):
            # Remove numbering
            description = re.sub(r'^\d+\.\s*', '', line).strip()
            if description:
                subtasks.append(Subtask(
                    id=i + 1,
                    description=description,
                    status='pending'
                ))
        return subtasks

@dataclass
class Subtask:
    id: int
    description: str
    status: str  # 'pending', 'in_progress', 'completed', 'failed'
    generated_code: Optional[str] = None
    validation_result: Optional[Dict] = None
```

### 4.2 Context Builder (`agent/context_builder.py`)

**Purpose**: Assemble relevant context for each subtask.

**Context Types**:

1. **Global Context**: Target file content (persistent across subtasks)
2. **Local Context**: Similar functions from repository (ephemeral, resets per subtask)
3. **Cumulative Memory**: Previously generated subtask code (accumulates)

**Dynamic k-Retrieval**:
- **min_similarity**: 0.7 (minimum cosine similarity threshold)
- **max_k**: 5 (maximum functions to retrieve)
- Adaptive: Returns fewer functions if similarity drops below threshold

**Implementation**:

```python
class ContextBuilder:
    def __init__(self, vector_db: VectorDB, dependency_graph: DependencyGraph):
        self.vector_db = vector_db
        self.dependency_graph = dependency_graph
        self.cumulative_memory = []  # Accumulates across subtasks
    
    def build_context(self, subtask: Subtask, target_file: str, 
                     config: Dict) -> Context:
        """Build context for subtask execution."""
        # Global context (persistent)
        global_context = self._load_target_file(target_file)
        
        # Local context (ephemeral, dynamic k-retrieval)
        local_context = self._retrieve_similar_functions(
            query=subtask.description,
            min_similarity=config['context']['local']['min_similarity'],
            max_k=config['context']['local']['max_k']
        )
        
        # Cumulative memory (accumulated)
        cumulative_context = self._format_cumulative_memory()
        
        return Context(
            global_context=global_context,
            local_context=local_context,
            cumulative_context=cumulative_context,
            subtask=subtask
        )
    
    def _retrieve_similar_functions(self, query: str, 
                                    min_similarity: float, 
                                    max_k: int) -> List[FunctionContext]:
        """Retrieve similar functions with dynamic k."""
        results = self.vector_db.search(
            query=query,
            k=max_k,
            min_similarity=min_similarity
        )
        
        # Format results
        function_contexts = []
        for result in results:
            # Load full function code
            func_id = result['id']
            func_data = self.vector_db.get_by_id(func_id)
            
            # Get transitive dependencies
            dependencies = self.dependency_graph.get_transitive_dependencies(func_id)
            
            function_contexts.append(FunctionContext(
                qualified_name=func_id,
                signature=func_data['metadata']['signature'],
                docstring=func_data['metadata'].get('docstring', ''),
                body=func_data['metadata'].get('body', ''),
                similarity=result['similarity'],
                dependencies=list(dependencies)[:3]  # Top 3 dependencies
            ))
        
        return function_contexts
    
    def accumulate_subtask_result(self, subtask: Subtask, code: str):
        """Add subtask result to cumulative memory."""
        self.cumulative_memory.append({
            'subtask_id': subtask.id,
            'description': subtask.description,
            'code': code
        })
    
    def _format_cumulative_memory(self) -> str:
        """Format cumulative memory for prompt."""
        if not self.cumulative_memory:
            return ""
        
        lines = ["Previously generated code in this session:"]
        for entry in self.cumulative_memory:
            lines.append(f"\n## Subtask {entry['subtask_id']}: {entry['description']}")
            lines.append(f"```python\n{entry['code']}\n```")
        
        return "\n".join(lines)

@dataclass
class Context:
    global_context: str           # Target file content
    local_context: List[FunctionContext]  # Similar functions
    cumulative_context: str       # Previous subtasks
    subtask: Subtask

@dataclass
class FunctionContext:
    qualified_name: str
    signature: str
    docstring: str
    body: str
    similarity: float
    dependencies: List[str]
```

### 4.3 Agent Orchestrator (`agent/agent.py`)

**Purpose**: Coordinate subtask execution, code generation, and validation.

**Workflow**:

```python
class Agent:
    def __init__(self, config: Dict):
        self.config = config
        self.llm = self._init_llm(config['agent']['llm'])
        self.context_builder = ContextBuilder(
            vector_db=VectorDB(config['vector_db']['persist_directory']),
            dependency_graph=self._load_dependency_graph()
        )
        self.validator = MetricValidator(config['metrics'])
        self.mode = config['agent']['mode']  # 'legacy' or 'greenfield'
    
    def execute(self, request: str, target_file: str) -> AgentResult:
        """Execute code generation request."""
        # Step 1: Decompose into subtasks
        planner = TaskPlanner(self.llm)
        subtasks = planner.decompose(request, target_file)
        print(f"Decomposed into {len(subtasks)} subtasks")
        
        # Step 2: Execute subtasks sequentially
        all_code = []
        for subtask in subtasks:
            print(f"\nExecuting subtask {subtask.id}: {subtask.description}")
            
            # Build context
            context = self.context_builder.build_context(
                subtask, target_file, self.config
            )
            
            # Generate code with retry logic
            code, validation_result = self._generate_with_retry(
                subtask, context, max_retries=3
            )
            
            if validation_result['passed']:
                # Accumulate successful result
                self.context_builder.accumulate_subtask_result(subtask, code)
                all_code.append(code)
                subtask.status = 'completed'
            else:
                subtask.status = 'failed'
                return AgentResult(
                    success=False,
                    subtasks=subtasks,
                    final_code=None,
                    error=f"Subtask {subtask.id} failed validation"
                )
        
        # Step 3: Merge results
        final_code = self._merge_subtask_code(all_code)
        
        return AgentResult(
            success=True,
            subtasks=subtasks,
            final_code=final_code,
            validation_summary=self._generate_summary(subtasks)
        )
    
    def _generate_with_retry(self, subtask: Subtask, context: Context, 
                            max_retries: int) -> Tuple[str, Dict]:
        """Generate code with validation and retry logic."""
        explanation = None
        
        for attempt in range(max_retries):
            print(f"  Attempt {attempt + 1}/{max_retries}")
            
            # Generate code
            code = self._generate_code(subtask, context, explanation)
            
            # Validate (skip in greenfield mode)
            if self.mode == 'greenfield':
                validation_result = {'passed': True, 'metrics': {}}
            else:
                validation_result = self.validator.validate(code, context)
            
            if validation_result['passed']:
                return code, validation_result
            
            # Generate explanation for retry
            explanation = self.validator.explain_failure(
                code, validation_result, context
            )
            print(f"  Validation failed: {explanation}")
        
        # Max retries reached
        return code, validation_result
    
    def _generate_code(self, subtask: Subtask, context: Context, 
                      explanation: Optional[str]) -> str:
        """Generate code using LLM."""
        prompt = self._build_generation_prompt(subtask, context, explanation)
        response = self.llm.generate(prompt)
        code = self._extract_code(response)
        return code
    
    def _build_generation_prompt(self, subtask: Subtask, context: Context, 
                                 explanation: Optional[str]) -> str:
        """Build prompt for code generation."""
        prompt_parts = [
            "You are a code generation agent. Generate Python code for this subtask.",
            ""
        ]
        
        if self.mode == 'legacy':
            prompt_parts.append(
                "IMPORTANT: Reuse existing functions from the repository whenever possible. "
                "Do NOT reimplement functionality that already exists."
            )
            prompt_parts.append("")
        
        # Global context
        prompt_parts.append("## Target File Content:")
        prompt_parts.append(f"```python\n{context.global_context}\n```")
        prompt_parts.append("")
        
        # Local context (similar functions)
        if context.local_context:
            prompt_parts.append("## Similar Functions from Repository (REUSE THESE):")
            for i, func in enumerate(context.local_context, 1):
                prompt_parts.append(f"\n### {i}. {func.qualified_name} (similarity: {func.similarity:.2f})")
                prompt_parts.append(f"```python\n{func.signature}\n{func.body}\n```")
                if func.docstring:
                    prompt_parts.append(f'"""{func.docstring}"""')
            prompt_parts.append("")
        
        # Cumulative context
        if context.cumulative_context:
            prompt_parts.append(context.cumulative_context)
            prompt_parts.append("")
        
        # Subtask
        prompt_parts.append(f"## Subtask {subtask.id}:")
        prompt_parts.append(subtask.description)
        prompt_parts.append("")
        
        # Explanation (if retry)
        if explanation:
            prompt_parts.append("## Previous Attempt Failed:")
            prompt_parts.append(explanation)
            prompt_parts.append("")
        
        # Instructions
        prompt_parts.append("## Requirements:")
        prompt_parts.append("- Import necessary modules")
        prompt_parts.append("- Add type hints")
        prompt_parts.append("- Add docstrings")
        prompt_parts.append("- Follow existing code style")
        if self.mode == 'legacy':
            prompt_parts.append("- REUSE functions from the repository (shown above)")
        prompt_parts.append("")
        prompt_parts.append("Generate ONLY the code for this subtask, nothing else:")
        
        return "\n".join(prompt_parts)
    
    def _extract_code(self, response: str) -> str:
        """Extract code from LLM response."""
        # Remove markdown code blocks
        code = re.sub(r'```python\n', '', response)
        code = re.sub(r'```', '', code)
        return code.strip()

@dataclass
class AgentResult:
    success: bool
    subtasks: List[Subtask]
    final_code: Optional[str]
    validation_summary: Optional[Dict] = None
    error: Optional[str] = None
```

---

## 5. Phase 3: Metric Validation System

### 5.1 Overview

The validation system enforces code reuse through three complementary metrics:

1. **Namespace Checker**: Verifies function calls reference repository functions
2. **Structural Matcher**: Detects structural plagiarism using Jaccard similarity
3. **Dependency Validator**: Ensures signature compatibility and import resolution

### 5.2 Namespace Checker (`metrics/namespace_checker.py`)

**Purpose**: Calculate reuse score based on function calls.

**Formula**:
$$\text{Reuse Score} = \frac{|\text{Called Functions} \cap \text{Repo Functions}|}{|\text{Called Functions}|}$$

**Threshold**: ≥40% (configurable)

**Implementation**:

```python
class NamespaceChecker:
    def __init__(self, dependency_graph: DependencyGraph):
        self.dependency_graph = dependency_graph
        self.repo_functions = set(dependency_graph.function_to_module.keys())
    
    def check(self, generated_code: str, threshold: float = 0.4) -> CheckResult:
        """Check namespace reuse in generated code."""
        # Parse generated code
        tree = ast.parse(generated_code)
        
        # Extract function calls
        called_functions = self._extract_calls(tree)
        
        if not called_functions:
            # No function calls - pass by default
            return CheckResult(
                passed=True,
                reuse_score=0.0,
                called_functions=set(),
                repo_functions_used=set(),
                new_functions=set(),
                message="No function calls detected"
            )
        
        # Resolve calls to qualified names
        resolved_calls = self._resolve_calls(called_functions, tree)
        
        # Calculate reuse
        repo_functions_used = resolved_calls & self.repo_functions
        new_functions = resolved_calls - self.repo_functions
        reuse_score = len(repo_functions_used) / len(resolved_calls)
        
        passed = reuse_score >= threshold
        
        return CheckResult(
            passed=passed,
            reuse_score=reuse_score,
            called_functions=resolved_calls,
            repo_functions_used=repo_functions_used,
            new_functions=new_functions,
            message=self._format_message(reuse_score, threshold, 
                                        repo_functions_used, new_functions)
        )
    
    def _extract_calls(self, tree: ast.AST) -> Set[str]:
        """Extract all function calls from AST."""
        calls = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                call_name = self._get_call_name(node)
                if call_name:
                    calls.add(call_name)
        return calls
    
    def _resolve_calls(self, calls: Set[str], tree: ast.AST) -> Set[str]:
        """Resolve function calls to qualified names."""
        # Extract imports
        imports = self._extract_imports(tree)
        
        resolved = set()
        for call in calls:
            # Try to resolve through imports
            qualified = self._resolve_through_imports(call, imports)
            if qualified:
                resolved.add(qualified)
            else:
                # Keep as-is if can't resolve
                resolved.add(call)
        
        return resolved
    
    def _resolve_through_imports(self, call: str, 
                                 imports: Dict[str, str]) -> Optional[str]:
        """Resolve call through import statements."""
        # Check direct imports: from module import function
        if call in imports:
            return imports[call]
        
        # Check if it's a method call: module.function
        parts = call.split('.')
        if len(parts) >= 2:
            module = parts[0]
            if module in imports:
                # Resolve module alias
                actual_module = imports[module]
                return f"{actual_module}.{'.'.join(parts[1:])}"
        
        return None

@dataclass
class CheckResult:
    passed: bool
    reuse_score: float
    called_functions: Set[str]
    repo_functions_used: Set[str]
    new_functions: Set[str]
    message: str
```

### 5.3 Structural Matcher (`metrics/structural_matcher.py`)

**Purpose**: Detect structural plagiarism (reimplementation of existing code).

**Method**: Jaccard similarity on structural tokens

**Formula**:
$$J(A, B) = \frac{|A \cap B|}{|A \cup B|}$$

**Plagiarism Detection**:
$$\text{Plagiarism} = (\text{Structural Sim} \geq 0.85) \land (\text{Namespace Reuse} = 0) \land (\text{Semantic Sim} \geq 0.75)$$

**Threshold**: <85% similarity (configurable)

**Structural Tokens**:
- Control flow: `if`, `for`, `while`, `try`, `with`
- Operations: `+`, `-`, `*`, `/`, `==`, `!=`, `and`, `or`
- Data structures: `list`, `dict`, `set`, `tuple`
- Function calls (normalized)
- Variable assignments (normalized)

**Implementation**:

```python
class StructuralMatcher:
    def __init__(self, vector_db: VectorDB):
        self.vector_db = vector_db
    
    def check(self, generated_code: str, context: Context, 
             threshold: float = 0.85) -> MatchResult:
        """Check for structural plagiarism."""
        # Extract structural tokens from generated code
        gen_tokens = self._extract_structural_tokens(generated_code)
        
        # Compare with similar functions from context
        max_similarity = 0.0
        most_similar_func = None
        
        for func in context.local_context:
            func_tokens = self._extract_structural_tokens(func.body)
            similarity = self._jaccard_similarity(gen_tokens, func_tokens)
            
            if similarity > max_similarity:
                max_similarity = similarity
                most_similar_func = func
        
        # Check for plagiarism
        is_plagiarism = (
            max_similarity >= threshold and
            self._has_no_reuse(generated_code) and
            self._has_high_semantic_similarity(generated_code, most_similar_func)
        )
        
        passed = not is_plagiarism
        
        return MatchResult(
            passed=passed,
            max_similarity=max_similarity,
            most_similar_function=most_similar_func.qualified_name if most_similar_func else None,
            is_plagiarism=is_plagiar

---

**User:**

[write_to_file for 'ARCHITECTURE.md'] Result:
The tool execution failed with the following error:
<error>
This appears to be content for an existing file.
Note: Your response may have been truncated because it exceeded your output limit. You wrote 1192 lines of content, but the line_count parameter was either missing or not included in your response.

RECOMMENDED APPROACH:
1. Try again with the line_count parameter in your response if you forgot to include it
2. Or try using apply_diff instead of write_to_file for targeted changes
3. Or use insert_content to add specific content at particular lines

# Reminder: Instructions for Tool Use

Tool uses are formatted using XML-style tags. The tool name itself becomes the XML tag name. Each parameter is enclosed within its own set of tags. Here's the structure:

<actual_tool_name>
<parameter1_name>value1</parameter1_name>
<parameter2_name>value2</parameter2_name>
...
</actual_tool_name>

For example, to use the attempt_completion tool:

<attempt_completion>
<result>
I have completed the task...
</result>
</attempt_completion>

Always use the actual tool name as the XML tag name for proper parsing and execution.
</error>
<environment_details>
# VSCode Visible Files
ARCHITECTURE.md

# VSCode Open Tabs
ARCHITECTURE.md

# Recently Modified Files
These files have been modified since you last accessed them (file was just edited so you may need to re-read it before editing):
ARCHITECTURE.md

# Current Time
Current time in ISO 8601 UTC format: 2026-05-16T19:59:08.936Z
User time zone: Asia/Calcutta, UTC+5:30

# Current Cost
$0.09

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
====

REMINDERS

Below is your current list of reminders for this task. Keep them updated as you progress.

| # | Content | Status |
|---|---------|--------|
| 1 | Create complete ARCHITECTURE.md with all 19 sections | Pending |
| 2 | Include technical specifications (Jina embeddings, ChromaDB, thresholds) | Pending |
| 3 | Add system diagrams and data flow | Pending |
| 4 | Include API contracts and data models | Pending |
| 5 | Add configuration examples and implementation plan | Pending |
| 6 | Verify completeness and production-readiness | Pending |


IMPORTANT: When task status changes, remember to call the `update_todo_list` tool to update your progress.

</environment_details>

---

**Assistant:**

I need to create the file in multiple parts due to length. Let me start by creating the first part of the ARCHITECTURE.md file with the correct line_count parameter.

<write_to_file>
<path>ARCHITECTURE.md</path>
<content>
# Context-Aware Code Generation Agent - Architecture Document

**Version**: 1.0  
**Last Updated**: May 16, 2026  
**Status**: Production-Ready Blueprint

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [System Architecture Overview](#2-system-architecture-overview)
3. [Phase 1: Offline Indexing Engine](#3-phase-1-offline-indexing-engine)
4. [Phase 2: Task Planner & Agent Orchestration](#4-phase-2-task-planner--agent-orchestration)
5. [Phase 3: Metric Validation System](#5-phase-3-metric-validation-system)
6. [Mode System](#6-mode-system)
7. [Data Flow Diagrams](#7-data-flow-diagrams)
8. [API Contracts and Data Models](#8-api-contracts-and-data-models)
9. [Configuration System](#9-configuration-system)
10. [Implementation Order](#10-implementation-order)
11. [Testing Strategy](#11-testing-strategy)
12. [Deployment Guide](#12-deployment-guide)
13. [Performance Considerations](#13-performance-considerations)
14. [Extensibility Points](#14-extensibility-points)
15. [Troubleshooting](#15-troubleshooting)
16. [Future Enhancements](#16-future-enhancements)
17. [Appendix](#17-appendix)
18. [Quick Reference](#18-quick-reference)
19. [Conclusion](#19-conclusion)

---

## 1. Executive Summary

### 1.1 Problem Statement

Modern code generation agents suffer from three critical issues:
1. **Code duplication**: Generated code reinvents existing functionality
2. **Context blindness**: Agents lack awareness of repository structure and dependencies
3. **Validation gaps**: No systematic verification of code reuse and structural integrity

### 1.2 Solution Overview

The **Context-Aware Code Generation Agent** is a production-ready system that enforces deterministic code reuse through:

- **Offline Indexing**: AST-based parsing, dependency graph construction, and semantic embeddings
- **Intelligent Context Building**: Dynamic retrieval of relevant functions with cumulative subtask memory
- **Multi-Metric Validation**: Namespace checking, structural similarity analysis, and dependency validation
- **Dual-Mode Operation**: Legacy mode (strict reuse) vs. Greenfield mode (flexible creation)

### 1.3 Key Innovations

1. **Rolling Subtask Context**: Ephemeral local context that resets per subtask, preventing token bloat
2. **Call Graph Tracking**: Transitive dependency analysis beyond simple imports
3. **Structural Plagiarism Detection**: Jaccard similarity to catch reimplementation patterns
4. **Dynamic k-Retrieval**: Adaptive context based on similarity thresholds (min_similarity=0.7, max_k=5)
5. **Explanation Layer**: Human-readable failure explanations with actionable suggestions

### 1.4 Technical Stack

| Component | Technology | Rationale |
|-----------|-----------|-----------|
| **Embedding Model** | Jina Code Embeddings V2 | Optimized for code semantics, 768-dim vectors |
| **Vector Database** | ChromaDB | Lightweight, persistent, HNSW indexing |
| **AST Parser** | Python `ast` module | Native, reliable, type-aware |
| **Dependency Analysis** | NetworkX | Graph algorithms, cycle detection |
| **LLM Integration** | OpenAI API (configurable) | Industry standard, extensible |

### 1.5 Success Metrics

- **Reuse Score**: ≥40% of function calls must reference existing repository functions
- **Structural Similarity**: <85% Jaccard similarity to prevent plagiarism
- **Dependency Validation**: 100% import resolution and signature compatibility
- **Performance**: <500ms validation time, <5min indexing for 500-file repos

---

## 2. System Architecture Overview

### 2.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     USER REQUEST                                 │
│  "Add email validation to user_service.py"                      │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                   TASK PLANNER                                   │
│  • Decompose into subtasks                                       │
│  • Determine execution order                                     │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                 AGENT ORCHESTRATOR                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │   Subtask 1  │→ │   Subtask 2  │→ │   Subtask 3  │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
│         │                  │                  │                  │
│         ▼                  ▼                  ▼                  │
│  ┌──────────────────────────────────────────────────┐          │
│  │          CONTEXT BUILDER                          │          │
│  │  • Global Context (target file)                   │          │
│  │  • Local Context (similar functions)              │          │
│  │  • Cumulative Memory (previous subtasks)          │          │
│  └──────────────────────────────────────────────────┘          │
│         │                                                         │
│         ▼                                                         │
│  ┌──────────────────────────────────────────────────┐          │
│  │          LLM CODE GENERATION                      │          │
│  │  • Generate code with context                     │          │
│  │  • Enforce reuse in prompt                        │          │
│  └──────────────────────────────────────────────────┘          │
│         │                                                         │
│         ▼                                                         │
│  ┌──────────────────────────────────────────────────┐          │
│  │       METRIC VALIDATION SYSTEM                    │          │
│  │  ┌────────────┐ ┌────────────┐ ┌────────────┐   │          │
│  │  │ Namespace  │ │ Structural │ │ Dependency │   │          │
│  │  │  Checker   │ │  Matcher   │ │ Validator  │   │          │
│  │  └────────────┘ └────────────┘ └────────────┘   │          │
│  └──────────────────────────────────────────────────┘          │
│         │                                                         │
│         ▼                                                         │
│  ┌──────────────────────────────────────────────────┐          │
│  │  PASS? → Accumulate → Next Subtask               │          │
│  │  FAIL? → Explain → Retry (max 3x)                │          │
│  └──────────────────────────────────────────────────┘          │
└─────────────────────────────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                   FINAL CODE OUTPUT                              │
│  • Merged subtask results                                        │
│  • Validation report                                             │
│  • Reuse statistics                                              │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│              OFFLINE INDEXING ENGINE (Pre-computed)              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │  AST Parser  │→ │ Dependency   │→ │  Vector DB   │         │
│  │              │  │    Graph     │  │  (ChromaDB)  │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
│         ↑                  ↑                  ↑                  │
│         └──────────────────┴──────────────────┘                 │
│                    Repository Files                              │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 Component Interaction Flow

```
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│   User   │────▶│  Planner │────▶│  Agent   │────▶│ Validator│
└──────────┘     └──────────┘     └──────────┘     └──────────┘
                       │                │                │
                       │                ▼                │
                       │         ┌──────────┐           │
                       │         │ Context  │           │
                       │         │ Builder  │           │
                       │         └──────────┘           │
                       │                │                │
                       │                ▼                │
                       │         ┌──────────┐           │
                       └────────▶│ Vector   │◀──────────┘
                                 │   DB     │
                                 └──────────┘
                                       │
                                       ▼
                                 ┌──────────┐
                                 │Dependency│
                                 │  Graph   │
                                 └──────────┘
```

### 2.3 Directory Structure

```
context-aware-agent/
├── indexer/
│   ├── __init__.py
│   ├── ast_parser.py          # AST parsing and extraction
│   ├── dependency_graph.py    # Import and call graph construction
│   ├── vector_db.py           # ChromaDB wrapper
│   └── indexer.py             # Main indexing orchestrator
├── planner/
│   ├── __init__.py
│   └── task_planner.py        # Subtask decomposition
├── agent/
│   ├── __init__.py
│   ├── context_builder.py     # Context assembly
│   └── agent.py               # Agent orchestration
├── metrics/
│   ├── __init__.py
│   ├── namespace_checker.py   # Function call analysis
│   ├── structural_matcher.py  # Jaccard similarity
│   ├── dependency_validator.py # Signature compatibility
│   ├── explanation_generator.py # Failure explanations
│   └── metric.py              # Validation orchestrator
├── config/
│   ├── __init__.py
│   └── config.yaml            # System configuration
├── cli/
│   ├── __init__.py
│   └── main.py                # CLI interface
├── tests/
│   ├── unit/
│   ├── integration/
│   └── fixtures/
├── docs/
│   ├── ARCHITECTURE.md        # This document
│   ├── API.md
│   └── EXAMPLES.md
├── requirements.txt
├── setup.py
└── README.md
```

---

## 3. Phase 1: Offline Indexing Engine

### 3.1 Overview

The indexing engine pre-processes the repository to create:
1. **Function metadata**: Signatures, docstrings, imports, calls
2. **Dependency graph**: Import relationships and call chains
3. **Vector embeddings**: Semantic representations for similarity search

### 3.2 AST Parser (`indexer/ast_parser.py`)

**Purpose**: Extract structured information from Python source files.

**Key Features**:
- Parse Python files into AST
- Extract function definitions with type hints
- Identify imports (including aliases: `import X as Y`, `from X import Y as Z`)
- Extract function calls (simple, nested, method calls)
- Handle decorators and class methods

**Data Extracted**:

```python
@dataclass
class FunctionMetadata:
    name: str                    # Function name
    qualified_name: str          # module.ClassName.function_name
    signature: str               # Full signature with type hints
    docstring: Optional[str]     # Docstring if present
    body: str                    # Function body code
    imports: List[str]           # Direct imports used
    calls: List[str]             # Function calls made
    line_start: int              # Starting line number
    line_end: int                # Ending line number
    file_path: str               # Source file path
    is_method: bool              # True if class method
    decorators: List[str]        # Applied decorators
```

**Implementation Highlights**:

```python
class ASTParser:
    def parse_file(self, file_path: str) -> List[FunctionMetadata]:
        """Parse a Python file and extract function metadata."""
        with open(file_path, 'r', encoding='utf-8') as f:
            source = f.read()
        
        try:
            tree = ast.parse(source, filename=file_path)
        except SyntaxError as e:
            logger.warning(f"Syntax error in {file_path}: {e}")
            return []
        
        functions = []
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                metadata = self._extract_function_metadata(node, file_path, source)
                functions.append(metadata)
        
        return functions
    
    def _extract_calls(self, node: ast.FunctionDef) -> List[str]:
        """Extract all function calls from function body."""
        calls = []
        for child in ast.walk(node):
            if isinstance(child, ast.Call):
                call_name = self._resolve_call_name(child)
                if call_name and not call_name.startswith('_'):  # Skip private
                    calls.append(call_name)
        return list(set(calls))  # Deduplicate
    
    def _resolve_call_name(self, call_node: ast.Call) -> Optional[str]:
        """Resolve function call to qualified name."""
        if isinstance(call_node.func, ast.Name):
            return call_node.func.id
        elif isinstance(call_node.func, ast.Attribute):
            # Handle method calls: obj.method()
            return self._resolve_attribute_chain(call_node.func)
        return None
    
    def _resolve_attribute_chain(self, node: ast.Attribute) -> str:
        """Resolve attribute chain like obj.attr.method."""
        parts = []
        current = node
        while isinstance(current, ast.Attribute):
            parts.append(current.attr)
            current = current.value
        if isinstance(current, ast.Name):
            parts.append(current.id)
        return '.'.join(reversed(parts))
```

**Edge Cases Handled**:
- Nested function definitions
- Lambda functions (excluded from indexing)
- Async functions
- Class methods and static methods
- Import aliases resolution
- Relative imports
- Syntax errors (logged and skipped)

### 3.3 Dependency Graph (`indexer/dependency_graph.py`)

**Purpose**: Build import and call graphs for dependency analysis.

**Graph Types**:

1. **Import Graph**: Module-level dependencies
   - Nodes: Python modules
   - Edges: Import relationships
   - Used for: Detecting circular imports, transitive dependencies

2. **Call Graph**: Function-level dependencies
   - Nodes: Functions (qualified names)
   - Edges: Function calls
   - Used for: Reuse validation, impact analysis

**Data Structure**:

```python
@dataclass
class DependencyGraph:
    import_graph: nx.DiGraph      # Module dependencies
    call_graph: nx.DiGraph        # Function call dependencies
    module_to_functions: Dict[str, List[str]]  # Module → Functions
    function_to_module: Dict[str, str]         # Function → Module
    
    def add_import(self, from_module: str, to_module: str):
        """Add import edge."""
        self.import_graph.add_edge(from_module, to_module)
    
    def add_call(self, caller: str, callee: str):
        """Add function call edge."""
        self.call_graph.add_edge(caller, callee)
    
    def get_transitive_dependencies(self, function: str) -> Set[str]:
        """Get all functions transitively called by this function."""
        if function not in self.call_graph:
            return set()
        return set(nx.descendants(self.call_graph, function))
    
    def detect_circular_imports(self) -> List[List[str]]:
        """Detect circular import chains."""
        try:
            cycles = list(nx.simple_cycles(self.import_graph))
            return cycles
        except nx.NetworkXNoCycle:
            return []
    
    def get_call_chain(self, from_func: str, to_func: str) -> Optional[List[str]]:
        """Find call chain between two functions."""
        try:
            path = nx.shortest_path(self.call_graph, from_func, to_func)
            return path
        except (nx.NetworkXNoPath, nx.NodeNotFound):
            return None
    
    def save(self, filepath: str):
        """Persist graph to disk."""
        data = {
            'import_graph': nx.node_link_data(self.import_graph),
            'call_graph': nx.node_link_data(self.call_graph),
            'module_to_functions': self.module_to_functions,
            'function_to_module': self.function_to_module
        }
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
    
    @classmethod
    def load(cls, filepath: str) -> 'DependencyGraph':
        """Load graph from disk."""
        with open(filepath, 'r') as f:
            data = json.load(f)
        return cls(
            import_graph=nx.node_link_graph(data['import_graph']),
            call_graph=nx.node_link_graph(data['call_graph']),
            module_to_functions=data['module_to_functions'],
            function_to_module=data['function_to_module']
        )
```

### 3.4 Vector Database (`indexer/vector_db.py`)

**Purpose**: Store and retrieve function embeddings for semantic search.

**Technology**: ChromaDB with HNSW indexing

**Configuration**:
- **Embedding Model**: Jina Code Embeddings V2 (jinaai/jina-embeddings-v2-base-code)
- **Dimensions**: 768
- **Distance Metric**: Cosine similarity
- **Index Type**: HNSW (Hierarchical Navigable Small World)
- **Persistence**: Disk-backed storage

**Implementation**:

```python
class VectorDB:
    def __init__(self, persist_directory: str = "./chroma_db"):
        """Initialize ChromaDB client."""
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection = self.client.get_or_create_collection(
            name="functions",
            metadata={"hnsw:space": "cosine"}
        )
        self.embedder = self._load_embedder()
    
    def _load_embedder(self):
        """Load Jina Code Embeddings V2."""
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer('jinaai/jina-embeddings-v2-base-code')
        return model
    
    def add_functions(self, functions: List[FunctionMetadata]):
        """Add functions to vector database."""
        if not functions:
            return
        
        # Prepare texts for embedding
        texts = [self._prepare_text(f) for f in functions]
        
        # Generate embeddings in batches
        embeddings = self.embedder.encode(
            texts, 
            batch_size=32,
            show_progress_bar=True
        )
        
        # Prepare metadata
        metadatas = [self._prepare_metadata(f) for f in functions]
        
        # Add to collection
        self.collection.add(
            ids=[f.qualified_name for f in functions],
            embeddings=embeddings.tolist(),
            metadatas=metadatas,
            documents=texts
        )
    
    def _prepare_text(self, func: FunctionMetadata) -> str:
        """Prepare text for embedding (optimized for code semantics)."""
        parts = [
            f"Function: {func.name}",
            f"Signature: {func.signature}"
        ]
        if func.docstring:
            parts.append(f"Description: {func.docstring}")
        # Include first few lines of body for context
        body_lines = func.body.split('\n')[:5]
        parts.append(f"Implementation: {' '.join(body_lines)}")
        return "\n".join(parts)
    
    def _prepare_metadata(self, func: FunctionMetadata) -> Dict:
        """Prepare metadata for storage."""
        return {
            'qualified_name': func.qualified_name,
            'name': func.name,
            'signature': func.signature,
            'docstring': func.docstring or '',
            'file_path': func.file_path,
            'line_start': func.line_start,
            'line_end': func.line_end,
            'imports': json.dumps(func.imports),
            'calls': json.dumps(func.calls),
            'is_method': func.is_method
        }
    
    def search(self, query: str, k: int = 5, 
               min_similarity: float = 0.7) -> List[Dict]:
        """Search for similar functions with dynamic k-retrieval."""
        # Embed query
        query_embedding = self.embedder.encode([query])[0]
        
        # Search with larger k to filter by similarity
        results = self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=min(k * 2, 20)  # Retrieve more to filter
        )
        
        if not results['ids'][0]:
            return []
        
        # Filter by minimum similarity
        filtered_results = []
        for i, distance in enumerate(results['distances'][0]):
            similarity = 1 - distance  # Convert distance to similarity
            if similarity >= min_similarity:
                filtered_results.append({
                    'id': results['ids'][0][i],
                    'metadata': results['metadatas'][0][i],
                    'similarity': similarity,
                    'document': results['documents'][0][i]
                })
        
        # Return top k after filtering
        return sorted(filtered_results, 
                     key=lambda x: x['similarity'], 
                     reverse=True)[:k]
    
    def get_by_id(self, function_id: str) -> Optional[Dict]:
        """Retrieve function by qualified name."""
        results = self.collection.get(ids=[function_id])
        if results['ids']:
            return {
                'id': results['ids'][0],
                'metadata': results['metadatas'][0],
                'document': results['documents'][0]
            }
        return None
    
    def delete(self, function_ids: List[str]):
        """Delete functions from database."""
        self.collection.delete(ids=function_ids)
    
    def count(self) -> int:
        """Get total number of functions indexed."""
        return self.collection.count()
```

### 3.5 Indexer Orchestrator (`indexer/indexer.py`)

**Purpose**: Coordinate the indexing pipeline.

**Workflow**:

```python
class Indexer:
    def __init__(self, config: Dict):
        self.config = config
        self.parser = ASTParser()
        self.graph_builder = DependencyGraphBuilder()
        self.vector_db = VectorDB(config['vector_db']['persist_directory'])
    
    def index_repository(self, repo_path: str) -> IndexResult:
        """Index entire repository."""
        logger.info(f"Starting indexing of repository: {repo_path}")
        start_time = time.time()
        
        # Step 1: Discover Python files
        python_files = self._discover_files(repo_path)
        logger.info(f"Found {len(python_files)} Python files")
        
        # Step 2: Parse files (parallel processing)
        all_functions = []
        with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
            results = pool.map(self.parser.parse_file, python_files)
            for functions in results:
                all_functions.extend(functions)
        logger.info(f"Extracted {len(all_functions)} functions")
        
        # Step 3: Build dependency graph
        dependency_graph = self.graph_builder.build(all_functions)
        logger.info(f"Built dependency graph: {len(dependency_graph.call_graph.nodes)} nodes, "
                   f"{len(dependency_graph.call_graph.edges)} edges")
        
        # Step 4: Store in vector database
        self.vector_db.add_functions(all_functions)
        logger.info(f"Stored {len(all_functions)} embeddings in vector database")
        
        # Step 5: Persist dependency graph
        graph_path = os.path.join(self.config['vector_db']['persist_directory'], 
                                  'dependency_graph.json')
        dependency_graph.save(graph_path)
        logger.info(f"Saved dependency graph to {graph_path}")
        
        # Step 6: Generate statistics
        stats = self._generate_stats(all_functions, dependency_graph)
        
        # Step 7: Save metadata
        metadata = {
            'repo_path': repo_path,
            'indexed_at': datetime.now().isoformat(),
            'total_files': len(python_files),
            'total_functions': len(all_functions),
            'indexing_time_seconds': time.time() - start_time,
            'stats': stats
        }
        metadata_path = os.path.join(self.config['vector_db']['persist_directory'], 
                                     'index_metadata.json')
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        logger.info(f"Indexing completed in {metadata['indexing_time_seconds']:.2f} seconds")
        
        return IndexResult(
            total_files=len(python_files),
            total_functions=len(all_functions),
            dependency_graph=dependency_graph,
            stats=stats,
            indexing_time=metadata['indexing_time_seconds']
        )
    
    def _discover_files(self, repo_path: str) -> List[str]:
        """Discover all Python files in repository."""
        python_files = []
        exclude_patterns = self.config.get('indexing', {}).get('exclude_patterns', [
            '*/test/*', '*/tests/*', '*/__pycache__/*', '*/venv/*', '*/.venv/*'
        ])
        
        for root, dirs, files in os.walk(repo_path):
            # Skip excluded directories
            dirs[:] = [d for d in dirs if not any(
                fnmatch.fnmatch(os.path.join(root, d), pattern) 
                for pattern in exclude_patterns
            )]
            
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    if not any(fnmatch.fnmatch(file_path, pattern) 
                             for pattern in exclude_patterns):
                        python_files.append(file_path)
        
        return python_files
    
    def _generate_stats(self, functions: List[FunctionMetadata], 
                       graph: DependencyGraph) -> Dict:
        """Generate indexing statistics."""
        return {
            'total_functions': len(functions),
            'functions_with_docstrings': sum(1 for f in functions if f.docstring),
            'functions_with_type_hints': sum(1 for f in functions if ':' in f.signature),
            'total_imports': sum(len(f.imports) for f in functions),
            'total_calls': sum(len(f.calls) for f in functions),
            'avg_calls_per_function': sum(len(f.calls) for f in functions) / len(functions) if functions else 0,
            'circular_imports': len(graph.detect_circular_imports()),
            'modules': len(graph.module_to_functions),
            'max_call_depth': self._calculate_max_call_depth(graph)
        }
    
    def _calculate_max_call_depth(self, graph: DependencyGraph) -> int:
        """Calculate maximum call depth in call graph."""
        if not graph.call_graph.nodes:
            return 0
        try:
            return nx.dag_longest_path_length(graph.call_graph)
        except:
            return 0  # Graph has cycles
    
    def update_index(self, modified_files: List[str]):
        """Incrementally update index for modified files."""
        logger.info(f"Updating index for {len(modified_files)} modified files")
        
        # Parse modified files
        new_functions = []
        for file_path in modified_files:
            functions = self.parser.parse_file(file_path)
            new_functions.extend(functions)
        
        # Remove old entries
        old_ids = [f.qualified_name for f in new_functions]
        self.vector_db.delete(old_ids)
        
        # Add new entries
        self.vector_db.add_functions(new_functions)
        
        # Rebuild dependency graph (full rebuild for simplicity)
        # In production, implement incremental graph updates
        logger.info("Rebuilding dependency graph...")
        # This requires re-parsing all files - optimization opportunity
        
        logger.info("Index update completed")

@dataclass
class IndexResult:
    total_files: int
    total_functions: int
    dependency_graph: DependencyGraph
    stats: Dict
    indexing_time: float
```

---

## 4. Phase 2: Task Planner & Agent Orchestration

### 4.1 Task Planner (`planner/task_planner.py`)

**Purpose**: Decompose user requests into isolated, executable subtasks.

**Decomposition Strategy**:
- Break complex tasks into 3-5 subtasks
- Each subtask should be independently executable
- Subtasks should have clear input/output boundaries
- Maintain logical execution order

**Implementation**:

```python
class TaskPlanner:
    def __init__(self, llm_client):
        self.llm = llm_client
    
    def decompose(self, request: str, target_file: str, 
                 context: Optional[str] = None) -> List[Subtask]:
        """Decompose request into subtasks."""
        prompt = self._build_decomposition_prompt(request, target_file, context)
        response = self.llm.generate(prompt, temperature=0.3, max_tokens=500)
        subtasks = self._parse_subtasks(response)
        
        logger.info(f"Decomposed request into {len(subtasks)} subtasks")
        for i, subtask in enumerate(subtasks, 1):
            logger.info(f"  {i}. {subtask.description}")
        
        return subtasks
    
    def _build_decomposition_prompt(self, request: str, target_file: str,
                                    context: Optional[str]) -> str:
        prompt_parts = [
            "You are a task planning expert. Break down this code generation request into 3-5 isolated subtasks.",
            "",
            f"Request: {request}",
            f"Target File: {target_file}",
        ]
        
        if context:
            prompt_parts.extend(["", f"Additional Context:", context])
        
        prompt_parts.extend([
            "",
            "Requirements:",
            "1. Each subtask must be independently executable",
            "2. Subtasks should have clear input/output",
            "3. Focus on single responsibility per subtask",
            "4. Maintain logical execution order",
            "5. Be specific about what each subtask should accomplish",
            "",
            "Output format (one per line):",
            "1. [Subtask description]",
            "2. [Subtask description]",
            "...",
            "",
            "Subtasks:"
        ])
        
        return "\n".join(prompt_parts)
    
    def _parse_subtasks(self, response: str) -> List[Subtask]:
        """Parse LLM response into subtask objects."""
        lines = response.strip().split('\n')
        subtasks = []
        for i, line in enumerate(lines):
            # Remove numbering and clean
            description = re.sub(r'^\d+\.\s*', '', line).strip()
            if description and len(description) > 10:  # Filter noise
                subtasks.append(Subtask(
                    id=i + 1,
                    description=description,
                    status='pending'
                ))
        
        # Ensure we have at least 1 subtask
        if not subtasks:
            subtasks.append(Subtask(
                id=1,
                description=response.strip(),
                status='pending'
            ))
        
        return subtasks

@dataclass
class Subtask:
    id: int
    description: str
    status: str  # 'pending', 'in_progress', 'completed', 'failed'
    generated_code: Optional[str] = None
    validation_result: Optional[Dict] = None
    retry_count: int = 0
```

### 4.2 Context Builder (`agent/context_builder.py`)

**Purpose**: Assemble relevant context for each subtask.

**Context Types**:

1. **Global Context**: Target file content (persistent across subtasks)
2. **Local Context**: Similar functions from repository (ephemeral, resets per subtask)
3. **Cumulative Memory**: Previously generated subtask code (accumulates)

**Dynamic k-Retrieval Parameters**:
- **min_similarity**: 0.7 (minimum cosine similarity threshold)
- **max_k**: 5 (maximum functions to retrieve)
- Adaptive: Returns fewer functions if similarity drops below threshold

**Implementation**:

```python
class ContextBuilder:
    def __init__(self, vector_db: VectorDB, dependency_graph: DependencyGraph, config: Dict):
        self.vector_db = vector_db
        self.dependency_graph = dependency_graph
        self.config = config
        self.cumulative_memory = []  # Accumulates across subtasks
    
    def build_context(self, subtask: Subtask, target_file: str) -> Context:
        """Build context for subtask execution."""
        # Global context (persistent)
        global_context = self._load_target_file(target_file)
        
        # Local context (ephemeral, dynamic k-retrieval)
        local_context = self._retrieve_similar_functions(
            query=subtask.description,
            min_similarity=self.config['context']['local']['min_similarity'],
            max_k=self.config['context']['local']['max_k']
        )
        
        # Cumulative memory (accumulated)
        cumulative_context = self._format_cumulative_memory()
        
        return Context(
            global_context=global_context,
            local_context=local_context,
            cumulative_context=cumulative_context,
            subtask=subtask
        )
    
    def _load_target_file(self, target_file: str) -> str:
        """Load target file content."""
        try:
            with open(target_file, 'r', encoding='utf-8') as f:
                content = f.read()
            return content
        except FileNotFoundError:
            logger.warning(f"Target file not found: {target_file}")
            return ""
    
    def _retrieve_similar_functions(self, query: str, 
                                    min_similarity: float, 
                                    max_k: int) -> List[FunctionContext]:
        """Retrieve similar functions with dynamic k."""
        results = self.vector_db.search(
            query=query,
            k=max_k,
            min_similarity=min_similarity
        )
        
        logger.info(f"Retrieved {len(results)} similar functions (min_sim={min_similarity})")
        
        # Format results
        function_contexts = []
        for result in results:
            func_id = result['id']
            metadata = result['metadata']
            
            # Get transitive dependencies (limited to top 3)
            dependencies = self.dependency_graph.get_transitive_dependencies(func_id)
            top_dependencies = list(dependencies)[:3]
            
            # Parse stored lists
            imports = json.loads(metadata.get('imports', '[]'))
            calls = json.loads(metadata.get('calls', '[]'))
            
            function_contexts.append(FunctionContext(
                qualified_name=func_id,
                name=metadata['name'],
                signature=metadata['signature'],
                docstring=metadata.get('docstring', ''),
                file_path=metadata['file_path'],
                similarity=result['similarity'],
                imports=imports,
                calls=calls,
                dependencies=top_dependencies
            ))
        
        return function_contexts
    
    def accumulate_subtask_result(self, subtask: Subtask, code: str):
        """Add subtask result to cumulative memory."""
        self.cumulative_memory.append({
            'subtask_id': subtask.id,
            'description': subtask.description,
            'code': code
        })
        logger.info(f"Accumulated subtask {subtask.id} to memory")
    
    def _format_cumulative_memory(self) -> str:
        """Format cumulative memory for prompt."""
        if not self.cumulative_memory:
            return ""
        
        lines = ["## Previously Generated Code in This Session:"]
        for entry in self.cumulative_memory:
            lines.append(f"\n### Subtask {entry['subtask_id']}: {entry['description']}")
            lines.append(f"```python\n{entry['code']}\n```")
        
        return "\n".join(lines)
    
    def reset_cumulative_memory(self):
        """Reset cumulative memory (for new request)."""
        self.cumulative_memory = []
        logger.info("Reset cumulative memory")

@dataclass
class Context:
    global_context: str           # Target file content
    local_context: List[FunctionContext]  # Similar functions
    cumulative_context: str       # Previous subtasks
    subtask: Subtask

@dataclass
class FunctionContext:
    qualified_name: str
    name: str
    signature: str
    docstring: str
    file_path: str
    similarity: float
    imports: List[str]
    calls: List[str]
    dependencies: List[str]
```

### 4.3 Agent Orchestrator (`agent/agent.py`)

**Purpose**: Coordinate subtask execution, code generation, and validation.

**Implementation**:

```python
class Agent:
    def __init__(self, config: Dict):
        self.config = config
        self.llm = self._init_llm(config['agent']['llm'])
        self.context_builder = ContextBuilder(
            vector_db=VectorDB(config['vector_db']['persist_directory']),
            dependency_graph=self._load_dependency_graph(),
            config=config
        )
        self.validator = MetricValidator(config['metrics'], self.context_builder.dependency_graph)
        self.mode = config['agent']['mode']  # 'legacy' or 'greenfield'
    
    def _init_llm(self, llm_config: Dict):
        """Initialize LLM client."""
        from openai import OpenAI
        return OpenAI(api_key=llm_config['api_key'])
    
    def _load_dependency_graph(self) -> DependencyGraph:
        """Load dependency graph from disk."""
        graph_path = os.path.join(
            self.config['vector_db']['persist_directory'],
            'dependency_graph.json'
        )
        return DependencyGraph.load(graph_path)
    
    def execute(self, request: str, target_file: str) -> AgentResult:
        """Execute code generation request."""
        logger.info(f"Starting execution: {request}")
        logger.info(f"Mode: {self.mode}")
        
        # Reset cumulative memory for new request
        self.context_builder.reset_cumulative_memory()
        
        # Step 1: Decompose into subtasks
        planner = TaskPlanner(self.llm)
        subtasks = planner.decompose(request, target_file)
        
        # Step 2: Execute subtasks sequentially
        all_code = []
        for subtask in subtasks:
            logger.info(f"\n{'='*60}")
            logger.info(f"Executing subtask {subtask.id}/{len(subtasks)}: {subtask.description}")
            logger.info(f"{'='*60}")
            
            subtask.status = 'in_progress'
            
            # Build context
            context = self.context_builder.build_context(subtask, target_file)
            
            # Generate code with retry logic
            code, validation_result = self._generate_with_retry(
                subtask, context, max_retries=self.config['metrics']['retry']['max_retries']
            )
            
            if validation_result['passed']:
                # Accumulate successful result
                self.context_builder.accumulate_subtask_result(subtask, code)
                all_code.append(code)
                subtask.status = 'completed'
                subtask.generated_code = code
                subtask.validation_result = validation_result
                logger.info(f"✓ Subtask {subtask.id} completed successfully")
            else:
                subtask.status = 'failed'
                subtask.validation_result = validation_result
                logger.error(f"✗ Subtask {subtask.id} failed after max retries")
                return AgentResult(
                    success=False,
                    subtasks=subtasks,
                    final_code=None,
                    error=f"Subtask {subtask.id} failed validation after {subtask.retry_count} retries"
                )
        
        # Step 3: Merge results
        final_code = self._merge_subtask_code(all_code)
        
        logger.info(f"\n{'='*60}")
        logger.info("All subtasks completed successfully!")
        logger.info(f"{'='*60}")
        
        return AgentResult(
            success=True,
            subtasks=subtasks,
            final_code=final_code,
            validation_summary=self._generate_summary(subtasks)
        )
    
    def _generate_with_retry(self, subtask: Subtask, context: Context, 
                            max_retries: int) -> Tuple[str, Dict]:
        """Generate code with validation and retry logic."""
        explanation = None
        
        for attempt in range(max_retries):
            logger.info(f"  Attempt {attempt + 1}/{max_retries}")
            subtask.retry_count = attempt + 1
            
            # Generate code
            code = self._generate_code(subtask, context, explanation)
            
            # Validate (skip in greenfield mode)
            if self.mode == 'greenfield':
                validation_result = {
                    'passed': True,
                    'mode': 'greenfield',
                    'metrics': {},
                    'message': 'Greenfield mode - validation skipped'
                }
            else:
                validation_result = self.validator.validate(code, context)
            
            if validation_result['passed']:
                logger.info(f"  ✓ Validation passed")
                return code, validation_result
            
            # Generate explanation for retry
            logger.warning(f"  ✗ Validation failed")
            explanation = self.validator.explain_failure(
                code, validation_result, context
            )
            logger.info(f"  Explanation: {explanation[:200]}...")
        
        # Max retries reached
        logger.error(f"  Max retries ({max_retries}) reached")
        return code, validation_result
    
    def _generate_code(self, subtask: Subtask, context: Context, 
                      explanation: Optional[str]) -> str:
        """Generate code using LLM."""
        prompt = self._build_generation_prompt(subtask, context, explanation)
        
        response = self.llm.chat.completions.create(
            model=self.config['agent']['llm']['model'],
            messages=[
                {"role": "system", "content": "You are an expert Python code generator."},
                {"role": "user", "content": prompt}
            ],
            temperature=self.config['agent']['llm'].get('temperature', 0.2),
            max_tokens=self.config['agent']['llm'].get('max_tokens', 2000)
        )
        
        code = self._extract_code(response.choices[0].message.content)
        return code
    
    def _build_generation_prompt(self, subtask: Subtask, context: Context, 
                                 explanation: Optional[str]) -> str:
        """Build prompt for code generation."""
        prompt_parts = [
            "You are a code generation agent. Generate Python code for this subtask.",
            ""
        ]
        
        if self.mode == 'legacy':
            prompt_parts.extend([
                "⚠️ IMPORTANT: Reuse existing functions from the repository whenever possible.",
                "Do NOT reimplement functionality that already exists.",
                "Import and call existing functions instead of writing new implementations.",
                ""
            ])
        
        # Global context
        if context.global_context:
            prompt_parts.extend([
                "## Target File Content:",
                "```python",
                context.global_context[:2000],  # Limit to avoid token overflow
                "```",
                ""
            ])
        
        # Local context (similar functions)
        if context.local_context:
            prompt_parts.append("## Similar Functions from Repository (REUSE THESE):")
            for i, func in enumerate(context.local_context, 1):
                prompt_parts.extend([
                    f"\n### {i}. {func.qualified_name} (similarity: {func.similarity:.2f})",
                    f"File: {func.file_path}",
                    f"```python",
                    f"{func.signature}",
                ])
                if func.docstring:
                    prompt_parts.append(f'    """{func.docstring}"""')
                prompt_parts.extend([
                    "```",
                    f"Imports needed: {

---

**User:**

[write_to_file for 'ARCHITECTURE.md'] Result:
The tool execution failed with the following error:
<error>
This appears to be content for an existing file.
Note: Your response may have been truncated because it exceeded your output limit. You wrote 1130 lines of content, but the line_count parameter was either missing or not included in your response.

RECOMMENDED APPROACH:
1. Try again with the line_count parameter in your response if you forgot to include it
2. Or try using apply_diff instead of write_to_file for targeted changes
3. Or use insert_content to add specific content at particular lines

# Reminder: Instructions for Tool Use

Tool uses are formatted using XML-style tags. The tool name itself becomes the XML tag name. Each parameter is enclosed within its own set of tags. Here's the structure:

<actual_tool_name>
<parameter1_name>value1</parameter1_name>
<parameter2_name>value2</parameter2_name>
...
</actual_tool_name>

For example, to use the attempt_completion tool:

<attempt_completion>
<result>
I have completed the task...
</result>
</attempt_completion>

Always use the actual tool name as the XML tag name for proper parsing and execution.
</error>
<environment_details>
# VSCode Visible Files
ARCHITECTURE.md

# VSCode Open Tabs
ARCHITECTURE.md

# Recently Modified Files
These files have been modified since you last accessed them (file was just edited so you may need to re-read it before editing):
ARCHITECTURE.md

# Current Time
Current time in ISO 8601 UTC format: 2026-05-16T20:01:27.411Z
User time zone: Asia/Calcutta, UTC+5:30

# Current Cost
$0.17

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
====

REMINDERS

Below is your current list of reminders for this task. Keep them updated as you progress.

| # | Content | Status |
|---|---------|--------|
| 1 | Create complete ARCHITECTURE.md with all 19 sections | Pending |
| 2 | Include technical specifications (Jina embeddings, ChromaDB, thresholds) | Pending |
| 3 | Add system diagrams and data flow | Pending |
| 4 | Include API contracts and data models | Pending |
| 5 | Add configuration examples and implementation plan | Pending |
| 6 | Verify completeness and production-readiness | Pending |


IMPORTANT: When task status changes, remember to call the `update_todo_list` tool to update your progress.

</environment_details>

---

**Assistant:**

I need to use the execute_command tool to create the complete ARCHITECTURE.md file. Let me create it using a different approach - I'll write it to a temporary file first and then move it.

<execute_command>
<command>powershell -Command "Get-Content ARCHITECTURE.md | Measure-Object -Line"</command>
</execute_command>

---

**User:**

[execute_command for 'powershell -Command "Get-Content ARCHITECTURE.md | Measure-Object -Line"'] Result:
Command executed in terminal  within working directory 'c:/Users/BIT/Desktop/ibmbob'. Exit code: 0
Output:

Lines Words Characters Property
----- ----- ---------- --------
  436                          



<environment_details>
# VSCode Visible Files
ARCHITECTURE.md

# VSCode Open Tabs
ARCHITECTURE.md

# Current Time
Current time in ISO 8601 UTC format: 2026-05-16T20:01:54.351Z
User time zone: Asia/Calcutta, UTC+5:30

# Current Cost
$0.26

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>plan</slug>
<name>📝 Plan</name>
====

REMINDERS

Below is your current list of reminders for this task. Keep them updated as you progress.

| # | Content | Status |
|---|---------|--------|
| 1 | Create complete ARCHITECTURE.md with all 19 sections | Pending |
| 2 | Include technical specifications (Jina embeddings, ChromaDB, thresholds) | Pending |
| 3 | Add system diagrams and data flow | Pending |
| 4 | Include API contracts and data models | Pending |
| 5 | Add configuration examples and implementation plan | Pending |
| 6 | Verify completeness and production-readiness | Pending |


IMPORTANT: When task status changes, remember to call the `update_todo_list` tool to update your progress.

</environment_details>

---

**Assistant:**

I see the current file has 436 lines. Since the file is too large to create in one go, I'll need to switch to Code mode to properly handle this. Let me switch modes to complete this task.

<switch_mode>
<mode_slug>code</mode_slug>
<reason>Need to create a large ARCHITECTURE.md file (2000+ lines) with all 19 sections. Code mode is better suited for handling large file operations and can work with the file in chunks if needed.</reason>
</switch_mode>

