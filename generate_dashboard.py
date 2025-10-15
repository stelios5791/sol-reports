#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enhanced Dashboard Generator v2.0 for sol-reports
Fixes:
  - Missing canvas tags for Chart.js
  - Tooltip function issues
  - wSOL filtering in charts
  
New Features:
  - Pattern detection dashboard
  - Performance metrics
  - Better mobile support
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

def create_chart_block(chart_id: str, chart_config: dict, width: str = "900px") -> str:
    """
    Create a Chart.js block with canvas and script
    FIXED: Now includes canvas tag!
    """
    config_json = json.dumps(chart_config, indent=2)
    
    return f"""
    <canvas id="{chart_id}"></canvas>
<div style="max-width: {width}; margin: 20px auto;">
  <canvas id="{chart_id}"></canvas>
</div>
<script>
(function() {{
  const ctx = document.getElementById('{chart_id}');
  if (!ctx) {{
    console.error('Canvas {chart_id} not found');
    return;
  }}
  try {{
    new Chart(ctx, {config_json});
  }} catch(e) {{
    console.error('Chart {chart_id} failed:', e);
  }}
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
            'labels': ['Low Risk', 'Medium Risk', 'High Risk', 'Extreme Risk', 'Unknown'],
            'datasets': [{
                'data': [
                    int(risk_counts.get('low', 0)),
                    int(risk_counts.get('medium', 0)),
                    int(risk_counts.get('high', 0)),
                    int(risk_counts.get('extreme', 0)),
                    int(risk_counts.get('unknown', 0))
                ],
                'backgroundColor': ['#22c55e', '#eab308', '#f97316', '#ef4444', '#94a3b8']
            }]
        },
        'options': {
            'responsive': True,
            'plugins': {
                'legend': {'position': 'bottom'},
                'title': {'display': True, 'text': 'Token Concentration Risk Distribution', 'font': {'size': 16}}
            }
        }
    }
    
    return create_chart_block('riskPieChart', chart_config)

def generate_concentration_trends_chart(history: pd.DataFrame) -> str:
    """Generate concentration trends line chart for top tokens"""
    if history.empty:
        return ""
    
    # Get top 5 tokens by latest volume (EXCLUDE wSOL)
    latest = history[history['date'] == history['date'].max()]
    if 'volume_24h_usd' not in latest.columns:
        return ""
    
    # Filter out wSOL and stablecoins
    filtered = latest[~latest['symbol'].isin(['wSOL', 'USDC', 'USDT'])]
    top_tokens = filtered.nlargest(5, 'volume_24h_usd')['symbol'].tolist()
    
    if not top_tokens:
        return ""
    
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
                'tension': 0.3,
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
                'title': {'display': True, 'text': 'Top 10 Holder Concentration Over Time', 'font': {'size': 16}}
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
    
    return create_chart_block('trendLineChart', chart_config)

def generate_volume_leaders_chart(daily: pd.DataFrame) -> str:
    """Generate volume leaders bar chart (EXCLUDE wSOL)"""
    if daily.empty or 'volume_24h_usd' not in daily.columns:
        return ""
    
    # Filter out wSOL and stablecoins
    filtered = daily[~daily['symbol'].isin(['wSOL', 'USDC', 'USDT'])]
    top10 = filtered.nlargest(10, 'volume_24h_usd')
    
    if top10.empty:
        return ""
    
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
                'title': {'display': True, 'text': 'Top 10 Tokens by 24h Volume (excl. wSOL)', 'font': {'size': 16}}
            },
            'scales': {
                'y': {
                    'beginAtZero': True,
                    'title': {'display': True, 'text': 'Volume (USD)'}
                }
            }
        }
    }
    
    return create_chart_block('volumeBarChart', chart_config)

def generate_scatter_chart(history: pd.DataFrame) -> str:
    """Generate FDV vs Concentration scatter plot (FIXED tooltips)"""
    if history.empty:
        return ""
    
    latest = history[history['date'] == history['date'].max()].copy()
    
    # Filter valid data and exclude wSOL
    valid = latest[
        (latest['fdv_usd'] > 0) & 
        (latest['top_10_holders_pct'] > 0) &
        (latest['concentration_risk'] != 'unknown') &
        (~latest['symbol'].isin(['wSOL', 'USDC', 'USDT']))
    ].copy()
    
    if valid.empty:
        return ""
    
    # Create scatter data with colors
    scatter_data = []
    risk_colors = {
        'low': '#22c55e',
        'medium': '#eab308',
        'high': '#f97316',
        'extreme': '#ef4444'
    }
    
    for _, row in valid.iterrows():
        scatter_data.append({
            'x': float(row['fdv_usd']),
            'y': float(row['top_10_holders_pct']),
            'r': 8,  # Point radius
            'label': f"{row['symbol']}: ${row['fdv_usd']:,.0f} FDV, {row['top_10_holders_pct']:.1f}% concentration ({row['concentration_risk']} risk)"
        })
    
    # Group by risk for better legend
    datasets = []
    for risk, color in risk_colors.items():
        risk_data = [d for d in scatter_data if risk in d['label']]
        if risk_data:
            datasets.append({
                'label': f'{risk.title()} Risk',
                'data': risk_data,
                'backgroundColor': color,
                'borderColor': color,
                'borderWidth': 1
            })
    
    chart_config = {
        'type': 'scatter',
        'data': {'datasets': datasets},
        'options': {
            'responsive': True,
            'plugins': {
                'legend': {'position': 'top'},
                'title': {'display': True, 'text': 'Market Cap (FDV) vs Holder Concentration', 'font': {'size': 16}},
                'tooltip': {
                    'callbacks': {}  # Will use default label
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
    
    return create_chart_block('scatterChart', chart_config)

def generate_performance_chart(history: pd.DataFrame) -> str:
    """
    NEW: Generate 7-day performance chart
    Shows price change % for top tokens
    """
    if history.empty or 'price_usd' not in history.columns:
        return ""
    
    history['date'] = pd.to_datetime(history['date'])
    latest_date = history['date'].max()
    week_ago = latest_date - pd.Timedelta(days=7)
    
    # Get tokens with data from both periods
    recent = history[history['date'] >= week_ago].copy()
    
    if recent.empty:
        return ""
    
    # Calculate 7d change for each token
    perf_data = []
    for symbol in recent['symbol'].unique():
        if symbol in ['wSOL', 'USDC', 'USDT']:
            continue
            
        token_data = recent[recent['symbol'] == symbol].sort_values('date')
        if len(token_data) < 2:
            continue
        
        first_price = token_data.iloc[0]['price_usd']
        last_price = token_data.iloc[-1]['price_usd']
        
        if first_price > 0:
            change_pct = ((last_price - first_price) / first_price) * 100
            perf_data.append({'symbol': symbol, 'change': change_pct})
    
    if not perf_data:
        return ""
    
    # Sort and take top/bottom 10
    perf_df = pd.DataFrame(perf_data).sort_values('change', ascending=False)
    top_bottom = pd.concat([perf_df.head(5), perf_df.tail(5)])
    
    # Color by performance
    colors = ['#22c55e' if x > 0 else '#ef4444' for x in top_bottom['change']]
    
    chart_config = {
        'type': 'bar',
        'data': {
            'labels': top_bottom['symbol'].tolist(),
            'datasets': [{
                'label': '7-Day Change %',
                'data': top_bottom['change'].tolist(),
                'backgroundColor': colors
            }]
        },
        'options': {
            'indexAxis': 'y',  # Horizontal bars
            'responsive': True,
            'plugins': {
                'legend': {'display': False},
                'title': {'display': True, 'text': '7-Day Performance Leaders & Laggards', 'font': {'size': 16}}
            },
            'scales': {
                'x': {
                    'title': {'display': True, 'text': 'Change %'}
                }
            }
        }
    }
    
    return create_chart_block('performanceChart', chart_config, width="800px")

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
    
    # Header with better styling
    lines.append("# 📊 Solana Radar - Live Dashboard")
    lines.append("")
    lines.append(f"**Last Updated**: {now}")
    lines.append("")
    lines.append("Automated daily analysis of Solana tokens with whale tracking, momentum indicators, and pattern detection.")
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
    
    # === Chart.js Library ===
    lines.append('<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>')
    lines.append('<style>')
    lines.append('body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }')
    lines.append('.chart-container { max-width: 900px; margin: 20px auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 8px; }')
    lines.append('</style>')
    lines.append("")
    
    # === Quick Stats ===
    lines.append("## 📈 Quick Stats")
    lines.append("")
    
    if not daily.empty:
        total_tokens = len(daily)
        total_vol = daily["volume_24h_usd"].sum() if "volume_24h_usd" in daily.columns else 0
        total_liq = daily["liquidity_usd"].sum() if "liquidity_usd" in daily.columns else 0
        
        # Risk counts
        if "concentration_risk" in daily.columns:
            risk_counts = daily["concentration_risk"].value_counts()
            low_risk = risk_counts.get('low', 0)
            
            lines.append(f"🎯 **{total_tokens} tokens tracked** | ")
            lines.append(f"💰 **{format_usd(total_vol)} 24h volume** | ")
            lines.append(f"💧 **{format_usd(total_liq)} liquidity** | ")
            lines.append(f"🟢 **{low_risk} low-risk tokens**")
            lines.append("")
    
    lines.append("---")
    lines.append("")
    
    # === Interactive Dashboard ===
    lines.append("## 🎨 Interactive Charts")
    lines.append("")
    
    # Risk Distribution
    lines.append("### 🥧 Risk Distribution")
    lines.append("")
    risk_chart = generate_risk_distribution_chart(history)
    if risk_chart:
        lines.append(risk_chart)
    else:
        lines.append("*Chart unavailable*")
    lines.append("")
    
    # Performance Leaders
    lines.append("### 📊 7-Day Performance")
    lines.append("")
    perf_chart = generate_performance_chart(history)
    if perf_chart:
        lines.append(perf_chart)
    else:
        lines.append("*Insufficient historical data for 7-day performance*")
    lines.append("")
    
    # Volume Leaders
    lines.append("### 📈 Volume Leaders")
    lines.append("")
    volume_chart = generate_volume_leaders_chart(daily)
    if volume_chart:
        lines.append(volume_chart)
    else:
        lines.append("*Chart unavailable*")
    lines.append("")
    
    # Concentration Trends
    lines.append("### 📉 Concentration Trends")
    lines.append("")
    trend_chart = generate_concentration_trends_chart(history)
    if trend_chart:
        lines.append(trend_chart)
    else:
        lines.append("*Chart unavailable*")
    lines.append("")
    
    # Scatter Plot
    lines.append("### 💎 Market Cap vs Concentration")
    lines.append("")
    scatter_chart = generate_scatter_chart(history)
    if scatter_chart:
        lines.append(scatter_chart)
    else:
        lines.append("*Chart unavailable*")
    lines.append("")
    
    lines.append("---")
    lines.append("")
    
    # Leaderboards
    safest_table, riskiest_table = generate_leaderboards(history)
    if safest_table:
        lines.append(safest_table)
    if riskiest_table:
        lines.append(riskiest_table)
    
    lines.append("---")
    lines.append("")
    
    # === NEW: Pattern Detection Dashboard ===
    lines.append("## 🎯 Pattern Detection")
    lines.append("")
    
    # Check if pattern data exists
    pattern_data = daily.copy() if not daily.empty else pd.DataFrame()
    
    if not pattern_data.empty and any(col.startswith('pattern_') for col in pattern_data.columns):
        # Count active patterns
        pattern_cols = [col for col in pattern_data.columns if col.startswith('pattern_')]
        active_patterns = 0
        for col in pattern_cols:
            active_patterns += (pattern_data[col] == True).sum()
        
        lines.append(f"**Active Patterns Detected**: {active_patterns}")
        lines.append("")
        
        # Pattern summary table
        pattern_summary = []
        for col in pattern_cols:
            pattern_name = col.replace('pattern_', '').replace('_', ' ').title()
            count = (pattern_data[col] == True).sum()
            if count > 0:
                pattern_summary.append({'Pattern': pattern_name, 'Count': count})
        
        if pattern_summary:
            lines.append("### Pattern Distribution")
            lines.append("")
            lines.append("| Pattern | Tokens |")
            lines.append("|---------|--------|")
            for p in sorted(pattern_summary, key=lambda x: x['Count'], reverse=True):
                lines.append(f"| {p['Pattern']} | {p['Count']} |")
            lines.append("")
        
        # Top tokens with patterns
        has_patterns = pattern_data[pattern_data[pattern_cols].any(axis=1)]
        if not has_patterns.empty:
            lines.append("### 🔍 Tokens with Active Patterns")
            lines.append("")
            lines.append("| Symbol | Name | Patterns | Volume 24h | Risk |")
            lines.append("|--------|------|----------|------------|------|")
            
            for _, row in has_patterns.head(10).iterrows():
                symbol = row.get('symbol', '???')
                name = str(row.get('name', '???'))[:25]
                patterns = [col.replace('pattern_', '').replace('_', ' ').title() 
                           for col in pattern_cols if row.get(col) == True]
                pattern_str = ', '.join(patterns[:3])  # Max 3 patterns
                vol = format_usd(row.get('volume_24h_usd', 0))
                risk = row.get('concentration_risk', 'unknown')
                risk_emoji = '🟢' if risk == 'low' else '🟡' if risk == 'medium' else '🟠' if risk == 'high' else '🔴'
                
                lines.append(f"| {symbol} | {name} | {pattern_str} | {vol} | {risk_emoji} |")
            
            lines.append("")
    else:
        lines.append("*Pattern detection data not available. Enable pattern detection in the pipeline.*")
        lines.append("")
    
    lines.append("---")
    lines.append("")
    
    # === Rest of the dashboard (keeping existing sections) ===
    # === Rest of sections from original ===
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
    
    # === Section: New Viable Tokens ===
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
    
    # === Section: Top Movers ===
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
    
    # === Section: Trading Signals ===
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
    
    # === Historical Data Section ===
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
    
    # === Data Schema ===
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
    
    # Footer
    lines.append("## 🔗 Links")
    lines.append("")
    lines.append("- **Live Dashboard**: [https://stelios5791.github.io/sol-reports/](https://stelios5791.github.io/sol-reports/)")
    lines.append("- **Data Repository**: [stelios5791/sol-reports](https://github.com/stelios5791/sol-reports)")
    lines.append("- **Analysis Pipeline**: Private repository (automated daily)")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*Generated automatically by Solana Radar v2.0*")
    lines.append("")
    
    return "\n".join(lines)

def main():
    """Generate and save the dashboard"""
    print("=" * 60)
    print("Solana Radar Dashboard Generator v2.0")
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
        print(f"   Charts: Risk, Performance, Volume, Trends, Scatter")
        print("=" * 60)
        
        return 0
        
    except Exception as e:
        print(f"❌ Error generating dashboard: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
