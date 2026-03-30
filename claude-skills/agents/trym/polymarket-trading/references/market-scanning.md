# Market Scanning — Think Broadly

**We are NOT limited to energy and crypto.** Polymarket has thousands of markets. Any event with a mispriced probability is a trading opportunity.

## Opportunity Categories to Scan

| Category | Examples | Crisis Connection |
|----------|---------|-------------------|
| **Energy** | Oil barriers, gas prices, OPEC | Direct impact |
| **Crypto** | BTC/ETH dips, crashes | Risk-off from energy shock |
| **Geopolitical** | Iran, ceasefire, regime, nuclear | Direct conflict |
| **Macro/Recession** | Fed rates, CPI, recession, unemployment | Oil shock → stagflation |
| **Equities** | S&P crash, sector moves, VIX | Market selloff |
| **Commodities** | Gold, wheat, fertilizer, metals | Safe haven + supply disruption |
| **Shipping/Trade** | Hormuz, Suez, shipping rates | Supply chain disruption |
| **Politics** | Elections, polls, policy changes | War affects elections |
| **Currencies** | USD, EUR, emerging markets | Oil shock → FX moves |
| **Agriculture/Food** | Wheat, fertilizer prices | Hormuz shutdown → food crisis |
| **Airlines/Travel** | Fuel costs, route changes | Jet fuel spike |
| **Insurance/Reinsurance** | Cat bonds, risk pricing | War risk repricing |
| **EU/Domestic politics** | Energy policy, sanctions votes | Crisis drives policy |

## Scanning Mandate

- **Every deep eval:** Scan ALL categories, not just current positions
- **Every sentinel alert:** Ask "what second-order markets does this affect?"
- **Hedging:** Always look for hedges against biggest exposure
- **Asymmetric priority:** Cheap YES bets ($0.03-0.30) with crisis catalysts get priority
- **Uncorrelated bets:** Actively seek markets NOT correlated with largest cluster

## Scan Script Enhancement

`scan_markets.py` currently filters too narrowly. When scanning, also search for:
- Markets created in the last 48h (new crisis-response markets)
- Markets with volume spikes (>2x 7-day avg = something happening)
- Markets where YES is $0.05-0.35 with >$10K liquidity (asymmetric sweet spot)
