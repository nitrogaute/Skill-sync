---
name: tana-inbox-processor
version: "1.0.0"
description: Process Tana inbox with intelligent content extraction for YouTube videos, articles, and links
author: nitromini
user-invocable: true
allowed-tools:
  - Bash
  - Read
triggers:
  - "process inbox"
  - "clear inbox"
  - "tana inbox"
  - "inbox processor"
metadata: {"clawdbot":{"emoji":"📥","requires":{"bins":["jq","curl"]},"optional":{"bins":["yt-dlp"]}}}
---

# Tana Inbox Processor

Process inbox items with automatic content extraction for YouTube videos, articles, and links.

## Usage

```bash
# Run inbox processor
{baseDir}/scripts/process-inbox.sh

# Dry run (no changes)
{baseDir}/scripts/process-inbox.sh --dry-run
```

## What It Does

1. Fetches unprocessed inbox items from Tana
2. Detects content type (YouTube, article, link, text)
3. Extracts metadata (title, description, channel, duration)
4. Creates enriched Tana nodes with proper tags
5. Moves items to appropriate folders (References, Notes, Ideas, Today)

## Content Type Detection

| Type | Detection | Extraction |
|------|-----------|------------|
| YouTube | `youtube.com/watch`, `youtu.be/`, `youtube.com/shorts` | Title, channel, duration via yt-dlp |
| Article | URL with `text/html` content-type | Open Graph metadata |
| Link | Other URLs | Basic title extraction |
| Text | Non-URL content | Action verb detection for todos |

## Destination Routing

- **#reference** items -> References folder
- **#todo** items -> Today's date node
- **#note** items -> Notes folder
- **#idea** items -> Ideas folder
- **#goal** items -> Skipped (should not be in inbox)

## Dependencies

Required:
- `jq` - JSON processing
- `curl` - Web fetching
- `mcporter` - Tana MCP integration

Optional:
- `yt-dlp` - Enhanced YouTube metadata extraction (gracefully degrades without it)

## Examples

**Manual processing:**
```bash
/tana-inbox-processor
```

**Check what would happen:**
```bash
/tana-inbox-processor --dry-run
```

## Scheduled Execution

The inbox processor runs automatically every hour via cron. Check the schedule:
```bash
$HOME/tana-scripts/setup-cron.sh --list
```

## Logs

Logs are stored in `$HOME/tana-scripts/logs/`:
- `inbox-processor-YYYYMMDD-HHMMSS.log` - Per-run logs
- `inbox-processor.log` - Cron job output
- `content-extractors.log` - Extraction details
