---
name: ai-dip-score
description: Score high-volatility AI theme stocks and 2x ETFs for pullback dip-buy setups, observation zones, trial entries, hold/reduce/take-profit/stop-loss reminders, and "do not chase" warnings. Use when the user asks to evaluate AI stocks such as MU, DRAM, QCOM, COHR, COHX, DELL, ARM, AVGO, NVDA, MRVL, AMD, SMCI, ORCL, or asks for a low-buy score, dip-buy watchlist, ETF holding discipline, or AI mainline short-term swing trading decision aid.
---

# AI Dip Score

Use this skill to produce a concise, rules-based low-buy score for AI mainline stocks and related 2x ETFs. Treat it as a quantitative decision aid, not a deterministic buy or sell instruction.

## Core Rule

First judge the underlying stock, then map the result to the related ETF if applicable. Fixed price levels are observation lines only; final output must come from the scoring model.

The strategy favors:

- Strong AI mainline names after a rational pullback
- Confirmed support or intraday recovery
- Intact AI logic
- Market conditions that are not still one-way down
- Short-term ETF use with strict stop-loss and staged take-profit discipline

Avoid:

- Chasing names near fresh highs
- Buying 2x ETFs before the underlying stock confirms support
- Treating a deep fall as automatically cheap
- Holding 2x ETFs as long-term conviction positions

## Workflow

1. Collect available inputs: ticker, current or after-hours price, recent stage high, 5/10/20-day moving averages, intraday low, volume or reversal evidence, AI logic/news state, broader market state, and existing holding if any.
2. If live market data is required, use a current data source before scoring. If only user-provided prices are available, state that the score is based on those inputs.
3. Read [references/scoring-rules.md](references/scoring-rules.md) when applying the detailed watchlist, observation lines, scoring thresholds, stop-loss rules, and holding rules.
4. For repeatable scoring, run [scripts/score_ai_dip.py](scripts/score_ai_dip.py) with JSON input.
5. Output a compact table. Keep analysis short and action-oriented.

## Output Contract

Prefer this table:

| 标的 | 当前价/夜盘价 | 阶段高点 | 回撤 | 低吸评分 | 结论 | 操作 |
| --- | ---: | ---: | ---: | ---: | --- | --- |

Allowed conclusions:

- 符合规则
- 可小仓试探
- 进入观察区
- 等确认
- 不低吸
- 不追高
- 持有观察
- 分批止盈
- 严格止损

Allowed actions:

- 可小仓
- 等站回关键位
- 等回踩
- 不买
- 持有
- 减仓
- 清仓
- 分批止盈

## Script Use

Create an input JSON like:

```json
{
  "market_state": "sideways_ai_strong",
  "items": [
    {
      "ticker": "ARM",
      "current": 384.94,
      "recent_high": 452.70,
      "ma5": 398,
      "ma10": 390,
      "ma20": 370,
      "support_signal": "reclaimed_key_level",
      "logic_state": "mainline_intact"
    }
  ]
}
```

Then run:

```bash
python3 scripts/score_ai_dip.py input.json
```

The script prints a Markdown table and a compact notes block. Review the result before answering, especially when news, after-hours moves, liquidity, or holding-specific rules matter.
