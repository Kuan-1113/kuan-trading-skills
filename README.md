# Kuan Trading Skills

Quantitative trading skills for Claude Code — Taiwan stocks and crypto signal analysis.

## Skills

### `/taiwan-stock-scan`
Scan Taiwan stocks using 9-Agent joint scoring (TrendAgent, MomentumAgent, VolumeAgent, ChipAgent, VolatilityAgent, KeltnerAgent, FundamentalAgent, NewsAgent, SentimentAgent). Outputs ★★★/★★/★ rated signals with entry price, stop-loss, and analysis rationale.

### `/crypto-trend`
Multi-strategy confluence analysis for cryptocurrency pairs. 11 strategies across 4 gates. Outputs STRONG/MODERATE/WEAK signal with layered exit targets (Exit A: 40% position, Exit B: 60% position). Targets 87.5% win rate on trending setups.

### `/quant-report`
Generate structured performance reports from signal history data. Calculates win rates by star rating and agent, ranks indicator performance, and produces NotebookLM-ready analysis questions.

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
/crypto-trend          # Analyze a crypto pair
/quant-report          # Generate performance report
```

## Author

[Kuan-1113](https://github.com/Kuan-1113) — Quantitative trading systems for Taiwan equities and crypto markets.
