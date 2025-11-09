# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-11-09 08:40 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **31 tokens tracked** | 
💰 **$118.88M 24h volume** | 
💧 **$45.79M liquidity** | 
🟢 **12 low-risk tokens**

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
          12,
          5,
          5,
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
          -53.56176735798016,
          -53.56176735798016
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
      "DREAM",
      "RAGEGUY",
      "LION",
      "1",
      "AI4",
      "HAROLD",
      "RUECAT",
      "AUSBAGWORK",
      "FARTLESS"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          13852.61,
          12322.51,
          12276.79,
          6944.87,
          6346.27,
          3687.47,
          2357.49,
          382.95,
          231.87,
          213.6
        ],
        "backgroundColor": [
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#22c55e",
          "#eab308",
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
      "2025-10-02",
      "2025-10-03",
      "2025-10-04",
      "2025-10-05",
      "2025-10-06",
      "2025-10-07",
      "2025-11-09"
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
          42.43
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
          33.06
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
          30.46
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
          74.75,
          95.17
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
            "x": 87360.0,
            "y": 42.43,
            "r": 8,
            "label": "1nu: $87,360 FDV, 42.4% concentration (low risk)"
          },
          {
            "x": 711344.0,
            "y": 33.06,
            "r": 8,
            "label": "DREAM: $711,344 FDV, 33.1% concentration (low risk)"
          },
          {
            "x": 430387.0,
            "y": 30.46,
            "r": 8,
            "label": "RAGEGUY: $430,387 FDV, 30.5% concentration (low risk)"
          },
          {
            "x": 43112815.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $43,112,815 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 180127.0,
            "y": 54.47,
            "r": 8,
            "label": "AI4: $180,127 FDV, 54.5% concentration (low risk)"
          },
          {
            "x": 335567.0,
            "y": 37.07,
            "r": 8,
            "label": "FARTLESS: $335,567 FDV, 37.1% concentration (low risk)"
          },
          {
            "x": 29170.0,
            "y": 57.28,
            "r": 8,
            "label": "SHITTER: $29,170 FDV, 57.3% concentration (low risk)"
          },
          {
            "x": 861319.0,
            "y": 26.56,
            "r": 8,
            "label": "XBT: $861,319 FDV, 26.6% concentration (low risk)"
          },
          {
            "x": 520239.0,
            "y": 32.07,
            "r": 8,
            "label": "ELIZABETH: $520,239 FDV, 32.1% concentration (low risk)"
          },
          {
            "x": 83909.0,
            "y": 42.98,
            "r": 8,
            "label": "YAO: $83,909 FDV, 43.0% concentration (low risk)"
          },
          {
            "x": 19612.0,
            "y": 27.46,
            "r": 8,
            "label": "FLY: $19,612 FDV, 27.5% concentration (low risk)"
          },
          {
            "x": 104284.0,
            "y": 42.17,
            "r": 8,
            "label": "USDUT: $104,284 FDV, 42.2% concentration (low risk)"
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
            "x": 11088.0,
            "y": 74.75,
            "r": 8,
            "label": "1: $11,088 FDV, 74.8% concentration (medium risk)"
          },
          {
            "x": 3230713.0,
            "y": 64.12,
            "r": 8,
            "label": "HAROLD: $3,230,713 FDV, 64.1% concentration (medium risk)"
          },
          {
            "x": 61972.0,
            "y": 61.32,
            "r": 8,
            "label": "RUECAT: $61,972 FDV, 61.3% concentration (medium risk)"
          },
          {
            "x": 14334.0,
            "y": 65.98,
            "r": 8,
            "label": "$CrepSol: $14,334 FDV, 66.0% concentration (medium risk)"
          },
          {
            "x": 5715.0,
            "y": 76.93,
            "r": 8,
            "label": "APOLLO: $5,715 FDV, 76.9% concentration (medium risk)"
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
            "x": 10634.0,
            "y": 90.91,
            "r": 8,
            "label": "AUSBAGWORK: $10,634 FDV, 90.9% concentration (high risk)"
          },
          {
            "x": 8165.0,
            "y": 82.22,
            "r": 8,
            "label": "1Bull: $8,165 FDV, 82.2% concentration (high risk)"
          },
          {
            "x": 4951.0,
            "y": 95.6,
            "r": 8,
            "label": "pibble: $4,951 FDV, 95.6% concentration (high risk)"
          },
          {
            "x": 6301.0,
            "y": 90.31,
            "r": 8,
            "label": "DARE: $6,301 FDV, 90.3% concentration (high risk)"
          },
          {
            "x": 4821.0,
            "y": 92.24,
            "r": 8,
            "label": "FARTWORM: $4,821 FDV, 92.2% concentration (high risk)"
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
            "x": 3102.0,
            "y": 99.6,
            "r": 8,
            "label": "ORE: $3,102 FDV, 99.6% concentration (extreme risk)"
          },
          {
            "x": 12344006.0,
            "y": 96.8,
            "r": 8,
            "label": "SOL: $12,344,006 FDV, 96.8% concentration (extreme risk)"
          },
          {
            "x": 3657.0,
            "y": 96.9,
            "r": 8,
            "label": "7: $3,657 FDV, 96.9% concentration (extreme risk)"
          },
          {
            "x": 3223.0,
            "y": 98.05,
            "r": 8,
            "label": "BLUB: $3,223 FDV, 98.0% concentration (extreme risk)"
          },
          {
            "x": 4450.63,
            "y": 99.92,
            "r": 8,
            "label": "Hamu: $4,451 FDV, 99.9% concentration (extreme risk)"
          },
          {
            "x": 3384.0,
            "y": 97.36,
            "r": 8,
            "label": "Streamless: $3,384 FDV, 97.4% concentration (extreme risk)"
          },
          {
            "x": 8292.0,
            "y": 94.23,
            "r": 8,
            "label": "MOCHI: $8,292 FDV, 94.2% concentration (extreme risk)"
          },
          {
            "x": 5147.0,
            "y": 95.17,
            "r": 8,
            "label": "1: $5,147 FDV, 95.2% concentration (extreme risk)"
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
| 1 | XBT | XBT | 26.56% | 🟢 low | $21.25 | $399.11 |
| 2 | FLY | Nexa | 27.46% | 🟢 low | $1.02 | $5.98K |
| 3 | RAGEGUY | Rage Guy | 30.46% | 🟢 low | $12.28K | $90.45K |
| 4 | ELIZABETH | Just Elizabeth Cat | 32.07% | 🟢 low | $20.05 | $35.36 |
| 5 | DREAM | Dreamsync | 33.06% | 🟢 low | $12.32K | $104.03K |
| 6 | FARTLESS | FARTLESS COIN | 37.07% | 🟢 low | $213.60 | $2.42K |
| 7 | USDUT | unstable tether | 42.17% | 🟢 low | $0.38 | $36.23 |
| 8 | 1nu | 1nu | 42.43% | 🟢 low | $13.85K | $40.02K |
| 9 | YAO | YAO MING | 42.98% | 🟢 low | $2.85 | $568.00 |
| 10 | AI4 | AI⁴ | 54.47% | 🟢 low | $3.69K | $73.45K |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | Hamu | Hamu | 99.92% | 🔴 extreme | $8.86 | $0.00 |
| 2 | ORE | Ore Labs | 99.60% | 🔴 extreme | $131.76 | $5.89K |
| 3 | BLUB | Blub | 98.05% | 🔴 extreme | $18.22 | $6.21K |
| 4 | Streamless | Streamless coin | 97.36% | 🔴 extreme | $4.20 | $6.47K |
| 5 | 7 | 7 Coin | 96.90% | 🔴 extreme | $28.81 | $6.61K |
| 6 | SOL | Solana | 96.80% | 🔴 extreme | $62.87 | $3.42K |
| 7 | pibble | pibble | 95.60% | 🟠 high | $52.52 | $7.78K |
| 8 | 1 | 1 pill can change your li | 95.17% | 🔴 extreme | $0.16 | $8.39K |
| 9 | MOCHI | MOCHI CULT | 94.23% | 🔴 extreme | $2.48 | $14.51K |
| 10 | FARTWORM | FARTWORM | 92.24% | 🟠 high | $1.00 | $7.73K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 31
**Combined 24h Volume**: $118.88M
**Combined Liquidity**: $45.79M

**Concentration Risk Distribution**:
- 🟢 Low: 12 tokens
- 🔴 Extreme: 8 tokens
- 🟢 Medium: 5 tokens
- 🟡 High: 5 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $118.82M | $43.53M | 🟢 unknown |
| 2 | 1nu | 1nu | $13.85K | $40.02K | 🟢 low |
| 3 | DREAM | Dreamsync | $12.32K | $104.03K | 🟢 low |
| 4 | RAGEGUY | Rage Guy | $12.28K | $90.45K | 🟢 low |
| 5 | LION | Loaded Lions | $6.94K | $1.32M | 🟢 low |
| 6 | 1 | 1 pill can change your life | $6.35K | $11.27K | 🟢 medium |
| 7 | AI4 | AI⁴ | $3.69K | $73.45K | 🟢 low |
| 8 | HAROLD | Harold | $2.36K | $446.20K | 🟢 medium |
| 9 | RUECAT | Rue Cat | $382.95 | $31.54K | 🟢 medium |
| 10 | AUSBAGWORK | AUSSIE BAG WORKERS | $231.87 | $13.32K | 🟡 high |

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
**Date Range**: 2025-10-01 to 2025-11-09

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
