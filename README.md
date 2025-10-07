# 📊 Solana Radar - Daily Reports

**Last Updated**: 2025-10-07 21:34 UTC

Automated daily analysis of Solana tokens with whale tracking and momentum indicators.

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 35
**Combined 24h Volume**: $408.89M
**Combined Liquidity**: $59.31M

**Concentration Risk Distribution**:
- 🟢 Low: 17 tokens
- 🔴 Extreme: 7 tokens
- 🟡 High: 6 tokens
- 🟢 Medium: 4 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $407.85M | $57.70M | 🟢 unknown |
| 2 | XBT | XBT | $566.74K | $433.41K | 🟢 low |
| 3 | early | not wrong just early | $121.95K | $34.00K | 🟢 low |
| 4 | USDUT | unstable tether | $59.11K | $115.19K | 🟢 low |
| 5 | CHARLIE | RIP CHARLIE KIRK | $45.84K | $99.80K | 🟢 low |
| 6 | 1nu | 1nu | $38.82K | $35.88K | 🟢 low |
| 7 | gib | gib | $31.25K | $160.04K | 🟢 low |
| 8 | Useless | Useless Coin | $27.25K | $57.44K | 🟢 low |
| 9 | 67 | 67coin | $27.24K | $55.17K | 🟢 low |
| 10 | SOL | Solana | $26.54K | $11.19K | 🔴 extreme |

📄 [Full data: daily_top50.csv](data/daily_top50.csv)

---

## 🌱 New Viable Tokens (7-14 Days Old)

New tokens showing potential with healthy metrics and lower concentration risk.

*No viable new tokens found with current criteria*

---

## 🎯 Trading Signals (Whale Filtered)

Signals filtered to exclude tokens with extreme concentration risk.

**Signal Distribution**:
- 👀 **Watch**: 3 tokens
- 🚀 **Breakout**: 2 tokens

### 🚀 Breakout Signals

| Symbol | Score | Vol 3v1 | Z-Score Vol | Liq 3d | Streak |
|--------|-------|---------|-------------|--------|--------|
| wSOL | 57909.60 | 2.52x | 1.68 | $57.90M | 7d |
| XBT | 427.19 | 2.14x | 1.68 | $417.40K | 7d |

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
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 35 |
| [new_viable.csv](data/new_viable.csv) | New tokens with potential | 0 |
| [signals_filtered.csv](data/signals_filtered.csv) | Whale-filtered trading signals | 5 |

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
