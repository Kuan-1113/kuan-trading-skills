# Kuan Trading Skills

The most comprehensive quantitative trading plugin for Claude Code — 9 skills covering Taiwan stocks, crypto, futures, options, and risk management.

## Skills

### `/taiwan-stock-scan`
Taiwan equity signal scanner using 9-Agent joint scoring. Outputs ★★★/★★/★ rated signals with entry, stop-loss, and rationale. Targets 70–75% win rate.

### `/crypto-trend`
Live crypto analysis via **Binance CCXT** — 11 strategies across 4 gates. Layered exit system (Exit A 40% / Exit B 60%). Targets 87.5% win rate.

### `/quant-report`
Structured performance reports from signal history. Win rate by star rating, agent ranking, and NotebookLM-ready analysis questions.

### `/futures-query`
Taiwan futures reference — 台指期, 小台, 電子期, 金融期, US index futures. Margin calculator, P&L simulation, liquidation warning.

### `/position-size`
Optimal position sizing — Kelly Criterion, risk-based, fixed fractional. Supports stocks (張) and futures (口). Full risk breakdown.

### `/fear-greed`
Live **Crypto Fear & Greed** (alternative.me) + **CNN Fear & Greed** index. Score, trend, and trading implications.

### `/options-calc`
Taiwan index options Greeks calculator (Black-Scholes). Delta, Gamma, Theta, Vega, Rho — plus theoretical price vs market price comparison and breakeven analysis.

### `/sector-rotation`
Live Taiwan sector ETF performance ranking via **yfinance**. Detects where money is flowing today — semiconductor, financials, electronics, high-dividend, and more.

### `/trading-journal`
Trading psychology analyzer. Paste your trade records — get bias diagnosis (loss aversion, revenge trading, anchoring), best/worst patterns, and concrete weekly improvement actions.

## Installation

```bash
claude plugins install Kuan-1113/kuan-trading-skills
```

## Usage

```
/taiwan-stock-scan    # Taiwan stock signals (9-Agent)
/crypto-trend         # Live crypto analysis (Binance)
/quant-report         # Performance report
/futures-query        # Futures margin & P&L
/position-size        # Kelly / risk-based sizing
/fear-greed           # Live sentiment index
/options-calc         # Options Greeks (Black-Scholes)
/sector-rotation      # Taiwan sector rotation (live)
/trading-journal      # Trade psychology analysis
```

## Author

[Kuan-1113](https://github.com/Kuan-1113) — Quantitative trading systems for Taiwan equities and crypto markets.
