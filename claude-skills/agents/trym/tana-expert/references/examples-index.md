# Tana Examples Index

Quick reference to all examples included in the Tana Expert skill.

## AI Command Nodes Examples

**Location:** [ai-features.md](ai-features.md)

### Prompt Examples

1. **Meeting Summary** - Extract key points, decisions, action items from meeting notes
2. **Task Prioritization** - AI suggests High/Medium/Low priority based on context
3. **Content Extraction** - Pull structured data (people, dates, actions, topics) from notes
4. **Article Summarization** - Generate 3-bullet executive summary

### Complete AI Agent Examples

1. **Project Status Reporter**
   - Analyzes project with all tasks
   - Generates completion %, milestones, blockers, recommendations
   - Trigger: Manual or weekly schedule

2. **Meeting Action Item Extractor**
   - Extracts action items from meeting transcripts
   - Creates task nodes with assignees and due dates
   - Links back to meeting
   - Trigger: When #meeting tag added

3. **Smart Inbox Processor**
   - Categorizes inbox items (task, note, idea, reference)
   - Suggests relevant project/area
   - Auto-tags and moves
   - Trigger: When added to Inbox

4. **Research Paper Analyzer**
   - Extracts hypothesis, methodology, findings
   - Generates topic tags
   - Lists citations
   - Trigger: When #research-paper tag added

### Voice-Enabled Supertag Examples

1. **Quick Task Capture** - Voice → auto-extract due date, priority, project
2. **Voice Journal** - Voice → sentiment analysis, topic extraction, linking

### API Integration Example

**Make API Request command** - Shows headers, authentication, payload templating with expressions

---

## Search & Filter Examples

**Location:** [api-workflows.md](api-workflows.md) and [views-and-search.md](views-and-search.md)

### Search Query Examples (JSON)

**Basic Queries:**
```json
{"hasType": "TAG_ID"}                    // Nodes with specific tag
{"is": "todo"}                           // Checkbox items
{"is": "done"}                           // Completed items
{"textContains": "quarterly"}            // Text search
{"created": {"last": 7}}                 // Last 7 days
{"overdue": true}                        // Overdue todos
```

**Complex Queries:**

1. **Incomplete High-Priority Tasks Created This Week:**
```json
{
  "and": [
    {"hasType": "TASK_TAG_ID"},
    {"is": "todo"},
    {"not": {"is": "done"}},
    {"created": {"last": 7}},
    {"field": {"fieldId": "PRIORITY_FIELD_ID", "equals": "High"}}
  ]
}
```

2. **Overdue OR Due Today:**
```json
{
  "and": [
    {"hasType": "TASK_TAG_ID"},
    {"is": "todo"},
    {"or": [
      {"overdue": true},
      {"onDate": "2026-02-04"}
    ]}
  ]
}
```

3. **Recent Meetings with Specific Attendee:**
```json
{
  "and": [
    {"hasType": "MEETING_TAG_ID"},
    {"created": {"last": 30}},
    {"linksTo": ["PERSON_NODE_ID"]}
  ]
}
```

### UI Filter Examples

**Location:** [views-and-search.md](views-and-search.md)

**Table View Filtering:**
```
Filter: Status = "In Progress"
Filter: Priority = "High"
Filter: Owner = "Alice"
Result: High-priority In-Progress tasks owned by Alice
```

### Common Search Patterns

**Location:** [views-and-search.md](views-and-search.md#common-search-patterns)

1. **My Tasks** - `hasType: TASK_TAG, is: todo, Owner: ${currentUser}`
2. **Recent Meetings** - `hasType: MEETING_TAG, created: last 14`
3. **High Priority Overdue** - `hasType: TASK_TAG, is: todo, overdue: true, Priority: High`
4. **Unprocessed Inbox** - `childOf: INBOX_NODE, not: has tag`
5. **This Week's Wins** - `hasType: WIN_TAG, created: last 7`

---

## Workflow Examples

**Location:** [ui-workflows.md](ui-workflows.md)

### Complete UI Workflows

1. **Create New Supertag** - Step-by-step from scratch
2. **Build Project Dashboard** - With search nodes, multiple views
3. **Set Up Meeting Note Template** - Fields, content template, AI integration
4. **Create CRM System** - Company, Person, Interaction tags with relationships
5. **Daily Review Routine** - Morning and evening workflows
6. **Set Up Smart Filters** - Task management searches
7. **Template-Based Workflows** - Daily note, project kickoff templates

### API Workflow Examples

**Location:** [api-workflows.md](api-workflows.md#common-api-workflows)

1. **Create Meeting Note** - Complete Tana Paste with fields, attendees, action items
2. **Find All Incomplete Tasks** - Search query with boolean logic
3. **Get Today's Daily Note** - Calendar node creation
4. **Add Task to Project** - Get children, import under specific node
5. **Build CRM Entry** - Hierarchical company/person/contact structure
6. **Create Weekly Review** - Structured review template
7. **Bulk Update Task Status** - Loop through search results, update fields
8. **Generate Project Summary** - Read all meetings, AI synthesize
9. **Daily Automation: Move Tasks** - Find tasks due today, reference in daily note
10. **Create Supertag Schema from API** - Tag creation, field addition

---

## View Configuration Examples

**Location:** [views-and-search.md](views-and-search.md)

### View Combination Examples

1. **Project Management with Tabs:**
   - Tab 1: Overview (Outline)
   - Tab 2: Tasks (Table)
   - Tab 3: Timeline (Calendar)
   - Tab 4: Team (Cards)

2. **Kanban Board:**
   - Cards view
   - Group by: Status
   - Drag-and-drop updates field

3. **Team Workload Dashboard:**
   - Table view
   - Group by: Owner
   - Columns: Task, Priority, Due Date, Status
   - Calculate: Count per owner

4. **Content Library:**
   - List view (navigation)
   - Left: Article titles
   - Right: Selected article with tabs

### Sort & Group Examples

**Multi-level Sort:**
```
Sort by:
1. Status (To Do, In Progress, Done)
2. Priority (High, Medium, Low)
3. Due Date (soonest first)
```

**Group Example:**
```
Tasks grouped by Status:
┌─ To Do (5 tasks)
├─ In Progress (3 tasks)
└─ Done (12 tasks)
```

---

## Tana Paste Format Examples

**Location:** [api-workflows.md](api-workflows.md#tana-paste-format)

### Basic Examples

**Simple Hierarchy:**
```
- Node text
  - Child node (2 spaces indent)
    - Grandchild (4 spaces)
```

**With Tags:**
```
- Meeting notes #meeting
- Project Alpha #[[Project Alpha]]
```

**With Fields:**
```
- Meeting #meeting
  - Attendees:: [[John]], [[Sarah]]
  - Date:: [[date:2026-01-15]]
  - Status:: In Progress
```

**With Todos:**
```
- [ ] Unchecked task
- [x] Completed task
```

**Complete Meeting Note:**
```
- Team Standup #meeting
  - Date:: [[date:2026-01-15 09:00]]
  - Attendees:: [[John Smith]], [[Sarah Jones]]
  - Topics::
    - Sprint progress
    - Blockers
  - Action Items::
    - [ ] Review PRs
    - [ ] Update docs
```

**CRM Entry:**
```
- Acme Corp #company
  - Website:: https://acme.com
  - Industry:: Technology
  - Contacts::
    - John Doe #person
      - Email:: john@acme.com
      - Role:: CEO
```

**Weekly Review:**
```
- Week 5 Review #weekly-review
  - Week:: [[date:2026-02-03]]
  - Wins::
    - Shipped feature X
    - Closed 15 support tickets
  - Challenges::
    - Blocked on API integration
  - Learnings::
    - Better time estimation needed
  - Next Week::
    - [ ] Finish API integration
    - [ ] Team retrospective
    - [ ] Q1 planning
```

---

## Automation Pattern Examples

**Location:** [ai-features.md](ai-features.md#automation-patterns)

### Complete Automation Workflows

1. **Inbox Zero with AI**
   - Quick capture → AI categorizes → Tag & route → Review → Move

2. **Smart Meeting Workflow**
   - Create note → AI pre-fills template → Notetaker transcribes → AI extracts actions → Creates tasks → Sends summary

3. **Weekly Review Automation**
   - Scheduled Sunday → Search completed tasks → Search meetings → Find wins → Compile review → Prompt reflection

4. **Research Paper Processing**
   - Import paper → Tag → AI extracts metadata → Summarize → Extract citations → Suggest related → Tag topics

5. **Daily Planning Assistant**
   - Morning → Review calendar + tasks → Generate plan → Populate today's note → Notify

---

## Migration Examples

**Location:** [ui-workflows.md](ui-workflows.md#migration-strategies) and [best-practices.md](best-practices.md#migration-strategies)

### Import/Export Examples

1. **From Notion** - Database → Supertag mapping
2. **From Roam** - Daily notes, pages, attributes
3. **From Obsidian** - Wikilinks, frontmatter, tags
4. **From Evernote** - Notebooks, tags, notes

---

## Advanced Pattern Examples

**Location:** [best-practices.md](best-practices.md#advanced-patterns)

### Multi-Level Hierarchy Example

```
Project Alpha #project
├── Overview
│   ├── Goals
│   ├── Success Criteria
│   └── Timeline
├── Workstreams
│   ├── Backend #workstream
│   │   ├── Tasks (search: is:todo, childOf:BACKEND_ID)
│   │   └── Docs
│   ├── Frontend #workstream
│   │   └── Tasks (search: is:todo, childOf:FRONTEND_ID)
└── All Tasks (search: is:todo, childOf:PROJECT_ID, recursive:true)
```

### Field Inheritance Example

```
Project Alpha
└── Status:: In Progress
    └── Task 1 #task
        └── Status:: In Progress (inherited)
```

### Zettelkasten Structure Example

```
Zettelkasten
├── Inbox (temporary notes)
├── Permanent Notes
│   ├── Note 1 #zettel
│   │   ├── Related:: [[Note 5]], [[Note 12]]
│   │   └── Tags:: #concept, #framework
│   └── Note 2 #zettel
├── Index
│   ├── Concepts (search)
│   └── Frameworks (search)
└── MOC (Maps of Content)
```

---

## Quick Reference: Where to Find Examples

| Need Example Of... | File | Section |
|-------------------|------|---------|
| AI Command Nodes | ai-features.md | Prompt Examples, Example Agents |
| Search Queries (JSON) | api-workflows.md | Search Query Syntax, Complex Query Examples |
| UI Filters | views-and-search.md | Filter section, Common Search Patterns |
| Tana Paste Format | api-workflows.md | Tana Paste Format, Complete Example |
| API Workflows | api-workflows.md | Common API Workflows (10 examples) |
| UI Workflows | ui-workflows.md | Common UI Workflows (7 examples) |
| View Configurations | views-and-search.md | View Combinations, all sections |
| Automation Patterns | ai-features.md | Automation Patterns |
| Voice Workflows | ai-features.md | Voice Workflow Examples |
| Migration | ui-workflows.md, best-practices.md | Migration Strategies |
| Advanced Patterns | best-practices.md | Advanced Patterns |

---

## Recently Added Examples ✅

### Event Trigger Examples (ai-features.md)
- ✅ When tag added/removed
- ✅ When field value changes
- ✅ When node created in location
- ✅ Scheduled triggers (daily, weekly)
- ✅ Chained event example

### Title Expression Examples (ui-workflows.md)
- ✅ Meeting titles: `${Date} - ${Type}`
- ✅ Task titles: `[${Priority}] ${Project} - ${sys:content}`
- ✅ Person titles: `${First Name} ${Last Name} (${Company})`
- ✅ Event titles with conditionals
- ✅ Article/book titles with formatting
- ✅ System field usage: `${sys:owner}`, `${sys:createdAt}`
- ✅ Character limits, date formatting, uppercase/lowercase

### Batch Processing Scripts (api-workflows.md)
- ✅ Batch import from CSV (complete working script)
- ✅ Import with error handling and logging
- ✅ Batch update existing nodes
- ✅ Export and backup automation
- ✅ Cron scheduling example

## Still Missing (Future Additions)

Based on common use cases, we could still add:

1. **Field Auto-initialization Examples** - Specific UI setup for ancestor field inheritance
2. **Calendar Integration Examples** - Google Calendar sync specifics
3. **Readwise Integration Examples** - If applicable
4. **Publishing Examples** - Tana Publish layouts and configurations
5. **Integration with Other Tools** - Zapier, Make, n8n workflows
