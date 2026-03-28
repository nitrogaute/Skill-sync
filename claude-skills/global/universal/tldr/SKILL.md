---
name: tldr
description: Save a structured summary of the current session to the Obsidian vault. Captures decisions, key learnings, and next actions, then stores in the right folder. Use when user says 'tldr', 'save summary', 'save this session', 'wrap up', or at the end of a work session.
---

# TL;DR — Session Summary to Vault

Requires: Obsidian CLI (`obsidian` command in PATH).

## Step 1 — Analyze the conversation

Review the entire conversation and extract:
1. **What was decided or figured out** — key decisions, conclusions
2. **Things to remember** — facts, preferences, patterns learned
3. **Next actions** — concrete follow-up tasks (if any)
4. **Topic/category** — which vault folder this belongs in

## Step 2 — Determine the right folder

Based on the topic discussed:
- Project work → `projects/[name].md` (append or create)
- Meeting notes → `meetings/[date]-[topic].md`
- Research/learning → `research/[topic].md`
- General/daily → append to today's daily note

Check existing folders:
```bash
obsidian folders
```

## Step 3 — Format the summary

Create a clean markdown note:

```markdown
---
date: YYYY-MM-DD
tags:
  - session-summary
  - [topic-tag]
---

# [Descriptive Title]

## Decisions
- [bullet points]

## Key Takeaways
- [bullet points]

## Next Actions
- [ ] [action item 1]
- [ ] [action item 2]

## Session Context
[1-2 sentences about what prompted this session]
```

## Step 4 — Save to vault

```bash
obsidian create path="[folder]/[filename].md" content="[formatted summary]"
```

If appending to an existing note (e.g., a project):
```bash
obsidian append path="[existing-note].md" content="\n\n---\n\n## Session [date]\n\n[summary content]"
```

## Step 5 — Update memory.md

Append a brief entry to memory.md:
```bash
obsidian append path="memory.md" content="\n\n## [date] — [topic]\n- [1-line summary]\n- Saved to: [path]"
```

## Step 6 — Update daily note

If today's daily note exists, append a reference:
```bash
obsidian daily:append content="- Saved session summary: [[filename]]"
```

## Step 7 — Confirm

Tell the user:
- Where the summary was saved
- How many decisions/actions were captured
- Suggest any follow-up
