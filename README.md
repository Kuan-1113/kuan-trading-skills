# Kuan Trading Skills

Quantitative trading skills for Claude Code — Taiwan stocks, crypto, futures, and risk management.

## Skills

### `/taiwan-stock-scan`
Taiwan equity signal scanner using 9-Agent joint scoring (TrendAgent, MomentumAgent, VolumeAgent, ChipAgent, VolatilityAgent, KeltnerAgent, FundamentalAgent, NewsAgent, SentimentAgent). Outputs ★★★/★★/★ rated signals with entry price, stop-loss, and analysis rationale. Targets 70–75% win rate.

### `/crypto-trend`
Multi-strategy confluence analysis for cryptocurrency pairs using **live Binance data via CCXT**. 11 strategies across 4 gates. Outputs STRONG/MODERATE/WEAK signal with layered exit targets (Exit A: 40% position, Exit B: 60% position). Targets 87.5% win rate on trending setups.

### `/quant-report`
Generate structured performance reports from signal history data. Calculates win rates by star rating and agent, ranks indicator performance, and produces NotebookLM-ready analysis questions.

### `/futures-query`
Taiwan futures contract reference — 台指期, 小台, 電子期, 金融期, and US index futures. Includes margin requirements, P&L simulation, and liquidation warning calculator.

### `/position-size`
Optimal position sizing using Kelly Criterion, risk-based, or fixed fractional methods. Supports stocks (張) and futures (口). Input your account size, entry, and stop-loss — get the recommended position with full risk breakdown.

### `/fear-greed`
Real-time market sentiment — fetches live **Crypto Fear & Greed Index** (alternative.me) and **CNN Fear & Greed Index**. Shows current score, trend vs yesterday, and trading implications.

## Installation

```bash
claude plugins install Kuan-1113/kuan-trading-skills
```

Or clone manually:
```bash
git clone https://github.com/Kuan-1113/kuan-trading-skills ~/.claude/plugins/kuan-trading-skills
```

## Usage

```
/taiwan-stock-scan     # Scan Taiwan stocks for signals
/crypto-trend          # Analyze a crypto pair with live data
/quant-report          # Generate performance report
/futures-query         # Taiwan futures specs & margin calc
/position-size         # Calculate optimal position size
/fear-greed            # Live market sentiment index
```

## Author

[Kuan-1113](https://github.com/Kuan-1113) — Quantitative trading systems for Taiwan equities and crypto markets.
