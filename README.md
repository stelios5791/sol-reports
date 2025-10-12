# 📊 Solana Radar - Daily Reports

**Last Updated**: 2025-10-12 08:33 UTC

Automated daily analysis of Solana tokens with whale tracking and momentum indicators.

---

## 📈 Interactive Dashboard

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>

### 🥧 Risk Distribution

Current distribution of concentration risk across all tracked tokens:


<div style="max-width: 900px; margin: 20px auto;">
  <canvas id="riskPieChart"></canvas>
</div>
<script>
(function() {
  const ctx = document.getElementById('riskPieChart');
  if (!ctx) return;
  new Chart(ctx, {
  "type": "pie",
  "data": {
    "labels": [
      "Extreme Risk",
      "High Risk",
      "Medium Risk",
      "Low Risk",
      "Unknown"
    ],
    "datasets": [
      {
        "data": [
          19,
          8,
          3,
          15,
          1
        ],
        "backgroundColor": [
          "#ef4444",
          "#f97316",
          "#eab308",
          "#22c55e",
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
        "text": "Token Concentration Risk Distribution"
      }
    }
  }
});
})();
</script>


### 🏆 Safest Tokens (Lowest Holder Concentration)

Top 10 tokens with the most distributed ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | XBT | XBT | 23.39% | 🟢 low | $266.12 | $539.69 |
| 2 | RAGEGUY | Rage Guy | 27.48% | 🟢 low | $31.52K | $116.91K |
| 3 | ELIZABETH | Just Elizabeth Cat | 29.15% | 🟢 low | $15.02 | $43.32 |
| 4 | DREAM | Dreamsync | 31.53% | 🟢 low | $172.00K | $169.53K |
| 5 | FLY | Nexa | 33.41% | 🟢 low | $86.11 | $7.77K |
| 6 | FARTLESS | FARTLESS COIN | 35.04% | 🟢 low | $1.31K | $3.34K |
| 7 | USDUT | unstable tether | 39.84% | 🟢 low | $2.64 | $63.74 |
| 8 | USEFUL | USEFUL COIN | 41.11% | 🟢 low | $1.41 | $47.64 |
| 9 | AI20X | Ai20x.ai | 41.41% | 🟢 low | $3.98K | $2.07M |
| 10 | gib | gib | 45.03% | 🟢 low | $0.44 | $68.81 |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | pmo | PMOCOIN | 100.00% | 🔴 extreme | $936.70 | $0.00 |
| 2 | TOKENIZER | TOKENIZER MEDIA | 99.98% | 🔴 extreme | $22.19 | $0.00 |
| 3 | MOONCOIN | MOON COIN | 99.70% | 🔴 extreme | $8.41 | $6.53K |
| 4 | MINDWORMS | mindworms | 99.68% | 🔴 extreme | $9.82 | $6.75K |
| 5 | KENNY | KENNY KO | 99.66% | 🔴 extreme | $20.90 | $6.56K |
| 6 | ACTIVITIES | REAL LIFE ACTIVITIES | 99.54% | 🔴 extreme | $8.26 | $6.54K |
| 7 | Mementoe | Mementoe | 99.42% | 🔴 extreme | $1.61 | $6.62K |
| 8 | BEANIE | BEANIE | 99.03% | 🔴 extreme | $0.59 | $7.74K |
| 9 | JIFFPOM | Jiffpom | 98.38% | 🔴 extreme | $5.22 | $10.18K |
| 10 | FALCONS | THE FALCONS | 98.28% | 🔴 extreme | $10.64 | $8.91K |

### 📈 Concentration Trends

Historical holder concentration for top volume tokens:


<div style="max-width: 900px; margin: 20px auto;">
  <canvas id="trendLineChart"></canvas>
</div>
<script>
(function() {
  const ctx = document.getElementById('trendLineChart');
  if (!ctx) return;
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
      "2025-10-12"
    ],
    "datasets": [
      {
        "label": "wSOL",
        "data": [
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          0.0
        ],
        "borderColor": "#3b82f6",
        "backgroundColor": "#3b82f620",
        "tension": 0.1,
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
          31.53
        ],
        "borderColor": "#ef4444",
        "backgroundColor": "#ef444420",
        "tension": 0.1,
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
          47.12
        ],
        "borderColor": "#22c55e",
        "backgroundColor": "#22c55e20",
        "tension": 0.1,
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
        "tension": 0.1,
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
          27.48
        ],
        "borderColor": "#8b5cf6",
        "backgroundColor": "#8b5cf620",
        "tension": 0.1,
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
        "text": "Top 10 Holder Concentration Over Time"
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
})();
</script>


### 📊 Volume Leaders

Top tokens by 24h trading volume (color-coded by risk):


<div style="max-width: 900px; margin: 20px auto;">
  <canvas id="volumeBarChart"></canvas>
</div>
<script>
(function() {
  const ctx = document.getElementById('volumeBarChart');
  if (!ctx) return;
  new Chart(ctx, {
  "type": "bar",
  "data": {
    "labels": [
      "wSOL",
      "DREAM",
      "AI4",
      "LION",
      "RAGEGUY",
      "HAROLD",
      "1nu",
      "SOL",
      "AI20X",
      "IDIOT"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          338628688.16,
          172003.14,
          91957.62,
          31697.75,
          31515.62,
          29610.09,
          7927.34,
          5087.1,
          3979.28,
          1362.72
        ],
        "backgroundColor": [
          "#94a3b8",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#22c55e",
          "#ef4444",
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
        "text": "Top 10 Tokens by 24h Volume"
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
})();
</script>


### 💰 Market Cap vs Concentration

Relationship between token valuation (FDV) and holder concentration:


<div style="max-width: 900px; margin: 20px auto;">
  <canvas id="scatterChart"></canvas>
</div>
<script>
(function() {
  const ctx = document.getElementById('scatterChart');
  if (!ctx) return;
  new Chart(ctx, {
  "type": "scatter",
  "data": {
    "datasets": [
      {
        "label": "Tokens",
        "data": [
          {
            "x": 1688094.0,
            "y": 31.53,
            "symbol": "DREAM",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 178784.0,
            "y": 47.12,
            "symbol": "AI4",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 60419519.0,
            "y": 57.84,
            "symbol": "LION",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 640274.0,
            "y": 27.48,
            "symbol": "RAGEGUY",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 2882158.0,
            "y": 62.94,
            "symbol": "HAROLD",
            "risk": "medium",
            "backgroundColor": "#eab308"
          },
          {
            "x": 32213.0,
            "y": 50.44,
            "symbol": "1nu",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 6990582.0,
            "y": 96.67,
            "symbol": "SOL",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 17445210.0,
            "y": 41.41,
            "symbol": "AI20X",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 11554.0,
            "y": 83.64,
            "symbol": "IDIOT",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 662512.0,
            "y": 35.04,
            "symbol": "FARTLESS",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 5111.7,
            "y": 100.0,
            "symbol": "pmo",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 26780.0,
            "y": 73.79,
            "symbol": "1Bull",
            "risk": "medium",
            "backgroundColor": "#eab308"
          },
          {
            "x": 33723.0,
            "y": 54.7,
            "symbol": "$CrepSol",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 9370.0,
            "y": 95.18,
            "symbol": "7",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 105716.0,
            "y": 52.5,
            "symbol": "RUECAT",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 4680.0,
            "y": 78.01,
            "symbol": "APOLLO",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 1359316.0,
            "y": 23.39,
            "symbol": "XBT",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 18240.0,
            "y": 67.34,
            "symbol": "SHITTER",
            "risk": "medium",
            "backgroundColor": "#eab308"
          },
          {
            "x": 15232.0,
            "y": 33.41,
            "symbol": "FLY",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 14903.0,
            "y": 86.07,
            "symbol": "AUSBAGWORK",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 8397.0,
            "y": 89.01,
            "symbol": "DARE",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 7649.0,
            "y": 93.84,
            "symbol": "SUPRACOIN",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 5236.0,
            "y": 94.23,
            "symbol": "1",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 6908.0,
            "y": 86.74,
            "symbol": "FARTWORM",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 10727.0,
            "y": 91.2,
            "symbol": "MOCHI",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 5605.92,
            "y": 99.98,
            "symbol": "TOKENIZER",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 5148.0,
            "y": 90.46,
            "symbol": "RWA",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 3473.0,
            "y": 99.66,
            "symbol": "KENNY",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 779281.0,
            "y": 29.15,
            "symbol": "ELIZABETH",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 4598.0,
            "y": 98.28,
            "symbol": "FALCONS",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4751.0,
            "y": 96.88,
            "symbol": "BULLCOIN",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 3561.0,
            "y": 99.68,
            "symbol": "MINDWORMS",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 3298.0,
            "y": 99.7,
            "symbol": "MOONCOIN",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 3297.0,
            "y": 99.54,
            "symbol": "ACTIVITIES",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 6198.0,
            "y": 98.38,
            "symbol": "JIFFPOM",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 3974.0,
            "y": 97.49,
            "symbol": "Hosico",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 178590.0,
            "y": 39.84,
            "symbol": "USDUT",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 3944.0,
            "y": 97.67,
            "symbol": "viewer",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 3507.0,
            "y": 99.42,
            "symbol": "Mementoe",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 1475.0,
            "y": 96.41,
            "symbol": "PROFIT",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 149608.0,
            "y": 41.11,
            "symbol": "USEFUL",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 4049.0,
            "y": 99.03,
            "symbol": "BEANIE",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 258216.0,
            "y": 45.03,
            "symbol": "gib",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 4158.0,
            "y": 96.46,
            "symbol": "Streamless",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4041.0,
            "y": 97.22,
            "symbol": "obvious",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          }
        ],
        "backgroundColor": [
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#22c55e",
          "#ef4444",
          "#22c55e",
          "#f97316",
          "#22c55e",
          "#ef4444",
          "#eab308",
          "#22c55e",
          "#ef4444",
          "#22c55e",
          "#f97316",
          "#22c55e",
          "#eab308",
          "#22c55e",
          "#f97316",
          "#f97316",
          "#ef4444",
          "#ef4444",
          "#f97316",
          "#f97316",
          "#ef4444",
          "#f97316",
          "#ef4444",
          "#22c55e",
          "#ef4444",
          "#ef4444",
          "#ef4444",
          "#ef4444",
          "#ef4444",
          "#ef4444",
          "#ef4444",
          "#22c55e",
          "#ef4444",
          "#ef4444",
          "#f97316",
          "#22c55e",
          "#ef4444",
          "#22c55e",
          "#ef4444",
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
        "text": "Market Cap (FDV) vs Holder Concentration"
      },
      "tooltip": {
        "callbacks": {
          "label": "function(context) { const d = context.raw; return d.symbol + \": $\" + d.x.toLocaleString() + \" FDV, \" + d.y.toFixed(1) + \"% concentration (\" + d.risk + \" risk)\"; }"
        }
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
})();
</script>


---

## 🔥 Today's Top 50 Tokens

**Total Tokens**: 46
**Combined 24h Volume**: $339.01M
**Combined Liquidity**: $55.19M

**Concentration Risk Distribution**:
- 🔴 Extreme: 19 tokens
- 🟢 Low: 15 tokens
- 🟡 High: 8 tokens
- 🟢 Medium: 3 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $338.63M | $50.28M | 🟢 unknown |
| 2 | DREAM | Dreamsync | $172.00K | $169.53K | 🟢 low |
| 3 | AI4 | AI⁴ | $91.96K | $75.91K | 🟢 low |
| 4 | LION | Loaded Lions | $31.70K | $1.67M | 🟢 low |
| 5 | RAGEGUY | Rage Guy | $31.52K | $116.91K | 🟢 low |
| 6 | HAROLD | Harold | $29.61K | $450.72K | 🟢 medium |
| 7 | 1nu | 1nu | $7.93K | $23.04K | 🟢 low |
| 8 | SOL | Solana | $5.09K | $10.59K | 🔴 extreme |
| 9 | AI20X | Ai20x.ai | $3.98K | $2.07M | 🟢 low |
| 10 | IDIOT | IDIOT | $1.36K | $13.47K | 🟡 high |

📄 [Full data: daily_top50.csv](data/daily_top50.csv)

---

## 🌱 New Viable Tokens (7-14 Days Old)

New tokens showing potential with healthy metrics and lower concentration risk.

**Found**: 2 viable new tokens

**Criteria**:
- First seen 7-14 days ago
- Volume > $50K
- Liquidity > $100K
- Missing streak < 2 (stable presence)
- Concentration risk: low/medium

| Symbol | Name | Age (days) | Volume 24h | Liquidity | Top 10% |
|--------|------|------------|------------|-----------|---------|
| wSOL | Wrapped SOL | 11 | $338.63M | $50.28M | 0.00% |
| DREAM | Dreamsync | 11 | $172.00K | $169.53K | 31.53% |

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
- 👀 **Watch**: 2 tokens

### 👀 Watch List

*2 tokens showing elevated activity*

📄 [Full data: signals_filtered.csv](data/signals_filtered.csv)

---

## 📈 Historical Data

**Total Historical Records**: 520
**Unique Tokens Tracked**: 103
**Date Range**: 2025-10-01 to 2025-10-12

**Master Aggregations**: 103 tokens
**Performance Metrics**: 520 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 520 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 103 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 520 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 46 |
| [new_viable.csv](data/new_viable.csv) | New tokens with potential | 2 |
| [signals_filtered.csv](data/signals_filtered.csv) | Whale-filtered trading signals | 2 |

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

- **Data Repository**: [stelios5791/sol-reports](https://github.com/stelios5791/sol-reports)
- **Analysis Pipeline**: Private repository (automated daily)

---

*Generated automatically by Solana Radar pipeline*
