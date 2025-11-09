# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-11-09 14:54 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **34 tokens tracked** | 
💰 **$128.15M 24h volume** | 
💧 **$47.03M liquidity** | 
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
          -59.828393135725435,
          -59.828393135725435
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
      "RAGEGUY",
      "1",
      "LION",
      "HAROLD",
      "AI4",
      "AUSBAGWORK",
      "pibble",
      "SOL"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          111567.39,
          11429.43,
          11220.55,
          9468.59,
          6917.76,
          4647.05,
          1878.03,
          363.53,
          273.93,
          245.85
        ],
        "backgroundColor": [
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#22c55e",
          "#eab308",
          "#22c55e",
          "#f97316",
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
      "2025-11-09"
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
          40.16
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
          30.56
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
          71.12,
          95.17
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
            "x": 711029.0,
            "y": 33.14,
            "r": 8,
            "label": "DREAM: $711,029 FDV, 33.1% concentration (low risk)"
          },
          {
            "x": 95455.0,
            "y": 40.16,
            "r": 8,
            "label": "1nu: $95,455 FDV, 40.2% concentration (low risk)"
          },
          {
            "x": 428779.0,
            "y": 30.56,
            "r": 8,
            "label": "RAGEGUY: $428,779 FDV, 30.6% concentration (low risk)"
          },
          {
            "x": 44291466.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $44,291,466 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 181972.0,
            "y": 54.67,
            "r": 8,
            "label": "AI4: $181,972 FDV, 54.7% concentration (low risk)"
          },
          {
            "x": 345418.0,
            "y": 36.99,
            "r": 8,
            "label": "FARTLESS: $345,418 FDV, 37.0% concentration (low risk)"
          },
          {
            "x": 29169.0,
            "y": 57.27,
            "r": 8,
            "label": "SHITTER: $29,169 FDV, 57.3% concentration (low risk)"
          },
          {
            "x": 638622.0,
            "y": 30.59,
            "r": 8,
            "label": "ELIZABETH: $638,622 FDV, 30.6% concentration (low risk)"
          },
          {
            "x": 904550.0,
            "y": 26.12,
            "r": 8,
            "label": "XBT: $904,550 FDV, 26.1% concentration (low risk)"
          },
          {
            "x": 83909.0,
            "y": 43.03,
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
            "x": 108476.0,
            "y": 47.69,
            "r": 8,
            "label": "USEFUL: $108,476 FDV, 47.7% concentration (low risk)"
          },
          {
            "x": 104284.0,
            "y": 42.44,
            "r": 8,
            "label": "USDUT: $104,284 FDV, 42.4% concentration (low risk)"
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
            "x": 12822.0,
            "y": 71.12,
            "r": 8,
            "label": "1: $12,822 FDV, 71.1% concentration (medium risk)"
          },
          {
            "x": 3234735.0,
            "y": 64.18,
            "r": 8,
            "label": "HAROLD: $3,234,735 FDV, 64.2% concentration (medium risk)"
          },
          {
            "x": 62856.0,
            "y": 61.34,
            "r": 8,
            "label": "RUECAT: $62,856 FDV, 61.3% concentration (medium risk)"
          },
          {
            "x": 14150.0,
            "y": 66.25,
            "r": 8,
            "label": "$CrepSol: $14,150 FDV, 66.2% concentration (medium risk)"
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
            "x": 10645.0,
            "y": 90.91,
            "r": 8,
            "label": "AUSBAGWORK: $10,645 FDV, 90.9% concentration (high risk)"
          },
          {
            "x": 8165.0,
            "y": 82.22,
            "r": 8,
            "label": "1Bull: $8,165 FDV, 82.2% concentration (high risk)"
          },
          {
            "x": 5324.0,
            "y": 77.91,
            "r": 8,
            "label": "APOLLO: $5,324 FDV, 77.9% concentration (high risk)"
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
            "x": 4402.0,
            "y": 96.44,
            "r": 8,
            "label": "pibble: $4,402 FDV, 96.4% concentration (extreme risk)"
          },
          {
            "x": 12373394.0,
            "y": 96.8,
            "r": 8,
            "label": "SOL: $12,373,394 FDV, 96.8% concentration (extreme risk)"
          },
          {
            "x": 3102.0,
            "y": 99.6,
            "r": 8,
            "label": "ORE: $3,102 FDV, 99.6% concentration (extreme risk)"
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
            "x": 3518.0,
            "y": 97.9,
            "r": 8,
            "label": "Bagwork: $3,518 FDV, 97.9% concentration (extreme risk)"
          },
          {
            "x": 4450.63,
            "y": 99.92,
            "r": 8,
            "label": "Hamu: $4,451 FDV, 99.9% concentration (extreme risk)"
          },
          {
            "x": 8593.0,
            "y": 94.21,
            "r": 8,
            "label": "MOCHI: $8,593 FDV, 94.2% concentration (extreme risk)"
          },
          {
            "x": 3384.0,
            "y": 97.36,
            "r": 8,
            "label": "Streamless: $3,384 FDV, 97.4% concentration (extreme risk)"
          },
          {
            "x": 3331.0,
            "y": 98.98,
            "r": 8,
            "label": "1% Club: $3,331 FDV, 99.0% concentration (extreme risk)"
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
| 1 | XBT | XBT | 26.12% | 🟢 low | $22.16 | $412.49 |
| 2 | FLY | Nexa | 27.46% | 🟢 low | $1.02 | $5.98K |
| 3 | RAGEGUY | Rage Guy | 30.56% | 🟢 low | $11.22K | $91.16K |
| 4 | ELIZABETH | Just Elizabeth Cat | 30.59% | 🟢 low | $23.16 | $39.18 |
| 5 | DREAM | Dreamsync | 33.14% | 🟢 low | $111.57K | $104.84K |
| 6 | FARTLESS | FARTLESS COIN | 36.99% | 🟢 low | $158.15 | $2.45K |
| 7 | 1nu | 1nu | 40.16% | 🟢 low | $11.43K | $41.84K |
| 8 | USDUT | unstable tether | 42.44% | 🟢 low | $0.18 | $36.23 |
| 9 | YAO | YAO MING | 43.03% | 🟢 low | $2.85 | $568.00 |
| 10 | USEFUL | USEFUL COIN | 47.69% | 🟢 low | $0.43 | $35.31 |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | Hamu | Hamu | 99.92% | 🔴 extreme | $8.86 | $0.00 |
| 2 | ORE | Ore Labs | 99.60% | 🔴 extreme | $131.76 | $5.89K |
| 3 | 1% Club | The 1% Club | 98.98% | 🔴 extreme | $0.21 | $6.07K |
| 4 | BLUB | Blub | 98.05% | 🔴 extreme | $18.22 | $6.21K |
| 5 | Bagwork | African Bagwork | 97.90% | 🔴 extreme | $9.30 | $6.72K |
| 6 | Streamless | Streamless coin | 97.36% | 🔴 extreme | $4.05 | $6.47K |
| 7 | 7 | 7 Coin | 96.90% | 🔴 extreme | $28.81 | $6.61K |
| 8 | SOL | Solana | 96.80% | 🔴 extreme | $245.85 | $13.34K |
| 9 | pibble | pibble | 96.44% | 🔴 extreme | $273.93 | $7.34K |
| 10 | 1 | 1 pill can change your li | 95.17% | 🔴 extreme | $0.16 | $8.39K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 34
**Combined 24h Volume**: $128.15M
**Combined Liquidity**: $47.03M

**Concentration Risk Distribution**:
- 🟢 Low: 13 tokens
- 🔴 Extreme: 11 tokens
- 🟡 High: 5 tokens
- 🟢 Medium: 4 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $127.99M | $44.70M | 🟢 unknown |
| 2 | DREAM | Dreamsync | $111.57K | $104.84K | 🟢 low |
| 3 | 1nu | 1nu | $11.43K | $41.84K | 🟢 low |
| 4 | RAGEGUY | Rage Guy | $11.22K | $91.16K | 🟢 low |
| 5 | 1 | 1 pill can change your life | $9.47K | $12.20K | 🟢 medium |
| 6 | LION | Loaded Lions | $6.92K | $1.35M | 🟢 low |
| 7 | HAROLD | Harold | $4.65K | $451.26K | 🟢 medium |
| 8 | AI4 | AI⁴ | $1.88K | $74.74K | 🟢 low |
| 9 | AUSBAGWORK | AUSSIE BAG WORKERS | $363.53 | $13.36K | 🟡 high |
| 10 | pibble | pibble | $273.93 | $7.34K | 🔴 extreme |

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

**Total Historical Records**: 508
**Unique Tokens Tracked**: 101
**Date Range**: 2025-10-01 to 2025-11-09

**Master Aggregations**: 101 tokens
**Performance Metrics**: 505 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 508 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 101 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 505 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 34 |
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
