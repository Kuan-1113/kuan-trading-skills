---
description: Detect Taiwan stock market sector rotation using real ETF data. Use when the user asks which sector is strong today, 板塊輪動, 資金流向, 哪個族群在漲, sector analysis, or market breadth. Fetches live Taiwan sector ETF data and ranks performance.
---

# Taiwan Sector Rotation Detector

Real-time Taiwan sector performance data fetched below. Identify where money is flowing today.

## Live Sector Data

!`python skills/sector-rotation/scripts/fetch_sectors.py`

## Rotation Signal Framework

**強勢信號（買進/加碼）**
- 板塊漲幅 > +1.5% 且成交量放大
- 連續2天領漲同一板塊 → 趨勢性輪動
- 防禦板塊（金融/高股息）強 → 市場轉保守

**弱勢信號（減碼/觀望）**
- 板塊跌幅 > -1.5%
- 昨日強勢板塊今日轉弱 → 短線獲利了結
- 半導體弱但其他板塊強 → 資金撤出科技

**輪動解讀**
- 半導體領漲 → AI/科技行情，關注台積電族群
- 金融領漲 → 升息預期或金融股除息行情
- 傳產領漲 → 景氣復甦訊號，關注原物料
- 高股息領漲 → 防禦性布局，市場偏保守

## Output Format

Using the live data above, generate this report in Traditional Chinese:

```
🔄 台股板塊輪動報告 [DATE]
━━━━━━━━━━━━━━━━━━━
📊 今日強弱排行
🥇 [最強板塊] +X.XX% ← 資金流入
🥈 [第二] +X.XX%
🥉 [第三] +X.XX%
...
📉 [最弱板塊] -X.XX% ← 資金流出

🎯 輪動解讀
主流資金：流向[板塊]（[原因分析]）
迴避板塊：[板塊]（[原因]）

💡 操作建議
• 今日重點族群：[具體建議]
• 搭配信號：[與 /taiwan-stock-scan 的連動建議]
• 風險提示：[注意事項]

📈 加密市場同步
BTC：$XX,XXX（±X.XX%）
ETH：$X,XXX（±X.XX%）
━━━━━━━━━━━━━━━━━━━
```

## Instructions

1. Parse the live sector data from the script output
2. Identify the top 2 and bottom 2 sectors
3. Explain the rotation logic in plain Chinese (why money moves)
4. Connect to actionable advice — which stocks/ETFs to watch
5. If crypto is also down significantly, note risk-off environment
6. Suggest combining with `/taiwan-stock-scan` to find specific stocks in the strong sector
