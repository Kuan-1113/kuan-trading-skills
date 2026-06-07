---
description: Show real-time market sentiment using Fear & Greed Index for both crypto and US stocks. Use when the user asks about market sentiment, fear and greed, 市場情緒, 恐慌指數, 貪婪指數, 現在市場氣氛, or whether it's a good time to enter. Fetches live data from alternative.me and CNN.
---

# Market Fear & Greed Analyzer

Real-time market sentiment data fetched below. Use it to assess current market psychology and provide trading context.

## Live Sentiment Data

!`python skills/fear-greed/scripts/fetch_sentiment.py`

## Interpretation Guide

| 分數 | 情緒 | 交易含義 |
|---|---|---|
| 0–25 | 極度恐慌 😱 | 逢低買入機會（市場超賣） |
| 26–45 | 恐慌 😰 | 謹慎，可開始佈局 |
| 46–55 | 中性 😐 | 等待方向確認 |
| 56–75 | 貪婪 😏 | 注意風險，降低倉位 |
| 76–100 | 極度貪婪 🤑 | 高度警戒，考慮減倉 |

**Warren Buffett 原則**：「別人恐慌時貪婪，別人貪婪時恐慌」

## Output Format

Based on the live data above, generate this report in Traditional Chinese:

```
📊 市場情緒報告 [DATE]
━━━━━━━━━━━━━━━━━━━
🔐 加密貨幣情緒
指數：XX/100 — [情緒標籤]
[進度條]
昨日：XX（變化：±X）
解讀：[1句解讀]

📈 美股情緒（CNN）
指數：XX/100 — [情緒標籤]
[進度條]
前日：XX（變化：±X）
解讀：[1句解讀]

🎯 綜合建議
[根據兩個指數的綜合建議，2-3句]

💡 今日操作提示
• 加密：[具體建議]
• 台股/美股：[具體建議]
• 風險提示：[注意事項]
━━━━━━━━━━━━━━━━━━━
⚠️ 情緒指標為輔助參考，需結合技術分析
```

## Instructions

1. Parse the live sentiment data from the script output above
2. If script returned an error for either index, note it and use only available data
3. Cross-reference both indices — if both extreme fear → stronger buy signal
4. If user asks about a specific coin or stock, combine sentiment with `/crypto-trend` or `/taiwan-stock-scan`
5. Always remind that sentiment is a contrarian indicator, not a timing tool

**Pro tip for users**: Combine with `/crypto-trend` for full signal — sentiment sets the backdrop, technicals set the entry.
