# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-11-06 08:45 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **40 tokens tracked** | 
💰 **$210.47M 24h volume** | 
💧 **$46.92M liquidity** | 
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
          4,
          5,
          15,
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
          -49.78622327790974,
          -49.78622327790974
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
      "1",
      "LION",
      "DREAM",
      "SHITTER",
      "RAGEGUY",
      "AI4",
      "pibble"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          365188.92,
          239562.37,
          37078.44,
          15985.65,
          13829.44,
          12400.94,
          10193.84,
          8685.63,
          7066.83,
          3988.52
        ],
        "backgroundColor": [
          "#22c55e",
          "#eab308",
          "#eab308",
          "#f97316",
          "#22c55e",
          "#22c55e",
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
      "2025-11-06"
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
          38.29
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
          69.09,
          93.12
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
          63.98
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
          69.09,
          93.12
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
            "x": 123383.0,
            "y": 38.29,
            "r": 8,
            "label": "1nu: $123,383 FDV, 38.3% concentration (low risk)"
          },
          {
            "x": 43144189.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $43,144,189 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 693223.0,
            "y": 33.15,
            "r": 8,
            "label": "DREAM: $693,223 FDV, 33.1% concentration (low risk)"
          },
          {
            "x": 31412.0,
            "y": 55.48,
            "r": 8,
            "label": "SHITTER: $31,412 FDV, 55.5% concentration (low risk)"
          },
          {
            "x": 495930.0,
            "y": 29.73,
            "r": 8,
            "label": "RAGEGUY: $495,930 FDV, 29.7% concentration (low risk)"
          },
          {
            "x": 187546.0,
            "y": 53.83,
            "r": 8,
            "label": "AI4: $187,546 FDV, 53.8% concentration (low risk)"
          },
          {
            "x": 392664.0,
            "y": 36.07,
            "r": 8,
            "label": "FARTLESS: $392,664 FDV, 36.1% concentration (low risk)"
          },
          {
            "x": 62927.0,
            "y": 59.8,
            "r": 8,
            "label": "RUECAT: $62,927 FDV, 59.8% concentration (low risk)"
          },
          {
            "x": 18207.0,
            "y": 28.94,
            "r": 8,
            "label": "FLY: $18,207 FDV, 28.9% concentration (low risk)"
          },
          {
            "x": 1031987.0,
            "y": 25.33,
            "r": 8,
            "label": "XBT: $1,031,987 FDV, 25.3% concentration (low risk)"
          },
          {
            "x": 341452.0,
            "y": 37.39,
            "r": 8,
            "label": "ELIZABETH: $341,452 FDV, 37.4% concentration (low risk)"
          },
          {
            "x": 118687.0,
            "y": 41.65,
            "r": 8,
            "label": "USDUT: $118,687 FDV, 41.6% concentration (low risk)"
          },
          {
            "x": 112815.0,
            "y": 46.19,
            "r": 8,
            "label": "USEFUL: $112,815 FDV, 46.2% concentration (low risk)"
          },
          {
            "x": 124363.0,
            "y": 46.49,
            "r": 8,
            "label": "gib: $124,363 FDV, 46.5% concentration (low risk)"
          },
          {
            "x": 97053.0,
            "y": 44.37,
            "r": 8,
            "label": "YAO: $97,053 FDV, 44.4% concentration (low risk)"
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
            "x": 12632.0,
            "y": 69.09,
            "r": 8,
            "label": "1: $12,632 FDV, 69.1% concentration (medium risk)"
          },
          {
            "x": 3354522.0,
            "y": 63.98,
            "r": 8,
            "label": "HAROLD: $3,354,522 FDV, 64.0% concentration (medium risk)"
          },
          {
            "x": 6321.0,
            "y": 75.14,
            "r": 8,
            "label": "APOLLO: $6,321 FDV, 75.1% concentration (medium risk)"
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
            "x": 6337.0,
            "y": 93.12,
            "r": 8,
            "label": "1: $6,337 FDV, 93.1% concentration (high risk)"
          },
          {
            "x": 5059.0,
            "y": 94.44,
            "r": 8,
            "label": "pibble: $5,059 FDV, 94.4% concentration (high risk)"
          },
          {
            "x": 4637.0,
            "y": 94.24,
            "r": 8,
            "label": "RWA: $4,637 FDV, 94.2% concentration (high risk)"
          },
          {
            "x": 8386.0,
            "y": 81.56,
            "r": 8,
            "label": "1Bull: $8,386 FDV, 81.6% concentration (high risk)"
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
            "x": 13534430.0,
            "y": 96.8,
            "r": 8,
            "label": "SOL: $13,534,430 FDV, 96.8% concentration (extreme risk)"
          },
          {
            "x": 3331.0,
            "y": 98.97,
            "r": 8,
            "label": "1% Club: $3,331 FDV, 99.0% concentration (extreme risk)"
          },
          {
            "x": 4685.75,
            "y": 99.9,
            "r": 8,
            "label": "1cat: $4,686 FDV, 99.9% concentration (extreme risk)"
          },
          {
            "x": 3498.0,
            "y": 97.23,
            "r": 8,
            "label": "Streamless: $3,498 FDV, 97.2% concentration (extreme risk)"
          },
          {
            "x": 8706.0,
            "y": 94.19,
            "r": 8,
            "label": "MOCHI: $8,706 FDV, 94.2% concentration (extreme risk)"
          },
          {
            "x": 2987.0,
            "y": 99.39,
            "r": 8,
            "label": "MMGA: $2,987 FDV, 99.4% concentration (extreme risk)"
          },
          {
            "x": 2986.0,
            "y": 99.9,
            "r": 8,
            "label": "BONKZ: $2,986 FDV, 99.9% concentration (extreme risk)"
          },
          {
            "x": 2932.0,
            "y": 99.67,
            "r": 8,
            "label": "ORE: $2,932 FDV, 99.7% concentration (extreme risk)"
          },
          {
            "x": 3433.0,
            "y": 99.38,
            "r": 8,
            "label": "BEANIE: $3,433 FDV, 99.4% concentration (extreme risk)"
          },
          {
            "x": 3568.0,
            "y": 97.61,
            "r": 8,
            "label": "obvious: $3,568 FDV, 97.6% concentration (extreme risk)"
          },
          {
            "x": 3877.0,
            "y": 96.41,
            "r": 8,
            "label": "7: $3,877 FDV, 96.4% concentration (extreme risk)"
          },
          {
            "x": 3175.0,
            "y": 99.24,
            "r": 8,
            "label": "SLOW: $3,175 FDV, 99.2% concentration (extreme risk)"
          },
          {
            "x": 3153.0,
            "y": 99.75,
            "r": 8,
            "label": "Supershiro: $3,153 FDV, 99.8% concentration (extreme risk)"
          },
          {
            "x": 3272.0,
            "y": 97.85,
            "r": 8,
            "label": "BLUB: $3,272 FDV, 97.8% concentration (extreme risk)"
          },
          {
            "x": 4692.26,
            "y": 99.8,
            "r": 8,
            "label": "YARA: $4,692 FDV, 99.8% concentration (extreme risk)"
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
| 1 | XBT | XBT | 25.33% | 🟢 low | $21.54 | $436.67 |
| 2 | FLY | Nexa | 28.94% | 🟢 low | $49.35 | $133.27 |
| 3 | RAGEGUY | Rage Guy | 29.73% | 🟢 low | $8.69K | $97.04K |
| 4 | DREAM | Dreamsync | 33.15% | 🟢 low | $12.40K | $102.67K |
| 5 | FARTLESS | FARTLESS COIN | 36.07% | 🟢 low | $532.70 | $2.61K |
| 6 | ELIZABETH | Just Elizabeth Cat | 37.39% | 🟢 low | $2.51 | $28.65 |
| 7 | 1nu | 1nu | 38.29% | 🟢 low | $365.19K | $47.35K |
| 8 | USDUT | unstable tether | 41.65% | 🟢 low | $1.55 | $39.14 |
| 9 | YAO | YAO MING | 44.37% | 🟢 low | $0.39 | $632.57 |
| 10 | USEFUL | USEFUL COIN | 46.19% | 🟢 low | $1.21 | $34.13 |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | 1cat | 1 cat can change your lif | 99.90% | 🔴 extreme | $308.45 | $0.00 |
| 2 | BONKZ | Bonkzilla | 99.90% | 🔴 extreme | $20.54 | $5.62K |
| 3 | YARA | Justice for Yara | 99.80% | 🔴 extreme | $0.00 | $0.00 |
| 4 | Supershiro | Super Shiro | 99.75% | 🔴 extreme | $1.66 | $5.98K |
| 5 | ORE | Ore Labs | 99.67% | 🔴 extreme | $5.12 | $5.79K |
| 6 | MMGA | MAKE MEMES GREAT AGAIN | 99.39% | 🔴 extreme | $155.62 | $5.81K |
| 7 | BEANIE | BEANIE | 99.38% | 🔴 extreme | $4.43 | $6.62K |
| 8 | SLOW | Slow Runner | 99.24% | 🔴 extreme | $2.38 | $6.28K |
| 9 | 1% Club | The 1% Club | 98.97% | 🔴 extreme | $1.55K | $6.07K |
| 10 | BLUB | Blub | 97.85% | 🔴 extreme | $0.50 | $6.29K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 40
**Combined 24h Volume**: $210.47M
**Combined Liquidity**: $46.92M

**Concentration Risk Distribution**:
- 🟢 Low: 15 tokens
- 🔴 Extreme: 15 tokens
- 🟡 High: 5 tokens
- 🟢 Medium: 4 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $209.75M | $44.60M | 🟢 unknown |
| 2 | 1nu | 1nu | $365.19K | $47.35K | 🟢 low |
| 3 | 1 | 1 pill can change your life | $239.56K | $12.03K | 🟢 medium |
| 4 | HAROLD | Harold | $37.08K | $454.17K | 🟢 medium |
| 5 | 1 | 1 pill can change your life | $15.99K | $9.39K | 🟡 high |
| 6 | LION | Loaded Lions | $13.83K | $1.32M | 🟢 low |
| 7 | DREAM | Dreamsync | $12.40K | $102.67K | 🟢 low |
| 8 | SHITTER | SHITTERCOIN | $10.19K | $24.30K | 🟢 low |
| 9 | RAGEGUY | Rage Guy | $8.69K | $97.04K | 🟢 low |
| 10 | AI4 | AI⁴ | $7.07K | $75.17K | 🟢 low |

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
- ❄️ **Cooling**: 2 tokens

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

**Total Historical Records**: 514
**Unique Tokens Tracked**: 101
**Date Range**: 2025-10-01 to 2025-11-06

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
| [signals_filtered.csv](data/signals_filtered.csv) | Whale-filtered trading signals | 126 |

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
