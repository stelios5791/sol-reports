# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-10-20 22:02 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **43 tokens tracked** | 
💰 **$220.46M 24h volume** | 
💧 **$58.25M liquidity** | 
🟢 **14 low-risk tokens**

---

## 🎨 Interactive Charts

### 🥧 Risk Distribution


    <canvas id="riskPieChart"></canvas>
<div style="max-width: 900px; margin: 20px auto;">
  <canvas id="riskPieChart"></canvas>
</div>
<script>
(function() {
  const ctx = document.getElementById('riskPieChart');
  if (!ctx) {
    console.error('Canvas riskPieChart not found');
    return;
  }
  try {
    new Chart(ctx, {
  "type": "pie",
  "data": {
    "labels": [
      "Low Risk",
      "Medium Risk",
      "High Risk",
      "Extreme Risk",
      "Unknown"
    ],
    "datasets": [
      {
        "data": [
          14,
          2,
          8,
          18,
          1
        ],
        "backgroundColor": [
          "#22c55e",
          "#eab308",
          "#f97316",
          "#ef4444",
          "#94a3b8"
        ]
      }
    ]
  },
  "options": {
    "responsive": true,
    "plugins": {
      "legend": {
        "position": "bottom"
      },
      "title": {
        "display": true,
        "text": "Token Concentration Risk Distribution",
        "font": {
          "size": 16
        }
      }
    }
  }
});
  } catch(e) {
    console.error('Chart riskPieChart failed:', e);
  }
})();
</script>


### 📊 7-Day Performance

*Insufficient historical data for 7-day performance*

### 📈 Volume Leaders


    <canvas id="volumeBarChart"></canvas>
<div style="max-width: 900px; margin: 20px auto;">
  <canvas id="volumeBarChart"></canvas>
</div>
<script>
(function() {
  const ctx = document.getElementById('volumeBarChart');
  if (!ctx) {
    console.error('Canvas volumeBarChart not found');
    return;
  }
  try {
    new Chart(ctx, {
  "type": "bar",
  "data": {
    "labels": [
      "DREAM",
      "AI4",
      "RAGEGUY",
      "LION",
      "1nu",
      "HAROLD",
      "$CrepSol",
      "FARTLESS",
      "SHITTER",
      "SOL"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          211070.56,
          83759.54,
          54654.45,
          21085.75,
          20239.3,
          6375.27,
          1292.28,
          792.38,
          520.06,
          262.49
        ],
        "backgroundColor": [
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#ef4444"
        ]
      }
    ]
  },
  "options": {
    "responsive": true,
    "plugins": {
      "legend": {
        "display": false
      },
      "title": {
        "display": true,
        "text": "Top 10 Tokens by 24h Volume (excl. wSOL)",
        "font": {
          "size": 16
        }
      }
    },
    "scales": {
      "y": {
        "beginAtZero": true,
        "title": {
          "display": true,
          "text": "Volume (USD)"
        }
      }
    }
  }
});
  } catch(e) {
    console.error('Chart volumeBarChart failed:', e);
  }
})();
</script>


### 📉 Concentration Trends


    <canvas id="trendLineChart"></canvas>
<div style="max-width: 900px; margin: 20px auto;">
  <canvas id="trendLineChart"></canvas>
</div>
<script>
(function() {
  const ctx = document.getElementById('trendLineChart');
  if (!ctx) {
    console.error('Canvas trendLineChart not found');
    return;
  }
  try {
    new Chart(ctx, {
  "type": "line",
  "data": {
    "labels": [
      "2025-10-01",
      "2025-10-03",
      "2025-10-04",
      "2025-10-05",
      "2025-10-06",
      "2025-10-07",
      "2025-10-20"
    ],
    "datasets": [
      {
        "label": "DREAM",
        "data": [
          0.0,
          0.0,
          0.0,
          31.97,
          31.96,
          32.3,
          31.91
        ],
        "borderColor": "#3b82f6",
        "backgroundColor": "#3b82f620",
        "tension": 0.3,
        "fill": false
      },
      {
        "label": "AI4",
        "data": [
          0.0,
          0.0,
          0.0,
          50.98,
          50.56,
          52.53,
          48.91
        ],
        "borderColor": "#ef4444",
        "backgroundColor": "#ef444420",
        "tension": 0.3,
        "fill": false
      },
      {
        "label": "RAGEGUY",
        "data": [
          0.0,
          0.0,
          0.0,
          25.99,
          26.1,
          25.76,
          27.61
        ],
        "borderColor": "#22c55e",
        "backgroundColor": "#22c55e20",
        "tension": 0.3,
        "fill": false
      },
      {
        "label": "LION",
        "data": [
          0.0,
          0.0,
          0.0,
          57.84,
          57.84,
          57.84,
          57.84
        ],
        "borderColor": "#eab308",
        "backgroundColor": "#eab30820",
        "tension": 0.3,
        "fill": false
      },
      {
        "label": "1nu",
        "data": [
          0.0,
          0.0,
          0.0,
          0.0,
          33.63,
          33.3,
          38.4,
          43.55
        ],
        "borderColor": "#8b5cf6",
        "backgroundColor": "#8b5cf620",
        "tension": 0.3,
        "fill": false
      }
    ]
  },
  "options": {
    "responsive": true,
    "plugins": {
      "legend": {
        "position": "top"
      },
      "title": {
        "display": true,
        "text": "Top 10 Holder Concentration Over Time",
        "font": {
          "size": 16
        }
      }
    },
    "scales": {
      "y": {
        "beginAtZero": true,
        "max": 100,
        "title": {
          "display": true,
          "text": "Concentration (%)"
        }
      },
      "x": {
        "title": {
          "display": true,
          "text": "Date"
        }
      }
    }
  }
});
  } catch(e) {
    console.error('Chart trendLineChart failed:', e);
  }
})();
</script>


### 💎 Market Cap vs Concentration


    <canvas id="scatterChart"></canvas>
<div style="max-width: 900px; margin: 20px auto;">
  <canvas id="scatterChart"></canvas>
</div>
<script>
(function() {
  const ctx = document.getElementById('scatterChart');
  if (!ctx) {
    console.error('Canvas scatterChart not found');
    return;
  }
  try {
    new Chart(ctx, {
  "type": "scatter",
  "data": {
    "datasets": [
      {
        "label": "Low Risk",
        "data": [
          {
            "x": 1542505.0,
            "y": 31.91,
            "r": 8,
            "label": "DREAM: $1,542,505 FDV, 31.9% concentration (low risk)"
          },
          {
            "x": 209096.0,
            "y": 48.91,
            "r": 8,
            "label": "AI4: $209,096 FDV, 48.9% concentration (low risk)"
          },
          {
            "x": 737959.0,
            "y": 27.61,
            "r": 8,
            "label": "RAGEGUY: $737,959 FDV, 27.6% concentration (low risk)"
          },
          {
            "x": 57026813.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $57,026,813 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 54653.0,
            "y": 43.55,
            "r": 8,
            "label": "1nu: $54,653 FDV, 43.5% concentration (low risk)"
          },
          {
            "x": 36402.0,
            "y": 56.33,
            "r": 8,
            "label": "$CrepSol: $36,402 FDV, 56.3% concentration (low risk)"
          },
          {
            "x": 716918.0,
            "y": 34.73,
            "r": 8,
            "label": "FARTLESS: $716,918 FDV, 34.7% concentration (low risk)"
          },
          {
            "x": 87899.0,
            "y": 54.45,
            "r": 8,
            "label": "RUECAT: $87,899 FDV, 54.5% concentration (low risk)"
          },
          {
            "x": 1501083.0,
            "y": 22.64,
            "r": 8,
            "label": "XBT: $1,501,083 FDV, 22.6% concentration (low risk)"
          },
          {
            "x": 18829748.0,
            "y": 39.75,
            "r": 8,
            "label": "AI20X: $18,829,748 FDV, 39.8% concentration (low risk)"
          },
          {
            "x": 713381.0,
            "y": 30.93,
            "r": 8,
            "label": "ELIZABETH: $713,381 FDV, 30.9% concentration (low risk)"
          },
          {
            "x": 18301.0,
            "y": 30.33,
            "r": 8,
            "label": "FLY: $18,301 FDV, 30.3% concentration (low risk)"
          },
          {
            "x": 105149.0,
            "y": 44.46,
            "r": 8,
            "label": "YAO: $105,149 FDV, 44.5% concentration (low risk)"
          },
          {
            "x": 129116.0,
            "y": 44.79,
            "r": 8,
            "label": "USEFUL: $129,116 FDV, 44.8% concentration (low risk)"
          }
        ],
        "backgroundColor": "#22c55e",
        "borderColor": "#22c55e",
        "borderWidth": 1
      },
      {
        "label": "Medium Risk",
        "data": [
          {
            "x": 3061164.0,
            "y": 63.56,
            "r": 8,
            "label": "HAROLD: $3,061,164 FDV, 63.6% concentration (medium risk)"
          },
          {
            "x": 20615.0,
            "y": 66.11,
            "r": 8,
            "label": "SHITTER: $20,615 FDV, 66.1% concentration (medium risk)"
          }
        ],
        "backgroundColor": "#eab308",
        "borderColor": "#eab308",
        "borderWidth": 1
      },
      {
        "label": "High Risk",
        "data": [
          {
            "x": 6214.0,
            "y": 90.03,
            "r": 8,
            "label": "FARTWORM: $6,214 FDV, 90.0% concentration (high risk)"
          },
          {
            "x": 14288.0,
            "y": 88.01,
            "r": 8,
            "label": "AUSBAGWORK: $14,288 FDV, 88.0% concentration (high risk)"
          },
          {
            "x": 9485.0,
            "y": 79.44,
            "r": 8,
            "label": "1Bull: $9,485 FDV, 79.4% concentration (high risk)"
          },
          {
            "x": 9713.0,
            "y": 89.39,
            "r": 8,
            "label": "IDIOT: $9,713 FDV, 89.4% concentration (high risk)"
          },
          {
            "x": 8984.0,
            "y": 88.86,
            "r": 8,
            "label": "DARE: $8,984 FDV, 88.9% concentration (high risk)"
          },
          {
            "x": 10699.0,
            "y": 92.63,
            "r": 8,
            "label": "MOCHI: $10,699 FDV, 92.6% concentration (high risk)"
          },
          {
            "x": 5386.0,
            "y": 90.44,
            "r": 8,
            "label": "RWA: $5,386 FDV, 90.4% concentration (high risk)"
          },
          {
            "x": 1572.0,
            "y": 96.51,
            "r": 8,
            "label": "PROFIT: $1,572 FDV, 96.5% concentration (high risk)"
          }
        ],
        "backgroundColor": "#f97316",
        "borderColor": "#f97316",
        "borderWidth": 1
      },
      {
        "label": "Extreme Risk",
        "data": [
          {
            "x": 11591454.0,
            "y": 96.74,
            "r": 8,
            "label": "SOL: $11,591,454 FDV, 96.7% concentration (extreme risk)"
          },
          {
            "x": 4373.0,
            "y": 97.66,
            "r": 8,
            "label": "1: $4,373 FDV, 97.7% concentration (extreme risk)"
          },
          {
            "x": 4547.0,
            "y": 95.39,
            "r": 8,
            "label": "pibble: $4,547 FDV, 95.4% concentration (extreme risk)"
          },
          {
            "x": 5804.0,
            "y": 95.62,
            "r": 8,
            "label": "7: $5,804 FDV, 95.6% concentration (extreme risk)"
          },
          {
            "x": 4008.0,
            "y": 98.8,
            "r": 8,
            "label": "19: $4,008 FDV, 98.8% concentration (extreme risk)"
          },
          {
            "x": 3512.0,
            "y": 99.46,
            "r": 8,
            "label": "ORE: $3,512 FDV, 99.5% concentration (extreme risk)"
          },
          {
            "x": 3677.0,
            "y": 99.2,
            "r": 8,
            "label": "GAZABOY: $3,677 FDV, 99.2% concentration (extreme risk)"
          },
          {
            "x": 6312.0,
            "y": 98.6,
            "r": 8,
            "label": "JIFFPOM: $6,312 FDV, 98.6% concentration (extreme risk)"
          },
          {
            "x": 4312.0,
            "y": 99.28,
            "r": 8,
            "label": "BEANS: $4,312 FDV, 99.3% concentration (extreme risk)"
          },
          {
            "x": 4166.0,
            "y": 97.02,
            "r": 8,
            "label": "Streamless: $4,166 FDV, 97.0% concentration (extreme risk)"
          },
          {
            "x": 4126.0,
            "y": 97.87,
            "r": 8,
            "label": "viewer: $4,126 FDV, 97.9% concentration (extreme risk)"
          },
          {
            "x": 4686.0,
            "y": 97.19,
            "r": 8,
            "label": "BULLCOIN: $4,686 FDV, 97.2% concentration (extreme risk)"
          },
          {
            "x": 3333.0,
            "y": 99.62,
            "r": 8,
            "label": "ACTIVITIES: $3,333 FDV, 99.6% concentration (extreme risk)"
          },
          {
            "x": 5595.4,
            "y": 99.88,
            "r": 8,
            "label": "1cat: $5,595 FDV, 99.9% concentration (extreme risk)"
          },
          {
            "x": 4251.0,
            "y": 97.28,
            "r": 8,
            "label": "obvious: $4,251 FDV, 97.3% concentration (extreme risk)"
          },
          {
            "x": 4837.0,
            "y": 98.68,
            "r": 8,
            "label": "REVIVE: $4,837 FDV, 98.7% concentration (extreme risk)"
          },
          {
            "x": 5750.14,
            "y": 99.97,
            "r": 8,
            "label": "LOW: $5,750 FDV, 100.0% concentration (extreme risk)"
          },
          {
            "x": 5465.86,
            "y": 99.7,
            "r": 8,
            "label": "1SOL: $5,466 FDV, 99.7% concentration (extreme risk)"
          }
        ],
        "backgroundColor": "#ef4444",
        "borderColor": "#ef4444",
        "borderWidth": 1
      }
    ]
  },
  "options": {
    "responsive": true,
    "plugins": {
      "legend": {
        "position": "top"
      },
      "title": {
        "display": true,
        "text": "Market Cap (FDV) vs Holder Concentration",
        "font": {
          "size": 16
        }
      },
      "tooltip": {
        "callbacks": {}
      }
    },
    "scales": {
      "x": {
        "type": "logarithmic",
        "title": {
          "display": true,
          "text": "FDV (USD) - Log Scale"
        }
      },
      "y": {
        "beginAtZero": true,
        "max": 100,
        "title": {
          "display": true,
          "text": "Top 10 Holder %"
        }
      }
    }
  }
});
  } catch(e) {
    console.error('Chart scatterChart failed:', e);
  }
})();
</script>


---

### 🏆 Safest Tokens (Lowest Holder Concentration)

Top 10 tokens with the most distributed ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | XBT | XBT | 22.64% | 🟢 low | $112.42 | $581.01 |
| 2 | RAGEGUY | Rage Guy | 27.61% | 🟢 low | $54.65K | $128.23K |
| 3 | FLY | Nexa | 30.33% | 🟢 low | $7.19 | $2.49K |
| 4 | ELIZABETH | Just Elizabeth Cat | 30.93% | 🟢 low | $20.57 | $41.03 |
| 5 | DREAM | Dreamsync | 31.91% | 🟢 low | $211.07K | $166.32K |
| 6 | FARTLESS | FARTLESS COIN | 34.73% | 🟢 low | $792.38 | $3.49K |
| 7 | AI20X | Ai20x.ai | 39.75% | 🟢 low | $42.10 | $2.24M |
| 8 | 1nu | 1nu | 43.55% | 🟢 low | $20.24K | $30.47K |
| 9 | YAO | YAO MING | 44.46% | 🟢 low | $2.80 | $723.84 |
| 10 | USEFUL | USEFUL COIN | 44.79% | 🟢 low | $0.78 | $55.49 |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | LOW | lowcut | 99.97% | 🔴 extreme | $0.00 | $0.00 |
| 2 | 1cat | 1 cat can change your lif | 99.88% | 🔴 extreme | $0.82 | $0.00 |
| 3 | 1SOL | 1 SOL and a dream | 99.70% | 🔴 extreme | $0.00 | $0.00 |
| 4 | ACTIVITIES | REAL LIFE ACTIVITIES | 99.62% | 🔴 extreme | $1.23 | $6.64K |
| 5 | ORE | Ore Labs | 99.46% | 🔴 extreme | $17.89 | $6.85K |
| 6 | BEANS | BEANS | 99.28% | 🔴 extreme | $3.41 | $8.39K |
| 7 | GAZABOY | GAZA BOY | 99.20% | 🔴 extreme | $4.64 | $7.18K |
| 8 | 19 | Cult of 19 | 98.80% | 🔴 extreme | $18.75 | $7.42K |
| 9 | REVIVE | reviving the memes | 98.68% | 🔴 extreme | $0.35 | $9.48K |
| 10 | JIFFPOM | Jiffpom | 98.60% | 🔴 extreme | $3.66 | $10.48K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 43
**Combined 24h Volume**: $220.46M
**Combined Liquidity**: $58.25M

**Concentration Risk Distribution**:
- 🔴 Extreme: 18 tokens
- 🟢 Low: 14 tokens
- 🟡 High: 8 tokens
- 🟢 Medium: 2 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $220.06M | $53.17M | 🟢 unknown |
| 2 | DREAM | Dreamsync | $211.07K | $166.32K | 🟢 low |
| 3 | AI4 | AI⁴ | $83.76K | $84.86K | 🟢 low |
| 4 | RAGEGUY | Rage Guy | $54.65K | $128.23K | 🟢 low |
| 5 | LION | Loaded Lions | $21.09K | $1.65M | 🟢 low |
| 6 | 1nu | 1nu | $20.24K | $30.47K | 🟢 low |
| 7 | HAROLD | Harold | $6.38K | $472.20K | 🟢 medium |
| 8 | $CrepSol | Crepe on Solana | $1.29K | $22.18K | 🟢 low |
| 9 | FARTLESS | FARTLESS COIN | $792.38 | $3.49K | 🟢 low |
| 10 | SHITTER | SHITTERCOIN | $520.06 | $20.13K | 🟢 medium |

📄 [Full data: daily_top50.csv](data/daily_top50.csv)

---

## 🌱 New Viable Tokens (7-14 Days Old)

New tokens showing potential with healthy metrics and lower concentration risk.

*No viable new tokens found with current criteria*

---

## 📈 Top Movers (24h Change)

Tokens with significant price or volume changes in the last 24 hours.

**Total Movers**: 10
- 🚀 **Gainers** (>+20%): 1
- 📉 **Losers** (<-20%): 1
- 📊 **Volume Spikes** (>+100%): 9

### 🚀 Top Gainers

| # | Symbol | Name | Change 24h | Current Price | Volume Change | Risk |
|---|--------|------|------------|---------------|---------------|------|
| 1 | $CrepSol | Crepe on Solana | +51.73% | $0.00 | +229.1% | 🟢 |

📄 [Full data: top_movers.csv](data/top_movers.csv)

---

## 🎯 Trading Signals (Whale Filtered)

Signals filtered to exclude tokens with extreme concentration risk.

**Signal Distribution**:
- 👀 **Watch**: 113 tokens
- 🚀 **Breakout**: 3 tokens
- ❄️ **Cooling**: 1 tokens

### 🚀 Breakout Signals

| Symbol | Score | Vol 3v1 | Z-Score Vol | Liq 3d | Streak |
|--------|-------|---------|-------------|--------|--------|
| wSOL | 4.24 | 2.51x | 1.69 | $57.82M | 0d |
| XBT | 3.65 | 2.10x | 1.74 | $421.14K | 0d |
| USDUT | 3.57 | 2.36x | 1.51 | $150.84K | 0d |

### 👀 Watch List

*113 tokens showing elevated activity*

📄 [Full data: signals_filtered.csv](data/signals_filtered.csv)

---

## 📈 Historical Data

**Total Historical Records**: 517
**Unique Tokens Tracked**: 102
**Date Range**: 2025-10-01 to 2025-10-20

**Master Aggregations**: 102 tokens
**Performance Metrics**: 517 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 517 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 102 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 517 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 43 |
| [new_viable.csv](data/new_viable.csv) | New tokens with potential | 0 |
| [signals_filtered.csv](data/signals_filtered.csv) | Whale-filtered trading signals | 117 |

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

- **Live Dashboard**: [https://stelios5791.github.io/sol-reports/](https://stelios5791.github.io/sol-reports/)
- **Data Repository**: [stelios5791/sol-reports](https://github.com/stelios5791/sol-reports)
- **Analysis Pipeline**: Private repository (automated daily)

---

*Generated automatically by Solana Radar v2.0*
