---
name: second-brain
description: Best practices for building and maintaining a second brain / personal knowledge management system with AI. Covers architecture patterns, capture workflows, retrieval strategies, and lessons learned from practitioners. Use when discussing knowledge management, note-taking systems, Obsidian/Sotto/Tana workflows, or evaluating PKM tools and approaches.
---

# Second Brain — Best Practices & Patterns

A living playbook for personal knowledge management (PKM) with AI augmentation. Built from real practitioner insights, our own experience, and research.

## Core Philosophy

**Context beats prompts.** Generic context produces generic output. The more structured knowledge your AI has access to, the better it performs — not through better prompting, but through better *context*.

**The compounding effect:** Session 1 → knows your folder structure. Session 5 → knows your projects and voice. Session 20 → personalized OS that knows your knowledge base better than you consciously remember.

## Architecture Patterns

### Pattern 1: AI-Native Workspace (Our Approach)
```
Inputs → AI Agent (Trym) → Structured DB (Sotto) + Flat Files (memory/)
                         → Processing: summarize, tag, link, act
                         → Output: searchable knowledge, proactive insights, task execution
```
- **Strengths:** Full automation, AI does capture + processing + retrieval
- **Weaknesses:** Dependent on agent availability, less "thinking space" feel
- **Tools:** OpenClaw + Sotto (Supabase) + memory/*.md + TickTick

### Pattern 2: Obsidian + AI Agent
```
Human writes in Obsidian → AI reads vault (read-only) → AI discovers patterns
                        → Custom commands: /trace, /emerge, /drift, /ideas
                        → AI never writes to vault (human controls truth)
```
- **Strengths:** Human owns the thinking, backlinks give AI relationship understanding, local-first privacy
- **Weaknesses:** Requires manual note-taking discipline, AI is reactive not proactive
- **Tools:** Obsidian (free) + Claude Code ($20/mo Pro) or API
- **Source:** Greg Eisenberg + Internet Vin, also "Claude Code + Obsidian Deep Dive"

### Pattern 3: Hybrid (Best of Both Worlds?)
```
Obsidian = thinking space (daily notes, ideas, reflection)
Sotto/DB = structured knowledge (resources, contacts, decisions, projects)
AI Agent = bridge (reads both, processes inputs, routes to correct store)
```
- **Status:** Under consideration. See references/hybrid-evaluation.md when created.

### Pattern 4: Three-Tier Agent Framework (Do, Make, Know)
```
L1 Do: Single task + cloud.md instructions + changelog
L2 Make: Multi-system workflows with sub-agents in parallel
L3 Know: Memory file that compounds knowledge across sessions
```
- **Key insight:** L3 turns AI from tool to asset. Logging prevents redo.
- **Source:** Brian Castle, "Three-Tier Claude Cowork Framework"

## Capture Workflows

### What to Capture
| Input | Processing | Storage |
|-------|-----------|---------|
| YouTube videos | Summarize → extract frameworks → tag | Sotto (resource) + skill if applicable |
| Articles/links | Summarize → relevance check → store | Sotto (resource) |
| Voice notes | Whisper transcribe → process → route | Sotto or daily memory |
| Meeting notes | Transcribe → action items → decisions | Sotto (meeting) + TickTick tasks |
| Ideas (shower thoughts) | Quick capture → develop later | Sotto (idea) or Obsidian daily note |
| Decisions | Document reasoning + context | Sotto (decision) — never lose the *why* |

### The YouTube Pipeline (Battle-Tested)
1. User sends link → `summarize` CLI extracts transcript
2. AI generates structured summary with key takeaways
3. Relevance check: business → GTB skill, productivity → Sotto, technical → project docs
4. Store with tags, source URL, and cross-references
5. ~2-3 min per video, handles rapid-fire batches

## Retrieval Strategies

### Making Knowledge Findable
- **Tags over folders** — flat + tagged beats deep hierarchies
- **Consistent schema** — same fields across similar items (source, summary, takeaways)
- **Cross-linking** — connect ideas across domains (Hormozi ↔ Abdaal ↔ Priestley)
- **AI-powered search** — semantic search over structured data beats keyword grep

### The Zettelkasten Principle
Literature notes → Permanent notes → Connected ideas
- Don't just save — *process*. Rewrite in your own framing.
- Atomic notes: one idea per note, well-linked.
- 500+ note systems work when AI helps find thematic connections across years.

## Security & Trust

- **Prompt injection risk:** Hidden instructions in emails/web content can hijack agents reading your notes
- **MCP supply chain:** Malicious MCP server updates could access your files
- **Mitigations:**
  - Only use trusted/self-created MCPs
  - Disable MCP auto-updates
  - Restrict AI agent to specific directories
  - Agent reads vault, doesn't write (Obsidian pattern)
  - API keys in keychain, never in notes

## Lessons Learned (Our Experience)

1. **"Manage the vault, not the agent"** — structure your knowledge well, and the AI becomes smart automatically
2. **Skills = executable knowledge** — repeatable workflows as markdown manuals, not one-off prompts
3. **Daily logs are underrated** — `memory/YYYY-MM-DD.md` gives temporal context no tag system can
4. **Don't duplicate** — one source of truth per item. Sotto for structured, memory/ for temporal
5. **Batch processing works** — rapid-fire video links → acknowledge batch → process in parallel
6. **Overnight compounding** — AI works while you sleep, knowledge base grows 24/7
7. **Map-Mind-Move for new domains** — 3-phase prompting: Map (briefing), Mind (inversion/risks), Move (action plan)
8. **Context window is scarce** — curate aggressively. Archive old, surface relevant.

## Tools Comparison

| Tool | Format | AI-Ready | Offline | Cost | Lock-in |
|------|--------|----------|---------|------|---------|
| Obsidian | Local markdown | ✅ Native | ✅ | Free | None |
| Sotto (Supabase) | Postgres + API | ✅ Via SQL/MCP | ❌ | Free tier | Low |
| Notion | Proprietary | ⚠️ Via API | ❌ | $8-15/mo | Medium |
| Tana | Proprietary | ⚠️ Via MCP | ❌ | Free/$10 | High |
| Apple Notes | iCloud DB | ⚠️ Via CLI | Partial | Free | High |
| Logseq | Local markdown | ✅ Native | ✅ | Free | None |

## Research Sources

See `references/sources.md` for full list of processed videos and articles.

## Gaute's Priorities (Definitive — 2026-02-27)

### Pri 1: Meeting & Call Transcription → Structured Storage
- Transcribe: Teams, phone calls, physical meetings
- Capture: app that records PC audio (Windows + mic)
- Store linked to: topics, dates, people, todos
- Must be searchable and cross-referenced
- **Sotto should OWN transcription** (not pipeline from Tana)

### Pri 2: Task Management Integrated with Knowledge
- Tasks linked to: topics, goals, OKRs, people
- Calendar view as primary task interface (TickTick's best feature)
- Tasks + meetings + calendar events in ONE unified view, multi-source
- Structured daily review (Sunsama-style): morning prioritization + evening review
- System must be TRUSTED — gives surplus and overview
- @Trym delegation inline in nodes
- AI involved for prioritization, execution, delivery

### Pri 3: Low-Friction Infrastructure
- Web version (primary)
- iOS app (PWA vs native TBD)
- Offline support: YES, important
- Maybe Apple Watch
- Apple Pencil support (missed from Amplenote)
- Minimize threshold to use for EVERYTHING in life

### The Real Purpose
**Second brain = context-building for Trym.** Not a notebook — it's Trym's memory and understanding, enabling autonomous action on Gaute's behalf.

## Tool Evaluations (Gaute's Experience)

| Tool | Loved | Hated | Verdict |
|------|-------|-------|---------|
| **Tana** | Transcription, supertags | iOS app, no notifications, templates break, limited AI | Good for meetings, bad for everything else |
| **TickTick** | Calendar view (99% used), fast capture | No review process, drowns in overdue, manual | Best task capture, worst task management |
| **Sunsama** | Structured morning/evening reviews | App too limited otherwise | Great workflow, weak tool |
| **Amplenote** | Tasks+notes combo, Apple Pencil/iPad | Task mgmt never clicked, no transcription, ugly | Pencil support is rare and missed |
| **Obsidian** | Never used but drawn to: .md files, interface, community | Worried about: AI integration, transcription, calendar/task view | Unproven but emotionally appealing |

### Key Pattern
Task management has NEVER clicked for Gaute in any tool. The problem isn't the tool — it's the missing review loop + AI assistance layer.

## Open Questions

- [ ] Sotto vs Obsidian — commit to one direction
- [ ] iOS: PWA vs native app?
- [ ] How to handle knowledge decay (outdated notes)?
- [ ] Optimal tagging taxonomy — flat vs hierarchical?
- [ ] Voice-first capture: Whisper local vs cloud API tradeoff?
- [ ] Windows desktop app for meeting capture (Electron/Tauri)?
- [ ] Calendar data sources: Google Calendar, Teams, TickTick — unified view architecture?
