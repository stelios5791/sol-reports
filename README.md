# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-10-19 17:40 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **38 tokens tracked** | 
💰 **$161.72M 24h volume** | 
💧 **$57.94M liquidity** | 
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
          3,
          8,
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
          -35.4388843314192,
          -35.4388843314192
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
      "RAGEGUY",
      "1nu",
      "LION",
      "1Bull",
      "HAROLD",
      "$CrepSol",
      "19",
      "FARTLESS"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          84584.84,
          76573.86,
          73884.6,
          24222.59,
          5138.18,
          5044.54,
          1587.09,
          1360.86,
          1186.62,
          631.35
        ],
        "backgroundColor": [
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#eab308",
          "#22c55e",
          "#ef4444",
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
      "2025-10-03",
      "2025-10-04",
      "2025-10-05",
      "2025-10-06",
      "2025-10-07",
      "2025-10-19"
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
          31.81
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
          49.34
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
          26.99
        ],
        "borderColor": "#22c55e",
        "backgroundColor": "#22c55e20",
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
          41.54
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
            "x": 1608569.0,
            "y": 31.81,
            "r": 8,
            "label": "DREAM: $1,608,569 FDV, 31.8% concentration (low risk)"
          },
          {
            "x": 190148.0,
            "y": 49.34,
            "r": 8,
            "label": "AI4: $190,148 FDV, 49.3% concentration (low risk)"
          },
          {
            "x": 870787.0,
            "y": 26.99,
            "r": 8,
            "label": "RAGEGUY: $870,787 FDV, 27.0% concentration (low risk)"
          },
          {
            "x": 65308.0,
            "y": 41.54,
            "r": 8,
            "label": "1nu: $65,308 FDV, 41.5% concentration (low risk)"
          },
          {
            "x": 55884085.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $55,884,085 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 34665.0,
            "y": 57.64,
            "r": 8,
            "label": "$CrepSol: $34,665 FDV, 57.6% concentration (low risk)"
          },
          {
            "x": 722127.0,
            "y": 34.82,
            "r": 8,
            "label": "FARTLESS: $722,127 FDV, 34.8% concentration (low risk)"
          },
          {
            "x": 90105.0,
            "y": 54.22,
            "r": 8,
            "label": "RUECAT: $90,105 FDV, 54.2% concentration (low risk)"
          },
          {
            "x": 1661261.0,
            "y": 22.34,
            "r": 8,
            "label": "XBT: $1,661,261 FDV, 22.3% concentration (low risk)"
          },
          {
            "x": 17969.0,
            "y": 30.33,
            "r": 8,
            "label": "FLY: $17,969 FDV, 30.3% concentration (low risk)"
          },
          {
            "x": 976081.0,
            "y": 27.41,
            "r": 8,
            "label": "ELIZABETH: $976,081 FDV, 27.4% concentration (low risk)"
          },
          {
            "x": 106845.0,
            "y": 44.51,
            "r": 8,
            "label": "YAO: $106,845 FDV, 44.5% concentration (low risk)"
          },
          {
            "x": 18266908.0,
            "y": 39.75,
            "r": 8,
            "label": "AI20X: $18,266,908 FDV, 39.8% concentration (low risk)"
          },
          {
            "x": 249680.0,
            "y": 45.87,
            "r": 8,
            "label": "gib: $249,680 FDV, 45.9% concentration (low risk)"
          },
          {
            "x": 130702.0,
            "y": 44.18,
            "r": 8,
            "label": "USEFUL: $130,702 FDV, 44.2% concentration (low risk)"
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
            "x": 9930.0,
            "y": 78.22,
            "r": 8,
            "label": "1Bull: $9,930 FDV, 78.2% concentration (medium risk)"
          },
          {
            "x": 3057350.0,
            "y": 63.56,
            "r": 8,
            "label": "HAROLD: $3,057,350 FDV, 63.6% concentration (medium risk)"
          },
          {
            "x": 22520.0,
            "y": 64.53,
            "r": 8,
            "label": "SHITTER: $22,520 FDV, 64.5% concentration (medium risk)"
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
            "x": 10572.0,
            "y": 92.61,
            "r": 8,
            "label": "MOCHI: $10,572 FDV, 92.6% concentration (high risk)"
          },
          {
            "x": 6727.0,
            "y": 88.22,
            "r": 8,
            "label": "FARTWORM: $6,727 FDV, 88.2% concentration (high risk)"
          },
          {
            "x": 5446.0,
            "y": 90.0,
            "r": 8,
            "label": "RWA: $5,446 FDV, 90.0% concentration (high risk)"
          },
          {
            "x": 4332.0,
            "y": 81.08,
            "r": 8,
            "label": "APOLLO: $4,332 FDV, 81.1% concentration (high risk)"
          },
          {
            "x": 6091.0,
            "y": 93.39,
            "r": 8,
            "label": "1: $6,091 FDV, 93.4% concentration (high risk)"
          },
          {
            "x": 14258.0,
            "y": 88.11,
            "r": 8,
            "label": "AUSBAGWORK: $14,258 FDV, 88.1% concentration (high risk)"
          },
          {
            "x": 8734.0,
            "y": 88.98,
            "r": 8,
            "label": "DARE: $8,734 FDV, 89.0% concentration (high risk)"
          },
          {
            "x": 9719.0,
            "y": 89.36,
            "r": 8,
            "label": "IDIOT: $9,719 FDV, 89.4% concentration (high risk)"
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
            "x": 4253.0,
            "y": 98.52,
            "r": 8,
            "label": "19: $4,253 FDV, 98.5% concentration (extreme risk)"
          },
          {
            "x": 12045374.0,
            "y": 96.74,
            "r": 8,
            "label": "SOL: $12,045,374 FDV, 96.7% concentration (extreme risk)"
          },
          {
            "x": 7318.0,
            "y": 94.93,
            "r": 8,
            "label": "SUPRACOIN: $7,318 FDV, 94.9% concentration (extreme risk)"
          },
          {
            "x": 3935.0,
            "y": 97.66,
            "r": 8,
            "label": "1: $3,935 FDV, 97.7% concentration (extreme risk)"
          },
          {
            "x": 4131.0,
            "y": 96.95,
            "r": 8,
            "label": "Streamless: $4,131 FDV, 97.0% concentration (extreme risk)"
          },
          {
            "x": 6009.0,
            "y": 95.45,
            "r": 8,
            "label": "7: $6,009 FDV, 95.5% concentration (extreme risk)"
          },
          {
            "x": 3702.0,
            "y": 99.67,
            "r": 8,
            "label": "KENNY: $3,702 FDV, 99.7% concentration (extreme risk)"
          },
          {
            "x": 3691.0,
            "y": 99.57,
            "r": 8,
            "label": "Supershiro: $3,691 FDV, 99.6% concentration (extreme risk)"
          },
          {
            "x": 4688.0,
            "y": 97.18,
            "r": 8,
            "label": "BULLCOIN: $4,688 FDV, 97.2% concentration (extreme risk)"
          },
          {
            "x": 4624.0,
            "y": 98.57,
            "r": 8,
            "label": "Noxi: $4,624 FDV, 98.6% concentration (extreme risk)"
          },
          {
            "x": 3372.0,
            "y": 99.99,
            "r": 8,
            "label": "UPC: $3,372 FDV, 100.0% concentration (extreme risk)"
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
| 1 | XBT | XBT | 22.34% | 🟢 low | $74.39 | $606.99 |
| 2 | RAGEGUY | Rage Guy | 26.99% | 🟢 low | $73.88K | $139.99K |
| 3 | ELIZABETH | Just Elizabeth Cat | 27.41% | 🟢 low | $23.10 | $47.99 |
| 4 | FLY | Nexa | 30.33% | 🟢 low | $56.18 | $2.46K |
| 5 | DREAM | Dreamsync | 31.81% | 🟢 low | $84.58K | $170.40K |
| 6 | FARTLESS | FARTLESS COIN | 34.82% | 🟢 low | $631.35 | $3.51K |
| 7 | AI20X | Ai20x.ai | 39.75% | 🟢 low | $8.05 | $2.17M |
| 8 | 1nu | 1nu | 41.54% | 🟢 low | $24.22K | $33.26K |
| 9 | USEFUL | USEFUL COIN | 44.18% | 🟢 low | $1.73 | $51.90 |
| 10 | YAO | YAO MING | 44.51% | 🟢 low | $17.96 | $746.22 |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | UPC | Upcoin | 99.99% | 🔴 extreme | $0.13 | $6.71K |
| 2 | KENNY | KENNY KO | 99.67% | 🔴 extreme | $1.20 | $7.00K |
| 3 | Supershiro | Super Shiro | 99.57% | 🔴 extreme | $0.98 | $6.98K |
| 4 | Noxi | Noxi Labs AI | 98.57% | 🔴 extreme | $0.23 | $40.29 |
| 5 | 19 | Cult of 19 | 98.52% | 🔴 extreme | $1.19K | $7.62K |
| 6 | 1 | 1 pill can change your li | 97.66% | 🔴 extreme | $44.88 | $7.30K |
| 7 | BULLCOIN | BULLCOIN | 97.18% | 🔴 extreme | $0.46 | $8.08K |
| 8 | Streamless | Streamless coin | 96.95% | 🔴 extreme | $16.53 | $7.85K |
| 9 | SOL | Solana | 96.74% | 🔴 extreme | $484.47 | $14.29K |
| 10 | 7 | 7 Coin | 95.45% | 🔴 extreme | $2.97 | $9.35K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 38
**Combined 24h Volume**: $161.72M
**Combined Liquidity**: $57.94M

**Concentration Risk Distribution**:
- 🟢 Low: 15 tokens
- 🔴 Extreme: 11 tokens
- 🟡 High: 8 tokens
- 🟢 Medium: 3 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $161.44M | $52.95M | 🟢 unknown |
| 2 | DREAM | Dreamsync | $84.58K | $170.40K | 🟢 low |
| 3 | AI4 | AI⁴ | $76.57K | $81.18K | 🟢 low |
| 4 | RAGEGUY | Rage Guy | $73.88K | $139.99K | 🟢 low |
| 5 | 1nu | 1nu | $24.22K | $33.26K | 🟢 low |
| 6 | LION | Loaded Lions | $5.14K | $1.64M | 🟢 low |
| 7 | 1Bull | One bull run to change your li | $5.04K | $11.89K | 🟢 medium |
| 8 | HAROLD | Harold | $1.59K | $474.18K | 🟢 medium |
| 9 | $CrepSol | Crepe on Solana | $1.36K | $21.74K | 🟢 low |
| 10 | 19 | Cult of 19 | $1.19K | $7.62K | 🔴 extreme |

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
- 👀 **Watch**: 111 tokens
- 🚀 **Breakout**: 3 tokens
- ❄️ **Cooling**: 1 tokens

### 🚀 Breakout Signals

| Symbol | Score | Vol 3v1 | Z-Score Vol | Liq 3d | Streak |
|--------|-------|---------|-------------|--------|--------|
| wSOL | 4.24 | 2.51x | 1.69 | $57.82M | 0d |
| XBT | 3.65 | 2.10x | 1.74 | $421.14K | 0d |
| USDUT | 3.57 | 2.36x | 1.51 | $150.84K | 0d |

### 👀 Watch List

*111 tokens showing elevated activity*

📄 [Full data: signals_filtered.csv](data/signals_filtered.csv)

---

## 📈 Historical Data

**Total Historical Records**: 512
**Unique Tokens Tracked**: 101
**Date Range**: 2025-10-01 to 2025-10-19

**Master Aggregations**: 101 tokens
**Performance Metrics**: 512 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 512 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 101 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 512 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 38 |
| [new_viable.csv](data/new_viable.csv) | New tokens with potential | 0 |
| [signals_filtered.csv](data/signals_filtered.csv) | Whale-filtered trading signals | 115 |

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
