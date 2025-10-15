# 📊 Solana Radar - Daily Reports

**Last Updated**: 2025-10-15 21:46 UTC

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
          13,
          8,
          2,
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
| 1 | XBT | XBT | 21.99% | 🟢 low | $0.66 | $0.00 |
| 2 | ELIZABETH | Just Elizabeth Cat | 26.87% | 🟢 low | $9.44 | $54.12 |
| 3 | RAGEGUY | Rage Guy | 27.56% | 🟢 low | $14.92K | $123.90K |
| 4 | FLY | Nexa | 31.52% | 🟢 low | $316.67 | $2.38K |
| 5 | DREAM | Dreamsync | 31.62% | 🟢 low | $103.28K | $180.45K |
| 6 | FARTLESS | FARTLESS COIN | 33.81% | 🟢 low | $810.84 | $3.73K |
| 7 | 1nu | 1nu | 38.39% | 🟢 low | $77.95K | $37.83K |
| 8 | USDUT | unstable tether | 38.71% | 🟢 low | $5.09 | $52.77 |
| 9 | USEFUL | USEFUL COIN | 40.03% | 🟢 low | $0.90 | $67.74 |
| 10 | AI20X | Ai20x.ai | 41.41% | 🟢 low | $57.45 | $2.29M |

### ⚠️ Highest Risk Tokens (Highest Holder Concentration)

Top 10 tokens with the most concentrated ownership:

| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |
|------|--------|------|---------|------|------------|-----------|
| 1 | 4 | 4COIN | 100.00% | 🔴 extreme | $3.49 | $0.00 |
| 2 | 2 | TWO IS BETTER THAN ONE | 99.85% | 🔴 extreme | $0.32 | $0.00 |
| 3 | 1SOL | 1SOL | 99.78% | 🔴 extreme | $0.33 | $7.74K |
| 4 | MINDWORMS | mindworms | 99.71% | 🔴 extreme | $1.25 | $7.71K |
| 5 | KENNY | KENNY KO | 99.67% | 🔴 extreme | $0.22 | $7.62K |
| 6 | BEANS | BEANS | 99.17% | 🔴 extreme | $0.31 | $8.91K |
| 7 | GAZABOY | GAZA BOY | 99.07% | 🔴 extreme | $1.85 | $7.60K |
| 8 | 19 | Cult of 19 | 98.90% | 🔴 extreme | $0.26 | $7.85K |
| 9 | 1% Club | The 1% Club | 98.11% | 🔴 extreme | $308.44 | $6.77K |
| 10 | BULLCOIN | BULLCOIN | 97.17% | 🔴 extreme | $6.49 | $8.62K |

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
      "2025-10-15"
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
          47.45
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
          31.62
        ],
        "borderColor": "#22c55e",
        "backgroundColor": "#22c55e20",
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
          38.39
        ],
        "borderColor": "#eab308",
        "backgroundColor": "#eab30820",
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
      "1nu",
      "LION",
      "SHITTER",
      "RAGEGUY",
      "HAROLD",
      "7",
      "1"
    ],
    "datasets": [
      {
        "label": "24h Volume (USD)",
        "data": [
          436169889.18,
          144127.72,
          103284.86,
          77951.69,
          33353.98,
          22699.91,
          14919.58,
          7949.11,
          2247.17,
          2096.07
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
            "x": 322147.0,
            "y": 47.45,
            "symbol": "AI4",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 1761415.0,
            "y": 31.62,
            "symbol": "DREAM",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 85963.0,
            "y": 38.39,
            "symbol": "1nu",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 59449759.0,
            "y": 57.84,
            "symbol": "LION",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 34501.0,
            "y": 54.94,
            "symbol": "SHITTER",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 673031.0,
            "y": 27.56,
            "symbol": "RAGEGUY",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 2945072.0,
            "y": 62.91,
            "symbol": "HAROLD",
            "risk": "medium",
            "backgroundColor": "#eab308"
          },
          {
            "x": 6500.0,
            "y": 95.13,
            "symbol": "7",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 6798.0,
            "y": 92.61,
            "symbol": "1",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 6430.0,
            "y": 94.72,
            "symbol": "1",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 7497061.0,
            "y": 96.67,
            "symbol": "SOL",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 104618.0,
            "y": 52.62,
            "symbol": "RUECAT",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 819040.0,
            "y": 33.81,
            "symbol": "FARTLESS",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 25711.0,
            "y": 75.66,
            "symbol": "1Bull",
            "risk": "medium",
            "backgroundColor": "#eab308"
          },
          {
            "x": 16193.0,
            "y": 86.59,
            "symbol": "AUSBAGWORK",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 5478.0,
            "y": 88.86,
            "symbol": "RWA",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 16583.0,
            "y": 31.52,
            "symbol": "FLY",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 4148.0,
            "y": 98.11,
            "symbol": "1% Club",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 32564.0,
            "y": 57.12,
            "symbol": "$CrepSol",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 4713.0,
            "y": 79.96,
            "symbol": "APOLLO",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 19339910.0,
            "y": 41.41,
            "symbol": "AI20X",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 9642.0,
            "y": 88.99,
            "symbol": "DARE",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 7274.0,
            "y": 87.49,
            "symbol": "FARTWORM",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 11996.0,
            "y": 86.75,
            "symbol": "IDIOT",
            "risk": "high",
            "backgroundColor": "#f97316"
          },
          {
            "x": 1241386.0,
            "y": 26.87,
            "symbol": "ELIZABETH",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 5005.0,
            "y": 97.17,
            "symbol": "BULLCOIN",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 203179.0,
            "y": 38.71,
            "symbol": "USDUT",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 5415.98,
            "y": 100.0,
            "symbol": "4",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 3920.0,
            "y": 99.07,
            "symbol": "GAZABOY",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4065.0,
            "y": 99.71,
            "symbol": "MINDWORMS",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 176313.0,
            "y": 40.03,
            "symbol": "USEFUL",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 4563.0,
            "y": 96.85,
            "symbol": "Streamless",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 273358.0,
            "y": 46.18,
            "symbol": "gib",
            "risk": "low",
            "backgroundColor": "#22c55e"
          },
          {
            "x": 3896.0,
            "y": 99.78,
            "symbol": "1SOL",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 5555.96,
            "y": 99.85,
            "symbol": "2",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4580.0,
            "y": 99.17,
            "symbol": "BEANS",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4226.0,
            "y": 98.9,
            "symbol": "19",
            "risk": "extreme",
            "backgroundColor": "#ef4444"
          },
          {
            "x": 4028.0,
            "y": 99.67,
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
          "#eab308",
          "#ef4444",
          "#f97316",
          "#f97316",
          "#ef4444",
          "#22c55e",
          "#22c55e",
          "#eab308",
          "#f97316",
          "#f97316",
          "#22c55e",
          "#ef4444",
          "#22c55e",
          "#f97316",
          "#22c55e",
          "#f97316",
          "#f97316",
          "#f97316",
          "#22c55e",
          "#ef4444",
          "#22c55e",
          "#ef4444",
          "#ef4444",
          "#ef4444",
          "#22c55e",
          "#ef4444",
          "#22c55e",
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

**Total Tokens**: 40
**Combined 24h Volume**: $436.59M
**Combined Liquidity**: $61.70M

**Concentration Risk Distribution**:
- 🟢 Low: 16 tokens
- 🔴 Extreme: 13 tokens
- 🟡 High: 8 tokens
- 🟢 Medium: 2 tokens
- 🟢 Unknown: 1 tokens

### Top 10 by Volume

| # | Symbol | Name | Volume 24h | Liquidity | Risk |
|---|--------|------|------------|-----------|------|
| 1 | wSOL | Wrapped SOL | $436.17M | $56.48M | 🟢 unknown |
| 2 | AI4 | AI⁴ | $144.13K | $105.85K | 🟢 low |
| 3 | DREAM | Dreamsync | $103.28K | $180.45K | 🟢 low |
| 4 | 1nu | 1nu | $77.95K | $37.83K | 🟢 low |
| 5 | LION | Loaded Lions | $33.35K | $1.71M | 🟢 low |
| 6 | SHITTER | SHITTERCOIN | $22.70K | $25.10K | 🟢 low |
| 7 | RAGEGUY | Rage Guy | $14.92K | $123.90K | 🟢 low |
| 8 | HAROLD | Harold | $7.95K | $468.30K | 🟢 medium |
| 9 | 7 | 7 Coin | $2.25K | $9.87K | 🔴 extreme |
| 10 | 1 | 1 pill can change your life | $2.10K | $10.74K | 🟡 high |

📄 [Full data: daily_top50.csv](data/daily_top50.csv)

---

## 🌱 New Viable Tokens (7-14 Days Old)

New tokens showing potential with healthy metrics and lower concentration risk.

**Found**: 3 viable new tokens

**Criteria**:
- First seen 7-14 days ago
- Volume > $50K
- Liquidity > $100K
- Missing streak < 2 (stable presence)
- Concentration risk: low/medium

| Symbol | Name | Age (days) | Volume 24h | Liquidity | Top 10% |
|--------|------|------------|------------|-----------|---------|
| wSOL | Wrapped SOL | 14 | $436.17M | $56.48M | 0.00% |
| AI4 | AI⁴ | 14 | $144.13K | $105.85K | 47.45% |
| DREAM | Dreamsync | 14 | $103.28K | $180.45K | 31.62% |

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
- 🚀 **Breakout**: 1 tokens

### 🚀 Breakout Signals

| Symbol | Score | Vol 3v1 | Z-Score Vol | Liq 3d | Streak |
|--------|-------|---------|-------------|--------|--------|
| wSOL | 57464.59 | 2.69x | 1.57 | $57.45M | 1d |

### 👀 Watch List

*3 tokens showing elevated activity*

📄 [Full data: signals_filtered.csv](data/signals_filtered.csv)

---

## 📈 Historical Data

**Total Historical Records**: 514
**Unique Tokens Tracked**: 102
**Date Range**: 2025-10-01 to 2025-10-15

**Master Aggregations**: 102 tokens
**Performance Metrics**: 514 records

### Available Datasets

| File | Description | Records |
|------|-------------|---------|
| [history.csv](data/history.csv) | Complete historical snapshots | 514 |
| [master.csv](data/master.csv) | Aggregated per-token metrics | 102 |
| [performance.csv](data/performance.csv) | Rolling performance indicators | 514 |
| [daily_top50.csv](data/daily_top50.csv) | Today's top 50 tokens | 40 |
| [new_viable.csv](data/new_viable.csv) | New tokens with potential | 3 |
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
