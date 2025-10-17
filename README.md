# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-10-17 08:38 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **43 tokens tracked** | 
💰 **$502.03M 24h volume** | 
💧 **$55.06M liquidity** | 
🟢 **15 low-risk tokens**

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
          15,
          3,
          8,
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
          -28.125482923813944,
          -28.125482923813944
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
      "AI4",
      "1nu",
      "DREAM",
      "HAROLD",
      "LION",
      "RAGEGUY",
      "AUSBAGWORK",
      "SHITTER",
      "1",
      "7"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          97127.48,
          72058.13,
          52612.7,
          51408.03,
          45389.89,
          14848.78,
          12087.07,
          5547.77,
          3373.11,
          1118.5
        ],
        "backgroundColor": [
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#22c55e",
          "#22c55e",
          "#f97316",
          "#eab308",
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
      "2025-10-17"
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
          50.27
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
          40.69
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
          31.6
        ],
        "borderColor": "#22c55e",
        "backgroundColor": "#22c55e20",
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
          63.8
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
            "x": 204612.0,
            "y": 50.27,
            "r": 8,
            "label": "AI4: $204,612 FDV, 50.3% concentration (low risk)"
          },
          {
            "x": 67061.0,
            "y": 40.69,
            "r": 8,
            "label": "1nu: $67,061 FDV, 40.7% concentration (low risk)"
          },
          {
            "x": 1611118.0,
            "y": 31.6,
            "r": 8,
            "label": "DREAM: $1,611,118 FDV, 31.6% concentration (low risk)"
          },
          {
            "x": 54150419.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $54,150,419 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 617264.0,
            "y": 27.6,
            "r": 8,
            "label": "RAGEGUY: $617,264 FDV, 27.6% concentration (low risk)"
          },
          {
            "x": 662991.0,
            "y": 34.96,
            "r": 8,
            "label": "FARTLESS: $662,991 FDV, 35.0% concentration (low risk)"
          },
          {
            "x": 29134.0,
            "y": 57.76,
            "r": 8,
            "label": "$CrepSol: $29,134 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 89755.0,
            "y": 53.46,
            "r": 8,
            "label": "RUECAT: $89,755 FDV, 53.5% concentration (low risk)"
          },
          {
            "x": 16812.0,
            "y": 30.21,
            "r": 8,
            "label": "FLY: $16,812 FDV, 30.2% concentration (low risk)"
          },
          {
            "x": 1464721.0,
            "y": 22.38,
            "r": 8,
            "label": "XBT: $1,464,721 FDV, 22.4% concentration (low risk)"
          },
          {
            "x": 1092284.0,
            "y": 27.23,
            "r": 8,
            "label": "ELIZABETH: $1,092,284 FDV, 27.2% concentration (low risk)"
          },
          {
            "x": 19276487.0,
            "y": 39.75,
            "r": 8,
            "label": "AI20X: $19,276,487 FDV, 39.8% concentration (low risk)"
          },
          {
            "x": 64463.0,
            "y": 48.58,
            "r": 8,
            "label": "YAO: $64,463 FDV, 48.6% concentration (low risk)"
          },
          {
            "x": 134496.0,
            "y": 42.23,
            "r": 8,
            "label": "USEFUL: $134,496 FDV, 42.2% concentration (low risk)"
          },
          {
            "x": 226709.0,
            "y": 47.14,
            "r": 8,
            "label": "gib: $226,709 FDV, 47.1% concentration (low risk)"
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
            "x": 2724227.0,
            "y": 63.8,
            "r": 8,
            "label": "HAROLD: $2,724,227 FDV, 63.8% concentration (medium risk)"
          },
          {
            "x": 24326.0,
            "y": 63.01,
            "r": 8,
            "label": "SHITTER: $24,326 FDV, 63.0% concentration (medium risk)"
          },
          {
            "x": 23440.0,
            "y": 75.45,
            "r": 8,
            "label": "1Bull: $23,440 FDV, 75.5% concentration (medium risk)"
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
            "x": 13998.0,
            "y": 87.69,
            "r": 8,
            "label": "AUSBAGWORK: $13,998 FDV, 87.7% concentration (high risk)"
          },
          {
            "x": 6466.0,
            "y": 92.55,
            "r": 8,
            "label": "1: $6,466 FDV, 92.5% concentration (high risk)"
          },
          {
            "x": 5322.0,
            "y": 89.87,
            "r": 8,
            "label": "RWA: $5,322 FDV, 89.9% concentration (high risk)"
          },
          {
            "x": 8256.0,
            "y": 88.93,
            "r": 8,
            "label": "DARE: $8,256 FDV, 88.9% concentration (high risk)"
          },
          {
            "x": 6796.0,
            "y": 87.68,
            "r": 8,
            "label": "FARTWORM: $6,796 FDV, 87.7% concentration (high risk)"
          },
          {
            "x": 10646.0,
            "y": 92.21,
            "r": 8,
            "label": "MOCHI: $10,646 FDV, 92.2% concentration (high risk)"
          },
          {
            "x": 9929.0,
            "y": 88.37,
            "r": 8,
            "label": "IDIOT: $9,929 FDV, 88.4% concentration (high risk)"
          },
          {
            "x": 4371.0,
            "y": 80.7,
            "r": 8,
            "label": "APOLLO: $4,371 FDV, 80.7% concentration (high risk)"
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
            "x": 4957.0,
            "y": 95.46,
            "r": 8,
            "label": "7: $4,957 FDV, 95.5% concentration (extreme risk)"
          },
          {
            "x": 4220.0,
            "y": 97.98,
            "r": 8,
            "label": "1% Club: $4,220 FDV, 98.0% concentration (extreme risk)"
          },
          {
            "x": 4650.0,
            "y": 97.04,
            "r": 8,
            "label": "1: $4,650 FDV, 97.0% concentration (extreme risk)"
          },
          {
            "x": 12313440.0,
            "y": 96.74,
            "r": 8,
            "label": "SOL: $12,313,440 FDV, 96.7% concentration (extreme risk)"
          },
          {
            "x": 4453.0,
            "y": 95.7,
            "r": 8,
            "label": "pibble: $4,453 FDV, 95.7% concentration (extreme risk)"
          },
          {
            "x": 6582.0,
            "y": 98.54,
            "r": 8,
            "label": "JIFFPOM: $6,582 FDV, 98.5% concentration (extreme risk)"
          },
          {
            "x": 3856.0,
            "y": 97.81,
            "r": 8,
            "label": "BLUB: $3,856 FDV, 97.8% concentration (extreme risk)"
          },
          {
            "x": 7537.0,
            "y": 94.71,
            "r": 8,
            "label": "SUPRACOIN: $7,537 FDV, 94.7% concentration (extreme risk)"
          },
          {
            "x": 4584.0,
            "y": 97.18,
            "r": 8,
            "label": "BULLCOIN: $4,584 FDV, 97.2% concentration (extreme risk)"
          },
          {
            "x": 3870.0,
            "y": 98.91,
            "r": 8,
            "label": "19: $3,870 FDV, 98.9% concentration (extreme risk)"
          },
          {
            "x": 3513.0,
            "y": 99.11,
            "r": 8,
            "label": "GAZABOY: $3,513 FDV, 99.1% concentration (extreme risk)"
          },
          {
            "x": 4367.0,
            "y": 97.23,
            "r": 8,
            "label": "obvious: $4,367 FDV, 97.2% concentration (extreme risk)"
          },
          {
            "x": 3435.0,
            "y": 99.99,
            "r": 8,
            "label": "UPC: $3,435 FDV, 100.0% concentration (extreme risk)"
          },
          {
            "x": 3434.0,
            "y": 99.26,
            "r": 8,
            "label": "ORE: $3,434 FDV, 99.3% concentration (extreme risk)"
          },
          {
            "x": 4098.0,
            "y": 99.46,
            "r": 8,
            "label": "MoneyBear: $4,098 FDV, 99.5% concentration (extreme risk)"
          },
          {
            "x": 4034.0,
            "y": 97.85,
            "r": 8,
            "label": "viewer: $4,034 FDV, 97.8% concentration (extreme risk)"
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
| 1 | XBT | XBT | 22.38% | 🟢 low | $54.50 | $547.41 |
| 2 | ELIZABETH | Just Elizabeth Cat | 27.23% | 🟢 low | $39.43 | $50.77 |
| 3 | RAGEGUY | Rage Guy | 27.60% | 🟢 low | $14.85K | $113.48K |
| 4 | FLY | Nexa | 30.21% | 🟢 low | $291.14 | $2.29K |
| 5 | DREAM | Dreamsync | 31.60% | 🟢 low | $52.61K | $164.25K |
| 6 | FARTLESS | FARTLESS COIN | 34.96% | 🟢 low | $808.96 | $3.36K |
| 7 | AI20X | Ai20x.ai | 39.75% | 🟢 low | $37.74 | $2.29M |
| 8 | 1nu | 1nu | 40.69% | 🟢 low | $72.06K | $33.60K |
| 9 | USEFUL | USEFUL COIN | 42.23% | 🟢 low | $2.58 | $47.44 |
| 10 | gib | gib | 47.14% | 🟢 low | $1.47 | $33.36 |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | UPC | Upcoin | 99.99% | 🔴 extreme | $0.40 | $6.83K |
| 2 | MoneyBear | The Money Bears | 99.46% | 🔴 extreme | $0.36 | $8.12K |
| 3 | ORE | Ore Labs | 99.26% | 🔴 extreme | $0.39 | $6.68K |
| 4 | GAZABOY | GAZA BOY | 99.11% | 🔴 extreme | $0.47 | $6.86K |
| 5 | 19 | Cult of 19 | 98.91% | 🔴 extreme | $0.62 | $7.19K |
| 6 | JIFFPOM | Jiffpom | 98.54% | 🔴 extreme | $52.42 | $10.87K |
| 7 | 1% Club | The 1% Club | 97.98% | 🔴 extreme | $563.58 | $6.83K |
| 8 | viewer | in a streamers world | 97.85% | 🔴 extreme | $0.23 | $7.73K |
| 9 | BLUB | Blub | 97.81% | 🔴 extreme | $13.40 | $7.39K |
| 10 | obvious | in hindsight | 97.23% | 🔴 extreme | $0.45 | $7.84K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 43
**Combined 24h Volume**: $502.03M
**Combined Liquidity**: $55.06M

**Concentration Risk Distribution**:
- 🔴 Extreme: 16 tokens
- 🟢 Low: 15 tokens
- 🟡 High: 8 tokens
- 🟢 Medium: 3 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $501.67M | $50.05M | 🟢 unknown |
| 2 | AI4 | AI⁴ | $97.13K | $81.02K | 🟢 low |
| 3 | 1nu | 1nu | $72.06K | $33.60K | 🟢 low |
| 4 | DREAM | Dreamsync | $52.61K | $164.25K | 🟢 low |
| 5 | HAROLD | Harold | $51.41K | $430.53K | 🟢 medium |
| 6 | LION | Loaded Lions | $45.39K | $1.57M | 🟢 low |
| 7 | RAGEGUY | Rage Guy | $14.85K | $113.48K | 🟢 low |
| 8 | AUSBAGWORK | AUSSIE BAG WORKERS | $12.09K | $16.47K | 🟡 high |
| 9 | SHITTER | SHITTERCOIN | $5.55K | $21.59K | 🟢 medium |
| 10 | 1 | 1 pill can change your life | $3.37K | $10.20K | 🟡 high |

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
- 👀 **Watch**: 3 tokens
- 🚀 **Breakout**: 1 tokens

### 🚀 Breakout Signals

| Symbol | Score | Vol 3v1 | Z-Score Vol | Liq 3d | Streak |
|--------|-------|---------|-------------|--------|--------|
| wSOL | 55321.15 | 2.47x | 1.94 | $55.31M | 1d |

### 👀 Watch List

*3 tokens showing elevated activity*

📄 [Full data: signals_filtered.csv](data/signals_filtered.csv)

---

## 📈 Historical Data

**Total Historical Records**: 517
**Unique Tokens Tracked**: 101
**Date Range**: 2025-10-01 to 2025-10-17

**Master Aggregations**: 101 tokens
**Performance Metrics**: 517 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 517 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 101 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 517 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 43 |
| [new_viable.csv](data/new_viable.csv) | New tokens with potential | 0 |
| [signals_filtered.csv](data/signals_filtered.csv) | Whale-filtered trading signals | 4 |

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
