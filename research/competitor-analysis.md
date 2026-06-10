# 量化交易 Claude Plugin 競品研究
更新：2026-06-10

---

## 一、市集競品（claudemarketplaces.com）

### 1. wshobson/agents — `quantitative-trading`
- **連結**：https://claudemarketplaces.com/plugins/wshobson-agents/quantitative-trading
- **功能**：量化分析、演算法交易策略、財務建模、投資組合風險管理、回測
- **特色**：通用型，無特定市場

### 2. omer-metin/skills — `quantitative-research`
- **連結**：https://claudemarketplaces.com/skills/omer-metin/skills-for-antigravity/quantitative-research
- **功能**：系統化交易策略回測、Alpha 生成、因子模型、統計套利
- **對象**：量化研究員、策略開發者

### 3. quant-sentiment-ai/claude-equity-research
- **連結**：https://claudemarketplaces.com/plugins/quant-sentiment-ai-claude-equity-research
- **GitHub**：https://github.com/quant-sentiment-ai/claude-equity-research
- **功能**：機構級股票研究、買賣建議、基本面分析、技術指標、風險評估
- **定位**：教育用途，非財務建議

### 4. Anthropic 官方 — `comps-analysis`
- **連結**：https://claudemarketplaces.com/skills/anthropics/financial-services/comps-analysis
- **功能**：公司比較分析（金融服務官方 skill）

---

## 二、GitHub 熱門競品

### 1. agiprolabs/claude-trading-skills ⭐⭐⭐（最強競品）
- **GitHub**：https://github.com/agiprolabs/claude-trading-skills
- **規模**：**62 個 skills**，覆蓋交易、DeFi、量化金融
- **相容性**：Claude Code、Cursor、Codex、Gemini CLI、30+ 工具
- **技術細節**：
  - Backtrader 回測引擎（逐 bar 執行）
  - Birdeye API（Solana 代幣數據）
  - CoinGecko API（13,000+ 代幣）
  - Pandas-TA（130+ 技術指標）
  - 鏈上指標：NVT、交易所流量、資金費率、聰明錢流向
  - 倉位管理：固定比例、波動率調整、Kelly、流動性限制
  - 稅務合規：Koinly、IRS 8949 格式
- **定位**：Crypto/DeFi 優先，可擴展至全量化金融
- **我們的差異**：他們沒有台股專項，我們的台股 9-Agent 是獨特優勢

### 2. roman-rr/trading-skills ⭐⭐（技術含量高）
- **GitHub**：https://github.com/roman-rr/trading-skills
- **架構**：17 觸發器 × 44 演算法 × 3 AI 專家
- **信號邏輯**：
  - 掃描 50+ 永續合約市場
  - 六個維度：成交量、持倉、價格動態、跨資產流量、微觀結構、選擇權信號
  - 3 個 AI 專家獨立分析，需達成共識才發信號
- **每個信號包含**：進場、止損、止盈、槓桿、倉位大小、推導鏈
- **API 工具**：register / get_signals / get_signal / get_signal_history / get_stats
- **授權**：Beta 免費，商業使用需付費
- **我們的差異**：他們純加密，我們有台股；他們需要 API 金鑰，我們直接用

### 3. tradermonty/claude-trading-skills ⭐（股票投資導向）
- **GitHub**：https://github.com/tradermonty/claude-trading-skills
- **文檔**：https://tradermonty.github.io/claude-trading-skills/en/
- **功能**：市場分析、技術圖表、經濟日曆、篩選器、策略開發
- **定位**：長期投資 + ETF + 股息股為核心，波段交易為衛星策略
- **對象**：時間有限的個人投資者

### 4. JoelLewis/finance_skills ⭐（最全面金融）
- **GitHub**：https://github.com/JoelLewis/finance_skills
- **規模**：**81 個 skills，7 個域插件**
- **覆蓋**：投資管理、法規合規、顧問流程、交易、運營
- **定位**：機構金融服務

### 5. CPZ-Lab/cpzai-plugin ⭐（系統化交易）
- **GitHub**：https://github.com/CPZ-Lab/cpzai-plugin
- **規模**：9 skills、5 命令、18 MCP 工具
- **功能**：建構量化策略、回測、即時風險監控、自然語言下單
- **特色**：系統化交易專家模式

### 6. staskh/trading_skills（選擇權）
- **GitHub**：https://github.com/staskh/trading_skills
- **功能**：Claude 驅動的選擇權交易顧問系統

### 7. joinQuantish/skills（預測市場）
- **GitHub**：https://github.com/joinQuantish/skills
- **功能**：預測市場交易（Polymarket 等）

---

## 三、競品分析摘要

| 競品 | 台股 | 加密 | 選擇權 | 回測 | 倉位管理 | 特色 |
|------|------|------|--------|------|---------|------|
| **我們（Kuan）** | ✅ 9-Agent | ✅ 4-Gate | ✅ BS | ❌ | ✅ Kelly | 台股專項、即時數據 |
| agiprolabs | ❌ | ✅ 62個skill | ❌ | ✅ | ✅ | 最大規模、DeFi |
| roman-rr | ❌ | ✅ 50+市場 | ✅ | ❌ | ✅ | 多維信號、AI共識 |
| tradermonty | ❌ | ❌ | ❌ | ❌ | ❌ | 個人投資者 |
| JoelLewis | ❌ | ❌ | ❌ | ✅ | ✅ | 機構金融 |
| CPZ-Lab | ❌ | ✅ | ❌ | ✅ | ✅ | 系統化+MCP |

---

## 四、我們的差異化優勢

1. **台股唯一**：沒有任何競品專注台灣股市，9-Agent 掃描是獨特定位
2. **中文介面**：所有輸出繁體中文，台灣用戶無障礙
3. **即時數據**：`/crypto-trend`（Binance CCXT）、`/sector-rotation`（yfinance）直接拉數據
4. **一站式**：台股 + 加密 + 期貨 + 選擇權 + 倉位 + 板塊 + 日誌，不用裝多個 plugin

---

## 五、可借鑑的改進方向

- [ ] 加入回測功能（agiprolabs 有 Backtrader 整合）
- [ ] 加入更多鏈上指標（NVT、交易所流量）
- [ ] 考慮 MCP 工具整合（CPZ-Lab 模式）
- [ ] 選擇權倉位管理更完整（staskh 模式）
- [ ] 加入 Pandas-TA 整合（130+ 指標）

---

## 六、參考連結

- [claudemarketplaces.com](https://claudemarketplaces.com)
- [agiprolabs/claude-trading-skills](https://github.com/agiprolabs/claude-trading-skills)
- [roman-rr/trading-skills](https://github.com/roman-rr/trading-skills)
- [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills)
- [JoelLewis/finance_skills](https://github.com/JoelLewis/finance_skills)
- [CPZ-Lab/cpzai-plugin](https://github.com/CPZ-Lab/cpzai-plugin)
- [Snyk Top 8 Claude Finance Skills](https://snyk.io/articles/top-claude-skills-finance-quantitative-developers/)
