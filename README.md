# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-11-05 21:29 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **35 tokens tracked** | 
💰 **$278.43M 24h volume** | 
💧 **$47.03M liquidity** | 
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
          3,
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
          -49.721995094031065,
          -49.721995094031065
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
      "HAROLD",
      "LION",
      "AI4",
      "1",
      "RAGEGUY",
      "DREAM",
      "SHITTER",
      "pibble"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          339779.05,
          214099.55,
          51747.38,
          24068.96,
          20450.04,
          14479.62,
          12108.04,
          10528.36,
          10022.05,
          3575.44
        ],
        "backgroundColor": [
          "#22c55e",
          "#eab308",
          "#eab308",
          "#22c55e",
          "#22c55e",
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
          37.9
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
          72.03,
          92.82
        ],
        "borderColor": "#ef4444",
        "backgroundColor": "#ef444420",
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
          63.96
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
            "x": 121783.0,
            "y": 37.9,
            "r": 8,
            "label": "1nu: $121,783 FDV, 37.9% concentration (low risk)"
          },
          {
            "x": 44095225.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $44,095,225 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 193025.0,
            "y": 54.25,
            "r": 8,
            "label": "AI4: $193,025 FDV, 54.2% concentration (low risk)"
          },
          {
            "x": 510969.0,
            "y": 29.72,
            "r": 8,
            "label": "RAGEGUY: $510,969 FDV, 29.7% concentration (low risk)"
          },
          {
            "x": 704479.0,
            "y": 33.15,
            "r": 8,
            "label": "DREAM: $704,479 FDV, 33.1% concentration (low risk)"
          },
          {
            "x": 31596.0,
            "y": 55.34,
            "r": 8,
            "label": "SHITTER: $31,596 FDV, 55.3% concentration (low risk)"
          },
          {
            "x": 393130.0,
            "y": 36.49,
            "r": 8,
            "label": "FARTLESS: $393,130 FDV, 36.5% concentration (low risk)"
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
            "y": 25.5,
            "r": 8,
            "label": "XBT: $1,026,023 FDV, 25.5% concentration (low risk)"
          },
          {
            "x": 331286.0,
            "y": 37.72,
            "r": 8,
            "label": "ELIZABETH: $331,286 FDV, 37.7% concentration (low risk)"
          },
          {
            "x": 116249.0,
            "y": 41.49,
            "r": 8,
            "label": "USDUT: $116,249 FDV, 41.5% concentration (low risk)"
          },
          {
            "x": 123344.0,
            "y": 46.34,
            "r": 8,
            "label": "gib: $123,344 FDV, 46.3% concentration (low risk)"
          },
          {
            "x": 100154.0,
            "y": 47.7,
            "r": 8,
            "label": "USEFUL: $100,154 FDV, 47.7% concentration (low risk)"
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
            "x": 12230.0,
            "y": 72.03,
            "r": 8,
            "label": "1: $12,230 FDV, 72.0% concentration (medium risk)"
          },
          {
            "x": 3420305.0,
            "y": 63.96,
            "r": 8,
            "label": "HAROLD: $3,420,305 FDV, 64.0% concentration (medium risk)"
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
            "x": 6145.0,
            "y": 92.82,
            "r": 8,
            "label": "1: $6,145 FDV, 92.8% concentration (high risk)"
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
            "x": 3616.0,
            "y": 79.96,
            "r": 8,
            "label": "APOLLO: $3,616 FDV, 80.0% concentration (high risk)"
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
            "x": 13851447.0,
            "y": 96.8,
            "r": 8,
            "label": "SOL: $13,851,447 FDV, 96.8% concentration (extreme risk)"
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
            "x": 3568.0,
            "y": 97.61,
            "r": 8,
            "label": "obvious: $3,568 FDV, 97.6% concentration (extreme risk)"
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
| 1 | XBT | XBT | 25.50% | 🟢 low | $21.72 | $440.72 |
| 2 | FLY | Nexa | 28.94% | 🟢 low | $49.35 | $133.27 |
| 3 | RAGEGUY | Rage Guy | 29.72% | 🟢 low | $12.11K | $99.90K |
| 4 | DREAM | Dreamsync | 33.15% | 🟢 low | $10.53K | $104.34K |
| 5 | FARTLESS | FARTLESS COIN | 36.49% | 🟢 low | $471.81 | $2.61K |
| 6 | ELIZABETH | Just Elizabeth Cat | 37.72% | 🟢 low | $4.04 | $28.22 |
| 7 | 1nu | 1nu | 37.90% | 🟢 low | $339.78K | $46.96K |
| 8 | USDUT | unstable tether | 41.49% | 🟢 low | $1.57 | $37.42 |
| 9 | gib | gib | 46.34% | 🟢 low | $0.83 | $24.61 |
| 10 | USEFUL | USEFUL COIN | 47.70% | 🟢 low | $0.52 | $33.88 |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | 1cat | 1 cat can change your lif | 99.90% | 🔴 extreme | $308.45 | $0.00 |
| 2 | BONKZ | Bonkzilla | 99.86% | 🔴 extreme | $136.04 | $5.66K |
| 3 | MMGA | MAKE MEMES GREAT AGAIN | 99.39% | 🔴 extreme | $157.60 | $5.81K |
| 4 | SLOW | Slow Runner | 99.24% | 🔴 extreme | $2.38 | $6.28K |
| 5 | 1% Club | The 1% Club | 98.87% | 🔴 extreme | $1.64K | $6.17K |
| 6 | BLUB | Blub | 97.85% | 🔴 extreme | $0.50 | $6.29K |
| 7 | obvious | in hindsight | 97.61% | 🔴 extreme | $4.13 | $6.43K |
| 8 | Streamless | Streamless coin | 97.12% | 🔴 extreme | $265.99 | $6.62K |
| 9 | SOL | Solana | 96.80% | 🔴 extreme | $2.50K | $14.19K |
| 10 | MOCHI | MOCHI CULT | 94.57% | 🔴 extreme | $63.57 | $14.51K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 35
**Combined 24h Volume**: $278.43M
**Combined Liquidity**: $47.03M

**Concentration Risk Distribution**:
- 🟢 Low: 14 tokens
- 🔴 Extreme: 10 tokens
- 🟡 High: 7 tokens
- 🟢 Medium: 3 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $277.72M | $44.68M | 🟢 unknown |
| 2 | 1nu | 1nu | $339.78K | $46.96K | 🟢 low |
| 3 | 1 | 1 pill can change your life | $214.10K | $11.92K | 🟢 medium |
| 4 | HAROLD | Harold | $51.75K | $463.90K | 🟢 medium |
| 5 | LION | Loaded Lions | $24.07K | $1.34M | 🟢 low |
| 6 | AI4 | AI⁴ | $20.45K | $77.13K | 🟢 low |
| 7 | 1 | 1 pill can change your life | $14.48K | $9.30K | 🟡 high |
| 8 | RAGEGUY | Rage Guy | $12.11K | $99.90K | 🟢 low |
| 9 | DREAM | Dreamsync | $10.53K | $104.34K | 🟢 low |
| 10 | SHITTER | SHITTERCOIN | $10.02K | $24.36K | 🟢 low |

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
- 👀 **Watch**: 121 tokens
- 🚀 **Breakout**: 3 tokens
- ❄️ **Cooling**: 1 tokens

### 🚀 Breakout Signals

| Symbol | Score | Vol 3v1 | Z-Score Vol | Liq 3d | Streak |
|--------|-------|---------|-------------|--------|--------|
| wSOL | 4.24 | 2.51x | 1.69 | $57.82M | 0d |
| XBT | 3.65 | 2.10x | 1.74 | $421.14K | 0d |
| USDUT | 3.57 | 2.36x | 1.51 | $150.84K | 0d |

### 👀 Watch List

*121 tokens showing elevated activity*

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
