---
name: subagent-driven-dev
description: Execute implementation plans using fresh subagents per task with two-stage review (spec compliance then code quality). Use when you have an implementation plan with mostly independent tasks to execute in the current session.
context: fork
---

# Subagent-Driven Development

Fresh subagent per task + two-stage review (spec then quality) = high quality, fast iteration.

## Process

1. **Read plan once** - extract all tasks with full text, note context, create TodoWrite
2. **Per task**:
   - Dispatch implementer subagent with full task text + context
   - If subagent asks questions: answer, then let them proceed
   - Subagent implements, tests, commits, self-reviews
   - Dispatch spec reviewer: does code match spec exactly?
   - If spec issues: implementer fixes, re-review until clean
   - Dispatch code quality reviewer on the commits
   - If quality issues: implementer fixes, re-review until clean
   - Mark task complete
3. **After all tasks** - dispatch final reviewer for entire implementation

## Key Rules

- One implementation subagent at a time (no parallel, avoids conflicts)
- Never skip reviews - both spec compliance AND code quality required
- Spec compliance must pass BEFORE code quality review starts
- Provide full task text to subagent (don't make them read plan files)
- Include scene-setting context so subagent understands where task fits
- If reviewer finds issues: implementer fixes, reviewer re-reviews, repeat until approved
- If subagent fails: dispatch fix subagent with specific instructions (don't fix manually)

## Prompt Templates

- `./implementer-prompt.md` - Implementation subagent
- `./spec-reviewer-prompt.md` - Spec compliance reviewer
- `./code-quality-reviewer-prompt.md` - Code quality reviewer

## When NOT to Use

- No implementation plan yet (write one first)
- Tightly coupled tasks (use manual execution)
- Need parallel sessions (use executing-plans skill instead)
