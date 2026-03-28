---
name: daily-note
description: Start the day with Obsidian vault context. Reads or creates today's daily note, checks inbox for unprocessed files, surfaces priorities, and asks what to work on. Use when user says 'daily', 'start my day', 'morning briefing', or 'daily note'.
---

# Daily Note — Morning Briefing

Requires: Obsidian CLI (`obsidian` command in PATH).

## Step 1 — Read or create today's daily note

```bash
obsidian daily:read
```

If no daily note exists yet, create one:
```bash
obsidian daily
```

Then read it to confirm content.

## Step 2 — Check inbox

```bash
obsidian files folder="inbox"
```

If there are files in inbox/, list them and note they need sorting.

## Step 3 — Gather context

Read the most recent daily notes for continuity:
```bash
obsidian files folder="daily" sort=modified limit=5
```

Read the last 2-3 daily notes to understand recent context.

Check for active tasks:
```bash
obsidian tasks todo
```

## Step 4 — Read CLAUDE.md and memory.md for context

```bash
obsidian read path="CLAUDE.md"
obsidian read path="memory.md"
```

## Step 5 — Briefing

Present a summary:
1. **Yesterday's carryover** — unfinished items from recent daily notes
2. **Inbox items** — files waiting to be sorted (count)
3. **Active tasks** — open tasks across the vault
4. **Top 3 priorities** — inferred from recent notes and tasks

Then ask: **"What are we working on today?"**

## Step 6 — Update daily note

After the user responds, append their focus items to today's daily note:
```bash
obsidian daily:append content="## Focus\n- [item 1]\n- [item 2]"
```
