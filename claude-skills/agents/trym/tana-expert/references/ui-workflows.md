# UI Workflows & Features

Complete guide to Tana's user interface features, templates, mobile app, and workspace management.

## Table of Contents
- [Common UI Workflows](#common-ui-workflows)
- [Tana Templates](#tana-templates)
- [Mobile App (Tana Capture)](#mobile-app-tana-capture)
- [Workspace Management](#workspace-management)
- [Collaboration Features](#collaboration-features)
- [Export & Import](#export--import)

---

## Common UI Workflows

### 1. Create a New Supertag from Scratch

**Steps:**
1. Create a node with desired tag name (e.g., "Book")
2. Use `Cmd/Ctrl+K` → "Convert to supertag"
3. Add fields via command line:
   - `Cmd/Ctrl+K` → "Add field to tag"
   - Choose field type (plain, options, date, etc.)
4. Configure template content (optional):
   - Add default fields with values
   - Include search nodes for dynamic lists
   - Add instructional content
5. Apply to nodes with `#Book`

**Example:**
- Create "Book" node
- Convert to supertag
- Add fields:
  - Author (plain text)
  - Rating (options: 1-5 stars)
  - Finished Date (date)
  - Genre (options: Fiction, Non-Fiction, etc.)
- Add template: "Notes::" section
- Tag any book note with `#Book`

### 2. Build a Project Dashboard

**Steps:**
1. Create project node
2. Add `#project` supertag
3. Add fields:
   - Status (options)
   - Start Date (date)
   - Owner (options from #person)
   - Priority (options)
4. Create child search nodes:
   - "Incomplete Tasks": `Cmd/K` → "Find nodes"
     - Filter: `is: todo`, `not: done`, `childOf: current`
   - "Recent Updates": Filter `edited: last 7`
   - "Team Members": Filter by #person tag
5. Switch view to Table or Cards
6. Pin project to sidebar for quick access (`Cmd/K` → "Pin node")

### 3. Set Up Meeting Note Template

**Via Supertag Configuration:**
1. Create `#meeting` supertag
2. Add fields:
   - Date (date type)
   - Attendees (options from #person)
   - Status (options: Scheduled, Completed, Cancelled)
   - Duration (number)
   - Meeting Type (options: Standup, Planning, Review, etc.)
3. Add template content (will auto-populate):
   ```
   - Agenda::
   - Notes::
   - Action Items::
     - [ ]
   - Decisions::
   - Follow-up::
   ```
4. Enable "Meeting" base type for AI transcription support
5. Configure event trigger (optional): When #meeting added, set Date to current date
6. Apply `#meeting` to any meeting note

### 4. Create a CRM System

**Setup Supertags:**

**Company Tag (`#company`):**
- Fields:
  - Industry (options)
  - Website (url)
  - Status (options: Lead, Customer, Partner, Inactive)
  - Size (options: Startup, SMB, Enterprise)
  - Primary Contact (options from #person)

**Person Tag (`#person`):**
- Fields:
  - Company (options from #company)
  - Email (email)
  - Phone (plain text)
  - Role (plain text)
  - LinkedIn (url)

**Interaction Tag (`#interaction`):**
- Fields:
  - Date (date)
  - Type (options: Call, Email, Meeting, Demo)
  - Person (options from #person)
  - Company (options from #company)
  - Outcome (options)

**Create Workspace Structure:**
1. Create workspace node "CRM"
2. Add search nodes:
   - "Active Customers": Filter `#company`, `Status:: Customer`
   - "Recent Interactions": Filter `#interaction`, `created: last 30`
   - "Follow-ups Needed": Custom filter for interaction outcomes
3. Use Table view with columns for key fields
4. Pin CRM workspace to sidebar

### 5. Daily Review Routine

**Morning Routine:**
1. `Cmd/Ctrl+Shift+D` to jump to today's note
2. Review calendar integration for scheduled items
3. Check pinned tasks in sidebar
4. Use command line search: "Find nodes" → `is: todo`, `onDate: today`
5. Prioritize tasks (drag to reorder or set Priority field)
6. Review yesterday's uncompleted items

**Evening Routine:**
1. Tag today's wins with `#win`
2. Move incomplete tasks:
   - `Cmd/K` → "Remind me" → Tomorrow
3. Add reflection notes to daily note
4. Review completed items: Search `done: last 1`
5. Plan tomorrow's top 3 priorities

### 6. Set Up Smart Filters & Searches

**Task Management Searches:**

Create search nodes for common queries:

**Overdue Tasks:**
```
Find nodes:
- is: todo
- overdue: true
- not: done
```

**This Week's Tasks:**
```
Find nodes:
- is: todo
- created: last 7
```

**By Project:**
```
Find nodes:
- is: todo
- childOf: [Project Node]
- recursive: true
```

**High Priority:**
```
Find nodes:
- is: todo
- Priority:: High
```

**Content Discovery:**

**Recent Articles:**
```
Find nodes:
- hasType: #article
- created: last 30
```

**Untagged Notes:**
```
Find nodes:
- not: has tag
- created: last 7
```

**Save searches:**
- Pin to sidebar for quick access
- Add to project dashboards
- Include in daily note template

### 7. Template-Based Workflows

**Daily Note Template:**
1. Create template supertag `#daily-template`
2. Add template content:
   ```
   - Morning Pages::
   - Top 3 Priorities::
     - [ ]
     - [ ]
     - [ ]
   - Meetings::
   - Notes::
   - Grateful For::
   - Tomorrow::
   ```
3. Set as default for day nodes (configure in calendar settings)

**Project Kickoff Template:**
1. Create `#project-kickoff` supertag
2. Template:
   ```
   - Project Overview::
   - Goals::
   - Success Criteria::
   - Stakeholders::
   - Timeline::
   - Risks::
   - Resources Needed::
   - Next Steps::
     - [ ]
   ```

### 8. Dynamic Title Expressions

Build dynamic titles from field values using `${field}` syntax in supertag configuration.

**Basic Examples:**

**Meeting Titles:**
```
Title expression: ${Date} - ${Type}
Fields:
- Date (date field)
- Type (options: Standup, Planning, Review)

Result: "2026-02-04 - Standup"
```

**Task Titles:**
```
Title expression: [${Priority}] ${Project} - ${sys:content}
Fields:
- Priority (options: P0, P1, P2)
- Project (options from #project)

Result: "[P0] Alpha Launch - Fix critical bug"
```

**Person Titles:**
```
Title expression: ${First Name} ${Last Name} (${Company})
Fields:
- First Name (plain)
- Last Name (plain)
- Company (options from #company)

Result: "John Smith (Acme Corp)"
```

**Advanced Examples:**

**Event Titles with Conditional:**
```
Title expression: ${Start Date} ${Event Type}${Speaker ? " with " + Speaker : ""}
Fields:
- Start Date (date)
- Event Type (options)
- Speaker (options from #person, optional)

Results:
- "2026-02-15 Workshop with Sarah Jones"
- "2026-02-20 Conference" (no speaker)
```

**Article/Book Titles:**
```
Title expression: ${Title} - ${Author} (${Year})
Fields:
- Title (plain)
- Author (plain)
- Year (number)

Result: "Thinking, Fast and Slow - Kahneman (2011)"
```

**Project Status Titles:**
```
Title expression: ${Name} [${Status}] ${Progress}%
Fields:
- Name (plain)
- Status (options: Active, On Hold, Complete)
- Progress (number, 0-100)

Result: "Website Redesign [Active] 65%"
```

**System Field Examples:**

Available system fields in title expressions:
- `${sys:owner}` - Node owner
- `${sys:createdAt}` - Creation date
- `${sys:editedAt}` - Last edit date
- `${sys:createdBy}` - Creator name

**With System Fields:**
```
Title expression: ${Topic} by ${sys:createdBy} on ${sys:createdAt}
Result: "API Integration by Alice on 2026-02-04"
```

**Formatting Options:**

**Character Limits:**
```
Title expression: ${Description:50}...
Result: Truncates Description field to 50 characters with "..."
```

**Date Formatting:**
```
Title expression: ${Due Date:YYYY-MM-DD} - ${Task Name}
Result: "2026-02-15 - Deploy to production"
```

**Uppercase/Lowercase:**
```
Title expression: ${Project:upper} - ${sys:content:lower}
Result: "ALPHA LAUNCH - fix critical bug"
```

**Practical Use Cases:**

1. **Meeting Notes Auto-Naming:**
   - Expression: `${Date} ${Attendees} Meeting`
   - Auto-generates: "2026-02-04 Alice, Bob, Carol Meeting"

2. **Task Identifiers:**
   - Expression: `${Project:upper}-${sys:nodeId:8}`
   - Auto-generates: "LAUNCH-a3b5c7d9" (project + short ID)

3. **Journal Entries:**
   - Expression: `${sys:createdAt:YYYY-MM-DD} Journal - ${Mood}`
   - Auto-generates: "2026-02-04 Journal - Energized"

4. **Versioned Documents:**
   - Expression: `${Doc Name} v${Version} (${sys:editedAt:YYYY-MM-DD})`
   - Auto-generates: "API Spec v2.1 (2026-02-04)"

**Setup in UI:**
1. Open supertag configuration
2. Scroll to "Title expression"
3. Enter expression with `${field name}` placeholders
4. Test with sample node
5. Adjust formatting as needed

**Important Notes:**
- Title expressions only work in UI configuration (not via API)
- Changes apply to new nodes with the tag
- Existing nodes keep their titles unless refreshed
- Use sparingly for frequently-edited fields (can cause confusion)

---

## Tana Templates

Pre-built supertags, workflows, and systems from the Tana community and official store.

### What Are Templates?

Templates are pre-configured supertags, fields, commands, and views that you can install into your workspace. They help you:
- Get started quickly with proven workflows
- Discover Tana capabilities
- Learn from community best practices
- Go from idea to structure without building from scratch

### How to Browse and Install

**Desktop/Web App:**
1. Click "Supertags" in sidebar
2. Click "Browse templates" button (right side)
3. Browse available templates by category
4. Click tile to preview
5. Select workspace (if multiple)
6. Click "Install"
7. Installation node opens with "Get started" instructions

**Mobile:**
- Visit https://tana.inc/templates
- Start installation from website
- Opens in mobile app for completion

### Template Categories

Available templates include:
- **Productivity**: Task management, GTD, weekly reviews
- **Note-taking**: Zettelkasten, PARA, Book notes
- **Project Management**: Agile, Kanban, roadmaps
- **Personal**: Journaling, habit tracking, goals
- **Knowledge Management**: Research, learning, PKM systems
- **Business**: CRM, meeting notes, OKRs

**Popular Templates:**
- Weekly Reflection with voice memo transcription
- Task Management Systems
- PARA organization method
- Zettelkasten note-taking
- Meeting Notes with AI summaries

### After Installation

**Template installations:**
- Copy all configuration into your workspace
- No connection to original after install
- Full freedom to modify and customize
- Currently no way to update templates (full copy only)

**Best Practices:**
- Read "Get started" instructions thoroughly
- Customize to fit your workflow
- Don't install too many at once
- Test on sample data first
- Combine templates for hybrid systems

---

## Mobile App (Tana Capture)

Seamless capture on iOS and Android with voice, text, media, and offline support.

### Platform Availability

- **iOS**: Available (released Nov 2024)
- **Android**: Available (released Feb 2025)
- Download from App Store / Google Play

### Key Features

**Text Capture:**
- Quick note entry
- Task creation with checkboxes
- Auto-sync to desktop/web

**Voice Recording:**
- Interview and meeting capture
- 91 language transcription
- AI enrichment with entities
- Automatic field filling based on supertag
- Rewrite feature for transcript transformation

**Media Sharing:**
- Share links from web/apps
- Take photos or videos
- Send directly to inbox
- Text scanning (OCR):
  - Physical documents
  - Business cards
  - Receipts
  - Signs and notes

**Offline Capability:**
- Works without internet
- Syncs when connection restored
- Local voice recording
- Transcription when online

### Inbox Integration

**How it Works:**
1. Capture content in mobile app
2. Content appears in Inbox (new section in sidebar)
3. Voice memos sent to current daily note via Inbox
4. Instant transcription and entity enrichment
5. Process inbox items:
   - Tag with appropriate supertags
   - Move to relevant projects
   - Set fields and values
   - Archive or trash

**Inbox Workflow:**
```
Mobile Capture → Inbox → Process → Organize
```

**Processing Inbox:**
1. Review new items daily
2. Apply tags: `#task`, `#note`, `#idea`, etc.
3. Set fields (due dates, assignees, etc.)
4. Move to projects or areas
5. Clear inbox regularly

### Voice Memo Best Practices

**Before Recording:**
- Select target supertag (e.g., #meeting, #idea)
- Ensure quiet environment for better transcription
- Know which fields you want auto-filled

**During Recording:**
- Speak clearly and at normal pace
- Mention key entities (people, projects, dates)
- Use natural language ("Meeting with John about Project Alpha")

**After Transcription:**
- Review transcript for accuracy
- Use Rewrite feature to format
- Extract action items
- Tag related nodes
- Add to daily note or project

**Example Voice Memo:**
"Meeting with Sarah about the Q1 launch. We discussed the timeline and she's concerned about the API integration. Action item: schedule technical review by Friday. Status is blocked."

Auto-fills:
- Attendees:: Sarah
- Project:: Q1 Launch
- Action Items:: Schedule technical review
- Due:: This Friday
- Status:: Blocked

---

## Workspace Management

Organize work across multiple contexts with workspace features.

### What Are Workspaces?

Workspaces are separate containers for big projects and collaborative efforts:
- Distinct knowledge graphs
- Separate from personal workspace
- Shared with team members
- Custom permissions and roles

### Creating Workspaces

1. Click Workspaces in sidebar
2. Click "Create workspace"
3. Name the workspace
4. Choose visibility (Private or Shared)
5. Invite members (optional)

### Workspace Types

**Personal Workspace:**
- Your private space
- Default for all captures
- Personal notes and tasks
- Private projects

**Team Workspaces:**
- Shared collaboration space
- Team projects and docs
- Shared knowledge base
- Real-time co-editing

**Public Workspaces:**
- Read-only sharing via Tana Publish
- Documentation sites
- Knowledge bases
- Marketing content

### Managing Workspaces

**Switching:**
- Click workspace name in sidebar
- Recent workspaces listed
- Reorder in settings

**Settings:**
- Members and permissions
- Default supertags and fields
- View preferences
- Export options

**Navigation:**
- Each workspace has own:
  - Library
  - Home
  - Calendar
  - Inbox (personal)
  - Supertags

### Moving Content Between Workspaces

**Manual Method:**
1. Select node
2. `Cmd/Ctrl+K` → "Move to"
3. Choose destination workspace
4. Node and children move (references preserved)

**API Method:**
```bash
# Read from one workspace
mcporter call tana-local.read_node --args '{"nodeId": "NODE_ID"}'

# Import to another workspace (switch workspace first)
mcporter call tana-local.import_tana_paste --args '{
  "tanaPaste": "[content from read]"
}'
```

### Workspace Organization Strategies

**By Context:**
- Personal (home, life, personal projects)
- Work (job-related)
- Side Projects
- Learning & Research

**By Team:**
- Engineering workspace
- Marketing workspace
- Product workspace
- Company-wide workspace

**By Project:**
- Each major project gets workspace
- Temporary workspaces for initiatives
- Archive when complete

---

## Collaboration Features

Real-time co-creation and team workflows.

### Adding Members

1. Open workspace settings
2. Click "Members"
3. Enter email address
4. Select role (Owner, Editor, Viewer)
5. Send invitation

### Roles & Permissions

| Role | Permissions |
|------|-------------|
| **Owner** | Full control, delete workspace, manage members |
| **Editor** | Create, edit, delete content, cannot manage members |
| **Viewer** | Read-only access, can comment |

### Real-Time Collaboration

**Features:**
- Live cursors show who's editing
- Instant updates across all users
- Edit history with user attribution
- Conflict resolution automatic

**Best Practices:**
- Communicate via comments
- Use @mentions for notifications
- Establish supertag standards
- Define field naming conventions
- Regular team sync on structure

### Notifications

**User Mentions:**
- Type `@` + team member name
- Sends notification to that user
- Appears in their notifications panel

**Viewing Notifications:**
- Notifications icon in sidebar
- Shows recent mentions and updates
- Click to jump to referenced node

### Edit History

**View History:**
- Right-click node
- "View history"
- See timeline of changes
- User attribution
- Revert to previous version (limited)

### Comments (Coming Soon)

Planned feature for inline discussions and feedback.

### Workspace Best Practices

**Establish Standards:**
- Supertag naming conventions
- Field standardization across tags
- Folder/hierarchy structure
- Tagging guidelines

**Documentation:**
- Create workspace guide node
- Pin to sidebar
- Include:
  - Supertag definitions
  - Workflow instructions
  - Team conventions
  - FAQ

**Regular Maintenance:**
- Archive completed projects
- Clean up duplicate tags
- Consolidate related nodes
- Review and update search nodes

---

## Export & Import

Move data in and out of Tana with various formats.

### Export Options

**Copy-Paste:**
- Select nodes
- `Cmd/Ctrl+C`
- Paste into other apps (formatted or plain text)
- Preserves hierarchy and formatting

**Export Workspace:**
1. Workspace settings
2. "Export"
3. Choose format:
   - **Markdown** - Hierarchical .md files
   - **JSON** - Complete data structure
   - **Tana Paste** - For reimport

**What Gets Exported:**
- All nodes and content
- Supertag definitions
- Field schemas
- References (as links or IDs)
- Date stamps
- User metadata

### Import Data

**From Other Tools:**
1. `Cmd/K` → "Import"
2. Choose source:
   - Roam Research
   - Notion
   - Obsidian
   - Evernote
   - Plain text / Markdown
   - CSV
3. Map fields to Tana structure
4. Review and confirm
5. Import creates nodes with hierarchy

**Tana Paste Format:**
- Universal clipboard format
- Preserves all structure
- Use for bulk operations
- API: `import_tana_paste` tool

### Migration Strategies

**From Notion:**
1. Export Notion workspace as Markdown
2. Import via Tana import tool
3. Map databases to supertags
4. Review and adjust field types
5. Recreate views and filters

**From Roam:**
1. Export as JSON
2. Import via Tana
3. Daily notes map to Tana daily notes
4. Pages become nodes
5. Tags and attributes map to supertags/fields

**From Obsidian:**
1. Export vault as Markdown
2. Import folder by folder
3. Wikilinks convert to references
4. Frontmatter maps to fields
5. Tags convert to Tana tags

### Backup Strategies

**Regular Exports:**
- Weekly full workspace export (JSON)
- Store in cloud backup (Dropbox, Google Drive)
- Version control for critical data

**Critical Data:**
- Export specific projects before major changes
- Keep local copies of important meeting notes
- Archive completed project workspaces

**Note:** Tana handles server-side backups, but local exports provide extra safety.
