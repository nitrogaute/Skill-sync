# Project Layout

```
~/clawd/projects/polymarket-bot/
├── trade.py              # CLI trade executor (buy/sell/positions/balance)
├── dashboard.py          # Portfolio dashboard → screenshot via dashboard_compact.html
├── validate.py           # Number verification (run before deploy)
├── stoploss_monitor.py   # Checks all on-chain positions
├── trade_ledger.json     # Trade log (not ground truth — on-chain is)
├── closed_trades.json    # Closed position summaries
├── team_context.md       # Shared specialist context (update after every eval)
├── scripts/
│   ├── reconcile.py      # On-chain ↔ ledger reconciliation
│   ├── track_clv.py      # CLV snapshots + edge measurement
│   ├── stale_line_monitor.py
│   ├── scan_markets.py   # Market scanner with GBM + Kelly
│   ├── kelly_calc.py     # Quick Kelly sizing CLI
│   ├── auto_scan.sh      # Zero-token scanning
│   ├── check_stoploss.py # Lightweight stoploss checker
│   ├── trading_status.py # Full status report
│   ├── news_sentinel.py  # RSS + Twitter/Nitter monitoring
│   ├── price_sentinel.py # Position price + BTC/ETH spot monitoring
│   ├── sentinel_cron.sh  # Wake wrapper for news sentinel
│   └── watchdog.py       # Dead-man's switch (cron-based)
└── public/index.html     # Dashboard HTML
```

## Key Paths

- **Dashboard:** Local only (Vercel dropped). Screenshot via `dashboard_compact.html` → Telegram.
- **Wallet:** `0x3df911149339B7eD777cFC340FFC01c2F3A12e43`
- **Private key:** macOS Keychain `polymarket-private-key`

## Auto-Learning System (capture_learning.py)

**Every exit MUST call this script.** No exceptions.

```bash
python3 scripts/capture_learning.py \
  --market "Market name" \
  --entry 0.XX --exit 0.XX --pnl "-X.XX" \
  --reason "stoploss|edge_evaporated|thesis_invalid|time_decay|manual" \
  --learning "One sentence: what happened and what to do differently" \
  [--new-rule "Rule text if this is a new systemic failure"]
```

**What it does automatically:**
1. Appends postmortem to `references/learnings-log.md`
2. Saves structured data to `references/learnings-structured.json`
3. If `--new-rule`: adds numbered rule to `references/hard-rules.md`
4. Runs pattern detection on last 10 trades — flags recurring failures:
   - 3+ stoplosses → suggests tightening entry criteria
   - 2+ CLV exits → suggests earlier CLV checking
   - 2+ illiquidity events → suggests minimum liquidity filter

**When to add `--new-rule`:**
- First time seeing a failure mode → add rule
- Repeat of known failure → skip (pattern detector handles it)
- System/process failure (not trade) → add rule with category "system"
