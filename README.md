# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-11-08 22:22 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **27 tokens tracked** | 
💰 **$152.79M 24h volume** | 
💧 **$45.81M liquidity** | 
🟢 **13 low-risk tokens**

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
          13,
          4,
          5,
          4,
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


    <canvas id="performanceChart"></canvas>
<div style="max-width: 800px; margin: 20px auto;">
  <canvas id="performanceChart"></canvas>
</div>
<script>
(function() {
  const ctx = document.getElementById('performanceChart');
  if (!ctx) {
    console.error('Canvas performanceChart not found');
    return;
  }
  try {
    new Chart(ctx, {
  "type": "bar",
  "data": {
    "labels": [
      "1",
      "1"
    ],
    "datasets": [
      {
        "label": "7-Day Change %",
        "data": [
          -31.209946167649317,
          -31.209946167649317
        ],
        "backgroundColor": [
          "#ef4444",
          "#ef4444"
        ]
      }
    ]
  },
  "options": {
    "indexAxis": "y",
    "responsive": true,
    "plugins": {
      "legend": {
        "display": false
      },
      "title": {
        "display": true,
        "text": "7-Day Performance Leaders & Laggards",
        "font": {
          "size": 16
        }
      }
    },
    "scales": {
      "x": {
        "title": {
          "display": true,
          "text": "Change %"
        }
      }
    }
  }
});
  } catch(e) {
    console.error('Chart performanceChart failed:', e);
  }
})();
</script>


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
      "LION",
      "1nu",
      "DREAM",
      "RAGEGUY",
      "HAROLD",
      "1",
      "AI4",
      "RUECAT",
      "SOL",
      "1Bull"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          16052.74,
          15527.69,
          13050.35,
          11981.04,
          4260.54,
          3335.03,
          3297.86,
          856.75,
          505.66,
          367.17
        ],
        "backgroundColor": [
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#f97316",
          "#22c55e",
          "#eab308",
          "#ef4444",
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
      "2025-11-08"
    ],
    "datasets": [
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
        "borderColor": "#3b82f6",
        "backgroundColor": "#3b82f620",
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
          43.19
        ],
        "borderColor": "#ef4444",
        "backgroundColor": "#ef444420",
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
          33.06
        ],
        "borderColor": "#22c55e",
        "backgroundColor": "#22c55e20",
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
          30.6
        ],
        "borderColor": "#eab308",
        "backgroundColor": "#eab30820",
        "tension": 0.3,
        "fill": false
      },
      {
        "label": "HAROLD",
        "data": [
          0.0,
          0.0,
          0.0,
          61.9,
          61.92,
          62.0,
          64.12
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
            "x": 43035074.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $43,035,074 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 81750.0,
            "y": 43.19,
            "r": 8,
            "label": "1nu: $81,750 FDV, 43.2% concentration (low risk)"
          },
          {
            "x": 704928.0,
            "y": 33.06,
            "r": 8,
            "label": "DREAM: $704,928 FDV, 33.1% concentration (low risk)"
          },
          {
            "x": 410344.0,
            "y": 30.6,
            "r": 8,
            "label": "RAGEGUY: $410,344 FDV, 30.6% concentration (low risk)"
          },
          {
            "x": 185990.0,
            "y": 54.1,
            "r": 8,
            "label": "AI4: $185,990 FDV, 54.1% concentration (low risk)"
          },
          {
            "x": 29171.0,
            "y": 57.27,
            "r": 8,
            "label": "SHITTER: $29,171 FDV, 57.3% concentration (low risk)"
          },
          {
            "x": 336669.0,
            "y": 37.25,
            "r": 8,
            "label": "FARTLESS: $336,669 FDV, 37.2% concentration (low risk)"
          },
          {
            "x": 852328.0,
            "y": 26.46,
            "r": 8,
            "label": "XBT: $852,328 FDV, 26.5% concentration (low risk)"
          },
          {
            "x": 520927.0,
            "y": 34.34,
            "r": 8,
            "label": "ELIZABETH: $520,927 FDV, 34.3% concentration (low risk)"
          },
          {
            "x": 20617.0,
            "y": 27.46,
            "r": 8,
            "label": "FLY: $20,617 FDV, 27.5% concentration (low risk)"
          },
          {
            "x": 119749.0,
            "y": 46.82,
            "r": 8,
            "label": "USEFUL: $119,749 FDV, 46.8% concentration (low risk)"
          },
          {
            "x": 106480.0,
            "y": 42.33,
            "r": 8,
            "label": "USDUT: $106,480 FDV, 42.3% concentration (low risk)"
          },
          {
            "x": 144819.0,
            "y": 46.49,
            "r": 8,
            "label": "gib: $144,819 FDV, 46.5% concentration (low risk)"
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
            "x": 3205328.0,
            "y": 64.12,
            "r": 8,
            "label": "HAROLD: $3,205,328 FDV, 64.1% concentration (medium risk)"
          },
          {
            "x": 62742.0,
            "y": 61.32,
            "r": 8,
            "label": "RUECAT: $62,742 FDV, 61.3% concentration (medium risk)"
          },
          {
            "x": 14334.0,
            "y": 65.98,
            "r": 8,
            "label": "$CrepSol: $14,334 FDV, 66.0% concentration (medium risk)"
          },
          {
            "x": 5715.0,
            "y": 76.93,
            "r": 8,
            "label": "APOLLO: $5,715 FDV, 76.9% concentration (medium risk)"
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
            "x": 7801.0,
            "y": 82.11,
            "r": 8,
            "label": "1: $7,801 FDV, 82.1% concentration (high risk)"
          },
          {
            "x": 8679.0,
            "y": 81.19,
            "r": 8,
            "label": "1Bull: $8,679 FDV, 81.2% concentration (high risk)"
          },
          {
            "x": 10799.0,
            "y": 90.05,
            "r": 8,
            "label": "AUSBAGWORK: $10,799 FDV, 90.0% concentration (high risk)"
          },
          {
            "x": 4951.0,
            "y": 95.6,
            "r": 8,
            "label": "pibble: $4,951 FDV, 95.6% concentration (high risk)"
          },
          {
            "x": 4806.0,
            "y": 92.24,
            "r": 8,
            "label": "FARTWORM: $4,806 FDV, 92.2% concentration (high risk)"
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
            "x": 12556284.0,
            "y": 96.8,
            "r": 8,
            "label": "SOL: $12,556,284 FDV, 96.8% concentration (extreme risk)"
          },
          {
            "x": 4306.0,
            "y": 95.91,
            "r": 8,
            "label": "RWA: $4,306 FDV, 95.9% concentration (extreme risk)"
          },
          {
            "x": 5363.0,
            "y": 95.17,
            "r": 8,
            "label": "1: $5,363 FDV, 95.2% concentration (extreme risk)"
          },
          {
            "x": 3384.0,
            "y": 97.36,
            "r": 8,
            "label": "Streamless: $3,384 FDV, 97.4% concentration (extreme risk)"
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
| 1 | XBT | XBT | 26.46% | 🟢 low | $24.96 | $394.45 |
| 2 | FLY | Nexa | 27.46% | 🟢 low | $1.50 | $2.42K |
| 3 | RAGEGUY | Rage Guy | 30.60% | 🟢 low | $11.98K | $87.98K |
| 4 | DREAM | Dreamsync | 33.06% | 🟢 low | $13.05K | $103.13K |
| 5 | ELIZABETH | Just Elizabeth Cat | 34.34% | 🟢 low | $16.23 | $35.38 |
| 6 | FARTLESS | FARTLESS COIN | 37.25% | 🟢 low | $279.41 | $2.42K |
| 7 | USDUT | unstable tether | 42.33% | 🟢 low | $0.19 | $36.44 |
| 8 | 1nu | 1nu | 43.19% | 🟢 low | $15.53K | $38.70K |
| 9 | gib | gib | 46.49% | 🟢 low | $0.18 | $26.67 |
| 10 | USEFUL | USEFUL COIN | 46.82% | 🟢 low | $0.25 | $36.67 |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | Streamless | Streamless coin | 97.36% | 🔴 extreme | $4.20 | $6.47K |
| 2 | SOL | Solana | 96.80% | 🔴 extreme | $505.66 | $13.53K |
| 3 | RWA | Real World Asses | 95.91% | 🔴 extreme | $76.09 | $7.37K |
| 4 | pibble | pibble | 95.60% | 🟠 high | $53.73 | $7.78K |
| 5 | 1 | 1 pill can change your li | 95.17% | 🔴 extreme | $26.81 | $8.72K |
| 6 | FARTWORM | FARTWORM | 92.24% | 🟠 high | $14.69 | $7.70K |
| 7 | AUSBAGWORK | AUSSIE BAG WORKERS | 90.05% | 🟠 high | $141.25 | $13.37K |
| 8 | 1 | 1 pill can change your li | 82.11% | 🟠 high | $3.34K | $9.42K |
| 9 | 1Bull | One bull run to change yo | 81.19% | 🟠 high | $367.17 | $10.22K |
| 10 | APOLLO | Apollo AI | 76.93% | 🟡 medium | $0.36 | $4.28K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 27
**Combined 24h Volume**: $152.79M
**Combined Liquidity**: $45.81M

**Concentration Risk Distribution**:
- 🟢 Low: 13 tokens
- 🟡 High: 5 tokens
- 🟢 Medium: 4 tokens
- 🔴 Extreme: 4 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $152.72M | $43.59M | 🟢 unknown |
| 2 | LION | Loaded Lions | $16.05K | $1.31M | 🟢 low |
| 3 | 1nu | 1nu | $15.53K | $38.70K | 🟢 low |
| 4 | DREAM | Dreamsync | $13.05K | $103.13K | 🟢 low |
| 5 | RAGEGUY | Rage Guy | $11.98K | $87.98K | 🟢 low |
| 6 | HAROLD | Harold | $4.26K | $442.10K | 🟢 medium |
| 7 | 1 | 1 pill can change your life | $3.34K | $9.42K | 🟡 high |
| 8 | AI4 | AI⁴ | $3.30K | $74.48K | 🟢 low |
| 9 | RUECAT | Rue Cat | $856.75 | $31.90K | 🟢 medium |
| 10 | SOL | Solana | $505.66 | $13.53K | 🔴 extreme |

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

**Total Historical Records**: 501
**Unique Tokens Tracked**: 101
**Date Range**: 2025-10-01 to 2025-11-08

**Master Aggregations**: 101 tokens
**Performance Metrics**: 501 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 501 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 101 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 501 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 27 |
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
