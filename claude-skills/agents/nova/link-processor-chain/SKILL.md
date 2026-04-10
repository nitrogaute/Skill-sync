---
name: link-processor-chain
description: "Chained skill: processes a URL end-to-end. Extracts content (defuddle), saves to Obsidian vault (13-References), cross-references via Knowledge Graph, and reports back. Use when Gaute sends any URL/link."
disable-model-invocation: true
allowed-tools: Bash, Read, Write, Edit, Grep, Glob
---

# Link Processor Chain

Deterministic multi-step pipeline for processing URLs into the Obsidian vault.

## Chain Steps

Execute these steps in order. Each step's output feeds the next. If a step fails, log the error and continue with whatever data you have.

### Step 1: Classify the URL

Determine the link type from the URL pattern:
- `youtube.com` or `youtu.be` -> `youtube`
- `github.com` -> `github`
- `x.com` or `twitter.com` -> `twitter`
- Everything else -> `article` (default, covers blogs, tools, products, docs)

For tools/products (SaaS landing pages, dev tools, hardware), override tag to `tool`.

### Step 2: Extract Content

**YouTube:**
```bash
bash /Users/nitromini/ClaudeClaw/scripts/youtube-summary.sh "URL"
```
This uses Gemini API. If it fails, fall back to the `youtube-watcher` skill pattern.
Never use browser or web_fetch for YouTube.

**Twitter/X:**
```bash
curl -s "https://publish.twitter.com/oembed?url=URL" | jq -r '.html'
```

**All other URLs:**
```bash
defuddle parse "URL" --md
```

Store the extracted content in a variable for the next step.

### Step 3: Build Vault Note

Create a reference note at `/Users/nitromini/Documents/vault/13-References/FILENAME.md`

**Filename:** kebab-case from title, e.g. `three-tier-claude-framework.md`

**Template:**
```yaml
---
title: "Descriptive Title - Creator Name"
type: Reference
source: "ORIGINAL_URL"
tags: [TAG_FROM_STEP_1]
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
---
```

**Required sections:**
1. `## Summary` - with creator attribution, 3-5 sentence overview
2. Content sections - detailed, fact-rich. Include specific numbers, tools, techniques, frameworks mentioned. Never write shallow one-line summaries.
3. `## Key Takeaways` - bulleted list of actionable insights
4. `## Relevance to Us` - how this connects to Gaute's projects, goals, or setup
5. `## Connections` - wikilinks to related vault notes (populated in Step 4)

**Language:** English always. Never Norwegian in vault files.

### Step 4: Cross-Reference via Knowledge Graph

Search the vault for related content:
```
kg_search with the title and key concepts from the note
```

From the search results, build the `## Connections` section with wikilinks:
```markdown
## Connections

- [[Related Note 1]] - how it relates
- [[Related Note 2]] - how it relates
```

Update the note file with the connections.

### Step 5: Verify

1. Read back the saved file to confirm it exists and has correct frontmatter
2. Confirm the file is in `13-References/`
3. Report: title, file path, tag, and number of connections found

## Output Format

After all steps complete, report concisely:

```
Saved: [title]
Path: 13-References/[filename].md
Type: [youtube|article|tool|github|twitter]
Connections: [N] related notes linked
```

## Error Handling

- Step 2 fails: Report "Could not extract content from URL" and stop
- Step 3 fails: Report the write error
- Step 4 fails (KG unavailable): Save note without connections, mention KG was offline
- Never silently skip steps
