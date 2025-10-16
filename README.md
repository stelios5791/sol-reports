# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-10-16 08:40 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **44 tokens tracked** | 
💰 **$395.87M 24h volume** | 
💧 **$61.59M liquidity** | 
🟢 **16 low-risk tokens**

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
          16,
          2,
          9,
          16,
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
          -23.492723492723492,
          -23.492723492723492
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
      "SHITTER",
      "RAGEGUY",
      "HAROLD",
      "LION",
      "SOL",
      "1",
      "1"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          125986.96,
          118639.46,
          116770.26,
          26054.71,
          20491.58,
          18459.11,
          15826.44,
          7540.65,
          4540.75,
          1937.67
        ],
        "backgroundColor": [
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#22c55e",
          "#ef4444",
          "#f97316",
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
      "2025-10-03",
      "2025-10-04",
      "2025-10-05",
      "2025-10-06",
      "2025-10-07",
      "2025-10-16"
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
          31.57
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
          48.39
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
          39.17
        ],
        "borderColor": "#22c55e",
        "backgroundColor": "#22c55e20",
        "tension": 0.3,
        "fill": false
      },
      {
        "label": "SHITTER",
        "data": [
          0.0,
          0.0,
          0.0,
          0.0,
          64.26,
          64.33,
          63.23,
          56.43
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
          27.93
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
            "x": 1758741.0,
            "y": 31.57,
            "r": 8,
            "label": "DREAM: $1,758,741 FDV, 31.6% concentration (low risk)"
          },
          {
            "x": 310423.0,
            "y": 48.39,
            "r": 8,
            "label": "AI4: $310,423 FDV, 48.4% concentration (low risk)"
          },
          {
            "x": 79425.0,
            "y": 39.17,
            "r": 8,
            "label": "1nu: $79,425 FDV, 39.2% concentration (low risk)"
          },
          {
            "x": 32310.0,
            "y": 56.43,
            "r": 8,
            "label": "SHITTER: $32,310 FDV, 56.4% concentration (low risk)"
          },
          {
            "x": 615456.0,
            "y": 27.93,
            "r": 8,
            "label": "RAGEGUY: $615,456 FDV, 27.9% concentration (low risk)"
          },
          {
            "x": 59026373.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $59,026,373 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 103811.0,
            "y": 52.62,
            "r": 8,
            "label": "RUECAT: $103,811 FDV, 52.6% concentration (low risk)"
          },
          {
            "x": 785244.0,
            "y": 34.13,
            "r": 8,
            "label": "FARTLESS: $785,244 FDV, 34.1% concentration (low risk)"
          },
          {
            "x": 31608.0,
            "y": 57.16,
            "r": 8,
            "label": "$CrepSol: $31,608 FDV, 57.2% concentration (low risk)"
          },
          {
            "x": 15632.0,
            "y": 31.72,
            "r": 8,
            "label": "FLY: $15,632 FDV, 31.7% concentration (low risk)"
          },
          {
            "x": 1633169.0,
            "y": 22.12,
            "r": 8,
            "label": "XBT: $1,633,169 FDV, 22.1% concentration (low risk)"
          },
          {
            "x": 19339910.0,
            "y": 41.41,
            "r": 8,
            "label": "AI20X: $19,339,910 FDV, 41.4% concentration (low risk)"
          },
          {
            "x": 1612890.0,
            "y": 26.0,
            "r": 8,
            "label": "ELIZABETH: $1,612,890 FDV, 26.0% concentration (low risk)"
          },
          {
            "x": 203179.0,
            "y": 38.57,
            "r": 8,
            "label": "USDUT: $203,179 FDV, 38.6% concentration (low risk)"
          },
          {
            "x": 162770.0,
            "y": 40.87,
            "r": 8,
            "label": "USEFUL: $162,770 FDV, 40.9% concentration (low risk)"
          },
          {
            "x": 268429.0,
            "y": 46.09,
            "r": 8,
            "label": "gib: $268,429 FDV, 46.1% concentration (low risk)"
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
            "x": 2779624.0,
            "y": 63.22,
            "r": 8,
            "label": "HAROLD: $2,779,624 FDV, 63.2% concentration (medium risk)"
          },
          {
            "x": 26337.0,
            "y": 75.0,
            "r": 8,
            "label": "1Bull: $26,337 FDV, 75.0% concentration (medium risk)"
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
            "x": 8172.0,
            "y": 91.51,
            "r": 8,
            "label": "1: $8,172 FDV, 91.5% concentration (high risk)"
          },
          {
            "x": 6255.0,
            "y": 94.74,
            "r": 8,
            "label": "1: $6,255 FDV, 94.7% concentration (high risk)"
          },
          {
            "x": 5455.0,
            "y": 88.86,
            "r": 8,
            "label": "RWA: $5,455 FDV, 88.9% concentration (high risk)"
          },
          {
            "x": 4697.0,
            "y": 95.39,
            "r": 8,
            "label": "pibble: $4,697 FDV, 95.4% concentration (high risk)"
          },
          {
            "x": 14675.0,
            "y": 87.52,
            "r": 8,
            "label": "AUSBAGWORK: $14,675 FDV, 87.5% concentration (high risk)"
          },
          {
            "x": 10700.0,
            "y": 88.36,
            "r": 8,
            "label": "IDIOT: $10,700 FDV, 88.4% concentration (high risk)"
          },
          {
            "x": 4316.0,
            "y": 80.7,
            "r": 8,
            "label": "APOLLO: $4,316 FDV, 80.7% concentration (high risk)"
          },
          {
            "x": 7187.0,
            "y": 87.5,
            "r": 8,
            "label": "FARTWORM: $7,187 FDV, 87.5% concentration (high risk)"
          },
          {
            "x": 9115.0,
            "y": 88.92,
            "r": 8,
            "label": "DARE: $9,115 FDV, 88.9% concentration (high risk)"
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
            "x": 13759806.0,
            "y": 96.74,
            "r": 8,
            "label": "SOL: $13,759,806 FDV, 96.7% concentration (extreme risk)"
          },
          {
            "x": 6302.0,
            "y": 95.49,
            "r": 8,
            "label": "7: $6,302 FDV, 95.5% concentration (extreme risk)"
          },
          {
            "x": 4135.0,
            "y": 98.25,
            "r": 8,
            "label": "1% Club: $4,135 FDV, 98.2% concentration (extreme risk)"
          },
          {
            "x": 4874.0,
            "y": 97.15,
            "r": 8,
            "label": "BULLCOIN: $4,874 FDV, 97.2% concentration (extreme risk)"
          },
          {
            "x": 5415.98,
            "y": 100.0,
            "r": 8,
            "label": "4: $5,416 FDV, 100.0% concentration (extreme risk)"
          },
          {
            "x": 3499.0,
            "y": 99.74,
            "r": 8,
            "label": "MOONCOIN: $3,499 FDV, 99.7% concentration (extreme risk)"
          },
          {
            "x": 3920.0,
            "y": 99.09,
            "r": 8,
            "label": "GAZABOY: $3,920 FDV, 99.1% concentration (extreme risk)"
          },
          {
            "x": 5628.15,
            "y": 99.85,
            "r": 8,
            "label": "1cat: $5,628 FDV, 99.8% concentration (extreme risk)"
          },
          {
            "x": 4330.0,
            "y": 97.22,
            "r": 8,
            "label": "obvious: $4,330 FDV, 97.2% concentration (extreme risk)"
          },
          {
            "x": 4334.0,
            "y": 99.2,
            "r": 8,
            "label": "BEANS: $4,334 FDV, 99.2% concentration (extreme risk)"
          },
          {
            "x": 3997.0,
            "y": 97.66,
            "r": 8,
            "label": "BLUB: $3,997 FDV, 97.7% concentration (extreme risk)"
          },
          {
            "x": 3896.0,
            "y": 99.78,
            "r": 8,
            "label": "1SOL: $3,896 FDV, 99.8% concentration (extreme risk)"
          },
          {
            "x": 5555.96,
            "y": 99.85,
            "r": 8,
            "label": "2: $5,556 FDV, 99.8% concentration (extreme risk)"
          },
          {
            "x": 4226.0,
            "y": 98.9,
            "r": 8,
            "label": "19: $4,226 FDV, 98.9% concentration (extreme risk)"
          },
          {
            "x": 7918.0,
            "y": 94.27,
            "r": 8,
            "label": "SUPRACOIN: $7,918 FDV, 94.3% concentration (extreme risk)"
          },
          {
            "x": 4162.0,
            "y": 97.84,
            "r": 8,
            "label": "viewer: $4,162 FDV, 97.8% concentration (extreme risk)"
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
| 1 | XBT | XBT | 22.12% | 🟢 low | $89.44 | $605.42 |
| 2 | ELIZABETH | Just Elizabeth Cat | 26.00% | 🟢 low | $10.15 | $61.69 |
| 3 | RAGEGUY | Rage Guy | 27.93% | 🟢 low | $20.49K | $117.94K |
| 4 | DREAM | Dreamsync | 31.57% | 🟢 low | $125.99K | $178.41K |
| 5 | FLY | Nexa | 31.72% | 🟢 low | $201.62 | $2.30K |
| 6 | FARTLESS | FARTLESS COIN | 34.13% | 🟢 low | $761.30 | $3.65K |
| 7 | USDUT | unstable tether | 38.57% | 🟢 low | $2.51 | $52.77 |
| 8 | 1nu | 1nu | 39.17% | 🟢 low | $116.77K | $36.44K |
| 9 | USEFUL | USEFUL COIN | 40.87% | 🟢 low | $1.23 | $62.55 |
| 10 | AI20X | Ai20x.ai | 41.41% | 🟢 low | $57.45 | $2.29M |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | 4 | 4COIN | 100.00% | 🔴 extreme | $3.49 | $0.00 |
| 2 | 1cat | 1 cat can change your lif | 99.85% | 🔴 extreme | $1.50 | $0.00 |
| 3 | 2 | TWO IS BETTER THAN ONE | 99.85% | 🔴 extreme | $0.32 | $0.00 |
| 4 | 1SOL | 1SOL | 99.78% | 🔴 extreme | $0.33 | $7.74K |
| 5 | MOONCOIN | MOON COIN | 99.74% | 🔴 extreme | $2.99 | $6.94K |
| 6 | BEANS | BEANS | 99.20% | 🔴 extreme | $0.92 | $8.43K |
| 7 | GAZABOY | GAZA BOY | 99.09% | 🔴 extreme | $1.85 | $7.60K |
| 8 | 19 | Cult of 19 | 98.90% | 🔴 extreme | $0.26 | $7.85K |
| 9 | 1% Club | The 1% Club | 98.25% | 🔴 extreme | $314.04 | $6.75K |
| 10 | viewer | in a streamers world | 97.84% | 🔴 extreme | $0.19 | $7.97K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 44
**Combined 24h Volume**: $395.87M
**Combined Liquidity**: $61.59M

**Concentration Risk Distribution**:
- 🟢 Low: 16 tokens
- 🔴 Extreme: 16 tokens
- 🟡 High: 9 tokens
- 🟢 Medium: 2 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $395.41M | $56.38M | 🟢 unknown |
| 2 | DREAM | Dreamsync | $125.99K | $178.41K | 🟢 low |
| 3 | AI4 | AI⁴ | $118.64K | $103.68K | 🟢 low |
| 4 | 1nu | 1nu | $116.77K | $36.44K | 🟢 low |
| 5 | SHITTER | SHITTERCOIN | $26.05K | $24.40K | 🟢 low |
| 6 | RAGEGUY | Rage Guy | $20.49K | $117.94K | 🟢 low |
| 7 | HAROLD | Harold | $18.46K | $454.85K | 🟢 medium |
| 8 | LION | Loaded Lions | $15.83K | $1.70M | 🟢 low |
| 9 | SOL | Solana | $7.54K | $15.31K | 🔴 extreme |
| 10 | 1 | 1 pill can change your life | $4.54K | $11.73K | 🟡 high |

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
- 👀 **Watch**: 5 tokens

### 👀 Watch List

*5 tokens showing elevated activity*

📄 [Full data: signals_filtered.csv](data/signals_filtered.csv)

---

## 📈 Historical Data

**Total Historical Records**: 518
**Unique Tokens Tracked**: 102
**Date Range**: 2025-10-01 to 2025-10-16

**Master Aggregations**: 102 tokens
**Performance Metrics**: 518 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 518 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 102 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 518 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 44 |
| [new_viable.csv](data/new_viable.csv) | New tokens with potential | 0 |
| [signals_filtered.csv](data/signals_filtered.csv) | Whale-filtered trading signals | 5 |

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
