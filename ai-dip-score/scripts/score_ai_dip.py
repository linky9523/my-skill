#!/usr/bin/env python3
"""Score AI pullback setups from user-provided market inputs."""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


MARKET_SCORES = {
    "strong_rebound": 10,
    "sideways_ai_strong": 8,
    "slightly_down_resilient": 6,
    "one_way_down": 2,
    "panic": 0,
}

SUPPORT_SCORES = {
    "one_way_down": 3,
    "no_clear_rebound": 8,
    "reclaimed_key_level": 15,
    "long_lower_shadow": 18,
    "after_hours_reclaim": 20,
    "volume_reversal": 25,
}

LOGIC_SCORES = {
    "improving": 20,
    "mainline_intact": 15,
    "market_drag": 12,
    "company_negative": 5,
    "invalidated": 0,
}

ETF_UNDERLYING = {
    "DRAM": "MU",
    "COHX": "COHR",
}

OBSERVATION_LINES = {
    "MU": 1000,
    "QCOM": 200,
    "COHR": 370,
    "DELL": 400,
}

HOLDINGS = {
    "DRAM": {"quantity": 10, "cost": 70.9},
    "COHX": {"quantity": 9, "cost": 53.4},
}


@dataclass
class ScoreResult:
    ticker: str
    current: float | None
    recent_high: float | None
    drawdown: float | None
    score: int | None
    conclusion: str
    action: str
    notes: list[str]


def as_float(value: Any) -> float | None:
    if value in (None, ""):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def price_pullback_score(drawdown: float | None) -> int:
    if drawdown is None:
        return 0
    pct = -drawdown * 100
    if pct < 5:
        return 5
    if pct < 8:
        return 10
    if pct < 12:
        return 18
    if pct < 18:
        return 25
    if pct <= 25:
        return 22
    return 8


def trend_score(current: float | None, ma5: float | None, ma10: float | None, ma20: float | None) -> tuple[int, str]:
    if current is None:
        return 0, "缺少当前价"
    if ma20 and current < ma20 * 0.985:
        return 4, "跌破20日线"
    if ma20 and abs(current / ma20 - 1) <= 0.025:
        return 20, "回踩20日线附近"
    if ma10 and abs(current / ma10 - 1) <= 0.025:
        return 15, "回踩10日线附近"
    if ma5 and abs(current / ma5 - 1) <= 0.02:
        return 10, "回踩5日线附近"
    if ma5 and current > ma5 * 1.04:
        return 5, "距离5日线偏远"
    return 8, "趋势位置一般"


def conclusion_action(score: int, market_state: str, support_signal: str, chase_risk: bool) -> tuple[str, str]:
    if chase_risk:
        return "不追高", "等回踩"
    if market_state in {"one_way_down", "panic"} and score < 85:
        return "等确认", "不买"
    if score >= 85:
        return "符合规则", "可小仓"
    if score >= 75 and support_signal not in {"one_way_down", "no_clear_rebound"}:
        return "可小仓试探", "可小仓"
    if score >= 65:
        return "进入观察区", "等站回关键位"
    if score >= 60:
        return "等确认", "不买"
    return "不低吸", "不买"


def holding_overlay(ticker: str, current: float | None, row: dict[str, Any], conclusion: str, action: str, notes: list[str]) -> tuple[str, str]:
    upper = ticker.upper()
    if upper == "COHX":
        cohr = as_float(row.get("underlying_price"))
        if current is not None and current >= 65:
            return "分批止盈", "清仓"
        if current is not None and 60 <= current < 65:
            notes.append("COHX到60-62可先卖部分锁定利润，65附近优先清仓纪律。")
            return "分批止盈", "分批止盈"
        if cohr is not None and cohr < 370:
            return "严格止损", "减仓"
        if cohr is not None and cohr < 380:
            return "严格止损", "减仓"
        return "持有观察", "持有"
    if upper == "DRAM":
        mu = as_float(row.get("underlying_price"))
        if mu is not None and mu < 950:
            return "严格止损", "减仓"
        if row.get("underlying_stagnating") is True:
            return "分批止盈", "分批止盈"
        return "持有观察", "持有"
    return conclusion, action


def score_item(row: dict[str, Any], default_market_state: str) -> ScoreResult:
    ticker = str(row.get("ticker", "")).upper()
    current = as_float(row.get("current"))
    recent_high = as_float(row.get("recent_high"))
    drawdown = None
    if current is not None and recent_high and recent_high > 0:
        drawdown = current / recent_high - 1

    ma5 = as_float(row.get("ma5"))
    ma10 = as_float(row.get("ma10"))
    ma20 = as_float(row.get("ma20"))
    support_signal = str(row.get("support_signal", "no_clear_rebound"))
    logic_state = str(row.get("logic_state", "mainline_intact"))
    market_state = str(row.get("market_state", default_market_state))

    notes: list[str] = []
    pullback = price_pullback_score(drawdown)
    trend, trend_note = trend_score(current, ma5, ma10, ma20)
    support = SUPPORT_SCORES.get(support_signal, 8)
    logic = LOGIC_SCORES.get(logic_state, 15)
    market = MARKET_SCORES.get(market_state, 6)
    score = pullback + trend + support + logic + market

    if drawdown is not None and drawdown > -0.05 and current is not None:
        notes.append("回撤不足5%，优先视为追高或等回踩。")
    if logic_state in {"company_negative", "invalidated"}:
        notes.append("公司级逻辑受损，跌幅不能自动视为机会。")
    if ticker in ETF_UNDERLYING:
        notes.append(f"{ticker}必须先看底层{ETF_UNDERLYING[ticker]}确认。")
    if ticker in OBSERVATION_LINES and current is not None and current <= OBSERVATION_LINES[ticker]:
        notes.append(f"已触及用户观察线{OBSERVATION_LINES[ticker]}，仍需承接确认。")
    notes.append(trend_note)

    chase_risk = drawdown is not None and drawdown > -0.05
    conclusion, action = conclusion_action(score, market_state, support_signal, chase_risk)
    if ticker in HOLDINGS:
        conclusion, action = holding_overlay(ticker, current, row, conclusion, action, notes)

    return ScoreResult(ticker, current, recent_high, drawdown, score, conclusion, action, notes)


def fmt_price(value: float | None) -> str:
    return "-" if value is None else f"{value:.2f}"


def fmt_drawdown(value: float | None) -> str:
    return "-" if value is None else f"{value * 100:.1f}%"


def render(results: list[ScoreResult]) -> str:
    lines = [
        "| 标的 | 当前价/夜盘价 | 阶段高点 | 回撤 | 低吸评分 | 结论 | 操作 |",
        "| --- | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for r in results:
        score = "-" if r.score is None else str(r.score)
        lines.append(
            f"| {r.ticker} | {fmt_price(r.current)} | {fmt_price(r.recent_high)} | "
            f"{fmt_drawdown(r.drawdown)} | {score} | {r.conclusion} | {r.action} |"
        )
    note_lines = []
    for r in results:
        compact = "；".join(dict.fromkeys(r.notes))
        if compact:
            note_lines.append(f"- {r.ticker}: {compact}")
    if note_lines:
        lines.extend(["", "备注:", *note_lines])
    return "\n".join(lines)


def load_payload(path: str) -> dict[str, Any]:
    if path == "-":
        return json.load(sys.stdin)
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: score_ai_dip.py input.json", file=sys.stderr)
        return 2
    payload = load_payload(sys.argv[1])
    default_market_state = str(payload.get("market_state", "slightly_down_resilient"))
    items = payload.get("items", [])
    if not isinstance(items, list) or not items:
        print("input.json must contain a non-empty items list", file=sys.stderr)
        return 2
    results = [score_item(item, default_market_state) for item in items]
    print(render(results))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
