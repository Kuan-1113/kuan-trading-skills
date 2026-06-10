#!/usr/bin/env python3
"""Fetch real OHLCV data and compute indicators for crypto-trend skill."""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
import json
from datetime import datetime, timezone

try:
    import ccxt
    import numpy as np
except ImportError:
    print("ERROR: Missing dependencies. Run: pip install ccxt numpy")
    sys.exit(1)

def ema(closes, period):
    result = [None] * len(closes)
    if len(closes) < period:
        return result
    k = 2 / (period + 1)
    val = sum(closes[:period]) / period
    result[period - 1] = val
    for i in range(period, len(closes)):
        val = closes[i] * k + val * (1 - k)
        result[i] = val
    return result

def rsi(closes, period=14):
    if len(closes) < period + 1:
        return None
    gains, losses = [], []
    for i in range(1, len(closes)):
        d = closes[i] - closes[i-1]
        gains.append(max(d, 0))
        losses.append(max(-d, 0))
    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period
    for i in range(period, len(gains)):
        avg_gain = (avg_gain * (period - 1) + gains[i]) / period
        avg_loss = (avg_loss * (period - 1) + losses[i]) / period
    if avg_loss == 0:
        return 100
    rs = avg_gain / avg_loss
    return round(100 - 100 / (1 + rs), 2)

def atr(highs, lows, closes, period=14):
    trs = []
    for i in range(1, len(closes)):
        tr = max(highs[i] - lows[i], abs(highs[i] - closes[i-1]), abs(lows[i] - closes[i-1]))
        trs.append(tr)
    if len(trs) < period:
        return None
    return round(sum(trs[-period:]) / period, 6)

def macd(closes):
    e12 = ema(closes, 12)
    e26 = ema(closes, 26)
    macd_line = [e12[i] - e26[i] if e12[i] and e26[i] else None for i in range(len(closes))]
    valid = [x for x in macd_line if x is not None]
    if len(valid) < 9:
        return None, None, None
    signal_vals = ema(valid, 9)
    m = macd_line[-1]
    s = signal_vals[-1]
    hist = round(m - s, 6) if m and s else None
    return round(m, 6) if m else None, round(s, 6) if s else None, hist

def keltner(highs, lows, closes, period=20, mult=2.0):
    mid = ema(closes, period)[-1]
    a = atr(highs, lows, closes, period)
    if not mid or not a:
        return None, None, None
    return round(mid - mult * a, 6), round(mid, 6), round(mid + mult * a, 6)

def bollinger(closes, period=20, mult=2.0):
    if len(closes) < period:
        return None, None, None
    window = closes[-period:]
    mid = sum(window) / period
    std = (sum((x - mid)**2 for x in window) / period) ** 0.5
    return round(mid - mult * std, 6), round(mid, 6), round(mid + mult * std, 6)

def main():
    symbol = sys.argv[1].upper() if len(sys.argv) > 1 else "BTC"
    timeframe = sys.argv[2] if len(sys.argv) > 2 else "4h"

    if "/" not in symbol:
        symbol = symbol + "/USDT"

    exchange = ccxt.binance({"enableRateLimit": True})
    futures = ccxt.binance({"options": {"defaultType": "future"}, "enableRateLimit": True})

    try:
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=100)
    except Exception as e:
        print(f"ERROR: Cannot fetch {symbol} — {e}")
        sys.exit(1)

    # Gate5: Funding Rate + Open Interest
    funding_rate = None
    oi_usd = None
    futures_symbol = symbol.replace("/USDT", "/USDT:USDT")
    try:
        fr = futures.fetch_funding_rate(futures_symbol)
        funding_rate = fr.get("fundingRate")
    except:
        pass
    try:
        oi = futures.fetch_open_interest(futures_symbol)
        oi_usd = oi.get("openInterestValue")
    except:
        pass

    if not ohlcv or len(ohlcv) < 30:
        print(f"ERROR: Not enough data for {symbol}")
        sys.exit(1)

    timestamps = [x[0] for x in ohlcv]
    opens   = [x[1] for x in ohlcv]
    highs   = [x[2] for x in ohlcv]
    lows    = [x[3] for x in ohlcv]
    closes  = [x[4] for x in ohlcv]
    volumes = [x[5] for x in ohlcv]

    price = closes[-1]
    prev  = closes[-2]
    change_pct = round((price - prev) / prev * 100, 2)

    e9  = ema(closes, 9)[-1]
    e21 = ema(closes, 21)[-1]
    e55 = ema(closes, 55)[-1]

    rsi_val = rsi(closes)
    atr_val = atr(highs, lows, closes)
    m, s, hist = macd(closes)
    kc_lower, kc_mid, kc_upper = keltner(highs, lows, closes)
    bb_lower, bb_mid, bb_upper = bollinger(closes)

    vol_now  = volumes[-1]
    vol_avg  = sum(volumes[-20:]) / 20
    vol_ratio = round(vol_now / vol_avg, 2) if vol_avg else 0

    obv = 0
    obv_list = []
    for i in range(1, len(closes)):
        obv += volumes[i] if closes[i] > closes[i-1] else (-volumes[i] if closes[i] < closes[i-1] else 0)
        obv_list.append(obv)
    obv_trend = "RISING" if len(obv_list) >= 5 and obv_list[-1] > obv_list[-5] else "FALLING"

    # Gate scoring
    gate1 = "PASS" if e9 and e21 and e55 and e9 > e21 > e55 else "FAIL"
    gate2_rsi = rsi_val and 45 <= rsi_val <= 70
    gate2_macd = hist and hist > 0
    gate2 = "PASS" if gate2_rsi and gate2_macd else ("WEAK" if gate2_rsi or gate2_macd else "FAIL")
    gate3_kc = kc_upper and price > kc_upper
    gate3_bb = bb_upper and price > bb_upper
    gate3_atr = atr_val is not None
    gate3 = "PASS" if (gate3_kc or gate3_bb) else "WEAK"
    gate4 = "PASS" if vol_ratio >= 1.5 and obv_trend == "RISING" else ("WEAK" if vol_ratio >= 1.2 else "FAIL")

    # Gate5: Market Sentiment (Funding Rate + OI)
    gate5 = "NEUTRAL"
    gate5_note = ""
    if funding_rate is not None:
        fr_pct = funding_rate * 100
        if fr_pct > 0.05:
            gate5 = "WARN"
            gate5_note = f"資金費率過高(+{fr_pct:.3f}%)，多頭擁擠，追高風險大"
        elif fr_pct < -0.03:
            gate5 = "PASS"
            gate5_note = f"資金費率為負({fr_pct:.3f}%)，空頭擁擠，反彈偏多"
        elif 0 <= fr_pct <= 0.05:
            gate5 = "PASS"
            gate5_note = f"資金費率健康({fr_pct:.3f}%)，無過熱"
        else:
            gate5 = "NEUTRAL"
            gate5_note = f"資金費率({fr_pct:.3f}%)"
    else:
        gate5_note = "無永續合約數據（現貨幣種）"

    gates = [gate1, gate2, gate3, gate4]
    pass_count = sum(1 for g in gates if g == "PASS")
    weak_count = sum(1 for g in gates if g == "WEAK")
    score = pass_count + weak_count * 0.5
    # Gate5 WARN 扣分，PASS 加分
    if gate5 == "WARN":
        score -= 0.5
    elif gate5 == "PASS" and funding_rate is not None:
        score += 0.3

    if score >= 3.5:
        strength = "STRONG"
    elif score >= 2.5:
        strength = "MODERATE"
    elif score >= 1.5:
        strength = "WEAK"
    else:
        strength = "NO SIGNAL"

    direction = "LONG" if gate1 == "PASS" and (gate2 == "PASS" or gate2 == "WEAK") else "NEUTRAL"

    ts = datetime.fromtimestamp(timestamps[-1] / 1000, tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    print(f"""
=== LIVE MARKET DATA: {symbol} ({timeframe}) ===
Time: {ts}
Price: {price}  |  Change: {change_pct}%

--- Indicators ---
EMA9:  {round(e9,4) if e9 else 'N/A'}
EMA21: {round(e21,4) if e21 else 'N/A'}
EMA55: {round(e55,4) if e55 else 'N/A'}
RSI(14): {rsi_val}
MACD Line: {m}  |  Signal: {s}  |  Histogram: {hist}
ATR(14): {atr_val}
Keltner Channel: Lower={kc_lower}  Mid={kc_mid}  Upper={kc_upper}
Bollinger Bands: Lower={bb_lower}  Mid={bb_mid}  Upper={bb_upper}
Volume Ratio (vs 20-avg): {vol_ratio}x
OBV Trend: {obv_trend}

--- Gate Scores ---
Gate 1 (Trend/EMA):        {gate1}
Gate 2 (Momentum/MACD):    {gate2}
Gate 3 (Volatility/KC):    {gate3}
Gate 4 (Volume/OBV):       {gate4}
Gate 5 (Sentiment/FR+OI):  {gate5}  {gate5_note}
Open Interest: {f"${oi_usd/1e6:.1f}M" if oi_usd else "N/A"}

--- Signal Summary ---
Signal Strength: {strength}
Direction: {direction}
Score: {round(score,2)}/4.3
=== END DATA ===
""")

if __name__ == "__main__":
    main()
