---
name: daily-brief-chain
description: "Chained skill: morning briefing pipeline. Fetches calendar, email, tasks, and weather in parallel, then assembles a structured brief. Use for 'brief', 'morgenbrief', 'hva skjer i dag', or morning updates."
disable-model-invocation: true
allowed-tools: Bash, Skill, Read, Grep, Glob
---

# Daily Brief Chain

Deterministic multi-step pipeline for generating the morning brief.

Current date and time:
! `date "+%A %d. %B %Y %H:%M %Z"`

## Chain Steps

### Step 1: Gather Data (parallel)

Run all four data fetches in parallel. Each produces a structured intermediate result.

**1a. Calendar**
Fetch today's events from ALL 3 calendars:
```bash
# Home + Shared calendars
gws calendar +agenda --days 1

# KM_2 (jobb) calendar - separate fetch
gog calendar events "gn6jpht66mrsdo315ripf4fdlfk6vn8u@import.calendar.google.com" 2>/dev/null
```
Note: KM_2 08:00-09:00 daily = training block, not a meeting.

**1b. Email**
```bash
gws gmail +triage --max 10
```

**1c. Tasks**
Check Todoist via MCP:
- Get today's tasks (due today)
- Get overdue tasks

If Todoist unavailable, check TickTick via MCP as fallback.
If both unavailable, check scheduled_tasks:
```bash
sqlite3 /Users/nitromini/ClaudeClaw/store/claudeclaw.db "SELECT * FROM scheduled_tasks WHERE status = 'active';"
```

**1d. Weather**
```bash
bash /Users/nitromini/ClaudeClaw/scripts/met-weather.sh 2>/dev/null || echo "Weather unavailable"
```

### Step 2: Process & Classify

From the raw data gathered in Step 1:

**Calendar:** Sort events by time. Flag any conflicts (overlapping times). Mark KM_2 08-09 as training.

**Email:** Classify each unread email:
- "Trenger handling" = requires a reply, decision, or action
- "FYI" = informational, newsletters, notifications
Sort by urgency within each group.

**Tasks:** Separate into:
- Due today
- Overdue (flag with `[!]`)
- No date but high priority

### Step 3: Assemble Brief

Format in Norwegian. No em dashes. No AI cliches. Tight and scannable.

```
BRIEF [dato]

VER
[temperatur, nedbor, vind - kort]

KALENDER
- HH:MM [tittel] ([kilde])
- HH:MM [tittel] - [lokasjon/personer]
[!] Konflikt: HH:MM [event1] overlapper [event2]

INBOX (X uleste)
Trenger handling:
- [avsender]: [emne]
FYI:
- [avsender]: [emne]

TASKS
- [ ] Oppgave 1
- [ ] Oppgave 2
- [!] Forfalt: Oppgave 3

PAMINNELSER I DAG
- HH:MM [beskrivelse]
```

### Step 4: Daily Note (optional)

If a daily note doesn't already exist for today, create one at:
`/Users/nitromini/Documents/vault/01-Daily/YYYY-MM-DD.md`

Check vault CLAUDE.md for the daily note template before creating.

Only create if the file doesn't exist yet. Never overwrite an existing daily note.

## Rules

- Use the injected date/time above. Do NOT run `date` separately.
- All times in Norwegian time (CET/CEST)
- Flag conflicts or double-bookings prominently
- Flag overdue tasks with [!]
- If a data source fails, note it briefly ("Kalender: feil ved henting") and continue
- Norwegian in brief output, English in any vault files
- No em dashes ever
- No "Certainly!", "Great question!", or any AI cliches
