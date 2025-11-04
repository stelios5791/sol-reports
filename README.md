# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-11-04 19:36 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **40 tokens tracked** | 
💰 **$315.81M 24h volume** | 
💧 **$45.10M liquidity** | 
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
          3,
          5,
          19,
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
          -0.17222820236815073,
          -0.17222820236815073
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
      "1nu",
      "RAGEGUY",
      "LION",
      "HAROLD",
      "SHITTER",
      "SOL",
      "1",
      "1"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          87551.03,
          75905.27,
          63970.54,
          32461.31,
          31773.87,
          14862.27,
          3955.32,
          3541.93,
          1433.03,
          1200.77
        ],
        "backgroundColor": [
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#eab308",
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
      "2025-11-04"
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
          33.16
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
          53.57
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
          45.06
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
          29.21
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
            "x": 707303.0,
            "y": 33.16,
            "r": 8,
            "label": "DREAM: $707,303 FDV, 33.2% concentration (low risk)"
          },
          {
            "x": 201683.0,
            "y": 53.57,
            "r": 8,
            "label": "AI4: $201,683 FDV, 53.6% concentration (low risk)"
          },
          {
            "x": 59037.0,
            "y": 45.06,
            "r": 8,
            "label": "1nu: $59,037 FDV, 45.1% concentration (low risk)"
          },
          {
            "x": 528014.0,
            "y": 29.21,
            "r": 8,
            "label": "RAGEGUY: $528,014 FDV, 29.2% concentration (low risk)"
          },
          {
            "x": 43537930.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $43,537,930 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 322712.0,
            "y": 37.3,
            "r": 8,
            "label": "FARTLESS: $322,712 FDV, 37.3% concentration (low risk)"
          },
          {
            "x": 917160.0,
            "y": 25.52,
            "r": 8,
            "label": "XBT: $917,160 FDV, 25.5% concentration (low risk)"
          },
          {
            "x": 61743.0,
            "y": 58.93,
            "r": 8,
            "label": "RUECAT: $61,743 FDV, 58.9% concentration (low risk)"
          },
          {
            "x": 332069.0,
            "y": 38.07,
            "r": 8,
            "label": "ELIZABETH: $332,069 FDV, 38.1% concentration (low risk)"
          },
          {
            "x": 16295.0,
            "y": 30.09,
            "r": 8,
            "label": "FLY: $16,295 FDV, 30.1% concentration (low risk)"
          },
          {
            "x": 120437.0,
            "y": 46.39,
            "r": 8,
            "label": "gib: $120,437 FDV, 46.4% concentration (low risk)"
          },
          {
            "x": 108118.0,
            "y": 47.46,
            "r": 8,
            "label": "USEFUL: $108,118 FDV, 47.5% concentration (low risk)"
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
            "x": 2668652.0,
            "y": 64.09,
            "r": 8,
            "label": "HAROLD: $2,668,652 FDV, 64.1% concentration (medium risk)"
          },
          {
            "x": 24491.0,
            "y": 61.53,
            "r": 8,
            "label": "SHITTER: $24,491 FDV, 61.5% concentration (medium risk)"
          },
          {
            "x": 14185.0,
            "y": 65.32,
            "r": 8,
            "label": "$CrepSol: $14,185 FDV, 65.3% concentration (medium risk)"
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
            "x": 10963.0,
            "y": 89.95,
            "r": 8,
            "label": "AUSBAGWORK: $10,963 FDV, 90.0% concentration (high risk)"
          },
          {
            "x": 7921.0,
            "y": 81.06,
            "r": 8,
            "label": "1Bull: $7,921 FDV, 81.1% concentration (high risk)"
          },
          {
            "x": 6086.0,
            "y": 90.24,
            "r": 8,
            "label": "DARE: $6,086 FDV, 90.2% concentration (high risk)"
          },
          {
            "x": 3547.0,
            "y": 81.56,
            "r": 8,
            "label": "APOLLO: $3,547 FDV, 81.6% concentration (high risk)"
          },
          {
            "x": 6864.0,
            "y": 92.86,
            "r": 8,
            "label": "IDIOT: $6,864 FDV, 92.9% concentration (high risk)"
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
            "x": 14226165.0,
            "y": 96.8,
            "r": 8,
            "label": "SOL: $14,226,165 FDV, 96.8% concentration (extreme risk)"
          },
          {
            "x": 4642.0,
            "y": 95.67,
            "r": 8,
            "label": "1: $4,642 FDV, 95.7% concentration (extreme risk)"
          },
          {
            "x": 4636.0,
            "y": 97.42,
            "r": 8,
            "label": "1: $4,636 FDV, 97.4% concentration (extreme risk)"
          },
          {
            "x": 8428.0,
            "y": 93.72,
            "r": 8,
            "label": "MOCHI: $8,428 FDV, 93.7% concentration (extreme risk)"
          },
          {
            "x": 3919.0,
            "y": 98.53,
            "r": 8,
            "label": "FALCONS: $3,919 FDV, 98.5% concentration (extreme risk)"
          },
          {
            "x": 3701.0,
            "y": 96.41,
            "r": 8,
            "label": "7: $3,701 FDV, 96.4% concentration (extreme risk)"
          },
          {
            "x": 4906.0,
            "y": 96.49,
            "r": 8,
            "label": "SUPRACOIN: $4,906 FDV, 96.5% concentration (extreme risk)"
          },
          {
            "x": 2951.0,
            "y": 99.32,
            "r": 8,
            "label": "MMGA: $2,951 FDV, 99.3% concentration (extreme risk)"
          },
          {
            "x": 3446.0,
            "y": 98.97,
            "r": 8,
            "label": "19: $3,446 FDV, 99.0% concentration (extreme risk)"
          },
          {
            "x": 3319.0,
            "y": 99.69,
            "r": 8,
            "label": "KENNY: $3,319 FDV, 99.7% concentration (extreme risk)"
          },
          {
            "x": 3235.0,
            "y": 99.98,
            "r": 8,
            "label": "COUNT: $3,235 FDV, 100.0% concentration (extreme risk)"
          },
          {
            "x": 3312.0,
            "y": 99.71,
            "r": 8,
            "label": "Supershiro: $3,312 FDV, 99.7% concentration (extreme risk)"
          },
          {
            "x": 3033.0,
            "y": 99.99,
            "r": 8,
            "label": "UPC: $3,033 FDV, 100.0% concentration (extreme risk)"
          },
          {
            "x": 3123.0,
            "y": 99.4,
            "r": 8,
            "label": "retail: $3,123 FDV, 99.4% concentration (extreme risk)"
          },
          {
            "x": 3016.0,
            "y": 99.81,
            "r": 8,
            "label": "NeverDie: $3,016 FDV, 99.8% concentration (extreme risk)"
          },
          {
            "x": 2960.0,
            "y": 99.66,
            "r": 8,
            "label": "ACTIVITIES: $2,960 FDV, 99.7% concentration (extreme risk)"
          },
          {
            "x": 2983.0,
            "y": 99.84,
            "r": 8,
            "label": "MOONCOIN: $2,983 FDV, 99.8% concentration (extreme risk)"
          },
          {
            "x": 3047.0,
            "y": 99.63,
            "r": 8,
            "label": "ORE: $3,047 FDV, 99.6% concentration (extreme risk)"
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
| 1 | XBT | XBT | 25.52% | 🟢 low | $277.91 | $408.46 |
| 2 | RAGEGUY | Rage Guy | 29.21% | 🟢 low | $32.46K | $99.03K |
| 3 | FLY | Nexa | 30.09% | 🟢 low | $4.32 | $5.35K |
| 4 | DREAM | Dreamsync | 33.16% | 🟢 low | $87.55K | $104.88K |
| 5 | FARTLESS | FARTLESS COIN | 37.30% | 🟢 low | $488.94 | $2.37K |
| 6 | ELIZABETH | Just Elizabeth Cat | 38.07% | 🟢 low | $5.78 | $28.25 |
| 7 | 1nu | 1nu | 45.06% | 🟢 low | $63.97K | $32.39K |
| 8 | gib | gib | 46.39% | 🟢 low | $3.14 | $24.32 |
| 9 | USEFUL | USEFUL COIN | 47.46% | 🟢 low | $1.62 | $33.77 |
| 10 | AI4 | AI⁴ | 53.57% | 🟢 low | $75.91K | $77.36K |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | YOU | YOU can change your life. | 100.00% | 🔴 extreme | $0.00 | $0.00 |
| 2 | UPC | Upcoin | 99.99% | 🔴 extreme | $1.55 | $6.04K |
| 3 | COUNT | Counting live till $100M | 99.98% | 🔴 extreme | $1.64 | $6.46K |
| 4 | MOONCOIN | MOON COIN | 99.84% | 🔴 extreme | $1.47 | $5.94K |
| 5 | NeverDie | MEMES WILL NEVER DIE | 99.81% | 🔴 extreme | $1.51 | $5.98K |
| 6 | Supershiro | Super Shiro | 99.71% | 🔴 extreme | $1.61 | $6.28K |
| 7 | KENNY | KENNY KO | 99.69% | 🔴 extreme | $1.65 | $6.28K |
| 8 | ACTIVITIES | REAL LIFE ACTIVITIES | 99.66% | 🔴 extreme | $1.49 | $5.91K |
| 9 | ORE | Ore Labs | 99.63% | 🔴 extreme | $1.45 | $6.02K |
| 10 | retail | retail | 99.40% | 🔴 extreme | $1.53 | $6.21K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 40
**Combined 24h Volume**: $315.81M
**Combined Liquidity**: $45.10M

**Concentration Risk Distribution**:
- 🔴 Extreme: 19 tokens
- 🟢 Low: 12 tokens
- 🟡 High: 5 tokens
- 🟢 Medium: 3 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $315.49M | $42.82M | 🟢 unknown |
| 2 | DREAM | Dreamsync | $87.55K | $104.88K | 🟢 low |
| 3 | AI4 | AI⁴ | $75.91K | $77.36K | 🟢 low |
| 4 | 1nu | 1nu | $63.97K | $32.39K | 🟢 low |
| 5 | RAGEGUY | Rage Guy | $32.46K | $99.03K | 🟢 low |
| 6 | LION | Loaded Lions | $31.77K | $1.31M | 🟢 low |
| 7 | HAROLD | Harold | $14.86K | $401.78K | 🟢 medium |
| 8 | SHITTER | SHITTERCOIN | $3.96K | $21.80K | 🟢 medium |
| 9 | SOL | Solana | $3.54K | $14.12K | 🔴 extreme |
| 10 | 1 | 1 pill can change your life | $1.43K | $7.90K | 🔴 extreme |

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
- 👀 **Watch**: 112 tokens
- 🚀 **Breakout**: 3 tokens
- ❄️ **Cooling**: 1 tokens

### 🚀 Breakout Signals

| Symbol | Score | Vol 3v1 | Z-Score Vol | Liq 3d | Streak |
|--------|-------|---------|-------------|--------|--------|
| wSOL | 4.24 | 2.51x | 1.69 | $57.82M | 0d |
| XBT | 3.65 | 2.10x | 1.74 | $421.14K | 0d |
| USDUT | 3.57 | 2.36x | 1.51 | $150.84K | 0d |

### 👀 Watch List

*112 tokens showing elevated activity*

📄 [Full data: signals_filtered.csv](data/signals_filtered.csv)

---

## 📈 Historical Data

**Total Historical Records**: 514
**Unique Tokens Tracked**: 101
**Date Range**: 2025-10-01 to 2025-11-04

**Master Aggregations**: 101 tokens
**Performance Metrics**: 514 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 514 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 101 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 514 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 40 |
| [new_viable.csv](data/new_viable.csv) | New tokens with potential | 0 |
| [signals_filtered.csv](data/signals_filtered.csv) | Whale-filtered trading signals | 116 |

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
