# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-11-05 19:25 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **35 tokens tracked** | 
💰 **$303.15M 24h volume** | 
💧 **$47.35M liquidity** | 
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
          7,
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
          -72.02309468822172,
          -72.02309468822172
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
      "1nu",
      "1",
      "LION",
      "AI4",
      "HAROLD",
      "1",
      "RAGEGUY",
      "SHITTER",
      "DREAM",
      "pibble"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          326278.3,
          199189.61,
          26710.62,
          25603.67,
          24244.28,
          13904.73,
          12492.28,
          9876.66,
          9414.29,
          3575.44
        ],
        "backgroundColor": [
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#f97316",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#f97316"
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
      "2025-10-02",
      "2025-10-03",
      "2025-10-04",
      "2025-10-05",
      "2025-10-06",
      "2025-10-07",
      "2025-11-05"
    ],
    "datasets": [
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
          37.21
        ],
        "borderColor": "#3b82f6",
        "backgroundColor": "#3b82f620",
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
          59.65,
          93.73
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
        "label": "AI4",
        "data": [
          0.0,
          0.0,
          0.0,
          50.98,
          50.56,
          52.53,
          54.25
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
          64.03
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
            "x": 130710.0,
            "y": 37.21,
            "r": 8,
            "label": "1nu: $130,710 FDV, 37.2% concentration (low risk)"
          },
          {
            "x": 21650.0,
            "y": 59.65,
            "r": 8,
            "label": "1: $21,650 FDV, 59.6% concentration (low risk)"
          },
          {
            "x": 44211989.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $44,211,989 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 193025.0,
            "y": 54.25,
            "r": 8,
            "label": "AI4: $193,025 FDV, 54.2% concentration (low risk)"
          },
          {
            "x": 505197.0,
            "y": 29.74,
            "r": 8,
            "label": "RAGEGUY: $505,197 FDV, 29.7% concentration (low risk)"
          },
          {
            "x": 32206.0,
            "y": 54.93,
            "r": 8,
            "label": "SHITTER: $32,206 FDV, 54.9% concentration (low risk)"
          },
          {
            "x": 708359.0,
            "y": 33.15,
            "r": 8,
            "label": "DREAM: $708,359 FDV, 33.1% concentration (low risk)"
          },
          {
            "x": 410230.0,
            "y": 36.18,
            "r": 8,
            "label": "FARTLESS: $410,230 FDV, 36.2% concentration (low risk)"
          },
          {
            "x": 64600.0,
            "y": 59.8,
            "r": 8,
            "label": "RUECAT: $64,600 FDV, 59.8% concentration (low risk)"
          },
          {
            "x": 18207.0,
            "y": 28.94,
            "r": 8,
            "label": "FLY: $18,207 FDV, 28.9% concentration (low risk)"
          },
          {
            "x": 1026023.0,
            "y": 25.33,
            "r": 8,
            "label": "XBT: $1,026,023 FDV, 25.3% concentration (low risk)"
          },
          {
            "x": 329807.0,
            "y": 38.1,
            "r": 8,
            "label": "ELIZABETH: $329,807 FDV, 38.1% concentration (low risk)"
          },
          {
            "x": 116249.0,
            "y": 41.57,
            "r": 8,
            "label": "USDUT: $116,249 FDV, 41.6% concentration (low risk)"
          },
          {
            "x": 120000.0,
            "y": 46.49,
            "r": 8,
            "label": "gib: $120,000 FDV, 46.5% concentration (low risk)"
          },
          {
            "x": 100154.0,
            "y": 47.82,
            "r": 8,
            "label": "USEFUL: $100,154 FDV, 47.8% concentration (low risk)"
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
            "x": 2944189.0,
            "y": 64.03,
            "r": 8,
            "label": "HAROLD: $2,944,189 FDV, 64.0% concentration (medium risk)"
          },
          {
            "x": 14797.0,
            "y": 65.49,
            "r": 8,
            "label": "$CrepSol: $14,797 FDV, 65.5% concentration (medium risk)"
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
            "x": 6053.0,
            "y": 93.73,
            "r": 8,
            "label": "1: $6,053 FDV, 93.7% concentration (high risk)"
          },
          {
            "x": 5222.0,
            "y": 93.56,
            "r": 8,
            "label": "pibble: $5,222 FDV, 93.6% concentration (high risk)"
          },
          {
            "x": 4840.0,
            "y": 94.24,
            "r": 8,
            "label": "RWA: $4,840 FDV, 94.2% concentration (high risk)"
          },
          {
            "x": 8551.0,
            "y": 80.04,
            "r": 8,
            "label": "1Bull: $8,551 FDV, 80.0% concentration (high risk)"
          },
          {
            "x": 3277.0,
            "y": 80.87,
            "r": 8,
            "label": "APOLLO: $3,277 FDV, 80.9% concentration (high risk)"
          },
          {
            "x": 10526.0,
            "y": 89.99,
            "r": 8,
            "label": "AUSBAGWORK: $10,526 FDV, 90.0% concentration (high risk)"
          },
          {
            "x": 6181.0,
            "y": 90.25,
            "r": 8,
            "label": "DARE: $6,181 FDV, 90.2% concentration (high risk)"
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
            "x": 13876621.0,
            "y": 96.8,
            "r": 8,
            "label": "SOL: $13,876,621 FDV, 96.8% concentration (extreme risk)"
          },
          {
            "x": 3439.0,
            "y": 98.87,
            "r": 8,
            "label": "1% Club: $3,439 FDV, 98.9% concentration (extreme risk)"
          },
          {
            "x": 4685.75,
            "y": 99.9,
            "r": 8,
            "label": "1cat: $4,686 FDV, 99.9% concentration (extreme risk)"
          },
          {
            "x": 3471.0,
            "y": 97.12,
            "r": 8,
            "label": "Streamless: $3,471 FDV, 97.1% concentration (extreme risk)"
          },
          {
            "x": 2987.0,
            "y": 99.39,
            "r": 8,
            "label": "MMGA: $2,987 FDV, 99.4% concentration (extreme risk)"
          },
          {
            "x": 3030.0,
            "y": 99.86,
            "r": 8,
            "label": "BONKZ: $3,030 FDV, 99.9% concentration (extreme risk)"
          },
          {
            "x": 8247.0,
            "y": 94.57,
            "r": 8,
            "label": "MOCHI: $8,247 FDV, 94.6% concentration (extreme risk)"
          },
          {
            "x": 3557.0,
            "y": 97.61,
            "r": 8,
            "label": "obvious: $3,557 FDV, 97.6% concentration (extreme risk)"
          },
          {
            "x": 3175.0,
            "y": 99.24,
            "r": 8,
            "label": "SLOW: $3,175 FDV, 99.2% concentration (extreme risk)"
          },
          {
            "x": 3272.0,
            "y": 97.85,
            "r": 8,
            "label": "BLUB: $3,272 FDV, 97.8% concentration (extreme risk)"
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
| 1 | XBT | XBT | 25.33% | 🟢 low | $25.40 | $440.72 |
| 2 | FLY | Nexa | 28.94% | 🟢 low | $49.35 | $133.27 |
| 3 | RAGEGUY | Rage Guy | 29.74% | 🟢 low | $12.49K | $99.08K |
| 4 | DREAM | Dreamsync | 33.15% | 🟢 low | $9.41K | $104.92K |
| 5 | FARTLESS | FARTLESS COIN | 36.18% | 🟢 low | $513.42 | $2.67K |
| 6 | 1nu | 1nu | 37.21% | 🟢 low | $326.28K | $48.61K |
| 7 | ELIZABETH | Just Elizabeth Cat | 38.10% | 🟢 low | $5.48 | $28.16 |
| 8 | USDUT | unstable tether | 41.57% | 🟢 low | $1.57 | $37.42 |
| 9 | gib | gib | 46.49% | 🟢 low | $0.71 | $24.27 |
| 10 | USEFUL | USEFUL COIN | 47.82% | 🟢 low | $0.62 | $33.88 |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | 1cat | 1 cat can change your lif | 99.90% | 🔴 extreme | $308.45 | $0.00 |
| 2 | BONKZ | Bonkzilla | 99.86% | 🔴 extreme | $136.04 | $5.66K |
| 3 | MMGA | MAKE MEMES GREAT AGAIN | 99.39% | 🔴 extreme | $157.60 | $5.81K |
| 4 | SLOW | Slow Runner | 99.24% | 🔴 extreme | $2.48 | $6.28K |
| 5 | 1% Club | The 1% Club | 98.87% | 🔴 extreme | $1.64K | $6.17K |
| 6 | BLUB | Blub | 97.85% | 🔴 extreme | $0.50 | $6.29K |
| 7 | obvious | in hindsight | 97.61% | 🔴 extreme | $4.03 | $6.41K |
| 8 | Streamless | Streamless coin | 97.12% | 🔴 extreme | $265.99 | $6.62K |
| 9 | SOL | Solana | 96.80% | 🔴 extreme | $2.51K | $14.23K |
| 10 | MOCHI | MOCHI CULT | 94.57% | 🔴 extreme | $71.80 | $14.51K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 35
**Combined 24h Volume**: $303.15M
**Combined Liquidity**: $47.35M

**Concentration Risk Distribution**:
- 🟢 Low: 15 tokens
- 🔴 Extreme: 10 tokens
- 🟡 High: 7 tokens
- 🟢 Medium: 2 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $302.49M | $45.02M | 🟢 unknown |
| 2 | 1nu | 1nu | $326.28K | $48.61K | 🟢 low |
| 3 | 1 | 1 pill can change your life | $199.19K | $15.94K | 🟢 low |
| 4 | LION | Loaded Lions | $26.71K | $1.35M | 🟢 low |
| 5 | AI4 | AI⁴ | $25.60K | $77.13K | 🟢 low |
| 6 | HAROLD | Harold | $24.24K | $430.10K | 🟢 medium |
| 7 | 1 | 1 pill can change your life | $13.90K | $9.25K | 🟡 high |
| 8 | RAGEGUY | Rage Guy | $12.49K | $99.08K | 🟢 low |
| 9 | SHITTER | SHITTERCOIN | $9.88K | $24.56K | 🟢 low |
| 10 | DREAM | Dreamsync | $9.41K | $104.92K | 🟢 low |

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
- 👀 **Watch**: 120 tokens
- 🚀 **Breakout**: 4 tokens
- ❄️ **Cooling**: 1 tokens

### 🚀 Breakout Signals

| Symbol | Score | Vol 3v1 | Z-Score Vol | Liq 3d | Streak |
|--------|-------|---------|-------------|--------|--------|
| HAROLD | 536.03 | 2.18x | 1.75 | $525.98K | 1d |
| wSOL | 4.24 | 2.51x | 1.69 | $57.82M | 0d |
| XBT | 3.65 | 2.10x | 1.74 | $421.14K | 0d |
| USDUT | 3.57 | 2.36x | 1.51 | $150.84K | 0d |

### 👀 Watch List

*120 tokens showing elevated activity*

📄 [Full data: signals_filtered.csv](data/signals_filtered.csv)

---

## 📈 Historical Data

**Total Historical Records**: 509
**Unique Tokens Tracked**: 101
**Date Range**: 2025-10-01 to 2025-11-05

**Master Aggregations**: 101 tokens
**Performance Metrics**: 509 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 509 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 101 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 509 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 35 |
| [new_viable.csv](data/new_viable.csv) | New tokens with potential | 0 |
| [signals_filtered.csv](data/signals_filtered.csv) | Whale-filtered trading signals | 125 |

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
