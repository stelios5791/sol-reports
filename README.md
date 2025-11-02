# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-11-02 08:33 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **29 tokens tracked** | 
💰 **$108.75M 24h volume** | 
💧 **$70.08M liquidity** | 
🟢 **11 low-risk tokens**

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
          11,
          3,
          6,
          8,
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
          -14.423375815977609,
          -14.423375815977609
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
      "DREAM",
      "1nu",
      "RAGEGUY",
      "LION",
      "SOL",
      "HAROLD",
      "Hosico",
      "RUECAT",
      "SHITTER"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          52354.1,
          30520.16,
          23821.14,
          14932.04,
          5916.24,
          1829.46,
          1724.56,
          1106.25,
          649.89,
          636.76
        ],
        "backgroundColor": [
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#ef4444",
          "#eab308",
          "#ef4444",
          "#22c55e",
          "#eab308"
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
          51.22
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
          33.44
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
          45.01
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
          29.9
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
            "x": 266553.0,
            "y": 51.22,
            "r": 8,
            "label": "AI4: $266,553 FDV, 51.2% concentration (low risk)"
          },
          {
            "x": 752805.0,
            "y": 33.44,
            "r": 8,
            "label": "DREAM: $752,805 FDV, 33.4% concentration (low risk)"
          },
          {
            "x": 69250.0,
            "y": 45.01,
            "r": 8,
            "label": "1nu: $69,250 FDV, 45.0% concentration (low risk)"
          },
          {
            "x": 565919.0,
            "y": 29.9,
            "r": 8,
            "label": "RAGEGUY: $565,919 FDV, 29.9% concentration (low risk)"
          },
          {
            "x": 53804850.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $53,804,850 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 71255.0,
            "y": 59.22,
            "r": 8,
            "label": "RUECAT: $71,255 FDV, 59.2% concentration (low risk)"
          },
          {
            "x": 1020935.0,
            "y": 24.87,
            "r": 8,
            "label": "XBT: $1,020,935 FDV, 24.9% concentration (low risk)"
          },
          {
            "x": 454549.0,
            "y": 36.72,
            "r": 8,
            "label": "FARTLESS: $454,549 FDV, 36.7% concentration (low risk)"
          },
          {
            "x": 18554.0,
            "y": 30.07,
            "r": 8,
            "label": "FLY: $18,554 FDV, 30.1% concentration (low risk)"
          },
          {
            "x": 410884.0,
            "y": 35.29,
            "r": 8,
            "label": "ELIZABETH: $410,884 FDV, 35.3% concentration (low risk)"
          },
          {
            "x": 144968.0,
            "y": 39.55,
            "r": 8,
            "label": "USDUT: $144,968 FDV, 39.5% concentration (low risk)"
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
            "x": 3306198.0,
            "y": 63.79,
            "r": 8,
            "label": "HAROLD: $3,306,198 FDV, 63.8% concentration (medium risk)"
          },
          {
            "x": 22704.0,
            "y": 63.48,
            "r": 8,
            "label": "SHITTER: $22,704 FDV, 63.5% concentration (medium risk)"
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
            "x": 6433.0,
            "y": 93.24,
            "r": 8,
            "label": "1: $6,433 FDV, 93.2% concentration (high risk)"
          },
          {
            "x": 12479.0,
            "y": 90.3,
            "r": 8,
            "label": "AUSBAGWORK: $12,479 FDV, 90.3% concentration (high risk)"
          },
          {
            "x": 9636.0,
            "y": 80.12,
            "r": 8,
            "label": "1Bull: $9,636 FDV, 80.1% concentration (high risk)"
          },
          {
            "x": 5731.0,
            "y": 92.01,
            "r": 8,
            "label": "FARTWORM: $5,731 FDV, 92.0% concentration (high risk)"
          },
          {
            "x": 8138.0,
            "y": 92.85,
            "r": 8,
            "label": "IDIOT: $8,138 FDV, 92.8% concentration (high risk)"
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
            "x": 16628010.0,
            "y": 96.8,
            "r": 8,
            "label": "SOL: $16,628,010 FDV, 96.8% concentration (extreme risk)"
          },
          {
            "x": 5120.0,
            "y": 97.29,
            "r": 8,
            "label": "Hosico: $5,120 FDV, 97.3% concentration (extreme risk)"
          },
          {
            "x": 5502.0,
            "y": 95.92,
            "r": 8,
            "label": "1: $5,502 FDV, 95.9% concentration (extreme risk)"
          },
          {
            "x": 3987.0,
            "y": 98.04,
            "r": 8,
            "label": "viewer: $3,987 FDV, 98.0% concentration (extreme risk)"
          },
          {
            "x": 4460.0,
            "y": 96.28,
            "r": 8,
            "label": "pibble: $4,460 FDV, 96.3% concentration (extreme risk)"
          },
          {
            "x": 3913.0,
            "y": 99.5,
            "r": 8,
            "label": "MoneyBear: $3,913 FDV, 99.5% concentration (extreme risk)"
          },
          {
            "x": 10039.0,
            "y": 93.86,
            "r": 8,
            "label": "MOCHI: $10,039 FDV, 93.9% concentration (extreme risk)"
          },
          {
            "x": 4549.0,
            "y": 97.59,
            "r": 8,
            "label": "BULLCOIN: $4,549 FDV, 97.6% concentration (extreme risk)"
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
| 1 | XBT | XBT | 24.87% | 🟢 low | $634.08 | $2.97K |
| 2 | RAGEGUY | Rage Guy | 29.90% | 🟢 low | $14.93K | $112.32K |
| 3 | FLY | Nexa | 30.07% | 🟢 low | $48.05 | $6.29K |
| 4 | DREAM | Dreamsync | 33.44% | 🟢 low | $30.52K | $115.89K |
| 5 | ELIZABETH | Just Elizabeth Cat | 35.29% | 🟢 low | $2.53 | $31.42 |
| 6 | FARTLESS | FARTLESS COIN | 36.72% | 🟢 low | $245.18 | $2.80K |
| 7 | USDUT | unstable tether | 39.55% | 🟢 low | $0.39 | $42.90 |
| 8 | 1nu | 1nu | 45.01% | 🟢 low | $23.82K | $34.88K |
| 9 | AI4 | AI⁴ | 51.22% | 🟢 low | $52.35K | $96.66K |
| 10 | LION | Loaded Lions | 57.84% | 🟢 low | $5.92K | $1.60M |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | MoneyBear | The Money Bears | 99.50% | 🔴 extreme | $4.06 | $7.76K |
| 2 | viewer | in a streamers world | 98.04% | 🔴 extreme | $4.46 | $7.65K |
| 3 | BULLCOIN | BULLCOIN | 97.59% | 🔴 extreme | $0.42 | $7.89K |
| 4 | Hosico | Hosico Cat | 97.29% | 🔴 extreme | $1.11K | $8.19K |
| 5 | SOL | Solana | 96.80% | 🔴 extreme | $1.83K | $16.74K |
| 6 | pibble | pibble | 96.28% | 🔴 extreme | $4.29 | $7.38K |
| 7 | 1 | 1 pill can change your li | 95.92% | 🔴 extreme | $546.48 | $9.43K |
| 8 | MOCHI | MOCHI CULT | 93.86% | 🔴 extreme | $2.84 | $17.52K |
| 9 | 1 | 1 pill can change your li | 93.24% | 🟠 high | $557.71 | $9.24K |
| 10 | IDIOT | IDIOT | 92.85% | 🟠 high | $2.36 | $11.49K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 29
**Combined 24h Volume**: $108.75M
**Combined Liquidity**: $70.08M

**Concentration Risk Distribution**:
- 🟢 Low: 11 tokens
- 🔴 Extreme: 8 tokens
- 🟡 High: 6 tokens
- 🟢 Medium: 3 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $108.62M | $67.40M | 🟢 unknown |
| 2 | AI4 | AI⁴ | $52.35K | $96.66K | 🟢 low |
| 3 | DREAM | Dreamsync | $30.52K | $115.89K | 🟢 low |
| 4 | 1nu | 1nu | $23.82K | $34.88K | 🟢 low |
| 5 | RAGEGUY | Rage Guy | $14.93K | $112.32K | 🟢 low |
| 6 | LION | Loaded Lions | $5.92K | $1.60M | 🟢 low |
| 7 | SOL | Solana | $1.83K | $16.74K | 🔴 extreme |
| 8 | HAROLD | Harold | $1.72K | $489.55K | 🟢 medium |
| 9 | Hosico | Hosico Cat | $1.11K | $8.19K | 🔴 extreme |
| 10 | RUECAT | Rue Cat | $649.89 | $36.70K | 🟢 low |

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

**Total Historical Records**: 503
**Unique Tokens Tracked**: 101
**Date Range**: 2025-10-01 to 2025-11-02

**Master Aggregations**: 101 tokens
**Performance Metrics**: 503 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 503 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 101 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 503 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 29 |
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
