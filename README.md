# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-10-20 08:39 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **38 tokens tracked** | 
💰 **$198.11M 24h volume** | 
💧 **$57.04M liquidity** | 
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
          2,
          8,
          14,
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
          45.78313253012048,
          45.78313253012048
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
      "1nu",
      "LION",
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
          260777.28,
          80370.5,
          38965.84,
          20774.84,
          15187.01,
          4959.71,
          1638.64,
          904.09,
          581.98,
          406.99
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
          31.86
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
          48.28
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
          26.61
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
          42.34
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
            "x": 1600888.0,
            "y": 31.86,
            "r": 8,
            "label": "DREAM: $1,600,888 FDV, 31.9% concentration (low risk)"
          },
          {
            "x": 192667.0,
            "y": 48.28,
            "r": 8,
            "label": "AI4: $192,667 FDV, 48.3% concentration (low risk)"
          },
          {
            "x": 955881.0,
            "y": 26.61,
            "r": 8,
            "label": "RAGEGUY: $955,881 FDV, 26.6% concentration (low risk)"
          },
          {
            "x": 68765.0,
            "y": 42.34,
            "r": 8,
            "label": "1nu: $68,765 FDV, 42.3% concentration (low risk)"
          },
          {
            "x": 57838697.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $57,838,697 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 37424.0,
            "y": 56.69,
            "r": 8,
            "label": "$CrepSol: $37,424 FDV, 56.7% concentration (low risk)"
          },
          {
            "x": 751961.0,
            "y": 34.22,
            "r": 8,
            "label": "FARTLESS: $751,961 FDV, 34.2% concentration (low risk)"
          },
          {
            "x": 87822.0,
            "y": 54.36,
            "r": 8,
            "label": "RUECAT: $87,822 FDV, 54.4% concentration (low risk)"
          },
          {
            "x": 511297.0,
            "y": 32.2,
            "r": 8,
            "label": "ELIZABETH: $511,297 FDV, 32.2% concentration (low risk)"
          },
          {
            "x": 18329.0,
            "y": 30.33,
            "r": 8,
            "label": "FLY: $18,329 FDV, 30.3% concentration (low risk)"
          },
          {
            "x": 105149.0,
            "y": 43.99,
            "r": 8,
            "label": "YAO: $105,149 FDV, 44.0% concentration (low risk)"
          },
          {
            "x": 249680.0,
            "y": 46.24,
            "r": 8,
            "label": "gib: $249,680 FDV, 46.2% concentration (low risk)"
          },
          {
            "x": 129116.0,
            "y": 44.32,
            "r": 8,
            "label": "USEFUL: $129,116 FDV, 44.3% concentration (low risk)"
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
            "x": 3120053.0,
            "y": 63.54,
            "r": 8,
            "label": "HAROLD: $3,120,053 FDV, 63.5% concentration (medium risk)"
          },
          {
            "x": 22492.0,
            "y": 64.56,
            "r": 8,
            "label": "SHITTER: $22,492 FDV, 64.6% concentration (medium risk)"
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
            "x": 9070.0,
            "y": 88.86,
            "r": 8,
            "label": "DARE: $9,070 FDV, 88.9% concentration (high risk)"
          },
          {
            "x": 6344.0,
            "y": 90.04,
            "r": 8,
            "label": "FARTWORM: $6,344 FDV, 90.0% concentration (high risk)"
          },
          {
            "x": 9857.0,
            "y": 78.71,
            "r": 8,
            "label": "1Bull: $9,857 FDV, 78.7% concentration (high risk)"
          },
          {
            "x": 5393.0,
            "y": 90.38,
            "r": 8,
            "label": "RWA: $5,393 FDV, 90.4% concentration (high risk)"
          },
          {
            "x": 4332.0,
            "y": 81.08,
            "r": 8,
            "label": "APOLLO: $4,332 FDV, 81.1% concentration (high risk)"
          },
          {
            "x": 13968.0,
            "y": 88.11,
            "r": 8,
            "label": "AUSBAGWORK: $13,968 FDV, 88.1% concentration (high risk)"
          },
          {
            "x": 9623.0,
            "y": 89.36,
            "r": 8,
            "label": "IDIOT: $9,623 FDV, 89.4% concentration (high risk)"
          },
          {
            "x": 10450.0,
            "y": 92.63,
            "r": 8,
            "label": "MOCHI: $10,450 FDV, 92.6% concentration (high risk)"
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
            "x": 12150930.0,
            "y": 96.74,
            "r": 8,
            "label": "SOL: $12,150,930 FDV, 96.7% concentration (extreme risk)"
          },
          {
            "x": 4008.0,
            "y": 98.8,
            "r": 8,
            "label": "19: $4,008 FDV, 98.8% concentration (extreme risk)"
          },
          {
            "x": 4233.0,
            "y": 97.53,
            "r": 8,
            "label": "1: $4,233 FDV, 97.5% concentration (extreme risk)"
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
            "x": 7318.0,
            "y": 94.93,
            "r": 8,
            "label": "SUPRACOIN: $7,318 FDV, 94.9% concentration (extreme risk)"
          },
          {
            "x": 4121.0,
            "y": 96.97,
            "r": 8,
            "label": "Streamless: $4,121 FDV, 97.0% concentration (extreme risk)"
          },
          {
            "x": 3677.0,
            "y": 99.2,
            "r": 8,
            "label": "GAZABOY: $3,677 FDV, 99.2% concentration (extreme risk)"
          },
          {
            "x": 3596.0,
            "y": 99.33,
            "r": 8,
            "label": "ORE: $3,596 FDV, 99.3% concentration (extreme risk)"
          },
          {
            "x": 4312.0,
            "y": 99.27,
            "r": 8,
            "label": "BEANS: $4,312 FDV, 99.3% concentration (extreme risk)"
          },
          {
            "x": 4688.0,
            "y": 97.18,
            "r": 8,
            "label": "BULLCOIN: $4,688 FDV, 97.2% concentration (extreme risk)"
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
| 1 | RAGEGUY | Rage Guy | 26.61% | 🟢 low | $38.97K | $147.18K |
| 2 | FLY | Nexa | 30.33% | 🟢 low | $10.51 | $2.50K |
| 3 | DREAM | Dreamsync | 31.86% | 🟢 low | $260.78K | $171.05K |
| 4 | ELIZABETH | Just Elizabeth Cat | 32.20% | 🟢 low | $20.20 | $34.73 |
| 5 | FARTLESS | FARTLESS COIN | 34.22% | 🟢 low | $904.09 | $3.57K |
| 6 | 1nu | 1nu | 42.34% | 🟢 low | $20.77K | $34.14K |
| 7 | YAO | YAO MING | 43.99% | 🟢 low | $6.15 | $723.84 |
| 8 | USEFUL | USEFUL COIN | 44.32% | 🟢 low | $1.38 | $55.49 |
| 9 | gib | gib | 46.24% | 🟢 low | $2.05 | $35.01 |
| 10 | AI4 | AI⁴ | 48.28% | 🟢 low | $80.37K | $82.37K |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | LOW | lowcut | 99.97% | 🔴 extreme | $0.00 | $0.00 |
| 2 | 1SOL | 1 SOL and a dream | 99.70% | 🔴 extreme | $0.00 | $0.00 |
| 3 | ORE | Ore Labs | 99.33% | 🔴 extreme | $3.48 | $7.00K |
| 4 | BEANS | BEANS | 99.27% | 🔴 extreme | $3.41 | $8.39K |
| 5 | GAZABOY | GAZA BOY | 99.20% | 🔴 extreme | $5.26 | $7.18K |
| 6 | 19 | Cult of 19 | 98.80% | 🔴 extreme | $255.91 | $7.42K |
| 7 | 1 | 1 pill can change your li | 97.53% | 🔴 extreme | $233.93 | $7.61K |
| 8 | BULLCOIN | BULLCOIN | 97.18% | 🔴 extreme | $0.46 | $8.08K |
| 9 | Streamless | Streamless coin | 96.97% | 🔴 extreme | $17.20 | $7.85K |
| 10 | SOL | Solana | 96.74% | 🔴 extreme | $406.99 | $14.46K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 38
**Combined 24h Volume**: $198.11M
**Combined Liquidity**: $57.04M

**Concentration Risk Distribution**:
- 🔴 Extreme: 14 tokens
- 🟢 Low: 13 tokens
- 🟡 High: 8 tokens
- 🟢 Medium: 2 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $197.68M | $54.15M | 🟢 unknown |
| 2 | DREAM | Dreamsync | $260.78K | $171.05K | 🟢 low |
| 3 | AI4 | AI⁴ | $80.37K | $82.37K | 🟢 low |
| 4 | RAGEGUY | Rage Guy | $38.97K | $147.18K | 🟢 low |
| 5 | 1nu | 1nu | $20.77K | $34.14K | 🟢 low |
| 6 | LION | Loaded Lions | $15.19K | $1.68M | 🟢 low |
| 7 | HAROLD | Harold | $4.96K | $481.41K | 🟢 medium |
| 8 | $CrepSol | Crepe on Solana | $1.64K | $22.66K | 🟢 low |
| 9 | FARTLESS | FARTLESS COIN | $904.09 | $3.57K | 🟢 low |
| 10 | SHITTER | SHITTERCOIN | $581.98 | $20.89K | 🟢 medium |

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

**Total Historical Records**: 512
**Unique Tokens Tracked**: 102
**Date Range**: 2025-10-01 to 2025-10-20

**Master Aggregations**: 102 tokens
**Performance Metrics**: 512 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 512 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 102 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 512 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 38 |
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
