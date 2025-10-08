# 📊 Solana Radar - Daily Reports

**Last Updated**: 2025-10-08 20:17 UTC

Automated daily analysis of Solana tokens with whale tracking and momentum indicators.

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 50
**Combined 24h Volume**: $340.74M
**Combined Liquidity**: $65.05M

**Concentration Risk Distribution**:
- 🔴 Extreme: 21 tokens
- 🟢 Low: 15 tokens
- 🟡 High: 9 tokens
- 🟢 Medium: 4 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $340.17M | $58.73M | 🟢 unknown |
| 2 | AI4 | AI⁴ | $160.45K | $97.97K | 🟢 low |
| 3 | DREAM | Dreamsync | $96.61K | $184.29K | 🟢 low |
| 4 | AI20X | Ai20x.ai | $90.87K | $2.74M | 🟢 low |
| 5 | RAGEGUY | Rage Guy | $88.55K | $153.17K | 🟢 low |
| 6 | LION | Loaded Lions | $50.60K | $2.11M | 🟢 low |
| 7 | HAROLD | Harold | $40.71K | $558.81K | 🟢 medium |
| 8 | 1nu | 1nu | $27.63K | $30.57K | 🟢 low |
| 9 | $CrepSol | Crepe on Solana | $5.87K | $28.15K | 🟢 low |
| 10 | SHITTER | SHITTERCOIN | $4.42K | $22.73K | 🟢 medium |

📄 [Full data: daily_top50.csv](data/daily_top50.csv)

---

## 🌱 New Viable Tokens (7-14 Days Old)

New tokens showing potential with healthy metrics and lower concentration risk.

**Found**: 6 viable new tokens

**Criteria**:
- First seen 7-14 days ago
- Volume > $50K
- Liquidity > $100K
- Missing streak < 2 (stable presence)
- Concentration risk: low/medium

| Symbol | Name | Age (days) | Volume 24h | Liquidity | Top 10% |
|--------|------|------------|------------|-----------|---------|
| wSOL | Wrapped SOL | 7 | $340.17M | $58.73M | 0.00% |
| DREAM | Dreamsync | 7 | $96.61K | $184.29K | 32.23% |
| AI20X | Ai20x.ai | 7 | $90.87K | $2.74M | 41.38% |
| RAGEGUY | Rage Guy | 7 | $88.55K | $153.17K | 27.04% |
| USDUT | unstable tether | 7 | $57.89K | $114.66K | 37.30% |
| LION | Loaded Lions | 7 | $50.60K | $2.11M | 57.84% |

📄 [Full data: new_viable.csv](data/new_viable.csv)

---

## 📈 Top Movers (24h Change)

Tokens with significant price or volume changes in the last 24 hours.

**Total Movers**: 11
- 🚀 **Gainers** (>+20%): 1
- 📉 **Losers** (<-20%): 1
- 📊 **Volume Spikes** (>+100%): 10

### 🚀 Top Gainers

| # | Symbol | Name | Change 24h | Current Price | Volume Change | Risk |
|---|--------|------|------------|---------------|---------------|------|
| 1 | $CrepSol | Crepe on Solana | +55.53% | $0.00 | +222.2% | 🟢 |

### 📉 Biggest Losers

| # | Symbol | Name | Change 24h | Current Price | Volume Change | Risk |
|---|--------|------|------------|---------------|---------------|------|
| 2 | 1nu | 1nu | -29.73% | $0.00 | -28.7% | 🟢 |

📄 [Full data: top_movers.csv](data/top_movers.csv)

---

## 🎯 Trading Signals (Whale Filtered)

Signals filtered to exclude tokens with extreme concentration risk.

**Signal Distribution**:
- 👀 **Watch**: 5 tokens

### 👀 Watch List

*5 tokens showing elevated activity*

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
| [new_viable.csv](data/new_viable.csv) | New tokens with potential | 6 |
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
