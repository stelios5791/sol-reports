# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-11-07 08:46 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **40 tokens tracked** | 
💰 **$268.95M 24h volume** | 
💧 **$48.50M liquidity** | 
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
          5,
          5,
          14,
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
          -48.48826291079813,
          -48.48826291079813
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
      "RAGEGUY",
      "LION",
      "1",
      "DREAM",
      "HAROLD",
      "AI4",
      "SHITTER",
      "SOL",
      "RUECAT"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          53519.27,
          22905.03,
          21469.43,
          20436.41,
          13747.64,
          13403.6,
          6358.98,
          3140.11,
          1164.06,
          808.17
        ],
        "backgroundColor": [
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#22c55e",
          "#eab308",
          "#22c55e",
          "#22c55e",
          "#ef4444",
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
      "2025-10-02",
      "2025-10-03",
      "2025-10-04",
      "2025-10-05",
      "2025-10-06",
      "2025-10-07",
      "2025-11-07"
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
          41.31
        ],
        "borderColor": "#3b82f6",
        "backgroundColor": "#3b82f620",
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
          30.32
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
          75.3,
          94.15
        ],
        "borderColor": "#eab308",
        "backgroundColor": "#eab30820",
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
          33.09
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
            "x": 93602.0,
            "y": 41.31,
            "r": 8,
            "label": "1nu: $93,602 FDV, 41.3% concentration (low risk)"
          },
          {
            "x": 436355.0,
            "y": 30.32,
            "r": 8,
            "label": "RAGEGUY: $436,355 FDV, 30.3% concentration (low risk)"
          },
          {
            "x": 44619309.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $44,619,309 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 699319.0,
            "y": 33.09,
            "r": 8,
            "label": "DREAM: $699,319 FDV, 33.1% concentration (low risk)"
          },
          {
            "x": 193937.0,
            "y": 53.42,
            "r": 8,
            "label": "AI4: $193,937 FDV, 53.4% concentration (low risk)"
          },
          {
            "x": 31156.0,
            "y": 55.67,
            "r": 8,
            "label": "SHITTER: $31,156 FDV, 55.7% concentration (low risk)"
          },
          {
            "x": 369213.0,
            "y": 36.32,
            "r": 8,
            "label": "FARTLESS: $369,213 FDV, 36.3% concentration (low risk)"
          },
          {
            "x": 19263.0,
            "y": 27.45,
            "r": 8,
            "label": "FLY: $19,263 FDV, 27.4% concentration (low risk)"
          },
          {
            "x": 974131.0,
            "y": 25.64,
            "r": 8,
            "label": "XBT: $974,131 FDV, 25.6% concentration (low risk)"
          },
          {
            "x": 90645.0,
            "y": 44.2,
            "r": 8,
            "label": "YAO: $90,645 FDV, 44.2% concentration (low risk)"
          },
          {
            "x": 433853.0,
            "y": 35.66,
            "r": 8,
            "label": "ELIZABETH: $433,853 FDV, 35.7% concentration (low risk)"
          },
          {
            "x": 14480258.0,
            "y": 39.94,
            "r": 8,
            "label": "AI20X: $14,480,258 FDV, 39.9% concentration (low risk)"
          },
          {
            "x": 106129.0,
            "y": 42.11,
            "r": 8,
            "label": "USDUT: $106,129 FDV, 42.1% concentration (low risk)"
          },
          {
            "x": 122792.0,
            "y": 47.71,
            "r": 8,
            "label": "gib: $122,792 FDV, 47.7% concentration (low risk)"
          },
          {
            "x": 110333.0,
            "y": 47.13,
            "r": 8,
            "label": "USEFUL: $110,333 FDV, 47.1% concentration (low risk)"
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
            "x": 10652.0,
            "y": 75.3,
            "r": 8,
            "label": "1: $10,652 FDV, 75.3% concentration (medium risk)"
          },
          {
            "x": 3258986.0,
            "y": 64.07,
            "r": 8,
            "label": "HAROLD: $3,258,986 FDV, 64.1% concentration (medium risk)"
          },
          {
            "x": 65959.0,
            "y": 59.97,
            "r": 8,
            "label": "RUECAT: $65,959 FDV, 60.0% concentration (medium risk)"
          },
          {
            "x": 5660.0,
            "y": 76.67,
            "r": 8,
            "label": "APOLLO: $5,660 FDV, 76.7% concentration (medium risk)"
          },
          {
            "x": 14303.0,
            "y": 65.71,
            "r": 8,
            "label": "$CrepSol: $14,303 FDV, 65.7% concentration (medium risk)"
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
            "x": 5482.0,
            "y": 94.15,
            "r": 8,
            "label": "1: $5,482 FDV, 94.2% concentration (high risk)"
          },
          {
            "x": 10703.0,
            "y": 89.99,
            "r": 8,
            "label": "AUSBAGWORK: $10,703 FDV, 90.0% concentration (high risk)"
          },
          {
            "x": 8724.0,
            "y": 80.98,
            "r": 8,
            "label": "1Bull: $8,724 FDV, 81.0% concentration (high risk)"
          },
          {
            "x": 5217.0,
            "y": 93.71,
            "r": 8,
            "label": "pibble: $5,217 FDV, 93.7% concentration (high risk)"
          },
          {
            "x": 4838.0,
            "y": 91.96,
            "r": 8,
            "label": "FARTWORM: $4,838 FDV, 92.0% concentration (high risk)"
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
            "x": 12586918.0,
            "y": 96.8,
            "r": 8,
            "label": "SOL: $12,586,918 FDV, 96.8% concentration (extreme risk)"
          },
          {
            "x": 4494.0,
            "y": 95.02,
            "r": 8,
            "label": "RWA: $4,494 FDV, 95.0% concentration (extreme risk)"
          },
          {
            "x": 3479.0,
            "y": 97.23,
            "r": 8,
            "label": "Streamless: $3,479 FDV, 97.2% concentration (extreme risk)"
          },
          {
            "x": 3170.0,
            "y": 99.23,
            "r": 8,
            "label": "HAMSTERUN: $3,170 FDV, 99.2% concentration (extreme risk)"
          },
          {
            "x": 4780.0,
            "y": 96.35,
            "r": 8,
            "label": "SUPRACOIN: $4,780 FDV, 96.3% concentration (extreme risk)"
          },
          {
            "x": 2862.0,
            "y": 99.99,
            "r": 8,
            "label": "UPC: $2,862 FDV, 100.0% concentration (extreme risk)"
          },
          {
            "x": 3185.0,
            "y": 97.86,
            "r": 8,
            "label": "BLUB: $3,185 FDV, 97.9% concentration (extreme risk)"
          },
          {
            "x": 3426.0,
            "y": 99.38,
            "r": 8,
            "label": "BEANIE: $3,426 FDV, 99.4% concentration (extreme risk)"
          },
          {
            "x": 2879.0,
            "y": 99.68,
            "r": 8,
            "label": "ORE: $2,879 FDV, 99.7% concentration (extreme risk)"
          },
          {
            "x": 2830.0,
            "y": 99.85,
            "r": 8,
            "label": "MOONCOIN: $2,830 FDV, 99.8% concentration (extreme risk)"
          },
          {
            "x": 8309.0,
            "y": 94.19,
            "r": 8,
            "label": "MOCHI: $8,309 FDV, 94.2% concentration (extreme risk)"
          },
          {
            "x": 3118.0,
            "y": 99.25,
            "r": 8,
            "label": "SLOW: $3,118 FDV, 99.2% concentration (extreme risk)"
          },
          {
            "x": 4141.0,
            "y": 98.68,
            "r": 8,
            "label": "REVIVE: $4,141 FDV, 98.7% concentration (extreme risk)"
          },
          {
            "x": 3486.0,
            "y": 99.9,
            "r": 8,
            "label": "PUMPFOLIO: $3,486 FDV, 99.9% concentration (extreme risk)"
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
| 1 | XBT | XBT | 25.64% | 🟢 low | $70.48 | $421.75 |
| 2 | FLY | Nexa | 27.45% | 🟢 low | $170.68 | $5.87K |
| 3 | RAGEGUY | Rage Guy | 30.32% | 🟢 low | $22.91K | $90.50K |
| 4 | DREAM | Dreamsync | 33.09% | 🟢 low | $13.75K | $102.70K |
| 5 | ELIZABETH | Just Elizabeth Cat | 35.66% | 🟢 low | $4.61 | $32.29 |
| 6 | FARTLESS | FARTLESS COIN | 36.32% | 🟢 low | $514.83 | $2.53K |
| 7 | AI20X | Ai20x.ai | 39.94% | 🟢 low | $2.93 | $1.78M |
| 8 | 1nu | 1nu | 41.31% | 🟢 low | $53.52K | $41.34K |
| 9 | USDUT | unstable tether | 42.11% | 🟢 low | $0.77 | $36.62 |
| 10 | YAO | YAO MING | 44.20% | 🟢 low | $15.94 | $621.86 |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | UPC | Upcoin | 99.99% | 🔴 extreme | $9.18 | $5.69K |
| 2 | PUMPFOLIO | Retail Summer | 99.90% | 🔴 extreme | $0.00 | $6.66K |
| 3 | MOONCOIN | MOON COIN | 99.85% | 🔴 extreme | $0.21 | $5.64K |
| 4 | ORE | Ore Labs | 99.68% | 🔴 extreme | $0.21 | $5.69K |
| 5 | BEANIE | BEANIE | 99.38% | 🔴 extreme | $0.22 | $6.61K |
| 6 | SLOW | Slow Runner | 99.25% | 🔴 extreme | $0.10 | $6.17K |
| 7 | HAMSTERUN | Hamster Runner | 99.23% | 🔴 extreme | $24.91 | $6.14K |
| 8 | REVIVE | reviving the memes | 98.68% | 🔴 extreme | $0.00 | $8.12K |
| 9 | BLUB | Blub | 97.86% | 🔴 extreme | $0.41 | $6.12K |
| 10 | Streamless | Streamless coin | 97.23% | 🔴 extreme | $31.48 | $6.65K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 40
**Combined 24h Volume**: $268.95M
**Combined Liquidity**: $48.50M

**Concentration Risk Distribution**:
- 🟢 Low: 15 tokens
- 🔴 Extreme: 14 tokens
- 🟢 Medium: 5 tokens
- 🟡 High: 5 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $268.79M | $44.38M | 🟢 unknown |
| 2 | 1nu | 1nu | $53.52K | $41.34K | 🟢 low |
| 3 | RAGEGUY | Rage Guy | $22.91K | $90.50K | 🟢 low |
| 4 | LION | Loaded Lions | $21.47K | $1.33M | 🟢 low |
| 5 | 1 | 1 pill can change your life | $20.44K | $11.01K | 🟢 medium |
| 6 | DREAM | Dreamsync | $13.75K | $102.70K | 🟢 low |
| 7 | HAROLD | Harold | $13.40K | $445.77K | 🟢 medium |
| 8 | AI4 | AI⁴ | $6.36K | $76.08K | 🟢 low |
| 9 | SHITTER | SHITTERCOIN | $3.14K | $24.22K | 🟢 low |
| 10 | SOL | Solana | $1.16K | $13.27K | 🔴 extreme |

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
- ❄️ **Cooling**: 2 tokens

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

**Total Historical Records**: 514
**Unique Tokens Tracked**: 101
**Date Range**: 2025-10-01 to 2025-11-07

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
| [signals_filtered.csv](data/signals_filtered.csv) | Whale-filtered trading signals | 118 |

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
