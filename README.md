# 📊 Solana Radar - Daily Reports

**Last Updated**: 2025-10-07 21:56 UTC

Automated daily analysis of Solana tokens with whale tracking and momentum indicators.

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 50
**Combined 24h Volume**: $408.30M
**Combined Liquidity**: $60.92M

**Concentration Risk Distribution**:
- 🔴 Extreme: 21 tokens
- 🟢 Low: 13 tokens
- 🟡 High: 9 tokens
- 🟢 Medium: 6 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $407.80M | $57.40M | 🟢 unknown |
| 2 | AI4 | AI⁴ | $180.94K | $94.59K | 🟢 low |
| 3 | DREAM | Dreamsync | $111.29K | $176.39K | 🟢 low |
| 4 | RAGEGUY | Rage Guy | $73.77K | $157.61K | 🟢 low |
| 5 | 1nu | 1nu | $38.77K | $36.41K | 🟢 low |
| 6 | LION | Loaded Lions | $27.17K | $2.08M | 🟢 low |
| 7 | SOL | Solana | $26.54K | $11.19K | 🔴 extreme |
| 8 | RUECAT | Rue Cat | $11.99K | $62.94K | 🟢 low |
| 9 | HAROLD | Harold | $10.61K | $572.07K | 🟢 medium |
| 10 | SHITTER | SHITTERCOIN | $4.50K | $22.21K | 🟢 medium |

📄 [Full data: daily_top50.csv](data/daily_top50.csv)

---

## 🌱 New Viable Tokens (7-14 Days Old)

New tokens showing potential with healthy metrics and lower concentration risk.

*No viable new tokens found with current criteria*

---

## 📈 Top Movers (24h Change)

Tokens with significant price or volume changes in the last 24 hours.

*No significant movers in the last 24 hours*

---

## 🎯 Trading Signals (Whale Filtered)

Signals filtered to exclude tokens with extreme concentration risk.

**Signal Distribution**:
- 👀 **Watch**: 3 tokens
- 🚀 **Breakout**: 1 tokens

### 🚀 Breakout Signals

| Symbol | Score | Vol 3v1 | Z-Score Vol | Liq 3d | Streak |
|--------|-------|---------|-------------|--------|--------|
| wSOL | 57810.08 | 2.52x | 1.68 | $57.80M | 7d |

### 👀 Watch List

*3 tokens showing elevated activity*

📄 [Full data: signals_filtered.csv](data/signals_filtered.csv)

---

## 📈 Historical Data

**Total Historical Records**: 474
**Unique Tokens Tracked**: 101
**Date Range**: 2025-10-01 to 2025-10-07

**Master Aggregations**: 101 tokens
**Performance Metrics**: 474 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 474 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 101 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 474 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 50 |
| [new_viable.csv](data/new_viable.csv) | New tokens with potential | 0 |
| [signals_filtered.csv](data/signals_filtered.csv) | Whale-filtered trading signals | 4 |

---

## 📋 Data Schema

### Key Columns

**Market Data**:
- `price_usd`: Current token price
- `volume_24h_usd`: 24-hour trading volume
- `liquidity_usd`: Total liquidity
- `fdv_usd`: Fully diluted valuation

**Whale Metrics (Holder Concentration)**:
- `top_10_holders_pct`: % held by top 10 wallets
- `top_5_holders_pct`: % held by top 5 wallets
- `holder_concentration`: Rating (critical/high/medium/low)
- `concentration_risk`: Risk level (extreme/high/medium/low)

**Performance Indicators**:
- `vol_mom_3v1`: 3-day vs 1-day volume momentum
- `zscore_vol_10d`: 10-day volume z-score
- `presence_7d`/`presence_30d`: Days seen in period
- `current_streak_days`: Consecutive days with data

---

## 🔗 Links

- **Data Repository**: [stelios5791/sol-reports](https://github.com/stelios5791/sol-reports)
- **Analysis Pipeline**: Private repository (automated daily)

---

*Generated automatically by Solana Radar pipeline*
