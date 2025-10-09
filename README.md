# 📊 Solana Radar - Daily Reports

**Last Updated**: 2025-10-09 08:37 UTC

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
| 1 | XBT | XBT | 22.29% | 🟢 low | $2.23 | $16.69 |
| 2 | RAGEGUY | Rage Guy | 27.44% | 🟢 low | $72.77K | $142.51K |
| 3 | ELIZABETH | Just Elizabeth Cat | 28.45% | 🟢 low | $17.07 | $55.25 |
| 4 | DREAM | Dreamsync | 32.18% | 🟢 low | $190.37K | $181.06K |
| 5 | FARTLESS | FARTLESS COIN | 33.10% | 🟢 low | $799.37 | $3.95K |
| 6 | FLY | Nexa | 34.30% | 🟢 low | $90.54 | $8.86K |
| 7 | AI20X | Ai20x.ai | 41.36% | 🟢 low | $93.19K | $2.68M |
| 8 | USEFUL | USEFUL COIN | 42.50% | 🟢 low | $1.98 | $63.81 |
| 9 | gib | gib | 43.96% | 🟢 low | $1.50 | $74.51 |
| 10 | YAO | YAO MING | 44.61% | 🟢 low | $13.12 | $794.72 |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | GIVE50 | GIVING $50 AWAY EVERY 10M | 100.00% | 🔴 extreme | $1.73 | $0.00 |
| 2 | Hamu | Hamu | 99.90% | 🔴 extreme | $1.54 | $0.00 |
| 3 | PUMPFOLIO | Retail Summer | 99.88% | 🔴 extreme | $4.11 | $9.31K |
| 4 | 1cat | 1 cat can change your lif | 99.78% | 🔴 extreme | $1.07 | $0.00 |
| 5 | MINDWORMS | mindworms | 99.62% | 🔴 extreme | $3.85 | $8.57K |
| 6 | MoneyBear | The Money Bears | 99.40% | 🔴 extreme | $29.24 | $9.69K |
| 7 | Mementoe | Mementoe | 99.37% | 🔴 extreme | $2.88 | $8.43K |
| 8 | BEANS | BEANS | 99.10% | 🔴 extreme | $2.15 | $9.61K |
| 9 | 19 | Cult of 19 | 98.82% | 🔴 extreme | $78.57 | $8.86K |
| 10 | REVIVE | reviving the memes | 98.59% | 🔴 extreme | $3.23 | $11.41K |

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
          32.18
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
          51.99
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
          27.44
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
      "LION",
      "1nu",
      "HAROLD",
      "SOL",
      "$CrepSol"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          372774327.45,
          190372.69,
          124940.18,
          93186.0,
          72771.17,
          45636.31,
          32645.31,
          16916.43,
          15380.69,
          6806.53
        ],
        "backgroundColor": [
          "#94a3b8",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#eab308",
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
            "x": 1589712.0,
            "y": 32.18,
            "symbol": "DREAM",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 229897.0,
            "y": 51.99,
            "symbol": "AI4",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 22763939.0,
            "y": 41.36,
            "symbol": "AI20X",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 788885.0,
            "y": 27.44,
            "symbol": "RAGEGUY",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 73252372.0,
            "y": 57.84,
            "symbol": "LION",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 50470.0,
            "y": 45.27,
            "symbol": "1nu",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 3481396.0,
            "y": 62.53,
            "symbol": "HAROLD",
            "risk": "medium",
            "backgroundColor": "#eab308"
          },
          {
            "x": 3446104.0,
            "y": 96.52,
            "symbol": "SOL",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 41906.0,
            "y": 53.75,
            "symbol": "$CrepSol",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 19340.0,
            "y": 66.05,
            "symbol": "SHITTER",
            "risk": "medium",
            "backgroundColor": "#eab308"
          },
          {
            "x": 35666.0,
            "y": 72.23,
            "symbol": "1Bull",
            "risk": "medium",
            "backgroundColor": "#eab308"
          },
          {
            "x": 10842.0,
            "y": 87.64,
            "symbol": "DARE",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 932150.0,
            "y": 33.1,
            "symbol": "FARTLESS",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 171333.0,
            "y": 49.81,
            "symbol": "RUECAT",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 10435.0,
            "y": 95.09,
            "symbol": "7",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 6243.0,
            "y": 76.4,
            "symbol": "APOLLO",
            "risk": "medium",
            "backgroundColor": "#eab308"
          },
          {
            "x": 6099.0,
            "y": 88.82,
            "symbol": "RWA",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 5004.0,
            "y": 92.42,
            "symbol": "pibble",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 17204.0,
            "y": 80.61,
            "symbol": "IDIOT",
            "risk": "medium",
            "backgroundColor": "#eab308"
          },
          {
            "x": 8784.0,
            "y": 85.81,
            "symbol": "FARTWORM",
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
            "x": 4807.0,
            "y": 98.82,
            "symbol": "19",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 291383.0,
            "y": 91.64,
            "symbol": "HOODIE",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 9665.0,
            "y": 93.53,
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
            "x": 1114815.0,
            "y": 28.45,
            "symbol": "ELIZABETH",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 20543.0,
            "y": 84.33,
            "symbol": "AUSBAGWORK",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 8008.0,
            "y": 91.42,
            "symbol": "1",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 104216.0,
            "y": 44.61,
            "symbol": "YAO",
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
            "x": 4726.0,
            "y": 97.26,
            "symbol": "1",
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
            "x": 4887.0,
            "y": 99.88,
            "symbol": "PUMPFOLIO",
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
            "x": 5828.0,
            "y": 98.59,
            "symbol": "REVIVE",
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
            "x": 5155.0,
            "y": 97.24,
            "symbol": "viewer",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 1845476.0,
            "y": 22.29,
            "symbol": "XBT",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 4945.0,
            "y": 99.1,
            "symbol": "BEANS",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 5154.0,
            "y": 96.64,
            "symbol": "Hosico",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 187340.0,
            "y": 42.5,
            "symbol": "USEFUL",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 5969.0,
            "y": 96.65,
            "symbol": "BULLCOIN",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 6363.73,
            "y": 100.0,
            "symbol": "GIVE50",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 6320.8,
            "y": 99.9,
            "symbol": "Hamu",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 352256.0,
            "y": 43.96,
            "symbol": "gib",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 6543.47,
            "y": 99.78,
            "symbol": "1cat",
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
          }
        ],
        "backgroundColor": [
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#ef4444",
          "#22c55e",
          "#eab308",
          "#eab308",
          "#f97316",
          "#22c55e",
          "#22c55e",
          "#ef4444",
          "#eab308",
          "#f97316",
          "#f97316",
          "#eab308",
          "#f97316",
          "#22c55e",
          "#ef4444",
          "#f97316",
          "#ef4444",
          "#ef4444",
          "#22c55e",
          "#f97316",
          "#f97316",
          "#22c55e",
          "#f97316",
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
          "#22c55e",
          "#ef4444",
          "#ef4444",
          "#ef4444",
          "#22c55e",
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
**Combined 24h Volume**: $373.38M
**Combined Liquidity**: $64.00M

**Concentration Risk Distribution**:
- 🔴 Extreme: 21 tokens
- 🟢 Low: 15 tokens
- 🟡 High: 8 tokens
- 🟢 Medium: 5 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $372.77M | $57.87M | 🟢 unknown |
| 2 | DREAM | Dreamsync | $190.37K | $181.06K | 🟢 low |
| 3 | AI4 | AI⁴ | $124.94K | $94.09K | 🟢 low |
| 4 | AI20X | Ai20x.ai | $93.19K | $2.68M | 🟢 low |
| 5 | RAGEGUY | Rage Guy | $72.77K | $142.51K | 🟢 low |
| 6 | LION | Loaded Lions | $45.64K | $2.02M | 🟢 low |
| 7 | 1nu | 1nu | $32.65K | $28.67K | 🟢 low |
| 8 | HAROLD | Harold | $16.92K | $544.73K | 🟢 medium |
| 9 | SOL | Solana | $15.38K | $8.16K | 🔴 extreme |
| 10 | $CrepSol | Crepe on Solana | $6.81K | $25.70K | 🟢 low |

📄 [Full data: daily_top50.csv](data/daily_top50.csv)

---

## 🌱 New Viable Tokens (7-14 Days Old)

New tokens showing potential with healthy metrics and lower concentration risk.

**Found**: 5 viable new tokens

**Criteria**:
- First seen 7-14 days ago
- Volume > $50K
- Liquidity > $100K
- Missing streak < 2 (stable presence)
- Concentration risk: low/medium

| Symbol | Name | Age (days) | Volume 24h | Liquidity | Top 10% |
|--------|------|------------|------------|-----------|---------|
| wSOL | Wrapped SOL | 8 | $372.77M | $57.87M | 0.00% |
| DREAM | Dreamsync | 8 | $190.37K | $181.06K | 32.18% |
| AI20X | Ai20x.ai | 8 | $93.19K | $2.68M | 41.36% |
| RAGEGUY | Rage Guy | 8 | $72.77K | $142.51K | 27.44% |
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
- 👀 **Watch**: 5 tokens

### 👀 Watch List

*5 tokens showing elevated activity*

📄 [Full data: signals_filtered.csv](data/signals_filtered.csv)

---

## 📈 Historical Data

**Total Historical Records**: 524
**Unique Tokens Tracked**: 101
**Date Range**: 2025-10-01 to 2025-10-09

**Master Aggregations**: 101 tokens
**Performance Metrics**: 524 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 524 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 101 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 524 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 50 |
| [new_viable.csv](data/new_viable.csv) | New tokens with potential | 5 |
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
