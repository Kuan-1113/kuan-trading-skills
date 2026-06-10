# 加密量化策略升級研究
更新：2026-06-10

---

## 一、競品怎麼做加密量化

### roman-rr：17×44×3 多維信號系統
**架構概念**：不只看技術指標，掃描六個「正交維度」（互不相關的信號源）：

| 維度 | 我們現在有? | 說明 |
|------|-----------|------|
| 1. 成交量 | ✅ OBV + 量比 | 買賣壓確認 |
| 2. 持倉（未平倉量）| ❌ | OI 變化 = 資金進出 |
| 3. 價格動態 | ✅ EMA/RSI/MACD | 趨勢動能 |
| 4. 跨資產流量 | ❌ | BTC.D、USDT.D、相關性 |
| 5. 微觀結構 | ❌ | 訂單簿深度、bid/ask 失衡 |
| 6. 選擇權衍生信號 | ❌ | Put/Call 比、IV skew |

**3 個 AI 專家共識機制**：三個不同視角分析，需要共識才出信號（降低假信號）

---

### agiprolabs：鏈上指標（crypto-native）

| 指標 | 意義 | 信號邏輯 |
|------|------|---------|
| **NVT Ratio** | 網絡價值/交易量 | NVT 高 = 估值過高；低 = 低估 |
| **MVRV Ratio** | 市值/實現市值 | MVRV > 3.5 = 歷史頂部警告 |
| **交易所流量** | 幣流入/流出交易所 | 大量流入 = 拋售壓力 |
| **資金費率** | 永續合約多空費率 | 極端正值 = 多頭過擁擠，反轉風險 |
| **聰明錢流向** | 大戶持倉變化 | 鯨魚累積 = 底部信號 |
| **長期持有者** | HODLer 供應量 | 長持增加 = 市場信心 |

---

## 二、我們現在的 /crypto-trend 分析

### 現有 4 Gate 架構
```
Gate1 趨勢：EMA9/21/55 多頭排列
Gate2 動能：RSI(40-70) + MACD 黃金交叉
Gate3 波動：Keltner Channel + Bollinger Bands 突破
Gate4 量能：量比 >1.2 + OBV 上升趨勢
```

### 優點
- 即時 Binance 數據（CCXT）
- 多策略評分（STRONG/MODERATE/WEAK）
- 有止損（ATR-based）和分層出場（Exit A 40% / Exit B 60%）

### 缺口
1. ❌ 沒有資金費率（持倉情緒最重要的指標）
2. ❌ 沒有未平倉量（OI）
3. ❌ 沒有鏈上數據（NVT/MVRV 等）
4. ❌ 沒有跨幣種相關性（BTC.D）
5. ❌ 沒有回測驗證

---

## 三、升級優先順序

### 🔴 優先級 1：加資金費率（最有價值，最容易做）
**為什麼重要**：資金費率是市場情緒最直接的反映
- 資金費率 > +0.1%（極端多頭擁擠）→ 警示信號，不追高
- 資金費率 < -0.05%（空頭擁擠）→ 反彈機會
- 可用 Binance API 免費取得

**實作方式**：
```python
# Binance Futures 資金費率
import ccxt
exchange = ccxt.binance()
funding = exchange.fetch_funding_rate('BTC/USDT:USDT')
rate = funding['fundingRate']  # 每8小時費率
annualized = rate * 3 * 365 * 100  # 年化%
```

### 🔴 優先級 2：加未平倉量（OI）
**為什麼重要**：OI 上升 + 價格上升 = 真實看漲；OI 下降 + 價格上升 = 軋空（不可持續）
- OI 突然暴增 → 大資金進場，關注
- OI 急速下降 → 去槓桿，危險

**實作方式**：
```python
# Binance OI
oi = exchange.fetch_open_interest('BTC/USDT:USDT')
oi_value = oi['openInterestAmount']
```

### 🟡 優先級 3：BTC 主導率（BTC.D）
**為什麼重要**：BTC.D 下降 = 資金流向山寨（altcoin season）；上升 = 資金回流 BTC（risk-off）
- 可透過 yfinance 抓 BTC-USD 和總市值推算
- 或用 CoinGecko API 免費取得

### 🟢 優先級 4：鏈上數據（進階）
- 需要 Glassnode/CryptoQuant API（付費）
- 短期可跳過

---

## 四、升級後的評分架構（建議）

```
Gate1 趨勢（現有）：EMA 排列          權重 25%
Gate2 動能（現有）：RSI + MACD         權重 20%
Gate3 波動（現有）：KC + BB 突破       權重 20%
Gate4 量能（現有）：量比 + OBV         權重 15%
Gate5 市場情緒（新增）：資金費率 + OI  權重 20%
```

資金費率過濾規則：
- 費率 > +0.05% → score -0.5（多頭擁擠警示）
- 費率 < -0.03% → score +0.3（空頭擁擠，反彈偏多）
- OI 同步上升 → score +0.3（確認趨勢）
- OI 下降但價格漲 → score -0.3（軋空，不可持續）

---

## 五、參考資源

- [roman-rr/trading-skills](https://github.com/roman-rr/trading-skills) — 6 維度多信號框架
- [agiprolabs/claude-trading-skills](https://github.com/agiprolabs/claude-trading-skills) — 鏈上指標整合
- [CryptoQuant 鏈上數據](https://cryptoquant.com/) — NVT/MVRV 付費 API
- [Binance Funding Rate API](https://binance-docs.github.io/apidocs/futures/en/) — 免費
- [altFINS OBV 教學](https://altfins.com/knowledge-base/obv/)
- [Top 10 Crypto Algo Strategies 2026](https://nurp.com/wisdom/top-10-strategies-to-optimize-crypto-trading/)
