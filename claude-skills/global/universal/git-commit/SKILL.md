---
name: git-commit
description: Create a well-structured git commit from staged/unstaged changes. Use when asked to commit, or after completing a task.
disable-model-invocation: true
---

# Git Commit

Create a clean, well-structured git commit.

## Steps

1. Run `git status` and `git diff --stat` to understand what changed
2. Run `git log --oneline -5` to match the repo's commit style
3. Stage relevant files (skip .env, credentials, build artifacts)
4. Write a commit message following conventional commits:

```
type(scope): short description

Optional body explaining why, not what.

Co-Authored-By: Claude <noreply@anthropic.com>
```

Types: feat, fix, refactor, docs, test, chore, style, perf

## Rules
- Message focuses on WHY, not WHAT (the diff shows what)
- One logical change per commit
- Never commit secrets, .env files, or credentials
- Never force push to main/master
- Never use --no-verify unless explicitly asked
- If pre-commit hook fails, fix and make a NEW commit (don't amend)
