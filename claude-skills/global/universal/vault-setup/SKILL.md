---
name: vault-setup
description: Interactive Obsidian vault configurator. Interviews the user about their role, projects, and goals, then builds a personalized vault structure, CLAUDE.md, and custom slash commands. Use when user says 'vault-setup', 'set up my vault', or 'configure obsidian'.
---

# Vault Setup — Obsidian Configurator

Requires: Obsidian CLI (`obsidian` command in PATH).

## STEP 1 — Discover current vault state

Before asking questions, read the current vault:

```bash
obsidian vaults verbose
obsidian files
obsidian folders
obsidian tags counts sort=count
obsidian properties sort=count counts
```

## STEP 2 — One question, free text

Display this message exactly, then wait for their response:

---

**Tell me about yourself in a few sentences so I can build your vault.**

Answer these in whatever order feels natural:

- What do you do for work?
- What falls through the cracks most — what do you wish you tracked better?
- Work only, or personal life too?
- Do you have existing files to import? (PDFs, docs, slides)

No need to be formal. A few sentences is enough.

---

## STEP 3 — Infer and preview, don't ask more questions

From their free-text answer, infer:
- Their role (tech leader / developer / consultant / creator / student)
- Their primary pain point
- Scope (work only / work + personal / full life OS)
- Whether they have existing files

Then show a vault preview using the **existing** folder structure as a base (don't replace what's already there). Propose additions only.

```
Here's your vault — ready to build when you are.

[folder tree with existing + proposed new folders]

Slash commands:
  /daily-note   — start your day with vault context
  /tldr         — save any session to the right folder
  /[role]       — [role-specific one-liner]

Type "build it" to create this, or tell me what to change.
```

Wait for confirmation before building anything.

## STEP 4 — Build after confirmation

Once they confirm:

### Create missing folders via CLI
```bash
obsidian create path="[folder]/.gitkeep" content=""
```

### Write CLAUDE.md to vault root
Use the Obsidian CLI to create/overwrite:

```bash
obsidian create path="CLAUDE.md" content="[content]" overwrite
```

The CLAUDE.md should contain:
- **Who I Am** — 2-3 sentences in first person about the vault owner
- **Vault Structure** — folder tree with purpose per folder
- **How I Work** — 3-4 bullet points about workflow, pain points, scope
- **Context Rules** — when to read which folders
- **Available Slash Commands** — list of installed commands

### Write memory.md
```bash
obsidian create path="memory.md" content="# Memory\n\nThis file is updated after each session.\n\n---\n\n<!-- Session summaries appended below -->" overwrite
```

## STEP 5 — Set up templates (if daily-notes plugin is enabled)

Check if templates are configured:
```bash
obsidian plugins:enabled
```

If `templates` is enabled but no template folder exists, create one with a daily note template.

## STEP 6 — Final output

```
Done. Your vault is configured.

Your slash commands:
  /daily-note   — run this tomorrow morning
  /tldr         — run this at the end of any session
  /file-intel   — process a folder of files into vault-ready summaries

Next: Try /daily-note to start your first day with vault context.
```
