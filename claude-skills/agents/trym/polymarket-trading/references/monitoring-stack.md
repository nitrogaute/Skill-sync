# Monitoring Stack & Operational Cadence

## Sentinel Scripts (added 2026-03-19)

```
scripts/
├── news_sentinel.py      # RSS + Twitter/Nitter monitoring (5-min cron)
├── price_sentinel.py     # Position price + BTC/ETH spot monitoring (5-min cron)
├── sentinel_cron.sh      # Wake wrapper for news sentinel
└── sentinel_state.json   # Dedup state for news
    price_state.json      # Price history for comparison
```

- **News Sentinel:** 4 RSS feeds + 5 Twitter accounts via Nitter (failover across 4 instances)
- **Price Sentinel:** Alerts on >5% position moves or >4% BTC/ETH moves in 30-min window
- **Twitter accounts:** @JavierBlas, @BNONews, @ELINTNews, @TheInsiderPaper, @zaborowski_m
- **Cron IDs:** news-sentinel (f09c7a92), price-sentinel (eb6d5804)

## Deep Eval Sessions (Adaptive Spawning)

| Cron | Oslo | Purpose |
|------|------|---------|
| `pm-eval-eu-open` | 08:00 | Pre-EU news. Research ready. |
| `pm-eval-us-open` | 14:30 | Most important — pre-US futures. Full scan + analysis. |
| `pm-eval-us-close` | 22:00 | Post-settlement. Daily P&L. **Touchpoint report.** |
| `pm-eval-asia` | 02:00 | Overnight developments. Silent unless actionable. |

## Lightweight Checks (PM Only — Zero Specialist Tokens)

- **Stoploss** — every 15 min: `check_stoploss.py` + `reconcile.py`. Spawn only if alerts.
- **Auto-scan** — hourly: `auto_scan.sh`. Spawn Analyst only if opportunities. Three empty scans → trigger deep eval.
- **Daily critique** — 21:00: Spawn Retrospector only if trades closed today.

## Token Efficiency (with Model Tiering)

- Idle eval: PM Opus only → near-zero specialist tokens
- Opportunity rejected: PM Opus + Analyst Opus + Risk Sonnet → ~2.2x
- Full trade cycle: + Execution Haiku + Monitor Haiku → ~2.5x
- Full deep eval: ~3.5x (vs ~7x if all-Opus)

## PM Watchdog — Two-Layer Fallback

### Layer 1: OpenClaw Heartbeat (primary — intelligent)

An OpenClaw scheduled task (`pm-heartbeat`) runs every 30 minutes independently of the PM session. Because it's a Claude session, it can assess the situation and act.

The heartbeat task:
1. Runs `scripts/reconcile.py` and `scripts/check_stoploss.py` directly
2. Checks `team_context.md` freshness — if stale >2 hours, PM is likely stalled
3. Checks if scheduled deep evals are producing output — if the last eval log is >6 hours old, PM may have stopped running
4. If stoploss breach detected → executes emergency exit via `trade.py`
5. Sends Telegram alert to Gaute with status and any actions taken

### Layer 2: Cron Watchdog (backup — dead-man's switch)

`scripts/watchdog.py` runs via cron every 30 minutes as a pure Python script. Does NOT depend on Claude or OpenClaw.

Three mechanical checks:
1. Was `team_context.md` updated in the last 2 hours?
2. Was `check_stoploss.py` run in the last 30 minutes?
3. Are any positions past -25% right now?

If any check fails → sends Telegram alert to Gaute. For v1, alert-only (no auto-execution).

### Why Two Layers
The heartbeat handles 99% of PM stall scenarios with intelligence. The cron script catches the edge case where OpenClaw itself is down.
