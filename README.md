# 📊 Solana Radar - Daily Reports

**Last Updated**: 2025-10-07 23:06 UTC

Automated daily analysis of Solana tokens with whale tracking and momentum indicators.

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 50
**Combined 24h Volume**: $407.82M
**Combined Liquidity**: $61.01M

**Concentration Risk Distribution**:
- 🔴 Extreme: 20 tokens
- 🟢 Low: 13 tokens
- 🟡 High: 10 tokens
- 🟢 Medium: 6 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $407.32M | $57.51M | 🟢 unknown |
| 2 | AI4 | AI⁴ | $179.87K | $94.43K | 🟢 low |
| 3 | DREAM | Dreamsync | $111.27K | $176.39K | 🟢 low |
| 4 | RAGEGUY | Rage Guy | $76.00K | $152.97K | 🟢 low |
| 5 | 1nu | 1nu | $39.55K | $35.12K | 🟢 low |
| 6 | LION | Loaded Lions | $26.54K | $2.06M | 🟢 low |
| 7 | SOL | Solana | $26.54K | $11.19K | 🔴 extreme |
| 8 | RUECAT | Rue Cat | $12.02K | $62.54K | 🟢 low |
| 9 | HAROLD | Harold | $10.54K | $572.07K | 🟢 medium |
| 10 | SHITTER | SHITTERCOIN | $4.40K | $22.19K | 🟢 medium |

📄 [Full data: daily_top50.csv](data/daily_top50.csv)

---

## 🌱 New Viable Tokens (7-14 Days Old)

New tokens showing potential with healthy metrics and lower concentration risk.

*No viable new tokens found with current criteria*

---

## 📈 Top Movers (24h Change)

Tokens with significant price or volume changes in the last 24 hours.

**Total Movers**: 25
- 🚀 **Gainers** (>+20%): 1
- 📉 **Losers** (<-20%): 11
- 📊 **Volume Spikes** (>+100%): 16

### 🚀 Top Gainers

| # | Symbol | Name | Change 24h | Current Price | Volume Change | Risk |
|---|--------|------|------------|---------------|---------------|------|
| 9 | XBT | XBT | +25.84% | $0.00 | -100.0% | 🟢 |

### 📉 Biggest Losers

| # | Symbol | Name | Change 24h | Current Price | Volume Change | Risk |
|---|--------|------|------------|---------------|---------------|------|
| 1 | early | not wrong just early | -70.64% | $0.00 | +376.0% | 🟢 |
| 2 | SOL | Solana | -63.56% | $400.92 | +10185.4% | 🔴 |
| 3 | RUECAT | Rue Cat | -47.94% | $0.00 | -53.1% | 🟢 |
| 4 | 1nu | 1nu | -37.50% | $0.00 | -5.4% | 🟢 |
| 5 | T-2049 | Token 2049 | -31.57% | $0.00 | +7.4% | 🟢 |
| 6 | 1Bull | One bull run to change yo | -30.41% | $0.00 | -34.7% | 🟢 |
| 7 | APOLLO | Apollo AI | -29.85% | $0.00 | -22.8% | 🟢 |
| 8 | FARTLESS | FARTLESS COIN | -29.08% | $0.00 | +24.2% | 🟢 |
| 10 | CHARLIE | RIP CHARLIE KIRK | -20.72% | $0.00 | +22.5% | 🟢 |
| 11 | walkusa | WALKING ACROSS AMERICA | -20.47% | $0.00 | +384.9% | 🟢 |

📄 [Full data: top_movers.csv](data/top_movers.csv)

---

## 🎯 Trading Signals (Whale Filtered)

Signals filtered to exclude tokens with extreme concentration risk.

**Signal Distribution**:
- 👀 **Watch**: 3 tokens
- 🚀 **Breakout**: 1 tokens

### 🚀 Breakout Signals

| Symbol | Score | Vol 3v1 | Z-Score Vol | Liq 3d | Streak |
|--------|-------|---------|-------------|--------|--------|
| wSOL | 57845.95 | 2.52x | 1.68 | $57.84M | 7d |

### 👀 Watch List

*3 tokens showing elevated activity*

📄 [Full data: signals_filtered.csv](data/signals_filtered.csv)

---

## 📈 Historical Data

**Total Historical Records**: 475
**Unique Tokens Tracked**: 101
**Date Range**: 2025-10-01 to 2025-10-07

**Master Aggregations**: 101 tokens
**Performance Metrics**: 475 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 475 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 101 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 475 |
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
