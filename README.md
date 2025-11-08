# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-11-08 17:21 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **29 tokens tracked** | 
💰 **$191.35M 24h volume** | 
💧 **$45.42M liquidity** | 
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
          4,
          5,
          5,
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
          -43.54092152324848,
          -43.54092152324848
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
      "LION",
      "1nu",
      "DREAM",
      "RAGEGUY",
      "HAROLD",
      "1",
      "AI4",
      "SOL",
      "RUECAT",
      "1Bull"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          23126.85,
          17654.4,
          13189.15,
          11125.21,
          9709.31,
          4549.53,
          3320.74,
          1392.5,
          890.65,
          385.33
        ],
        "backgroundColor": [
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#f97316",
          "#22c55e",
          "#ef4444",
          "#eab308",
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
      "2025-11-08"
    ],
    "datasets": [
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
          45.46
        ],
        "borderColor": "#ef4444",
        "backgroundColor": "#ef444420",
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
          30.87
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
          64.12
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
            "x": 42521606.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $42,521,606 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 78250.0,
            "y": 45.46,
            "r": 8,
            "label": "1nu: $78,250 FDV, 45.5% concentration (low risk)"
          },
          {
            "x": 699086.0,
            "y": 33.06,
            "r": 8,
            "label": "DREAM: $699,086 FDV, 33.1% concentration (low risk)"
          },
          {
            "x": 391029.0,
            "y": 30.87,
            "r": 8,
            "label": "RAGEGUY: $391,029 FDV, 30.9% concentration (low risk)"
          },
          {
            "x": 186871.0,
            "y": 54.11,
            "r": 8,
            "label": "AI4: $186,871 FDV, 54.1% concentration (low risk)"
          },
          {
            "x": 29159.0,
            "y": 57.28,
            "r": 8,
            "label": "SHITTER: $29,159 FDV, 57.3% concentration (low risk)"
          },
          {
            "x": 348236.0,
            "y": 36.98,
            "r": 8,
            "label": "FARTLESS: $348,236 FDV, 37.0% concentration (low risk)"
          },
          {
            "x": 813795.0,
            "y": 26.65,
            "r": 8,
            "label": "XBT: $813,795 FDV, 26.6% concentration (low risk)"
          },
          {
            "x": 533739.0,
            "y": 35.29,
            "r": 8,
            "label": "ELIZABETH: $533,739 FDV, 35.3% concentration (low risk)"
          },
          {
            "x": 20617.0,
            "y": 27.46,
            "r": 8,
            "label": "FLY: $20,617 FDV, 27.5% concentration (low risk)"
          },
          {
            "x": 144819.0,
            "y": 46.54,
            "r": 8,
            "label": "gib: $144,819 FDV, 46.5% concentration (low risk)"
          },
          {
            "x": 89826.0,
            "y": 42.66,
            "r": 8,
            "label": "YAO: $89,826 FDV, 42.7% concentration (low risk)"
          },
          {
            "x": 119749.0,
            "y": 46.37,
            "r": 8,
            "label": "USEFUL: $119,749 FDV, 46.4% concentration (low risk)"
          },
          {
            "x": 106480.0,
            "y": 42.31,
            "r": 8,
            "label": "USDUT: $106,480 FDV, 42.3% concentration (low risk)"
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
            "x": 3192113.0,
            "y": 64.12,
            "r": 8,
            "label": "HAROLD: $3,192,113 FDV, 64.1% concentration (medium risk)"
          },
          {
            "x": 62742.0,
            "y": 61.32,
            "r": 8,
            "label": "RUECAT: $62,742 FDV, 61.3% concentration (medium risk)"
          },
          {
            "x": 14261.0,
            "y": 66.09,
            "r": 8,
            "label": "$CrepSol: $14,261 FDV, 66.1% concentration (medium risk)"
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
            "x": 9504.0,
            "y": 80.4,
            "r": 8,
            "label": "1: $9,504 FDV, 80.4% concentration (high risk)"
          },
          {
            "x": 8679.0,
            "y": 81.19,
            "r": 8,
            "label": "1Bull: $8,679 FDV, 81.2% concentration (high risk)"
          },
          {
            "x": 4951.0,
            "y": 95.6,
            "r": 8,
            "label": "pibble: $4,951 FDV, 95.6% concentration (high risk)"
          },
          {
            "x": 10461.0,
            "y": 90.17,
            "r": 8,
            "label": "AUSBAGWORK: $10,461 FDV, 90.2% concentration (high risk)"
          },
          {
            "x": 4916.0,
            "y": 92.22,
            "r": 8,
            "label": "FARTWORM: $4,916 FDV, 92.2% concentration (high risk)"
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
            "x": 12556284.0,
            "y": 96.8,
            "r": 8,
            "label": "SOL: $12,556,284 FDV, 96.8% concentration (extreme risk)"
          },
          {
            "x": 5363.0,
            "y": 95.17,
            "r": 8,
            "label": "1: $5,363 FDV, 95.2% concentration (extreme risk)"
          },
          {
            "x": 4306.0,
            "y": 95.91,
            "r": 8,
            "label": "RWA: $4,306 FDV, 95.9% concentration (extreme risk)"
          },
          {
            "x": 3364.0,
            "y": 97.93,
            "r": 8,
            "label": "BLUB: $3,364 FDV, 97.9% concentration (extreme risk)"
          },
          {
            "x": 3484.0,
            "y": 97.24,
            "r": 8,
            "label": "Streamless: $3,484 FDV, 97.2% concentration (extreme risk)"
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
| 1 | XBT | XBT | 26.65% | 🟢 low | $16.03 | $384.33 |
| 2 | FLY | Nexa | 27.46% | 🟢 low | $5.42 | $2.42K |
| 3 | RAGEGUY | Rage Guy | 30.87% | 🟢 low | $11.13K | $85.43K |
| 4 | DREAM | Dreamsync | 33.06% | 🟢 low | $13.19K | $102.27K |
| 5 | ELIZABETH | Just Elizabeth Cat | 35.29% | 🟢 low | $14.31 | $35.82 |
| 6 | FARTLESS | FARTLESS COIN | 36.98% | 🟢 low | $321.39 | $2.46K |
| 7 | USDUT | unstable tether | 42.31% | 🟢 low | $0.19 | $36.44 |
| 8 | YAO | YAO MING | 42.66% | 🟢 low | $1.01 | $614.20 |
| 9 | 1nu | 1nu | 45.46% | 🟢 low | $17.65K | $37.86K |
| 10 | USEFUL | USEFUL COIN | 46.37% | 🟢 low | $0.53 | $36.67 |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | BLUB | Blub | 97.93% | 🔴 extreme | $0.28 | $6.47K |
| 2 | Streamless | Streamless coin | 97.24% | 🔴 extreme | $0.14 | $6.66K |
| 3 | SOL | Solana | 96.80% | 🔴 extreme | $1.39K | $13.53K |
| 4 | RWA | Real World Asses | 95.91% | 🔴 extreme | $76.25 | $7.37K |
| 5 | pibble | pibble | 95.60% | 🟠 high | $169.23 | $7.78K |
| 6 | 1 | 1 pill can change your li | 95.17% | 🔴 extreme | $258.27 | $8.72K |
| 7 | FARTWORM | FARTWORM | 92.22% | 🟠 high | $16.65 | $7.86K |
| 8 | AUSBAGWORK | AUSSIE BAG WORKERS | 90.17% | 🟠 high | $74.32 | $13.09K |
| 9 | 1Bull | One bull run to change yo | 81.19% | 🟠 high | $385.33 | $10.22K |
| 10 | 1 | 1 pill can change your li | 80.40% | 🟠 high | $4.55K | $10.35K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 29
**Combined 24h Volume**: $191.35M
**Combined Liquidity**: $45.42M

**Concentration Risk Distribution**:
- 🟢 Low: 14 tokens
- 🔴 Extreme: 5 tokens
- 🟡 High: 5 tokens
- 🟢 Medium: 4 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $191.26M | $43.21M | 🟢 unknown |
| 2 | LION | Loaded Lions | $23.13K | $1.30M | 🟢 low |
| 3 | 1nu | 1nu | $17.65K | $37.86K | 🟢 low |
| 4 | DREAM | Dreamsync | $13.19K | $102.27K | 🟢 low |
| 5 | RAGEGUY | Rage Guy | $11.13K | $85.43K | 🟢 low |
| 6 | HAROLD | Harold | $9.71K | $440.12K | 🟢 medium |
| 7 | 1 | 1 pill can change your life | $4.55K | $10.35K | 🟡 high |
| 8 | AI4 | AI⁴ | $3.32K | $74.36K | 🟢 low |
| 9 | SOL | Solana | $1.39K | $13.53K | 🔴 extreme |
| 10 | RUECAT | Rue Cat | $890.65 | $31.90K | 🟢 medium |

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

**Total Historical Records**: 503
**Unique Tokens Tracked**: 101
**Date Range**: 2025-10-01 to 2025-11-08

**Master Aggregations**: 101 tokens
**Performance Metrics**: 503 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 503 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 101 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 503 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 29 |
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
