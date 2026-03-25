---
name: daily-brief
description: Daily morning briefing for Gaute. Checks calendar (all 3 calendars), unread emails, tasks, and scheduled reminders. Use when Gaute asks for a brief, morning update, "hva skjer i dag", or starts the day.
disable-model-invocation: true
allowed-tools: Bash, Skill, Read, Grep, Glob
---

# Daily Brief

Current date and time:
! `date "+%A %d. %B %Y %H:%M %Z"`

Generate a concise daily briefing for Gaute. Norwegian language, tight format.

## Data to collect (run in parallel where possible)

### 1. Calendar - Today's schedule
Fetch events from ALL 3 calendars (Home, Shared, KM_2) for today.
Use `gws calendar events list` or `gog calendar events`.
Include: time, title, location, attendees for each event.
Note: KM_2 has daily 08-09 training block.

### 2. Email - Unread inbox
Use `gws gmail messages list --params '{"maxResults": 10, "q": "is:unread"}'` or the gmail skill.
Show: sender, subject, urgency indicator.
Group by: action needed vs FYI.

### 3. Tasks
Check TickTick via MCP for today's tasks and overdue items.
If TickTick unavailable, check scheduled_tasks in SQLite: `sqlite3 /Users/nitromini/ClaudeClaw/store/claudeclaw.db "SELECT * FROM scheduled_tasks WHERE status = 'active';"`

### 4. Weather (optional)
If available, include Stavanger weather summary.

## Output format

Keep it tight. No fluff. Norwegian. No em dashes.

```
BRIEF [dato]

KALENDER
- 08:00 Trening (KM_2)
- 09:30 Standup med teamet
- 14:00 Mote med [person] - [tema]

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
- 10:00 [beskrivelse]
```

## Example output

```
BRIEF tirsdag 18. mars 2026

KALENDER
- 08:00 Trening (KM_2)
- 09:00 Standup DevOps
- 10:30 Mote med Frode - NEL kontrakt
- 14:00 Styremotet GTB Ventures

INBOX (4 uleste)
Trenger handling:
- Martin Skog: Re: Startup-evaluering Q2
- Isabelle Dahl: ERP-nummer mangler for TO-003
FYI:
- HR KM: Oppdatert reisepolicy
- Garmin: Ukentlig treningsrapport

TASKS
- [ ] Oppdater HydePoint chief engineer skill
- [ ] Sjekk Stitch 2.0
- [!] Forfalt: Send tilbud til NEL

PAMINNELSER I DAG
- 10:00 Ring Isabelle om ERP
- 12:30 Sjekk KM AI-strategi notat
```

## Rules
- Use the injected date/time above. Do NOT run `date` separately.
- All times in Norwegian time (CET/CEST)
- Flag conflicts or double-bookings
- Flag overdue tasks prominently
- If a data source fails, note it briefly and continue with the rest
- No em dashes. Use regular hyphens.
- No AI cliches. No "Certainly!", "Great question!", etc.
