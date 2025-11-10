# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-11-10 22:23 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **31 tokens tracked** | 
💰 **$235.45M 24h volume** | 
💧 **$48.56M liquidity** | 
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
          3,
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
          -47.90786948176583,
          -47.90786948176583
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
      "LION",
      "HAROLD",
      "RAGEGUY",
      "1",
      "AI4",
      "1cat",
      "SOL",
      "SHITTER"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          150590.09,
          29651.1,
          29213.65,
          15044.48,
          7490.34,
          5978.61,
          2871.88,
          2340.4,
          2092.89,
          1768.87
        ],
        "backgroundColor": [
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#22c55e",
          "#eab308",
          "#22c55e",
          "#ef4444",
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
      "2025-11-10"
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
          33.23
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
          41.6
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
        "label": "HAROLD",
        "data": [
          0.0,
          0.0,
          0.0,
          61.9,
          61.92,
          62.0,
          64.39
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
          30.99
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
            "x": 711175.0,
            "y": 33.23,
            "r": 8,
            "label": "DREAM: $711,175 FDV, 33.2% concentration (low risk)"
          },
          {
            "x": 84403.0,
            "y": 41.6,
            "r": 8,
            "label": "1nu: $84,403 FDV, 41.6% concentration (low risk)"
          },
          {
            "x": 45602533.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $45,602,533 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 415568.0,
            "y": 30.99,
            "r": 8,
            "label": "RAGEGUY: $415,568 FDV, 31.0% concentration (low risk)"
          },
          {
            "x": 174133.0,
            "y": 55.14,
            "r": 8,
            "label": "AI4: $174,133 FDV, 55.1% concentration (low risk)"
          },
          {
            "x": 33677.0,
            "y": 54.22,
            "r": 8,
            "label": "SHITTER: $33,677 FDV, 54.2% concentration (low risk)"
          },
          {
            "x": 371526.0,
            "y": 36.93,
            "r": 8,
            "label": "FARTLESS: $371,526 FDV, 36.9% concentration (low risk)"
          },
          {
            "x": 896740.0,
            "y": 26.42,
            "r": 8,
            "label": "XBT: $896,740 FDV, 26.4% concentration (low risk)"
          },
          {
            "x": 683184.0,
            "y": 31.6,
            "r": 8,
            "label": "ELIZABETH: $683,184 FDV, 31.6% concentration (low risk)"
          },
          {
            "x": 86442.0,
            "y": 42.64,
            "r": 8,
            "label": "YAO: $86,442 FDV, 42.6% concentration (low risk)"
          },
          {
            "x": 126517.0,
            "y": 39.74,
            "r": 8,
            "label": "USDUT: $126,517 FDV, 39.7% concentration (low risk)"
          },
          {
            "x": 21709.0,
            "y": 27.46,
            "r": 8,
            "label": "FLY: $21,709 FDV, 27.5% concentration (low risk)"
          },
          {
            "x": 152703.0,
            "y": 47.18,
            "r": 8,
            "label": "gib: $152,703 FDV, 47.2% concentration (low risk)"
          },
          {
            "x": 98954.0,
            "y": 49.0,
            "r": 8,
            "label": "USEFUL: $98,954 FDV, 49.0% concentration (low risk)"
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
            "x": 3106847.0,
            "y": 64.39,
            "r": 8,
            "label": "HAROLD: $3,106,847 FDV, 64.4% concentration (medium risk)"
          },
          {
            "x": 10422.0,
            "y": 74.84,
            "r": 8,
            "label": "1: $10,422 FDV, 74.8% concentration (medium risk)"
          },
          {
            "x": 15142.0,
            "y": 65.85,
            "r": 8,
            "label": "$CrepSol: $15,142 FDV, 65.8% concentration (medium risk)"
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
            "x": 11389.0,
            "y": 91.06,
            "r": 8,
            "label": "AUSBAGWORK: $11,389 FDV, 91.1% concentration (high risk)"
          },
          {
            "x": 8334.0,
            "y": 83.27,
            "r": 8,
            "label": "1Bull: $8,334 FDV, 83.3% concentration (high risk)"
          },
          {
            "x": 5637.0,
            "y": 77.81,
            "r": 8,
            "label": "APOLLO: $5,637 FDV, 77.8% concentration (high risk)"
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
            "x": 12692845.0,
            "y": 96.8,
            "r": 8,
            "label": "SOL: $12,692,845 FDV, 96.8% concentration (extreme risk)"
          },
          {
            "x": 5424.0,
            "y": 95.21,
            "r": 8,
            "label": "1: $5,424 FDV, 95.2% concentration (extreme risk)"
          },
          {
            "x": 8902.0,
            "y": 94.22,
            "r": 8,
            "label": "MOCHI: $8,902 FDV, 94.2% concentration (extreme risk)"
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
            "x": 4307.0,
            "y": 98.73,
            "r": 8,
            "label": "REVIVE: $4,307 FDV, 98.7% concentration (extreme risk)"
          },
          {
            "x": 3584.0,
            "y": 97.37,
            "r": 8,
            "label": "Streamless: $3,584 FDV, 97.4% concentration (extreme risk)"
          },
          {
            "x": 3889.0,
            "y": 96.91,
            "r": 8,
            "label": "7: $3,889 FDV, 96.9% concentration (extreme risk)"
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
| 1 | XBT | XBT | 26.42% | 🟢 low | $116.04 | $414.31 |
| 2 | FLY | Nexa | 27.46% | 🟢 low | $1.65 | $2.55K |
| 3 | RAGEGUY | Rage Guy | 30.99% | 🟢 low | $7.49K | $90.65K |
| 4 | ELIZABETH | Just Elizabeth Cat | 31.60% | 🟢 low | $44.50 | $40.52 |
| 5 | DREAM | Dreamsync | 33.23% | 🟢 low | $150.59K | $106.60K |
| 6 | FARTLESS | FARTLESS COIN | 36.93% | 🟢 low | $409.08 | $2.55K |
| 7 | USDUT | unstable tether | 39.74% | 🟢 low | $1.68 | $39.81 |
| 8 | 1nu | 1nu | 41.60% | 🟢 low | $29.65K | $39.42K |
| 9 | YAO | YAO MING | 42.64% | 🟢 low | $7.13 | $570.88 |
| 10 | gib | gib | 47.18% | 🟢 low | $0.71 | $27.38 |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | 1cat | 1 cat can change your lif | 99.91% | 🔴 extreme | $2.34K | $0.00 |
| 2 | REVIVE | reviving the memes | 98.73% | 🔴 extreme | $1.92 | $8.44K |
| 3 | Hosico | Hosico Cat | 98.20% | 🔴 extreme | $4.03 | $6.43K |
| 4 | Streamless | Streamless coin | 97.37% | 🔴 extreme | $0.52 | $6.86K |
| 5 | 7 | 7 Coin | 96.91% | 🔴 extreme | $0.41 | $7.05K |
| 6 | SOL | Solana | 96.80% | 🔴 extreme | $2.09K | $13.77K |
| 7 | pibble | pibble | 96.60% | 🔴 extreme | $4.84 | $7.33K |
| 8 | 1 | 1 pill can change your li | 95.21% | 🔴 extreme | $656.54 | $8.81K |
| 9 | MOCHI | MOCHI CULT | 94.22% | 🔴 extreme | $12.93 | $15.57K |
| 10 | AUSBAGWORK | AUSSIE BAG WORKERS | 91.06% | 🟠 high | $1.52K | $14.13K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 31
**Combined 24h Volume**: $235.45M
**Combined Liquidity**: $48.56M

**Concentration Risk Distribution**:
- 🟢 Low: 14 tokens
- 🔴 Extreme: 9 tokens
- 🟢 Medium: 4 tokens
- 🟡 High: 3 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $235.20M | $46.22M | 🟢 unknown |
| 2 | DREAM | Dreamsync | $150.59K | $106.60K | 🟢 low |
| 3 | 1nu | 1nu | $29.65K | $39.42K | 🟢 low |
| 4 | LION | Loaded Lions | $29.21K | $1.38M | 🟢 low |
| 5 | HAROLD | Harold | $15.04K | $447.11K | 🟢 medium |
| 6 | RAGEGUY | Rage Guy | $7.49K | $90.65K | 🟢 low |
| 7 | 1 | 1 pill can change your life | $5.98K | $11.15K | 🟢 medium |
| 8 | AI4 | AI⁴ | $2.87K | $73.98K | 🟢 low |
| 9 | 1cat | 1 cat can change your life | $2.34K | $0.00 | 🔴 extreme |
| 10 | SOL | Solana | $2.09K | $13.77K | 🔴 extreme |

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

**Total Historical Records**: 505
**Unique Tokens Tracked**: 101
**Date Range**: 2025-10-01 to 2025-11-10

**Master Aggregations**: 101 tokens
**Performance Metrics**: 506 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 505 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 101 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 506 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 31 |
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
