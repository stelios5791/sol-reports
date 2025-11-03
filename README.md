# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-11-03 08:42 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **31 tokens tracked** | 
💰 **$230.73M 24h volume** | 
💧 **$68.61M liquidity** | 
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
          3,
          9,
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
      "AI4",
      "RAGEGUY",
      "DREAM",
      "LION",
      "HAROLD",
      "1nu",
      "1",
      "Hosico",
      "AUSBAGWORK",
      "FARTLESS"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          66832.39,
          22757.41,
          14372.74,
          12515.67,
          10857.29,
          9000.07,
          933.07,
          538.57,
          447.55,
          297.79
        ],
        "backgroundColor": [
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#22c55e",
          "#ef4444",
          "#ef4444",
          "#f97316",
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
      "2025-11-03"
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
          51.26
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
          30.02
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
          33.45
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
        "label": "HAROLD",
        "data": [
          0.0,
          0.0,
          0.0,
          61.9,
          61.92,
          62.0,
          63.84
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
            "x": 247904.0,
            "y": 51.26,
            "r": 8,
            "label": "AI4: $247,904 FDV, 51.3% concentration (low risk)"
          },
          {
            "x": 520257.0,
            "y": 30.02,
            "r": 8,
            "label": "RAGEGUY: $520,257 FDV, 30.0% concentration (low risk)"
          },
          {
            "x": 704630.0,
            "y": 33.45,
            "r": 8,
            "label": "DREAM: $704,630 FDV, 33.5% concentration (low risk)"
          },
          {
            "x": 49496186.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $49,496,186 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 62804.0,
            "y": 46.39,
            "r": 8,
            "label": "1nu: $62,804 FDV, 46.4% concentration (low risk)"
          },
          {
            "x": 399189.0,
            "y": 36.78,
            "r": 8,
            "label": "FARTLESS: $399,189 FDV, 36.8% concentration (low risk)"
          },
          {
            "x": 66216.0,
            "y": 59.06,
            "r": 8,
            "label": "RUECAT: $66,216 FDV, 59.1% concentration (low risk)"
          },
          {
            "x": 18185.0,
            "y": 30.07,
            "r": 8,
            "label": "FLY: $18,185 FDV, 30.1% concentration (low risk)"
          },
          {
            "x": 1101001.0,
            "y": 24.79,
            "r": 8,
            "label": "XBT: $1,101,001 FDV, 24.8% concentration (low risk)"
          },
          {
            "x": 16410931.0,
            "y": 39.94,
            "r": 8,
            "label": "AI20X: $16,410,931 FDV, 39.9% concentration (low risk)"
          },
          {
            "x": 127020.0,
            "y": 41.07,
            "r": 8,
            "label": "YAO: $127,020 FDV, 41.1% concentration (low risk)"
          },
          {
            "x": 403639.0,
            "y": 36.07,
            "r": 8,
            "label": "ELIZABETH: $403,639 FDV, 36.1% concentration (low risk)"
          },
          {
            "x": 164653.0,
            "y": 45.91,
            "r": 8,
            "label": "gib: $164,653 FDV, 45.9% concentration (low risk)"
          },
          {
            "x": 134167.0,
            "y": 40.12,
            "r": 8,
            "label": "USDUT: $134,167 FDV, 40.1% concentration (low risk)"
          },
          {
            "x": 107970.0,
            "y": 45.88,
            "r": 8,
            "label": "USEFUL: $107,970 FDV, 45.9% concentration (low risk)"
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
            "x": 3073468.0,
            "y": 63.84,
            "r": 8,
            "label": "HAROLD: $3,073,468 FDV, 63.8% concentration (medium risk)"
          },
          {
            "x": 22575.0,
            "y": 63.63,
            "r": 8,
            "label": "SHITTER: $22,575 FDV, 63.6% concentration (medium risk)"
          },
          {
            "x": 16855.0,
            "y": 64.42,
            "r": 8,
            "label": "$CrepSol: $16,855 FDV, 64.4% concentration (medium risk)"
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
            "x": 11675.0,
            "y": 90.54,
            "r": 8,
            "label": "AUSBAGWORK: $11,675 FDV, 90.5% concentration (high risk)"
          },
          {
            "x": 9505.0,
            "y": 80.76,
            "r": 8,
            "label": "1Bull: $9,505 FDV, 80.8% concentration (high risk)"
          },
          {
            "x": 7384.0,
            "y": 90.18,
            "r": 8,
            "label": "DARE: $7,384 FDV, 90.2% concentration (high risk)"
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
            "x": 3732.0,
            "y": 97.74,
            "r": 8,
            "label": "1: $3,732 FDV, 97.7% concentration (extreme risk)"
          },
          {
            "x": 3985.0,
            "y": 98.03,
            "r": 8,
            "label": "Hosico: $3,985 FDV, 98.0% concentration (extreme risk)"
          },
          {
            "x": 15638578.0,
            "y": 96.8,
            "r": 8,
            "label": "SOL: $15,638,578 FDV, 96.8% concentration (extreme risk)"
          },
          {
            "x": 4164.0,
            "y": 96.24,
            "r": 8,
            "label": "RWA: $4,164 FDV, 96.2% concentration (extreme risk)"
          },
          {
            "x": 8026.0,
            "y": 98.78,
            "r": 8,
            "label": "JIFFPOM: $8,026 FDV, 98.8% concentration (extreme risk)"
          },
          {
            "x": 4100.0,
            "y": 97.61,
            "r": 8,
            "label": "Bagwork: $4,100 FDV, 97.6% concentration (extreme risk)"
          },
          {
            "x": 4454.0,
            "y": 96.34,
            "r": 8,
            "label": "pibble: $4,454 FDV, 96.3% concentration (extreme risk)"
          },
          {
            "x": 9941.0,
            "y": 93.86,
            "r": 8,
            "label": "MOCHI: $9,941 FDV, 93.9% concentration (extreme risk)"
          },
          {
            "x": 3794.0,
            "y": 98.05,
            "r": 8,
            "label": "viewer: $3,794 FDV, 98.0% concentration (extreme risk)"
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
| 1 | XBT | XBT | 24.79% | 🟢 low | $50.96 | $471.81 |
| 2 | RAGEGUY | Rage Guy | 30.02% | 🟢 low | $22.76K | $104.54K |
| 3 | FLY | Nexa | 30.07% | 🟢 low | $69.77 | $6.03K |
| 4 | DREAM | Dreamsync | 33.45% | 🟢 low | $14.37K | $108.59K |
| 5 | ELIZABETH | Just Elizabeth Cat | 36.07% | 🟢 low | $1.96 | $31.15 |
| 6 | FARTLESS | FARTLESS COIN | 36.78% | 🟢 low | $297.79 | $2.63K |
| 7 | AI20X | Ai20x.ai | 39.94% | 🟢 low | $6.99 | $2.02M |
| 8 | USDUT | unstable tether | 40.12% | 🟢 low | $0.92 | $39.62 |
| 9 | YAO | YAO MING | 41.07% | 🟢 low | $2.70 | $799.19 |
| 10 | USEFUL | USEFUL COIN | 45.88% | 🟢 low | $0.86 | $36.43 |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | JIFFPOM | Jiffpom | 98.78% | 🔴 extreme | $9.17 | $11.59K |
| 2 | viewer | in a streamers world | 98.05% | 🔴 extreme | $0.50 | $7.28K |
| 3 | Hosico | Hosico Cat | 98.03% | 🔴 extreme | $538.57 | $7.21K |
| 4 | 1 | 1 pill can change your li | 97.74% | 🔴 extreme | $933.07 | $6.85K |
| 5 | Bagwork | African Bagwork | 97.61% | 🔴 extreme | $2.52 | $7.81K |
| 6 | SOL | Solana | 96.80% | 🔴 extreme | $101.16 | $3.83K |
| 7 | pibble | pibble | 96.34% | 🔴 extreme | $2.51 | $7.38K |
| 8 | RWA | Real World Asses | 96.24% | 🔴 extreme | $17.08 | $7.25K |
| 9 | MOCHI | MOCHI CULT | 93.86% | 🔴 extreme | $0.53 | $17.24K |
| 10 | AUSBAGWORK | AUSSIE BAG WORKERS | 90.54% | 🟠 high | $447.55 | $14.68K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 31
**Combined 24h Volume**: $230.73M
**Combined Liquidity**: $68.61M

**Concentration Risk Distribution**:
- 🟢 Low: 15 tokens
- 🔴 Extreme: 9 tokens
- 🟢 Medium: 3 tokens
- 🟡 High: 3 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $230.59M | $64.12M | 🟢 unknown |
| 2 | AI4 | AI⁴ | $66.83K | $90.39K | 🟢 low |
| 3 | RAGEGUY | Rage Guy | $22.76K | $104.54K | 🟢 low |
| 4 | DREAM | Dreamsync | $14.37K | $108.59K | 🟢 low |
| 5 | LION | Loaded Lions | $12.52K | $1.48M | 🟢 low |
| 6 | HAROLD | Harold | $10.86K | $457.14K | 🟢 medium |
| 7 | 1nu | 1nu | $9.00K | $33.24K | 🟢 low |
| 8 | 1 | 1 pill can change your life | $933.07 | $6.85K | 🔴 extreme |
| 9 | Hosico | Hosico Cat | $538.57 | $7.21K | 🔴 extreme |
| 10 | AUSBAGWORK | AUSSIE BAG WORKERS | $447.55 | $14.68K | 🟡 high |

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

**Total Historical Records**: 505
**Unique Tokens Tracked**: 101
**Date Range**: 2025-10-01 to 2025-11-03

**Master Aggregations**: 101 tokens
**Performance Metrics**: 505 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 505 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 101 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 505 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 31 |
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
