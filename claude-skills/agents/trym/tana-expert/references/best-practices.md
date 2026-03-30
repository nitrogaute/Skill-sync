# Best Practices & Advanced Patterns

Strategic guidance for effective Tana usage, optimization, and hybrid workflows.

## Table of Contents
- [Data Organization](#data-organization)
- [Workflow Efficiency](#workflow-efficiency)
- [Hybrid UI/API Workflows](#hybrid-uiapi-workflows)
- [Performance Optimization](#performance-optimization)
- [Security & Privacy](#security--privacy)
- [Advanced Patterns](#advanced-patterns)
- [Migration Strategies](#migration-strategies)

---

## Data Organization

Fundamental principles for organizing information in Tana.

### Keep Nodes Atomic

**Principle:** One idea per node.

**Why:**
- References become more useful
- Search results more precise
- Easier to reorganize
- Better reusability
- Clearer connections

**Good Example:**
```
- Meeting with Sarah #meeting
  - Date:: [[date:2026-02-04]]
  - Discussed API integration timeline
  - Decision: Move deadline to Feb 15
  - Action: [[Schedule technical review]]
```

**Bad Example:**
```
- Meeting with Sarah about API integration where we discussed the timeline and decided to move the deadline to Feb 15 and I need to schedule a technical review
```

**Rule of Thumb:**
- If you'd want to reference it separately, make it a separate node
- Keep node names concise (details go in children)
- Use fields for attributes, children for related content

### Use Supertags Consistently

**Establish Schema Early:**
- Define core supertags before bulk data entry
- Document field meanings
- Share conventions with team
- Pin important fields

**Apply Tags Liberally:**
- Tag as you create, not later
- Use multiple tags when appropriate
- Don't over-categorize (avoid tag proliferation)
- Archive unused tags

**Leverage Inheritance:**
```
#task (base)
├── #work-task (extends #task)
│   └── Adds: Client field
├── #personal-task (extends #task)
│   └── Adds: Energy level field
└── #recurring-task (extends #task)
    └── Adds: Frequency field
```

**Pin Important Fields:**
- Makes filtering faster
- Appears in filter toolbar
- Signals importance to team
- Reduces cognitive load

### Reference Over Duplicate

**Why Reference:**
- Single source of truth
- Updates propagate everywhere
- Maintains connections
- Saves space
- Shows relationships

**When to Reference:**
```
Meeting notes → Reference attendees
Project → Reference team members
Task → Reference related projects
Article → Reference authors
```

**When to Duplicate:**
- Templates (intentional copies)
- Archival snapshots
- External data imports (no source to reference)

**Best Practices:**
- Copy references (`Cmd/Ctrl+C`), not content
- Use `@mentions` for inline references
- Create bidirectional links via fields
- Check references section to see what links to a node

### Hierarchy vs. Tags vs. Fields

**Hierarchy (Parent/Child):**
- Belongs to / part of relationships
- Ownership and containment
- Default organization

**Tags (Supertags):**
- Type/category
- Cross-cutting classifications
- Enables database-like queries

**Fields:**
- Attributes and metadata
- Structured data
- For filtering and sorting

**Example:**
```
Project Alpha (hierarchy: belongs to Projects)
#project (tag: is a project type)
Status:: In Progress (field: attribute)
Owner:: Alice (field: relationship via reference)
```

**Decision Matrix:**

| Need | Solution |
|------|----------|
| "This is a type of X" | Supertag |
| "This belongs to X" | Parent/child hierarchy |
| "This has property X" | Field |
| "This is related to X" | Reference in field or child |

---

## Workflow Efficiency

Practices for faster, smoother Tana usage.

### Keyboard-First Approach

**Master These:**
- `Cmd/Ctrl+K` - Command line (most important!)
- `Cmd/Ctrl+S` - Global search
- `Cmd/Ctrl+Shift+D` - Today's note
- `Tab` / `Shift+Tab` - Indent/outdent
- `@` - Quick reference
- `#` - Quick tag

**Create Custom Shortcuts:**
1. `Cmd/K` to open command line
2. Find command
3. `Cmd/Shift+K` to record shortcut
4. Examples:
   - `Cmd+Shift+T` for "Find nodes → is:todo"
   - `Cmd+Shift+M` for "Move to"
   - `Cmd+Shift+P` for specific project search

**Avoid Mouse:**
- Navigate with arrows
- Select with Shift+arrows
- Expand/collapse with Cmd+arrows
- Use command line instead of menus

### Search Smarter

**Save Common Searches:**
- Pin to sidebar
- Add to daily note template
- Include in project dashboards

**Build Search Library:**
```
Searches workspace
├── Tasks
│   ├── My Tasks (owner = me, is:todo)
│   ├── Overdue (overdue:true)
│   ├── This Week (created:last 7)
│   └── High Priority (Priority:High, is:todo)
├── Content
│   ├── Recent Notes (created:last 14, not:has:tag)
│   ├── Unprocessed Inbox (childOf:Inbox)
│   └── Needs Review (Status:Draft)
└── People
    ├── Active Contacts (hasType:PERSON, linksTo:last 30)
    └── Team (hasType:PERSON, Company:Acme)
```

**Combine Filters:**
- Use AND logic for specificity
- Create search nodes for OR logic
- Nest searches for complex queries

**Search Workflow:**
1. Start broad
2. Add filters incrementally
3. Save when useful
4. Refine over time

### Template Everything

**Common Templates:**
- Daily note (morning pages, priorities, review)
- Meeting note (agenda, attendees, action items)
- Project kickoff (goals, team, timeline, risks)
- Weekly review (wins, challenges, learnings, next week)
- Decision log (context, options, decision, outcome)
- 1:1 meeting (previous notes, agenda, discussion, action items)

**Template Strategy:**
- Start with basic structure
- Evolve based on actual use
- Don't over-engineer
- Make optional sections clear
- Use search nodes for dynamic content

**Template Distribution:**
- Supertag templates (auto-apply)
- Workspace template library
- Share via Tana Paste
- Team documentation

### Batch Operations

**Group Similar Tasks:**
- Process inbox in batch
- Tag multiple nodes at once
- Bulk field updates
- Weekly planning sessions

**Use API for Bulk:**
```bash
# Tag all untagged inbox items
INBOX_ITEMS=$(search_nodes --query '{"childOf": "INBOX_ID", "not": {"has": "tag"}}')
for item in $INBOX_ITEMS; do
  tag --nodeId $item --tagId "NOTE_TAG_ID"
done
```

**Avoid Context Switching:**
- Dedicated capture time
- Dedicated processing time
- Dedicated review time
- Batch similar work

---

## Hybrid UI/API Workflows

Combine manual and automated approaches for maximum effectiveness.

### When to Use UI vs. API

| Task | Best Method | Reason |
|------|-------------|--------|
| Quick capture | UI | Faster, mobile-friendly |
| Bulk updates | API | Scriptable, consistent |
| Visual organization | UI | Drag-drop, immediate feedback |
| Data analysis | API | Structured queries, programmatic |
| Complex filters | API | Boolean logic, precision |
| Browse/explore | UI | Better UX, serendipity |
| Automation | API | Event-driven, reliable |
| Schema design | UI | Visual feedback, iteration |
| Template setup | UI | WYSIWYG, testing |
| Batch import | API | Tana Paste format, bulk |

### Pattern 1: Capture → Process → Organize

**UI Capture:**
- Mobile voice memos
- Quick text notes
- Web clipper
- Manual entry

**API Processing:**
```bash
# Daily automation: Process inbox
INBOX=$(search_nodes --query '{"childOf": "INBOX_ID"}')

for node in $INBOX; do
  # AI categorize
  CATEGORY=$(ai_categorize $node)

  # Tag appropriately
  tag --nodeId $node --tagId $CATEGORY

  # Extract metadata
  extract_fields $node

  # Move to destination
  move_node $node $DESTINATION
done
```

**UI Review:**
- Verify AI categorization
- Adjust tags and fields
- Add context and notes
- Connect related nodes

### Pattern 2: Bulk Operations with Review

**API Bulk Update:**
```bash
# Update all completed tasks
COMPLETED=$(search_nodes --query '{"is": "done", "Status": {"not": "Completed"}}')

for task in $COMPLETED; do
  set_field_option --nodeId $task --fieldId "STATUS_ID" --value "Completed"
  set_field_content --nodeId $task --fieldId "COMPLETED_DATE_ID" --content "[[date:2026-02-04]]"
done
```

**UI Spot Check:**
- Review sample of updated nodes
- Verify field values correct
- Check for edge cases
- Fix any errors

### Pattern 3: Hybrid Dashboards

**UI Setup:**
- Create project structure
- Define supertags and fields
- Configure views
- Pin to sidebar

**API Population:**
```bash
# Daily update: Populate metrics
PROJECT_TASKS=$(search_nodes --query '{"childOf": "PROJECT_ID", "hasType": "TASK"}')

TOTAL=$(count $PROJECT_TASKS)
COMPLETED=$(count_where $PROJECT_TASKS "is:done")
IN_PROGRESS=$(count_where $PROJECT_TASKS "Status:In Progress")
BLOCKED=$(count_where $PROJECT_TASKS "Status:Blocked")

# Update dashboard fields
set_field_content --nodeId "PROJECT_ID" --fieldId "TOTAL_TASKS" --content "$TOTAL"
set_field_content --nodeId "PROJECT_ID" --fieldId "COMPLETED" --content "$COMPLETED"
# ... etc
```

**UI Consumption:**
- View dashboard in UI
- Drill into details
- Take action on issues
- Update plans

### Pattern 4: Voice → AI → Review

**Voice Capture (Mobile):**
- Record meeting notes
- Capture ideas while walking
- Quick task creation

**AI Processing (Automatic):**
- Transcription (automatic)
- Entity extraction
- Field population
- Tag suggestion

**API Enhancement (Scheduled):**
```bash
# Process voice memos
VOICE_MEMOS=$(search_nodes --query '{"hasType": "VOICE_MEMO", "processed": false}')

for memo in $VOICE_MEMOS; do
  # AI extract action items
  ACTIONS=$(ai_extract_actions $memo)

  # Create task nodes
  for action in $ACTIONS; do
    create_task "$action" --parent $memo
  done

  # Mark processed
  set_field_content --nodeId $memo --fieldId "PROCESSED" --content "true"
done
```

**UI Review (Daily):**
- Review transcripts
- Verify action items
- Add context
- Link to projects

---

## Performance Optimization

Strategies for maintaining speed and responsiveness.

### For Large Workspaces

**Search Optimization:**
- Use specific queries vs. browsing
- Set reasonable result limits (100-500)
- Filter by date when possible
- Use tag filters before text search

**Hierarchy Management:**
- Don't nest more than 5-7 levels deep
- Use references instead of deep nesting
- Archive old data to separate workspace
- Break up mega-nodes (>100 children)

**View Configuration:**
- Set lower page sizes for large tables
- Use filters to reduce result sets
- Group sparingly in very large views
- Hide unnecessary display fields

**UI Performance:**
- Desktop app > Web app
- Close unnecessary browser tabs
- Reduce number of open panels
- Pin frequently-used nodes vs. searching

### For API Usage

**Batch Operations:**
```bash
# Good: Batch tag creation
TAGS=("tag1" "tag2" "tag3" "tag4")
for tag in ${TAGS[@]}; do
  create_tag --name "$tag" &
done
wait

# Bad: Sequential with delays
create_tag --name "tag1"
create_tag --name "tag2"
# ... slow
```

**Cache IDs:**
```bash
# Get tag IDs once, reuse
TASK_TAG_ID=$(list_tags | grep "task" | get_id)

# Use cached ID in loop
for node in $NODES; do
  tag --nodeId $node --tagId $TASK_TAG_ID
done
```

**Efficient Queries:**
```bash
# Good: Search by ID when known
read_node --nodeId "KNOWN_ID"

# Bad: Text search every time
search_nodes --query '{"textContains": "unique name"}'
```

**Pagination:**
```bash
# For large result sets
OFFSET=0
PAGE_SIZE=100

while true; do
  RESULTS=$(search_nodes --query "$QUERY" --limit $PAGE_SIZE --offset $OFFSET)

  if [ -z "$RESULTS" ]; then
    break
  fi

  process_results $RESULTS
  OFFSET=$((OFFSET + PAGE_SIZE))
done
```

### Workspace Hygiene

**Regular Cleanup:**
- Weekly: Clear inbox
- Monthly: Archive completed projects
- Quarterly: Review and merge duplicate tags
- Yearly: Export and archive old data

**Tag Management:**
- Consolidate similar tags
- Delete unused tags (check usage first)
- Standardize naming conventions
- Document tag purposes

**Search Node Maintenance:**
- Remove obsolete searches
- Update filters as schema changes
- Consolidate similar searches
- Document search purposes

---

## Security & Privacy

Protecting your data and managing access.

### API Security

**Local API Characteristics:**
- Only accessible when desktop app running
- Localhost only (no remote access)
- Each client requires authorization
- Authorization via desktop modal + browser

**Best Practices:**
- Review connected clients regularly (Settings → API)
- Revoke unused client connections
- Don't share API tokens
- Close desktop app when not in use (to disable API)

**In Alpha:**
- Backup workspace regularly
- Test on copies before bulk operations
- Version control for critical data
- Export before major API scripts

### Data Safety

**Regular Exports:**
- Weekly full workspace export (JSON)
- Store in cloud backup (Dropbox, Google Drive, OneDrive)
- Keep local copies of critical data
- Version exports by date

**Pre-Operation Backups:**
```bash
# Before major API operations
export_workspace > backup-$(date +%Y%m%d).json

# Run operation
bulk_operation

# Verify success
verify_results

# If error, import from backup
```

**Critical Data Protection:**
- Export specific projects before major changes
- Keep offline copies of important meeting notes
- Archive completed project workspaces
- Use trash_node instead of permanent deletion

### Workspace Privacy

**Private Workspaces:**
- Encrypted member-only access
- Full access control
- Content invisible to non-members
- Separate workspaces for different security levels

**Shared Workspaces:**
- Review member list regularly
- Use appropriate roles (Owner, Editor, Viewer)
- Establish data sharing policies
- Train team on security practices

**Public Sharing (Tana Publish):**
- Review visibility settings carefully
- Password-protect sensitive pages (paid feature)
- Regularly audit published content
- Unpublish when no longer needed

**Data Handling:**
- Don't put credentials in Tana
- Avoid PII in public workspaces
- Use references instead of copying sensitive data
- Follow company data policies

---

## Advanced Patterns

Sophisticated organizational strategies.

### Multi-Level Hierarchies

**Project Structure:**
```
Project Alpha #project
├── Overview
│   ├── Goals
│   ├── Success Criteria
│   └── Timeline
├── Workstreams
│   ├── Backend #workstream
│   │   ├── Tasks
│   │   │   %%search%%: is:todo, childOf:BACKEND_ID
│   │   └── Docs
│   ├── Frontend #workstream
│   │   ├── Tasks
│   │   │   %%search%%: is:todo, childOf:FRONTEND_ID
│   │   └── Docs
│   └── QA #workstream
│       └── (similar structure)
├── Team
│   %%search%%: hasType:PERSON, linksTo:PROJECT_ID
└── All Tasks
    %%search%%: is:todo, childOf:PROJECT_ID, recursive:true
```

**Benefits:**
- Clear organization
- Dynamic aggregation
- Easy navigation
- Scalable structure

### Field Inheritance

**Concept:** Child nodes inherit field values from ancestors.

**Setup (UI):**
1. Configure field on supertag
2. Set "Auto-initialize from ancestor with supertag"
3. Children automatically get parent's value

**Example:**
```
Project Alpha
└── Status:: In Progress

  └── Task 1 #task
      └── Status:: In Progress (inherited)

  └── Task 2 #task
      └── Status:: In Progress (inherited)
```

**Use Cases:**
- Project → Tasks (inherit project reference)
- Epic → Stories (inherit epic priority)
- Area → Notes (inherit area tags)
- Client → Projects (inherit client reference)

**Benefits:**
- Consistency across hierarchy
- Less manual entry
- Update parent to update children
- Maintains relationships

### Dynamic Collections

**Principle:** Use live search instead of manual lists.

**Traditional (Manual):**
```
High Priority Tasks
├── Task A (manually added)
├── Task B (manually added)
└── Task C (manually added)
```

**Dynamic (Search):**
```
High Priority Tasks
%%search%%
  - hasType: TASK
  - Priority:: High
  - is: todo

(automatically includes all matching, updates in real-time)
```

**Benefits:**
- Always current
- No manual maintenance
- Scales infinitely
- Combines with grouping/sorting

**Advanced:**
```
Project Dashboard
├── Urgent & Important
│   %%search%%: Priority:High, Due:next 3
├── Important Not Urgent
│   %%search%%: Priority:High, Due:after 3 days
├── Urgent Not Important
│   %%search%%: Priority:Medium, Due:next 3
└── Neither
    %%search%%: Priority:Low
```

### Cross-Workspace Workflows

**Use Case:** Personal capture, team collaboration.

**Setup:**
- Personal workspace for all capture
- Team workspace for shared work

**Workflow:**
```
Personal Workspace:
- Quick capture to inbox
- Daily notes
- Personal projects
- Learning notes

↓ Move relevant items ↓

Team Workspace:
- Shared projects
- Team meetings
- Collaborative docs
- Knowledge base
```

**Manual Move:**
1. Tag for team workspace
2. Use "Move to" command
3. Select team workspace
4. References preserved

**API Automation:**
```bash
# Daily: Move tagged items
TEAM_ITEMS=$(search_nodes --query '{"has": "tag", "textContains": "#share-with-team"}')

for item in $TEAM_ITEMS; do
  # Export from personal
  CONTENT=$(read_node --nodeId $item)

  # Import to team workspace (switch context)
  import_tana_paste --workspace "Team" --tanaPaste "$CONTENT"

  # Archive in personal
  tag --nodeId $item --tagId "MOVED_TAG"
done
```

### Zettelkasten in Tana

**Principles:**
- Atomic notes (one idea per node)
- Permanent notes tagged #zettel
- Heavy linking between related ideas
- Index nodes for entry points

**Structure:**
```
Zettelkasten
├── Inbox (temporary notes)
├── Permanent Notes
│   ├── Note 1 #zettel
│   │   ├── Related:: [[Note 5]], [[Note 12]]
│   │   └── Tags:: #concept, #framework
│   └── Note 2 #zettel
│       └── Builds on:: [[Note 1]]
├── Index
│   ├── Concepts
│   │   %%search%%: hasType:zettel, textContains:concept
│   └── Frameworks
│       %%search%%: hasType:zettel, textContains:framework
└── MOC (Maps of Content)
    ├── Productivity MOC
    │   - Manual curation of related zettels
    └── Learning MOC
```

**Benefits in Tana:**
- Bidirectional links automatic
- Search for connections
- Views for different perspectives
- Fields for metadata

---

## Migration Strategies

Moving to or from Tana effectively.

### Migrating TO Tana

**From Notion:**
1. Export Notion workspace as Markdown + CSV
2. Import via Tana → Import tool
3. Map Notion databases to Tana supertags:
   - Database = Supertag
   - Properties = Fields
   - Views = Tana views
4. Recreate relations as "options from supertag" fields
5. Rebuild formulas with search nodes + views
6. Test and iterate

**From Roam Research:**
1. Export as JSON or EDN
2. Import via Tana
3. Daily notes map 1:1
4. Pages become nodes
5. Tags become supertags
6. Attributes become fields
7. Block references become node references

**From Obsidian:**
1. Export vault (already Markdown files)
2. Import folder by folder
3. Wikilinks convert to Tana references
4. Frontmatter YAML becomes fields
5. Tags convert to Tana supertags
6. Folder structure flattens (use tags instead)

**From Evernote:**
1. Export notebooks as ENEX
2. Convert to Markdown (using tools)
3. Import to Tana
4. Notebooks become workspace sections
5. Tags become Tana tags
6. Review and restructure

### Migration Best Practices

**Plan Before Importing:**
- Map old structure to Tana concepts
- Design supertag schema first
- Decide on hierarchy vs. tags
- Plan field types and names

**Import in Phases:**
- Start with small section
- Test structure
- Refine and adjust
- Then import bulk

**Clean As You Go:**
- Don't import everything (curate)
- Restructure during migration
- Remove duplicates
- Update outdated info

**Post-Migration:**
- Set up search nodes
- Create templates
- Configure views
- Train team on new structure

### Exporting FROM Tana

**Full Workspace:**
1. Settings → Export
2. Choose format:
   - **JSON:** Full data, reimportable
   - **Markdown:** Readable, portable
   - **Tana Paste:** For selective import
3. Unzip archive
4. Verify content

**Selective Export:**
1. Navigate to node
2. Right-click → Export
3. Same format options
4. Exports node + children

**Via API:**
```bash
# Export specific project
PROJECT=$(read_node --nodeId "PROJECT_ID")
echo "$PROJECT" > project-export.md

# Export all tasks
TASKS=$(search_nodes --query '{"hasType": "TASK"}')
for task in $TASKS; do
  read_node --nodeId $task >> tasks-export.md
done
```

**Migration to Other Tools:**
- **To Notion:** Use Markdown export, import to Notion
- **To Obsidian:** Markdown export, copy to vault
- **To Roam:** Use Tana Paste, convert to Roam format
- **To Plain Text:** Markdown export, organize in file system
