# 📊 Solana Radar - Live Dashboard

**Last Updated**: 2025-11-04 08:42 UTC

Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.

---

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }
</style>

## 📈 Quick Stats

🎯 **42 tokens tracked** | 
💰 **$357.38M 24h volume** | 
💧 **$51.72M liquidity** | 
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
          3,
          6,
          19,
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
      "LION",
      "1nu",
      "RAGEGUY",
      "HAROLD",
      "DREAM",
      "SOL",
      "SHITTER",
      "FARTLESS",
      "RUECAT"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          62875.66,
          38242.85,
          21788.8,
          20079.5,
          11194.06,
          5061.77,
          3979.11,
          518.13,
          492.42,
          209.35
        ],
        "backgroundColor": [
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#22c55e",
          "#ef4444",
          "#eab308",
          "#22c55e",
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
      "2025-11-04"
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
          53.7
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
          48.49
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
          29.29
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
          63.9
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
            "x": 245059.0,
            "y": 53.7,
            "r": 8,
            "label": "AI4: $245,059 FDV, 53.7% concentration (low risk)"
          },
          {
            "x": 45006465.0,
            "y": 57.84,
            "r": 8,
            "label": "LION: $45,006,465 FDV, 57.8% concentration (low risk)"
          },
          {
            "x": 49565.0,
            "y": 48.49,
            "r": 8,
            "label": "1nu: $49,565 FDV, 48.5% concentration (low risk)"
          },
          {
            "x": 531086.0,
            "y": 29.29,
            "r": 8,
            "label": "RAGEGUY: $531,086 FDV, 29.3% concentration (low risk)"
          },
          {
            "x": 676323.0,
            "y": 33.18,
            "r": 8,
            "label": "DREAM: $676,323 FDV, 33.2% concentration (low risk)"
          },
          {
            "x": 315193.0,
            "y": 37.72,
            "r": 8,
            "label": "FARTLESS: $315,193 FDV, 37.7% concentration (low risk)"
          },
          {
            "x": 63768.0,
            "y": 58.88,
            "r": 8,
            "label": "RUECAT: $63,768 FDV, 58.9% concentration (low risk)"
          },
          {
            "x": 16618.0,
            "y": 30.08,
            "r": 8,
            "label": "FLY: $16,618 FDV, 30.1% concentration (low risk)"
          },
          {
            "x": 989880.0,
            "y": 24.92,
            "r": 8,
            "label": "XBT: $989,880 FDV, 24.9% concentration (low risk)"
          },
          {
            "x": 16071410.0,
            "y": 39.94,
            "r": 8,
            "label": "AI20X: $16,071,410 FDV, 39.9% concentration (low risk)"
          },
          {
            "x": 334631.0,
            "y": 37.09,
            "r": 8,
            "label": "ELIZABETH: $334,631 FDV, 37.1% concentration (low risk)"
          },
          {
            "x": 98675.0,
            "y": 47.06,
            "r": 8,
            "label": "USEFUL: $98,675 FDV, 47.1% concentration (low risk)"
          },
          {
            "x": 147465.0,
            "y": 46.11,
            "r": 8,
            "label": "gib: $147,465 FDV, 46.1% concentration (low risk)"
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
            "x": 2840855.0,
            "y": 63.9,
            "r": 8,
            "label": "HAROLD: $2,840,855 FDV, 63.9% concentration (medium risk)"
          },
          {
            "x": 21393.0,
            "y": 65.1,
            "r": 8,
            "label": "SHITTER: $21,393 FDV, 65.1% concentration (medium risk)"
          },
          {
            "x": 14603.0,
            "y": 65.47,
            "r": 8,
            "label": "$CrepSol: $14,603 FDV, 65.5% concentration (medium risk)"
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
            "x": 10973.0,
            "y": 89.94,
            "r": 8,
            "label": "AUSBAGWORK: $10,973 FDV, 89.9% concentration (high risk)"
          },
          {
            "x": 3560.0,
            "y": 81.52,
            "r": 8,
            "label": "APOLLO: $3,560 FDV, 81.5% concentration (high risk)"
          },
          {
            "x": 5138.0,
            "y": 92.01,
            "r": 8,
            "label": "FARTWORM: $5,138 FDV, 92.0% concentration (high risk)"
          },
          {
            "x": 6864.0,
            "y": 92.86,
            "r": 8,
            "label": "IDIOT: $6,864 FDV, 92.9% concentration (high risk)"
          },
          {
            "x": 8958.0,
            "y": 80.77,
            "r": 8,
            "label": "1Bull: $8,958 FDV, 80.8% concentration (high risk)"
          },
          {
            "x": 6685.0,
            "y": 90.18,
            "r": 8,
            "label": "DARE: $6,685 FDV, 90.2% concentration (high risk)"
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
            "x": 15067267.0,
            "y": 96.8,
            "r": 8,
            "label": "SOL: $15,067,267 FDV, 96.8% concentration (extreme risk)"
          },
          {
            "x": 3741.0,
            "y": 96.41,
            "r": 8,
            "label": "7: $3,741 FDV, 96.4% concentration (extreme risk)"
          },
          {
            "x": 4906.0,
            "y": 96.49,
            "r": 8,
            "label": "SUPRACOIN: $4,906 FDV, 96.5% concentration (extreme risk)"
          },
          {
            "x": 3349.0,
            "y": 98.03,
            "r": 8,
            "label": "1: $3,349 FDV, 98.0% concentration (extreme risk)"
          },
          {
            "x": 8428.0,
            "y": 93.72,
            "r": 8,
            "label": "MOCHI: $8,428 FDV, 93.7% concentration (extreme risk)"
          },
          {
            "x": 3919.0,
            "y": 98.53,
            "r": 8,
            "label": "FALCONS: $3,919 FDV, 98.5% concentration (extreme risk)"
          },
          {
            "x": 3780.0,
            "y": 97.68,
            "r": 8,
            "label": "Bagwork: $3,780 FDV, 97.7% concentration (extreme risk)"
          },
          {
            "x": 3883.0,
            "y": 97.5,
            "r": 8,
            "label": "obvious: $3,883 FDV, 97.5% concentration (extreme risk)"
          },
          {
            "x": 3123.0,
            "y": 99.4,
            "r": 8,
            "label": "retail: $3,123 FDV, 99.4% concentration (extreme risk)"
          },
          {
            "x": 3633.0,
            "y": 98.09,
            "r": 8,
            "label": "Hosico: $3,633 FDV, 98.1% concentration (extreme risk)"
          },
          {
            "x": 3446.0,
            "y": 98.97,
            "r": 8,
            "label": "19: $3,446 FDV, 99.0% concentration (extreme risk)"
          },
          {
            "x": 3319.0,
            "y": 99.69,
            "r": 8,
            "label": "KENNY: $3,319 FDV, 99.7% concentration (extreme risk)"
          },
          {
            "x": 3235.0,
            "y": 99.98,
            "r": 8,
            "label": "COUNT: $3,235 FDV, 100.0% concentration (extreme risk)"
          },
          {
            "x": 3312.0,
            "y": 99.71,
            "r": 8,
            "label": "Supershiro: $3,312 FDV, 99.7% concentration (extreme risk)"
          },
          {
            "x": 3033.0,
            "y": 99.99,
            "r": 8,
            "label": "UPC: $3,033 FDV, 100.0% concentration (extreme risk)"
          },
          {
            "x": 3016.0,
            "y": 99.81,
            "r": 8,
            "label": "NeverDie: $3,016 FDV, 99.8% concentration (extreme risk)"
          },
          {
            "x": 2960.0,
            "y": 99.66,
            "r": 8,
            "label": "ACTIVITIES: $2,960 FDV, 99.7% concentration (extreme risk)"
          },
          {
            "x": 2983.0,
            "y": 99.84,
            "r": 8,
            "label": "MOONCOIN: $2,983 FDV, 99.8% concentration (extreme risk)"
          },
          {
            "x": 3047.0,
            "y": 99.63,
            "r": 8,
            "label": "ORE: $3,047 FDV, 99.6% concentration (extreme risk)"
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
| 1 | XBT | XBT | 24.92% | 🟢 low | $20.46 | $421.95 |
| 2 | RAGEGUY | Rage Guy | 29.29% | 🟢 low | $20.08K | $99.63K |
| 3 | FLY | Nexa | 30.08% | 🟢 low | $32.20 | $5.46K |
| 4 | DREAM | Dreamsync | 33.18% | 🟢 low | $5.06K | $100.50K |
| 5 | ELIZABETH | Just Elizabeth Cat | 37.09% | 🟢 low | $4.45 | $28.36 |
| 6 | FARTLESS | FARTLESS COIN | 37.72% | 🟢 low | $492.42 | $2.34K |
| 7 | AI20X | Ai20x.ai | 39.94% | 🟢 low | $15.88 | $1.97M |
| 8 | gib | gib | 46.11% | 🟢 low | $0.76 | $26.91 |
| 9 | USEFUL | USEFUL COIN | 47.06% | 🟢 low | $1.05 | $31.63 |
| 10 | 1nu | 1nu | 48.49% | 🟢 low | $21.79K | $29.57K |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | UPC | Upcoin | 99.99% | 🔴 extreme | $1.55 | $6.04K |
| 2 | COUNT | Counting live till $100M | 99.98% | 🔴 extreme | $1.64 | $6.46K |
| 3 | MOONCOIN | MOON COIN | 99.84% | 🔴 extreme | $1.47 | $5.94K |
| 4 | NeverDie | MEMES WILL NEVER DIE | 99.81% | 🔴 extreme | $1.51 | $5.98K |
| 5 | Supershiro | Super Shiro | 99.71% | 🔴 extreme | $1.61 | $6.28K |
| 6 | KENNY | KENNY KO | 99.69% | 🔴 extreme | $1.65 | $6.28K |
| 7 | ACTIVITIES | REAL LIFE ACTIVITIES | 99.66% | 🔴 extreme | $1.49 | $5.91K |
| 8 | ORE | Ore Labs | 99.63% | 🔴 extreme | $1.45 | $6.02K |
| 9 | retail | retail | 99.40% | 🔴 extreme | $1.91 | $6.21K |
| 10 | 19 | Cult of 19 | 98.97% | 🔴 extreme | $1.67 | $6.41K |

---

## 🎯 Pattern Detection

*Pattern detection data not available. Enable pattern detection in the pipeline.*

---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 42
**Combined 24h Volume**: $357.38M
**Combined Liquidity**: $51.72M

**Concentration Risk Distribution**:
- 🔴 Extreme: 19 tokens
- 🟢 Low: 13 tokens
- 🟡 High: 6 tokens
- 🟢 Medium: 3 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $357.21M | $47.40M | 🟢 unknown |
| 2 | AI4 | AI⁴ | $62.88K | $86.01K | 🟢 low |
| 3 | LION | Loaded Lions | $38.24K | $1.34M | 🟢 low |
| 4 | 1nu | 1nu | $21.79K | $29.57K | 🟢 low |
| 5 | RAGEGUY | Rage Guy | $20.08K | $99.63K | 🟢 low |
| 6 | HAROLD | Harold | $11.19K | $419.31K | 🟢 medium |
| 7 | DREAM | Dreamsync | $5.06K | $100.50K | 🟢 low |
| 8 | SOL | Solana | $3.98K | $14.69K | 🔴 extreme |
| 9 | SHITTER | SHITTERCOIN | $518.13 | $20.57K | 🟢 medium |
| 10 | FARTLESS | FARTLESS COIN | $492.42 | $2.34K | 🟢 low |

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

**Total Historical Records**: 516
**Unique Tokens Tracked**: 101
**Date Range**: 2025-10-01 to 2025-11-04

**Master Aggregations**: 101 tokens
**Performance Metrics**: 516 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 516 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 101 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 516 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 42 |
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
