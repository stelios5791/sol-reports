# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-11-11 19:46 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **37 tokens tracked** | 
💰 **$253.76M 24h volume** | 
💧 **$47.29M liquidity** | 
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
          3,
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
      "HAROLD",
      "LION",
      "1nu",
      "RAGEGUY",
      "DREAM",
      "1",
      "AI4",
      "AUSBAGWORK",
      "19",
      "SHITTER"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          60444.43,
          19271.67,
          18033.61,
          7843.7,
          7377.52,
          3017.78,
          1650.86,
          1477.54,
          1442.53,
          972.03
        ],
        "backgroundColor": [
          "#eab308",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#f97316",
          "#22c55e",
          "#f97316",
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
      "2025-11-11"
    ],
    "datasets": [
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
        "borderColor": "#3b82f6",
        "backgroundColor": "#3b82f620",
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
          41.85
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
          30.14
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
          33.24
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
            "x": 44090127.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $44,090,127 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 83629.0,
            "y": 41.85,
            "r": 8,
            "label": "1nu: $83,629 FDV, 41.9% concentration (low risk)"
          },
          {
            "x": 414485.0,
            "y": 30.14,
            "r": 8,
            "label": "RAGEGUY: $414,485 FDV, 30.1% concentration (low risk)"
          },
          {
            "x": 681283.0,
            "y": 33.24,
            "r": 8,
            "label": "DREAM: $681,283 FDV, 33.2% concentration (low risk)"
          },
          {
            "x": 170358.0,
            "y": 54.66,
            "r": 8,
            "label": "AI4: $170,358 FDV, 54.7% concentration (low risk)"
          },
          {
            "x": 30443.0,
            "y": 56.4,
            "r": 8,
            "label": "SHITTER: $30,443 FDV, 56.4% concentration (low risk)"
          },
          {
            "x": 321745.0,
            "y": 37.56,
            "r": 8,
            "label": "FARTLESS: $321,745 FDV, 37.6% concentration (low risk)"
          },
          {
            "x": 920368.0,
            "y": 25.97,
            "r": 8,
            "label": "XBT: $920,368 FDV, 26.0% concentration (low risk)"
          },
          {
            "x": 758077.0,
            "y": 31.14,
            "r": 8,
            "label": "ELIZABETH: $758,077 FDV, 31.1% concentration (low risk)"
          },
          {
            "x": 86933.0,
            "y": 42.04,
            "r": 8,
            "label": "YAO: $86,933 FDV, 42.0% concentration (low risk)"
          },
          {
            "x": 21070.0,
            "y": 27.46,
            "r": 8,
            "label": "FLY: $21,070 FDV, 27.5% concentration (low risk)"
          },
          {
            "x": 143909.0,
            "y": 47.35,
            "r": 8,
            "label": "gib: $143,909 FDV, 47.4% concentration (low risk)"
          },
          {
            "x": 96150.0,
            "y": 49.11,
            "r": 8,
            "label": "USEFUL: $96,150 FDV, 49.1% concentration (low risk)"
          },
          {
            "x": 122601.0,
            "y": 40.63,
            "r": 8,
            "label": "USDUT: $122,601 FDV, 40.6% concentration (low risk)"
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
            "x": 3560467.0,
            "y": 64.51,
            "r": 8,
            "label": "HAROLD: $3,560,467 FDV, 64.5% concentration (medium risk)"
          },
          {
            "x": 14657.0,
            "y": 65.91,
            "r": 8,
            "label": "$CrepSol: $14,657 FDV, 65.9% concentration (medium risk)"
          },
          {
            "x": 63145.0,
            "y": 61.57,
            "r": 8,
            "label": "RUECAT: $63,145 FDV, 61.6% concentration (medium risk)"
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
            "x": 8473.0,
            "y": 81.18,
            "r": 8,
            "label": "1: $8,473 FDV, 81.2% concentration (high risk)"
          },
          {
            "x": 11089.0,
            "y": 90.29,
            "r": 8,
            "label": "AUSBAGWORK: $11,089 FDV, 90.3% concentration (high risk)"
          },
          {
            "x": 7285.0,
            "y": 84.18,
            "r": 8,
            "label": "1Bull: $7,285 FDV, 84.2% concentration (high risk)"
          },
          {
            "x": 5589.0,
            "y": 77.45,
            "r": 8,
            "label": "APOLLO: $5,589 FDV, 77.5% concentration (high risk)"
          },
          {
            "x": 7226.0,
            "y": 92.91,
            "r": 8,
            "label": "IDIOT: $7,226 FDV, 92.9% concentration (high risk)"
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
            "x": 12175932.0,
            "y": 96.8,
            "r": 8,
            "label": "SOL: $12,175,932 FDV, 96.8% concentration (extreme risk)"
          },
          {
            "x": 3565.0,
            "y": 97.75,
            "r": 8,
            "label": "obvious: $3,565 FDV, 97.8% concentration (extreme risk)"
          },
          {
            "x": 4384.0,
            "y": 96.6,
            "r": 8,
            "label": "pibble: $4,384 FDV, 96.6% concentration (extreme risk)"
          },
          {
            "x": 3608.0,
            "y": 97.42,
            "r": 8,
            "label": "Streamless: $3,608 FDV, 97.4% concentration (extreme risk)"
          },
          {
            "x": 8829.0,
            "y": 94.22,
            "r": 8,
            "label": "MOCHI: $8,829 FDV, 94.2% concentration (extreme risk)"
          },
          {
            "x": 4075.0,
            "y": 97.61,
            "r": 8,
            "label": "BULLCOIN: $4,075 FDV, 97.6% concentration (extreme risk)"
          },
          {
            "x": 3330.0,
            "y": 98.99,
            "r": 8,
            "label": "1% Club: $3,330 FDV, 99.0% concentration (extreme risk)"
          },
          {
            "x": 4226.0,
            "y": 98.73,
            "r": 8,
            "label": "REVIVE: $4,226 FDV, 98.7% concentration (extreme risk)"
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
            "x": 3242.0,
            "y": 99.24,
            "r": 8,
            "label": "HAMSTERUN: $3,242 FDV, 99.2% concentration (extreme risk)"
          },
          {
            "x": 3505.0,
            "y": 98.05,
            "r": 8,
            "label": "viewer: $3,505 FDV, 98.0% concentration (extreme risk)"
          },
          {
            "x": 4730.0,
            "y": 96.35,
            "r": 8,
            "label": "SUPRACOIN: $4,730 FDV, 96.3% concentration (extreme risk)"
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
| 1 | XBT | XBT | 25.97% | 🟢 low | $23.50 | $413.07 |
| 2 | FLY | Nexa | 27.46% | 🟢 low | $1.29 | $145.57 |
| 3 | RAGEGUY | Rage Guy | 30.14% | 🟢 low | $7.84K | $88.56K |
| 4 | ELIZABETH | Just Elizabeth Cat | 31.14% | 🟢 low | $13.60 | $42.68 |
| 5 | DREAM | Dreamsync | 33.24% | 🟢 low | $7.38K | $102.86K |
| 6 | FARTLESS | FARTLESS COIN | 37.56% | 🟢 low | $392.22 | $2.37K |
| 7 | USDUT | unstable tether | 40.63% | 🟢 low | $0.21 | $39.36 |
| 8 | 1nu | 1nu | 41.85% | 🟢 low | $18.03K | $39.26K |
| 9 | YAO | YAO MING | 42.04% | 🟢 low | $10.41 | $552.77 |
| 10 | gib | gib | 47.35% | 🟢 low | $0.50 | $26.58 |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | HAMSTERUN | Hamster Runner | 99.24% | 🔴 extreme | $0.11 | $6.31K |
| 2 | GAZABOY | GAZA BOY | 99.21% | 🔴 extreme | $0.24 | $6.01K |
| 3 | 1% Club | The 1% Club | 98.99% | 🔴 extreme | $0.26 | $6.07K |
| 4 | REVIVE | reviving the memes | 98.73% | 🔴 extreme | $0.24 | $8.29K |
| 5 | 19 | Cult of 19 | 98.53% | 🔴 extreme | $1.44K | $6.94K |
| 6 | FALCONS | THE FALCONS | 98.53% | 🔴 extreme | $0.17 | $7.94K |
| 7 | viewer | in a streamers world | 98.05% | 🔴 extreme | $0.08 | $6.73K |
| 8 | obvious | in hindsight | 97.75% | 🔴 extreme | $17.76 | $6.44K |
| 9 | BULLCOIN | BULLCOIN | 97.61% | 🔴 extreme | $0.66 | $7.07K |
| 10 | Streamless | Streamless coin | 97.42% | 🔴 extreme | $1.86 | $6.91K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 37
**Combined 24h Volume**: $253.76M
**Combined Liquidity**: $47.29M

**Concentration Risk Distribution**:
- 🟢 Low: 14 tokens
- 🔴 Extreme: 14 tokens
- 🟡 High: 5 tokens
- 🟢 Medium: 3 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $253.64M | $44.96M | 🟢 unknown |
| 2 | HAROLD | Harold | $60.44K | $466.96K | 🟢 medium |
| 3 | LION | Loaded Lions | $19.27K | $1.33M | 🟢 low |
| 4 | 1nu | 1nu | $18.03K | $39.26K | 🟢 low |
| 5 | RAGEGUY | Rage Guy | $7.84K | $88.56K | 🟢 low |
| 6 | DREAM | Dreamsync | $7.38K | $102.86K | 🟢 low |
| 7 | 1 | 1 pill can change your life | $3.02K | $9.85K | 🟡 high |
| 8 | AI4 | AI⁴ | $1.65K | $71.63K | 🟢 low |
| 9 | AUSBAGWORK | AUSSIE BAG WORKERS | $1.48K | $13.57K | 🟡 high |
| 10 | 19 | Cult of 19 | $1.44K | $6.94K | 🔴 extreme |

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
- 👀 **Watch**: 114 tokens
- 🚀 **Breakout**: 3 tokens
- ❄️ **Cooling**: 1 tokens

### 🚀 Breakout Signals

| Symbol | Score | Vol 3v1 | Z-Score Vol | Liq 3d | Streak |
|--------|-------|---------|-------------|--------|--------|
| wSOL | 4.24 | 2.51x | 1.69 | $57.82M | 0d |
| XBT | 3.65 | 2.10x | 1.74 | $421.14K | 0d |
| USDUT | 3.57 | 2.36x | 1.51 | $150.84K | 0d |

### 👀 Watch List

*114 tokens showing elevated activity*

📄 [Full data: signals_filtered.csv](data/signals_filtered.csv)

---

## 📈 Historical Data

**Total Historical Records**: 511
**Unique Tokens Tracked**: 101
**Date Range**: 2025-10-01 to 2025-11-11

**Master Aggregations**: 101 tokens
**Performance Metrics**: 513 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 511 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 101 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 513 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 37 |
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
