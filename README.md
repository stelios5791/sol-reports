# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-11-05 08:45 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **31 tokens tracked** | 
💰 **$360.90M 24h volume** | 
💧 **$45.32M liquidity** | 
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
          4,
          10,
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
          -15.500685871056236,
          -15.500685871056236
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
      "AI4",
      "LION",
      "HAROLD",
      "RAGEGUY",
      "SHITTER",
      "SOL",
      "1",
      "1"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          89929.61,
          81412.4,
          63269.95,
          30537.42,
          28715.51,
          24580.4,
          4997.69,
          2199.68,
          1697.16,
          1206.99
        ],
        "backgroundColor": [
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#22c55e",
          "#eab308",
          "#ef4444",
          "#ef4444",
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
      "2025-11-05"
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
          33.14
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
          40.62
        ],
        "borderColor": "#ef4444",
        "backgroundColor": "#ef444420",
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
          53.61
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
        "label": "HAROLD",
        "data": [
          0.0,
          0.0,
          0.0,
          61.9,
          61.92,
          62.0,
          63.99
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
            "x": 674980.0,
            "y": 33.14,
            "r": 8,
            "label": "DREAM: $674,980 FDV, 33.1% concentration (low risk)"
          },
          {
            "x": 77473.0,
            "y": 40.62,
            "r": 8,
            "label": "1nu: $77,473 FDV, 40.6% concentration (low risk)"
          },
          {
            "x": 191514.0,
            "y": 53.61,
            "r": 8,
            "label": "AI4: $191,514 FDV, 53.6% concentration (low risk)"
          },
          {
            "x": 43207463.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $43,207,463 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 511200.0,
            "y": 29.38,
            "r": 8,
            "label": "RAGEGUY: $511,200 FDV, 29.4% concentration (low risk)"
          },
          {
            "x": 312926.0,
            "y": 37.63,
            "r": 8,
            "label": "FARTLESS: $312,926 FDV, 37.6% concentration (low risk)"
          },
          {
            "x": 953777.0,
            "y": 25.8,
            "r": 8,
            "label": "XBT: $953,777 FDV, 25.8% concentration (low risk)"
          },
          {
            "x": 61770.0,
            "y": 58.52,
            "r": 8,
            "label": "RUECAT: $61,770 FDV, 58.5% concentration (low risk)"
          },
          {
            "x": 358152.0,
            "y": 37.99,
            "r": 8,
            "label": "ELIZABETH: $358,152 FDV, 38.0% concentration (low risk)"
          },
          {
            "x": 15899.0,
            "y": 30.09,
            "r": 8,
            "label": "FLY: $15,899 FDV, 30.1% concentration (low risk)"
          },
          {
            "x": 117152.0,
            "y": 47.8,
            "r": 8,
            "label": "gib: $117,152 FDV, 47.8% concentration (low risk)"
          },
          {
            "x": 99637.0,
            "y": 48.61,
            "r": 8,
            "label": "USEFUL: $99,637 FDV, 48.6% concentration (low risk)"
          },
          {
            "x": 118360.0,
            "y": 40.06,
            "r": 8,
            "label": "USDUT: $118,360 FDV, 40.1% concentration (low risk)"
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
            "x": 2790191.0,
            "y": 63.99,
            "r": 8,
            "label": "HAROLD: $2,790,191 FDV, 64.0% concentration (medium risk)"
          },
          {
            "x": 27276.0,
            "y": 58.87,
            "r": 8,
            "label": "SHITTER: $27,276 FDV, 58.9% concentration (medium risk)"
          },
          {
            "x": 13991.0,
            "y": 65.35,
            "r": 8,
            "label": "$CrepSol: $13,991 FDV, 65.3% concentration (medium risk)"
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
            "x": 3589.0,
            "y": 81.15,
            "r": 8,
            "label": "APOLLO: $3,589 FDV, 81.2% concentration (high risk)"
          },
          {
            "x": 7697.0,
            "y": 81.06,
            "r": 8,
            "label": "1Bull: $7,697 FDV, 81.1% concentration (high risk)"
          },
          {
            "x": 10526.0,
            "y": 89.99,
            "r": 8,
            "label": "AUSBAGWORK: $10,526 FDV, 90.0% concentration (high risk)"
          },
          {
            "x": 6086.0,
            "y": 90.24,
            "r": 8,
            "label": "DARE: $6,086 FDV, 90.2% concentration (high risk)"
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
            "x": 13279145.0,
            "y": 96.8,
            "r": 8,
            "label": "SOL: $13,279,145 FDV, 96.8% concentration (extreme risk)"
          },
          {
            "x": 5100.0,
            "y": 95.67,
            "r": 8,
            "label": "1: $5,100 FDV, 95.7% concentration (extreme risk)"
          },
          {
            "x": 4312.0,
            "y": 97.28,
            "r": 8,
            "label": "1: $4,312 FDV, 97.3% concentration (extreme risk)"
          },
          {
            "x": 3326.0,
            "y": 98.97,
            "r": 8,
            "label": "1% Club: $3,326 FDV, 99.0% concentration (extreme risk)"
          },
          {
            "x": 3030.0,
            "y": 99.86,
            "r": 8,
            "label": "BONKZ: $3,030 FDV, 99.9% concentration (extreme risk)"
          },
          {
            "x": 8101.0,
            "y": 94.57,
            "r": 8,
            "label": "MOCHI: $8,101 FDV, 94.6% concentration (extreme risk)"
          },
          {
            "x": 4098.0,
            "y": 96.67,
            "r": 8,
            "label": "RWA: $4,098 FDV, 96.7% concentration (extreme risk)"
          },
          {
            "x": 2802.0,
            "y": 99.39,
            "r": 8,
            "label": "MMGA: $2,802 FDV, 99.4% concentration (extreme risk)"
          },
          {
            "x": 3000.0,
            "y": 99.19,
            "r": 8,
            "label": "SLOW: $3,000 FDV, 99.2% concentration (extreme risk)"
          },
          {
            "x": 4519.54,
            "y": 100.0,
            "r": 8,
            "label": "YOU: $4,520 FDV, 100.0% concentration (extreme risk)"
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
| 1 | XBT | XBT | 25.80% | 🟢 low | $286.24 | $417.64 |
| 2 | RAGEGUY | Rage Guy | 29.38% | 🟢 low | $24.58K | $96.98K |
| 3 | FLY | Nexa | 30.09% | 🟢 low | $4.21 | $5.22K |
| 4 | DREAM | Dreamsync | 33.14% | 🟢 low | $89.93K | $99.80K |
| 5 | FARTLESS | FARTLESS COIN | 37.63% | 🟢 low | $432.62 | $2.33K |
| 6 | ELIZABETH | Just Elizabeth Cat | 37.99% | 🟢 low | $6.82 | $29.34 |
| 7 | USDUT | unstable tether | 40.06% | 🟢 low | $0.58 | $35.61 |
| 8 | 1nu | 1nu | 40.62% | 🟢 low | $81.41K | $37.13K |
| 9 | gib | gib | 47.80% | 🟢 low | $3.03 | $23.98 |
| 10 | USEFUL | USEFUL COIN | 48.61% | 🟢 low | $1.17 | $32.23 |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | YOU | YOU can change your life. | 100.00% | 🔴 extreme | $0.00 | $0.00 |
| 2 | BONKZ | Bonkzilla | 99.86% | 🔴 extreme | $136.04 | $5.66K |
| 3 | MMGA | MAKE MEMES GREAT AGAIN | 99.39% | 🔴 extreme | $4.56 | $5.52K |
| 4 | SLOW | Slow Runner | 99.19% | 🔴 extreme | $0.10 | $5.93K |
| 5 | 1% Club | The 1% Club | 98.97% | 🔴 extreme | $141.35 | $6.06K |
| 6 | 1 | 1 pill can change your li | 97.28% | 🔴 extreme | $1.21K | $6.98K |
| 7 | SOL | Solana | 96.80% | 🔴 extreme | $2.20K | $9.02K |
| 8 | RWA | Real World Asses | 96.67% | 🔴 extreme | $71.01 | $7.20K |
| 9 | 1 | 1 pill can change your li | 95.67% | 🔴 extreme | $1.70K | $8.33K |
| 10 | MOCHI | MOCHI CULT | 94.57% | 🔴 extreme | $71.59 | $14.26K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 31
**Combined 24h Volume**: $360.90M
**Combined Liquidity**: $45.32M

**Concentration Risk Distribution**:
- 🟢 Low: 13 tokens
- 🔴 Extreme: 10 tokens
- 🟡 High: 4 tokens
- 🟢 Medium: 3 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $360.57M | $43.12M | 🟢 unknown |
| 2 | DREAM | Dreamsync | $89.93K | $99.80K | 🟢 low |
| 3 | 1nu | 1nu | $81.41K | $37.13K | 🟢 low |
| 4 | AI4 | AI⁴ | $63.27K | $75.03K | 🟢 low |
| 5 | LION | Loaded Lions | $30.54K | $1.30M | 🟢 low |
| 6 | HAROLD | Harold | $28.72K | $407.97K | 🟢 medium |
| 7 | RAGEGUY | Rage Guy | $24.58K | $96.98K | 🟢 low |
| 8 | SHITTER | SHITTERCOIN | $5.00K | $22.83K | 🟢 medium |
| 9 | SOL | Solana | $2.20K | $9.02K | 🔴 extreme |
| 10 | 1 | 1 pill can change your life | $1.70K | $8.33K | 🔴 extreme |

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
**Date Range**: 2025-10-01 to 2025-11-05

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
