# AI Low-Buy Scoring Rules

## Strategy Objective

Track hot AI-related stocks and related 2x ETFs for short-term or swing pullback opportunities. The user has small capital, seeks high return, prefers high-volatility AI mainline names, and often uses 2x ETFs to amplify rebounds.

The skill must not provide certain buy/sell commands. It should output:

- Whether the name is in a low-buy observation zone
- Current low-buy score
- Whether small-position trial entry is reasonable
- Whether to continue watching
- Whether the setup is too extended to chase
- Holding reminders: hold, reduce, take profit, or stop loss

## Watchlist

| Ticker | Logic | Trading Use |
| --- | --- | --- |
| MU | AI storage, DRAM/HBM | Judge DRAM ETF strength |
| DRAM | Storage industry ETF | Key holding and storage mainline tool |
| QCOM | Edge AI, AI data center, low-power AI compute | Pullback rebound candidate |
| COHR | AI optical communication, modules, data center chain | Judge COHX strength |
| COHX | 2x COHR ETF | High-volatility rebound tool |
| DELL | AI servers and infrastructure delivery | Strong-trend pullback/breakout |
| ARM | AI compute architecture, IP licensing, data center CPU story | High-valuation rebound candidate |
| AVGO | AI ASIC, custom silicon, networking chips | Higher-quality AI pullback candidate |
| NVDA | AI GPU core leader | Mainline sentiment anchor |
| MRVL | AI custom silicon and data center networking | High-volatility rebound watch |
| AMD | AI GPU/CPU | Mainline catch-up watch |
| SMCI | AI servers | Observe only, not priority |
| ORCL | AI cloud infrastructure | Observe only, not priority |

## Observation Lines

These are alert lines only, not buy points.

| Ticker | User Observation Line |
| --- | --- |
| MU | Below 1000 |
| QCOM | Below 200 |
| COHR | Below 370 |
| DELL | Below 400 |
| ARM | No fixed line; judge pullback from recent high |
| AVGO | No fixed line; judge pullback from recent high |
| NVDA | No fixed line; judge pullback from recent high |
| MRVL | No fixed line; judge pullback from recent high |

## Score Formula

Total score = price pullback + trend location + support signal + fundamental logic + market environment.

| Module | Weight |
| --- | ---: |
| A. Price pullback | 25 |
| B. Trend location | 20 |
| C. Support signal | 25 |
| D. Fundamental logic | 20 |
| E. Market environment | 10 |

## A. Price Pullback, 25 Points

Current drawdown = current price / recent stage high - 1.

| Drawdown | Score |
| --- | ---: |
| Less than 5% | 5 |
| 5%-8% | 10 |
| 8%-12% | 18 |
| 12%-18% | 25 |
| 18%-25% | 22 |
| More than 25% | Do not auto-add; check whether logic is broken |

Ideal zones:

| Type | Ideal Pullback |
| --- | --- |
| Strong-trend AI leader | 8%-12% |
| High-volatility AI hardware | 12%-18% |
| News-driven rerating name | 15%-25% |
| Broken-trend stock | Do not buy merely because it fell |

## B. Trend Location, 20 Points

| Price Location | Score |
| --- | ---: |
| High above 5-day moving average, insufficient pullback | 5 |
| Pullback near 5-day moving average | 10 |
| Pullback near 10-day moving average | 15 |
| Pullback near 20-day moving average without effective breakdown | 20 |
| Breaks below 20-day and cannot reclaim | 0-5 |

Prioritize 10-day and 20-day pullbacks for strong AI stocks. If price is far above moving averages after an after-hours surge, treat as chase risk.

## C. Support Signal, 25 Points

| Support Shape | Score |
| --- | ---: |
| One-way down, no rebound | 0-5 |
| Hits observation zone with no clear rebound | 8 |
| Breaks key price then quickly reclaims | 15 |
| Long lower shadow | 18 |
| High-volume bullish reversal over prior red candle | 25 |
| After-hours rebound and reclaim of key level | 18-22 |

Priority:

1. Did it break then reclaim a key price?
2. Did it rebound clearly from the intraday low?
3. Did it reclaim an important round number or moving average?
4. Did volume confirm the rebound?
5. Did other AI mainline names strengthen at the same time?

## D. Fundamental Logic, 20 Points

| Logic State | Score |
| --- | ---: |
| Earnings, guidance, orders, or AI narrative improves | 20 |
| No new negative news; mainline still intact | 15 |
| Falling only with the broader market | 12 |
| Company-specific negative news | 0-5 |
| Earnings invalidation or guidance cut | 0 |

Ticker logic:

| Ticker | Core Logic |
| --- | --- |
| MU / DRAM | AI storage, DRAM/HBM price increases, storage cycle upturn |
| QCOM | Edge AI, data center CPU, Meta cooperation, low-power AI compute |
| COHR / COHX | AI optical communications, data center optical modules, laser/optics |
| DELL | AI server orders, AI data center delivery, EPS revisions |
| ARM | AI compute architecture, IP licensing, data center CPU, power efficiency |
| AVGO | AI ASIC, custom chips, networking chips |
| NVDA | AI GPU leader and mainline sentiment anchor |
| MRVL | AI networking, custom chips, data center connectivity |

## E. Market Environment, 10 Points

| Market State | Score |
| --- | ---: |
| Nasdaq or semiconductor index strong rebound | 10 |
| Market sideways, AI mainline strong | 8 |
| Market slightly down, target stock resilient | 6 |
| Market one-way selling | 2 |
| Panic selloff | 0 unless strong late recovery |

Do not recommend buying 2x ETFs when the market is still one-way down. If the target stock is resilient or rising against the market, support score may improve. If AI mainline names weaken together, reduce all scores.

## Result Interpretation

| Score | Conclusion | Action |
| ---: | --- | --- |
| 85+ | High-quality low-buy point | Consider 2x ETF only with position control |
| 75-84 | Trial entry | Light position only, wait for confirmation |
| 65-74 | Observation zone | Do not rush; wait to reclaim key level |
| 60-64 | Weak observation | Do not buy yet |
| Below 60 | Not qualified | Do not buy; avoid chasing or catching falling knife |

Only output "可小仓试探" when:

1. The name is a strong AI mainline stock.
2. Pullback from recent high is rational.
3. Price is near key support, moving average, or observation line.
4. A support signal appears.
5. Broader market is not still one-way down.
6. Related 2x ETF has no obvious liquidity issue.

## Stop-Loss Rules

2x ETFs require strict stop loss. Reduce or exit if the underlying stock breaks key support and cannot reclaim it, if the expected rebound does not occur, or if the core logic receives a major negative shock.

| Ticker | Failure Condition |
| --- | --- |
| MU | Breaks recent support low and cannot reclaim, or breaks 950 area |
| QCOM | Breaks 190 and cannot reclaim; below 180 pause trading |
| COHR | Breaks 360 and cannot reclaim; below 350 trend weakens |
| DELL | Breaks 390 and cannot reclaim |
| ARM | Breaks previous low and cannot reclaim |
| AVGO | Breaks recent support and cannot reclaim |
| NVDA | Breaks round number or recent low and cannot reclaim |
| MRVL | Breaks recent low and cannot reclaim |

## Take-Profit Rules

Take profit when:

1. Price rebounds near previous high.
2. It spikes but cannot continue.
3. High-volume stagnation appears.
4. After-hours ETF surges but underlying stock cannot break out.
5. 2x ETF reaches target price.
6. Underlying is strong but ETF does not follow.

Preferred exit:

- Sell 1/3 at first resistance.
- Sell 1/3 at second resistance.
- Sell the rest if momentum turns down or stagnates.
- Prioritize discipline when a 2x ETF reaches target price.

## Current Holding Rules

| Holding | Quantity | Cost |
| --- | ---: | ---: |
| DRAM | 10 | 70.9 |
| COHX | 9 | 53.4 |

DRAM:

- Judge by MU and storage mainline strength.
- If MU keeps making new highs, DRAM may continue to hold.
- If MU makes a new high then stagnates, moves sideways, or turns down, DRAM should start staged selling.
- If MU breaks key support, DRAM should reduce.
- Do not add DRAM when MU has already surged near new highs.

COHX:

- Judge mainly by COHR.
- User target is near 65 for full exit.
- If COHX reaches 60-62, sell part to lock profit.
- If COHR breaks 410 and keeps strengthening, COHX can continue toward 65.
- If COHR breaks 380, reduce COHX.
- If COHR breaks 370, do not hesitate.
