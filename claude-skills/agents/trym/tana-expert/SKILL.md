# Tana Expert Skill

---
name: tana-expert
description: Comprehensive Tana expertise covering both Local API/MCP integration and UI/app features. Use when user asks how to do something in Tana, wants to interact with Tana via API, or needs guidance on Tana features including supertags, fields, views, AI agents, command line, outline editor, daily notes, templates, mobile app, workspace management, or any Tana-related tasks.
requires: For API - mcporter, tana-local MCP server, Tana Desktop running. For UI - Tana Desktop or Web app.
---

## Overview

Tana is a knowledge management tool that combines an outline editor with a knowledge graph. Everything is a **node**. Nodes can have **supertags** (types) with **fields** (attributes). This skill covers both UI features and API/MCP integration.

**Quick Access:**
- **API/MCP Details:** See [api-workflows.md](references/api-workflows.md)
- **UI Features:** See [ui-workflows.md](references/ui-workflows.md)
- **AI & Automation:** See [ai-features.md](references/ai-features.md)
- **Views & Search:** See [views-and-search.md](references/views-and-search.md)
- **Best Practices:** See [best-practices.md](references/best-practices.md)

---

## Core Concepts

### Nodes
- Everything is a node in an outline
- Atomic units of information
- Can be nested (parent/child)
- Can have multiple supertags
- References link nodes: `[[Node name]]` or `[[^nodeId]]`
- One owner, multiple parents possible

### Supertags = Types
- Classify nodes as specific object types
- Define fields (attributes) for that type
- Contain content templates
- Can extend other tags (inheritance)
- Examples: #task, #meeting, #person, #project

### Fields = Attributes

| Type | Description | Example |
|------|-------------|---------|
| `plain` | Free text | Notes, descriptions |
| `number` | Numeric value | Priority, count |
| `date` | Date/datetime | Due date, meeting time |
| `url` | Web link | Website, reference |
| `email` | Email address | Contact email |
| `checkbox` | Boolean | Urgent flag |
| `options` | Dropdown (text values) | Status: To Do, In Progress, Done |
| `options from supertag` | Instance reference (links to tagged nodes) | Assignee → #person nodes |

**Key Insight:** "Options from supertag" creates references and can auto-create tagged nodes!

---

## Essential Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| **Command Line** | `Cmd/Ctrl+K` (most important!) |
| **Global Search** | `Cmd/Ctrl+S` |
| **Today's Note** | `Cmd/Ctrl+Shift+D` |
| Indent Child | `Tab` |
| Outdent Sibling | `Shift+Tab` |
| Move Node Up/Down | `Cmd/Ctrl+Shift+↑/↓` |
| Expand/Collapse | `Cmd/Ctrl+↓/↑` |
| Copy Reference | `Cmd/Ctrl+C` |
| Move To Menu | `Cmd/Ctrl+Shift+M` |
| Create Shortcut | `Cmd/Ctrl+Shift+K` |
| @ Mention/Reference | `@` + name |
| Apply Tag | `#` + tagname |

---

## MCP/Local API Quick Reference

### First Time Using the API?

**See [Getting Started: Workspace Discovery](references/api-workflows.md#getting-started-workspace-discovery)** for the essential workflow:

1. `list_workspaces` → Get your workspace ID
2. `list_tags` → See all your supertags
3. `get_tag_schema` → Inspect tag fields
4. `search_nodes` → Find nodes by tag
5. `read_node` → Get full content

This is the recommended exploration pattern for any Tana workspace.

### Setup & Connection

**Enable API:**
1. Open Tana Desktop
2. Settings → Tana Labs → Enable "Local API/MCP server (Alpha)"
3. Verify: `curl http://localhost:8262/health`

**Endpoints:**
- MCP: `http://localhost:8262/mcp`
- Health: `http://localhost:8262/health`
- Docs: `http://localhost:8262/docs`
- OpenAPI: `http://localhost:8262/openapi.json`

**Claude Code Setup (Auto):**
- Desktop: Options → Local API settings → Enable Claude Code
- Manual: `claude mcp add --transport http tana-local http://localhost:8262/mcp`

**Other Clients:**
- Codex: `codex mcp add tana-local --url http://localhost:8262/mcp`
- Gemini: `gemini mcp add -t http -s user tana-local http://localhost:8262/mcp`

### Essential MCP Tools

**IMPORTANT:** Most tools require a `workspaceId` parameter. Always run `list_workspaces` first!

**Read Operations:**
- `list_workspaces` - Get available workspaces (START HERE!)
- `search_nodes` - Query with filters (requires workspaceId)
- `read_node` - Get node content as markdown (requires workspaceId)
- `get_children` - Paginated child nodes (requires workspaceId)
- `list_tags` - All workspace tags (requires workspaceId)
- `get_tag_schema` - Tag field definitions (requires workspaceId)

**Write Operations:**
- `import_tana_paste` - Import hierarchical content (primary creation method)
- `tag` / `untag` - Add/remove tags
- `set_field_option` - Set dropdown/reference fields
- `set_field_content` - Set text/number/date fields
- `create_tag` - New supertag
- `add_field_to_tag` - Extend tag schema
- `check_node` / `uncheck_node` - Todo status
- `edit_node` - Modify node text
- `trash_node` - Move to trash
- `get_or_create_calendar_node` - Daily/weekly notes

**For complete API reference and examples:** See [api-workflows.md](references/api-workflows.md)

---

## UI Features Quick Reference

### Views (7 Types)

**Editing Views:**
- **Outline:** Bullet list with full editor (default)
- **Table:** Rows=nodes, Columns=fields, calculations
- **Cards:** Card grid, drag-and-drop, Kanban-style

**Navigation Views:**
- **List:** Two-panel master-detail
- **Calendar:** Day/week/month time-based
- **Side Menu:** Navigation sidebar
- **Tabs:** Horizontal tab interface

**Access:** Right-click → "View as" or `Cmd/K` → "View as [type]"

**For detailed view usage:** See [views-and-search.md](references/views-and-search.md)

### Command Line (`Cmd/Ctrl+K`)

Access to all Tana actions:
- Find Nodes - Search with filters
- Remind me - Schedule for date
- View as - Switch visualization
- Move to - Relocate nodes
- Convert to supertag - Create tag from node

**Custom Shortcuts:** `Cmd/Shift+K` after finding command

### Daily Notes & Calendar

- `Cmd/Ctrl+Shift+D` - Jump to today
- Each day is a node
- Calendar integration (Google Calendar, etc.)
- Calendar view plots by date fields

### Tana Templates

**Access:** Sidebar → Supertags → "Browse templates"

**What They Are:**
- Pre-built supertags, workflows, systems
- Install into workspace
- Full freedom to modify after install
- No connection to original post-install

**Categories:** Productivity, note-taking, project management, personal, business

**For template workflows:** See [ui-workflows.md](references/ui-workflows.md)

### Mobile App (Tana Capture)

**Platforms:** iOS (Nov 2024+), Android (Feb 2025+)

**Features:**
- Text capture
- Voice memos (91 languages, auto-transcription)
- Photo/video capture
- Text scanning (OCR)
- Share from other apps
- Offline capable
- Syncs to Inbox

**For mobile workflows:** See [ui-workflows.md](references/ui-workflows.md)

### Workspace Management

**Types:**
- Personal - Private space
- Team - Collaborative shared space
- Public - Read-only via Tana Publish

**Collaboration:**
- Roles: Owner, Editor, Viewer
- Real-time co-editing
- @mentions for notifications
- Edit history with attribution

**For workspace details:** See [ui-workflows.md](references/ui-workflows.md)

---

## AI Features

**Requirements:** Paid subscription

**Available Features:**
- **AI Chat:** Conversational AI with workspace context
- **AI Command Nodes:** Automate content generation, API calls, transcription
- **AI Agents:** Custom multi-step workflows
- **Meeting Notetaker:** Bot-free transcription (Google Meet, Zoom)
- **Mobile Voice:** Voice-to-text with AI enrichment
- **Autotag:** AI-powered tag suggestion

**Prompt Expressions:**
- `${name}` - Node title
- `${sys:context}` - All node data
- `${sys:content}` - Children only
- `${FieldName}` - Field value
- `${sys:currentDate}` - Today's date
- `${sys:nodeId}` - Unique ID

**For complete AI guide:** See [ai-features.md](references/ai-features.md)

---

## Common Workflows

### Create New Supertag

1. Create node with tag name
2. `Cmd/K` → "Convert to supertag"
3. Add fields: `Cmd/K` → "Add field to tag"
4. Configure template (optional)
5. Apply with `#tagname`

### Build Project Dashboard

1. Create project node with #project tag
2. Add fields (Status, Owner, Due Date, Priority)
3. Create child search nodes:
   - Incomplete Tasks: `is:todo, not:done, childOf:current`
   - Recent Updates: `edited:last 7`
4. Switch to Table or Cards view
5. Pin to sidebar

### Process Inbox with API

```bash
# Get inbox items
INBOX=$(mcporter call tana-local.search_nodes --args '{"query": {"childOf": {"nodeId": "INBOX_ID"}}}')

# Process each
for item in $INBOX; do
  # Read content
  CONTENT=$(mcporter call tana-local.read_node --args '{"nodeId": "'$item'"}')

  # AI categorize, tag, move (your logic)
done
```

**For detailed workflows:** See [ui-workflows.md](references/ui-workflows.md) and [api-workflows.md](references/api-workflows.md)

---

## Search & Filters

### Live Search

Create dynamic search nodes that auto-update:

**Via Command Line:**
1. `Cmd/K` → "Find nodes"
2. Build query with filters
3. Save as search node

**Common Queries:**
- My tasks: `hasType:TASK, is:todo, Owner:me`
- Overdue: `hasType:TASK, overdue:true`
- Recent notes: `created:last 14`
- Untagged: `not:has tag`

**For advanced search syntax:** See [views-and-search.md](references/views-and-search.md) and [api-workflows.md](references/api-workflows.md)

---

## Troubleshooting

### API/MCP Issues

**Connection Failed:**
1. Is Tana Desktop running?
2. Settings → Tana Labs → API enabled?
3. `curl http://localhost:8262/health`
4. Remove and re-add MCP config
5. Restart client

**Node Not Found:**
- IDs are workspace-specific
- Use `search_nodes` to find IDs
- Check correct workspace
- Node may be trashed

**Import Failed:**
- Check Tana Paste syntax (2 spaces per indent!)
- Verify tag/field IDs exist
- Test simpler paste first

### UI Issues

**Command Line Not Working:**
- Check `Cmd/K` not blocked by system
- Click node first
- Verify keyboard shortcuts in Settings

**Views Not Updating:**
- `Cmd/R` to refresh
- Check filter settings
- Clear filters to see all
- Reload page

**Sync Issues:**
- Check internet connection
- Force sync in Settings
- Desktop app more reliable than web

**Performance Slow:**
- Reduce search result limits
- Use filters to narrow data
- Desktop > Web for speed
- Clear browser cache

**For detailed troubleshooting:** See [best-practices.md](references/best-practices.md)

---

## Best Practices

### Data Organization
- Keep nodes atomic (one idea per node)
- Use supertags consistently
- Reference over duplicate
- Pin important fields

### Workflow Efficiency
- Keyboard-first approach
- Save common searches
- Template everything
- Batch similar tasks

### Hybrid UI/API
- UI for capture and review
- API for bulk operations
- Combine for maximum power
- See decision matrix in [best-practices.md](references/best-practices.md)

### Performance
- Desktop app faster than web
- Cache tag/field IDs in scripts
- Use filters to reduce result sets
- Archive old data regularly

**For comprehensive best practices:** See [best-practices.md](references/best-practices.md)

---

## Quick Reference Card

### When to Use What

| Task | Use | Shortcut/Command |
|------|-----|------------------|
| Quick capture | UI | `Cmd/Shift+D` then type |
| Bulk update | API | `search_nodes` + loop |
| Create structure | UI | `Cmd/K` + manual editing |
| Data analysis | API | `search_nodes` with filters |
| Visual organization | UI Views | Right-click → View as |
| Automation | API/AI | AI Command Nodes + scripts |
| Exploration | UI | `Cmd/S` global search |
| Repetitive tasks | API | `import_tana_paste` batch |

### Documentation Map

1. **Need API/MCP details?** → [api-workflows.md](references/api-workflows.md)
   - Tana Paste format
   - Search query syntax
   - MCP tools reference
   - API workflow examples

2. **Need UI guidance?** → [ui-workflows.md](references/ui-workflows.md)
   - UI workflows
   - Templates
   - Mobile app
   - Workspace management
   - Collaboration

3. **Need AI/automation help?** → [ai-features.md](references/ai-features.md)
   - AI Command Nodes
   - Prompt expressions
   - AI Agents
   - Voice features
   - Automation patterns

4. **Need views/search help?** → [views-and-search.md](references/views-and-search.md)
   - All 7 view types
   - View customization
   - Live search
   - Advanced search patterns

5. **Need strategic guidance?** → [best-practices.md](references/best-practices.md)
   - Organization principles
   - Performance optimization
   - Hybrid workflows
   - Migration strategies
   - Advanced patterns

---

## Getting Help

**Documentation:**
- https://tana.inc/docs (official docs)
- https://tana.inc/learn (learning center)
- https://tana.inc/templates (template store)

**Community:**
- Tana Slack community
- Tana Ideas (feature requests)
- YouTube tutorials

**This Skill:**
- Start with this overview
- Dive into reference files for details
- Use search to find specific topics
- Combine UI and API for power workflows
