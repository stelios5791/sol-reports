# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-10-15 22:17 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **40 tokens tracked** | 
💰 **$439.27M 24h volume** | 
💧 **$61.80M liquidity** | 
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
          8,
          13,
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
          -5.454278153484275,
          -5.454278153484275
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
      "LION",
      "SHITTER",
      "RAGEGUY",
      "HAROLD",
      "1",
      "1",
      "7"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          145506.02,
          103284.86,
          77733.88,
          33452.68,
          23241.24,
          14878.13,
          8432.31,
          2096.07,
          1936.66,
          1932.75
        ],
        "backgroundColor": [
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#f97316",
          "#f97316",
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
      "2025-10-15"
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
          47.44
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
          31.62
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
          38.45
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
        "label": "SHITTER",
        "data": [
          0.0,
          0.0,
          0.0,
          0.0,
          64.26,
          64.33,
          63.23,
          56.48
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
            "x": 326439.0,
            "y": 47.44,
            "r": 8,
            "label": "AI4: $326,439 FDV, 47.4% concentration (low risk)"
          },
          {
            "x": 1761415.0,
            "y": 31.62,
            "r": 8,
            "label": "DREAM: $1,761,415 FDV, 31.6% concentration (low risk)"
          },
          {
            "x": 85528.0,
            "y": 38.45,
            "r": 8,
            "label": "1nu: $85,528 FDV, 38.5% concentration (low risk)"
          },
          {
            "x": 59082790.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $59,082,790 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 31404.0,
            "y": 56.48,
            "r": 8,
            "label": "SHITTER: $31,404 FDV, 56.5% concentration (low risk)"
          },
          {
            "x": 665124.0,
            "y": 27.59,
            "r": 8,
            "label": "RAGEGUY: $665,124 FDV, 27.6% concentration (low risk)"
          },
          {
            "x": 104618.0,
            "y": 52.62,
            "r": 8,
            "label": "RUECAT: $104,618 FDV, 52.6% concentration (low risk)"
          },
          {
            "x": 811998.0,
            "y": 33.83,
            "r": 8,
            "label": "FARTLESS: $811,998 FDV, 33.8% concentration (low risk)"
          },
          {
            "x": 16583.0,
            "y": 31.52,
            "r": 8,
            "label": "FLY: $16,583 FDV, 31.5% concentration (low risk)"
          },
          {
            "x": 32564.0,
            "y": 57.12,
            "r": 8,
            "label": "$CrepSol: $32,564 FDV, 57.1% concentration (low risk)"
          },
          {
            "x": 19339910.0,
            "y": 41.41,
            "r": 8,
            "label": "AI20X: $19,339,910 FDV, 41.4% concentration (low risk)"
          },
          {
            "x": 1255687.0,
            "y": 26.68,
            "r": 8,
            "label": "ELIZABETH: $1,255,687 FDV, 26.7% concentration (low risk)"
          },
          {
            "x": 203179.0,
            "y": 38.83,
            "r": 8,
            "label": "USDUT: $203,179 FDV, 38.8% concentration (low risk)"
          },
          {
            "x": 169930.0,
            "y": 40.03,
            "r": 8,
            "label": "USEFUL: $169,930 FDV, 40.0% concentration (low risk)"
          },
          {
            "x": 268430.0,
            "y": 46.25,
            "r": 8,
            "label": "gib: $268,430 FDV, 46.2% concentration (low risk)"
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
            "x": 2959061.0,
            "y": 62.89,
            "r": 8,
            "label": "HAROLD: $2,959,061 FDV, 62.9% concentration (medium risk)"
          },
          {
            "x": 25939.0,
            "y": 75.41,
            "r": 8,
            "label": "1Bull: $25,939 FDV, 75.4% concentration (medium risk)"
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
            "x": 6798.0,
            "y": 92.61,
            "r": 8,
            "label": "1: $6,798 FDV, 92.6% concentration (high risk)"
          },
          {
            "x": 6430.0,
            "y": 94.72,
            "r": 8,
            "label": "1: $6,430 FDV, 94.7% concentration (high risk)"
          },
          {
            "x": 16193.0,
            "y": 86.59,
            "r": 8,
            "label": "AUSBAGWORK: $16,193 FDV, 86.6% concentration (high risk)"
          },
          {
            "x": 5478.0,
            "y": 88.86,
            "r": 8,
            "label": "RWA: $5,478 FDV, 88.9% concentration (high risk)"
          },
          {
            "x": 4713.0,
            "y": 79.96,
            "r": 8,
            "label": "APOLLO: $4,713 FDV, 80.0% concentration (high risk)"
          },
          {
            "x": 9642.0,
            "y": 88.99,
            "r": 8,
            "label": "DARE: $9,642 FDV, 89.0% concentration (high risk)"
          },
          {
            "x": 7274.0,
            "y": 87.49,
            "r": 8,
            "label": "FARTWORM: $7,274 FDV, 87.5% concentration (high risk)"
          },
          {
            "x": 11996.0,
            "y": 86.75,
            "r": 8,
            "label": "IDIOT: $11,996 FDV, 86.8% concentration (high risk)"
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
            "x": 6500.0,
            "y": 95.36,
            "r": 8,
            "label": "7: $6,500 FDV, 95.4% concentration (extreme risk)"
          },
          {
            "x": 7534455.0,
            "y": 96.67,
            "r": 8,
            "label": "SOL: $7,534,455 FDV, 96.7% concentration (extreme risk)"
          },
          {
            "x": 4135.0,
            "y": 98.25,
            "r": 8,
            "label": "1% Club: $4,135 FDV, 98.2% concentration (extreme risk)"
          },
          {
            "x": 5005.0,
            "y": 97.15,
            "r": 8,
            "label": "BULLCOIN: $5,005 FDV, 97.2% concentration (extreme risk)"
          },
          {
            "x": 5415.98,
            "y": 100.0,
            "r": 8,
            "label": "4: $5,416 FDV, 100.0% concentration (extreme risk)"
          },
          {
            "x": 3920.0,
            "y": 99.07,
            "r": 8,
            "label": "GAZABOY: $3,920 FDV, 99.1% concentration (extreme risk)"
          },
          {
            "x": 4065.0,
            "y": 99.71,
            "r": 8,
            "label": "MINDWORMS: $4,065 FDV, 99.7% concentration (extreme risk)"
          },
          {
            "x": 4563.0,
            "y": 96.85,
            "r": 8,
            "label": "Streamless: $4,563 FDV, 96.8% concentration (extreme risk)"
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
            "x": 4580.0,
            "y": 99.17,
            "r": 8,
            "label": "BEANS: $4,580 FDV, 99.2% concentration (extreme risk)"
          },
          {
            "x": 4226.0,
            "y": 98.9,
            "r": 8,
            "label": "19: $4,226 FDV, 98.9% concentration (extreme risk)"
          },
          {
            "x": 4028.0,
            "y": 99.67,
            "r": 8,
            "label": "KENNY: $4,028 FDV, 99.7% concentration (extreme risk)"
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
| 1 | XBT | XBT | 22.01% | 🟢 low | $0.66 | $0.00 |
| 2 | ELIZABETH | Just Elizabeth Cat | 26.68% | 🟢 low | $9.56 | $54.44 |
| 3 | RAGEGUY | Rage Guy | 27.59% | 🟢 low | $14.88K | $122.74K |
| 4 | FLY | Nexa | 31.52% | 🟢 low | $316.67 | $2.38K |
| 5 | DREAM | Dreamsync | 31.62% | 🟢 low | $103.28K | $180.45K |
| 6 | FARTLESS | FARTLESS COIN | 33.83% | 🟢 low | $816.50 | $3.71K |
| 7 | 1nu | 1nu | 38.45% | 🟢 low | $77.73K | $37.74K |
| 8 | USDUT | unstable tether | 38.83% | 🟢 low | $5.09 | $52.77 |
| 9 | USEFUL | USEFUL COIN | 40.03% | 🟢 low | $1.02 | $63.71 |
| 10 | AI20X | Ai20x.ai | 41.41% | 🟢 low | $57.45 | $2.29M |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | 4 | 4COIN | 100.00% | 🔴 extreme | $3.49 | $0.00 |
| 2 | 2 | TWO IS BETTER THAN ONE | 99.85% | 🔴 extreme | $0.32 | $0.00 |
| 3 | 1SOL | 1SOL | 99.78% | 🔴 extreme | $0.33 | $7.74K |
| 4 | MINDWORMS | mindworms | 99.71% | 🔴 extreme | $1.25 | $7.71K |
| 5 | KENNY | KENNY KO | 99.67% | 🔴 extreme | $0.22 | $7.62K |
| 6 | BEANS | BEANS | 99.17% | 🔴 extreme | $0.31 | $8.91K |
| 7 | GAZABOY | GAZA BOY | 99.07% | 🔴 extreme | $1.85 | $7.60K |
| 8 | 19 | Cult of 19 | 98.90% | 🔴 extreme | $0.26 | $7.85K |
| 9 | 1% Club | The 1% Club | 98.25% | 🔴 extreme | $314.04 | $6.75K |
| 10 | BULLCOIN | BULLCOIN | 97.15% | 🔴 extreme | $6.49 | $8.62K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 40
**Combined 24h Volume**: $439.27M
**Combined Liquidity**: $61.80M

**Concentration Risk Distribution**:
- 🟢 Low: 16 tokens
- 🔴 Extreme: 13 tokens
- 🟡 High: 8 tokens
- 🟢 Medium: 2 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $438.85M | $56.60M | 🟢 unknown |
| 2 | AI4 | AI⁴ | $145.51K | $106.53K | 🟢 low |
| 3 | DREAM | Dreamsync | $103.28K | $180.45K | 🟢 low |
| 4 | 1nu | 1nu | $77.73K | $37.74K | 🟢 low |
| 5 | LION | Loaded Lions | $33.45K | $1.70M | 🟢 low |
| 6 | SHITTER | SHITTERCOIN | $23.24K | $24.09K | 🟢 low |
| 7 | RAGEGUY | Rage Guy | $14.88K | $122.74K | 🟢 low |
| 8 | HAROLD | Harold | $8.43K | $469.56K | 🟢 medium |
| 9 | 1 | 1 pill can change your life | $2.10K | $10.74K | 🟡 high |
| 10 | 1 | 1 pill can change your life | $1.94K | $9.47K | 🟡 high |

📄 [Full data: daily_top50.csv](data/daily_top50.csv)

---

## 🌱 New Viable Tokens (7-14 Days Old)

New tokens showing potential with healthy metrics and lower concentration risk.

**Found**: 3 viable new tokens

**Criteria**:
- First seen 7-14 days ago
- Volume > $50K
- Liquidity > $100K
- Missing streak < 2 (stable presence)
- Concentration risk: low/medium

| Symbol | Name | Age (days) | Volume 24h | Liquidity | Top 10% |
|--------|------|------------|------------|-----------|---------|
| wSOL | Wrapped SOL | 14 | $438.85M | $56.60M | 0.00% |
| AI4 | AI⁴ | 14 | $145.51K | $106.53K | 47.44% |
| DREAM | Dreamsync | 14 | $103.28K | $180.45K | 31.62% |

📄 [Full data: new_viable.csv](data/new_viable.csv)

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
- 👀 **Watch**: 3 tokens
- 🚀 **Breakout**: 1 tokens

### 🚀 Breakout Signals

| Symbol | Score | Vol 3v1 | Z-Score Vol | Liq 3d | Streak |
|--------|-------|---------|-------------|--------|--------|
| wSOL | 57502.42 | 2.68x | 1.59 | $57.49M | 1d |

### 👀 Watch List

*3 tokens showing elevated activity*

📄 [Full data: signals_filtered.csv](data/signals_filtered.csv)

---

## 📈 Historical Data

**Total Historical Records**: 514
**Unique Tokens Tracked**: 102
**Date Range**: 2025-10-01 to 2025-10-15

**Master Aggregations**: 102 tokens
**Performance Metrics**: 514 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 514 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 102 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 514 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 40 |
| [new_viable.csv](data/new_viable.csv) | New tokens with potential | 3 |
| [signals_filtered.csv](data/signals_filtered.csv) | Whale-filtered trading signals | 4 |

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
