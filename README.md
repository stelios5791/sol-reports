# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-10-31 22:28 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **34 tokens tracked** | 
💰 **$260.56M 24h volume** | 
💧 **$71.99M liquidity** | 
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
          5,
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
          -13.89851875196975,
          -13.89851875196975
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
      "LION",
      "RAGEGUY",
      "DREAM",
      "HAROLD",
      "SOL",
      "SHITTER",
      "1Bull",
      "RUECAT"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          69463.24,
          51184.14,
          29145.37,
          19013.45,
          13593.3,
          11130.64,
          2762.29,
          1944.26,
          1294.82,
          885.21
        ],
        "backgroundColor": [
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#ef4444",
          "#eab308",
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
      "2025-10-31"
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
          49.97
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
          41.82
        ],
        "borderColor": "#ef4444",
        "backgroundColor": "#ef444420",
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
          29.5
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
          32.07
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
            "x": 302494.0,
            "y": 49.97,
            "r": 8,
            "label": "AI4: $302,494 FDV, 50.0% concentration (low risk)"
          },
          {
            "x": 78810.0,
            "y": 41.82,
            "r": 8,
            "label": "1nu: $78,810 FDV, 41.8% concentration (low risk)"
          },
          {
            "x": 53218700.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $53,218,700 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 593658.0,
            "y": 29.5,
            "r": 8,
            "label": "RAGEGUY: $593,658 FDV, 29.5% concentration (low risk)"
          },
          {
            "x": 1111158.0,
            "y": 32.07,
            "r": 8,
            "label": "DREAM: $1,111,158 FDV, 32.1% concentration (low risk)"
          },
          {
            "x": 72030.0,
            "y": 58.75,
            "r": 8,
            "label": "RUECAT: $72,030 FDV, 58.8% concentration (low risk)"
          },
          {
            "x": 1058584.0,
            "y": 25.65,
            "r": 8,
            "label": "XBT: $1,058,584 FDV, 25.6% concentration (low risk)"
          },
          {
            "x": 472350.0,
            "y": 36.82,
            "r": 8,
            "label": "FARTLESS: $472,350 FDV, 36.8% concentration (low risk)"
          },
          {
            "x": 18208.0,
            "y": 30.06,
            "r": 8,
            "label": "FLY: $18,208 FDV, 30.1% concentration (low risk)"
          },
          {
            "x": 120798.0,
            "y": 41.23,
            "r": 8,
            "label": "YAO: $120,798 FDV, 41.2% concentration (low risk)"
          },
          {
            "x": 450039.0,
            "y": 33.47,
            "r": 8,
            "label": "ELIZABETH: $450,039 FDV, 33.5% concentration (low risk)"
          },
          {
            "x": 125668.0,
            "y": 44.34,
            "r": 8,
            "label": "USEFUL: $125,668 FDV, 44.3% concentration (low risk)"
          },
          {
            "x": 155943.0,
            "y": 39.08,
            "r": 8,
            "label": "USDUT: $155,943 FDV, 39.1% concentration (low risk)"
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
            "x": 3279238.0,
            "y": 63.81,
            "r": 8,
            "label": "HAROLD: $3,279,238 FDV, 63.8% concentration (medium risk)"
          },
          {
            "x": 26091.0,
            "y": 60.48,
            "r": 8,
            "label": "SHITTER: $26,091 FDV, 60.5% concentration (medium risk)"
          },
          {
            "x": 18764.0,
            "y": 63.87,
            "r": 8,
            "label": "$CrepSol: $18,764 FDV, 63.9% concentration (medium risk)"
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
            "x": 10309.0,
            "y": 78.97,
            "r": 8,
            "label": "1Bull: $10,309 FDV, 79.0% concentration (high risk)"
          },
          {
            "x": 6345.0,
            "y": 93.24,
            "r": 8,
            "label": "1: $6,345 FDV, 93.2% concentration (high risk)"
          },
          {
            "x": 12877.0,
            "y": 89.74,
            "r": 8,
            "label": "AUSBAGWORK: $12,877 FDV, 89.7% concentration (high risk)"
          },
          {
            "x": 7584.0,
            "y": 89.71,
            "r": 8,
            "label": "DARE: $7,584 FDV, 89.7% concentration (high risk)"
          },
          {
            "x": 5759.0,
            "y": 91.99,
            "r": 8,
            "label": "FARTWORM: $5,759 FDV, 92.0% concentration (high risk)"
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
            "x": 17049127.0,
            "y": 96.8,
            "r": 8,
            "label": "SOL: $17,049,127 FDV, 96.8% concentration (extreme risk)"
          },
          {
            "x": 5514.0,
            "y": 96.37,
            "r": 8,
            "label": "SUPRACOIN: $5,514 FDV, 96.4% concentration (extreme risk)"
          },
          {
            "x": 5243.41,
            "y": 100.0,
            "r": 8,
            "label": "YOU: $5,243 FDV, 100.0% concentration (extreme risk)"
          },
          {
            "x": 3645.0,
            "y": 98.87,
            "r": 8,
            "label": "1% Club: $3,645 FDV, 98.9% concentration (extreme risk)"
          },
          {
            "x": 10056.0,
            "y": 93.85,
            "r": 8,
            "label": "MOCHI: $10,056 FDV, 93.8% concentration (extreme risk)"
          },
          {
            "x": 4472.0,
            "y": 96.18,
            "r": 8,
            "label": "pibble: $4,472 FDV, 96.2% concentration (extreme risk)"
          },
          {
            "x": 7966.0,
            "y": 98.77,
            "r": 8,
            "label": "JIFFPOM: $7,966 FDV, 98.8% concentration (extreme risk)"
          },
          {
            "x": 3750.0,
            "y": 99.67,
            "r": 8,
            "label": "KENNY: $3,750 FDV, 99.7% concentration (extreme risk)"
          },
          {
            "x": 5289.5,
            "y": 99.89,
            "r": 8,
            "label": "2: $5,290 FDV, 99.9% concentration (extreme risk)"
          },
          {
            "x": 5460.0,
            "y": 95.8,
            "r": 8,
            "label": "1: $5,460 FDV, 95.8% concentration (extreme risk)"
          },
          {
            "x": 4652.0,
            "y": 96.39,
            "r": 8,
            "label": "7: $4,652 FDV, 96.4% concentration (extreme risk)"
          },
          {
            "x": 4712.0,
            "y": 98.45,
            "r": 8,
            "label": "FALCONS: $4,712 FDV, 98.5% concentration (extreme risk)"
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
| 1 | XBT | XBT | 25.65% | 🟢 low | $707.65 | $3.03K |
| 2 | RAGEGUY | Rage Guy | 29.50% | 🟢 low | $19.01K | $115.07K |
| 3 | FLY | Nexa | 30.06% | 🟢 low | $95.73 | $6.27K |
| 4 | DREAM | Dreamsync | 32.07% | 🟢 low | $13.59K | $140.90K |
| 5 | ELIZABETH | Just Elizabeth Cat | 33.47% | 🟢 low | $2.27 | $32.89 |
| 6 | FARTLESS | FARTLESS COIN | 36.82% | 🟢 low | $491.20 | $2.86K |
| 7 | USDUT | unstable tether | 39.08% | 🟢 low | $0.17 | $44.79 |
| 8 | YAO | YAO MING | 41.23% | 🟢 low | $32.08 | $779.07 |
| 9 | 1nu | 1nu | 41.82% | 🟢 low | $51.18K | $37.16K |
| 10 | USEFUL | USEFUL COIN | 44.34% | 🟢 low | $0.30 | $43.38 |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | YOU | YOU can change your life. | 100.00% | 🔴 extreme | $578.35 | $0.00 |
| 2 | 2 | TWO IS BETTER THAN ONE | 99.89% | 🔴 extreme | $4.26 | $0.00 |
| 3 | KENNY | KENNY KO | 99.67% | 🔴 extreme | $4.43 | $7.09K |
| 4 | 1% Club | The 1% Club | 98.87% | 🔴 extreme | $103.76 | $6.35K |
| 5 | JIFFPOM | Jiffpom | 98.77% | 🔴 extreme | $18.93 | $11.58K |
| 6 | FALCONS | THE FALCONS | 98.45% | 🔴 extreme | $0.39 | $9.16K |
| 7 | SOL | Solana | 96.80% | 🔴 extreme | $2.76K | $16.93K |
| 8 | 7 | 7 Coin | 96.39% | 🔴 extreme | $1.97 | $8.11K |
| 9 | SUPRACOIN | GIVING CAR AWAY AT 10MIL  | 96.37% | 🔴 extreme | $612.05 | $9.63K |
| 10 | pibble | pibble | 96.18% | 🔴 extreme | $52.60 | $7.39K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 34
**Combined 24h Volume**: $260.56M
**Combined Liquidity**: $71.99M

**Concentration Risk Distribution**:
- 🟢 Low: 13 tokens
- 🔴 Extreme: 12 tokens
- 🟡 High: 5 tokens
- 🟢 Medium: 3 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $260.35M | $69.27M | 🟢 unknown |
| 2 | AI4 | AI⁴ | $69.46K | $102.89K | 🟢 low |
| 3 | 1nu | 1nu | $51.18K | $37.16K | 🟢 low |
| 4 | LION | Loaded Lions | $29.15K | $1.59M | 🟢 low |
| 5 | RAGEGUY | Rage Guy | $19.01K | $115.07K | 🟢 low |
| 6 | DREAM | Dreamsync | $13.59K | $140.90K | 🟢 low |
| 7 | HAROLD | Harold | $11.13K | $487.78K | 🟢 medium |
| 8 | SOL | Solana | $2.76K | $16.93K | 🔴 extreme |
| 9 | SHITTER | SHITTERCOIN | $1.94K | $22.39K | 🟢 medium |
| 10 | 1Bull | One bull run to change your li | $1.29K | $12.17K | 🟡 high |

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
- 👀 **Watch**: 114 tokens
- 🚀 **Breakout**: 3 tokens
- ❄️ **Cooling**: 1 tokens

### 🚀 Breakout Signals

| Symbol | Score | Vol 3v1 | Z-Score Vol | Liq 3d | Streak |
|--------|-------|---------|-------------|--------|--------|
| wSOL | 4.24 | 2.51x | 1.69 | $57.82M | 0d |
| XBT | 3.65 | 2.10x | 1.74 | $421.14K | 0d |
| USDUT | 3.57 | 2.36x | 1.51 | $150.84K | 0d |

### 👀 Watch List

*114 tokens showing elevated activity*

📄 [Full data: signals_filtered.csv](data/signals_filtered.csv)

---

## 📈 Historical Data

**Total Historical Records**: 508
**Unique Tokens Tracked**: 101
**Date Range**: 2025-10-01 to 2025-10-31

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
| [signals_filtered.csv](data/signals_filtered.csv) | Whale-filtered trading signals | 118 |

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
