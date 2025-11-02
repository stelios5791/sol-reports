# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-11-02 14:29 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **28 tokens tracked** | 
💰 **$126.16M 24h volume** | 
💧 **$69.37M liquidity** | 
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
          3,
          4,
          7,
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
          0.21842009464870865,
          0.21842009464870865
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
      "1nu",
      "RAGEGUY",
      "LION",
      "HAROLD",
      "Hosico",
      "SOL",
      "1",
      "RUECAT"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          53642.77,
          25621.27,
          21997.62,
          10588.65,
          7216.92,
          2293.59,
          1498.24,
          1085.75,
          804.13,
          602.09
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
          "#f97316",
          "#22c55e"
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
          51.61
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
          33.41
        ],
        "borderColor": "#ef4444",
        "backgroundColor": "#ef444420",
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
          45.68
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
          29.82
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
            "x": 251418.0,
            "y": 51.61,
            "r": 8,
            "label": "AI4: $251,418 FDV, 51.6% concentration (low risk)"
          },
          {
            "x": 747352.0,
            "y": 33.41,
            "r": 8,
            "label": "DREAM: $747,352 FDV, 33.4% concentration (low risk)"
          },
          {
            "x": 66314.0,
            "y": 45.68,
            "r": 8,
            "label": "1nu: $66,314 FDV, 45.7% concentration (low risk)"
          },
          {
            "x": 559659.0,
            "y": 29.82,
            "r": 8,
            "label": "RAGEGUY: $559,659 FDV, 29.8% concentration (low risk)"
          },
          {
            "x": 52602724.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $52,602,724 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 71255.0,
            "y": 59.22,
            "r": 8,
            "label": "RUECAT: $71,255 FDV, 59.2% concentration (low risk)"
          },
          {
            "x": 446206.0,
            "y": 36.68,
            "r": 8,
            "label": "FARTLESS: $446,206 FDV, 36.7% concentration (low risk)"
          },
          {
            "x": 1146693.0,
            "y": 24.95,
            "r": 8,
            "label": "XBT: $1,146,693 FDV, 24.9% concentration (low risk)"
          },
          {
            "x": 410884.0,
            "y": 35.41,
            "r": 8,
            "label": "ELIZABETH: $410,884 FDV, 35.4% concentration (low risk)"
          },
          {
            "x": 128086.0,
            "y": 40.69,
            "r": 8,
            "label": "YAO: $128,086 FDV, 40.7% concentration (low risk)"
          },
          {
            "x": 178144.0,
            "y": 45.33,
            "r": 8,
            "label": "gib: $178,144 FDV, 45.3% concentration (low risk)"
          },
          {
            "x": 144968.0,
            "y": 39.76,
            "r": 8,
            "label": "USDUT: $144,968 FDV, 39.8% concentration (low risk)"
          },
          {
            "x": 120671.0,
            "y": 44.73,
            "r": 8,
            "label": "USEFUL: $120,671 FDV, 44.7% concentration (low risk)"
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
            "x": 3280871.0,
            "y": 63.8,
            "r": 8,
            "label": "HAROLD: $3,280,871 FDV, 63.8% concentration (medium risk)"
          },
          {
            "x": 22653.0,
            "y": 63.54,
            "r": 8,
            "label": "SHITTER: $22,653 FDV, 63.5% concentration (medium risk)"
          },
          {
            "x": 17912.0,
            "y": 64.4,
            "r": 8,
            "label": "$CrepSol: $17,912 FDV, 64.4% concentration (medium risk)"
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
            "x": 5494.0,
            "y": 95.27,
            "r": 8,
            "label": "1: $5,494 FDV, 95.3% concentration (high risk)"
          },
          {
            "x": 12603.0,
            "y": 89.79,
            "r": 8,
            "label": "AUSBAGWORK: $12,603 FDV, 89.8% concentration (high risk)"
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
            "x": 4402.0,
            "y": 97.84,
            "r": 8,
            "label": "Hosico: $4,402 FDV, 97.8% concentration (extreme risk)"
          },
          {
            "x": 16382047.0,
            "y": 96.8,
            "r": 8,
            "label": "SOL: $16,382,047 FDV, 96.8% concentration (extreme risk)"
          },
          {
            "x": 5502.0,
            "y": 95.92,
            "r": 8,
            "label": "1: $5,502 FDV, 95.9% concentration (extreme risk)"
          },
          {
            "x": 4454.0,
            "y": 96.34,
            "r": 8,
            "label": "pibble: $4,454 FDV, 96.3% concentration (extreme risk)"
          },
          {
            "x": 3987.0,
            "y": 98.04,
            "r": 8,
            "label": "viewer: $3,987 FDV, 98.0% concentration (extreme risk)"
          },
          {
            "x": 3913.0,
            "y": 99.5,
            "r": 8,
            "label": "MoneyBear: $3,913 FDV, 99.5% concentration (extreme risk)"
          },
          {
            "x": 5517.0,
            "y": 93.86,
            "r": 8,
            "label": "MOCHI: $5,517 FDV, 93.9% concentration (extreme risk)"
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
| 1 | XBT | XBT | 24.95% | 🟢 low | $30.28 | $494.03 |
| 2 | RAGEGUY | Rage Guy | 29.82% | 🟢 low | $10.59K | $110.90K |
| 3 | DREAM | Dreamsync | 33.41% | 🟢 low | $25.62K | $114.51K |
| 4 | ELIZABETH | Just Elizabeth Cat | 35.41% | 🟢 low | $2.52 | $31.42 |
| 5 | FARTLESS | FARTLESS COIN | 36.68% | 🟢 low | $266.09 | $2.78K |
| 6 | USDUT | unstable tether | 39.76% | 🟢 low | $0.39 | $42.90 |
| 7 | YAO | YAO MING | 40.69% | 🟢 low | $1.94 | $811.12 |
| 8 | USEFUL | USEFUL COIN | 44.73% | 🟢 low | $0.23 | $40.74 |
| 9 | gib | gib | 45.33% | 🟢 low | $0.59 | $29.58 |
| 10 | 1nu | 1nu | 45.68% | 🟢 low | $22.00K | $34.14K |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | MoneyBear | The Money Bears | 99.50% | 🔴 extreme | $4.06 | $7.76K |
| 2 | viewer | in a streamers world | 98.04% | 🔴 extreme | $4.46 | $7.65K |
| 3 | Hosico | Hosico Cat | 97.84% | 🔴 extreme | $1.50K | $7.60K |
| 4 | SOL | Solana | 96.80% | 🔴 extreme | $1.09K | $16.44K |
| 5 | pibble | pibble | 96.34% | 🔴 extreme | $6.80 | $7.38K |
| 6 | 1 | 1 pill can change your li | 95.92% | 🔴 extreme | $546.48 | $9.43K |
| 7 | 1 | 1 pill can change your li | 95.27% | 🟠 high | $804.13 | $8.54K |
| 8 | MOCHI | MOCHI CULT | 93.86% | 🔴 extreme | $1.49 | $0.97 |
| 9 | FARTWORM | FARTWORM | 92.01% | 🟠 high | $5.83 | $9.15K |
| 10 | DARE | DareCoin | 90.18% | 🟠 high | $35.20 | $11.34K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 28
**Combined 24h Volume**: $126.16M
**Combined Liquidity**: $69.37M

**Concentration Risk Distribution**:
- 🟢 Low: 13 tokens
- 🔴 Extreme: 7 tokens
- 🟡 High: 4 tokens
- 🟢 Medium: 3 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $126.03M | $66.79M | 🟢 unknown |
| 2 | AI4 | AI⁴ | $53.64K | $93.19K | 🟢 low |
| 3 | DREAM | Dreamsync | $25.62K | $114.51K | 🟢 low |
| 4 | 1nu | 1nu | $22.00K | $34.14K | 🟢 low |
| 5 | RAGEGUY | Rage Guy | $10.59K | $110.90K | 🟢 low |
| 6 | LION | Loaded Lions | $7.22K | $1.57M | 🟢 low |
| 7 | HAROLD | Harold | $2.29K | $484.81K | 🟢 medium |
| 8 | Hosico | Hosico Cat | $1.50K | $7.60K | 🔴 extreme |
| 9 | SOL | Solana | $1.09K | $16.44K | 🔴 extreme |
| 10 | 1 | 1 pill can change your life | $804.13 | $8.54K | 🟡 high |

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

**Total Historical Records**: 502
**Unique Tokens Tracked**: 101
**Date Range**: 2025-10-01 to 2025-11-02

**Master Aggregations**: 101 tokens
**Performance Metrics**: 502 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 502 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 101 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 502 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 28 |
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
