**User:**

<task>
The biggest issues when using AI agents for engineering tasks are:

1. Context Dilution & Global Architecture Ignorance: Agents operate on localized file lookups. They cannot ingest a 20,000+ line repository context window simultaneously, meaning they fail to grasp the interdependencies across the codebase and introduce silent downstream failures.
2. Failure of Code Reuse (The "New Ingredients" Problem): Agents naturally prefer writing new inline logic, variables, and dependencies rather than reusing existing utilities. This violates DRY principles, introduces massive technical debt, and creates an audit bottleneck for senior engineers reviewing the pull requests.

I am building an idea to solve this: A "Context-Aware Code Generation Agent" pipeline designed to enforce deterministic code reuse and slash token overhead. 

The core architecture consists of:
- The Indexing Engine & Dependency Graph: An offline Python AST (Abstract Syntax Tree) parser that maps the repository's internal import topology (ast.Import/ast.ImportFrom) and indexes function signatures + structural implementation bodies directly into a local vector database—completely bypassing the need for slow, brittle human docstrings.
- Fully-Qualified AST Reward Metric: A verification layer that parses the AI-generated code output, extracts all called nodes, and runs a mathematical intersection against the indexed repository namespaces. If the agent introduces redundant code instead of using an existing utility, the system catches it at the AST level and rejects the output.
- Adaptive Dual-Mode Orchestration: A toggleable execution layer. "Greenfield Mode" allows for net-new, isolated features without restriction, while "Legacy Mode" enforces the strict AST reward metric, forcing the AI agent to act like a precise surgical scalpel using existing infrastructure.

I want us to build an MVP for this tool  First tell me any refinements to this idea you want to suggest from your side
</task>
<environment_details>
# VSCode Visible Files


# VSCode Open Tabs


# Current Time
Current time in ISO 8601 UTC format: 2026-05-16T11:44:26.861Z
User time zone: Asia/Calcutta, UTC+5:30

# Current Cost
$0.00

# Review Exclusions
The following file patterns are excluded from code reviews:
- .vscode/**

# Current Mode
<slug>plan</slug>
<name>📝 Plan</name>


# Current Workspace Directory (c:/Users/BIT/Desktop/ibmbob) Files
No files found.
You have not created a todo list yet. Create one with `update_todo_list` if your task is complicated or involves multiple steps.
</environment_details>

