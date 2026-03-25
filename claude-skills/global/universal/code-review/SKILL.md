---
name: code-review
description: Review code changes for bugs, security issues, performance problems, and style. Use when asked to review a PR, diff, or code changes.
disable-model-invocation: true
context: fork
agent: Explore
---

# Code Review

Review the provided code changes thoroughly.

## Checklist

For each file changed, check:

1. **Correctness** - Logic errors, off-by-one, null/undefined handling, race conditions
2. **Security** - Injection (SQL, XSS, command), auth/authz gaps, secret leaks, OWASP top 10
3. **Performance** - N+1 queries, unnecessary re-renders, missing indexes, memory leaks
4. **Error handling** - Unhandled promises, missing try/catch at boundaries, swallowed errors
5. **Readability** - Naming, complexity, dead code, misleading comments

## Output format

For each issue found:

```
[SEVERITY] file:line - description
  > problematic code snippet
  FIX: suggested fix
```

Severity levels:
- **CRITICAL** - Will cause bugs, security holes, or data loss
- **WARNING** - Likely problem, should fix before merge
- **SUGGESTION** - Improvement, not blocking

End with a summary: total issues by severity, and whether the change is safe to merge.

## Rules
- Be specific. Point to exact lines.
- Don't nitpick formatting if a formatter/linter is configured.
- Focus on what matters. 3 real issues > 20 style nits.
- If the code looks good, say so. Don't invent problems.
