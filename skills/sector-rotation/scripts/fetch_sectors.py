#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fetch Taiwan sector ETF performance to detect rotation signals."""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from datetime import datetime, timezone, timedelta

try:
    import yfinance as yf
except ImportError:
    print("ERROR: Run: pip install yfinance")
    sys.exit(1)

# Taiwan sector ETFs & major indices
SECTORS = {
    "半導體": "00830.TW",
    "金融": "0055.TW",
    "電子": "0053.TW",
    "傳產/工業": "0054.TW",
    "科技(QQQ台版)": "00662.TW",
    "高股息": "0056.TW",
    "台灣50": "0050.TW",
}

CRYPTO_PROXY = {
    "BTC": "BTC-USD",
    "ETH": "ETH-USD",
}

def get_change(ticker, days=1):
    try:
        t = yf.Ticker(ticker)
        hist = t.history(period="5d")
        if len(hist) < 2:
            return None, None
        close = hist["Close"].iloc[-1]
        prev = hist["Close"].iloc[-2]
        change = (close - prev) / prev * 100
        return round(close, 2), round(change, 2)
    except:
        return None, None

def bar(change, width=10):
    if change is None:
        return "N/A"
    filled = min(int(abs(change) / 0.5), width)
    if change >= 0:
        return "+" + "█" * filled + f" +{change:.2f}%"
    else:
        return "-" + "█" * filled + f" {change:.2f}%"

def main():
    ts = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print(f"\n=== 台股板塊輪動分析 ({ts}) ===\n")

    results = []
    for name, ticker in SECTORS.items():
        price, chg = get_change(ticker)
        results.append((name, ticker, price, chg))

    # Sort by change descending
    results.sort(key=lambda x: x[3] if x[3] is not None else -999, reverse=True)

    print("【今日板塊強弱排行】")
    for i, (name, ticker, price, chg) in enumerate(results):
        rank = ["🥇","🥈","🥉","4️⃣","5️⃣","6️⃣","7️⃣"][i] if i < 7 else f"{i+1}."
        if price and chg is not None:
            print(f"{rank} {name:<12} {price:>8.2f}  {bar(chg)}")
        else:
            print(f"{rank} {name:<12} 數據無法取得")

    # Top and bottom
    valid = [(n, c) for n, _, _, c in results if c is not None]
    if valid:
        top = valid[0]
        bot = valid[-1]
        print(f"\n💪 最強板塊：{top[0]} ({top[1]:+.2f}%)")
        print(f"📉 最弱板塊：{bot[0]} ({bot[1]:+.2f}%)")

    print("\n【加密市場參考】")
    for name, ticker in CRYPTO_PROXY.items():
        price, chg = get_change(ticker)
        if price and chg is not None:
            print(f"  {name}: ${price:,.0f}  {bar(chg)}")

    print("\n=== END SECTOR DATA ===\n")

if __name__ == "__main__":
    main()
