---
name: file-intel
description: Process a folder of files (PDF, DOCX, PPTX, XLSX, images, code) and generate Obsidian-ready markdown summaries in the vault inbox. Uses the agent's built-in capabilities to read and summarize files. Use when user says 'file intel', 'process these files', 'summarize this folder', 'import files', or provides a folder path to process.
---

# File Intel — Folder Processor to Obsidian

Processes any folder of files and generates clean, structured Obsidian markdown summaries.

## Step 1 — Get the folder

Ask the user which folder to process. They can provide:
- An absolute path
- A relative path
- "inbox" to process the vault's inbox folder

## Step 2 — Scan the folder

List all files in the target folder. Supported formats:
- Documents: `.pdf`, `.docx`, `.pptx`, `.xlsx`, `.csv`
- Text: `.md`, `.txt`, `.json`, `.xml`, `.yaml`
- Code: `.py`, `.js`, `.ts`, `.html`, `.css`
- Images: `.png`, `.jpg` (describe if possible)

Report the count and types found. Ask for confirmation before processing.

## Step 3 — Process each file

For each file:
1. Read the file content
2. Extract the key information — strip boilerplate, headers, filler
3. Create a compressed summary (300-600 words max)
4. Format as Obsidian markdown with frontmatter

Summary template:
```markdown
---
date: YYYY-MM-DD
source: [original filename]
type: [document/spreadsheet/presentation/code/text]
tags:
  - file-intel
  - [topic-tag]
---

# [Descriptive Title]

## Key Points
- [extracted insights]

## Details
[compressed content — signal, not noise]

## Source
Original file: `[path/filename]`
Processed: [date]
```

## Step 4 — Save summaries to vault

Save each summary to the vault inbox:
```bash
obsidian create path="inbox/[descriptive-name].md" content="[summary]"
```

## Step 5 — Create master summary

If multiple files were processed, create a digest:
```bash
obsidian create path="inbox/DIGEST-[date].md" content="[master summary of all files]"
```

## Step 6 — Report back

Tell the user:
- How many files were processed
- Where summaries landed (inbox/)
- Point them to the digest note
- Suggest: "Want me to sort these from inbox/ into the right folders?"
