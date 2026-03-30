# Views & Search

Complete guide to Tana's visualization and search capabilities.

## Table of Contents
- [View Types](#view-types)
- [View Customization](#view-customization)
- [Live Search](#live-search)
- [Advanced Search Patterns](#advanced-search-patterns)
- [View Combinations](#view-combinations)

---

## View Types

Views transform how information displays without changing underlying data. Switch instantly between formats.

### Editing Views

Direct manipulation of content with full editing capabilities.

#### Outline View

**Description:** Bullet list format with full outline editor functionality.

**Best For:**
- Writing and editing
- Hierarchical organization
- Quick capture and organization
- Deep nesting of ideas

**Features:**
- Expand/collapse branches
- Drag-and-drop reordering
- Indenting with Tab/Shift+Tab
- Inline editing
- Reference visibility
- Checkbox support

**When to Use:**
- Default view for most nodes
- Brainstorming sessions
- Note-taking
- Organizing thoughts
- Working with deeply nested content

**Customization:**
- Filter: Hide/show specific content
- Sort: Reorder by fields
- Group: Organize by field values
- Display: Show/hide specific fields

#### Table View

**Description:** Rows represent nodes, columns represent fields. Spreadsheet-like interface.

**Best For:**
- Database-like content
- Supertag instances
- Comparing multiple items
- Field-heavy nodes

**Features:**
- Column calculations (sum, average, median, min, max, count)
- Sortable columns
- Filterable rows
- Inline field editing
- Resize columns
- Hide/show columns

**Column Calculations:**
- **Sum:** Total of number fields
- **Average:** Mean value
- **Median:** Middle value
- **Min:** Smallest value
- **Max:** Largest value
- **Count:** Number of non-empty values

**When to Use:**
- Project dashboards
- Task lists
- CRM contact lists
- Inventory management
- Comparing field values across nodes

**Example Use Cases:**
- Project with Status, Owner, Due Date columns
- Book list with Title, Author, Rating, Finished Date
- Contact database with Name, Email, Phone, Company

**Customization:**
- Add/remove columns (fields)
- Sort by any column
- Filter rows by field values
- Group by field (creates sections)
- Calculate totals in footer

#### Cards View

**Description:** Each child node displays as a card in a grid layout.

**Best For:**
- Visual organization
- Kanban-style workflows
- Image-heavy content
- Grouping by status or category

**Features:**
- Drag-and-drop between groups
- Group by field values
- Card size options
- Field visibility on cards
- Cover images
- Quick actions

**Grouping:**
- Group by any field
- Creates columns/sections
- Drag cards between groups
- Updates field value automatically

**When to Use:**
- Kanban boards (group by Status)
- Visual project planning
- Image galleries
- Recipe collections
- Product catalogs

**Example Setup:**
```
Tasks #task → Cards view
Group by: Status
Columns: To Do | In Progress | Done

Drag task cards between columns
Status field updates automatically
```

**Customization:**
- Group by field
- Card display fields
- Card size (small, medium, large)
- Sort within groups
- Filter cards

---

### Navigation Views

Browsing-focused views for exploring content.

#### List View (Navigation)

**Description:** Two-panel layout - items on left, full content on right.

**Best For:**
- Master-detail interfaces
- Browsing collections
- Preview and select
- Sequential review

**Features:**
- Left panel: Node titles and preview
- Right panel: Full node content
- Click to switch detail view
- Keyboard navigation (up/down arrows)

**When to Use:**
- Document collections
- Meeting notes archive
- Article library
- Knowledge base browsing
- Recipe book

**Example:**
```
Left panel: Meeting titles with dates
Right panel: Selected meeting's full content
Navigate with arrow keys
```

**Customization:**
- Filter items in left panel
- Sort order
- Display fields in preview
- Right panel view type

#### Calendar View

**Description:** Time-based visualization with day, week, or month granularities.

**Best For:**
- Time-based planning
- Event management
- Deadline tracking
- Schedule overview

**Granularities:**
- **Day:** Hour-by-hour view
- **Week:** 7-day overview
- **Month:** Month-at-a-glance

**Features:**
- Plots nodes by date fields
- Multiple date field support
- Click date to create node
- Drag to reschedule
- Color coding by tag or field

**When to Use:**
- Meeting schedules
- Project timelines
- Deadline tracking
- Habit tracking
- Event planning

**Date Field Mapping:**
- Choose which field to plot (Due Date, Start Date, Meeting Date, etc.)
- Multiple fields create multiple entries
- Links to calendar nodes

**Example:**
```
Tasks #task → Calendar view
Plot by: Due Date
View: Month
See all deadlines at a glance
```

**Customization:**
- Select date field to plot
- Choose granularity
- Filter which nodes show
- Color coding
- Show/hide completed items

#### Side Menu View

**Description:** Child nodes appear as clickable menu items in left sidebar.

**Best For:**
- Navigation structures
- Documentation sites
- Course content
- Guidebooks

**Features:**
- Nested menu structure
- Collapse/expand sections
- Active item highlighting
- Right panel shows content

**When to Use:**
- Documentation hubs
- Course syllabi
- Company handbooks
- Travel guides
- Recipe categories

**Example:**
```
Company Handbook
├── HR Policies
│   ├── Time Off
│   ├── Benefits
│   └── Code of Conduct
├── Engineering
│   ├── Onboarding
│   ├── Best Practices
│   └── Tools
└── Product
    ├── Roadmap
    └── Feature Specs
```

**Customization:**
- Default expanded/collapsed
- Menu item order
- Show/hide empty sections

#### Tabs View

**Description:** Child nodes display as horizontal tabs at top.

**Best For:**
- Switching between related views
- Dashboard with sections
- Multi-faceted content

**Features:**
- Tab bar at top
- Click to switch
- Keyboard shortcuts (Cmd+number)
- Each tab can have different view

**When to Use:**
- Project dashboard (Overview, Tasks, Meetings, Docs)
- Product page (Details, Reviews, Specs)
- Supertag pages (All instances, by Status, Archive)
- Research topic (Papers, Notes, Ideas)

**Example:**
```
Project Node → Tabs view
Tabs:
- Overview (outline view)
- Tasks (table view, filtered to #task)
- Timeline (calendar view)
- Team (cards view, #person)
```

**Customization:**
- Tab order
- Tab names
- View type per tab
- Default tab

---

## View Customization

All views support customization via the view toolbar.

### Filter

Restrict displayed content by criteria.

**Text Filters:**
- Contains text (case-insensitive)
- Exact match
- Regular expressions (advanced)

**Field Filters:**
- Field equals value
- Field is empty/not empty
- Field contains text
- Date before/after
- Number greater/less than

**Tag Filters:**
- Has specific tag
- Does not have tag
- Has any tag

**Status Filters:**
- Is todo
- Is done
- Is template
- Is field definition

**Combining Filters:**
- Multiple filters = AND logic
- All must match
- No OR support in UI (use search nodes for OR)

**Example Filters:**
```
Table view of #task:
Filter: Status = "In Progress"
Filter: Priority = "High"
Filter: Owner = "Alice"
Result: High-priority In-Progress tasks owned by Alice
```

### Sort

Arrange nodes in specific order.

**Sort Options:**
- Any field (ascending/descending)
- System fields:
  - Created date
  - Edited date
  - Name (alphabetical)
  - Owner
- Manual order (default in outline)

**Multiple Sort:**
- Primary sort
- Secondary sort for ties
- Tertiary sort, etc.

**Example:**
```
Sort by:
1. Status (To Do, In Progress, Done)
2. Priority (High, Medium, Low)
3. Due Date (soonest first)
```

**Available in:**
- Outline view
- Table view
- Cards view
- List view

### Group

Organize nodes by field values into sections.

**Grouping:**
- Select any field
- Creates sections/columns
- Nodes appear under their value
- Empty value = separate group

**Available in:**
- Outline view (creates collapsible sections)
- Cards view (creates columns)
- List view (creates sections in left panel)

**Example:**
```
Tasks grouped by Status:
┌─ To Do (5 tasks)
├─ In Progress (3 tasks)
└─ Done (12 tasks)
```

**Drag-and-Drop:**
- In Cards view, drag between groups
- Updates field value automatically
- Enables Kanban workflows

### Display

Choose which fields appear beneath node titles.

**Options:**
- Select specific fields to show
- Show all fields
- Hide all fields
- Order of field display

**Available in:**
- Outline view
- Table view (choose columns)
- Cards view (choose card fields)
- List view (preview panel)
- Calendar view (event details)

**Example:**
```
Display on task cards:
☑ Due Date
☑ Owner
☑ Priority
☐ Description (too long)
☐ Created date (not relevant)
```

### Page Size & Result Limit

**Page Size:**
- Default: 100 nodes
- Options: 25, 50, 100, 250, 500
- "Load more" pagination

**Result Limit:**
- Cap total results up to 2,500 nodes
- Prevents performance issues
- Encourages filtering

**When to Adjust:**
- Large collections: Increase page size
- Performance issues: Decrease limit
- Specific queries: Adjust as needed

### Content Width

Display width for node content.

**Options:**
- **Auto:** Adjusts to content
- **Medium:** Fixed comfortable width
- **Full:** Full window width

**When to Use:**
- Full: Tables with many columns
- Medium: Reading documents
- Auto: Mixed content types

### Save for Everyone

In multi-member workspaces, save view settings as default for all users.

**Usage:**
1. Configure view (filters, sort, groups)
2. Check "Save for everyone"
3. All workspace members see same default

**Best Practices:**
- Establish team standards
- Document view purposes
- Allow personal overrides
- Update when workflows change

---

## Live Search

Dynamic search nodes that auto-update with matching results.

### Creating Live Searches

**Method 1: Command Line**
1. `Cmd/K` → "Find nodes"
2. Build query with filters
3. Creates search node
4. Results update automatically

**Method 2: Tana Paste**
```
%%search%%
  - hasType: TAG_ID
  - is: todo
  - created: last 7
```

**Method 3: API**
```bash
mcporter call tana-local.search_nodes --args '{
  "query": {"hasType": "TASK_TAG_ID", "is": "todo"}
}'
```

### Search Operators

**Basic:**
- `hasType: TAG_ID` - Nodes with specific tag
- `is: todo` - Checkbox items
- `is: done` - Completed items
- `has: tag` - Has any tag
- `has: field` - Has any field

**Text:**
- `textContains: "keyword"` - Contains text
- `textMatches: "regex"` - Regex match

**Dates:**
- `created: last 7` - Last 7 days
- `edited: last 30` - Edited recently
- `onDate: YYYY-MM-DD` - Specific date
- `overdue: true` - Overdue todos

**Relationships:**
- `childOf: NODE_ID` - Direct children
- `childOf: NODE_ID, recursive: true` - All descendants
- `linksTo: NODE_ID` - References node

**Boolean:**
- `and: [filter1, filter2]` - All must match
- `or: [filter1, filter2]` - Any can match
- `not: filter` - Exclude

### Common Search Patterns

**My Tasks:**
```
%%search%%
  - hasType: TASK_TAG
  - is: todo
  - Owner:: ${currentUser}
```

**Recent Meetings:**
```
%%search%%
  - hasType: MEETING_TAG
  - created: last 14
```

**High Priority Overdue:**
```
%%search%%
  - hasType: TASK_TAG
  - is: todo
  - overdue: true
  - Priority:: High
```

**Unprocessed Inbox:**
```
%%search%%
  - childOf: INBOX_NODE
  - not: has tag
```

**This Week's Wins:**
```
%%search%%
  - hasType: WIN_TAG
  - created: last 7
```

---

## Advanced Search Patterns

### Saved Searches as Dashboard

Create multiple search nodes for comprehensive views.

**Project Dashboard Example:**
```
Project Alpha
├── Incomplete Tasks
│   %%search%%: hasType:TASK, childOf:current, is:todo
├── Done This Week
│   %%search%%: hasType:TASK, childOf:current, done:last 7
├── Upcoming Deadlines
│   %%search%%: hasType:TASK, childOf:current, Due Date:next 7
└── Team Members
    %%search%%: hasType:PERSON, linksTo:current
```

### Combining Search with Views

**Example 1: Kanban Board**
```
All Tasks (search node)
%%search%%: hasType:TASK, is:todo

View: Cards
Group by: Status
Result: Kanban board of all tasks
```

**Example 2: Timeline**
```
Sprint 5 Tasks
%%search%%: hasType:TASK, Project::Sprint 5

View: Calendar
Plot by: Due Date
Result: Visual timeline
```

**Example 3: Team Workload**
```
Team Tasks
%%search%%: hasType:TASK, is:todo

View: Table
Group by: Owner
Columns: Task, Priority, Due Date, Status
Calculate: Count per owner
Result: Workload distribution
```

### Nested Searches

Search results can contain search nodes, creating multi-level queries.

**Example:**
```
Projects (main node)
└── Active Projects
    %%search%%: hasType:PROJECT, Status:Active

    Each project can contain:
    └── Project Tasks
        %%search%%: hasType:TASK, childOf:parent
```

### Search + Automation

Combine searches with AI commands for powerful workflows.

**Example: Auto-Prioritize Overdue**
```
Overdue Tasks
%%search%%: is:todo, overdue:true

AI Command on results:
- Trigger: Daily at 9am
- Action: Set Priority::High
- Notify owners
```

---

## View Combinations

Leverage multiple views for different perspectives on same data.

### Tabs with Different Views

**Example: Project Management**
```
Project Node → Tabs View

Tab 1: "Overview" (Outline view)
- Project description
- Goals
- Team
- Resources

Tab 2: "Tasks" (Table view)
- All tasks with fields
- Sort by Due Date
- Filter by Status

Tab 3: "Timeline" (Calendar view)
- Visual schedule
- Deadline tracking

Tab 4: "Team" (Cards view)
- Group by Owner
- Visual workload
```

### Master View with Detail Views

**Example: Content Library**
```
Articles (List view)
├── Left panel: Article titles
└── Right panel: Selected article
    ├── Overview (Outline)
    ├── Related (Search → Table)
    └── Citations (Search → Outline)
```

### Search Results with Multiple Views

Save same search node, switch views as needed.

**Example: Task Management**
```
My Tasks (search node)

View as Outline: Focus mode for completion
View as Table: Compare fields and sort
View as Cards: Kanban workflow (group by Status)
View as Calendar: Deadline overview
```

### Nested Views for Hierarchies

**Example: Company Handbook**
```
Handbook (Side Menu view)
├── Department 1 (Tabs view)
│   ├── Policies (Outline)
│   ├── Team (Table)
│   └── Resources (Cards)
└── Department 2 (Tabs view)
    └── (similar structure)
```

### Best View Combinations

**For Projects:**
- Main: Outline (project details)
- Tasks: Table (comparison) or Cards (kanban)
- Timeline: Calendar (deadlines)
- Team: Cards or Table (workload)

**For Knowledge Management:**
- Main: Outline (writing/reading)
- Related: List (navigation)
- By Topic: Cards (visual browsing)
- Timeline: Calendar (when created)

**For CRM:**
- Contacts: Table (full data)
- Pipeline: Cards grouped by Stage
- Calendar: Meetings and follow-ups
- Activity: List (chronological)

**For Content Creation:**
- Outline: Writing and structure
- Table: Metadata comparison
- Calendar: Publishing schedule
- Cards: Visual status tracking
