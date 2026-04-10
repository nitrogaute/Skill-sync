---
name: claudeclaw-dev
description: ClaudeClaw development patterns, architecture, and conventions
---
# ClaudeClaw Development Guide

## Architecture
- **agent.ts**: Claude Agent SDK wrapper. Handles streaming, hooks, retries, AbortController timeout.
- **bot.ts**: Grammy Telegram bot. Routes messages, manages sessions per topic (forum support).
- **db.ts**: SQLite with WAL. Tables: sessions, memories (FTS5), scheduled_tasks.
- **memory.ts**: Semantic/episodic memory with salience decay (0.98x/day).
- **format.ts**: Markdown to Telegram HTML converter.
- **scheduler.ts**: Cron task runner (60s poll, 90s dedup window, Europe/Oslo timezone).

## Key Patterns
- Session keying: `chatId` for DM, `chatId:threadId` for forum topics
- Agent SDK: `query()` returns async generator of events (system, assistant, tool_progress, stream_event, result)
- Streaming: `onTextDelta` accumulates in buffer, flushed every 2s to Telegram via message edit
- Hooks: `PreToolUse`/`PostToolUse` track tool timing via Map
- Error handling: 2 retries with session reset, HTML fallback to plain text

## Testing
- `npx vitest run` -- full suite
- `npx vitest run src/__tests__/agent.test.ts` -- agent only
- Mock SDK with `makeAsyncGenerator()` helper
- Use `vi.useFakeTimers()` for timeout tests

## Build
- `npm run build` -- TypeScript to dist/
- `npm run dev` -- tsx direct execution
- `npm run typecheck` -- tsc --noEmit
