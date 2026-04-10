# Polymarket API Patterns

## APIs
| API | Base URL | Auth | Purpose |
|-----|----------|------|---------|
| Gamma | `gamma-api.polymarket.com` | None | Markets, events, search |
| CLOB | `clob.polymarket.com` | L2 HMAC | Orderbook, orders, trades |

## Finding Markets
```python
# NEVER use slug, slug_contains, _q, or tag params — returns WRONG markets!
# ALWAYS fetch all and filter locally:
url = f"{GAMMA_API}/markets?active=true&closed=false&limit=500&order=volume24hr&ascending=false"
markets = [m for m in all_markets if "keyword" in m["question"].lower()]
```

## Token ID → Market Name Lookup
```python
# Use clob_token_ids param — ONLY reliable way
url = f"{GAMMA_API}/markets?clob_token_ids={token_id}&limit=1"
# ⚠️ conditionId param returns WRONG results. Don't use it.
```

## Placing Orders
```python
from py_clob_client.clob_types import OrderArgs, PartialCreateOrderOptions
from py_clob_client.order_builder.constants import BUY, SELL

# ALWAYS use neg_risk=False (py-clob-client 0.34.6 bug)
opts = PartialCreateOrderOptions(tick_size='0.01', neg_risk=False)
client.create_and_post_order(
    OrderArgs(token_id=FULL_TOKEN_ID, price=0.47, size=10, side=BUY), opts
)
```

## Critical Rules
- **Minimum order size:** 5 shares
- **neg_risk=True causes "invalid signature"** on both BUY and SELL. Always use False.
- **Token IDs** must be FULL length (76+ chars)
- **NO tokens:** Get from `clobTokenIds[1]` in Gamma response. Different from YES token.
- **NegRisk order books:** Show extreme spreads ($0.001/$0.999). Use Gamma `outcomePrices` for real values.
- **CLOB `get_trades()`:** Misses taker fills. Use `trade_ledger.json` as source of truth.
- **Batch trading:** Deploy in 5-share chunks for NegRisk markets.
- **After sells:** USDC.e may not be immediately available. Try smaller amounts.

## Collateral
- Polymarket uses **USDC.e** (bridged): `0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174`
- NOT native USDC. Swap via Uniswap V3 (fee tier 100 = 0.01%)
- Approve: USDC.e → CTF Exchange + NegRisk Exchange + NegRisk Adapter (already done, infinite approval)

## Ledger entries for NO positions
MUST include `"outcome": "No"` AND correct NO token_id (from `clobTokenIds[1]`)
Dashboard keys on market+outcome to separate YES/NO on same market.
