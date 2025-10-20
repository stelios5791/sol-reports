# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-10-20 17:46 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **40 tokens tracked** | 
💰 **$207.94M 24h volume** | 
💧 **$57.73M liquidity** | 
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
          7,
          16,
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
          41.11593871484106,
          41.11593871484106
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
      "DREAM",
      "AI4",
      "RAGEGUY",
      "LION",
      "1nu",
      "HAROLD",
      "FARTLESS",
      "$CrepSol",
      "DARE",
      "1"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          224590.45,
          83019.81,
          45030.49,
          20228.49,
          19181.82,
          6170.76,
          910.03,
          822.15,
          361.11,
          212.36
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
          47.83
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
          27.28
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
          43.81
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
            "x": 1514778.0,
            "y": 31.91,
            "r": 8,
            "label": "DREAM: $1,514,778 FDV, 31.9% concentration (low risk)"
          },
          {
            "x": 208484.0,
            "y": 47.83,
            "r": 8,
            "label": "AI4: $208,484 FDV, 47.8% concentration (low risk)"
          },
          {
            "x": 788002.0,
            "y": 27.28,
            "r": 8,
            "label": "RAGEGUY: $788,002 FDV, 27.3% concentration (low risk)"
          },
          {
            "x": 56184781.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $56,184,781 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 53620.0,
            "y": 43.81,
            "r": 8,
            "label": "1nu: $53,620 FDV, 43.8% concentration (low risk)"
          },
          {
            "x": 699674.0,
            "y": 34.82,
            "r": 8,
            "label": "FARTLESS: $699,674 FDV, 34.8% concentration (low risk)"
          },
          {
            "x": 33732.0,
            "y": 57.31,
            "r": 8,
            "label": "$CrepSol: $33,732 FDV, 57.3% concentration (low risk)"
          },
          {
            "x": 89379.0,
            "y": 54.45,
            "r": 8,
            "label": "RUECAT: $89,379 FDV, 54.5% concentration (low risk)"
          },
          {
            "x": 1403743.0,
            "y": 23.0,
            "r": 8,
            "label": "XBT: $1,403,743 FDV, 23.0% concentration (low risk)"
          },
          {
            "x": 18829748.0,
            "y": 39.75,
            "r": 8,
            "label": "AI20X: $18,829,748 FDV, 39.8% concentration (low risk)"
          },
          {
            "x": 647502.0,
            "y": 31.62,
            "r": 8,
            "label": "ELIZABETH: $647,502 FDV, 31.6% concentration (low risk)"
          },
          {
            "x": 18301.0,
            "y": 30.33,
            "r": 8,
            "label": "FLY: $18,301 FDV, 30.3% concentration (low risk)"
          },
          {
            "x": 105149.0,
            "y": 44.31,
            "r": 8,
            "label": "YAO: $105,149 FDV, 44.3% concentration (low risk)"
          },
          {
            "x": 129116.0,
            "y": 44.42,
            "r": 8,
            "label": "USEFUL: $129,116 FDV, 44.4% concentration (low risk)"
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
            "x": 3021838.0,
            "y": 63.57,
            "r": 8,
            "label": "HAROLD: $3,021,838 FDV, 63.6% concentration (medium risk)"
          },
          {
            "x": 22288.0,
            "y": 64.81,
            "r": 8,
            "label": "SHITTER: $22,288 FDV, 64.8% concentration (medium risk)"
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
            "x": 8984.0,
            "y": 88.86,
            "r": 8,
            "label": "DARE: $8,984 FDV, 88.9% concentration (high risk)"
          },
          {
            "x": 6344.0,
            "y": 90.04,
            "r": 8,
            "label": "FARTWORM: $6,344 FDV, 90.0% concentration (high risk)"
          },
          {
            "x": 9685.0,
            "y": 79.44,
            "r": 8,
            "label": "1Bull: $9,685 FDV, 79.4% concentration (high risk)"
          },
          {
            "x": 14075.0,
            "y": 88.02,
            "r": 8,
            "label": "AUSBAGWORK: $14,075 FDV, 88.0% concentration (high risk)"
          },
          {
            "x": 9713.0,
            "y": 89.39,
            "r": 8,
            "label": "IDIOT: $9,713 FDV, 89.4% concentration (high risk)"
          },
          {
            "x": 5386.0,
            "y": 90.44,
            "r": 8,
            "label": "RWA: $5,386 FDV, 90.4% concentration (high risk)"
          },
          {
            "x": 10699.0,
            "y": 92.63,
            "r": 8,
            "label": "MOCHI: $10,699 FDV, 92.6% concentration (high risk)"
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
            "x": 4373.0,
            "y": 97.66,
            "r": 8,
            "label": "1: $4,373 FDV, 97.7% concentration (extreme risk)"
          },
          {
            "x": 11758353.0,
            "y": 96.74,
            "r": 8,
            "label": "SOL: $11,758,353 FDV, 96.7% concentration (extreme risk)"
          },
          {
            "x": 4008.0,
            "y": 98.8,
            "r": 8,
            "label": "19: $4,008 FDV, 98.8% concentration (extreme risk)"
          },
          {
            "x": 5996.0,
            "y": 95.48,
            "r": 8,
            "label": "7: $5,996 FDV, 95.5% concentration (extreme risk)"
          },
          {
            "x": 4547.0,
            "y": 95.39,
            "r": 8,
            "label": "pibble: $4,547 FDV, 95.4% concentration (extreme risk)"
          },
          {
            "x": 6167.0,
            "y": 93.91,
            "r": 8,
            "label": "1: $6,167 FDV, 93.9% concentration (extreme risk)"
          },
          {
            "x": 3598.0,
            "y": 99.4,
            "r": 8,
            "label": "ORE: $3,598 FDV, 99.4% concentration (extreme risk)"
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
| 1 | XBT | XBT | 23.00% | 🟢 low | $149.02 | $554.73 |
| 2 | RAGEGUY | Rage Guy | 27.28% | 🟢 low | $45.03K | $131.26K |
| 3 | FLY | Nexa | 30.33% | 🟢 low | $7.78 | $2.49K |
| 4 | ELIZABETH | Just Elizabeth Cat | 31.62% | 🟢 low | $23.65 | $39.09 |
| 5 | DREAM | Dreamsync | 31.91% | 🟢 low | $224.59K | $163.34K |
| 6 | FARTLESS | FARTLESS COIN | 34.82% | 🟢 low | $910.03 | $3.45K |
| 7 | AI20X | Ai20x.ai | 39.75% | 🟢 low | $42.10 | $2.24M |
| 8 | 1nu | 1nu | 43.81% | 🟢 low | $19.18K | $30.17K |
| 9 | YAO | YAO MING | 44.31% | 🟢 low | $5.19 | $723.84 |
| 10 | USEFUL | USEFUL COIN | 44.42% | 🟢 low | $1.05 | $55.49 |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | LOW | lowcut | 99.97% | 🔴 extreme | $0.00 | $0.00 |
| 2 | 1cat | 1 cat can change your lif | 99.88% | 🔴 extreme | $0.82 | $0.00 |
| 3 | 1SOL | 1 SOL and a dream | 99.70% | 🔴 extreme | $0.00 | $0.00 |
| 4 | ORE | Ore Labs | 99.40% | 🔴 extreme | $7.10 | $7.01K |
| 5 | BEANS | BEANS | 99.28% | 🔴 extreme | $3.41 | $8.39K |
| 6 | GAZABOY | GAZA BOY | 99.20% | 🔴 extreme | $5.26 | $7.18K |
| 7 | 19 | Cult of 19 | 98.80% | 🔴 extreme | $102.81 | $7.42K |
| 8 | JIFFPOM | Jiffpom | 98.60% | 🔴 extreme | $3.66 | $10.48K |
| 9 | viewer | in a streamers world | 97.87% | 🔴 extreme | $1.55 | $7.90K |
| 10 | 1 | 1 pill can change your li | 97.66% | 🔴 extreme | $212.36 | $7.74K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 40
**Combined 24h Volume**: $207.94M
**Combined Liquidity**: $57.73M

**Concentration Risk Distribution**:
- 🔴 Extreme: 16 tokens
- 🟢 Low: 14 tokens
- 🟡 High: 7 tokens
- 🟢 Medium: 2 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $207.54M | $52.70M | 🟢 unknown |
| 2 | DREAM | Dreamsync | $224.59K | $163.34K | 🟢 low |
| 3 | AI4 | AI⁴ | $83.02K | $84.06K | 🟢 low |
| 4 | RAGEGUY | Rage Guy | $45.03K | $131.26K | 🟢 low |
| 5 | LION | Loaded Lions | $20.23K | $1.62M | 🟢 low |
| 6 | 1nu | 1nu | $19.18K | $30.17K | 🟢 low |
| 7 | HAROLD | Harold | $6.17K | $466.31K | 🟢 medium |
| 8 | FARTLESS | FARTLESS COIN | $910.03 | $3.45K | 🟢 low |
| 9 | $CrepSol | Crepe on Solana | $822.15 | $21.16K | 🟢 low |
| 10 | DARE | DareCoin | $361.11 | $12.74K | 🟡 high |

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

**Total Historical Records**: 514
**Unique Tokens Tracked**: 102
**Date Range**: 2025-10-01 to 2025-10-20

**Master Aggregations**: 102 tokens
**Performance Metrics**: 514 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 514 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 102 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 514 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 40 |
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
