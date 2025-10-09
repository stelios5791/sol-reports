# 📊 Solana Radar - Daily Reports

**Last Updated**: 2025-10-09 17:26 UTC

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
          9,
          5,
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
| 1 | XBT | XBT | 22.28% | 🟢 low | $2.21 | $17.29 |
| 2 | RAGEGUY | Rage Guy | 27.80% | 🟢 low | $39.44K | $135.27K |
| 3 | ELIZABETH | Just Elizabeth Cat | 28.98% | 🟢 low | $27.24 | $51.51 |
| 4 | DREAM | Dreamsync | 31.66% | 🟢 low | $205.96K | $196.84K |
| 5 | FARTLESS | FARTLESS COIN | 33.31% | 🟢 low | $741.86 | $3.91K |
| 6 | FLY | Nexa | 33.41% | 🟢 low | $198.39 | $9.30K |
| 7 | USEFUL | USEFUL COIN | 40.10% | 🟢 low | $4.44 | $68.55 |
| 8 | AI20X | Ai20x.ai | 41.36% | 🟢 low | $72.38K | $2.57M |
| 9 | 1nu | 1nu | 44.13% | 🟢 low | $38.78K | $30.22K |
| 10 | gib | gib | 44.24% | 🟢 low | $1.89 | $73.36 |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | GIVE50 | GIVING $50 AWAY EVERY 10M | 100.00% | 🔴 extreme | $1.73 | $0.00 |
| 2 | COUNT | Counting live till $100M | 99.98% | 🔴 extreme | $0.98 | $8.46K |
| 3 | KENNY | KENNY KO | 99.66% | 🔴 extreme | $0.10 | $8.55K |
| 4 | MINDWORMS | mindworms | 99.62% | 🔴 extreme | $3.85 | $8.57K |
| 5 | MoneyBear | The Money Bears | 99.40% | 🔴 extreme | $29.24 | $9.69K |
| 6 | ORE | Ore Labs | 99.20% | 🔴 extreme | $1.17 | $8.16K |
| 7 | BEANS | BEANS | 99.13% | 🔴 extreme | $1.59 | $9.54K |
| 8 | 19 | Cult of 19 | 98.82% | 🔴 extreme | $0.57 | $8.86K |
| 9 | JIFFPOM | Jiffpom | 98.24% | 🔴 extreme | $18.85 | $12.46K |
| 10 | FALCONS | THE FALCONS | 98.15% | 🔴 extreme | $0.14 | $11.10K |

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
      "2025-10-09"
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
          31.66
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
          50.59
        ],
        "borderColor": "#22c55e",
        "backgroundColor": "#22c55e20",
        "tension": 0.1,
        "fill": false
      },
      {
        "label": "AI20X",
        "data": [
          0.0,
          0.0,
          0.0,
          0.0,
          0.0,
          39.37,
          41.36
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
          27.8
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
      "AI20X",
      "RAGEGUY",
      "1nu",
      "LION",
      "SOL",
      "HAROLD",
      "SHITTER"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          433808273.47,
          205961.75,
          106431.83,
          72384.17,
          39444.73,
          38777.15,
          22780.76,
          17465.12,
          12257.32,
          3499.54
        ],
        "backgroundColor": [
          "#94a3b8",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#ef4444",
          "#eab308",
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
            "x": 1903546.0,
            "y": 31.66,
            "symbol": "DREAM",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 240988.0,
            "y": 50.59,
            "symbol": "AI4",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 21837179.0,
            "y": 41.36,
            "symbol": "AI20X",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 719538.0,
            "y": 27.8,
            "symbol": "RAGEGUY",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 55907.0,
            "y": 44.13,
            "symbol": "1nu",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 72690216.0,
            "y": 57.84,
            "symbol": "LION",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 2908212.0,
            "y": 96.52,
            "symbol": "SOL",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 3501525.0,
            "y": 62.52,
            "symbol": "HAROLD",
            "risk": "medium",
            "backgroundColor": "#eab308"
          },
          {
            "x": 21116.0,
            "y": 63.55,
            "symbol": "SHITTER",
            "risk": "medium",
            "backgroundColor": "#eab308"
          },
          {
            "x": 43035.0,
            "y": 53.86,
            "symbol": "$CrepSol",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 31141.0,
            "y": 73.45,
            "symbol": "1Bull",
            "risk": "medium",
            "backgroundColor": "#eab308"
          },
          {
            "x": 8083.0,
            "y": 91.41,
            "symbol": "1",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 913089.0,
            "y": 33.31,
            "symbol": "FARTLESS",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 5255.0,
            "y": 89.62,
            "symbol": "RWA",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 9734.0,
            "y": 95.07,
            "symbol": "7",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 164714.0,
            "y": 50.04,
            "symbol": "RUECAT",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 10601.0,
            "y": 87.68,
            "symbol": "DARE",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 19233.0,
            "y": 85.16,
            "symbol": "AUSBAGWORK",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 17789.0,
            "y": 33.41,
            "symbol": "FLY",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 4875.0,
            "y": 97.12,
            "symbol": "1",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 16857.0,
            "y": 80.69,
            "symbol": "IDIOT",
            "risk": "medium",
            "backgroundColor": "#eab308"
          },
          {
            "x": 5004.0,
            "y": 92.42,
            "symbol": "pibble",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 6337.0,
            "y": 76.43,
            "symbol": "APOLLO",
            "risk": "medium",
            "backgroundColor": "#eab308"
          },
          {
            "x": 287129.0,
            "y": 91.61,
            "symbol": "HOODIE",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 5826.0,
            "y": 96.83,
            "symbol": "BULLCOIN",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 9377.0,
            "y": 93.79,
            "symbol": "SUPRACOIN",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4911.0,
            "y": 99.4,
            "symbol": "MoneyBear",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 1044676.0,
            "y": 28.98,
            "symbol": "ELIZABETH",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 7602.0,
            "y": 98.24,
            "symbol": "JIFFPOM",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 104216.0,
            "y": 45.12,
            "symbol": "YAO",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 209710.0,
            "y": 40.1,
            "symbol": "USEFUL",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 5084.0,
            "y": 97.3,
            "symbol": "viewer",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4534.0,
            "y": 99.62,
            "symbol": "MINDWORMS",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 1838.0,
            "y": 96.31,
            "symbol": "PROFIT",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 1989523.0,
            "y": 22.28,
            "symbol": "XBT",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 5154.0,
            "y": 96.64,
            "symbol": "Hosico",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 332656.0,
            "y": 44.24,
            "symbol": "gib",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 13173.0,
            "y": 90.93,
            "symbol": "MOCHI",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 6363.73,
            "y": 100.0,
            "symbol": "GIVE50",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4910.0,
            "y": 99.13,
            "symbol": "BEANS",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4200.0,
            "y": 99.2,
            "symbol": "ORE",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4267.0,
            "y": 99.98,
            "symbol": "COUNT",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4807.0,
            "y": 98.82,
            "symbol": "19",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 8832.0,
            "y": 85.82,
            "symbol": "FARTWORM",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 5082.0,
            "y": 96.91,
            "symbol": "obvious",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4745.0,
            "y": 97.49,
            "symbol": "BLUB",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 5743.0,
            "y": 98.15,
            "symbol": "FALCONS",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4520.0,
            "y": 99.66,
            "symbol": "KENNY",
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
          "#22c55e",
          "#ef4444",
          "#eab308",
          "#eab308",
          "#22c55e",
          "#eab308",
          "#f97316",
          "#22c55e",
          "#f97316",
          "#ef4444",
          "#22c55e",
          "#f97316",
          "#f97316",
          "#22c55e",
          "#ef4444",
          "#eab308",
          "#f97316",
          "#eab308",
          "#f97316",
          "#ef4444",
          "#ef4444",
          "#ef4444",
          "#22c55e",
          "#ef4444",
          "#22c55e",
          "#22c55e",
          "#ef4444",
          "#ef4444",
          "#f97316",
          "#22c55e",
          "#ef4444",
          "#22c55e",
          "#f97316",
          "#ef4444",
          "#ef4444",
          "#ef4444",
          "#ef4444",
          "#ef4444",
          "#f97316",
          "#ef4444",
          "#ef4444",
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

**Total Tokens**: 49
**Combined 24h Volume**: $434.34M
**Combined Liquidity**: $63.73M

**Concentration Risk Distribution**:
- 🔴 Extreme: 19 tokens
- 🟢 Low: 15 tokens
- 🟡 High: 9 tokens
- 🟢 Medium: 5 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $433.81M | $57.70M | 🟢 unknown |
| 2 | DREAM | Dreamsync | $205.96K | $196.84K | 🟢 low |
| 3 | AI4 | AI⁴ | $106.43K | $95.84K | 🟢 low |
| 4 | AI20X | Ai20x.ai | $72.38K | $2.57M | 🟢 low |
| 5 | RAGEGUY | Rage Guy | $39.44K | $135.27K | 🟢 low |
| 6 | 1nu | 1nu | $38.78K | $30.22K | 🟢 low |
| 7 | LION | Loaded Lions | $22.78K | $2.00M | 🟢 low |
| 8 | SOL | Solana | $17.47K | $7.46K | 🔴 extreme |
| 9 | HAROLD | Harold | $12.26K | $542.88K | 🟢 medium |
| 10 | SHITTER | SHITTERCOIN | $3.50K | $20.24K | 🟢 medium |

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
| wSOL | Wrapped SOL | 8 | $433.81M | $57.70M | 0.00% |
| DREAM | Dreamsync | 8 | $205.96K | $196.84K | 31.66% |
| AI20X | Ai20x.ai | 8 | $72.38K | $2.57M | 41.36% |
| USDUT | unstable tether | 8 | $57.89K | $114.66K | 37.30% |

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
- 👀 **Watch**: 4 tokens
- 🚀 **Breakout**: 1 tokens

### 🚀 Breakout Signals

| Symbol | Score | Vol 3v1 | Z-Score Vol | Liq 3d | Streak |
|--------|-------|---------|-------------|--------|--------|
| wSOL | 57871.02 | 2.70x | 1.55 | $57.86M | 1d |

### 👀 Watch List

*4 tokens showing elevated activity*

📄 [Full data: signals_filtered.csv](data/signals_filtered.csv)

---

## 📈 Historical Data

**Total Historical Records**: 523
**Unique Tokens Tracked**: 101
**Date Range**: 2025-10-01 to 2025-10-09

**Master Aggregations**: 101 tokens
**Performance Metrics**: 523 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 523 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 101 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 523 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 49 |
| [new_viable.csv](data/new_viable.csv) | New tokens with potential | 4 |
| [signals_filtered.csv](data/signals_filtered.csv) | Whale-filtered trading signals | 5 |

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
