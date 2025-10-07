#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enhanced Dashboard Generator for sol-reports
Generates README.md with:
  - Daily Top 50 overview
  - New Viable Tokens (7-14 day old with potential)
  - Whale-filtered Signals
  - Historical stats and charts
"""

from pathlib import Path
from datetime import datetime
import pandas as pd

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
    
    # === Section 1: Daily Top 50 ===
    lines.append("## 🔥 Today's Top 50 Tokens")
    lines.append("")
    
    daily = safe_read_csv("daily_top50.csv")
    
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
            name = getattr(row, "name", "???")[:30]  # Truncate long names
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
    
    viable = safe_read_csv("new_viable.csv")
    
    if not viable.empty:
        lines.append(f"**Found**: {len(viable)} viable new tokens")
        lines.append("")
        
        # Criteria reminder
        lines.append("**Criteria**:")
        lines.append("- First seen 7-14 days ago")
        lines.append("- Volume > $50K")
        lines.append("- Liquidity > $100K")
        lines.append("- Missing streak < 2 (stable presence)")
        lines.append("- Concentration risk: low/medium")
        lines.append("")
        
        # Show table
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
    
    movers = safe_read_csv("top_movers.csv")
    
    if not movers.empty:
        # Summary stats
        gainers = movers[movers["category"].str.contains("gainer", na=False)]
        losers = movers[movers["category"].str.contains("loser", na=False)]
        spikes = movers[movers["category"].str.contains("volume_spike", na=False)]
        
        lines.append(f"**Total Movers**: {len(movers)}")
        lines.append(f"- 🚀 **Gainers** (>+20%): {len(gainers)}")
        lines.append(f"- 📉 **Losers** (<-20%): {len(losers)}")
        lines.append(f"- 📊 **Volume Spikes** (>+100%): {len(spikes)}")
        lines.append("")
        
        # Top Gainers
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
        
        # Top Losers
        if not losers.empty:
            lines.append("### 📉 Biggest Losers")
            lines.append("")
            lines.append("| # | Symbol | Name | Change 24h | Current Price | Volume Change | Risk |")
            lines.append("|---|--------|------|------------|---------------|---------------|------|")
            
            # Sort losers by price change (most negative first)
            losers_sorted = losers.sort_values("price_change_24h_pct", ascending=True)
            top_losers = losers_sorted.head(10)
            
            for row in top_losers.itertuples():
                rank = getattr(row, "rank", "?")
                symbol = getattr(row, "symbol", "???")
                name = getattr(row, "name", "???")[:25]
                price_chg = f"{getattr(row, 'price_change_24h_pct', 0):.2f}%"
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
    
    signals = safe_read_csv("signals_filtered.csv")
    
    if not signals.empty:
        # Count by signal type
        if "signal" in signals.columns:
            signal_counts = signals["signal"].value_counts()
            lines.append("**Signal Distribution**:")
            for sig, count in signal_counts.items():
                emoji = "🚀" if sig == "Breakout" else "👀" if sig == "Watch" else "❄️"
                lines.append(f"- {emoji} **{sig}**: {count} tokens")
            lines.append("")
        
        # Breakout signals
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
        
        # Watch signals
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
    
    # === Section 4: Historical Data ===
    lines.append("## 📈 Historical Data")
    lines.append("")
    
    history = safe_read_csv("history.csv")
    master = safe_read_csv("master.csv")
    performance = safe_read_csv("performance.csv")
    
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
    
    # === Section 5: Data Schema ===
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
    print("Generating Enhanced Dashboard")
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
