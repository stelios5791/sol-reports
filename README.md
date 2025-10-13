# 📊 Solana Radar - Daily Reports

**Last Updated**: 2025-10-13 08:40 UTC

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
          17,
          7,
          3,
          16,
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
| 1 | XBT | XBT | 22.91% | 🟢 low | $363.48 | $605.38 |
| 2 | RAGEGUY | Rage Guy | 27.24% | 🟢 low | $18.42K | $130.48K |
| 3 | ELIZABETH | Just Elizabeth Cat | 28.86% | 🟢 low | $8.66 | $46.61 |
| 4 | DREAM | Dreamsync | 31.60% | 🟢 low | $88.75K | $181.82K |
| 5 | FLY | Nexa | 31.73% | 🟢 low | $11.61 | $8.42K |
| 6 | FARTLESS | FARTLESS COIN | 34.52% | 🟢 low | $2.32K | $3.69K |
| 7 | USDUT | unstable tether | 40.39% | 🟢 low | $9.74 | $70.68 |
| 8 | USEFUL | USEFUL COIN | 40.51% | 🟢 low | $3.56 | $63.78 |
| 9 | AI20X | Ai20x.ai | 41.41% | 🟢 low | $23.95 | $2.32M |
| 10 | gib | gib | 44.58% | 🟢 low | $0.81 | $71.52 |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | KINT | Kintscan | 100.00% | 🔴 extreme | $8.38 | $0.00 |
| 2 | Jewcat | Jewish Cat | 99.87% | 🔴 extreme | $8.19 | $0.00 |
| 3 | Supershiro | Super Shiro | 99.53% | 🔴 extreme | $1.99 | $7.33K |
| 4 | BEANS | BEANS | 99.17% | 🔴 extreme | $0.57 | $8.59K |
| 5 | Noxi | Noxi Labs AI | 98.51% | 🔴 extreme | $1.81 | $8.23K |
| 6 | JIFFPOM | Jiffpom | 98.43% | 🔴 extreme | $3.06 | $10.44K |
| 7 | FALCONS | THE FALCONS | 98.29% | 🔴 extreme | $4.18 | $9.64K |
| 8 | viewer | in a streamers world | 97.73% | 🔴 extreme | $2.40 | $8.08K |
| 9 | 1 | 1 pill can change your li | 97.54% | 🔴 extreme | $9.69 | $7.60K |
| 10 | BLUB | Blub | 97.49% | 🔴 extreme | $1.08 | $7.87K |

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
      "2025-10-13"
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
          31.6
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
          45.78
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
        "label": "HAROLD",
        "data": [
          0.0,
          0.0,
          0.0,
          61.9,
          61.92,
          62.0,
          62.83
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
      "HAROLD",
      "RAGEGUY",
      "HOODIE",
      "1nu",
      "1Bull",
      "FARTLESS"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          511281981.97,
          88754.1,
          84504.7,
          44269.91,
          20409.62,
          18415.37,
          17216.18,
          16793.48,
          2648.0,
          2323.36
        ],
        "backgroundColor": [
          "#94a3b8",
          "#22c55e",
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#22c55e",
          "#22c55e",
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
            "x": 1785700.0,
            "y": 31.6,
            "symbol": "DREAM",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 274707.0,
            "y": 45.78,
            "symbol": "AI4",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 64539554.0,
            "y": 57.84,
            "symbol": "LION",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 3149244.0,
            "y": 62.83,
            "symbol": "HAROLD",
            "risk": "medium",
            "backgroundColor": "#eab308"
          },
          {
            "x": 737414.0,
            "y": 27.24,
            "symbol": "RAGEGUY",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 60782.0,
            "y": 53.17,
            "symbol": "HOODIE",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 31937.0,
            "y": 51.87,
            "symbol": "1nu",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 28470.0,
            "y": 74.1,
            "symbol": "1Bull",
            "risk": "medium",
            "backgroundColor": "#eab308"
          },
          {
            "x": 804872.0,
            "y": 34.52,
            "symbol": "FARTLESS",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 40092.0,
            "y": 53.45,
            "symbol": "$CrepSol",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 7342630.0,
            "y": 96.67,
            "symbol": "SOL",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 18485.0,
            "y": 67.69,
            "symbol": "SHITTER",
            "risk": "medium",
            "backgroundColor": "#eab308"
          },
          {
            "x": 16668.0,
            "y": 86.19,
            "symbol": "AUSBAGWORK",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 11895.0,
            "y": 85.69,
            "symbol": "IDIOT",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 116524.0,
            "y": 52.27,
            "symbol": "RUECAT",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 1571730.0,
            "y": 22.91,
            "symbol": "XBT",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 4558.0,
            "y": 95.38,
            "symbol": "pibble",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 8012.0,
            "y": 94.24,
            "symbol": "SUPRACOIN",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4849.0,
            "y": 97.07,
            "symbol": "BULLCOIN",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 11480.0,
            "y": 91.24,
            "symbol": "MOCHI",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 5245.0,
            "y": 89.7,
            "symbol": "RWA",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 9114.0,
            "y": 89.05,
            "symbol": "DARE",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 19538696.0,
            "y": 41.41,
            "symbol": "AI20X",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 16544.0,
            "y": 31.73,
            "symbol": "FLY",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 197701.0,
            "y": 40.39,
            "symbol": "USDUT",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 4107.0,
            "y": 97.54,
            "symbol": "1",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 885682.0,
            "y": 28.86,
            "symbol": "ELIZABETH",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 5300.0,
            "y": 100.0,
            "symbol": "KINT",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 5581.44,
            "y": 99.87,
            "symbol": "Jewcat",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4972.0,
            "y": 98.29,
            "symbol": "FALCONS",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 172844.0,
            "y": 40.51,
            "symbol": "USEFUL",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 5530.0,
            "y": 94.29,
            "symbol": "1",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 6357.0,
            "y": 98.43,
            "symbol": "JIFFPOM",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4223.0,
            "y": 97.73,
            "symbol": "viewer",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 3900.0,
            "y": 99.53,
            "symbol": "Supershiro",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 5199.0,
            "y": 78.01,
            "symbol": "APOLLO",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 4763.0,
            "y": 98.51,
            "symbol": "Noxi",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4310.0,
            "y": 97.25,
            "symbol": "obvious",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4155.0,
            "y": 97.49,
            "symbol": "BLUB",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 6797.0,
            "y": 86.75,
            "symbol": "FARTWORM",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 298579.0,
            "y": 44.58,
            "symbol": "gib",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 4417.0,
            "y": 99.17,
            "symbol": "BEANS",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4164.0,
            "y": 96.47,
            "symbol": "Streamless",
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
          "#22c55e",
          "#eab308",
          "#22c55e",
          "#22c55e",
          "#ef4444",
          "#eab308",
          "#f97316",
          "#f97316",
          "#22c55e",
          "#22c55e",
          "#ef4444",
          "#ef4444",
          "#ef4444",
          "#f97316",
          "#f97316",
          "#f97316",
          "#22c55e",
          "#22c55e",
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
          "#f97316",
          "#ef4444",
          "#ef4444",
          "#ef4444",
          "#f97316",
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

**Total Tokens**: 44
**Combined 24h Volume**: $511.58M
**Combined Liquidity**: $59.06M

**Concentration Risk Distribution**:
- 🔴 Extreme: 17 tokens
- 🟢 Low: 16 tokens
- 🟡 High: 7 tokens
- 🟢 Medium: 3 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $511.28M | $53.67M | 🟢 unknown |
| 2 | DREAM | Dreamsync | $88.75K | $181.82K | 🟢 low |
| 3 | AI4 | AI⁴ | $84.50K | $98.22K | 🟢 low |
| 4 | LION | Loaded Lions | $44.27K | $1.80M | 🟢 low |
| 5 | HAROLD | Harold | $20.41K | $489.95K | 🟢 medium |
| 6 | RAGEGUY | Rage Guy | $18.42K | $130.48K | 🟢 low |
| 7 | HOODIE | Hoodie | $17.22K | $1.52K | 🟢 low |
| 8 | 1nu | 1nu | $16.79K | $22.95K | 🟢 low |
| 9 | 1Bull | One bull run to change your li | $2.65K | $20.63K | 🟢 medium |
| 10 | FARTLESS | FARTLESS COIN | $2.32K | $3.69K | 🟢 low |

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
| wSOL | Wrapped SOL | 12 | $511.28M | $53.67M | 0.00% |
| DREAM | Dreamsync | 12 | $88.75K | $181.82K | 31.60% |

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
- 🚀 **Breakout**: 1 tokens

### 🚀 Breakout Signals

| Symbol | Score | Vol 3v1 | Z-Score Vol | Liq 3d | Streak |
|--------|-------|---------|-------------|--------|--------|
| wSOL | 56528.48 | 2.44x | 1.98 | $56.52M | 1d |

### 👀 Watch List

*2 tokens showing elevated activity*

📄 [Full data: signals_filtered.csv](data/signals_filtered.csv)

---

## 📈 Historical Data

**Total Historical Records**: 518
**Unique Tokens Tracked**: 102
**Date Range**: 2025-10-01 to 2025-10-13

**Master Aggregations**: 102 tokens
**Performance Metrics**: 518 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 518 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 102 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 518 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 44 |
| [new_viable.csv](data/new_viable.csv) | New tokens with potential | 2 |
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
