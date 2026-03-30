# AI Features & Automation

Complete guide to Tana's AI capabilities including AI Command Nodes, AI Agents, voice features, and automation.

## Table of Contents
- [AI Command Nodes](#ai-command-nodes)
- [Prompt Expressions](#prompt-expressions)
- [Available AI Commands](#available-ai-commands)
- [AI Agents](#ai-agents)
- [AI Chat](#ai-chat)
- [Meeting Notetaker](#meeting-notetaker)
- [Mobile Voice & Transcription](#mobile-voice--transcription)
- [Automation Patterns](#automation-patterns)

---

## AI Command Nodes

AI Command Nodes automate tasks using Tana AI for content generation, API requests, transcription, and more.

**Requirements:**
- Tana paid subscription
- Desktop or web app (some features)

### Creating AI Command Nodes

**Method 1: From Supertag**
1. Open supertag configuration
2. Click "Add command" or "Commands" section
3. Choose AI command type
4. Configure prompt and settings
5. Add to command palette or event triggers

**Method 2: Standalone**
1. Create new node
2. `Cmd/K` → "Convert to command"
3. Select AI command type
4. Configure

### Prompt Workbench

Test and refine prompts before deployment.

**Features:**
- Test against real nodes
- Preview expanded prompts (see exact AI input)
- Monitor token costs
- Adjust temperature/creativity
- Iterate quickly

**How to Use:**
1. Open AI command node
2. Click "Open Prompt Workbench"
3. Select test node(s)
4. View expanded prompt
5. Run test completion
6. Adjust and retest
7. Deploy when satisfied

**Best Practices:**
- Always test with representative data
- Check token estimates
- Verify output format
- Test edge cases (empty fields, missing data)
- Monitor cost for batch operations

### Configuration Parameters

**Essential Settings:**

| Parameter | Description | Usage |
|-----------|-------------|-------|
| Prompt expression | Template with variables | Core AI input |
| Target node | Where output goes | Insert as child, replace, etc. |
| Node filter | Which nodes command applies to | Restricts scope |
| Model selection | AI model to use | GPT-4, Claude, etc. |

**Advanced Options:**

| Parameter | Range | Description |
|-----------|-------|-------------|
| Temperature | 0-2 | Output randomness (0=deterministic, 2=creative) |
| Top P | 0-1 | Nucleus sampling (alternative to temperature) |
| Max tokens | Number | Maximum response length |
| Stop sequences | Strings | When to stop generation |
| Presence penalty | -2 to 2 | Discourage topic repetition |
| Frequency penalty | -2 to 2 | Discourage word repetition |

**Output Control:**
- Insert as child of target node
- Replace target node content
- Insert as sibling
- Set field value
- Create new node

**Event Triggers:**
- When tag added to node
- When tag removed
- When field value changes
- Manual execution only

### Safety Features

**Infinite Loop Prevention:**
Tana warns when similar events trigger within 60 seconds. Event system disables until page reload to prevent cascading automation failures.

**Cost Protection:**
- Token estimates in Prompt Workbench
- Batch operations show total cost
- Set max tokens to cap expense

---

## Prompt Expressions

Variables that embed content into AI prompts using `${variable}` syntax.

### Available Keywords

**Content References:**

| Expression | Returns |
|------------|---------|
| `${name}` | Node title/name only |
| `${sys:context}` | All node data (name, fields, children, references) |
| `${sys:content}` | Child nodes only (excludes fields) |
| `${description}` | Node description field |

**Metadata:**

| Expression | Returns |
|------------|---------|
| `${sys:tags}` | All supertags applied to node |
| `${sys:nodeId}` | Unique node identifier |
| `${sys:nodeURL}` | Direct link to node |
| `${sys:owner}` | User who owns node |
| `${sys:createdBy}` | User who created node |

**Temporal:**

| Expression | Returns |
|------------|---------|
| `${sys:currentDate}` | Today's date |
| `${sys:currentDateTime}` | Current date and time |
| `${sys:createdAt}` | When node was created |
| `${sys:editedAt}` | Last edit timestamp |

**Field Values:**

| Expression | Returns |
|------------|---------|
| `${FieldName}` | Value of named field |
| `${Status}` | Value of "Status" field |
| `${Due Date}` | Value of "Due Date" field |

**Important Limitation:**
Variables work only in plain text nodes, not within reference nodes.

### Example Prompts

**Meeting Summary:**
```
Summarize this meeting:

Title: ${name}
Date: ${Meeting Date}
Attendees: ${Attendees}

Notes:
${sys:content}

Extract:
1. Key decisions
2. Action items
3. Follow-up topics

Format as bullet points.
```

**Task Prioritization:**
```
Analyze this task and suggest a priority (High/Medium/Low):

Task: ${name}
Description: ${description}
Due Date: ${Due Date}
Project: ${Project}
Context: ${sys:context}

Consider urgency, impact, and dependencies.
Respond with just: High, Medium, or Low.
```

**Content Extraction:**
```
Extract structured information from this note:

${sys:content}

Find and return:
- People mentioned (format: @Name)
- Dates mentioned (format: [[date:YYYY-MM-DD]])
- Action items (format: - [ ] Item)
- Key topics (format: #tag)

Preserve original text where possible.
```

**Article Summarization:**
```
Summarize this article in 3 bullet points:

${sys:context}

Focus on:
- Main argument or thesis
- Key supporting points
- Practical takeaways

Each bullet should be 1-2 sentences.
```

---

## Available AI Commands

Comprehensive list of built-in AI operations.

### Core AI Commands

**Ask AI (Streaming):**
- Generic AI query with real-time response
- Accepts user-provided OpenAI keys
- Fastest for simple queries
- Shows incremental output

**Ask AI (Non-Streaming):**
- Batch processing mode
- Advanced parameter control
- Better for multiple nodes
- Full response at once

**Configuration:**
- Both support custom prompts
- Temperature, top P, penalties
- Max tokens, stop sequences
- Model selection

### API Integration

**Make API Request:**
- Integrate external services
- Custom headers and authentication
- Payload templating with expressions
- Response parsing and field mapping

**Example Use Cases:**
- Fetch data from external APIs
- Update CRM systems
- Trigger webhooks
- Sync with other tools

**Configuration:**
```json
{
  "url": "https://api.example.com/endpoint",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer ${API_KEY}",
    "Content-Type": "application/json"
  },
  "body": {
    "content": "${sys:content}",
    "metadata": {
      "nodeId": "${sys:nodeId}",
      "created": "${sys:createdAt}"
    }
  }
}
```

### Media Generation

**Generate Images:**
- AI image creation (DALL-E, Stable Diffusion, etc.)
- Multiple sizes: 256px, 512px, 1024px
- Quantity: 1-10 images
- Prompt from node content

**Example Prompt:**
```
Create an illustration: ${name}

Style: ${Image Style}
Mood: ${Mood}
Details: ${description}
```

**Transcribe Audio:**
- WhisperAI integration
- 91 language support
- Automatic language detection
- Or specify language

**Configuration:**
- Audio file reference
- Target language (optional)
- Output format
- Timestamp options

### Specialized AI Tools

**Autotag:**
- AI-powered tag assignment
- Analyzes node content
- Suggests relevant supertags
- Can auto-apply or suggest

**Configuration:**
```
Analyze this content and suggest appropriate tags:

${sys:context}

Available tags: ${sys:workspaceTags}

Return as: #tag1, #tag2, #tag3
```

**Add Meeting Bot:**
- Video call transcription agent
- Google Meet compatible
- Zoom compatible
- Teams support (beta)

**Setup:**
1. Create meeting node with #meeting tag
2. Add Meeting Bot command
3. Provide meeting link
4. Bot joins, records, transcribes
5. Output inserted as child nodes

**Text Processing Agent:**
- Extract summaries from transcripts
- Identify entities (people, places, things)
- Pull out action items
- Generate metadata

**Example:**
```
Process this meeting transcript:

${Transcript}

Extract:
1. Summary (3-5 sentences)
2. Participants (as @mentions)
3. Action items (as checkboxes)
4. Decisions made
5. Next steps
```

---

## AI Agents

Custom AI automations for specific workflows.

### What Are AI Agents?

AI Agents are reusable AI workflows configured once and triggered automatically or manually.

**Characteristics:**
- Context-aware (access to workspace data)
- Multi-step reasoning
- Can execute multiple commands
- Triggered by events or manual invocation

### Creating Custom Agents

**Method 1: Via Supertag**
1. Configure supertag (e.g., #project-report)
2. Add AI command node to template
3. Set event trigger: "When tag added"
4. Configure multi-step workflow
5. Test on sample data

**Method 2: Standalone Agent**
1. Create agent node
2. Define purpose and scope
3. Configure prompts and commands
4. Set up triggers
5. Add to command palette

### Example Agents

**Project Status Reporter:**
```
Prompt:
Analyze this project and generate a status report:

Project: ${name}
Status: ${Status}
Due Date: ${Due Date}

Tasks:
${search:childOf:current,hasType:TASK}

Generate:
1. Overall status (On Track/At Risk/Blocked)
2. Completion percentage
3. Upcoming milestones
4. Blockers and risks
5. Recommended actions

Target: Insert as child
Trigger: Manual or weekly schedule
```

**Meeting Action Item Extractor:**
```
Prompt:
Extract action items from this meeting:

${sys:content}

For each action item:
- Create checkbox
- Tag with #task
- Set Assignee if mentioned
- Set Due Date if mentioned
- Link back to meeting

Target: Create new nodes under "Action Items::" field
Trigger: When #meeting tag added
```

**Smart Inbox Processor:**
```
Prompt:
Analyze this inbox item and categorize it:

${sys:content}

Determine:
1. Type (task, note, idea, reference)
2. Relevant project or area
3. Suggested tags
4. Priority (if task)
5. Due date (if mentioned)

Apply appropriate tag and move to correct location.

Target: Modify node and move
Trigger: When added to Inbox
```

**Research Paper Analyzer:**
```
Prompt:
Analyze this research paper:

Title: ${name}
Content: ${sys:content}

Extract:
1. Main hypothesis/question
2. Methodology
3. Key findings
4. Implications
5. Related topics (as tags)
6. Citations to follow up on

Target: Insert structured summary as children
Trigger: When #research-paper tag added
```

### Event Trigger Examples

AI Command Nodes can be triggered automatically by events. Here are practical examples:

**When Tag Added:**
```
Trigger: When #meeting tag is added to a node
Action: Auto-populate template fields
- Set Date to current date
- Set Status to "Scheduled"
- Create "Agenda::" and "Notes::" child nodes
```

**When Tag Removed:**
```
Trigger: When #draft tag is removed
Action: Publish workflow
- Move node to Published section
- Set Published Date to today
- Notify subscribers
```

**When Field Value Changes:**
```
Trigger: When Status field changes to "Completed"
Action: Archive and celebrate
- Move to Completed section
- Set Completed Date to today
- Add to #win tag
- Send notification
```

**When Node Created in Location:**
```
Trigger: When node created under "Inbox"
Action: Smart categorization
- AI analyzes content
- Suggests tags and project
- Extracts metadata
- Moves to suggested location
```

**Scheduled Triggers:**
```
Daily at 9am:
- Generate daily plan from calendar + tasks
- Populate today's daily note
- Send notification

Weekly on Sunday:
- Compile weekly review
- Gather completed tasks and meetings
- Create review node
```

**Chained Event Example:**
```
Event 1: When #task tag added
  → Auto-set Priority based on keywords
  → If contains "urgent" or "asap" → Priority: High

Event 2: When Priority field set to "High"
  → Add to Today's note
  → Notify task owner
  → Set Due Date to today + 2 days
```

### Agent Best Practices

**Prompt Design:**
- Be specific about desired output format
- Include examples when possible
- Use expressions for dynamic content
- Test with edge cases

**Error Handling:**
- Handle missing fields gracefully
- Provide defaults for optional data
- Validate input before processing
- Log failures for debugging

**Performance:**
- Keep prompts focused
- Avoid redundant API calls
- Batch similar operations
- Monitor token usage

**Maintenance:**
- Document agent purpose and logic
- Version control prompt changes
- Test after workspace schema changes
- Archive unused agents

---

## AI Chat

Conversational AI with workspace context.

**Features:**
- Access to workspace data
- Multi-turn conversations
- Can search and read nodes
- Can create and modify content

**Access:**
- Sidebar AI Chat button
- `Cmd/K` → "AI Chat"
- Requires paid subscription

**Use Cases:**
- Ask questions about your notes
- Generate content ideas
- Analyze patterns in data
- Get suggestions for organization
- Brainstorm with context

**Example Interactions:**
- "Summarize all my meetings from last week"
- "What are the common themes in my project notes?"
- "Create a weekly review based on my completed tasks"
- "Find nodes related to [topic] and create a summary"

---

## Meeting Notetaker

Automated transcription and action item extraction for video calls.

### Features

**Bot-Free Transcription:**
- No visible bot in meeting
- Uses Tana's meeting integration
- Google Meet compatible
- Zoom compatible

**Automatic Processing:**
- Real-time transcription
- Speaker identification (when possible)
- Timestamp markers
- Automatic field population

**AI Enhancement:**
- Extract action items
- Identify decisions
- Summarize key points
- Tag participants

### Setup

**For Google Meet:**
1. Create meeting note with #meeting tag
2. Set Meeting base type on tag
3. Add meeting link to field
4. Enable Meeting Notetaker
5. Transcription appears in node

**For Zoom:**
- Similar setup
- May require Zoom integration settings
- Check workspace integrations

### Post-Meeting Processing

**Automatic:**
- Transcription inserted as child
- Participants tagged (if in workspace)
- Date/time fields populated
- Status updated

**Manual Review:**
1. Read transcript
2. Extract additional action items
3. Tag related projects
4. Move tasks to appropriate locations
5. Share summary with attendees

---

## Mobile Voice & Transcription

Voice-to-text on mobile with 91 language support.

### Voice Memo Features

**Recording:**
- Tap microphone in mobile app
- Record voice memo
- Offline capable (transcribes later)
- Select target supertag before recording

**Transcription:**
- Automatic when online
- 91 languages supported
- Speaker identification (single speaker)
- Sent to today's daily note via Inbox

**AI Enrichment:**
- Entities extracted (people, dates, projects)
- Fields auto-populated based on supertag
- References created to mentioned nodes
- Tags suggested

**Rewrite Feature:**
- Transform transcript style
- Summarize long recordings
- Extract specific information
- Format as structured notes

### Audio-Enabled Supertags

Configure supertags for voice input optimization.

**Setup:**
1. Open supertag configuration
2. Enable "Audio-enabled tag"
3. Configure field mapping:
   - Title from: [part of transcript]
   - Field1 from: [extracted entity]
   - Field2 from: [date mentioned]
4. Set post-processing command (optional)

**Example: Voice Task Capture**
```
Supertag: #quick-task
Audio-enabled: Yes
Field mapping:
- Title: First sentence
- Due Date: Any date mentioned
- Priority: Keywords (urgent, important, etc.)
- Project: Mentioned project names

Post-processing:
Extract due date and set field
Tag mentioned projects
Move to project if specified
```

**Example: Voice Journal**
```
Supertag: #journal-entry
Audio-enabled: Yes
Field mapping:
- Title: "${sys:currentDate} Journal"
- Mood: Sentiment analysis
- Topics: Mentioned themes

Post-processing:
Tag topics mentioned
Link related journal entries
Extract gratitude items
```

### Voice Workflow Examples

**Quick Task Capture:**
1. Open Tana mobile
2. Tap microphone
3. Say: "Task: Call Sarah about project update by Friday. High priority."
4. Auto-creates:
   - Node: "Call Sarah about project update"
   - Tag: #task
   - Due Date: This Friday
   - Priority: High
   - Related: Links to Sarah's node

**Meeting Notes While Walking:**
1. Select #meeting tag
2. Record voice memo
3. Transcript appears in daily note
4. Review and tag later
5. Extract action items with AI command

**Idea Capture:**
1. Quick voice recording
2. Transcribed to Inbox
3. AI suggests tags and projects
4. Move to appropriate location

---

## Automation Patterns

Combine AI features for powerful workflows.

### Pattern 1: Inbox Zero with AI

**Workflow:**
1. Quick capture to Inbox (mobile/desktop)
2. AI agent processes new items:
   - Analyzes content
   - Suggests supertags
   - Identifies related projects
   - Extracts metadata
3. Review and approve suggestions
4. AI moves to correct location
5. Inbox stays clean

**Implementation:**
- Create #inbox-processor AI agent
- Trigger: When node added to Inbox
- Prompt: Categorize and route content
- Output: Tag, set fields, move node

### Pattern 2: Smart Meeting Workflow

**Workflow:**
1. Create meeting note (#meeting tag)
2. Trigger: AI pre-fills template
3. During meeting: Notetaker transcribes
4. After meeting:
   - AI extracts action items
   - Creates task nodes
   - Assigns to attendees
   - Links to project
   - Sends summary

**Implementation:**
- Multiple AI commands on #meeting tag
- Event triggers at different stages
- Chained operations

### Pattern 3: Weekly Review Automation

**Workflow:**
1. Every Sunday, AI creates review node
2. Searches completed tasks from week
3. Searches meetings attended
4. Finds achievements tagged #win
5. Compiles into structured review
6. Prompts for reflection

**Implementation:**
- Scheduled AI command (weekly)
- Multiple search queries
- Template-based output
- Manual reflection step

### Pattern 4: Research Paper Processing

**Workflow:**
1. Import paper (PDF or paste)
2. Tag with #research-paper
3. Trigger AI to:
   - Extract metadata (authors, date, journal)
   - Summarize abstract
   - Identify key findings
   - Extract citations
   - Suggest related papers in workspace
   - Generate topic tags
4. Manual annotation and notes

**Implementation:**
- AI command on #research-paper
- Event trigger: When tag added
- Multi-step extraction
- Field population

### Pattern 5: Daily Planning Assistant

**Workflow:**
1. Every morning, AI reviews:
   - Calendar for the day
   - Tasks due today
   - Tasks overdue
   - Priorities from yesterday
2. Generates suggested plan
3. Populates today's note
4. Sends notification

**Implementation:**
- Scheduled AI command (daily)
- Multiple search operations
- Template output to daily note
- Integration with calendar

### Combining UI and API

**Hybrid Power:**
- UI for setup and review
- API for bulk operations
- AI for intelligence
- Manual for judgment calls

**Example:**
1. Voice capture on mobile → Inbox
2. API batch-processes inbox items
3. AI categorizes and suggests
4. UI review and final decisions
5. API moves to destinations
