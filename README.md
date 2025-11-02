# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-11-02 23:13 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **29 tokens tracked** | 
💰 **$136.39M 24h volume** | 
💧 **$69.86M liquidity** | 
🟢 **12 low-risk tokens**

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
          12,
          3,
          4,
          9,
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
          16.479796911360282,
          16.479796911360282
        ],
        "backgroundColor": [
          "#22c55e",
          "#22c55e"
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
      "AI4",
      "DREAM",
      "RAGEGUY",
      "1nu",
      "LION",
      "HAROLD",
      "1",
      "Hosico",
      "RUECAT",
      "SHITTER"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          58269.23,
          19164.34,
          16433.66,
          11621.28,
          9143.55,
          4660.01,
          583.43,
          551.14,
          529.93,
          336.24
        ],
        "backgroundColor": [
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#ef4444",
          "#ef4444",
          "#22c55e",
          "#eab308"
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
      "2025-11-02"
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
          51.6
        ],
        "borderColor": "#3b82f6",
        "backgroundColor": "#3b82f620",
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
          33.47
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
          29.49
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
          44.55
        ],
        "borderColor": "#eab308",
        "backgroundColor": "#eab30820",
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
            "x": 254385.0,
            "y": 51.6,
            "r": 8,
            "label": "AI4: $254,385 FDV, 51.6% concentration (low risk)"
          },
          {
            "x": 740674.0,
            "y": 33.47,
            "r": 8,
            "label": "DREAM: $740,674 FDV, 33.5% concentration (low risk)"
          },
          {
            "x": 598174.0,
            "y": 29.49,
            "r": 8,
            "label": "RAGEGUY: $598,174 FDV, 29.5% concentration (low risk)"
          },
          {
            "x": 72509.0,
            "y": 44.55,
            "r": 8,
            "label": "1nu: $72,509 FDV, 44.5% concentration (low risk)"
          },
          {
            "x": 52664120.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $52,664,120 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 69433.0,
            "y": 59.22,
            "r": 8,
            "label": "RUECAT: $69,433 FDV, 59.2% concentration (low risk)"
          },
          {
            "x": 437153.0,
            "y": 37.08,
            "r": 8,
            "label": "FARTLESS: $437,153 FDV, 37.1% concentration (low risk)"
          },
          {
            "x": 1252463.0,
            "y": 24.31,
            "r": 8,
            "label": "XBT: $1,252,463 FDV, 24.3% concentration (low risk)"
          },
          {
            "x": 127020.0,
            "y": 41.0,
            "r": 8,
            "label": "YAO: $127,020 FDV, 41.0% concentration (low risk)"
          },
          {
            "x": 178144.0,
            "y": 45.66,
            "r": 8,
            "label": "gib: $178,144 FDV, 45.7% concentration (low risk)"
          },
          {
            "x": 426260.0,
            "y": 35.65,
            "r": 8,
            "label": "ELIZABETH: $426,260 FDV, 35.6% concentration (low risk)"
          },
          {
            "x": 120671.0,
            "y": 44.8,
            "r": 8,
            "label": "USEFUL: $120,671 FDV, 44.8% concentration (low risk)"
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
            "x": 3288869.0,
            "y": 63.74,
            "r": 8,
            "label": "HAROLD: $3,288,869 FDV, 63.7% concentration (medium risk)"
          },
          {
            "x": 22680.0,
            "y": 63.51,
            "r": 8,
            "label": "SHITTER: $22,680 FDV, 63.5% concentration (medium risk)"
          },
          {
            "x": 17381.0,
            "y": 64.53,
            "r": 8,
            "label": "$CrepSol: $17,381 FDV, 64.5% concentration (medium risk)"
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
            "x": 12621.0,
            "y": 89.8,
            "r": 8,
            "label": "AUSBAGWORK: $12,621 FDV, 89.8% concentration (high risk)"
          },
          {
            "x": 9505.0,
            "y": 80.76,
            "r": 8,
            "label": "1Bull: $9,505 FDV, 80.8% concentration (high risk)"
          },
          {
            "x": 7384.0,
            "y": 90.18,
            "r": 8,
            "label": "DARE: $7,384 FDV, 90.2% concentration (high risk)"
          },
          {
            "x": 5731.0,
            "y": 92.01,
            "r": 8,
            "label": "FARTWORM: $5,731 FDV, 92.0% concentration (high risk)"
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
            "x": 4726.0,
            "y": 97.23,
            "r": 8,
            "label": "1: $4,726 FDV, 97.2% concentration (extreme risk)"
          },
          {
            "x": 3985.0,
            "y": 98.03,
            "r": 8,
            "label": "Hosico: $3,985 FDV, 98.0% concentration (extreme risk)"
          },
          {
            "x": 16442977.0,
            "y": 96.8,
            "r": 8,
            "label": "SOL: $16,442,977 FDV, 96.8% concentration (extreme risk)"
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
            "x": 5502.0,
            "y": 95.92,
            "r": 8,
            "label": "1: $5,502 FDV, 95.9% concentration (extreme risk)"
          },
          {
            "x": 4103.0,
            "y": 97.61,
            "r": 8,
            "label": "Bagwork: $4,103 FDV, 97.6% concentration (extreme risk)"
          },
          {
            "x": 4454.0,
            "y": 96.34,
            "r": 8,
            "label": "pibble: $4,454 FDV, 96.3% concentration (extreme risk)"
          },
          {
            "x": 9798.0,
            "y": 93.86,
            "r": 8,
            "label": "MOCHI: $9,798 FDV, 93.9% concentration (extreme risk)"
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
| 1 | XBT | XBT | 24.31% | 🟢 low | $25.57 | $515.55 |
| 2 | RAGEGUY | Rage Guy | 29.49% | 🟢 low | $16.43K | $114.55K |
| 3 | DREAM | Dreamsync | 33.47% | 🟢 low | $19.16K | $114.40K |
| 4 | ELIZABETH | Just Elizabeth Cat | 35.65% | 🟢 low | $0.56 | $32.01 |
| 5 | FARTLESS | FARTLESS COIN | 37.08% | 🟢 low | $260.28 | $2.75K |
| 6 | YAO | YAO MING | 41.00% | 🟢 low | $2.70 | $799.19 |
| 7 | 1nu | 1nu | 44.55% | 🟢 low | $11.62K | $35.71K |
| 8 | USEFUL | USEFUL COIN | 44.80% | 🟢 low | $0.23 | $40.74 |
| 9 | gib | gib | 45.66% | 🟢 low | $0.59 | $29.58 |
| 10 | AI4 | AI⁴ | 51.60% | 🟢 low | $58.27K | $94.20K |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | JIFFPOM | Jiffpom | 98.78% | 🔴 extreme | $9.17 | $11.59K |
| 2 | Hosico | Hosico Cat | 98.03% | 🔴 extreme | $551.14 | $7.21K |
| 3 | Bagwork | African Bagwork | 97.61% | 🔴 extreme | $2.51 | $7.82K |
| 4 | 1 | 1 pill can change your li | 97.23% | 🔴 extreme | $583.43 | $7.88K |
| 5 | SOL | Solana | 96.80% | 🔴 extreme | $175.51 | $16.54K |
| 6 | pibble | pibble | 96.34% | 🔴 extreme | $2.51 | $7.38K |
| 7 | RWA | Real World Asses | 96.24% | 🔴 extreme | $17.08 | $7.25K |
| 8 | 1 | 1 pill can change your li | 95.92% | 🔴 extreme | $4.94 | $9.43K |
| 9 | MOCHI | MOCHI CULT | 93.86% | 🔴 extreme | $1.76 | $17.10K |
| 10 | FARTWORM | FARTWORM | 92.01% | 🟠 high | $3.70 | $9.15K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 29
**Combined 24h Volume**: $136.39M
**Combined Liquidity**: $69.86M

**Concentration Risk Distribution**:
- 🟢 Low: 12 tokens
- 🔴 Extreme: 9 tokens
- 🟡 High: 4 tokens
- 🟢 Medium: 3 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $136.27M | $67.23M | 🟢 unknown |
| 2 | AI4 | AI⁴ | $58.27K | $94.20K | 🟢 low |
| 3 | DREAM | Dreamsync | $19.16K | $114.40K | 🟢 low |
| 4 | RAGEGUY | Rage Guy | $16.43K | $114.55K | 🟢 low |
| 5 | 1nu | 1nu | $11.62K | $35.71K | 🟢 low |
| 6 | LION | Loaded Lions | $9.14K | $1.57M | 🟢 low |
| 7 | HAROLD | Harold | $4.66K | $484.64K | 🟢 medium |
| 8 | 1 | 1 pill can change your life | $583.43 | $7.88K | 🔴 extreme |
| 9 | Hosico | Hosico Cat | $551.14 | $7.21K | 🔴 extreme |
| 10 | RUECAT | Rue Cat | $529.93 | $36.19K | 🟢 low |

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

**Total Historical Records**: 503
**Unique Tokens Tracked**: 101
**Date Range**: 2025-10-01 to 2025-11-02

**Master Aggregations**: 101 tokens
**Performance Metrics**: 503 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 503 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 101 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 503 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 29 |
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
