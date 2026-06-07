#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fetch real-time market sentiment data: CNN Fear & Greed + Crypto Fear & Greed."""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
import urllib.request
import json
from datetime import datetime, timezone

def fetch_crypto_fg():
    try:
        url = "https://api.alternative.me/fng/?limit=2&format=json"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=8) as r:
            data = json.loads(r.read())["data"]
        now = data[0]
        prev = data[1] if len(data) > 1 else None
        return {
            "value": int(now["value"]),
            "label": now["value_classification"],
            "prev_value": int(prev["value"]) if prev else None,
            "prev_label": prev["value_classification"] if prev else None
        }
    except Exception as e:
        return {"error": str(e)}

def fetch_cnn_fg():
    # Try multiple endpoints
    endpoints = [
        "https://production.dataviz.cnn.io/index/fearandgreed/graphdata",
        "https://fear-and-greed-index.p.rapidapi.com/v1/fgi",
    ]
    headers_list = [
        {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36", "Accept": "application/json", "Referer": "https://edition.cnn.com/markets/fear-and-greed"},
    ]
    for url in endpoints[:1]:
        for headers in headers_list:
            try:
                req = urllib.request.Request(url, headers=headers)
                with urllib.request.urlopen(req, timeout=10) as r:
                    data = json.loads(r.read())
                score = data["fear_and_greed"]["score"]
                rating = data["fear_and_greed"]["rating"]
                prev = data["fear_and_greed"].get("previous_close", None)
                return {
                    "value": round(score, 1),
                    "label": rating,
                    "prev_value": round(prev, 1) if prev else None,
                }
            except Exception:
                continue
    return {"error": "CNN Fear & Greed API unavailable (geo-blocked). Use crypto index as reference."}

def sentiment_bar(value):
    filled = int(value / 5)
    bar = "█" * filled + "░" * (20 - filled)
    return f"[{bar}] {value}/100"

def zone_label(value):
    if value <= 25:   return "極度恐慌 😱"
    elif value <= 45: return "恐慌 😰"
    elif value <= 55: return "中性 😐"
    elif value <= 75: return "貪婪 😏"
    else:             return "極度貪婪 🤑"

def main():
    ts = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    crypto = fetch_crypto_fg()
    cnn = fetch_cnn_fg()

    print(f"\n=== 市場情緒指標 ({ts}) ===\n")

    print("【加密貨幣 Fear & Greed Index】")
    if "error" not in crypto:
        v = crypto["value"]
        print(f"當前：{v} — {zone_label(v)}")
        print(f"進度：{sentiment_bar(v)}")
        if crypto.get("prev_value"):
            diff = v - crypto["prev_value"]
            arrow = "↑" if diff > 0 else "↓" if diff < 0 else "→"
            print(f"昨日：{crypto['prev_value']} ({arrow}{abs(diff):+d})")
    else:
        print(f"無法取得數據：{crypto['error']}")

    print("\n【美股 CNN Fear & Greed Index】")
    if "error" not in cnn:
        v = cnn["value"]
        print(f"當前：{v} — {zone_label(v)}")
        print(f"進度：{sentiment_bar(v)}")
        if cnn.get("prev_value"):
            diff = v - cnn["prev_value"]
            arrow = "↑" if diff > 0 else "↓" if diff < 0 else "→"
            print(f"前日：{cnn['prev_value']} ({arrow}{abs(diff):.1f})")
    else:
        print(f"無法取得數據：{cnn['error']}")

    print("\n=== END SENTIMENT DATA ===\n")

if __name__ == "__main__":
    main()
