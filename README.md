# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-10-19 19:01 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **37 tokens tracked** | 
💰 **$163.22M 24h volume** | 
💧 **$57.75M liquidity** | 
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
          2,
          8,
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
          -36.23399773132394,
          -36.23399773132394
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
      "AI4",
      "RAGEGUY",
      "1nu",
      "LION",
      "1Bull",
      "HAROLD",
      "$CrepSol",
      "19",
      "FARTLESS"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          85486.71,
          78702.82,
          61012.56,
          23746.01,
          5138.18,
          5092.93,
          1687.93,
          1468.59,
          1186.62,
          731.37
        ],
        "backgroundColor": [
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#f97316",
          "#eab308",
          "#22c55e",
          "#ef4444",
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
      "2025-10-19"
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
          31.82
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
          49.0
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
          26.99
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
          41.68
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
            "x": 1595495.0,
            "y": 31.82,
            "r": 8,
            "label": "DREAM: $1,595,495 FDV, 31.8% concentration (low risk)"
          },
          {
            "x": 185518.0,
            "y": 49.0,
            "r": 8,
            "label": "AI4: $185,518 FDV, 49.0% concentration (low risk)"
          },
          {
            "x": 853784.0,
            "y": 26.99,
            "r": 8,
            "label": "RAGEGUY: $853,784 FDV, 27.0% concentration (low risk)"
          },
          {
            "x": 64592.0,
            "y": 41.68,
            "r": 8,
            "label": "1nu: $64,592 FDV, 41.7% concentration (low risk)"
          },
          {
            "x": 55884085.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $55,884,085 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 35346.0,
            "y": 57.36,
            "r": 8,
            "label": "$CrepSol: $35,346 FDV, 57.4% concentration (low risk)"
          },
          {
            "x": 713817.0,
            "y": 34.39,
            "r": 8,
            "label": "FARTLESS: $713,817 FDV, 34.4% concentration (low risk)"
          },
          {
            "x": 90105.0,
            "y": 54.22,
            "r": 8,
            "label": "RUECAT: $90,105 FDV, 54.2% concentration (low risk)"
          },
          {
            "x": 1700913.0,
            "y": 22.0,
            "r": 8,
            "label": "XBT: $1,700,913 FDV, 22.0% concentration (low risk)"
          },
          {
            "x": 17969.0,
            "y": 30.33,
            "r": 8,
            "label": "FLY: $17,969 FDV, 30.3% concentration (low risk)"
          },
          {
            "x": 826647.0,
            "y": 28.31,
            "r": 8,
            "label": "ELIZABETH: $826,647 FDV, 28.3% concentration (low risk)"
          },
          {
            "x": 106845.0,
            "y": 44.62,
            "r": 8,
            "label": "YAO: $106,845 FDV, 44.6% concentration (low risk)"
          },
          {
            "x": 18266908.0,
            "y": 39.75,
            "r": 8,
            "label": "AI20X: $18,266,908 FDV, 39.8% concentration (low risk)"
          },
          {
            "x": 249680.0,
            "y": 46.08,
            "r": 8,
            "label": "gib: $249,680 FDV, 46.1% concentration (low risk)"
          },
          {
            "x": 128933.0,
            "y": 44.25,
            "r": 8,
            "label": "USEFUL: $128,933 FDV, 44.2% concentration (low risk)"
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
            "x": 3057469.0,
            "y": 63.56,
            "r": 8,
            "label": "HAROLD: $3,057,469 FDV, 63.6% concentration (medium risk)"
          },
          {
            "x": 22521.0,
            "y": 64.53,
            "r": 8,
            "label": "SHITTER: $22,521 FDV, 64.5% concentration (medium risk)"
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
            "x": 9895.0,
            "y": 78.71,
            "r": 8,
            "label": "1Bull: $9,895 FDV, 78.7% concentration (high risk)"
          },
          {
            "x": 6727.0,
            "y": 88.22,
            "r": 8,
            "label": "FARTWORM: $6,727 FDV, 88.2% concentration (high risk)"
          },
          {
            "x": 10572.0,
            "y": 92.61,
            "r": 8,
            "label": "MOCHI: $10,572 FDV, 92.6% concentration (high risk)"
          },
          {
            "x": 5406.0,
            "y": 90.29,
            "r": 8,
            "label": "RWA: $5,406 FDV, 90.3% concentration (high risk)"
          },
          {
            "x": 4332.0,
            "y": 81.08,
            "r": 8,
            "label": "APOLLO: $4,332 FDV, 81.1% concentration (high risk)"
          },
          {
            "x": 14258.0,
            "y": 88.11,
            "r": 8,
            "label": "AUSBAGWORK: $14,258 FDV, 88.1% concentration (high risk)"
          },
          {
            "x": 8910.0,
            "y": 88.99,
            "r": 8,
            "label": "DARE: $8,910 FDV, 89.0% concentration (high risk)"
          },
          {
            "x": 9719.0,
            "y": 89.36,
            "r": 8,
            "label": "IDIOT: $9,719 FDV, 89.4% concentration (high risk)"
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
            "x": 4253.0,
            "y": 98.52,
            "r": 8,
            "label": "19: $4,253 FDV, 98.5% concentration (extreme risk)"
          },
          {
            "x": 11985515.0,
            "y": 96.74,
            "r": 8,
            "label": "SOL: $11,985,515 FDV, 96.7% concentration (extreme risk)"
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
            "x": 3935.0,
            "y": 97.66,
            "r": 8,
            "label": "1: $3,935 FDV, 97.7% concentration (extreme risk)"
          },
          {
            "x": 4131.0,
            "y": 96.95,
            "r": 8,
            "label": "Streamless: $4,131 FDV, 97.0% concentration (extreme risk)"
          },
          {
            "x": 6009.0,
            "y": 95.45,
            "r": 8,
            "label": "7: $6,009 FDV, 95.5% concentration (extreme risk)"
          },
          {
            "x": 3702.0,
            "y": 99.67,
            "r": 8,
            "label": "KENNY: $3,702 FDV, 99.7% concentration (extreme risk)"
          },
          {
            "x": 3691.0,
            "y": 99.57,
            "r": 8,
            "label": "Supershiro: $3,691 FDV, 99.6% concentration (extreme risk)"
          },
          {
            "x": 4688.0,
            "y": 97.18,
            "r": 8,
            "label": "BULLCOIN: $4,688 FDV, 97.2% concentration (extreme risk)"
          },
          {
            "x": 4624.0,
            "y": 98.57,
            "r": 8,
            "label": "Noxi: $4,624 FDV, 98.6% concentration (extreme risk)"
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
| 1 | XBT | XBT | 22.00% | 🟢 low | $78.68 | $612.24 |
| 2 | RAGEGUY | Rage Guy | 26.99% | 🟢 low | $61.01K | $138.12K |
| 3 | ELIZABETH | Just Elizabeth Cat | 28.31% | 🟢 low | $24.08 | $44.17 |
| 4 | FLY | Nexa | 30.33% | 🟢 low | $44.73 | $2.46K |
| 5 | DREAM | Dreamsync | 31.82% | 🟢 low | $85.49K | $169.17K |
| 6 | FARTLESS | FARTLESS COIN | 34.39% | 🟢 low | $731.37 | $3.48K |
| 7 | AI20X | Ai20x.ai | 39.75% | 🟢 low | $8.05 | $2.17M |
| 8 | 1nu | 1nu | 41.68% | 🟢 low | $23.75K | $33.07K |
| 9 | USEFUL | USEFUL COIN | 44.25% | 🟢 low | $1.99 | $52.49 |
| 10 | YAO | YAO MING | 44.62% | 🟢 low | $17.96 | $746.22 |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | KENNY | KENNY KO | 99.67% | 🔴 extreme | $1.20 | $7.00K |
| 2 | Supershiro | Super Shiro | 99.57% | 🔴 extreme | $0.98 | $6.98K |
| 3 | Noxi | Noxi Labs AI | 98.57% | 🔴 extreme | $0.23 | $40.29 |
| 4 | 19 | Cult of 19 | 98.52% | 🔴 extreme | $1.19K | $7.62K |
| 5 | 1 | 1 pill can change your li | 97.66% | 🔴 extreme | $44.88 | $7.30K |
| 6 | BULLCOIN | BULLCOIN | 97.18% | 🔴 extreme | $0.46 | $8.08K |
| 7 | Streamless | Streamless coin | 96.95% | 🔴 extreme | $16.53 | $7.85K |
| 8 | SOL | Solana | 96.74% | 🔴 extreme | $458.90 | $14.19K |
| 9 | 7 | 7 Coin | 95.45% | 🔴 extreme | $2.97 | $9.35K |
| 10 | SUPRACOIN | GIVING CAR AWAY AT 10MIL  | 94.93% | 🔴 extreme | $88.07 | $11.12K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 37
**Combined 24h Volume**: $163.22M
**Combined Liquidity**: $57.75M

**Concentration Risk Distribution**:
- 🟢 Low: 15 tokens
- 🔴 Extreme: 11 tokens
- 🟡 High: 8 tokens
- 🟢 Medium: 2 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $162.95M | $52.78M | 🟢 unknown |
| 2 | DREAM | Dreamsync | $85.49K | $169.17K | 🟢 low |
| 3 | AI4 | AI⁴ | $78.70K | $79.96K | 🟢 low |
| 4 | RAGEGUY | Rage Guy | $61.01K | $138.12K | 🟢 low |
| 5 | 1nu | 1nu | $23.75K | $33.07K | 🟢 low |
| 6 | LION | Loaded Lions | $5.14K | $1.64M | 🟢 low |
| 7 | 1Bull | One bull run to change your li | $5.09K | $11.98K | 🟡 high |
| 8 | HAROLD | Harold | $1.69K | $474.01K | 🟢 medium |
| 9 | $CrepSol | Crepe on Solana | $1.47K | $21.87K | 🟢 low |
| 10 | 19 | Cult of 19 | $1.19K | $7.62K | 🔴 extreme |

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
- 👀 **Watch**: 111 tokens
- 🚀 **Breakout**: 3 tokens
- ❄️ **Cooling**: 1 tokens

### 🚀 Breakout Signals

| Symbol | Score | Vol 3v1 | Z-Score Vol | Liq 3d | Streak |
|--------|-------|---------|-------------|--------|--------|
| wSOL | 4.24 | 2.51x | 1.69 | $57.82M | 0d |
| XBT | 3.65 | 2.10x | 1.74 | $421.14K | 0d |
| USDUT | 3.57 | 2.36x | 1.51 | $150.84K | 0d |

### 👀 Watch List

*111 tokens showing elevated activity*

📄 [Full data: signals_filtered.csv](data/signals_filtered.csv)

---

## 📈 Historical Data

**Total Historical Records**: 511
**Unique Tokens Tracked**: 101
**Date Range**: 2025-10-01 to 2025-10-19

**Master Aggregations**: 101 tokens
**Performance Metrics**: 511 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 511 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 101 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 511 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 37 |
| [new_viable.csv](data/new_viable.csv) | New tokens with potential | 0 |
| [signals_filtered.csv](data/signals_filtered.csv) | Whale-filtered trading signals | 115 |

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
