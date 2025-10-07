# 📊 Solana Radar - Daily Reports

**Last Updated**: 2025-10-07 22:00 UTC

Automated daily analysis of Solana tokens with whale tracking and momentum indicators.

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 33
**Combined 24h Volume**: $409.44M
**Combined Liquidity**: $59.02M

**Concentration Risk Distribution**:
- 🟢 Low: 17 tokens
- 🔴 Extreme: 6 tokens
- 🟡 High: 5 tokens
- 🟢 Medium: 4 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $408.39M | $57.46M | 🟢 unknown |
| 2 | XBT | XBT | $587.34K | $444.63K | 🟢 low |
| 3 | early | not wrong just early | $119.19K | $33.19K | 🟢 low |
| 4 | USDUT | unstable tether | $57.89K | $114.66K | 🟢 low |
| 5 | CHARLIE | RIP CHARLIE KIRK | $45.37K | $98.59K | 🟢 low |
| 6 | 1nu | 1nu | $38.77K | $36.41K | 🟢 low |
| 7 | gib | gib | $30.56K | $158.28K | 🟢 low |
| 8 | 67 | 67coin | $27.51K | $54.06K | 🟢 low |
| 9 | Useless | Useless Coin | $27.30K | $56.29K | 🟢 low |
| 10 | SOL | Solana | $26.54K | $11.19K | 🔴 extreme |

📄 [Full data: daily_top50.csv](data/daily_top50.csv)

---

## 🌱 New Viable Tokens (7-14 Days Old)

New tokens showing potential with healthy metrics and lower concentration risk.

*No viable new tokens found with current criteria*

---

## 📈 Top Movers (24h Change)

Tokens with significant price or volume changes in the last 24 hours.

**Total Movers**: 23
- 🚀 **Gainers** (>+20%): 1
- 📉 **Losers** (<-20%): 11
- 📊 **Volume Spikes** (>+100%): 14

### 🚀 Top Gainers

| # | Symbol | Name | Change 24h | Current Price | Volume Change | Risk |
|---|--------|------|------------|---------------|---------------|------|
| 9 | XBT | XBT | +28.44% | $0.00 | +34.2% | 🟢 |

### 📉 Biggest Losers

| # | Symbol | Name | Change 24h | Current Price | Volume Change | Risk |
|---|--------|------|------------|---------------|---------------|------|
| 1 | early | not wrong just early | -70.64% | $0.00 | +376.0% | 🟢 |
| 2 | SOL | Solana | -63.56% | $400.92 | +10185.4% | 🔴 |
| 3 | RUECAT | Rue Cat | -47.71% | $0.00 | -53.2% | 🟢 |
| 4 | 1nu | 1nu | -32.80% | $0.00 | -7.3% | 🟢 |
| 5 | T-2049 | Token 2049 | -31.57% | $0.00 | +7.4% | 🟢 |
| 6 | FARTLESS | FARTLESS COIN | -31.11% | $0.00 | +31.9% | 🟢 |
| 7 | 1Bull | One bull run to change yo | -31.09% | $0.00 | -34.8% | 🟢 |
| 8 | APOLLO | Apollo AI | -29.85% | $0.00 | -22.3% | 🟢 |
| 10 | CHARLIE | RIP CHARLIE KIRK | -20.72% | $0.00 | +22.5% | 🟢 |
| 11 | walkusa | WALKING ACROSS AMERICA | -20.47% | $0.00 | +384.9% | 🟢 |

📄 [Full data: top_movers.csv](data/top_movers.csv)

---

## 🎯 Trading Signals (Whale Filtered)

Signals filtered to exclude tokens with extreme concentration risk.

**Signal Distribution**:
- 👀 **Watch**: 3 tokens
- 🚀 **Breakout**: 2 tokens

### 🚀 Breakout Signals

| Symbol | Score | Vol 3v1 | Z-Score Vol | Liq 3d | Streak |
|--------|-------|---------|-------------|--------|--------|
| wSOL | 57832.09 | 2.51x | 1.69 | $57.82M | 7d |
| XBT | 430.91 | 2.10x | 1.74 | $421.14K | 7d |

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
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 33 |
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
