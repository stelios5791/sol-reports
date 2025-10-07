# 🌊 Solana Radar - Daily Analysis Dashboard

> **Live tracking of top Solana tokens with whale concentration analysis**

📅 **Latest Data**: 2025-10-07  
🔄 **Last Updated**: 2025-10-07 17:17 UTC  
📊 **Data Source**: [Private Radar System](https://github.com/stelios5791) → DexScreener + Helius RPC

---

## 📈 Daily Overview

| Metric | Value |
|--------|-------|
| 🪙 **Tokens Tracked** | 72 |
| 📊 **Avg Concentration** | 73.88% (top 10 holders) |
| 📉 **Median Concentration** | 89.18% |
| 💰 **Total 24h Volume** | $420.61M |
| 💧 **Avg Liquidity** | $868.72K |

---

## ⚠️ Risk Distribution

**Holder Concentration Breakdown:**

| Risk Level | Count | Percentage | Description |
|------------|-------|------------|-------------|
| 🔴 **Critical** | 25 | 34.7% | Top 10 hold >90% |
| 🟠 **High** | 15 | 20.8% | Top 10 hold 70-90% |
| 🟡 **Medium** | 9 | 12.5% | Top 10 hold 50-70% |
| 🟢 **Low** | 22 | 30.6% | Top 10 hold <50% |

**Distribution Chart:**
```
Critical: █████████████████ 25
High:     ██████████ 15
Medium:   ██████ 9
Low:      ███████████████ 22
```

---

## 🏆 Safety Leaderboard (Lowest Concentration)

**Safest tokens based on holder distribution:**

| Rank | Symbol | Name | Top 10% | Top 5% | Risk | Liquidity |
|------|--------|------|---------|--------|------|-----------|
| 1 | **XBT** | XBT | 21.71% | 15.95% | 🟢 low | $480.13K |
| 2 | **RAGEGUY** | Rage Guy | 25.71% | 18.13% | 🟢 low | $158.16K |
| 3 | **ELIZABETH** | Just Elizabeth Cat | 26.90% | 18.33% | 🟢 low | $58.84 |
| 4 | **CRND** | Crundle | 30.08% | 24.95% | 🟢 low | $59.13K |
| 5 | **DREAM** | Dreamsync | 31.92% | 17.76% | 🟢 low | $190.28K |
| 6 | **FARTLESS** | FARTLESS COIN | 32.59% | 27.36% | 🟢 low | $4.25K |
| 7 | **FLY** | Nexa | 34.30% | 32.54% | 🟢 low | $9.01K |
| 8 | **USDUT** | unstable tether | 38.13% | 29.87% | 🟢 low | $111.36K |
| 9 | **1nu** | 1nu | 40.10% | 32.29% | 🟢 low | $35.08K |
| 10 | **USEFUL** | USEFUL COIN | 40.52% | 33.76% | 🟢 low | $103.17K |

---

## 🚨 High Risk Alert (Highest Concentration)

**Tokens with extreme holder concentration - HIGH RUG RISK:**

| Rank | Symbol | Name | Top 10% | Top 5% | Risk |
|------|--------|------|---------|--------|------|
| 1 | **VAN** | Man with a Van | 100.00% | 99.96% | 🔴 extreme |
| 2 | **YOU** | YOU can change your  | 99.99% | 99.93% | 🔴 extreme |
| 3 | **Hamu** | Hamu | 99.88% | 99.76% | 🔴 extreme |
| 4 | **2** | TWO IS BETTER THAN O | 99.84% | 99.66% | 🔴 extreme |
| 5 | **AMG** | ASCII MEME GENERATOR | 99.82% | 99.54% | 🔴 extreme |
| 6 | **1cat** | 1 cat can change you | 99.72% | 99.24% | 🔴 extreme |
| 7 | **BITX** | Mega Bitminer X | 99.71% | 0.00% | ⚪ unknown |
| 8 | **1SOL** | 1 SOL and a dream | 99.68% | 99.48% | 🔴 extreme |
| 9 | **MMGA** | MAKE MEMES GREAT AGA | 99.24% | 98.73% | 🔴 extreme |
| 10 | **ORE** | Ore Labs | 99.17% | 0.00% | ⚪ unknown |

---

## 🚀 Top Gainers (24h)

| Symbol | Name | Price Change | Volume Change | Current Price |
|--------|------|--------------|---------------|---------------|
| 📈 **XBT** | XBT | +49.59% | +12.3% | $0.002356 |
| 📈 **AUSBAGWORK** | AUSSIE BAG WORKERS | +15.94% | +103.2% | $0.000020 |
| 📈 **USEFUL** | USEFUL COIN | +9.68% | -1.5% | $0.000207 |
| 📈 **Useless** | Useless Coin | +7.91% | -1.5% | $0.000149 |
| 📈 **RAGEGUY** | Rage Guy | +7.84% | +36.4% | $0.000964 |

---

## 📉 Top Losers (24h)

| Symbol | Name | Price Change | Volume Change | Current Price |
|--------|------|--------------|---------------|---------------|
| 💥 **early** | not wrong just early | -66.17% | +389.8% | $0.000069 |
| 💥 **SOL** | Solana | -64.78% | +9905.4% | $387.470000 |
| 📉 **RUECAT** | Rue Cat | -47.32% | -52.3% | $0.000246 |
| 📉 **1nu** | 1nu | -37.62% | +6.1% | $0.000076 |
| 📉 **T-2049** | Token 2049 | -34.08% | +77.0% | $0.000047 |

---

## 📊 Data Files

All historical data is available in the `/data` directory:

- **`history.csv`** - Complete daily snapshots (19 columns)
- **`master.csv`** - Aggregated per-token metrics
- **`performance.csv`** - Rolling performance indicators
- **`signals.csv`** - Trading signals (Breakout/Watch/Cooling)
- **`token_cache.csv`** - Token metadata cache

### Schema: history.csv (19 columns)

```
date, symbol, name, address,
price_usd, volume_24h_usd, liquidity_usd, fdv_usd,
source, data_status, missing_streak,
top_10_holders_pct, top_5_holders_pct, holder_concentration, concentration_risk
```

---

## 🔍 Methodology

### Whale Tracking Approach (v3.0)

**What we track:**
- ✅ **Holder Concentration** - % held by top 5 and top 10 wallets
- ✅ **Risk Classification** - Automatic risk level assignment
- ✅ **Distribution Analysis** - Real ownership structure

**Why holder concentration?**
- Shows true distribution of power
- Can't be faked with wash trading
- Predictive of rug risk
- Works for all token types

**Risk Levels:**
- 🔴 **Critical/Extreme**: >90% held by top 10 → Very high rug risk
- 🟠 **High**: 70-90% held by top 10 → Elevated risk
- 🟡 **Medium**: 50-70% held by top 10 → Moderate risk
- 🟢 **Low**: <50% held by top 10 → Lower risk, better distribution

---

## 🤖 Automation

**Daily Updates:**
- Runs at **08:05 UTC** via GitHub Actions
- Discovers top 50 Solana tokens (DexScreener)
- Enriches with whale metrics (Helius RPC)
- Generates CSVs and updates this dashboard
- ~70 second runtime, 100% success rate

**Technology Stack:**
- Python 3.x (pandas, requests)
- DexScreener API (market data)
- Helius RPC (holder analysis)
- GitHub Actions (automation)

---

## ⚠️ Disclaimer

This dashboard is for **informational purposes only**. 

- High concentration ≠ guaranteed rug (but increases risk)
- Low concentration ≠ guaranteed safety (other factors matter)
- Always DYOR (Do Your Own Research)
- Never invest more than you can afford to lose
- Crypto is highly volatile and risky

---

## 📞 Links

- **Private Radar System**: [GitHub](https://github.com/stelios5791) (code repo)
- **Public Data Repo**: [sol-reports](https://github.com/stelios5791/sol-reports)
- **Documentation**: See [Project Gist](https://gist.github.com/stelios5791/bced5fa175b3f3934801c4428b5fb0cd)

---

**Generated by Solana Radar v4.0** | Last update: {update_time}
