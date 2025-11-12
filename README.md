# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-11-12 08:42 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **37 tokens tracked** | 
💰 **$181.69M 24h volume** | 
💧 **$49.04M liquidity** | 
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
          4,
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

*Insufficient historical data for 7-day performance*

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
      "AI20X",
      "1nu",
      "LION",
      "HAROLD",
      "AI4",
      "RAGEGUY",
      "1",
      "19",
      "SOL",
      "DREAM"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          25991.53,
          14849.37,
          14555.97,
          13247.35,
          9199.53,
          8313.7,
          3725.13,
          1442.53,
          1026.15,
          835.82
        ],
        "backgroundColor": [
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#22c55e",
          "#22c55e",
          "#f97316",
          "#ef4444",
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
      "2025-10-02",
      "2025-10-03",
      "2025-10-04",
      "2025-10-05",
      "2025-10-06",
      "2025-11-12"
    ],
    "datasets": [
      {
        "label": "AI20X",
        "data": [
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          39.37,
          40.13
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
          44.23
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
        "label": "HAROLD",
        "data": [
          0.0,
          0.0,
          0.0,
          61.9,
          61.92,
          62.0,
          64.51
        ],
        "borderColor": "#eab308",
        "backgroundColor": "#eab30820",
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
          53.53
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
            "x": 13797910.0,
            "y": 40.13,
            "r": 8,
            "label": "AI20X: $13,797,910 FDV, 40.1% concentration (low risk)"
          },
          {
            "x": 70418.0,
            "y": 44.23,
            "r": 8,
            "label": "1nu: $70,418 FDV, 44.2% concentration (low risk)"
          },
          {
            "x": 43957779.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $43,957,779 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 203815.0,
            "y": 53.53,
            "r": 8,
            "label": "AI4: $203,815 FDV, 53.5% concentration (low risk)"
          },
          {
            "x": 421501.0,
            "y": 29.9,
            "r": 8,
            "label": "RAGEGUY: $421,501 FDV, 29.9% concentration (low risk)"
          },
          {
            "x": 658860.0,
            "y": 33.22,
            "r": 8,
            "label": "DREAM: $658,860 FDV, 33.2% concentration (low risk)"
          },
          {
            "x": 30460.0,
            "y": 56.39,
            "r": 8,
            "label": "SHITTER: $30,460 FDV, 56.4% concentration (low risk)"
          },
          {
            "x": 313335.0,
            "y": 37.69,
            "r": 8,
            "label": "FARTLESS: $313,335 FDV, 37.7% concentration (low risk)"
          },
          {
            "x": 1082591.0,
            "y": 25.45,
            "r": 8,
            "label": "XBT: $1,082,591 FDV, 25.4% concentration (low risk)"
          },
          {
            "x": 386229.0,
            "y": 36.16,
            "r": 8,
            "label": "ELIZABETH: $386,229 FDV, 36.2% concentration (low risk)"
          },
          {
            "x": 86539.0,
            "y": 42.11,
            "r": 8,
            "label": "YAO: $86,539 FDV, 42.1% concentration (low risk)"
          },
          {
            "x": 19061.0,
            "y": 27.46,
            "r": 8,
            "label": "FLY: $19,061 FDV, 27.5% concentration (low risk)"
          },
          {
            "x": 143909.0,
            "y": 47.26,
            "r": 8,
            "label": "gib: $143,909 FDV, 47.3% concentration (low risk)"
          },
          {
            "x": 92512.0,
            "y": 48.93,
            "r": 8,
            "label": "USEFUL: $92,512 FDV, 48.9% concentration (low risk)"
          },
          {
            "x": 122601.0,
            "y": 40.28,
            "r": 8,
            "label": "USDUT: $122,601 FDV, 40.3% concentration (low risk)"
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
            "x": 3519138.0,
            "y": 64.51,
            "r": 8,
            "label": "HAROLD: $3,519,138 FDV, 64.5% concentration (medium risk)"
          },
          {
            "x": 61373.0,
            "y": 61.41,
            "r": 8,
            "label": "RUECAT: $61,373 FDV, 61.4% concentration (medium risk)"
          },
          {
            "x": 5919.0,
            "y": 76.5,
            "r": 8,
            "label": "APOLLO: $5,919 FDV, 76.5% concentration (medium risk)"
          },
          {
            "x": 14090.0,
            "y": 66.1,
            "r": 8,
            "label": "$CrepSol: $14,090 FDV, 66.1% concentration (medium risk)"
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
            "x": 6846.0,
            "y": 83.67,
            "r": 8,
            "label": "1: $6,846 FDV, 83.7% concentration (high risk)"
          },
          {
            "x": 10731.0,
            "y": 90.3,
            "r": 8,
            "label": "AUSBAGWORK: $10,731 FDV, 90.3% concentration (high risk)"
          },
          {
            "x": 6837.0,
            "y": 83.95,
            "r": 8,
            "label": "1Bull: $6,837 FDV, 84.0% concentration (high risk)"
          },
          {
            "x": 6773.0,
            "y": 93.1,
            "r": 8,
            "label": "IDIOT: $6,773 FDV, 93.1% concentration (high risk)"
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
            "x": 4191.0,
            "y": 98.53,
            "r": 8,
            "label": "19: $4,191 FDV, 98.5% concentration (extreme risk)"
          },
          {
            "x": 11459884.0,
            "y": 96.8,
            "r": 8,
            "label": "SOL: $11,459,884 FDV, 96.8% concentration (extreme risk)"
          },
          {
            "x": 3562.0,
            "y": 97.14,
            "r": 8,
            "label": "7: $3,562 FDV, 97.1% concentration (extreme risk)"
          },
          {
            "x": 3565.0,
            "y": 97.75,
            "r": 8,
            "label": "obvious: $3,565 FDV, 97.8% concentration (extreme risk)"
          },
          {
            "x": 2851.0,
            "y": 99.46,
            "r": 8,
            "label": "MMGA: $2,851 FDV, 99.5% concentration (extreme risk)"
          },
          {
            "x": 4028.0,
            "y": 98.77,
            "r": 8,
            "label": "REVIVE: $4,028 FDV, 98.8% concentration (extreme risk)"
          },
          {
            "x": 4381.0,
            "y": 96.63,
            "r": 8,
            "label": "pibble: $4,381 FDV, 96.6% concentration (extreme risk)"
          },
          {
            "x": 3330.0,
            "y": 98.99,
            "r": 8,
            "label": "1% Club: $3,330 FDV, 99.0% concentration (extreme risk)"
          },
          {
            "x": 3076.0,
            "y": 99.21,
            "r": 8,
            "label": "GAZABOY: $3,076 FDV, 99.2% concentration (extreme risk)"
          },
          {
            "x": 4069.0,
            "y": 98.53,
            "r": 8,
            "label": "FALCONS: $4,069 FDV, 98.5% concentration (extreme risk)"
          },
          {
            "x": 3349.0,
            "y": 97.43,
            "r": 8,
            "label": "Streamless: $3,349 FDV, 97.4% concentration (extreme risk)"
          },
          {
            "x": 3242.0,
            "y": 99.24,
            "r": 8,
            "label": "HAMSTERUN: $3,242 FDV, 99.2% concentration (extreme risk)"
          },
          {
            "x": 3159.0,
            "y": 98.05,
            "r": 8,
            "label": "BLUB: $3,159 FDV, 98.0% concentration (extreme risk)"
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
| 1 | XBT | XBT | 25.45% | 🟢 low | $149.86 | $444.36 |
| 2 | FLY | Nexa | 27.46% | 🟢 low | $1.06 | $5.81K |
| 3 | RAGEGUY | Rage Guy | 29.90% | 🟢 low | $8.31K | $88.47K |
| 4 | DREAM | Dreamsync | 33.22% | 🟢 low | $835.82 | $99.61K |
| 5 | ELIZABETH | Just Elizabeth Cat | 36.16% | 🟢 low | $31.85 | $30.47 |
| 6 | FARTLESS | FARTLESS COIN | 37.69% | 🟢 low | $315.26 | $2.34K |
| 7 | AI20X | Ai20x.ai | 40.13% | 🟢 low | $25.99K | $1.72M |
| 8 | USDUT | unstable tether | 40.28% | 🟢 low | $0.21 | $39.36 |
| 9 | YAO | YAO MING | 42.11% | 🟢 low | $11.37 | $547.06 |
| 10 | 1nu | 1nu | 44.23% | 🟢 low | $14.85K | $36.05K |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | MMGA | MAKE MEMES GREAT AGAIN | 99.46% | 🔴 extreme | $5.63 | $5.63K |
| 2 | HAMSTERUN | Hamster Runner | 99.24% | 🔴 extreme | $0.11 | $6.31K |
| 3 | GAZABOY | GAZA BOY | 99.21% | 🔴 extreme | $0.24 | $6.01K |
| 4 | 1% Club | The 1% Club | 98.99% | 🔴 extreme | $0.26 | $6.07K |
| 5 | REVIVE | reviving the memes | 98.77% | 🔴 extreme | $1.85 | $7.90K |
| 6 | 19 | Cult of 19 | 98.53% | 🔴 extreme | $1.44K | $6.94K |
| 7 | FALCONS | THE FALCONS | 98.53% | 🔴 extreme | $0.17 | $7.94K |
| 8 | BLUB | Blub | 98.05% | 🔴 extreme | $0.05 | $6.11K |
| 9 | obvious | in hindsight | 97.75% | 🔴 extreme | $17.76 | $6.44K |
| 10 | Streamless | Streamless coin | 97.43% | 🔴 extreme | $0.16 | $6.41K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 37
**Combined 24h Volume**: $181.69M
**Combined Liquidity**: $49.04M

**Concentration Risk Distribution**:
- 🟢 Low: 15 tokens
- 🔴 Extreme: 13 tokens
- 🟢 Medium: 4 tokens
- 🟡 High: 4 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $181.59M | $45.02M | 🟢 unknown |
| 2 | AI20X | Ai20x.ai | $25.99K | $1.72M | 🟢 low |
| 3 | 1nu | 1nu | $14.85K | $36.05K | 🟢 low |
| 4 | LION | Loaded Lions | $14.56K | $1.32M | 🟢 low |
| 5 | HAROLD | Harold | $13.25K | $462.10K | 🟢 medium |
| 6 | AI4 | AI⁴ | $9.20K | $77.67K | 🟢 low |
| 7 | RAGEGUY | Rage Guy | $8.31K | $88.47K | 🟢 low |
| 8 | 1 | 1 pill can change your life | $3.73K | $8.78K | 🟡 high |
| 9 | 19 | Cult of 19 | $1.44K | $6.94K | 🔴 extreme |
| 10 | SOL | Solana | $1.03K | $12.76K | 🔴 extreme |

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

**Total Historical Records**: 511
**Unique Tokens Tracked**: 101
**Date Range**: 2025-10-01 to 2025-11-12

**Master Aggregations**: 101 tokens
**Performance Metrics**: 511 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 511 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 101 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 511 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 37 |
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
