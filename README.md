# 📊 Solana Radar - Daily Reports

**Last Updated**: 2025-10-11 08:33 UTC

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
          24,
          6,
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
| 1 | XBT | XBT | 22.74% | 🟢 low | $494.48 | $569.60 |
| 2 | RAGEGUY | Rage Guy | 28.11% | 🟢 low | $69.57K | $108.86K |
| 3 | ELIZABETH | Just Elizabeth Cat | 29.51% | 🟢 low | $19.88 | $42.05 |
| 4 | DREAM | Dreamsync | 31.64% | 🟢 low | $85.46K | $164.99K |
| 5 | FLY | Nexa | 33.41% | 🟢 low | $12.67 | $7.63K |
| 6 | FARTLESS | FARTLESS COIN | 34.88% | 🟢 low | $2.46K | $3.42K |
| 7 | USEFUL | USEFUL COIN | 40.95% | 🟢 low | $7.08 | $46.80 |
| 8 | AI20X | Ai20x.ai | 41.39% | 🟢 low | $393.49 | $2.17M |
| 9 | YAO | YAO MING | 43.86% | 🟢 low | $3.51 | $683.04 |
| 10 | gib | gib | 44.95% | 🟢 low | $5.25 | $69.63 |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | Trey | Justice For Trey Reed | 100.00% | 🔴 extreme | $1.35 | $0.00 |
| 2 | Gaming | Gaming Cult | 99.97% | 🔴 extreme | $2.90 | $0.00 |
| 3 | 2 | TWO IS BETTER THAN ONE | 99.85% | 🔴 extreme | $0.53 | $0.00 |
| 4 | Jewcat | Jewish Cat | 99.85% | 🔴 extreme | $0.18 | $0.00 |
| 5 | MOONCOIN | MOON COIN | 99.70% | 🔴 extreme | $38.40 | $7.34K |
| 6 | MINDWORMS | mindworms | 99.63% | 🔴 extreme | $0.25 | $7.00K |
| 7 | MoneyBear | The Money Bears | 99.45% | 🔴 extreme | $3.59 | $7.78K |
| 8 | retail | retail | 99.37% | 🔴 extreme | $66.46 | $7.11K |
| 9 | BEANS | BEANS | 99.15% | 🔴 extreme | $0.91 | $7.99K |
| 10 | BEANIE | BEANIE | 99.05% | 🔴 extreme | $101.05 | $7.67K |

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
      "2025-10-11"
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
          50.63
        ],
        "borderColor": "#ef4444",
        "backgroundColor": "#ef444420",
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
        "borderColor": "#22c55e",
        "backgroundColor": "#22c55e20",
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
        "borderColor": "#eab308",
        "backgroundColor": "#eab30820",
        "tension": 0.1,
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
          62.87
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
      "LION",
      "DREAM",
      "HAROLD",
      "RAGEGUY",
      "1nu",
      "SOL",
      "FARTLESS",
      "1Bull"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          1236840689.03,
          146646.22,
          107607.75,
          85456.84,
          69673.07,
          69573.39,
          24423.13,
          3882.24,
          2460.9,
          2077.7
        ],
        "backgroundColor": [
          "#94a3b8",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#22c55e",
          "#22c55e",
          "#ef4444",
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
            "x": 182268.0,
            "y": 50.63,
            "symbol": "AI4",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 60393841.0,
            "y": 57.84,
            "symbol": "LION",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 1601688.0,
            "y": 31.64,
            "symbol": "DREAM",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 2953164.0,
            "y": 62.87,
            "symbol": "HAROLD",
            "risk": "medium",
            "backgroundColor": "#eab308"
          },
          {
            "x": 558025.0,
            "y": 28.11,
            "symbol": "RAGEGUY",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 36581.0,
            "y": 49.04,
            "symbol": "1nu",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 4356322.0,
            "y": 96.6,
            "symbol": "SOL",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 695033.0,
            "y": 34.88,
            "symbol": "FARTLESS",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 26071.0,
            "y": 73.43,
            "symbol": "1Bull",
            "risk": "medium",
            "backgroundColor": "#eab308"
          },
          {
            "x": 18889.0,
            "y": 66.29,
            "symbol": "SHITTER",
            "risk": "medium",
            "backgroundColor": "#eab308"
          },
          {
            "x": 33897.0,
            "y": 54.73,
            "symbol": "$CrepSol",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 109640.0,
            "y": 52.22,
            "symbol": "RUECAT",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 1508198.0,
            "y": 22.74,
            "symbol": "XBT",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 18285366.0,
            "y": 41.39,
            "symbol": "AI20X",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 11045.0,
            "y": 91.16,
            "symbol": "MOCHI",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 8820.0,
            "y": 88.65,
            "symbol": "DARE",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 15930.0,
            "y": 85.83,
            "symbol": "AUSBAGWORK",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 14967.0,
            "y": 79.74,
            "symbol": "IDIOT",
            "risk": "medium",
            "backgroundColor": "#eab308"
          },
          {
            "x": 7908.0,
            "y": 95.55,
            "symbol": "7",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4702.0,
            "y": 98.47,
            "symbol": "Noxi",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 6017.0,
            "y": 93.57,
            "symbol": "1",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 7490.0,
            "y": 94.25,
            "symbol": "SUPRACOIN",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4041.0,
            "y": 99.05,
            "symbol": "BEANIE",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 3609.0,
            "y": 99.37,
            "symbol": "retail",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4019.0,
            "y": 97.39,
            "symbol": "Hosico",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 7080.0,
            "y": 86.58,
            "symbol": "FARTWORM",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 4677.0,
            "y": 98.89,
            "symbol": "19",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 3734.0,
            "y": 99.7,
            "symbol": "MOONCOIN",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4743.0,
            "y": 96.88,
            "symbol": "BULLCOIN",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 744391.0,
            "y": 29.51,
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
            "x": 5925.0,
            "y": 76.7,
            "symbol": "APOLLO",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 14642.0,
            "y": 33.41,
            "symbol": "FLY",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 4425.0,
            "y": 96.46,
            "symbol": "Streamless",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 156169.0,
            "y": 40.95,
            "symbol": "USEFUL",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 4091.0,
            "y": 97.21,
            "symbol": "obvious",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 270594.0,
            "y": 44.95,
            "symbol": "gib",
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
            "x": 3930.0,
            "y": 99.45,
            "symbol": "MoneyBear",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 89733.0,
            "y": 43.86,
            "symbol": "YAO",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 5943.85,
            "y": 99.97,
            "symbol": "Gaming",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 3939.0,
            "y": 97.62,
            "symbol": "viewer",
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
            "x": 4109.0,
            "y": 99.15,
            "symbol": "BEANS",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4759.0,
            "y": 98.19,
            "symbol": "FALCONS",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 5230.48,
            "y": 99.85,
            "symbol": "2",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 3700.0,
            "y": 99.63,
            "symbol": "MINDWORMS",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
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
          "#eab308",
          "#22c55e",
          "#22c55e",
          "#ef4444",
          "#22c55e",
          "#eab308",
          "#eab308",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#f97316",
          "#f97316",
          "#f97316",
          "#eab308",
          "#ef4444",
          "#ef4444",
          "#ef4444",
          "#ef4444",
          "#ef4444",
          "#ef4444",
          "#ef4444",
          "#f97316",
          "#ef4444",
          "#ef4444",
          "#ef4444",
          "#22c55e",
          "#f97316",
          "#f97316",
          "#22c55e",
          "#ef4444",
          "#22c55e",
          "#ef4444",
          "#22c55e",
          "#ef4444",
          "#ef4444",
          "#ef4444",
          "#22c55e",
          "#ef4444",
          "#ef4444",
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
**Combined 24h Volume**: $1.24B
**Combined Liquidity**: $56.16M

**Concentration Risk Distribution**:
- 🔴 Extreme: 24 tokens
- 🟢 Low: 15 tokens
- 🟡 High: 6 tokens
- 🟢 Medium: 4 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $1.24B | $51.11M | 🟢 unknown |
| 2 | AI4 | AI⁴ | $146.65K | $76.99K | 🟢 low |
| 3 | LION | Loaded Lions | $107.61K | $1.68M | 🟢 low |
| 4 | DREAM | Dreamsync | $85.46K | $164.99K | 🟢 low |
| 5 | HAROLD | Harold | $69.67K | $460.32K | 🟢 medium |
| 6 | RAGEGUY | Rage Guy | $69.57K | $108.86K | 🟢 low |
| 7 | 1nu | 1nu | $24.42K | $24.53K | 🟢 low |
| 8 | SOL | Solana | $3.88K | $8.40K | 🔴 extreme |
| 9 | FARTLESS | FARTLESS COIN | $2.46K | $3.42K | 🟢 low |
| 10 | 1Bull | One bull run to change your li | $2.08K | $19.22K | 🟢 medium |

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
| wSOL | Wrapped SOL | 10 | $1.24B | $51.11M | 0.00% |
| LION | Loaded Lions | 10 | $107.61K | $1.68M | 57.84% |
| DREAM | Dreamsync | 10 | $85.46K | $164.99K | 31.64% |
| HAROLD | Harold | 10 | $69.67K | $460.32K | 62.87% |
| RAGEGUY | Rage Guy | 10 | $69.57K | $108.86K | 28.11% |
| USDUT | unstable tether | 10 | $57.89K | $114.66K | 37.30% |

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

### 👀 Watch List

*4 tokens showing elevated activity*

📄 [Full data: signals_filtered.csv](data/signals_filtered.csv)

---

## 📈 Historical Data

**Total Historical Records**: 524
**Unique Tokens Tracked**: 102
**Date Range**: 2025-10-01 to 2025-10-11

**Master Aggregations**: 102 tokens
**Performance Metrics**: 524 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 524 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 102 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 524 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 50 |
| [new_viable.csv](data/new_viable.csv) | New tokens with potential | 6 |
| [signals_filtered.csv](data/signals_filtered.csv) | Whale-filtered trading signals | 4 |

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
