# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-11-08 08:40 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **26 tokens tracked** | 
💰 **$277.64M 24h volume** | 
💧 **$46.37M liquidity** | 
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
          4,
          4,
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
          -41.99092088197147,
          -41.99092088197147
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
      "HAROLD",
      "RAGEGUY",
      "1",
      "SOL",
      "AI4",
      "1",
      "RUECAT"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          30439.49,
          28821.79,
          13318.61,
          12358.46,
          9491.35,
          6254.62,
          3184.8,
          1861.06,
          657.83,
          631.11
        ],
        "backgroundColor": [
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#22c55e",
          "#f97316",
          "#ef4444",
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
          44.07
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
          33.04
        ],
        "borderColor": "#22c55e",
        "backgroundColor": "#22c55e20",
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
          64.13
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
          30.7
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
            "x": 43658539.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $43,658,539 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 77314.0,
            "y": 44.07,
            "r": 8,
            "label": "1nu: $77,314 FDV, 44.1% concentration (low risk)"
          },
          {
            "x": 726361.0,
            "y": 33.04,
            "r": 8,
            "label": "DREAM: $726,361 FDV, 33.0% concentration (low risk)"
          },
          {
            "x": 411126.0,
            "y": 30.7,
            "r": 8,
            "label": "RAGEGUY: $411,126 FDV, 30.7% concentration (low risk)"
          },
          {
            "x": 197822.0,
            "y": 54.02,
            "r": 8,
            "label": "AI4: $197,822 FDV, 54.0% concentration (low risk)"
          },
          {
            "x": 28950.0,
            "y": 57.44,
            "r": 8,
            "label": "SHITTER: $28,950 FDV, 57.4% concentration (low risk)"
          },
          {
            "x": 360556.0,
            "y": 36.43,
            "r": 8,
            "label": "FARTLESS: $360,556 FDV, 36.4% concentration (low risk)"
          },
          {
            "x": 886431.0,
            "y": 26.52,
            "r": 8,
            "label": "XBT: $886,431 FDV, 26.5% concentration (low risk)"
          },
          {
            "x": 20617.0,
            "y": 27.46,
            "r": 8,
            "label": "FLY: $20,617 FDV, 27.5% concentration (low risk)"
          },
          {
            "x": 421796.0,
            "y": 35.99,
            "r": 8,
            "label": "ELIZABETH: $421,796 FDV, 36.0% concentration (low risk)"
          },
          {
            "x": 142823.0,
            "y": 46.53,
            "r": 8,
            "label": "gib: $142,823 FDV, 46.5% concentration (low risk)"
          },
          {
            "x": 89826.0,
            "y": 42.91,
            "r": 8,
            "label": "YAO: $89,826 FDV, 42.9% concentration (low risk)"
          },
          {
            "x": 119749.0,
            "y": 46.15,
            "r": 8,
            "label": "USEFUL: $119,749 FDV, 46.1% concentration (low risk)"
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
            "x": 3295581.0,
            "y": 64.13,
            "r": 8,
            "label": "HAROLD: $3,295,581 FDV, 64.1% concentration (medium risk)"
          },
          {
            "x": 63740.0,
            "y": 60.91,
            "r": 8,
            "label": "RUECAT: $63,740 FDV, 60.9% concentration (medium risk)"
          },
          {
            "x": 14749.0,
            "y": 65.95,
            "r": 8,
            "label": "$CrepSol: $14,749 FDV, 66.0% concentration (medium risk)"
          },
          {
            "x": 5437.0,
            "y": 76.92,
            "r": 8,
            "label": "APOLLO: $5,437 FDV, 76.9% concentration (medium risk)"
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
            "x": 9250.0,
            "y": 81.2,
            "r": 8,
            "label": "1: $9,250 FDV, 81.2% concentration (high risk)"
          },
          {
            "x": 8690.0,
            "y": 82.21,
            "r": 8,
            "label": "1Bull: $8,690 FDV, 82.2% concentration (high risk)"
          },
          {
            "x": 5086.0,
            "y": 94.69,
            "r": 8,
            "label": "pibble: $5,086 FDV, 94.7% concentration (high risk)"
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
            "x": 12442223.0,
            "y": 96.8,
            "r": 8,
            "label": "SOL: $12,442,223 FDV, 96.8% concentration (extreme risk)"
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
| 1 | XBT | XBT | 26.52% | 🟢 low | $15.65 | $410.15 |
| 2 | FLY | Nexa | 27.46% | 🟢 low | $5.42 | $2.42K |
| 3 | RAGEGUY | Rage Guy | 30.70% | 🟢 low | $9.49K | $88.73K |
| 4 | DREAM | Dreamsync | 33.04% | 🟢 low | $13.32K | $105.90K |
| 5 | ELIZABETH | Just Elizabeth Cat | 35.99% | 🟢 low | $3.07 | $31.84 |
| 6 | FARTLESS | FARTLESS COIN | 36.43% | 🟢 low | $550.85 | $2.51K |
| 7 | YAO | YAO MING | 42.91% | 🟢 low | $1.01 | $614.20 |
| 8 | 1nu | 1nu | 44.07% | 🟢 low | $28.82K | $37.62K |
| 9 | USEFUL | USEFUL COIN | 46.15% | 🟢 low | $0.84 | $36.67 |
| 10 | gib | gib | 46.53% | 🟢 low | $1.20 | $26.48 |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | BLUB | Blub | 97.93% | 🔴 extreme | $1.93 | $6.47K |
| 2 | SOL | Solana | 96.80% | 🔴 extreme | $3.18K | $13.40K |
| 3 | RWA | Real World Asses | 95.91% | 🔴 extreme | $76.25 | $7.37K |
| 4 | 1 | 1 pill can change your li | 95.17% | 🔴 extreme | $657.83 | $8.72K |
| 5 | pibble | pibble | 94.69% | 🟠 high | $152.37 | $7.89K |
| 6 | FARTWORM | FARTWORM | 92.22% | 🟠 high | $18.63 | $7.86K |
| 7 | 1Bull | One bull run to change yo | 82.21% | 🟠 high | $492.27 | $10.36K |
| 8 | 1 | 1 pill can change your li | 81.20% | 🟠 high | $6.25K | $10.42K |
| 9 | APOLLO | Apollo AI | 76.92% | 🟡 medium | $12.10 | $4.08K |
| 10 | $CrepSol | Crepe on Solana | 65.95% | 🟡 medium | $151.72 | $13.12K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 26
**Combined 24h Volume**: $277.64M
**Combined Liquidity**: $46.37M

**Concentration Risk Distribution**:
- 🟢 Low: 13 tokens
- 🟡 High: 4 tokens
- 🟢 Medium: 4 tokens
- 🔴 Extreme: 4 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $277.53M | $44.12M | 🟢 unknown |
| 2 | LION | Loaded Lions | $30.44K | $1.33M | 🟢 low |
| 3 | 1nu | 1nu | $28.82K | $37.62K | 🟢 low |
| 4 | DREAM | Dreamsync | $13.32K | $105.90K | 🟢 low |
| 5 | HAROLD | Harold | $12.36K | $454.19K | 🟢 medium |
| 6 | RAGEGUY | Rage Guy | $9.49K | $88.73K | 🟢 low |
| 7 | 1 | 1 pill can change your life | $6.25K | $10.42K | 🟡 high |
| 8 | SOL | Solana | $3.18K | $13.40K | 🔴 extreme |
| 9 | AI4 | AI⁴ | $1.86K | $77.73K | 🟢 low |
| 10 | 1 | 1 pill can change your life | $657.83 | $8.72K | 🔴 extreme |

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

**Total Historical Records**: 500
**Unique Tokens Tracked**: 101
**Date Range**: 2025-10-01 to 2025-11-08

**Master Aggregations**: 101 tokens
**Performance Metrics**: 500 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 500 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 101 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 500 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 26 |
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
