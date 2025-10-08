# 📊 Solana Radar - Daily Reports

**Last Updated**: 2025-10-08 08:37 UTC

Automated daily analysis of Solana tokens with whale tracking and momentum indicators.

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 50
**Combined 24h Volume**: $393.08M
**Combined Liquidity**: $63.71M

**Concentration Risk Distribution**:
- 🔴 Extreme: 19 tokens
- 🟢 Low: 14 tokens
- 🟡 High: 10 tokens
- 🟢 Medium: 6 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $392.69M | $57.48M | 🟢 unknown |
| 2 | AI4 | AI⁴ | $176.06K | $97.82K | 🟢 low |
| 3 | RAGEGUY | Rage Guy | $81.77K | $137.63K | 🟢 low |
| 4 | HAROLD | Harold | $41.31K | $543.53K | 🟢 medium |
| 5 | 1nu | 1nu | $27.78K | $31.22K | 🟢 low |
| 6 | LION | Loaded Lions | $24.55K | $2.08M | 🟢 low |
| 7 | DREAM | Dreamsync | $11.76K | $177.75K | 🟢 low |
| 8 | RUECAT | Rue Cat | $10.72K | $61.53K | 🟢 low |
| 9 | SHITTER | SHITTERCOIN | $4.63K | $21.36K | 🟢 medium |
| 10 | FARTLESS | FARTLESS COIN | $2.88K | $4.13K | 🟢 low |

📄 [Full data: daily_top50.csv](data/daily_top50.csv)

---

## 🌱 New Viable Tokens (7-14 Days Old)

New tokens showing potential with healthy metrics and lower concentration risk.

**Found**: 3 viable new tokens

**Criteria**:
- First seen 7-14 days ago
- Volume > $50K
- Liquidity > $100K
- Missing streak < 2 (stable presence)
- Concentration risk: low/medium

| Symbol | Name | Age (days) | Volume 24h | Liquidity | Top 10% |
|--------|------|------------|------------|-----------|---------|
| wSOL | Wrapped SOL | 7 | $392.69M | $57.48M | 0.00% |
| RAGEGUY | Rage Guy | 7 | $81.77K | $137.63K | 26.91% |
| USDUT | unstable tether | 7 | $57.89K | $114.66K | 37.30% |

📄 [Full data: new_viable.csv](data/new_viable.csv)

---

## 📈 Top Movers (24h Change)

Tokens with significant price or volume changes in the last 24 hours.

**Total Movers**: 9
- 🚀 **Gainers** (>+20%): 0
- 📉 **Losers** (<-20%): 2
- 📊 **Volume Spikes** (>+100%): 7

### 📉 Biggest Losers

| # | Symbol | Name | Change 24h | Current Price | Volume Change | Risk |
|---|--------|------|------------|---------------|---------------|------|
| 1 | 1nu | 1nu | -26.57% | $0.00 | -28.3% | 🟢 |
| 2 | RAGEGUY | Rage Guy | -23.43% | $0.00 | +10.8% | 🟢 |

📄 [Full data: top_movers.csv](data/top_movers.csv)

---

## 🎯 Trading Signals (Whale Filtered)

Signals filtered to exclude tokens with extreme concentration risk.

**Signal Distribution**:
- 👀 **Watch**: 3 tokens

### 👀 Watch List

*3 tokens showing elevated activity*

📄 [Full data: signals_filtered.csv](data/signals_filtered.csv)

---

## 📈 Historical Data

**Total Historical Records**: 524
**Unique Tokens Tracked**: 101
**Date Range**: 2025-10-01 to 2025-10-08

**Master Aggregations**: 101 tokens
**Performance Metrics**: 524 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 524 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 101 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 524 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 50 |
| [new_viable.csv](data/new_viable.csv) | New tokens with potential | 3 |
| [signals_filtered.csv](data/signals_filtered.csv) | Whale-filtered trading signals | 3 |

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
