# Solana Scalping Analysis Report
**Date:** 2025-10-13  
**Generated:** 18:44 UTC

---

## 🎯 Top Opportunities

```
======================================================================
🎯 SCALPING OPPORTUNITIES - TODAY
======================================================================

✅ Loaded 29 snapshots (959 datapoints)
Traceback (most recent call last):
  File "/home/runner/work/solana/solana/analyze.py", line 301, in <module>
    main()
  File "/home/runner/work/solana/solana/analyze.py", line 291, in main
    analyze_opportunities(args)
  File "/home/runner/work/solana/solana/analyze.py", line 28, in analyze_opportunities
    opportunities = analyzer.get_top_opportunities(date=args.date, top_n=args.top)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/solana/solana/utils/intraday_analyzer.py", line 337, in get_top_opportunities
    token_data = self.generate_signals(token_data)  # Keep legacy signals for comparison
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/solana/solana/utils/intraday_analyzer.py", line 253, in generate_signals
    if self.debug:
       ^^^^^^^^^^
AttributeError: 'IntradayAnalyzer' object has no attribute 'debug'
```

![Top Opportunities](../charts/opportunities_2025-10-13.png)


---

## 📋 Watchlist Performance

```
======================================================================
📋 WATCHLIST PERFORMANCE - TODAY
======================================================================

✅ Loaded 29 snapshots (959 datapoints)
📊 49 watchlist tokens tracked today:

🟢 TOP GAINERS
  EDG      +350.66% @ $0.00004128
  POORLESS +315.70% @ $0.00009848
  PEACEMAK +155.37% @ $0.00039940
  ADELOS   +127.82% @ $0.00087870
  CAPRA    +98.60% @ $0.00005547

🔴 TOP LOSERS
  BARNEY   -65.10% @ $0.00002089
  MSGA     -82.47% @ $0.00001278
  MANIFEST -85.93% @ $0.00001238
  TRENCHER -92.95% @ $0.00000528
  AI6900   -94.11% @ $0.00001685

📈 STATS
  Average Change: +11.53%
  Median Change: +2.22%
  Gainers: 28
  Losers: 20

======================================================================
```

### Correlation Heatmap

![Watchlist Correlation](../charts/watchlist_correlation_2025-10-13.png)

---

## 🔬 Backtesting Results (7-day)

```
======================================================================
🔬 BACKTESTING WATCHLIST (7 days)
======================================================================

🔄 Backtesting 50 watchlist tokens...
  [1/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [2/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [3/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [4/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [5/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [6/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [7/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [8/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [9/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [10/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [11/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [12/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [13/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [14/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [15/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [16/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [17/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [18/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [19/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [20/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [21/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [22/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [23/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [24/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [25/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [26/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [27/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [28/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [29/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [30/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [31/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [32/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [33/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [34/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [35/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [36/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [37/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [38/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [39/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [40/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [41/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [42/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [43/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [44/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [45/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [46/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [47/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [48/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [49/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11
  [50/50] Testing...✅ Loaded 29 snapshots (959 datapoints)
✅ Loaded 47 snapshots (493 datapoints)
✅ Loaded 14 snapshots (25 datapoints)
❌ No data for 2025-10-10
❌ No data for 2025-10-09
❌ No data for 2025-10-08
❌ No data for 2025-10-07
✅ Loaded 3 days of data: 2025-10-13 to 2025-10-11

❌ No backtest results
❌ No results
```


---

## 📊 How to Use

### Signal Interpretation
- 🟢 **BUY**: High volatility + positive momentum + volume surge
- 🔴 **SELL**: Momentum reversal or volume decline
- 🟡 **HOLD**: Low volatility or neutral conditions

### Signal Strength
- **0-2**: Weak signal, high risk
- **2-3**: Moderate signal, medium risk
- **3-4**: Strong signal, lower risk
- **4-5**: Very strong signal, best opportunities

### Opportunity Score
Composite score based on:
- Volatility (30%)
- Momentum (30%)
- Volume (20%)
- Signal strength (20%)
- Watchlist bonus (+20 if tracked)

### Recommendations
1. Focus on watchlist tokens (📌) - more reliable data
2. Look for signal strength ≥3.0
3. Confirm with volume momentum
4. Check support/resistance levels before entry

---

**Next Update:** In 30 minutes  
**Data Source:** [Intraday Snapshots](https://github.com/stelios5791/sol-reports/tree/main/intraday)
