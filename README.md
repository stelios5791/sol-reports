# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-11-10 08:41 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **32 tokens tracked** | 
💰 **$206.81M 24h volume** | 
💧 **$48.07M liquidity** | 
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
          4,
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
          -49.2193675889328,
          -49.2193675889328
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
      "LION",
      "1nu",
      "1",
      "HAROLD",
      "RAGEGUY",
      "SOL",
      "AI4",
      "$CrepSol",
      "1cat"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          240746.32,
          22441.67,
          20871.21,
          11190.4,
          9067.75,
          8368.22,
          3169.3,
          2915.25,
          1557.39,
          1086.99
        ],
        "backgroundColor": [
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#eab308",
          "#22c55e",
          "#ef4444",
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
          33.17
        ],
        "borderColor": "#3b82f6",
        "backgroundColor": "#3b82f620",
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
          40.08
        ],
        "borderColor": "#22c55e",
        "backgroundColor": "#22c55e20",
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
          74.19,
          95.55
        ],
        "borderColor": "#eab308",
        "backgroundColor": "#eab30820",
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
          64.18
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
            "x": 729577.0,
            "y": 33.17,
            "r": 8,
            "label": "DREAM: $729,577 FDV, 33.2% concentration (low risk)"
          },
          {
            "x": 45600909.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $45,600,909 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 96265.0,
            "y": 40.08,
            "r": 8,
            "label": "1nu: $96,265 FDV, 40.1% concentration (low risk)"
          },
          {
            "x": 393875.0,
            "y": 31.11,
            "r": 8,
            "label": "RAGEGUY: $393,875 FDV, 31.1% concentration (low risk)"
          },
          {
            "x": 188783.0,
            "y": 54.48,
            "r": 8,
            "label": "AI4: $188,783 FDV, 54.5% concentration (low risk)"
          },
          {
            "x": 29828.0,
            "y": 56.85,
            "r": 8,
            "label": "SHITTER: $29,828 FDV, 56.9% concentration (low risk)"
          },
          {
            "x": 397155.0,
            "y": 36.45,
            "r": 8,
            "label": "FARTLESS: $397,155 FDV, 36.5% concentration (low risk)"
          },
          {
            "x": 1028627.0,
            "y": 25.53,
            "r": 8,
            "label": "XBT: $1,028,627 FDV, 25.5% concentration (low risk)"
          },
          {
            "x": 585302.0,
            "y": 32.4,
            "r": 8,
            "label": "ELIZABETH: $585,302 FDV, 32.4% concentration (low risk)"
          },
          {
            "x": 88326.0,
            "y": 42.46,
            "r": 8,
            "label": "YAO: $88,326 FDV, 42.5% concentration (low risk)"
          },
          {
            "x": 152703.0,
            "y": 47.33,
            "r": 8,
            "label": "gib: $152,703 FDV, 47.3% concentration (low risk)"
          },
          {
            "x": 105466.0,
            "y": 48.99,
            "r": 8,
            "label": "USEFUL: $105,466 FDV, 49.0% concentration (low risk)"
          },
          {
            "x": 21346.0,
            "y": 27.46,
            "r": 8,
            "label": "FLY: $21,346 FDV, 27.5% concentration (low risk)"
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
            "x": 10119.0,
            "y": 74.19,
            "r": 8,
            "label": "1: $10,119 FDV, 74.2% concentration (medium risk)"
          },
          {
            "x": 3272597.0,
            "y": 64.18,
            "r": 8,
            "label": "HAROLD: $3,272,597 FDV, 64.2% concentration (medium risk)"
          },
          {
            "x": 15324.0,
            "y": 65.57,
            "r": 8,
            "label": "$CrepSol: $15,324 FDV, 65.6% concentration (medium risk)"
          },
          {
            "x": 64361.0,
            "y": 61.56,
            "r": 8,
            "label": "RUECAT: $64,361 FDV, 61.6% concentration (medium risk)"
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
            "x": 5474.0,
            "y": 77.78,
            "r": 8,
            "label": "APOLLO: $5,474 FDV, 77.8% concentration (high risk)"
          },
          {
            "x": 6995.0,
            "y": 92.88,
            "r": 8,
            "label": "IDIOT: $6,995 FDV, 92.9% concentration (high risk)"
          },
          {
            "x": 8476.0,
            "y": 82.24,
            "r": 8,
            "label": "1Bull: $8,476 FDV, 82.2% concentration (high risk)"
          },
          {
            "x": 4942.0,
            "y": 92.26,
            "r": 8,
            "label": "FARTWORM: $4,942 FDV, 92.3% concentration (high risk)"
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
            "x": 12756660.0,
            "y": 96.8,
            "r": 8,
            "label": "SOL: $12,756,660 FDV, 96.8% concentration (extreme risk)"
          },
          {
            "x": 4846.94,
            "y": 99.9,
            "r": 8,
            "label": "1cat: $4,847 FDV, 99.9% concentration (extreme risk)"
          },
          {
            "x": 4396.0,
            "y": 96.49,
            "r": 8,
            "label": "pibble: $4,396 FDV, 96.5% concentration (extreme risk)"
          },
          {
            "x": 5135.0,
            "y": 95.55,
            "r": 8,
            "label": "1: $5,135 FDV, 95.5% concentration (extreme risk)"
          },
          {
            "x": 3518.0,
            "y": 97.9,
            "r": 8,
            "label": "Bagwork: $3,518 FDV, 97.9% concentration (extreme risk)"
          },
          {
            "x": 8876.0,
            "y": 94.21,
            "r": 8,
            "label": "MOCHI: $8,876 FDV, 94.2% concentration (extreme risk)"
          },
          {
            "x": 3466.0,
            "y": 98.11,
            "r": 8,
            "label": "Hosico: $3,466 FDV, 98.1% concentration (extreme risk)"
          },
          {
            "x": 3889.0,
            "y": 96.91,
            "r": 8,
            "label": "7: $3,889 FDV, 96.9% concentration (extreme risk)"
          },
          {
            "x": 3331.0,
            "y": 98.98,
            "r": 8,
            "label": "1% Club: $3,331 FDV, 99.0% concentration (extreme risk)"
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
| 1 | XBT | XBT | 25.53% | 🟢 low | $168.47 | $448.63 |
| 2 | FLY | Nexa | 27.46% | 🟢 low | $1.38 | $2.50K |
| 3 | RAGEGUY | Rage Guy | 31.11% | 🟢 low | $8.37K | $88.72K |
| 4 | ELIZABETH | Just Elizabeth Cat | 32.40% | 🟢 low | $49.34 | $37.51 |
| 5 | DREAM | Dreamsync | 33.17% | 🟢 low | $240.75K | $108.10K |
| 6 | FARTLESS | FARTLESS COIN | 36.45% | 🟢 low | $513.89 | $2.63K |
| 7 | 1nu | 1nu | 40.08% | 🟢 low | $20.87K | $42.05K |
| 8 | YAO | YAO MING | 42.46% | 🟢 low | $5.87 | $585.90 |
| 9 | gib | gib | 47.33% | 🟢 low | $1.74 | $27.38 |
| 10 | USEFUL | USEFUL COIN | 48.99% | 🟢 low | $1.44 | $38.66 |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | 1cat | 1 cat can change your lif | 99.90% | 🔴 extreme | $1.09K | $0.00 |
| 2 | 1% Club | The 1% Club | 98.98% | 🔴 extreme | $0.21 | $6.07K |
| 3 | Hosico | Hosico Cat | 98.11% | 🔴 extreme | $0.70 | $6.40K |
| 4 | Bagwork | African Bagwork | 97.90% | 🔴 extreme | $9.30 | $6.72K |
| 5 | 7 | 7 Coin | 96.91% | 🔴 extreme | $0.41 | $7.05K |
| 6 | SOL | Solana | 96.80% | 🔴 extreme | $3.17K | $13.84K |
| 7 | pibble | pibble | 96.49% | 🔴 extreme | $223.91 | $7.34K |
| 8 | 1 | 1 pill can change your li | 95.55% | 🔴 extreme | $206.94 | $8.58K |
| 9 | MOCHI | MOCHI CULT | 94.21% | 🔴 extreme | $2.34 | $15.53K |
| 10 | IDIOT | IDIOT | 92.88% | 🟠 high | $1.68 | $9.88K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 32
**Combined 24h Volume**: $206.81M
**Combined Liquidity**: $48.07M

**Concentration Risk Distribution**:
- 🟢 Low: 13 tokens
- 🔴 Extreme: 9 tokens
- 🟡 High: 5 tokens
- 🟢 Medium: 4 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $206.48M | $45.70M | 🟢 unknown |
| 2 | DREAM | Dreamsync | $240.75K | $108.10K | 🟢 low |
| 3 | LION | Loaded Lions | $22.44K | $1.39M | 🟢 low |
| 4 | 1nu | 1nu | $20.87K | $42.05K | 🟢 low |
| 5 | 1 | 1 pill can change your life | $11.19K | $11.05K | 🟢 medium |
| 6 | HAROLD | Harold | $9.07K | $460.19K | 🟢 medium |
| 7 | RAGEGUY | Rage Guy | $8.37K | $88.72K | 🟢 low |
| 8 | SOL | Solana | $3.17K | $13.84K | 🔴 extreme |
| 9 | AI4 | AI⁴ | $2.92K | $77.28K | 🟢 low |
| 10 | $CrepSol | Crepe on Solana | $1.56K | $13.50K | 🟢 medium |

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

**Total Historical Records**: 506
**Unique Tokens Tracked**: 101
**Date Range**: 2025-10-01 to 2025-11-10

**Master Aggregations**: 101 tokens
**Performance Metrics**: 510 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 506 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 101 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 510 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 32 |
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
