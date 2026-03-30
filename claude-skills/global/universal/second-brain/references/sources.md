# Second Brain — Research Sources

## Videos Processed

| Title | Author | Duration | Key Takeaway | Sotto ID |
|-------|--------|----------|-------------|----------|
| Obsidian + Claude Code as Thinking Partner | Greg Eisenberg + Internet Vin | ~45 min | Vault = persistent context, custom commands (/trace, /emerge, /drift), agent never writes | bc21eb36 |
| Claude Code + Obsidian Second Brain Deep Dive | Unknown | 35 min | Compounding effect (1→5→20 sessions), skills as slash commands, MCP extensions, security concerns | ae28d808 |
| Three-Tier Claude Cowork Framework (Do, Make, Know) | Unknown | 16 min | L1 Do, L2 Make, L3 Know — memory file turns AI from tool to asset | 4a72f3df |
| Map-Mind-Move Framework | Unknown | 11 min | 3-phase AI prompting for unfamiliar domains | 7d520be0 |
| Agent Job Structure | Brian Castle | ~15 min | Agents as recurring jobs, skills as markdown manuals, scheduling = mission control | bdbd3055 |
| AI Agents Get Real Money — 90-Day Survival | Mike Russell | 13 min | Autonomous agents with real budgets, treasurer AI as gatekeeper | 8a5dd602 |
| OpenClaw Generates $2,350 in Crypto | Mike Russell | 7 min | Agent becomes cash-flow positive in 72hrs via social media presence | (pending) |
| How Journaling Can Change Your Life | Ali Abdaal | 23 min | Externalizing thoughts reduces power, 3 levels of journaling, AI as journal partner | 1040920f |
| The GPS Method for Goal Achievement | Ali Abdaal | 21 min | Goal/Plan/System framework, writing goals = 42% more likely | ec08de21 |
| How to Get Rich on Easy Mode | Ali Abdaal | 20 min | Help others make money, B2B > B2C, price on value | 42c4712d |
| Systematically Generate Business Ideas | Ali Abdaal | 25 min | Holy Trinity (person+problem+product), diverge→converge→emerge | 75c1ea2d |
| Zero to $1M Business Framework | Ali Abdaal x Daniel Priestley | 1h 12m | 766 apprenticeship, scout→squad, P4P, repeatable week | 5c0097ed |
| Four Books to Achieve Financial Freedom | Ali Abdaal | 21 min | Millionaire Fast Lane, $100M Offers, DotCom Secrets, Million Dollar Weekend | 59d368e8 |

## Architecture References

| Source | Pattern | Notes |
|--------|---------|-------|
| Gaute's draw.io diagram (Jan 29) | Input→Process→Store→Output pipeline | Original second brain architecture vision |
| Our live system | OpenClaw + MEMORY.md + memory/*.md + Sotto | Battle-tested daily since Jan 2026 |
| Zettelkasten method | Literature→Permanent→Connected notes | Classic, works well with AI pattern discovery |
| PARA (Tiago Forte) | Projects/Areas/Resources/Archive | Popular but may over-categorize for AI use |
| Johnny Decimal | Numbered categories | Good for file systems, less relevant for AI-native |

## Obsidian Plugin Reality Check (2026-02-27)

| Plugin | What it does | Limitation for Gaute |
|--------|-------------|---------------------|
| Tasks | Query-based task lists from markdown checkboxes | No calendar view, no drag-drop scheduling, no Sunsama-style review |
| Full Calendar | FullCalendar lib in Obsidian, events from frontmatter/daily notes | Remote calendars (ICS/CalDAV) are READ-ONLY. No task integration. No multi-source unified view with drag-drop. |
| Dataview | Query notes as database | Read-only queries, not interactive task management |
| Kanban | Board view from markdown | No calendar, no time-based scheduling |
| Periodic Notes | Daily/weekly/monthly templates | Just templates, no review flow |

**Verdict:** Obsidian cannot deliver unified calendar view (tasks + meetings + Google Cal + drag-drop). Would require 4-5 plugins glued together, each with different UX. Not viable for Gaute's requirements.

## To Research
- Tiago Forte "Building a Second Brain" (book) — PARA method deep dive
- Nick Milo "Linking Your Thinking" — MOC (Maps of Content) approach
- August Bradley "PPV" (Pillars, Pipelines, Vaults) — Notion-based system
- Maggie Appleton "Digital Gardens" — publish-as-you-learn philosophy
- PowerSync for Supabase offline-first
- Capacitor for wrapping Next.js as native iOS app
