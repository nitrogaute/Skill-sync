# API Workflows & Advanced Examples

Complete guide to MCP API operations, Tana Paste format, and search queries.

## Table of Contents
- [Getting Started: Workspace Discovery](#getting-started-workspace-discovery)
- [Tana Paste Format](#tana-paste-format)
- [Search Query Syntax](#search-query-syntax)
- [Common API Workflows](#common-api-workflows)
- [Field Configuration Patterns](#field-configuration-patterns)

---

## Getting Started: Workspace Discovery

When first connecting to Tana via MCP, follow this workflow to explore your workspace.

### Step 1: List Your Workspaces

**Always start here** - You need the workspace ID for most operations.

```bash
mcporter call tana-local.list_workspaces
```

**Example Output:**
```json
[
  {
    "id": "3FIglnVSXUud",
    "name": "Personal Workspace",
    "homeNodeId": "L8NgOQAI9JiQ"
  },
  {
    "id": "7Abc123XyZ45",
    "name": "Team Workspace",
    "homeNodeId": "K9MnOpQrStUv"
  }
]
```

**Save the workspace ID** - You'll use it for subsequent operations.

### Step 2: Discover Your Tags (Supertags)

**IMPORTANT:** `list_tags` requires a `workspaceId` parameter.

```bash
# Replace with your actual workspace ID
mcporter call tana-local.list_tags --args '{"workspaceId": "3FIglnVSXUud"}'
```

**Example Output:**
```json
[
  {
    "id": "hL_DOnp3VAGD",
    "name": "todo"
  },
  {
    "id": "FPUKao-pYkp0",
    "name": "meeting"
  },
  {
    "id": "jG86zqH7MMdl",
    "name": "person"
  }
]
```

This shows all supertags in your workspace with their IDs.

### Step 3: Inspect Tag Schemas

Once you know your tags, inspect their field definitions:

```bash
# Get schema for a specific tag (e.g., "meeting")
mcporter call tana-local.get_tag_schema --args '{
  "workspaceId": "3FIglnVSXUud",
  "tagId": "FPUKao-pYkp0"
}'
```

**Example Output:**
```json
{
  "id": "FPUKao-pYkp0",
  "name": "meeting",
  "fields": [
    {
      "id": "field_date_123",
      "name": "Date",
      "type": "date"
    },
    {
      "id": "field_attendees_456",
      "name": "Attendees",
      "type": "options from supertag",
      "referencedTagId": "jG86zqH7MMdl"
    },
    {
      "id": "field_status_789",
      "name": "Status",
      "type": "options",
      "options": ["Scheduled", "Completed", "Cancelled"]
    }
  ],
  "extends": null,
  "contentTemplate": "- Agenda::\n- Notes::\n- Action Items::\n"
}
```

This shows:
- All fields defined on the tag
- Field types
- Options (for dropdown fields)
- Referenced tags (for "options from supertag" fields)
- Content template

### Step 4: Search for Nodes

Now search for nodes with specific tags:

```bash
# Find all meeting nodes
mcporter call tana-local.search_nodes --args '{
  "workspaceId": "3FIglnVSXUud",
  "query": {
    "hasType": "FPUKao-pYkp0"
  }
}'
```

**Example Output:**
```json
{
  "nodes": [
    {
      "id": "node_abc123",
      "name": "Team Standup",
      "created": "2026-02-04T10:00:00Z"
    },
    {
      "id": "node_def456",
      "name": "Client Meeting",
      "created": "2026-02-03T14:30:00Z"
    }
  ],
  "hasMore": false
}
```

### Step 5: Read Node Details

Get full content of a specific node:

```bash
mcporter call tana-local.read_node --args '{
  "workspaceId": "3FIglnVSXUud",
  "nodeId": "node_abc123"
}'
```

**Example Output (Markdown format):**
```markdown
# Team Standup

- Date:: [[date:2026-02-04]]
- Attendees:: [[John Smith]], [[Sarah Jones]]
- Status:: Completed

## Agenda
- Sprint progress
- Blockers

## Notes
- Backend deployment delayed
- Frontend on track

## Action Items
- [ ] Review PR #123
- [ ] Update timeline
```

### Complete Discovery Script

Here's a bash script to explore a workspace:

```bash
#!/bin/bash

# 1. Get workspace ID
WORKSPACE_ID=$(mcporter call tana-local.list_workspaces | jq -r '.[0].id')
echo "Workspace ID: $WORKSPACE_ID"

# 2. List all tags
echo -e "\n=== Tags ==="
mcporter call tana-local.list_tags --args "{\"workspaceId\": \"$WORKSPACE_ID\"}" | jq -r '.[] | "- \(.name) (ID: \(.id))"'

# 3. Get schema for first tag
TAG_ID=$(mcporter call tana-local.list_tags --args "{\"workspaceId\": \"$WORKSPACE_ID\"}" | jq -r '.[0].id')
echo -e "\n=== Schema for first tag ==="
mcporter call tana-local.get_tag_schema --args "{\"workspaceId\": \"$WORKSPACE_ID\", \"tagId\": \"$TAG_ID\"}"

# 4. Search for nodes with that tag
echo -e "\n=== Nodes with tag ==="
mcporter call tana-local.search_nodes --args "{\"workspaceId\": \"$WORKSPACE_ID\", \"query\": {\"hasType\": \"$TAG_ID\"}}"
```

### Common Gotchas

**❌ Missing workspace ID:**
```bash
# This will FAIL:
mcporter call tana-local.list_tags

# Error: Input validation error: expected string, received undefined
```

**✅ Include workspace ID:**
```bash
# This works:
mcporter call tana-local.list_tags --args '{"workspaceId": "YOUR_ID"}'
```

**❌ Wrong workspace ID:**
- IDs are workspace-specific
- Tag/node/field IDs from one workspace won't work in another
- Always use `list_workspaces` first

**✅ Cache workspace ID:**
```bash
# Save to variable for reuse
WORKSPACE_ID="3FIglnVSXUud"

# Use in all subsequent calls
mcporter call tana-local.list_tags --args "{\"workspaceId\": \"$WORKSPACE_ID\"}"
mcporter call tana-local.search_nodes --args "{\"workspaceId\": \"$WORKSPACE_ID\", \"query\": {...}}"
```

---

## Tana Paste Format

The `import_tana_paste` tool accepts Tana's clipboard format for hierarchical content.

### Basic Syntax

```
- Node text
  - Child node (2 spaces indent)
    - Grandchild (4 spaces)
```

**CRITICAL**: Use exactly 2 spaces per indentation level. Tabs or incorrect spacing will fail.

### Tags

```
- Meeting notes #meeting
- Project Alpha #[[Project Alpha]]
- Specific tag #[[^TAG_NODE_ID]]
```

Three ways to apply tags:
1. `#tagname` - Simple tag by name
2. `#[[Tag Name]]` - Tag with spaces or special characters
3. `#[[^TAG_ID]]` - Tag by specific ID (guaranteed match)

### Fields

```
- Meeting #meeting
  - Attendees:: [[John]], [[Sarah]]
  - Date:: [[date:2026-01-15]]
  - Status:: In Progress
  - [[^FIELD_ID]]:: Value using field ID
```

Field syntax: `FieldName:: value` (note the double colon and space)

**Field types in Tana Paste:**
- Plain text: `Notes:: Some text here`
- References: `Person:: [[John Smith]]`
- Dates: `Due:: [[date:2026-01-15]]`
- DateTime: `Meeting:: [[date:2026-01-15 14:30]]`
- Numbers: `Priority:: 5`
- Multiple values: `Tags:: [[tag1]], [[tag2]]`

### References

```
- Discussed [[Project Alpha]]
- See also [[^NODE_ID]]
```

Two reference formats:
- `[[Name]]` - Reference by node name (finds first match)
- `[[^NODE_ID]]` - Reference by specific ID (guaranteed unique)

### Dates

```
- Due:: [[date:2026-01-15]]
- Meeting:: [[date:2026-01-15 14:30]]
- Reminder:: [[date:2026-02-01 09:00]]
```

Date formats:
- Date only: `[[date:YYYY-MM-DD]]`
- With time: `[[date:YYYY-MM-DD HH:MM]]`
- Links to calendar nodes automatically

### Checkboxes (Todos)

```
- [ ] Unchecked task
- [x] Completed task
- [ ] Parent task
  - [x] Completed subtask
  - [ ] Pending subtask
```

### Text Formatting

```
- **bold text**
- ^^highlighted^^
- __italic__
- `code`
- ~~strikethrough~~
```

### Views (Reference Only)

```
%%view:table%%
%%view:calendar%%
%%view:list%%
%%view:cards%%
%%view:tabs%%
%%view:outline%%
%%view:sidemenu%%
```

**Note**: Views are created in UI or via these markers in paste format.

### Live Search Nodes

```
%%search%%
  - hasType: TAG_ID
  - is: todo
  - created: last 7
```

Creates a dynamic search node that auto-updates with matching results.

### Complete Example

```
- Q1 Planning #project
  - Status:: In Progress
  - Start Date:: [[date:2026-01-01]]
  - Owner:: [[Alice Johnson]]
  - Goals::
    - Increase revenue by 20%
    - Launch new product line
  - Workstreams::
    - [ ] Backend Development #workstream
      - Lead:: [[Bob Smith]]
      - Due:: [[date:2026-03-15]]
    - [ ] Frontend Development #workstream
      - Lead:: [[Carol Davis]]
      - Due:: [[date:2026-03-20]]
  - Tasks::
    %%search%%
      - hasType: TASK_TAG_ID
      - childOf: CURRENT_NODE
```

---

## Search Query Syntax

Queries are JSON objects passed to `search_nodes` for powerful filtering.

### Basic Filters

```json
// By tag type
{"hasType": "TAG_ID"}
{"hasType": ["TAG_ID1", "TAG_ID2"]}  // Multiple types

// By status
{"is": "done"}       // completed todos
{"is": "todo"}       // unchecked items
{"is": "template"}   // template nodes
{"is": "field"}      // field definitions

// Has something
{"has": "tag"}       // has any tag
{"has": "field"}     // has any field
{"has": "media"}     // has images/videos
```

### Text Search

```json
// Contains text (case-insensitive)
{"textContains": "quarterly"}

// Regex pattern match
{"textMatches": "Q[1-4] 2026"}
{"textMatches": "\\b\\d{3}-\\d{3}-\\d{4}\\b"}  // Phone numbers
```

### Relationship Filters

```json
// Children of specific node(s)
{"childOf": {"nodeIds": ["NODE_ID"]}}
{"childOf": {"nodeIds": ["NODE_ID"], "recursive": true}}  // All descendants

// Owned by (in subtree of)
{"ownedBy": {"nodeId": "NODE_ID"}}
{"ownedBy": {"nodeId": "NODE_ID", "recursive": true}}

// Links to specific node(s)
{"linksTo": ["NODE_ID"]}
{"linksTo": ["NODE_ID1", "NODE_ID2"]}  // Links to any of these
```

### Date Filters

```json
// Created/edited in last N days
{"created": {"last": 7}}
{"edited": {"last": 30}}
{"done": {"last": 7}}

// On specific date
{"onDate": "2026-01-15"}

// Date range (custom field)
{"fieldDate": {
  "fieldId": "FIELD_ID",
  "after": "2026-01-01",
  "before": "2026-12-31"
}}

// Overdue todos
{"overdue": true}
```

### Boolean Combinations

```json
// AND (all must match)
{"and": [
  {"hasType": "TAG_ID"},
  {"is": "todo"}
]}

// OR (any matches)
{"or": [
  {"hasType": "TAG1"},
  {"hasType": "TAG2"}
]}

// NOT (exclude)
{"not": {"is": "done"}}

// Complex nesting
{"and": [
  {"hasType": "TASK"},
  {"or": [
    {"overdue": true},
    {"created": {"last": 7}}
  ]},
  {"not": {"is": "done"}}
]}
```

### Field Value Filters

```json
// Field equals value
{"field": {"fieldId": "STATUS_FIELD_ID", "equals": "In Progress"}}

// Field contains text
{"field": {"fieldId": "NOTES_FIELD_ID", "contains": "important"}}

// Field is empty
{"field": {"fieldId": "FIELD_ID", "isEmpty": true}}

// Field is not empty
{"not": {"field": {"fieldId": "FIELD_ID", "isEmpty": true}}}
```

### Complex Query Examples

**Find all incomplete high-priority tasks created this week:**
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

**Find overdue tasks OR tasks due today:**
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

**Find recent meeting notes with specific attendee:**
```json
{
  "and": [
    {"hasType": "MEETING_TAG_ID"},
    {"created": {"last": 30}},
    {"linksTo": ["PERSON_NODE_ID"]}
  ]
}
```

---

## Common API Workflows

### 1. Create a Meeting Note

```bash
mcporter call tana-local.import_tana_paste --args '{
  "tanaPaste": "- Team Standup #meeting\n  - Date:: [[date:2026-01-15 09:00]]\n  - Attendees:: [[John Smith]], [[Sarah Jones]]\n  - Topics::\n    - Sprint progress\n    - Blockers\n  - Action Items::\n    - [ ] Review PRs\n    - [ ] Update docs"
}'
```

### 2. Find All Incomplete Tasks

```bash
mcporter call tana-local.search_nodes --args '{
  "query": {
    "and": [
      {"is": "todo"},
      {"not": {"is": "done"}}
    ]
  }
}'
```

### 3. Get Today's Daily Note

```bash
mcporter call tana-local.get_or_create_calendar_node --args '{
  "date": "2026-02-04",
  "granularity": "day"
}'
```

### 4. Add Task to Existing Project

```bash
# First, get children to find the tasks section
mcporter call tana-local.get_children --args '{"nodeId": "PROJECT_NODE_ID"}'

# Then import under the tasks node
mcporter call tana-local.import_tana_paste --args '{
  "targetNodeId": "TASKS_SECTION_ID",
  "tanaPaste": "- [ ] New task #task\n  - Due:: [[date:2026-01-20]]\n  - Priority:: High"
}'
```

### 5. Build a CRM Entry

```bash
mcporter call tana-local.import_tana_paste --args '{
  "tanaPaste": "- Acme Corp #company\n  - Website:: https://acme.com\n  - Industry:: Technology\n  - Contacts::\n    - John Doe #person\n      - Email:: john@acme.com\n      - Role:: CEO\n      - Phone:: 555-0100"
}'
```

### 6. Create Weekly Review

```bash
mcporter call tana-local.import_tana_paste --args '{
  "tanaPaste": "- Week 5 Review #weekly-review\n  - Week:: [[date:2026-02-03]]\n  - Wins::\n    - Shipped feature X\n    - Closed 15 support tickets\n  - Challenges::\n    - Blocked on API integration\n  - Learnings::\n    - Better time estimation needed\n  - Next Week::\n    - [ ] Finish API integration\n    - [ ] Team retrospective\n    - [ ] Q1 planning"
}'
```

### 7. Bulk Update Task Status

```bash
# Search for completed tasks
COMPLETED=$(mcporter call tana-local.search_nodes --args '{
  "query": {"and": [{"hasType": "TASK_TAG_ID"}, {"is": "done"}]}
}')

# Loop through and update field
for NODE_ID in $COMPLETED; do
  mcporter call tana-local.set_field_option --args '{
    "nodeId": "'$NODE_ID'",
    "fieldId": "STATUS_FIELD_ID",
    "value": "Completed"
  }'
done
```

### 8. Generate Project Summary

```bash
# Get all meetings for a project
MEETINGS=$(mcporter call tana-local.search_nodes --args '{
  "query": {
    "and": [
      {"hasType": "MEETING_TAG_ID"},
      {"childOf": {"nodeId": "PROJECT_NODE_ID", "recursive": true}}
    ]
  }
}')

# Read each meeting
for MEETING_ID in $MEETINGS; do
  mcporter call tana-local.read_node --args '{"nodeId": "'$MEETING_ID'"}'
done

# Use AI to synthesize summary, then import back
```

### 9. Daily Automation: Move Tasks

```bash
# Find tasks due today
TODAY_TASKS=$(mcporter call tana-local.search_nodes --args '{
  "query": {
    "and": [
      {"is": "todo"},
      {"onDate": "2026-02-04"}
    ]
  }
}')

# Get or create today's note
TODAY_NODE=$(mcporter call tana-local.get_or_create_calendar_node --args '{
  "date": "2026-02-04",
  "granularity": "day"
}')

# Reference tasks in today's note
for TASK_ID in $TODAY_TASKS; do
  mcporter call tana-local.import_tana_paste --args '{
    "targetNodeId": "'$TODAY_NODE'",
    "tanaPaste": "- [[^'$TASK_ID']]"
  }'
done
```

### 10. Create Supertag Schema from API

```bash
# Create the tag
TAG_ID=$(mcporter call tana-local.create_tag --args '{
  "name": "Book",
  "color": "purple"
}')

# Add fields
mcporter call tana-local.add_field_to_tag --args '{
  "tagId": "'$TAG_ID'",
  "fieldName": "Author",
  "fieldType": "plain"
}'

mcporter call tana-local.add_field_to_tag --args '{
  "tagId": "'$TAG_ID'",
  "fieldName": "Rating",
  "fieldType": "options"
}'

mcporter call tana-local.add_field_to_tag --args '{
  "tagId": "'$TAG_ID'",
  "fieldName": "Finished Date",
  "fieldType": "date"
}'

mcporter call tana-local.add_field_to_tag --args '{
  "tagId": "'$TAG_ID'",
  "fieldName": "Genre",
  "fieldType": "options"
}'
```

### 11. Batch Import from CSV

Complete script to import data from CSV into Tana with proper tagging and fields.

**Example CSV (books.csv):**
```csv
Title,Author,Rating,Finished,Genre
"Thinking Fast and Slow",Daniel Kahneman,5,2026-01-15,Non-Fiction
"Project Hail Mary",Andy Weir,4,2026-01-20,Fiction
"Atomic Habits",James Clear,5,2026-02-01,Self-Help
```

**Import Script (import-books.sh):**
```bash
#!/bin/bash

# Configuration
WORKSPACE_ID="3FIglnVSXUud"  # Replace with your workspace ID
CSV_FILE="books.csv"
TAG_NAME="book"

# Get or create the book tag
echo "Setting up book tag..."
TAGS=$(mcporter call tana-local.list_tags --args "{\"workspaceId\": \"$WORKSPACE_ID\"}")
TAG_ID=$(echo "$TAGS" | jq -r ".[] | select(.name == \"$TAG_NAME\") | .id")

if [ -z "$TAG_ID" ]; then
  echo "Creating book tag..."
  TAG_ID=$(mcporter call tana-local.create_tag --args "{\"workspaceId\": \"$WORKSPACE_ID\", \"name\": \"$TAG_NAME\"}" | jq -r '.id')
fi

echo "Book tag ID: $TAG_ID"

# Read CSV and import each row
echo "Importing books..."
COUNTER=0

# Skip header, read CSV
tail -n +2 "$CSV_FILE" | while IFS=, read -r title author rating finished genre; do
  # Remove quotes from fields
  title=$(echo "$title" | sed 's/"//g')
  author=$(echo "$author" | sed 's/"//g')
  genre=$(echo "$genre" | sed 's/"//g')

  # Build Tana Paste
  TANA_PASTE=$(cat <<EOF
- $title #$TAG_NAME
  - Author:: $author
  - Rating:: $rating
  - Finished Date:: [[date:$finished]]
  - Genre:: $genre
  - Notes::
EOF
)

  # Import to Tana
  echo "Importing: $title..."
  mcporter call tana-local.import_tana_paste --args "{
    \"workspaceId\": \"$WORKSPACE_ID\",
    \"tanaPaste\": $(echo "$TANA_PASTE" | jq -R -s .)
  }"

  COUNTER=$((COUNTER + 1))

  # Rate limiting (avoid overwhelming API)
  sleep 0.5
done

echo "Import complete! Imported $COUNTER books."
```

**Usage:**
```bash
chmod +x import-books.sh
./import-books.sh
```

**Advanced: Import with Error Handling:**
```bash
#!/bin/bash

WORKSPACE_ID="3FIglnVSXUud"
CSV_FILE="books.csv"
LOG_FILE="import-log.txt"
ERROR_FILE="import-errors.txt"

> "$LOG_FILE"    # Clear log
> "$ERROR_FILE"  # Clear errors

SUCCESS=0
FAILED=0

tail -n +2 "$CSV_FILE" | while IFS=, read -r title author rating finished genre; do
  title=$(echo "$title" | sed 's/"//g')
  author=$(echo "$author" | sed 's/"//g')

  TANA_PASTE="- $title #book\n  - Author:: $author\n  - Rating:: $rating"

  # Try import with error capture
  RESULT=$(mcporter call tana-local.import_tana_paste --args "{
    \"workspaceId\": \"$WORKSPACE_ID\",
    \"tanaPaste\": $(echo -e "$TANA_PASTE" | jq -R -s .)
  }" 2>&1)

  if [ $? -eq 0 ]; then
    echo "[SUCCESS] $title" >> "$LOG_FILE"
    SUCCESS=$((SUCCESS + 1))
  else
    echo "[FAILED] $title: $RESULT" >> "$ERROR_FILE"
    FAILED=$((FAILED + 1))
  fi

  sleep 0.5
done

echo "Import complete!"
echo "Success: $SUCCESS"
echo "Failed: $FAILED"
echo "Check $LOG_FILE and $ERROR_FILE for details"
```

### 12. Batch Update Existing Nodes

Update field values for multiple existing nodes.

```bash
#!/bin/bash

WORKSPACE_ID="3FIglnVSXUud"

# Find all book nodes without a genre
BOOKS=$(mcporter call tana-local.search_nodes --args "{
  \"workspaceId\": \"$WORKSPACE_ID\",
  \"query\": {
    \"and\": [
      {\"hasType\": \"BOOK_TAG_ID\"},
      {\"field\": {\"fieldId\": \"GENRE_FIELD_ID\", \"isEmpty\": true}}
    ]
  }
}" | jq -r '.nodes[].id')

# Update each book
for BOOK_ID in $BOOKS; do
  # Read book to get title
  BOOK=$(mcporter call tana-local.read_node --args "{
    \"workspaceId\": \"$WORKSPACE_ID\",
    \"nodeId\": \"$BOOK_ID\"
  }")

  TITLE=$(echo "$BOOK" | grep "^#" | head -1 | sed 's/# //')

  echo "Processing: $TITLE"

  # AI categorize genre (pseudo-code)
  # GENRE=$(ai_categorize_genre "$TITLE")

  # For demo, just set to "Uncategorized"
  mcporter call tana-local.set_field_option --args "{
    \"workspaceId\": \"$WORKSPACE_ID\",
    \"nodeId\": \"$BOOK_ID\",
    \"fieldId\": \"GENRE_FIELD_ID\",
    \"value\": \"Uncategorized\"
  }"

  echo "  → Set genre to: Uncategorized"
done

echo "Batch update complete!"
```

### 13. Export and Backup Automation

Daily backup script for critical data.

```bash
#!/bin/bash

WORKSPACE_ID="3FIglnVSXUud"
BACKUP_DIR="$HOME/tana-backups"
DATE=$(date +%Y-%m-%d)

mkdir -p "$BACKUP_DIR"

echo "Starting backup for $DATE..."

# Export all meetings
MEETINGS=$(mcporter call tana-local.search_nodes --args "{
  \"workspaceId\": \"$WORKSPACE_ID\",
  \"query\": {\"hasType\": \"MEETING_TAG_ID\"}
}" | jq -r '.nodes[].id')

MEETING_BACKUP="$BACKUP_DIR/meetings-$DATE.md"
> "$MEETING_BACKUP"

for MEETING_ID in $MEETINGS; do
  mcporter call tana-local.read_node --args "{
    \"workspaceId\": \"$WORKSPACE_ID\",
    \"nodeId\": \"$MEETING_ID\"
  }" >> "$MEETING_BACKUP"
  echo -e "\n---\n" >> "$MEETING_BACKUP"
done

echo "Meetings backed up to: $MEETING_BACKUP"

# Export all tasks
TASKS=$(mcporter call tana-local.search_nodes --args "{
  \"workspaceId\": \"$WORKSPACE_ID\",
  \"query\": {
    \"and\": [
      {\"hasType\": \"TASK_TAG_ID\"},
      {\"is\": \"todo\"}
    ]
  }
}")

echo "$TASKS" > "$BACKUP_DIR/tasks-$DATE.json"
echo "Tasks backed up to: $BACKUP_DIR/tasks-$DATE.json"

# Keep only last 30 days
find "$BACKUP_DIR" -name "*.md" -mtime +30 -delete
find "$BACKUP_DIR" -name "*.json" -mtime +30 -delete

echo "Backup complete!"
```

**Schedule with cron:**
```bash
# Add to crontab (runs daily at 2am)
0 2 * * * /path/to/backup-script.sh
```

---

## Field Configuration Patterns

### Options (Free Dropdown)

**Use case:** Status field with values: Not Started, In Progress, Done, Blocked

**Behavior:**
- Users can type new values
- Values are plain text, not linked
- Good for fixed enumerations

**API example:**
```bash
mcporter call tana-local.add_field_to_tag --args '{
  "tagId": "TAG_ID",
  "fieldName": "Status",
  "fieldType": "options"
}'

# Set value
mcporter call tana-local.set_field_option --args '{
  "nodeId": "NODE_ID",
  "fieldId": "STATUS_FIELD_ID",
  "value": "In Progress"
}'
```

### Options from Supertag (Instance Reference)

**Use case:** Assignee field → options from #person

**Behavior:**
- Shows existing #person nodes as options
- Selecting creates a **reference link**
- Typing new name **auto-creates** a #person node!
- Creates bidirectional relationships

**API example:**
```bash
mcporter call tana-local.add_field_to_tag --args '{
  "tagId": "TASK_TAG_ID",
  "fieldName": "Assignee",
  "fieldType": "options from supertag",
  "referencedTagId": "PERSON_TAG_ID"
}'

# Set to existing person (by node ID)
mcporter call tana-local.set_field_option --args '{
  "nodeId": "TASK_NODE_ID",
  "fieldId": "ASSIGNEE_FIELD_ID",
  "value": "PERSON_NODE_ID"
}'

# Or create new person by name
mcporter call tana-local.set_field_option --args '{
  "nodeId": "TASK_NODE_ID",
  "fieldId": "ASSIGNEE_FIELD_ID",
  "value": "Alice Johnson"
}'
```

### Auto-Initialize Options

| Setting | Behavior | API Support |
|---------|----------|-------------|
| To ancestor with supertag | Inherits value from parent with matching tag | Configure in UI |
| To random node | Picks random from options | Configure in UI |
| To value from ancestor field | Copies specific field from parent | Configure in UI |
| Current date | Sets to today | Configure in UI |
| Current user | Sets to triggering user | Configure in UI |

**Note:** Auto-initialization is configured in the UI. API can set field values but not auto-init rules.

### Number Fields with Validation

```bash
# Add number field
mcporter call tana-local.add_field_to_tag --args '{
  "tagId": "TAG_ID",
  "fieldName": "Priority",
  "fieldType": "number"
}'

# Set number value
mcporter call tana-local.set_field_content --args '{
  "nodeId": "NODE_ID",
  "fieldId": "PRIORITY_FIELD_ID",
  "content": "5"
}'
```

**UI Configuration:** Set min/max in supertag field settings (not available via API).

### Date Fields

```bash
# Add date field
mcporter call tana-local.add_field_to_tag --args '{
  "tagId": "TAG_ID",
  "fieldName": "Due Date",
  "fieldType": "date"
}'

# Set date value (links to calendar node)
mcporter call tana-local.set_field_content --args '{
  "nodeId": "NODE_ID",
  "fieldId": "DUE_DATE_FIELD_ID",
  "content": "[[date:2026-02-15]]"
}'
```

### Checkbox Fields

```bash
# Add checkbox field
mcporter call tana-local.add_field_to_tag --args '{
  "tagId": "TAG_ID",
  "fieldName": "Urgent",
  "fieldType": "checkbox"
}'

# Use check/uncheck on node (for todo status)
mcporter call tana-local.check_node --args '{"nodeId": "NODE_ID"}'
mcporter call tana-local.uncheck_node --args '{"nodeId": "NODE_ID"}'
```
