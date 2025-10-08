# 📊 Solana Radar - Daily Reports

**Last Updated**: 2025-10-08 22:37 UTC

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
          9,
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
| 1 | XBT | XBT | 22.68% | 🟢 low | $2.88 | $13.37 |
| 2 | RAGEGUY | Rage Guy | 27.29% | 🟢 low | $86.74K | $149.83K |
| 3 | ELIZABETH | Just Elizabeth Cat | 27.95% | 🟢 low | $21.18 | $57.56 |
| 4 | DREAM | Dreamsync | 32.23% | 🟢 low | $96.63K | $184.66K |
| 5 | FARTLESS | FARTLESS COIN | 33.38% | 🟢 low | $1.23K | $4.03K |
| 6 | FLY | Nexa | 34.30% | 🟢 low | $92.98 | $8.86K |
| 7 | USEFUL | USEFUL COIN | 41.10% | 🟢 low | $2.76 | $69.22 |
| 8 | AI20X | Ai20x.ai | 41.38% | 🟢 low | $90.87K | $2.74M |
| 9 | 1nu | 1nu | 42.88% | 🟢 low | $27.18K | $31.29K |
| 10 | gib | gib | 43.53% | 🟢 low | $2.47 | $75.73 |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | Hamu | Hamu | 99.90% | 🔴 extreme | $1.54 | $0.00 |
| 2 | PUMPFOLIO | Retail Summer | 99.88% | 🔴 extreme | $4.11 | $9.31K |
| 3 | Jewcat | Jewish Cat | 99.83% | 🔴 extreme | $1.04 | $0.00 |
| 4 | 1cat | 1 cat can change your lif | 99.78% | 🔴 extreme | $7.56 | $0.00 |
| 5 | MoneyBear | The Money Bears | 99.40% | 🔴 extreme | $42.77 | $9.69K |
| 6 | Mementoe | Mementoe | 99.37% | 🔴 extreme | $2.88 | $8.43K |
| 7 | BEANS | BEANS | 99.10% | 🔴 extreme | $2.15 | $9.61K |
| 8 | 19 | Cult of 19 | 98.82% | 🔴 extreme | $78.57 | $8.93K |
| 9 | REVIVE | reviving the memes | 98.59% | 🔴 extreme | $4.47 | $11.22K |
| 10 | FALCONS | THE FALCONS | 98.15% | 🔴 extreme | $4.33 | $10.70K |

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
      "2025-10-08"
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
          51.35
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
          32.23
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
          41.38
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
          27.29
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
      "AI20X",
      "RAGEGUY",
      "LION",
      "HAROLD",
      "1nu",
      "$CrepSol",
      "SHITTER"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          342445240.57,
          154294.78,
          96625.04,
          90865.1,
          86744.22,
          49137.81,
          43256.1,
          27184.82,
          5995.91,
          3820.59
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
          "#22c55e",
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
            "x": 252903.0,
            "y": 51.35,
            "symbol": "AI4",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 1609164.0,
            "y": 32.23,
            "symbol": "DREAM",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 23791169.0,
            "y": 41.38,
            "symbol": "AI20X",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 842378.0,
            "y": 27.29,
            "symbol": "RAGEGUY",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 76998080.0,
            "y": 57.84,
            "symbol": "LION",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 3582715.0,
            "y": 62.43,
            "symbol": "HAROLD",
            "risk": "medium",
            "backgroundColor": "#eab308"
          },
          {
            "x": 60229.0,
            "y": 42.88,
            "symbol": "1nu",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 47426.0,
            "y": 52.45,
            "symbol": "$CrepSol",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 27742.0,
            "y": 60.99,
            "symbol": "SHITTER",
            "risk": "medium",
            "backgroundColor": "#eab308"
          },
          {
            "x": 6964729.0,
            "y": 96.6,
            "symbol": "SOL",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 34502.0,
            "y": 73.18,
            "symbol": "1Bull",
            "risk": "medium",
            "backgroundColor": "#eab308"
          },
          {
            "x": 970192.0,
            "y": 33.38,
            "symbol": "FARTLESS",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 10475.0,
            "y": 88.6,
            "symbol": "DARE",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 173967.0,
            "y": 49.73,
            "symbol": "RUECAT",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 6098.0,
            "y": 88.82,
            "symbol": "RWA",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 10689.0,
            "y": 94.94,
            "symbol": "7",
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
            "x": 8784.0,
            "y": 85.81,
            "symbol": "FARTWORM",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 8085.0,
            "y": 91.24,
            "symbol": "1",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 6216.0,
            "y": 76.36,
            "symbol": "APOLLO",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 16264.0,
            "y": 34.3,
            "symbol": "FLY",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 9775.0,
            "y": 93.46,
            "symbol": "SUPRACOIN",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4857.0,
            "y": 98.82,
            "symbol": "19",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 312301.0,
            "y": 91.57,
            "symbol": "HOODIE",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 20723.0,
            "y": 84.33,
            "symbol": "AUSBAGWORK",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 4911.0,
            "y": 99.4,
            "symbol": "MoneyBear",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 13474.0,
            "y": 90.93,
            "symbol": "MOCHI",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 104526.0,
            "y": 44.27,
            "symbol": "YAO",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 1231313.0,
            "y": 27.95,
            "symbol": "ELIZABETH",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 4958.0,
            "y": 96.9,
            "symbol": "obvious",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 6543.47,
            "y": 99.78,
            "symbol": "1cat",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 5752.0,
            "y": 95.72,
            "symbol": "Streamless",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 5730.0,
            "y": 98.59,
            "symbol": "REVIVE",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 5536.0,
            "y": 98.15,
            "symbol": "FALCONS",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4887.0,
            "y": 99.88,
            "symbol": "PUMPFOLIO",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4474.0,
            "y": 99.37,
            "symbol": "Mementoe",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 1999085.0,
            "y": 22.68,
            "symbol": "XBT",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 211666.0,
            "y": 41.1,
            "symbol": "USEFUL",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 373531.0,
            "y": 43.53,
            "symbol": "gib",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 4151.0,
            "y": 98.06,
            "symbol": "1% Club",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 5268.0,
            "y": 97.23,
            "symbol": "viewer",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4945.0,
            "y": 99.1,
            "symbol": "BEANS",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 17293.0,
            "y": 79.61,
            "symbol": "IDIOT",
            "risk": "medium",
            "backgroundColor": "#eab308"
          },
          {
            "x": 6320.8,
            "y": 99.9,
            "symbol": "Hamu",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 6348.1,
            "y": 99.83,
            "symbol": "Jewcat",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 7716.0,
            "y": 98.01,
            "symbol": "JIFFPOM",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 5801.0,
            "y": 96.62,
            "symbol": "BULLCOIN",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 5805.0,
            "y": 98.02,
            "symbol": "Noxi",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4745.0,
            "y": 97.49,
            "symbol": "BLUB",
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
          "#22c55e",
          "#eab308",
          "#ef4444",
          "#eab308",
          "#22c55e",
          "#f97316",
          "#22c55e",
          "#f97316",
          "#ef4444",
          "#f97316",
          "#f97316",
          "#f97316",
          "#f97316",
          "#22c55e",
          "#ef4444",
          "#ef4444",
          "#f97316",
          "#f97316",
          "#ef4444",
          "#f97316",
          "#22c55e",
          "#22c55e",
          "#ef4444",
          "#ef4444",
          "#ef4444",
          "#ef4444",
          "#ef4444",
          "#ef4444",
          "#ef4444",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#ef4444",
          "#ef4444",
          "#ef4444",
          "#eab308",
          "#ef4444",
          "#ef4444",
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

**Total Tokens**: 50
**Combined 24h Volume**: $343.01M
**Combined Liquidity**: $65.08M

**Concentration Risk Distribution**:
- 🔴 Extreme: 21 tokens
- 🟢 Low: 15 tokens
- 🟡 High: 9 tokens
- 🟢 Medium: 4 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $342.45M | $58.75M | 🟢 unknown |
| 2 | AI4 | AI⁴ | $154.29K | $100.28K | 🟢 low |
| 3 | DREAM | Dreamsync | $96.63K | $184.66K | 🟢 low |
| 4 | AI20X | Ai20x.ai | $90.87K | $2.74M | 🟢 low |
| 5 | RAGEGUY | Rage Guy | $86.74K | $149.83K | 🟢 low |
| 6 | LION | Loaded Lions | $49.14K | $2.11M | 🟢 low |
| 7 | HAROLD | Harold | $43.26K | $561.49K | 🟢 medium |
| 8 | 1nu | 1nu | $27.18K | $31.29K | 🟢 low |
| 9 | $CrepSol | Crepe on Solana | $6.00K | $27.74K | 🟢 low |
| 10 | SHITTER | SHITTERCOIN | $3.82K | $22.74K | 🟢 medium |

📄 [Full data: daily_top50.csv](data/daily_top50.csv)

---

## 🌱 New Viable Tokens (7-14 Days Old)

New tokens showing potential with healthy metrics and lower concentration risk.

**Found**: 6 viable new tokens

**Criteria**:
- First seen 7-14 days ago
- Volume > $50K
- Liquidity > $100K
- Missing streak < 2 (stable presence)
- Concentration risk: low/medium

| Symbol | Name | Age (days) | Volume 24h | Liquidity | Top 10% |
|--------|------|------------|------------|-----------|---------|
| wSOL | Wrapped SOL | 7 | $342.45M | $58.75M | 0.00% |
| AI4 | AI⁴ | 7 | $154.29K | $100.28K | 51.35% |
| DREAM | Dreamsync | 7 | $96.63K | $184.66K | 32.23% |
| AI20X | Ai20x.ai | 7 | $90.87K | $2.74M | 41.38% |
| RAGEGUY | Rage Guy | 7 | $86.74K | $149.83K | 27.29% |
| USDUT | unstable tether | 7 | $57.89K | $114.66K | 37.30% |

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
- 👀 **Watch**: 5 tokens

### 👀 Watch List

*5 tokens showing elevated activity*

📄 [Full data: signals_filtered.csv](data/signals_filtered.csv)

---

## 📈 Historical Data

**Total Historical Records**: 524
**Unique Tokens Tracked**: 101
**Date Range**: 2025-10-01 to 2025-10-08

**Master Aggregations**: 101 tokens
**Performance Metrics**: 524 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 524 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 101 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 524 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 50 |
| [new_viable.csv](data/new_viable.csv) | New tokens with potential | 6 |
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
