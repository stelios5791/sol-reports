#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enhanced Dashboard Generator for sol-reports
Generates README.md with:
  - Interactive Chart.js visualizations
  - Daily Top 50 overview
  - New Viable Tokens (7-14 day old with potential)
  - Whale-filtered Signals
  - Historical stats and charts
"""

from pathlib import Path
from datetime import datetime
import pandas as pd
import json

DATA_DIR = Path("data")

def safe_read_csv(filename: str) -> pd.DataFrame:
    """Safely read CSV, return empty DataFrame if not found"""
    path = DATA_DIR / filename
    try:
        if path.exists():
            df = pd.read_csv(path)
            print(f"✅ Loaded {filename}: {len(df)} rows")
            return df
        else:
            print(f"⚠️  {filename} not found")
            return pd.DataFrame()
    except Exception as e:
        print(f"❌ Error loading {filename}: {e}")
        return pd.DataFrame()

def format_usd(value):
    """Format USD value with K/M/B suffixes"""
    try:
        v = float(value)
        if v >= 1_000_000_000:
            return f"${v/1_000_000_000:.2f}B"
        elif v >= 1_000_000:
            return f"${v/1_000_000:.2f}M"
        elif v >= 1_000:
            return f"${v/1_000:.2f}K"
        else:
            return f"${v:.2f}"
    except:
        return "N/A"

def format_pct(value):
    """Format percentage"""
    try:
        return f"{float(value):.2f}%"
    except:
        return "N/A"

def create_chart_script(chart_id: str, chart_config: dict) -> str:
    """Create a Chart.js script block"""
    config_json = json.dumps(chart_config, indent=2)
    return f"""
<div style="max-width: 900px; margin: 20px auto;">
  <canvas id="{chart_id}"></canvas>
</div>
<script>
(function() {{
  const ctx = document.getElementById('{chart_id}');
  if (!ctx) return;
  new Chart(ctx, {config_json});
}})();
</script>
"""

def generate_risk_distribution_chart(history: pd.DataFrame) -> str:
    """Generate risk distribution pie chart"""
    if history.empty or 'concentration_risk' not in history.columns:
        return ""
    
    latest = history[history['date'] == history['date'].max()]
    risk_counts = latest['concentration_risk'].value_counts()
    
    chart_config = {
        'type': 'pie',
        'data': {
            'labels': ['Extreme Risk', 'High Risk', 'Medium Risk', 'Low Risk', 'Unknown'],
            'datasets': [{
                'data': [
                    int(risk_counts.get('extreme', 0)),
                    int(risk_counts.get('high', 0)),
                    int(risk_counts.get('medium', 0)),
                    int(risk_counts.get('low', 0)),
                    int(risk_counts.get('unknown', 0))
                ],
                'backgroundColor': ['#ef4444', '#f97316', '#eab308', '#22c55e', '#94a3b8']
            }]
        },
        'options': {
            'responsive': True,
            'plugins': {
                'legend': {'position': 'bottom'},
                'title': {'display': True, 'text': 'Token Concentration Risk Distribution'}
            }
        }
    }
    
    return create_chart_script('riskPieChart', chart_config)

def generate_concentration_trends_chart(history: pd.DataFrame) -> str:
    """Generate concentration trends line chart for top tokens"""
    if history.empty:
        return ""
    
    # Get top 5 tokens by latest volume
    latest = history[history['date'] == history['date'].max()]
    if 'volume_24h_usd' not in latest.columns:
        return ""
    
    top_tokens = latest.nlargest(5, 'volume_24h_usd')['symbol'].tolist()
    
    # Get historical data for these tokens
    history['date'] = pd.to_datetime(history['date'])
    history_sorted = history.sort_values('date')
    
    datasets = []
    colors = ['#3b82f6', '#ef4444', '#22c55e', '#eab308', '#8b5cf6']
    
    all_dates = []
    for i, symbol in enumerate(top_tokens):
        token_data = history_sorted[history_sorted['symbol'] == symbol]
        if not token_data.empty and 'top_10_holders_pct' in token_data.columns:
            dates = token_data['date'].dt.strftime('%Y-%m-%d').tolist()
            concentrations = token_data['top_10_holders_pct'].fillna(0).tolist()
            
            if not all_dates:
                all_dates = dates
            
            datasets.append({
                'label': symbol,
                'data': concentrations,
                'borderColor': colors[i % len(colors)],
                'backgroundColor': colors[i % len(colors)] + '20',
                'tension': 0.1,
                'fill': False
            })
    
    if not datasets:
        return ""
    
    chart_config = {
        'type': 'line',
        'data': {
            'labels': all_dates,
            'datasets': datasets
        },
        'options': {
            'responsive': True,
            'plugins': {
                'legend': {'position': 'top'},
                'title': {'display': True, 'text': 'Top 10 Holder Concentration Over Time'}
            },
            'scales': {
                'y': {
                    'beginAtZero': True,
                    'max': 100,
                    'title': {'display': True, 'text': 'Concentration (%)'}
                },
                'x': {
                    'title': {'display': True, 'text': 'Date'}
                }
            }
        }
    }
    
    return create_chart_script('trendLineChart', chart_config)

def generate_volume_leaders_chart(daily: pd.DataFrame) -> str:
    """Generate volume leaders bar chart"""
    if daily.empty or 'volume_24h_usd' not in daily.columns:
        return ""
    
    top10 = daily.nlargest(10, 'volume_24h_usd')
    
    # Color-code by risk
    colors = []
    for risk in top10.get('concentration_risk', ['unknown'] * len(top10)):
        if risk == 'low':
            colors.append('#22c55e')
        elif risk == 'medium':
            colors.append('#eab308')
        elif risk == 'high':
            colors.append('#f97316')
        elif risk == 'extreme':
            colors.append('#ef4444')
        else:
            colors.append('#94a3b8')
    
    chart_config = {
        'type': 'bar',
        'data': {
            'labels': top10['symbol'].tolist(),
            'datasets': [{
                'label': '24h Volume (USD)',
                'data': top10['volume_24h_usd'].tolist(),
                'backgroundColor': colors
            }]
        },
        'options': {
            'responsive': True,
            'plugins': {
                'legend': {'display': False},
                'title': {'display': True, 'text': 'Top 10 Tokens by 24h Volume'}
            },
            'scales': {
                'y': {
                    'beginAtZero': True,
                    'title': {'display': True, 'text': 'Volume (USD)'}
                }
            }
        }
    }
    
    return create_chart_script('volumeBarChart', chart_config)

def generate_scatter_chart(history: pd.DataFrame) -> str:
    """Generate FDV vs Concentration scatter plot"""
    if history.empty:
        return ""
    
    latest = history[history['date'] == history['date'].max()].copy()
    
    # Filter valid data
    valid = latest[
        (latest['fdv_usd'] > 0) & 
        (latest['top_10_holders_pct'] > 0) &
        (latest['concentration_risk'] != 'unknown')
    ].copy()
    
    if valid.empty:
        return ""
    
    # Create scatter data with colors
    scatter_data = []
    risk_colors = {
        'extreme': '#ef4444',
        'high': '#f97316',
        'medium': '#eab308',
        'low': '#22c55e'
    }
    
    for _, row in valid.iterrows():
        scatter_data.append({
            'x': float(row['fdv_usd']),
            'y': float(row['top_10_holders_pct']),
            'symbol': row['symbol'],
            'risk': row['concentration_risk'],
            'backgroundColor': risk_colors.get(row['concentration_risk'], '#94a3b8')
        })
    
    chart_config = {
        'type': 'scatter',
        'data': {
            'datasets': [{
                'label': 'Tokens',
                'data': scatter_data,
                'backgroundColor': [d['backgroundColor'] for d in scatter_data]
            }]
        },
        'options': {
            'responsive': True,
            'plugins': {
                'legend': {'display': False},
                'title': {'display': True, 'text': 'Market Cap (FDV) vs Holder Concentration'},
                'tooltip': {
                    'callbacks': {
                        'label': 'function(context) { const d = context.raw; return d.symbol + ": $" + d.x.toLocaleString() + " FDV, " + d.y.toFixed(1) + "% concentration (" + d.risk + " risk)"; }'
                    }
                }
            },
            'scales': {
                'x': {
                    'type': 'logarithmic',
                    'title': {'display': True, 'text': 'FDV (USD) - Log Scale'}
                },
                'y': {
                    'beginAtZero': True,
                    'max': 100,
                    'title': {'display': True, 'text': 'Top 10 Holder %'}
                }
            }
        }
    }
    
    return create_chart_script('scatterChart', chart_config)

def generate_leaderboards(history: pd.DataFrame) -> tuple:
    """Generate safest and riskiest token leaderboards"""
    if history.empty:
        return "", ""
    
    latest = history[history['date'] == history['date'].max()].copy()
    known = latest[latest['concentration_risk'] != 'unknown'].copy()
    
    if known.empty:
        return "", ""
    
    # Safest tokens (lowest concentration)
    safest = known.nsmallest(10, 'top_10_holders_pct')
    safest_lines = []
    safest_lines.append("### 🏆 Safest Tokens (Lowest Holder Concentration)")
    safest_lines.append("")
    safest_lines.append("Top 10 tokens with the most distributed ownership:")
    safest_lines.append("")
    safest_lines.append("| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |")
    safest_lines.append("|------|--------|------|---------|------|------------|-----------|")
    
    for i, row in enumerate(safest.itertuples(), 1):
        symbol = getattr(row, 'symbol', '???')
        name = getattr(row, 'name', '???')[:25]
        top10 = format_pct(getattr(row, 'top_10_holders_pct', 0))
        risk = getattr(row, 'concentration_risk', 'unknown')
        risk_emoji = '🟢' if risk == 'low' else '🟡' if risk == 'medium' else '🟠' if risk == 'high' else '🔴'
        vol = format_usd(getattr(row, 'volume_24h_usd', 0))
        liq = format_usd(getattr(row, 'liquidity_usd', 0))
        
        safest_lines.append(f"| {i} | {symbol} | {name} | {top10} | {risk_emoji} {risk} | {vol} | {liq} |")
    
    safest_lines.append("")
    
    # Riskiest tokens (highest concentration)
    riskiest = known.nlargest(10, 'top_10_holders_pct')
    riskiest_lines = []
    riskiest_lines.append("### ⚠️ Highest Risk Tokens (Highest Holder Concentration)")
    riskiest_lines.append("")
    riskiest_lines.append("Top 10 tokens with the most concentrated ownership:")
    riskiest_lines.append("")
    riskiest_lines.append("| Rank | Symbol | Name | Top 10% | Risk | Volume 24h | Liquidity |")
    riskiest_lines.append("|------|--------|------|---------|------|------------|-----------|")
    
    for i, row in enumerate(riskiest.itertuples(), 1):
        symbol = getattr(row, 'symbol', '???')
        name = getattr(row, 'name', '???')[:25]
        top10 = format_pct(getattr(row, 'top_10_holders_pct', 0))
        risk = getattr(row, 'concentration_risk', 'unknown')
        risk_emoji = '🟢' if risk == 'low' else '🟡' if risk == 'medium' else '🟠' if risk == 'high' else '🔴'
        vol = format_usd(getattr(row, 'volume_24h_usd', 0))
        liq = format_usd(getattr(row, 'liquidity_usd', 0))
        
        riskiest_lines.append(f"| {i} | {symbol} | {name} | {top10} | {risk_emoji} {risk} | {vol} | {liq} |")
    
    riskiest_lines.append("")
    
    return "\n".join(safest_lines), "\n".join(riskiest_lines)

def generate_markdown():
    """Generate the README.md content"""
    
    lines = []
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    
    # Header
    lines.append("# 📊 Solana Radar - Daily Reports")
    lines.append("")
    lines.append(f"**Last Updated**: {now}")
    lines.append("")
    lines.append("Automated daily analysis of Solana tokens with whale tracking and momentum indicators.")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Load all data
    daily = safe_read_csv("daily_top50.csv")
    history = safe_read_csv("history.csv")
    viable = safe_read_csv("new_viable.csv")
    movers = safe_read_csv("top_movers.csv")
    signals = safe_read_csv("signals_filtered.csv")
    master = safe_read_csv("master.csv")
    performance = safe_read_csv("performance.csv")
    
    # === NEW SECTION: Interactive Dashboard ===
    lines.append("## 📈 Interactive Dashboard")
    lines.append("")
    lines.append('<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>')
    lines.append("")
    
    # Risk Distribution Pie Chart
    lines.append("### 🥧 Risk Distribution")
    lines.append("")
    lines.append("Current distribution of concentration risk across all tracked tokens:")
    lines.append("")
    risk_chart = generate_risk_distribution_chart(history)
    if risk_chart:
        lines.append(risk_chart)
    else:
        lines.append("*Chart unavailable - insufficient data*")
    lines.append("")
    
    # Leaderboards
    safest_table, riskiest_table = generate_leaderboards(history)
    if safest_table:
        lines.append(safest_table)
    if riskiest_table:
        lines.append(riskiest_table)
    
    # Concentration Trends
    lines.append("### 📈 Concentration Trends")
    lines.append("")
    lines.append("Historical holder concentration for top volume tokens:")
    lines.append("")
    trend_chart = generate_concentration_trends_chart(history)
    if trend_chart:
        lines.append(trend_chart)
    else:
        lines.append("*Chart unavailable - insufficient historical data*")
    lines.append("")
    
    # Volume Leaders
    lines.append("### 📊 Volume Leaders")
    lines.append("")
    lines.append("Top tokens by 24h trading volume (color-coded by risk):")
    lines.append("")
    volume_chart = generate_volume_leaders_chart(daily)
    if volume_chart:
        lines.append(volume_chart)
    else:
        lines.append("*Chart unavailable - no volume data*")
    lines.append("")
    
    # Scatter Plot
    lines.append("### 💰 Market Cap vs Concentration")
    lines.append("")
    lines.append("Relationship between token valuation (FDV) and holder concentration:")
    lines.append("")
    scatter_chart = generate_scatter_chart(history)
    if scatter_chart:
        lines.append(scatter_chart)
    else:
        lines.append("*Chart unavailable - insufficient data*")
    lines.append("")
    
    lines.append("---")
    lines.append("")
    
    # === Section 1: Daily Top 50 ===
    lines.append("## 🔥 Today's Top 50 Tokens")
    lines.append("")
    
    if not daily.empty:
        # Summary stats
        total_vol = daily["volume_24h_usd"].sum() if "volume_24h_usd" in daily.columns else 0
        total_liq = daily["liquidity_usd"].sum() if "liquidity_usd" in daily.columns else 0
        
        lines.append(f"**Total Tokens**: {len(daily)}")
        lines.append(f"**Combined 24h Volume**: {format_usd(total_vol)}")
        lines.append(f"**Combined Liquidity**: {format_usd(total_liq)}")
        lines.append("")
        
        # Risk distribution
        if "concentration_risk" in daily.columns:
            risk_counts = daily["concentration_risk"].value_counts()
            lines.append("**Concentration Risk Distribution**:")
            for risk, count in risk_counts.items():
                emoji = "🔴" if risk == "extreme" else "🟡" if risk == "high" else "🟢"
                lines.append(f"- {emoji} {risk.title()}: {count} tokens")
            lines.append("")
        
        # Top 10 by volume
        lines.append("### Top 10 by Volume")
        lines.append("")
        lines.append("| # | Symbol | Name | Volume 24h | Liquidity | Risk |")
        lines.append("|---|--------|------|------------|-----------|------|")
        
        top10 = daily.head(10)
        for idx, row in enumerate(top10.itertuples(), 1):
            symbol = getattr(row, "symbol", "???")
            name = getattr(row, "name", "???")[:30]
            vol = format_usd(getattr(row, "volume_24h_usd", 0))
            liq = format_usd(getattr(row, "liquidity_usd", 0))
            risk = getattr(row, "concentration_risk", "unknown")
            risk_emoji = "🔴" if risk == "extreme" else "🟡" if risk == "high" else "🟢"
            
            lines.append(f"| {idx} | {symbol} | {name} | {vol} | {liq} | {risk_emoji} {risk} |")
        
        lines.append("")
        lines.append(f"📄 [Full data: daily_top50.csv](data/daily_top50.csv)")
    else:
        lines.append("*No data available for today*")
    
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # === Section 2: New Viable Tokens ===
    lines.append("## 🌱 New Viable Tokens (7-14 Days Old)")
    lines.append("")
    lines.append("New tokens showing potential with healthy metrics and lower concentration risk.")
    lines.append("")
    
    if not viable.empty:
        lines.append(f"**Found**: {len(viable)} viable new tokens")
        lines.append("")
        
        lines.append("**Criteria**:")
        lines.append("- First seen 7-14 days ago")
        lines.append("- Volume > $50K")
        lines.append("- Liquidity > $100K")
        lines.append("- Missing streak < 2 (stable presence)")
        lines.append("- Concentration risk: low/medium")
        lines.append("")
        
        lines.append("| Symbol | Name | Age (days) | Volume 24h | Liquidity | Top 10% |")
        lines.append("|--------|------|------------|------------|-----------|---------|")
        
        for row in viable.head(15).itertuples():
            symbol = getattr(row, "symbol", "???")
            name = getattr(row, "name", "???")[:25]
            age = getattr(row, "days_since_first_seen", "?")
            vol = format_usd(getattr(row, "volume_24h_usd", 0))
            liq = format_usd(getattr(row, "liquidity_usd", 0))
            top10 = format_pct(getattr(row, "top_10_holders_pct", 0)) if hasattr(row, "top_10_holders_pct") else "N/A"
            
            lines.append(f"| {symbol} | {name} | {age} | {vol} | {liq} | {top10} |")
        
        lines.append("")
        lines.append(f"📄 [Full data: new_viable.csv](data/new_viable.csv)")
    else:
        lines.append("*No viable new tokens found with current criteria*")
    
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # === Section 3: Top Movers ===
    lines.append("## 📈 Top Movers (24h Change)")
    lines.append("")
    lines.append("Tokens with significant price or volume changes in the last 24 hours.")
    lines.append("")
    
    if not movers.empty:
        gainers = movers[movers["category"].str.contains("gainer", na=False)]
        losers = movers[movers["category"].str.contains("loser", na=False)]
        spikes = movers[movers["category"].str.contains("volume_spike", na=False)]
        
        lines.append(f"**Total Movers**: {len(movers)}")
        lines.append(f"- 🚀 **Gainers** (>+20%): {len(gainers)}")
        lines.append(f"- 📉 **Losers** (<-20%): {len(losers)}")
        lines.append(f"- 📊 **Volume Spikes** (>+100%): {len(spikes)}")
        lines.append("")
        
        if not gainers.empty:
            lines.append("### 🚀 Top Gainers")
            lines.append("")
            lines.append("| # | Symbol | Name | Change 24h | Current Price | Volume Change | Risk |")
            lines.append("|---|--------|------|------------|---------------|---------------|------|")
            
            top_gainers = gainers.head(10)
            for row in top_gainers.itertuples():
                rank = getattr(row, "rank", "?")
                symbol = getattr(row, "symbol", "???")
                name = getattr(row, "name", "???")[:25]
                price_chg = f"+{getattr(row, 'price_change_24h_pct', 0):.2f}%"
                price = format_usd(getattr(row, "current_price", 0))
                vol_chg = f"+{getattr(row, 'volume_change_24h_pct', 0):.1f}%" if getattr(row, "volume_change_24h_pct", 0) > 0 else f"{getattr(row, 'volume_change_24h_pct', 0):.1f}%"
                risk = getattr(row, "concentration_risk", "unknown")
                risk_emoji = "🔴" if risk == "extreme" else "🟡" if risk == "high" else "🟢"
                
                lines.append(f"| {rank} | {symbol} | {name} | {price_chg} | {price} | {vol_chg} | {risk_emoji} |")
            
            lines.append("")
        
        lines.append(f"📄 [Full data: top_movers.csv](data/top_movers.csv)")
    else:
        lines.append("*No significant movers in the last 24 hours*")
    
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # === Section 4: Whale-Filtered Signals ===
    lines.append("## 🎯 Trading Signals (Whale Filtered)")
    lines.append("")
    lines.append("Signals filtered to exclude tokens with extreme concentration risk.")
    lines.append("")
    
    if not signals.empty:
        if "signal" in signals.columns:
            signal_counts = signals["signal"].value_counts()
            lines.append("**Signal Distribution**:")
            for sig, count in signal_counts.items():
                emoji = "🚀" if sig == "Breakout" else "👀" if sig == "Watch" else "❄️"
                lines.append(f"- {emoji} **{sig}**: {count} tokens")
            lines.append("")
        
        breakouts = signals[signals["signal"] == "Breakout"] if "signal" in signals.columns else pd.DataFrame()
        if not breakouts.empty:
            lines.append("### 🚀 Breakout Signals")
            lines.append("")
            lines.append("| Symbol | Score | Vol 3v1 | Z-Score Vol | Liq 3d | Streak |")
            lines.append("|--------|-------|---------|-------------|--------|--------|")
            
            for row in breakouts.head(10).itertuples():
                symbol = getattr(row, "symbol", "???")
                score = f"{getattr(row, 'score', 0):.2f}"
                vol_mom = f"{getattr(row, 'vol_mom_3v1', 0):.2f}x"
                zscore = f"{getattr(row, 'zscore_vol_10d', 0):.2f}"
                liq = format_usd(getattr(row, "liq_3d", 0))
                streak = getattr(row, "current_streak_days", 0)
                
                lines.append(f"| {symbol} | {score} | {vol_mom} | {zscore} | {liq} | {streak}d |")
            
            lines.append("")
        
        watch = signals[signals["signal"] == "Watch"] if "signal" in signals.columns else pd.DataFrame()
        if not watch.empty:
            lines.append("### 👀 Watch List")
            lines.append("")
            lines.append(f"*{len(watch)} tokens showing elevated activity*")
            lines.append("")
        
        lines.append(f"📄 [Full data: signals_filtered.csv](data/signals_filtered.csv)")
    else:
        lines.append("*No signals available (all filtered or no data)*")
    
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # === Section 5: Historical Data ===
    lines.append("## 📈 Historical Data")
    lines.append("")
    
    if not history.empty:
        lines.append(f"**Total Historical Records**: {len(history):,}")
        
        if "address" in history.columns:
            unique_tokens = history["address"].nunique()
            lines.append(f"**Unique Tokens Tracked**: {unique_tokens:,}")
        
        if "date" in history.columns:
            history["date"] = pd.to_datetime(history["date"], errors="coerce")
            date_range = f"{history['date'].min().date()} to {history['date'].max().date()}"
            lines.append(f"**Date Range**: {date_range}")
    
    lines.append("")
    
    if not master.empty:
        lines.append(f"**Master Aggregations**: {len(master)} tokens")
    
    if not performance.empty:
        lines.append(f"**Performance Metrics**: {len(performance)} records")
    
    lines.append("")
    lines.append("### Available Datasets")
    lines.append("")
    lines.append("| File | Description | Records |")
    lines.append("|------|-------------|---------|")
    
    datasets = [
        ("history.csv", "Complete historical snapshots", len(history)),
        ("master.csv", "Aggregated per-token metrics", len(master)),
        ("performance.csv", "Rolling performance indicators", len(performance)),
        ("daily_top50.csv", "Today's top 50 tokens", len(daily)),
        ("new_viable.csv", "New tokens with potential", len(viable)),
        ("signals_filtered.csv", "Whale-filtered trading signals", len(signals)),
    ]
    
    for filename, desc, count in datasets:
        lines.append(f"| [{filename}](data/{filename}) | {desc} | {count:,} |")
    
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # === Section 6: Data Schema ===
    lines.append("## 📋 Data Schema")
    lines.append("")
    lines.append("### Key Columns")
    lines.append("")
    lines.append("**Market Data**:")
    lines.append("- `price_usd`: Current token price")
    lines.append("- `volume_24h_usd`: 24-hour trading volume")
    lines.append("- `liquidity_usd`: Total liquidity")
    lines.append("- `fdv_usd`: Fully diluted valuation")
    lines.append("")
    lines.append("**Whale Metrics (Holder Concentration)**:")
    lines.append("- `top_10_holders_pct`: % held by top 10 wallets")
    lines.append("- `top_5_holders_pct`: % held by top 5 wallets")
    lines.append("- `holder_concentration`: Rating (critical/high/medium/low)")
    lines.append("- `concentration_risk`: Risk level (extreme/high/medium/low)")
    lines.append("")
    lines.append("**Performance Indicators**:")
    lines.append("- `vol_mom_3v1`: 3-day vs 1-day volume momentum")
    lines.append("- `zscore_vol_10d`: 10-day volume z-score")
    lines.append("- `presence_7d`/`presence_30d`: Days seen in period")
    lines.append("- `current_streak_days`: Consecutive days with data")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # === Footer ===
    lines.append("## 🔗 Links")
    lines.append("")
    lines.append("- **Data Repository**: [stelios5791/sol-reports](https://github.com/stelios5791/sol-reports)")
    lines.append("- **Analysis Pipeline**: Private repository (automated daily)")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*Generated automatically by Solana Radar pipeline*")
    lines.append("")
    
    return "\n".join(lines)

def main():
    """Generate and save the dashboard"""
    print("=" * 60)
    print("Generating Enhanced Dashboard with Interactive Charts")
    print("=" * 60)
    print("")
    
    # Verify data directory exists
    if not DATA_DIR.exists():
        print(f"❌ ERROR: {DATA_DIR} directory not found!")
        return 1
    
    # Generate markdown
    try:
        markdown = generate_markdown()
        
        # Write to README.md
        readme_path = Path("README.md")
        readme_path.write_text(markdown, encoding="utf-8")
        
        print("")
        print("=" * 60)
        print(f"✅ Dashboard generated: {readme_path}")
        print(f"   Size: {len(markdown):,} characters")
        print("=" * 60)
        
        return 0
        
    except Exception as e:
        print(f"❌ Error generating dashboard: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
