# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-11-09 19:05 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **36 tokens tracked** | 
💰 **$138.67M 24h volume** | 
💧 **$47.14M liquidity** | 
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
          4,
          6,
          11,
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
          -53.68705035971223,
          -53.68705035971223
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
      "DREAM",
      "1nu",
      "1",
      "LION",
      "RAGEGUY",
      "HAROLD",
      "AI4",
      "SOL",
      "AUSBAGWORK",
      "pibble"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          123125.95,
          12750.06,
          11393.15,
          8450.43,
          8210.97,
          5027.51,
          2400.35,
          878.31,
          355.28,
          223.95
        ],
        "backgroundColor": [
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#22c55e",
          "#ef4444",
          "#f97316",
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
      "2025-11-09"
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
          33.24
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
          40.64
        ],
        "borderColor": "#ef4444",
        "backgroundColor": "#ef444420",
        "tension": 0.3,
        "fill": false
      },
      {
        "label": "1",
        "data": [
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          97.36,
          90.03,
          89.98,
          97.49,
          97.39,
          90.65,
          73.63,
          95.17
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
        "label": "RAGEGUY",
        "data": [
          0.0,
          0.0,
          0.0,
          25.99,
          26.1,
          25.76,
          30.58
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
            "x": 700874.0,
            "y": 33.24,
            "r": 8,
            "label": "DREAM: $700,874 FDV, 33.2% concentration (low risk)"
          },
          {
            "x": 91945.0,
            "y": 40.64,
            "r": 8,
            "label": "1nu: $91,945 FDV, 40.6% concentration (low risk)"
          },
          {
            "x": 43793202.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $43,793,202 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 427081.0,
            "y": 30.58,
            "r": 8,
            "label": "RAGEGUY: $427,081 FDV, 30.6% concentration (low risk)"
          },
          {
            "x": 188454.0,
            "y": 54.26,
            "r": 8,
            "label": "AI4: $188,454 FDV, 54.3% concentration (low risk)"
          },
          {
            "x": 379131.0,
            "y": 36.25,
            "r": 8,
            "label": "FARTLESS: $379,131 FDV, 36.2% concentration (low risk)"
          },
          {
            "x": 29136.0,
            "y": 57.3,
            "r": 8,
            "label": "SHITTER: $29,136 FDV, 57.3% concentration (low risk)"
          },
          {
            "x": 655610.0,
            "y": 30.85,
            "r": 8,
            "label": "ELIZABETH: $655,610 FDV, 30.9% concentration (low risk)"
          },
          {
            "x": 913491.0,
            "y": 26.05,
            "r": 8,
            "label": "XBT: $913,491 FDV, 26.1% concentration (low risk)"
          },
          {
            "x": 83909.0,
            "y": 43.47,
            "r": 8,
            "label": "YAO: $83,909 FDV, 43.5% concentration (low risk)"
          },
          {
            "x": 19612.0,
            "y": 27.46,
            "r": 8,
            "label": "FLY: $19,612 FDV, 27.5% concentration (low risk)"
          },
          {
            "x": 161557.0,
            "y": 45.64,
            "r": 8,
            "label": "gib: $161,557 FDV, 45.6% concentration (low risk)"
          },
          {
            "x": 109167.0,
            "y": 47.66,
            "r": 8,
            "label": "USEFUL: $109,167 FDV, 47.7% concentration (low risk)"
          },
          {
            "x": 104284.0,
            "y": 41.78,
            "r": 8,
            "label": "USDUT: $104,284 FDV, 41.8% concentration (low risk)"
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
            "x": 11118.0,
            "y": 73.63,
            "r": 8,
            "label": "1: $11,118 FDV, 73.6% concentration (medium risk)"
          },
          {
            "x": 3206977.0,
            "y": 64.21,
            "r": 8,
            "label": "HAROLD: $3,206,977 FDV, 64.2% concentration (medium risk)"
          },
          {
            "x": 64142.0,
            "y": 61.29,
            "r": 8,
            "label": "RUECAT: $64,142 FDV, 61.3% concentration (medium risk)"
          },
          {
            "x": 14150.0,
            "y": 66.25,
            "r": 8,
            "label": "$CrepSol: $14,150 FDV, 66.2% concentration (medium risk)"
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
            "x": 10596.0,
            "y": 91.05,
            "r": 8,
            "label": "AUSBAGWORK: $10,596 FDV, 91.0% concentration (high risk)"
          },
          {
            "x": 8476.0,
            "y": 82.24,
            "r": 8,
            "label": "1Bull: $8,476 FDV, 82.2% concentration (high risk)"
          },
          {
            "x": 5474.0,
            "y": 77.78,
            "r": 8,
            "label": "APOLLO: $5,474 FDV, 77.8% concentration (high risk)"
          },
          {
            "x": 6301.0,
            "y": 90.31,
            "r": 8,
            "label": "DARE: $6,301 FDV, 90.3% concentration (high risk)"
          },
          {
            "x": 4942.0,
            "y": 92.26,
            "r": 8,
            "label": "FARTWORM: $4,942 FDV, 92.3% concentration (high risk)"
          },
          {
            "x": 6995.0,
            "y": 92.88,
            "r": 8,
            "label": "IDIOT: $6,995 FDV, 92.9% concentration (high risk)"
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
            "x": 12623495.0,
            "y": 96.8,
            "r": 8,
            "label": "SOL: $12,623,495 FDV, 96.8% concentration (extreme risk)"
          },
          {
            "x": 4396.0,
            "y": 96.49,
            "r": 8,
            "label": "pibble: $4,396 FDV, 96.5% concentration (extreme risk)"
          },
          {
            "x": 3102.0,
            "y": 99.6,
            "r": 8,
            "label": "ORE: $3,102 FDV, 99.6% concentration (extreme risk)"
          },
          {
            "x": 3657.0,
            "y": 96.9,
            "r": 8,
            "label": "7: $3,657 FDV, 96.9% concentration (extreme risk)"
          },
          {
            "x": 3223.0,
            "y": 98.05,
            "r": 8,
            "label": "BLUB: $3,223 FDV, 98.0% concentration (extreme risk)"
          },
          {
            "x": 3518.0,
            "y": 97.9,
            "r": 8,
            "label": "Bagwork: $3,518 FDV, 97.9% concentration (extreme risk)"
          },
          {
            "x": 4450.63,
            "y": 99.92,
            "r": 8,
            "label": "Hamu: $4,451 FDV, 99.9% concentration (extreme risk)"
          },
          {
            "x": 8593.0,
            "y": 94.21,
            "r": 8,
            "label": "MOCHI: $8,593 FDV, 94.2% concentration (extreme risk)"
          },
          {
            "x": 3384.0,
            "y": 97.36,
            "r": 8,
            "label": "Streamless: $3,384 FDV, 97.4% concentration (extreme risk)"
          },
          {
            "x": 3331.0,
            "y": 98.98,
            "r": 8,
            "label": "1% Club: $3,331 FDV, 99.0% concentration (extreme risk)"
          },
          {
            "x": 5147.0,
            "y": 95.17,
            "r": 8,
            "label": "1: $5,147 FDV, 95.2% concentration (extreme risk)"
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
| 1 | XBT | XBT | 26.05% | 🟢 low | $6.39 | $415.31 |
| 2 | FLY | Nexa | 27.46% | 🟢 low | $1.02 | $5.98K |
| 3 | RAGEGUY | Rage Guy | 30.58% | 🟢 low | $8.21K | $90.84K |
| 4 | ELIZABETH | Just Elizabeth Cat | 30.85% | 🟢 low | $13.45 | $39.69 |
| 5 | DREAM | Dreamsync | 33.24% | 🟢 low | $123.13K | $104.77K |
| 6 | FARTLESS | FARTLESS COIN | 36.25% | 🟢 low | $222.75 | $2.57K |
| 7 | 1nu | 1nu | 40.64% | 🟢 low | $12.75K | $41.07K |
| 8 | USDUT | unstable tether | 41.78% | 🟢 low | $0.18 | $36.23 |
| 9 | YAO | YAO MING | 43.47% | 🟢 low | $2.85 | $568.00 |
| 10 | gib | gib | 45.64% | 🟢 low | $0.81 | $28.17 |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | Hamu | Hamu | 99.92% | 🔴 extreme | $8.86 | $0.00 |
| 2 | ORE | Ore Labs | 99.60% | 🔴 extreme | $131.76 | $5.89K |
| 3 | 1% Club | The 1% Club | 98.98% | 🔴 extreme | $0.21 | $6.07K |
| 4 | BLUB | Blub | 98.05% | 🔴 extreme | $18.22 | $6.21K |
| 5 | Bagwork | African Bagwork | 97.90% | 🔴 extreme | $9.30 | $6.72K |
| 6 | Streamless | Streamless coin | 97.36% | 🔴 extreme | $4.05 | $6.47K |
| 7 | 7 | 7 Coin | 96.90% | 🔴 extreme | $28.81 | $6.61K |
| 8 | SOL | Solana | 96.80% | 🔴 extreme | $878.31 | $13.63K |
| 9 | pibble | pibble | 96.49% | 🔴 extreme | $223.95 | $7.34K |
| 10 | 1 | 1 pill can change your li | 95.17% | 🔴 extreme | $0.16 | $8.39K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 36
**Combined 24h Volume**: $138.67M
**Combined Liquidity**: $47.14M

**Concentration Risk Distribution**:
- 🟢 Low: 14 tokens
- 🔴 Extreme: 11 tokens
- 🟡 High: 6 tokens
- 🟢 Medium: 4 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $138.49M | $44.82M | 🟢 unknown |
| 2 | DREAM | Dreamsync | $123.13K | $104.77K | 🟢 low |
| 3 | 1nu | 1nu | $12.75K | $41.07K | 🟢 low |
| 4 | 1 | 1 pill can change your life | $11.39K | $11.37K | 🟢 medium |
| 5 | LION | Loaded Lions | $8.45K | $1.34M | 🟢 low |
| 6 | RAGEGUY | Rage Guy | $8.21K | $90.84K | 🟢 low |
| 7 | HAROLD | Harold | $5.03K | $449.27K | 🟢 medium |
| 8 | AI4 | AI⁴ | $2.40K | $75.88K | 🟢 low |
| 9 | SOL | Solana | $878.31 | $13.63K | 🔴 extreme |
| 10 | AUSBAGWORK | AUSSIE BAG WORKERS | $355.28 | $13.39K | 🟡 high |

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

**Total Historical Records**: 510
**Unique Tokens Tracked**: 101
**Date Range**: 2025-10-01 to 2025-11-09

**Master Aggregations**: 101 tokens
**Performance Metrics**: 508 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 510 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 101 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 508 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 36 |
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
