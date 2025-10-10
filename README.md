# 📊 Solana Radar - Daily Reports

**Last Updated**: 2025-10-10 17:14 UTC

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
          21,
          8,
          4,
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
| 1 | XBT | XBT | 22.62% | 🟢 low | $95.91 | $665.08 |
| 2 | RAGEGUY | Rage Guy | 28.35% | 🟢 low | $58.11K | $122.84K |
| 3 | ELIZABETH | Just Elizabeth Cat | 28.65% | 🟢 low | $18.59 | $51.22 |
| 4 | DREAM | Dreamsync | 31.64% | 🟢 low | $99.11K | $189.64K |
| 5 | FLY | Nexa | 33.41% | 🟢 low | $2.42 | $9.26K |
| 6 | FARTLESS | FARTLESS COIN | 34.67% | 🟢 low | $1.27K | $3.65K |
| 7 | USEFUL | USEFUL COIN | 41.03% | 🟢 low | $4.98 | $56.69 |
| 8 | AI20X | Ai20x.ai | 41.39% | 🟢 low | $5.33K | $2.60M |
| 9 | YAO | YAO MING | 43.17% | 🟢 low | $3.22 | $753.71 |
| 10 | gib | gib | 43.88% | 🟢 low | $0.54 | $72.73 |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | Trey | Justice For Trey Reed | 100.00% | 🔴 extreme | $1.35 | $0.00 |
| 2 | YOU | YOU can change your life. | 99.99% | 🔴 extreme | $0.69 | $0.00 |
| 3 | Jewcat | Jewish Cat | 99.85% | 🔴 extreme | $0.18 | $0.00 |
| 4 | MoneyBear | The Money Bears | 99.44% | 🔴 extreme | $3.37 | $8.87K |
| 5 | Mementoe | Mementoe | 99.40% | 🔴 extreme | $6.13 | $8.29K |
| 6 | 19 | Cult of 19 | 98.89% | 🔴 extreme | $474.47 | $8.64K |
| 7 | REVIVE | reviving the memes | 98.66% | 🔴 extreme | $4.97 | $11.27K |
| 8 | JIFFPOM | Jiffpom | 98.29% | 🔴 extreme | $4.21 | $2.16K |
| 9 | Noxi | Noxi Labs AI | 98.28% | 🔴 extreme | $14.33 | $9.52K |
| 10 | FALCONS | THE FALCONS | 98.19% | 🔴 extreme | $1.93 | $10.80K |

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
      "2025-10-10"
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
        "label": "AI4",
        "data": [
          0.0,
          0.0,
          0.0,
          50.98,
          50.56,
          52.53,
          50.77
        ],
        "borderColor": "#ef4444",
        "backgroundColor": "#ef444420",
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
          31.64
        ],
        "borderColor": "#22c55e",
        "backgroundColor": "#22c55e20",
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
          28.35
        ],
        "borderColor": "#eab308",
        "backgroundColor": "#eab30820",
        "tension": 0.1,
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
          44.2
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
      "AI4",
      "DREAM",
      "RAGEGUY",
      "1nu",
      "LION",
      "HAROLD",
      "AI20X",
      "SHITTER",
      "FARTLESS"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          397344452.75,
          114594.33,
          99109.55,
          58114.38,
          31311.42,
          26996.36,
          10443.87,
          5332.74,
          1764.13,
          1271.19
        ],
        "backgroundColor": [
          "#94a3b8",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#22c55e",
          "#eab308",
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
            "x": 202846.0,
            "y": 50.77,
            "symbol": "AI4",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 1840820.0,
            "y": 31.64,
            "symbol": "DREAM",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 614734.0,
            "y": 28.35,
            "symbol": "RAGEGUY",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 46869.0,
            "y": 44.2,
            "symbol": "1nu",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 69717740.0,
            "y": 57.84,
            "symbol": "LION",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 3572267.0,
            "y": 62.36,
            "symbol": "HAROLD",
            "risk": "medium",
            "backgroundColor": "#eab308"
          },
          {
            "x": 22015464.0,
            "y": 41.39,
            "symbol": "AI20X",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 19029.0,
            "y": 66.07,
            "symbol": "SHITTER",
            "risk": "medium",
            "backgroundColor": "#eab308"
          },
          {
            "x": 791727.0,
            "y": 34.67,
            "symbol": "FARTLESS",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 40696.0,
            "y": 54.21,
            "symbol": "$CrepSol",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 3078724.0,
            "y": 96.52,
            "symbol": "SOL",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 6163.0,
            "y": 93.5,
            "symbol": "1",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 28066.0,
            "y": 74.45,
            "symbol": "1Bull",
            "risk": "medium",
            "backgroundColor": "#eab308"
          },
          {
            "x": 154161.0,
            "y": 50.3,
            "symbol": "RUECAT",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 4677.0,
            "y": 98.89,
            "symbol": "19",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 5070.0,
            "y": 96.31,
            "symbol": "Streamless",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 17248.0,
            "y": 79.74,
            "symbol": "IDIOT",
            "risk": "medium",
            "backgroundColor": "#eab308"
          },
          {
            "x": 4595.0,
            "y": 97.3,
            "symbol": "1",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 8415.0,
            "y": 87.15,
            "symbol": "FARTWORM",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 18952.0,
            "y": 85.47,
            "symbol": "AUSBAGWORK",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 9875.0,
            "y": 88.84,
            "symbol": "DARE",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 4928.0,
            "y": 97.59,
            "symbol": "viewer",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 274956.0,
            "y": 91.74,
            "symbol": "HOODIE",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 9253.0,
            "y": 94.2,
            "symbol": "SUPRACOIN",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 1761858.0,
            "y": 22.62,
            "symbol": "XBT",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 6099.0,
            "y": 76.69,
            "symbol": "APOLLO",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 4961.0,
            "y": 96.96,
            "symbol": "Hosico",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4890.0,
            "y": 93.32,
            "symbol": "pibble",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 9772.0,
            "y": 95.28,
            "symbol": "7",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 1131365.0,
            "y": 28.65,
            "symbol": "ELIZABETH",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 5206.0,
            "y": 90.0,
            "symbol": "RWA",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 5706.0,
            "y": 98.28,
            "symbol": "Noxi",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4944.0,
            "y": 97.07,
            "symbol": "obvious",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 12438.0,
            "y": 90.96,
            "symbol": "MOCHI",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 4395.0,
            "y": 99.4,
            "symbol": "Mementoe",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 163649.0,
            "y": 41.03,
            "symbol": "USEFUL",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 5754.0,
            "y": 98.66,
            "symbol": "REVIVE",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 7403.0,
            "y": 98.29,
            "symbol": "JIFFPOM",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4480.0,
            "y": 99.44,
            "symbol": "MoneyBear",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 98000.0,
            "y": 43.17,
            "symbol": "YAO",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 17716.0,
            "y": 33.41,
            "symbol": "FLY",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 5585.0,
            "y": 98.19,
            "symbol": "FALCONS",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 6199.51,
            "y": 100.0,
            "symbol": "Trey",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 5805.0,
            "y": 96.82,
            "symbol": "BULLCOIN",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 7533.73,
            "y": 99.99,
            "symbol": "YOU",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 5010.0,
            "y": 97.16,
            "symbol": "Bagwork",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 322108.0,
            "y": 43.88,
            "symbol": "gib",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 6299.44,
            "y": 99.85,
            "symbol": "Jewcat",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          }
        ],
        "backgroundColor": [
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#22c55e",
          "#eab308",
          "#22c55e",
          "#22c55e",
          "#ef4444",
          "#ef4444",
          "#eab308",
          "#22c55e",
          "#ef4444",
          "#ef4444",
          "#eab308",
          "#ef4444",
          "#f97316",
          "#f97316",
          "#f97316",
          "#ef4444",
          "#f97316",
          "#ef4444",
          "#22c55e",
          "#f97316",
          "#ef4444",
          "#f97316",
          "#ef4444",
          "#22c55e",
          "#f97316",
          "#ef4444",
          "#ef4444",
          "#f97316",
          "#ef4444",
          "#22c55e",
          "#ef4444",
          "#ef4444",
          "#ef4444",
          "#22c55e",
          "#22c55e",
          "#ef4444",
          "#ef4444",
          "#ef4444",
          "#ef4444",
          "#ef4444",
          "#22c55e",
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

**Total Tokens**: 49
**Combined 24h Volume**: $397.70M
**Combined Liquidity**: $62.23M

**Concentration Risk Distribution**:
- 🔴 Extreme: 21 tokens
- 🟢 Low: 15 tokens
- 🟡 High: 8 tokens
- 🟢 Medium: 4 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $397.34M | $56.32M | 🟢 unknown |
| 2 | AI4 | AI⁴ | $114.59K | $86.33K | 🟢 low |
| 3 | DREAM | Dreamsync | $99.11K | $189.64K | 🟢 low |
| 4 | RAGEGUY | Rage Guy | $58.11K | $122.84K | 🟢 low |
| 5 | 1nu | 1nu | $31.31K | $27.73K | 🟢 low |
| 6 | LION | Loaded Lions | $27.00K | $1.92M | 🟢 low |
| 7 | HAROLD | Harold | $10.44K | $539.64K | 🟢 medium |
| 8 | AI20X | Ai20x.ai | $5.33K | $2.60M | 🟢 low |
| 9 | SHITTER | SHITTERCOIN | $1.76K | $19.37K | 🟢 medium |
| 10 | FARTLESS | FARTLESS COIN | $1.27K | $3.65K | 🟢 low |

📄 [Full data: daily_top50.csv](data/daily_top50.csv)

---

## 🌱 New Viable Tokens (7-14 Days Old)

New tokens showing potential with healthy metrics and lower concentration risk.

**Found**: 4 viable new tokens

**Criteria**:
- First seen 7-14 days ago
- Volume > $50K
- Liquidity > $100K
- Missing streak < 2 (stable presence)
- Concentration risk: low/medium

| Symbol | Name | Age (days) | Volume 24h | Liquidity | Top 10% |
|--------|------|------------|------------|-----------|---------|
| wSOL | Wrapped SOL | 9 | $397.34M | $56.32M | 0.00% |
| DREAM | Dreamsync | 9 | $99.11K | $189.64K | 31.64% |
| RAGEGUY | Rage Guy | 9 | $58.11K | $122.84K | 28.35% |
| USDUT | unstable tether | 9 | $57.89K | $114.66K | 37.30% |

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

### 👀 Watch List

*3 tokens showing elevated activity*

📄 [Full data: signals_filtered.csv](data/signals_filtered.csv)

---

## 📈 Historical Data

**Total Historical Records**: 523
**Unique Tokens Tracked**: 102
**Date Range**: 2025-10-01 to 2025-10-10

**Master Aggregations**: 102 tokens
**Performance Metrics**: 523 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 523 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 102 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 523 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 49 |
| [new_viable.csv](data/new_viable.csv) | New tokens with potential | 4 |
| [signals_filtered.csv](data/signals_filtered.csv) | Whale-filtered trading signals | 3 |

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
