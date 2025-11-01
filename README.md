# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-11-01 17:36 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **38 tokens tracked** | 
💰 **$148.85M 24h volume** | 
💧 **$71.50M liquidity** | 
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
          7,
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
          -12.837947223571325,
          -12.837947223571325
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
      "LION",
      "RAGEGUY",
      "HAROLD",
      "XBT",
      "SOL",
      "SHITTER",
      "SUPRACOIN"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          71573.68,
          28596.36,
          19396.21,
          17878.89,
          12802.0,
          3655.45,
          2019.32,
          1838.13,
          964.39,
          611.85
        ],
        "backgroundColor": [
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#22c55e",
          "#ef4444",
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
      "2025-11-01"
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
          51.73
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
          40.76
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
          32.58
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
          29.8
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
            "x": 251100.0,
            "y": 51.73,
            "r": 8,
            "label": "AI4: $251,100 FDV, 51.7% concentration (low risk)"
          },
          {
            "x": 107485.0,
            "y": 40.76,
            "r": 8,
            "label": "1nu: $107,485 FDV, 40.8% concentration (low risk)"
          },
          {
            "x": 939094.0,
            "y": 32.58,
            "r": 8,
            "label": "DREAM: $939,094 FDV, 32.6% concentration (low risk)"
          },
          {
            "x": 53914176.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $53,914,176 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 567975.0,
            "y": 29.8,
            "r": 8,
            "label": "RAGEGUY: $567,975 FDV, 29.8% concentration (low risk)"
          },
          {
            "x": 1020935.0,
            "y": 25.29,
            "r": 8,
            "label": "XBT: $1,020,935 FDV, 25.3% concentration (low risk)"
          },
          {
            "x": 72852.0,
            "y": 58.38,
            "r": 8,
            "label": "RUECAT: $72,852 FDV, 58.4% concentration (low risk)"
          },
          {
            "x": 454133.0,
            "y": 37.04,
            "r": 8,
            "label": "FARTLESS: $454,133 FDV, 37.0% concentration (low risk)"
          },
          {
            "x": 18554.0,
            "y": 30.07,
            "r": 8,
            "label": "FLY: $18,554 FDV, 30.1% concentration (low risk)"
          },
          {
            "x": 126732.0,
            "y": 40.1,
            "r": 8,
            "label": "YAO: $126,732 FDV, 40.1% concentration (low risk)"
          },
          {
            "x": 17232803.0,
            "y": 39.94,
            "r": 8,
            "label": "AI20X: $17,232,803 FDV, 39.9% concentration (low risk)"
          },
          {
            "x": 421461.0,
            "y": 33.86,
            "r": 8,
            "label": "ELIZABETH: $421,461 FDV, 33.9% concentration (low risk)"
          },
          {
            "x": 153712.0,
            "y": 39.45,
            "r": 8,
            "label": "USDUT: $153,712 FDV, 39.5% concentration (low risk)"
          },
          {
            "x": 186297.0,
            "y": 44.91,
            "r": 8,
            "label": "gib: $186,297 FDV, 44.9% concentration (low risk)"
          },
          {
            "x": 125668.0,
            "y": 44.64,
            "r": 8,
            "label": "USEFUL: $125,668 FDV, 44.6% concentration (low risk)"
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
            "x": 3271986.0,
            "y": 63.8,
            "r": 8,
            "label": "HAROLD: $3,271,986 FDV, 63.8% concentration (medium risk)"
          },
          {
            "x": 23821.0,
            "y": 62.21,
            "r": 8,
            "label": "SHITTER: $23,821 FDV, 62.2% concentration (medium risk)"
          },
          {
            "x": 17869.0,
            "y": 64.41,
            "r": 8,
            "label": "$CrepSol: $17,869 FDV, 64.4% concentration (medium risk)"
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
            "x": 9728.0,
            "y": 80.12,
            "r": 8,
            "label": "1Bull: $9,728 FDV, 80.1% concentration (high risk)"
          },
          {
            "x": 12565.0,
            "y": 89.75,
            "r": 8,
            "label": "AUSBAGWORK: $12,565 FDV, 89.8% concentration (high risk)"
          },
          {
            "x": 6176.0,
            "y": 93.46,
            "r": 8,
            "label": "1: $6,176 FDV, 93.5% concentration (high risk)"
          },
          {
            "x": 7497.0,
            "y": 89.71,
            "r": 8,
            "label": "DARE: $7,497 FDV, 89.7% concentration (high risk)"
          },
          {
            "x": 8138.0,
            "y": 92.85,
            "r": 8,
            "label": "IDIOT: $8,138 FDV, 92.8% concentration (high risk)"
          },
          {
            "x": 5743.0,
            "y": 91.95,
            "r": 8,
            "label": "FARTWORM: $5,743 FDV, 92.0% concentration (high risk)"
          },
          {
            "x": 4011.0,
            "y": 82.49,
            "r": 8,
            "label": "APOLLO: $4,011 FDV, 82.5% concentration (high risk)"
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
            "x": 16485714.0,
            "y": 96.8,
            "r": 8,
            "label": "SOL: $16,485,714 FDV, 96.8% concentration (extreme risk)"
          },
          {
            "x": 5514.0,
            "y": 96.37,
            "r": 8,
            "label": "SUPRACOIN: $5,514 FDV, 96.4% concentration (extreme risk)"
          },
          {
            "x": 4474.0,
            "y": 96.39,
            "r": 8,
            "label": "7: $4,474 FDV, 96.4% concentration (extreme risk)"
          },
          {
            "x": 3645.0,
            "y": 98.87,
            "r": 8,
            "label": "1% Club: $3,645 FDV, 98.9% concentration (extreme risk)"
          },
          {
            "x": 4460.0,
            "y": 96.28,
            "r": 8,
            "label": "pibble: $4,460 FDV, 96.3% concentration (extreme risk)"
          },
          {
            "x": 5380.0,
            "y": 96.01,
            "r": 8,
            "label": "1: $5,380 FDV, 96.0% concentration (extreme risk)"
          },
          {
            "x": 9958.0,
            "y": 93.86,
            "r": 8,
            "label": "MOCHI: $9,958 FDV, 93.9% concentration (extreme risk)"
          },
          {
            "x": 3750.0,
            "y": 99.67,
            "r": 8,
            "label": "KENNY: $3,750 FDV, 99.7% concentration (extreme risk)"
          },
          {
            "x": 3913.0,
            "y": 99.5,
            "r": 8,
            "label": "MoneyBear: $3,913 FDV, 99.5% concentration (extreme risk)"
          },
          {
            "x": 4549.0,
            "y": 97.59,
            "r": 8,
            "label": "BULLCOIN: $4,549 FDV, 97.6% concentration (extreme risk)"
          },
          {
            "x": 4657.0,
            "y": 98.46,
            "r": 8,
            "label": "FALCONS: $4,657 FDV, 98.5% concentration (extreme risk)"
          },
          {
            "x": 7984.0,
            "y": 98.78,
            "r": 8,
            "label": "JIFFPOM: $7,984 FDV, 98.8% concentration (extreme risk)"
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
| 1 | XBT | XBT | 25.29% | 🟢 low | $2.02K | $2.97K |
| 2 | RAGEGUY | Rage Guy | 29.80% | 🟢 low | $12.80K | $112.32K |
| 3 | FLY | Nexa | 30.07% | 🟢 low | $48.05 | $6.29K |
| 4 | DREAM | Dreamsync | 32.58% | 🟢 low | $19.40K | $128.76K |
| 5 | ELIZABETH | Just Elizabeth Cat | 33.86% | 🟢 low | $1.66 | $31.83 |
| 6 | FARTLESS | FARTLESS COIN | 37.04% | 🟢 low | $169.41 | $2.80K |
| 7 | USDUT | unstable tether | 39.45% | 🟢 low | $0.35 | $44.54 |
| 8 | AI20X | Ai20x.ai | 39.94% | 🟢 low | $3.34 | $2.12M |
| 9 | YAO | YAO MING | 40.10% | 🟢 low | $22.95 | $806.40 |
| 10 | 1nu | 1nu | 40.76% | 🟢 low | $28.60K | $43.43K |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | KENNY | KENNY KO | 99.67% | 🔴 extreme | $4.43 | $7.09K |
| 2 | MoneyBear | The Money Bears | 99.50% | 🔴 extreme | $4.06 | $7.76K |
| 3 | 1% Club | The 1% Club | 98.87% | 🔴 extreme | $101.97 | $6.35K |
| 4 | JIFFPOM | Jiffpom | 98.78% | 🔴 extreme | $0.30 | $11.61K |
| 5 | FALCONS | THE FALCONS | 98.46% | 🔴 extreme | $0.35 | $9.05K |
| 6 | BULLCOIN | BULLCOIN | 97.59% | 🔴 extreme | $0.42 | $7.89K |
| 7 | SOL | Solana | 96.80% | 🔴 extreme | $1.84K | $16.57K |
| 8 | 7 | 7 Coin | 96.39% | 🔴 extreme | $187.76 | $7.97K |
| 9 | SUPRACOIN | GIVING CAR AWAY AT 10MIL  | 96.37% | 🔴 extreme | $611.85 | $9.63K |
| 10 | pibble | pibble | 96.28% | 🔴 extreme | $57.35 | $7.38K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 38
**Combined 24h Volume**: $148.85M
**Combined Liquidity**: $71.50M

**Concentration Risk Distribution**:
- 🟢 Low: 15 tokens
- 🔴 Extreme: 12 tokens
- 🟡 High: 7 tokens
- 🟢 Medium: 3 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $148.68M | $66.65M | 🟢 unknown |
| 2 | AI4 | AI⁴ | $71.57K | $93.35K | 🟢 low |
| 3 | 1nu | 1nu | $28.60K | $43.43K | 🟢 low |
| 4 | DREAM | Dreamsync | $19.40K | $128.76K | 🟢 low |
| 5 | LION | Loaded Lions | $17.88K | $1.59M | 🟢 low |
| 6 | RAGEGUY | Rage Guy | $12.80K | $112.32K | 🟢 low |
| 7 | HAROLD | Harold | $3.66K | $486.40K | 🟢 medium |
| 8 | XBT | XBT | $2.02K | $2.97K | 🟢 low |
| 9 | SOL | Solana | $1.84K | $16.57K | 🔴 extreme |
| 10 | SHITTER | SHITTERCOIN | $964.39 | $21.53K | 🟢 medium |

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

**Total Historical Records**: 512
**Unique Tokens Tracked**: 101
**Date Range**: 2025-10-01 to 2025-11-01

**Master Aggregations**: 101 tokens
**Performance Metrics**: 512 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 512 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 101 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 512 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 38 |
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
