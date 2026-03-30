---
name: ticktick-sync
description: Bidirectional sync between TickTick and Tana. TickTick is the mobile/execution layer, Tana is the source of truth. Use for scheduled sync tasks and manual sync requests.
version: 1.0.0
---

# TickTick ↔ Tana Sync

Bidirectional task sync. **Tana = source of truth. TickTick = execution/mobile layer.**

## Tools

- **TickTick**: `mcporter call ticktick.<tool>` (list_tasks, create_task, update_task, complete_task, list_projects, etc.)
- **Tana**: `mcporter call tana-local.<tool>` (search_nodes, import_tana_paste, set_field_content, set_field_option, check_node, uncheck_node, etc.)

## Constants Reference

All Tana IDs are defined in code at `projects/openclaw-integrations/src/tana/constants.ts`.

### #todo tag (id: `hL_DOnp3VAGD`)

| Field | ID | Type |
|-------|----|------|
| Status | `dgt63EZO_Imm` | Options |
| Priority | `YH1wW4JgSOzF` | Options |
| Due date | `lfr8DiFg08LP` | Date |
| Area | `xuEHKzTezGDZ` | Instance |
| Related Person | `5whLHix7vjIp` | Options |
| Topic | `YNtQUYqn2b35` | Instance |
| TickTick ID | `E0j-AZ96lJ9d` | Plain |
| TickTick List | `i0wUusmWA4U1` | Plain |

### Status options

| Status | ID |
|--------|----|
| Inbox | `XO5N9DQP7JMN` |
| Todo | `cu_jUXMFsA5o` |
| In Progress | `zxwtJzykp1lE` |
| Done | `CevrzULBGIA6` |
| Blocked | `53a2Xavktphr` |

### Priority options

| Priority | ID |
|----------|----|
| High | `ZxQG4FQxFsOV` |
| Medium | `EZ_mk-_bl5Ry` |
| Low | `omHg7--6jDJ8` |

## Field Mapping

| Tana | TickTick | Mapping |
|------|----------|---------|
| Node name | title | Direct |
| Due date (`lfr8DiFg08LP`) | dueDate | DateTime (see below) |
| Priority High | priority 5 | Value map |
| Priority Medium | priority 3 | Value map |
| Priority Low | priority 1 | Value map |
| Status Done | completed | Boolean |
| Status In Progress | open + tag "in-progress" | Convention |
| Children (text nodes) | content/description | Concatenate as markdown |
| Area | project | Name-based mapping |
| TickTick ID (`E0j-AZ96lJ9d`) | id | Sync key |
| TickTick List (`i0wUusmWA4U1`) | projectId/projectName | Stored for reference |

### DateTime Handling

**Every task MUST have both date AND time.** No all-day tasks.

- TickTick stores datetime as ISO strings with a fixed `+0000` suffix (the time is already local, NOT UTC): `2026-03-15T14:30:00.000+0000`
- Tana stores datetime in the format: `2026-03-15 14:30`
- TickTick fields: `startDate`, `dueDate`, `isAllDay` (always set to `false`), `timeZone`
- Conversion helpers in `src/tana/ticktick-sync.ts`: `tickTickDateToTana()` and `tanaDateToTickTick()`

**TickTick → Tana**: Extract the time directly from the ISO string (do NOT parse as Date/UTC). Store in Tana as `[[date:2026-03-15 14:30]]`.

**Tana → TickTick**: Always set `isAllDay: false`. If the Tana date has a time, convert directly. If the Tana date has NO time, use smart placement (see below).

## Smart Time Placement

When a Tana task has a date but no time and needs to be pushed to TickTick, find a clear slot in the day:

1. **Check the day's schedule** by querying both systems:
   - TickTick: `mcporter call ticktick.list_tasks` and filter for the target date
   - Tana calendar: `tana-local.search_nodes` for tasks on that date, or read the day node via `get_or_create_calendar_node`
   - Google Calendar (if available): check for meetings/events

2. **Find a gap** in the schedule:
   - Working hours: 08:00–18:00
   - Prefer morning slots (09:00–12:00) for focused tasks
   - Prefer afternoon slots (13:00–16:00) for routine tasks
   - Avoid overlap with existing timed tasks/events
   - Leave at least 30 min buffer between tasks

3. **Assign the time** and set `isAllDay: false` on the TickTick task.

4. **Write the time back to Tana** so both systems stay in sync: use `set_field_content` to update the Due date field with the datetime.

## Sync: TickTick → Tana (Import)

1. Fetch open tasks:
   ```bash
   mcporter call ticktick.list_tasks
   ```
   Or per project:
   ```bash
   mcporter call ticktick.list_project_tasks --args '{"projectId": "<pid>"}'
   ```

2. For each task, search Tana by TickTick ID:
   ```bash
   mcporter call tana-local.search_nodes --args '{"query": {"and": [{"hasType": "hL_DOnp3VAGD"}, {"field": {"fieldId": "E0j-AZ96lJ9d", "stringValue": "<ticktick_id>"}}]}}'
   ```

3. **Not found** → Create in Tana (use `tickTickDateToTana()` to convert the datetime — preserves time):
   ```bash
   mcporter call tana-local.import_tana_paste --args '{"parentNodeId": "3FIglnVSXUud_CAPTURE_INBOX", "content": "- Task title #[[^hL_DOnp3VAGD]]\n  - [[^E0j-AZ96lJ9d]]:: <ticktick_id>\n  - [[^i0wUusmWA4U1]]:: <project_name>\n  - [[^lfr8DiFg08LP]]:: [[date:<date> <HH:MM>]]"}'
   ```
   Example with time: `[[date:2026-03-15 14:30]]`
   Then set Priority and Status via `set_field_option`:
   ```bash
   mcporter call tana-local.set_field_option --args '{"nodeId": "<new_node_id>", "attributeId": "YH1wW4JgSOzF", "optionId": "<priority_option_id>"}'
   mcporter call tana-local.set_field_option --args '{"nodeId": "<new_node_id>", "attributeId": "dgt63EZO_Imm", "optionId": "<status_option_id>"}'
   ```

4. **Found** → Compare modification times. If TickTick is newer, update Tana fields.

## Sync: Tana → TickTick (Push)

1. Search for recently edited #todo tasks:
   ```bash
   mcporter call tana-local.search_nodes --args '{"query": {"and": [{"hasType": "hL_DOnp3VAGD"}, {"edited": {"last": 8}}]}}'
   ```

2. Read each node to get current field values.

3. **Has TickTick ID** → Update existing task. Use `tanaDateToTickTick()` to convert. Always set `isAllDay: false`:
   ```bash
   mcporter call ticktick.update_task --args '{"projectId": "<pid>", "taskId": "<tid>", "title": "<title>", "priority": <priority>, "dueDate": "<iso_datetime>", "isAllDay": false}'
   ```

4. **No TickTick ID** → Create new task in TickTick. **Never create all-day tasks.** If the Tana date has no time (`tanaDateToTickTick().hasTime === false`), run Smart Time Placement first to assign a time, then write it back to Tana:
   ```bash
   mcporter call ticktick.create_task --args '{"title": "<title>", "priority": <priority>, "dueDate": "<iso_datetime>", "isAllDay": false}'
   mcporter call tana-local.set_field_content --args '{"nodeId": "<tana_node_id>", "attributeId": "E0j-AZ96lJ9d", "content": "<new_ticktick_id>"}'
   ```
   If smart placement assigned a time, also update Tana's Due date:
   ```bash
   mcporter call tana-local.set_field_content --args '{"nodeId": "<tana_node_id>", "attributeId": "lfr8DiFg08LP", "content": "<date> <HH:MM>"}'
   ```

## Sync: Completions

- **TickTick task completed** → Find in Tana by TickTick ID → `check_node` + set Status to Done:
  ```bash
  mcporter call tana-local.check_node --args '{"nodeId": "<tana_node_id>"}'
  mcporter call tana-local.set_field_option --args '{"nodeId": "<tana_node_id>", "attributeId": "dgt63EZO_Imm", "optionId": "CevrzULBGIA6"}'
  ```

- **Tana task checked/Done** → Find by TickTick ID → Complete in TickTick:
  ```bash
  mcporter call ticktick.complete_task --args '{"projectId": "<pid>", "taskId": "<tid>"}'
  ```

- **Tana task unchecked** → Reopen in TickTick:
  ```bash
  mcporter call ticktick.update_task --args '{"projectId": "<pid>", "taskId": "<tid>", "status": 0}'
  ```

## Conflict Resolution

**Tana always wins.** If both systems changed since last sync:
1. Read Tana's current state
2. Push Tana's values to TickTick
3. Log the conflict for review

## TickTick Tag Convention

- Tasks tagged `trym` in TickTick → Apply `#trym` supertag in Tana (tag ID: `VQ0SdVj7Ghdu`), not just `#todo`
- Tasks tagged `in-progress` in TickTick → Set Status to In Progress in Tana

## Sync Schedule

**Every heartbeat** — sync runs on each heartbeat cycle (~30 min intervals).
Replaced fixed 3x daily schedule (07:15, 12:15, 18:15) with continuous heartbeat sync.

## Error Handling

- If TickTick API is unavailable, log and skip (don't block other tasks)
- If a single task fails to sync, continue with remaining tasks
- Report sync summary: created/updated/failed counts
- Only message Gaute if there are failures or noteworthy changes (>5 new tasks, conflicts)
