# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-11-03 18:45 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **34 tokens tracked** | 
💰 **$366.59M 24h volume** | 
💧 **$65.83M liquidity** | 
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
          3,
          4,
          12,
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
      "AI4",
      "LION",
      "RAGEGUY",
      "1nu",
      "DREAM",
      "HAROLD",
      "1",
      "FARTLESS",
      "SHITTER",
      "AUSBAGWORK"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          65801.4,
          29031.86,
          20266.02,
          13131.09,
          12435.64,
          11772.49,
          663.13,
          409.59,
          357.32,
          352.57
        ],
        "backgroundColor": [
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#ef4444",
          "#22c55e",
          "#eab308",
          "#f97316"
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
      "2025-11-03"
    ],
    "datasets": [
      {
        "label": "AI4",
        "data": [
          0.0,
          0.0,
          0.0,
          50.98,
          50.56,
          52.53,
          52.35
        ],
        "borderColor": "#3b82f6",
        "backgroundColor": "#3b82f620",
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
          29.97
        ],
        "borderColor": "#22c55e",
        "backgroundColor": "#22c55e20",
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
          49.11
        ],
        "borderColor": "#eab308",
        "backgroundColor": "#eab30820",
        "tension": 0.3,
        "fill": false
      },
      {
        "label": "DREAM",
        "data": [
          0.0,
          0.0,
          0.0,
          31.97,
          31.96,
          32.3,
          33.36
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
            "x": 245045.0,
            "y": 52.35,
            "r": 8,
            "label": "AI4: $245,045 FDV, 52.4% concentration (low risk)"
          },
          {
            "x": 47479306.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $47,479,306 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 497410.0,
            "y": 29.97,
            "r": 8,
            "label": "RAGEGUY: $497,410 FDV, 30.0% concentration (low risk)"
          },
          {
            "x": 47222.0,
            "y": 49.11,
            "r": 8,
            "label": "1nu: $47,222 FDV, 49.1% concentration (low risk)"
          },
          {
            "x": 686590.0,
            "y": 33.36,
            "r": 8,
            "label": "DREAM: $686,590 FDV, 33.4% concentration (low risk)"
          },
          {
            "x": 378573.0,
            "y": 36.43,
            "r": 8,
            "label": "FARTLESS: $378,573 FDV, 36.4% concentration (low risk)"
          },
          {
            "x": 64156.0,
            "y": 58.91,
            "r": 8,
            "label": "RUECAT: $64,156 FDV, 58.9% concentration (low risk)"
          },
          {
            "x": 18701.0,
            "y": 30.08,
            "r": 8,
            "label": "FLY: $18,701 FDV, 30.1% concentration (low risk)"
          },
          {
            "x": 1068093.0,
            "y": 24.74,
            "r": 8,
            "label": "XBT: $1,068,093 FDV, 24.7% concentration (low risk)"
          },
          {
            "x": 16071410.0,
            "y": 39.94,
            "r": 8,
            "label": "AI20X: $16,071,410 FDV, 39.9% concentration (low risk)"
          },
          {
            "x": 378295.0,
            "y": 35.75,
            "r": 8,
            "label": "ELIZABETH: $378,295 FDV, 35.8% concentration (low risk)"
          },
          {
            "x": 101744.0,
            "y": 46.82,
            "r": 8,
            "label": "USEFUL: $101,744 FDV, 46.8% concentration (low risk)"
          },
          {
            "x": 134167.0,
            "y": 40.38,
            "r": 8,
            "label": "USDUT: $134,167 FDV, 40.4% concentration (low risk)"
          },
          {
            "x": 159868.0,
            "y": 45.65,
            "r": 8,
            "label": "gib: $159,868 FDV, 45.6% concentration (low risk)"
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
            "x": 2968812.0,
            "y": 63.87,
            "r": 8,
            "label": "HAROLD: $2,968,812 FDV, 63.9% concentration (medium risk)"
          },
          {
            "x": 21363.0,
            "y": 65.14,
            "r": 8,
            "label": "SHITTER: $21,363 FDV, 65.1% concentration (medium risk)"
          },
          {
            "x": 16946.0,
            "y": 64.41,
            "r": 8,
            "label": "$CrepSol: $16,946 FDV, 64.4% concentration (medium risk)"
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
            "x": 5226.0,
            "y": 90.04,
            "r": 8,
            "label": "AUSBAGWORK: $5,226 FDV, 90.0% concentration (high risk)"
          },
          {
            "x": 8958.0,
            "y": 80.77,
            "r": 8,
            "label": "1Bull: $8,958 FDV, 80.8% concentration (high risk)"
          },
          {
            "x": 3852.0,
            "y": 81.58,
            "r": 8,
            "label": "APOLLO: $3,852 FDV, 81.6% concentration (high risk)"
          },
          {
            "x": 5437.0,
            "y": 92.01,
            "r": 8,
            "label": "FARTWORM: $5,437 FDV, 92.0% concentration (high risk)"
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
            "x": 3590.0,
            "y": 97.98,
            "r": 8,
            "label": "1: $3,590 FDV, 98.0% concentration (extreme risk)"
          },
          {
            "x": 15153904.0,
            "y": 96.8,
            "r": 8,
            "label": "SOL: $15,153,904 FDV, 96.8% concentration (extreme risk)"
          },
          {
            "x": 4155.0,
            "y": 96.64,
            "r": 8,
            "label": "7: $4,155 FDV, 96.6% concentration (extreme risk)"
          },
          {
            "x": 5158.0,
            "y": 96.38,
            "r": 8,
            "label": "SUPRACOIN: $5,158 FDV, 96.4% concentration (extreme risk)"
          },
          {
            "x": 4164.0,
            "y": 96.24,
            "r": 8,
            "label": "RWA: $4,164 FDV, 96.2% concentration (extreme risk)"
          },
          {
            "x": 8026.0,
            "y": 98.78,
            "r": 8,
            "label": "JIFFPOM: $8,026 FDV, 98.8% concentration (extreme risk)"
          },
          {
            "x": 3780.0,
            "y": 97.68,
            "r": 8,
            "label": "Bagwork: $3,780 FDV, 97.7% concentration (extreme risk)"
          },
          {
            "x": 3883.0,
            "y": 97.5,
            "r": 8,
            "label": "obvious: $3,883 FDV, 97.5% concentration (extreme risk)"
          },
          {
            "x": 3633.0,
            "y": 98.09,
            "r": 8,
            "label": "Hosico: $3,633 FDV, 98.1% concentration (extreme risk)"
          },
          {
            "x": 3794.0,
            "y": 98.05,
            "r": 8,
            "label": "viewer: $3,794 FDV, 98.0% concentration (extreme risk)"
          },
          {
            "x": 3154.0,
            "y": 99.39,
            "r": 8,
            "label": "retail: $3,154 FDV, 99.4% concentration (extreme risk)"
          },
          {
            "x": 9104.0,
            "y": 93.86,
            "r": 8,
            "label": "MOCHI: $9,104 FDV, 93.9% concentration (extreme risk)"
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
| 1 | XBT | XBT | 24.74% | 🟢 low | $53.09 | $454.35 |
| 2 | RAGEGUY | Rage Guy | 29.97% | 🟢 low | $20.27K | $100.06K |
| 3 | FLY | Nexa | 30.08% | 🟢 low | $100.10 | $6.14K |
| 4 | DREAM | Dreamsync | 33.36% | 🟢 low | $12.44K | $104.48K |
| 5 | ELIZABETH | Just Elizabeth Cat | 35.75% | 🟢 low | $3.30 | $30.15 |
| 6 | FARTLESS | FARTLESS COIN | 36.43% | 🟢 low | $409.59 | $2.56K |
| 7 | AI20X | Ai20x.ai | 39.94% | 🟢 low | $22.88 | $1.97M |
| 8 | USDUT | unstable tether | 40.38% | 🟢 low | $0.92 | $39.62 |
| 9 | gib | gib | 45.65% | 🟢 low | $0.57 | $28.02 |
| 10 | USEFUL | USEFUL COIN | 46.82% | 🟢 low | $0.99 | $36.23 |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | retail | retail | 99.39% | 🔴 extreme | $0.37 | $6.27K |
| 2 | JIFFPOM | Jiffpom | 98.78% | 🔴 extreme | $9.17 | $11.59K |
| 3 | Hosico | Hosico Cat | 98.09% | 🔴 extreme | $1.86 | $6.71K |
| 4 | viewer | in a streamers world | 98.05% | 🔴 extreme | $0.50 | $7.28K |
| 5 | 1 | 1 pill can change your li | 97.98% | 🔴 extreme | $663.13 | $6.72K |
| 6 | Bagwork | African Bagwork | 97.68% | 🔴 extreme | $4.90 | $7.21K |
| 7 | obvious | in hindsight | 97.50% | 🔴 extreme | $2.42 | $6.99K |
| 8 | SOL | Solana | 96.80% | 🔴 extreme | $191.37 | $3.78K |
| 9 | 7 | 7 Coin | 96.64% | 🔴 extreme | $64.44 | $7.44K |
| 10 | SUPRACOIN | GIVING CAR AWAY AT 10MIL  | 96.38% | 🔴 extreme | $38.65 | $9.07K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 34
**Combined 24h Volume**: $366.59M
**Combined Liquidity**: $65.83M

**Concentration Risk Distribution**:
- 🟢 Low: 14 tokens
- 🔴 Extreme: 12 tokens
- 🟡 High: 4 tokens
- 🟢 Medium: 3 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $366.44M | $61.46M | 🟢 unknown |
| 2 | AI4 | AI⁴ | $65.80K | $88.23K | 🟢 low |
| 3 | LION | Loaded Lions | $29.03K | $1.42M | 🟢 low |
| 4 | RAGEGUY | Rage Guy | $20.27K | $100.06K | 🟢 low |
| 5 | 1nu | 1nu | $13.13K | $28.83K | 🟢 low |
| 6 | DREAM | Dreamsync | $12.44K | $104.48K | 🟢 low |
| 7 | HAROLD | Harold | $11.77K | $440.43K | 🟢 medium |
| 8 | 1 | 1 pill can change your life | $663.13 | $6.72K | 🔴 extreme |
| 9 | FARTLESS | FARTLESS COIN | $409.59 | $2.56K | 🟢 low |
| 10 | SHITTER | SHITTERCOIN | $357.32 | $20.56K | 🟢 medium |

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
- 👀 **Watch**: 112 tokens
- 🚀 **Breakout**: 3 tokens
- ❄️ **Cooling**: 1 tokens

### 🚀 Breakout Signals

| Symbol | Score | Vol 3v1 | Z-Score Vol | Liq 3d | Streak |
|--------|-------|---------|-------------|--------|--------|
| wSOL | 4.24 | 2.51x | 1.69 | $57.82M | 0d |
| XBT | 3.65 | 2.10x | 1.74 | $421.14K | 0d |
| USDUT | 3.57 | 2.36x | 1.51 | $150.84K | 0d |

### 👀 Watch List

*112 tokens showing elevated activity*

📄 [Full data: signals_filtered.csv](data/signals_filtered.csv)

---

## 📈 Historical Data

**Total Historical Records**: 508
**Unique Tokens Tracked**: 101
**Date Range**: 2025-10-01 to 2025-11-03

**Master Aggregations**: 101 tokens
**Performance Metrics**: 508 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 508 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 101 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 508 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 34 |
| [new_viable.csv](data/new_viable.csv) | New tokens with potential | 0 |
| [signals_filtered.csv](data/signals_filtered.csv) | Whale-filtered trading signals | 116 |

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
