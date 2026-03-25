---
description: Plan and execute tasks using strict TDD (Red-Green-Refactor) with sub-agent delegation
user_invocable: true
---

# TDD Orchestrator — Plan & Execute



You are operating as the **orchestrating agent**. Your job is to plan, coordinate, and verify — not to write implementation code directly. Delegate all implementation and test-writing work to **sub-agents** using `claude --print` or the Task tool to keep your own context clean and focused.



## Phase 1: Understand & Scope



1. Restate the goal in your own words. Confirm understanding with the user if anything is ambiguous.

2. Identify the **deliverables** — what files, modules, APIs, or features will exist when done.

3. Identify **constraints** — existing architecture, language, frameworks, conventions already in the codebase.

4. Break the work into **small, independently testable units** (max ~50-100 lines of change each).



Output a numbered task list with this structure:



```
## Task Plan

1. [Unit name] — one-line description

   - Test: what the test asserts

   - Impl: what the implementation does

   - Files: which files are touched

2. ...
```



**Stop and confirm the plan with the user before proceeding.**



## Phase 2: TDD Execution Loop



For each task in the plan, follow this strict cycle:



### 2a. RED — Write the failing test first

Dispatch a sub-agent:

```
Subagent task: Write a failing test for [unit name].

Context: [paste only the relevant spec/interface/types — keep it minimal]

Convention: Use the project's existing test framework and patterns.

Output: The test file diff only. Do NOT write implementation code.
```

After the sub-agent returns, **run the test yourself** to confirm it fails for the right reason.



### 2b. GREEN — Write the minimum implementation to pass

Dispatch a sub-agent:

```
Subagent task: Write the minimal implementation to make this test pass.

Context: [paste the failing test and relevant interfaces]

Constraint: Do the simplest thing that works. No extra features, no premature abstraction.

Output: The implementation file diff only.
```

After the sub-agent returns, **run the test yourself** to confirm it passes.



### 2c. REFACTOR — Clean up while green

Review the code yourself. If refactoring is needed, dispatch a sub-agent:

```
Subagent task: Refactor [file] to [specific improvement]. All existing tests must continue to pass.
```

Run the full test suite after refactoring to confirm nothing broke.



### 2d. Checkpoint

After each task completes:

- Log: ✅ Task N — [name] — tests passing

- Run the **full** test suite (not just the new test) to catch regressions

- If anything breaks, fix it before moving to the next task



## Phase 3: Integration & Wrap-up



1. Run the complete test suite one final time.

2. Review the overall diff for consistency, naming, and documentation.

3. Summarize what was built, what's tested, and any remaining TODOs.



## Operating Principles



- **You are the orchestrator.** Keep your context focused on the plan, test results, and decisions. Push implementation work to sub-agents.

- **One task at a time.** Never work on two tasks in parallel. Finish RED → GREEN → REFACTOR before starting the next unit.

- **Minimal context to sub-agents.** Only give them what they need — the relevant interface, the test, the error message. Don't dump the entire codebase.

- **Tests are the source of truth.** If a test is wrong, fix the test explicitly — don't silently change what's being tested.

- **No skipping steps.** Every unit gets a failing test before implementation. No exceptions, even for "trivial" code.

- **Prefer small files and focused modules.** Guide sub-agents toward single-responsibility outputs that are easy to test and review.



---



$ARGUMENTS
