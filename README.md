# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-11-11 08:40 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **31 tokens tracked** | 
💰 **$272.07M 24h volume** | 
💧 **$48.41M liquidity** | 
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
          -36.3060314480169,
          -36.3060314480169
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
      "HAROLD",
      "DREAM",
      "1nu",
      "LION",
      "RAGEGUY",
      "1",
      "AI4",
      "AUSBAGWORK",
      "SHITTER",
      "1cat"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          60930.21,
          36189.7,
          29811.38,
          24103.24,
          5740.13,
          4650.49,
          2579.29,
          1653.49,
          1462.01,
          1253.4
        ],
        "backgroundColor": [
          "#eab308",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#f97316",
          "#22c55e",
          "#f97316",
          "#22c55e",
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
      "2025-11-11"
    ],
    "datasets": [
      {
        "label": "HAROLD",
        "data": [
          0.0,
          0.0,
          0.0,
          61.9,
          61.92,
          62.0,
          64.46
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
          33.22
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
          42.19
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
          31.28
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
            "x": 701497.0,
            "y": 33.22,
            "r": 8,
            "label": "DREAM: $701,497 FDV, 33.2% concentration (low risk)"
          },
          {
            "x": 80298.0,
            "y": 42.19,
            "r": 8,
            "label": "1nu: $80,298 FDV, 42.2% concentration (low risk)"
          },
          {
            "x": 45563021.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $45,563,021 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 388601.0,
            "y": 31.28,
            "r": 8,
            "label": "RAGEGUY: $388,601 FDV, 31.3% concentration (low risk)"
          },
          {
            "x": 173341.0,
            "y": 55.0,
            "r": 8,
            "label": "AI4: $173,341 FDV, 55.0% concentration (low risk)"
          },
          {
            "x": 32458.0,
            "y": 55.0,
            "r": 8,
            "label": "SHITTER: $32,458 FDV, 55.0% concentration (low risk)"
          },
          {
            "x": 347063.0,
            "y": 36.83,
            "r": 8,
            "label": "FARTLESS: $347,063 FDV, 36.8% concentration (low risk)"
          },
          {
            "x": 944424.0,
            "y": 26.02,
            "r": 8,
            "label": "XBT: $944,424 FDV, 26.0% concentration (low risk)"
          },
          {
            "x": 587584.0,
            "y": 32.36,
            "r": 8,
            "label": "ELIZABETH: $587,584 FDV, 32.4% concentration (low risk)"
          },
          {
            "x": 21089.0,
            "y": 27.46,
            "r": 8,
            "label": "FLY: $21,089 FDV, 27.5% concentration (low risk)"
          },
          {
            "x": 126517.0,
            "y": 40.94,
            "r": 8,
            "label": "USDUT: $126,517 FDV, 40.9% concentration (low risk)"
          },
          {
            "x": 86442.0,
            "y": 42.58,
            "r": 8,
            "label": "YAO: $86,442 FDV, 42.6% concentration (low risk)"
          },
          {
            "x": 97413.0,
            "y": 49.26,
            "r": 8,
            "label": "USEFUL: $97,413 FDV, 49.3% concentration (low risk)"
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
            "x": 3730578.0,
            "y": 64.46,
            "r": 8,
            "label": "HAROLD: $3,730,578 FDV, 64.5% concentration (medium risk)"
          },
          {
            "x": 14899.0,
            "y": 65.88,
            "r": 8,
            "label": "$CrepSol: $14,899 FDV, 65.9% concentration (medium risk)"
          },
          {
            "x": 64438.0,
            "y": 61.6,
            "r": 8,
            "label": "RUECAT: $64,438 FDV, 61.6% concentration (medium risk)"
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
            "x": 8519.0,
            "y": 79.59,
            "r": 8,
            "label": "1: $8,519 FDV, 79.6% concentration (high risk)"
          },
          {
            "x": 10777.0,
            "y": 91.06,
            "r": 8,
            "label": "AUSBAGWORK: $10,777 FDV, 91.1% concentration (high risk)"
          },
          {
            "x": 7819.0,
            "y": 83.31,
            "r": 8,
            "label": "1Bull: $7,819 FDV, 83.3% concentration (high risk)"
          },
          {
            "x": 5730.0,
            "y": 77.55,
            "r": 8,
            "label": "APOLLO: $5,730 FDV, 77.5% concentration (high risk)"
          },
          {
            "x": 7226.0,
            "y": 92.91,
            "r": 8,
            "label": "IDIOT: $7,226 FDV, 92.9% concentration (high risk)"
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
            "x": 4851.93,
            "y": 99.91,
            "r": 8,
            "label": "1cat: $4,852 FDV, 99.9% concentration (extreme risk)"
          },
          {
            "x": 5424.0,
            "y": 95.21,
            "r": 8,
            "label": "1: $5,424 FDV, 95.2% concentration (extreme risk)"
          },
          {
            "x": 12605671.0,
            "y": 96.8,
            "r": 8,
            "label": "SOL: $12,605,671 FDV, 96.8% concentration (extreme risk)"
          },
          {
            "x": 8829.0,
            "y": 94.22,
            "r": 8,
            "label": "MOCHI: $8,829 FDV, 94.2% concentration (extreme risk)"
          },
          {
            "x": 4384.0,
            "y": 96.6,
            "r": 8,
            "label": "pibble: $4,384 FDV, 96.6% concentration (extreme risk)"
          },
          {
            "x": 3481.0,
            "y": 98.2,
            "r": 8,
            "label": "Hosico: $3,481 FDV, 98.2% concentration (extreme risk)"
          },
          {
            "x": 3608.0,
            "y": 97.42,
            "r": 8,
            "label": "Streamless: $3,608 FDV, 97.4% concentration (extreme risk)"
          },
          {
            "x": 4307.0,
            "y": 98.73,
            "r": 8,
            "label": "REVIVE: $4,307 FDV, 98.7% concentration (extreme risk)"
          },
          {
            "x": 4075.0,
            "y": 97.6,
            "r": 8,
            "label": "BULLCOIN: $4,075 FDV, 97.6% concentration (extreme risk)"
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
| 1 | XBT | XBT | 26.02% | 🟢 low | $30.96 | $425.46 |
| 2 | FLY | Nexa | 27.46% | 🟢 low | $1.96 | $2.47K |
| 3 | RAGEGUY | Rage Guy | 31.28% | 🟢 low | $5.74K | $87.44K |
| 4 | ELIZABETH | Just Elizabeth Cat | 32.36% | 🟢 low | $9.91 | $37.58 |
| 5 | DREAM | Dreamsync | 33.22% | 🟢 low | $36.19K | $105.42K |
| 6 | FARTLESS | FARTLESS COIN | 36.83% | 🟢 low | $356.87 | $2.46K |
| 7 | USDUT | unstable tether | 40.94% | 🟢 low | $1.68 | $39.81 |
| 8 | 1nu | 1nu | 42.19% | 🟢 low | $29.81K | $38.46K |
| 9 | YAO | YAO MING | 42.58% | 🟢 low | $1.25 | $570.88 |
| 10 | USEFUL | USEFUL COIN | 49.26% | 🟢 low | $0.48 | $35.32 |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | 1cat | 1 cat can change your lif | 99.91% | 🔴 extreme | $1.25K | $0.00 |
| 2 | REVIVE | reviving the memes | 98.73% | 🔴 extreme | $1.92 | $8.44K |
| 3 | Hosico | Hosico Cat | 98.20% | 🔴 extreme | $3.32 | $6.43K |
| 4 | BULLCOIN | BULLCOIN | 97.60% | 🔴 extreme | $0.66 | $7.07K |
| 5 | Streamless | Streamless coin | 97.42% | 🔴 extreme | $2.39 | $6.91K |
| 6 | SOL | Solana | 96.80% | 🔴 extreme | $408.56 | $13.66K |
| 7 | pibble | pibble | 96.60% | 🔴 extreme | $4.84 | $7.33K |
| 8 | 1 | 1 pill can change your li | 95.21% | 🔴 extreme | $656.54 | $8.81K |
| 9 | MOCHI | MOCHI CULT | 94.22% | 🔴 extreme | $12.70 | $15.45K |
| 10 | IDIOT | IDIOT | 92.91% | 🟠 high | $2.11 | $10.21K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 31
**Combined 24h Volume**: $272.07M
**Combined Liquidity**: $48.41M

**Concentration Risk Distribution**:
- 🟢 Low: 13 tokens
- 🔴 Extreme: 9 tokens
- 🟡 High: 5 tokens
- 🟢 Medium: 3 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $271.90M | $46.04M | 🟢 unknown |
| 2 | HAROLD | Harold | $60.93K | $487.80K | 🟢 medium |
| 3 | DREAM | Dreamsync | $36.19K | $105.42K | 🟢 low |
| 4 | 1nu | 1nu | $29.81K | $38.46K | 🟢 low |
| 5 | LION | Loaded Lions | $24.10K | $1.38M | 🟢 low |
| 6 | RAGEGUY | Rage Guy | $5.74K | $87.44K | 🟢 low |
| 7 | 1 | 1 pill can change your life | $4.65K | $10.04K | 🟡 high |
| 8 | AI4 | AI⁴ | $2.58K | $73.47K | 🟢 low |
| 9 | AUSBAGWORK | AUSSIE BAG WORKERS | $1.65K | $13.62K | 🟡 high |
| 10 | SHITTER | SHITTERCOIN | $1.46K | $24.67K | 🟢 low |

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

**Total Historical Records**: 505
**Unique Tokens Tracked**: 101
**Date Range**: 2025-10-01 to 2025-11-11

**Master Aggregations**: 101 tokens
**Performance Metrics**: 505 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 505 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 101 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 505 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 31 |
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
