"""Generate README.md from data/tools.json and data/papers.json.

    python scripts/build_readme.py
"""
from __future__ import annotations

import json
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = json.loads((ROOT / "data" / "tools.json").read_text(encoding="utf-8"))
PAPERS = json.loads((ROOT / "data" / "papers.json").read_text(encoding="utf-8"))
SNAPSHOT = "September 2026"

# Public-copy cleanup of phrases written for an internal brief.
REPLACE = {
    "Massive-style data feed": "standard price + news data feed",
    "Massive-style news+price feed": "standard news + price feed",
    "Massive-style news+transcript feed": "news + transcript feed",
    "Massive-style news feed": "standard news feed",
    "Massive-style daily data": "standard daily price data",
    "Massive-style price+fundamentals+news feed": "standard price + fundamentals + news feed",
    " requested in this brief": "",
    "but included per the research brief": "but included for completeness",
    "�": "—",
}


def clean(s) -> str:
    s = "" if s is None else str(s)
    for a, b in REPLACE.items():
        s = s.replace(a, b)
    return " ".join(s.split())


def cell(s) -> str:
    return clean(s).replace("|", "\\|") or "—"


def stars(n) -> str:
    if not isinstance(n, (int, float)):
        return "—"
    return f"{n / 1000:.1f}k" if n >= 1000 else str(int(n))


def status(m) -> str:
    m = {True: "active", False: "stale", None: "unknown"}.get(m, m) if not isinstance(m, str) else m
    return {"active": "🟢", "slow": "🟡", "stale": "🟠", "archived": "🔴"}.get(m, "⚪")


def anchor(title: str) -> str:
    keep = "".join(ch for ch in title.lower() if ch.isalnum() or ch in " -")
    return keep.replace(" ", "-")


SECTIONS = [
    ("backtesting", "🧪", "Backtesting & quant research", """
The engines split by execution model. **Vectorized** engines (vectorbt, bt, backtesting.py) trade realism for
speed and suit parameter sweeps and signal research. **Event-driven** engines (NautilusTrader, LEAN, backtrader,
zipline-reloaded, vnpy) model order-by-order state and suit path-dependent logic, options and multi-asset books.
If you want the same strategy code to run in backtest and live, start with **NautilusTrader** or **QuantConnect LEAN**.""",
     ["The original Python “big three” (backtrader, Zipline, PyAlgoTrade) are largely unmaintained upstream. Use community successors such as zipline-reloaded and its reloaded analysis stack.",
      "**hftbacktest** is the rare open engine that models queue position and latency on L2/L3 data. Use it for market making; skip it otherwise.",
      "**quantstats** is the default tearsheet, **alphalens-reloaded** the default factor validator, and **PyPortfolioOpt → Riskfolio-Lib/skfolio → cvxportfolio** a sensible ladder of portfolio-optimization depth.",
      "China has a large, very active parallel ecosystem (vnpy, QUANTAXIS, WonderTrader, Hikyuu, rqalpha), documented mostly in Chinese."],
     {"backtesting-engine": "Backtesting engines", "research-platform": "Research platforms", "factor-research": "Factor research",
      "performance-analytics": "Performance analytics & tearsheets", "portfolio-optimization": "Portfolio optimization",
      "data-tooling": "Data tooling", "other": "Lists & other"}),
    ("live_trading", "⚡", "Live trading, execution & brokers", """
Connectivity, order management and bots for running strategies live. For **Interactive Brokers**, the maintained
path is **ib_async** (successor to the archived ib_insync), with **ib-gateway-docker + IBC** for a headless gateway.
Use **NautilusTrader** or **LEAN** when you want a full engine with IBKR adapters, reconciliation and risk checks.""",
     ["**alpaca-py** is a clean official SDK and a practical second venue or paper environment.",
      "In crypto, **freqtrade** (bots), **Hummingbot** (market making) and **CCXT** (exchange connectivity) are the de facto standards.",
      "Reserve FIX engines (the QuickFIX family) for venues that require FIX. Broker APIs cover most retail and small-fund needs.",
      "Gap: there is no widely adopted standalone TWAP/VWAP execution-algo library for equities. That logic lives inside the full platforms."],
     {"ibkr": "Interactive Brokers", "broker-sdk": "Broker SDKs", "execution-oms": "Execution & OMS", "crypto-bot": "Crypto bots",
      "market-making": "Market making", "fix-engine": "FIX engines", "webhook-bridge": "TradingView webhook bridges", "other": "Other"}),
    ("prediction_markets", "🎯", "Prediction markets (Kalshi, Polymarket & more)", """
SDKs, market makers, arbitrage bots, forecasting agents and datasets for event contracts. Several of Polymarket's
official repos (including `py-clob-client` and `agents`) are **archived**. Community SDKs and “CCXT for prediction
markets” libraries (**pmxt**, **dr-manhattan**) now fill the gap.""",
     ["**Jon-Becker/prediction-market-analysis** is the largest public Kalshi + Polymarket trade dataset, a strong first stop for research data.",
      "Cross-venue YES+NO arbitrage is a crowded, well-documented niche. Expect competition and fee changes.",
      "LLM forecasting bots cluster around Metaculus’s AI benchmarking tooling (**forecasting-tools**, **metac-bot-template**).",
      "Check jurisdictional access rules before trading. Kalshi is CFTC-regulated; Polymarket has restricted US retail access."],
     {"kalshi": "Kalshi", "polymarket": "Polymarket", "cross-venue": "Cross-venue & unified SDKs", "forecasting-agent": "Forecasting agents",
      "data-dataset": "Data & datasets", "sports-odds": "Sports odds", "other": "Other venues (Manifold, PredictIt, Limitless, DFlow…)"}),
    ("options", "📐", "Options, greeks & volatility", """
Pricing libraries, implied-volatility and surface fitting, options backtesters, greeks and gamma-exposure tools.
**QuantLib** remains the standard. **FinancePy**, **tf-quant-finance** and **RustQuant** are strong alternatives,
and **py_vollib** is the lightweight Black–Scholes / greeks / IV stack.""",
     ["**optopsy** is the most mature open options backtester.",
      "Gamma-exposure (GEX) dashboards are the most active niche (**gammagrid**, **gex-terminal**).",
      "Gap: no dominant, polished SVI/SABR surface-fitting library exists yet. The space is mostly single-author notebooks.",
      "Crypto-options tooling is almost entirely Deribit-specific and mostly dated."],
     {"pricing-library": "Pricing libraries", "vol-surface": "Volatility surfaces", "options-backtest": "Options backtesting",
      "greeks-risk": "Greeks & risk", "gamma-exposure": "Gamma exposure (GEX)", "vol-trading": "Volatility trading",
      "options-data": "Options data", "crypto-options": "Crypto options", "other": "Other"}),
    ("ai_agents", "🤖", "AI, agents & machine learning", """
LLM multi-agent trading frameworks, alpha mining, reinforcement learning, market foundation models, trading MCP
servers and evaluation benchmarks. **TradingAgents**, **ai-hedge-fund**, **FinRL**, **Microsoft RD-Agent(Q)** and
**Kronos** (a foundation model trained on candlestick data) anchor the space.""",
     ["Leakage-free live benchmarks (**DeepFund**, **Agent Market Arena**) find that even frontier LLMs struggle to make money once memorized history is taken away. Treat backtests of LLM traders with suspicion.",
      "Star counts in this area are often driven by virality. Weigh them against maturity.",
      "MCP servers now exist from Alpaca, Massive (formerly Polygon) and OpenBB, so agents can reach brokers and data directly.",
      "**Jev** is TypeSafe AI’s typed-judgment model (launched Sep 2026). Early trading projects use it either as the decision-maker or as a pass/reject gate on trades. See *Uses Jev*."],
     {"llm-multi-agent": "LLM multi-agent frameworks", "alpha-mining": "Alpha mining", "reinforcement-learning": "Reinforcement learning",
      "ml-trading": "ML trading", "foundation-model": "Foundation models", "mcp-server": "MCP servers", "benchmark": "Benchmarks",
      "uses-jev": "Uses Jev (TypeSafe)", "other": "Lists & other"}),
    ("fundamental_data", "📊", "Fundamentals, market data & alternative data", """
SEC filings, valuation, transcripts, ownership, market-data SDKs, tick storage, news sentiment and alt-data.
**OpenBB Platform** is the dominant open research hub, **edgartools** is best-in-class for SEC/XBRL, and
**ArcticDB / QuestDB / TimescaleDB** are the credible open time-series stores.""",
     ["Polygon.io is now **Massive** (`massive-com/client-python`). IEX Cloud shut down in 2024.",
      "**FinBERT** is still the default financial-sentiment baseline.",
      "Gaps: no open source for earnings-call transcripts (they are paywalled), and satellite or other exotic alt-data is almost entirely proprietary."],
     {"research-terminal": "Research terminals", "sec-filings": "SEC filings & XBRL", "valuation": "Valuation",
      "earnings-transcripts": "Earnings transcripts", "ownership-insider": "Ownership & insider", "market-data-sdk": "Market-data SDKs",
      "data-storage": "Tick & time-series storage", "news-sentiment": "News & sentiment", "alt-data": "Alternative data",
      "screener": "Screeners", "other": "Other"}),
]

PAPER_CATS = {
    "earnings-events": "Earnings events & PEAD", "analyst-revisions": "Analyst revisions", "momentum": "Momentum",
    "value-quality": "Value & quality", "fundamental-composite": "Fundamental composites", "factor-timing": "Factor timing & crowding",
    "short-interest": "Short interest & borrow", "options-implied": "Options-implied signals", "intraday-overnight": "Intraday & overnight",
    "stat-arb": "Statistical arbitrage", "ml-prediction": "ML return prediction", "llm-signals": "LLM signals",
    "llm-agents": "LLM trading agents", "rl-portfolio": "RL portfolio management", "alpha-mining": "Alpha mining",
    "crypto": "Crypto", "prediction-markets": "Prediction markets", "other": "Other",
}

TOP_STRATEGIES = [
    ("Text-based post-earnings drift", "Earnings-call and press-release text measures of surprise drift for weeks and beat numeric-surprise-only PEAD.", "PEAD.txt (JFQA 2023), earnings-call NLP papers"),
    ("Analyst estimate-revision momentum", "Cheap and implementable with consensus-estimate history. It works best in less-covered names.", "Fundamental-momentum literature"),
    ("Crash-aware cross-sectional momentum", "Classic 3–12 month momentum with volatility scaling to survive momentum crashes.", "Jegadeesh–Titman (1993), Daniel–Moskowitz (2016)"),
    ("Short-term reversal as liquidity provision", "A days-horizon strategy that pays for providing liquidity. It is sensitive to costs, so model spreads.", "Dai, Medhat, Novy-Marx & Rizova (2024)"),
    ("Overnight vs. intraday decomposition", "Most index gains accrue overnight. It is cheap to test with OHLC data, but partly arbitraged.", "Overnight-returns papers"),
    ("Options-implied skew, regime-conditioned", "A classic cross-sectional signal, but a 2026 paper finds it weakened in the AI/mega-cap regime.", "Tian & Wu; JFE 2025; arXiv 2608.26115"),
    ("Fine-tuned LLM news sentiment", "Real incremental information, but reported Sharpe ratios are inflated by look-ahead. Test forward.", "Lopez-Lira & Tang (2023), FinDPO, newsflow fine-tuning"),
    ("ML cross-sectional prediction + text", "Small per-stock R² still produces meaningful long–short spreads. Add news embeddings.", "Gu–Kelly–Xiu (2020), Chen–Pelger–Zhu (2023)"),
    ("Factor timing & decay monitoring", "An overlay that decides which sleeves to lean into as regimes change.", "Deep-learning factor-timing papers"),
    ("Automated alpha mining", "Generate formulaic alphas with RL or LLM search, then feed them into an ML or timing layer.", "AlphaGen (KDD 2023), RD-Agent(Q) (NeurIPS 2025)"),
]


def tool_block(items: list[dict]) -> list[str]:
    out = ["| Project | ★ | Lang | | What it's good at |", "|---|---:|---|:-:|---|"]
    for t in items:
        out.append(f"| [**{cell(t['name'])}**]({t['url']}) | {stars(t.get('stars'))} | {cell(t.get('language'))} | "
                   f"{status(t.get('maintained'))} | {cell(t.get('good_at'))} |")
    out += ["", f"<details><summary>Explainers ({len(items)})</summary>", ""]
    for t in items:
        out += [f"**[{clean(t['name'])}]({t['url']})** · {clean(t.get('language')) or '—'} · ★ {stars(t.get('stars'))}"
                f"{' · last push ' + clean(t['last_push']) if t.get('last_push') else ''}  ",
                clean(t.get("explainer")), "",
                f"✅ *Good at:* {clean(t.get('good_at')) or '—'}  ", f"⚠️ *Limitations:* {clean(t.get('limitations')) or '—'}", ""]
    out += ["</details>", ""]
    return out


def yesno(v) -> str:
    return "✅" if v is True else "❌" if v is False else "❔"


def main() -> None:
    by_sec = defaultdict(lambda: defaultdict(list))
    for t in TOOLS:
        by_sec[t["section"]][t.get("category") or "other"].append(t)
    for sec in by_sec.values():
        for items in sec.values():
            items.sort(key=lambda x: -(x.get("stars") or 0))
    n_code = sum(1 for p in PAPERS if p.get("code_url"))

    L = [
        '<div align="center">', "",
        "# Awesome Open-Source Trading", "",
        "**A curated map of open-source trading software and recent quant strategy research:**  ",
        "backtesting · live execution · Interactive Brokers · Kalshi & Polymarket · options & greeks · AI agents · fundamentals & data", "",
        f"![projects](https://img.shields.io/badge/projects-{len(TOOLS)}-2ea44f)"
        f" ![papers](https://img.shields.io/badge/papers-{len(PAPERS)}-8a2be2)"
        f" ![snapshot](https://img.shields.io/badge/snapshot-{SNAPSHOT.replace(' ', '%20')}-blue)"
        " ![license](https://img.shields.io/badge/license-CC0--1.0-lightgrey)", "",
        "</div>", "",
        "Every project has a short explainer, what it is good at, and its limitations. Every paper lists its strategy, "
        "the return **as reported by the authors**, whether costs and out-of-sample testing were included, and how to "
        "recreate it. Machine-readable data lives in [`data/`](data).", "",
        "> **Status legend:** 🟢 active · 🟡 slow · 🟠 stale · 🔴 archived · ⚪ unknown. Stars and activity are a "
        f"snapshot from {SNAPSHOT}.", "",
        "## Contents", "",
    ]
    for key, emoji, title, *_ in SECTIONS:
        L.append(f"- {emoji} [{title}](#{anchor(title)}) — {sum(len(v) for v in by_sec[key].values())} projects")
    L += [f"- 📚 [Strategy research papers](#strategy-research-papers) — {len(PAPERS)} papers",
          "- 🧭 [Methodology & caveats](#methodology--caveats)", "- 🤝 [Contributing](#contributing)", ""]

    L += ["## Start here", "", "| If you want to… | Start with |", "|---|---|",
          "| Research and backtest a stock strategy in Python | vectorbt (speed) or NautilusTrader / LEAN (realism, live parity) |",
          "| Trade live through Interactive Brokers | ib_async + ib-gateway-docker + IBC, or NautilusTrader / LEAN adapters |",
          "| Run a crypto bot or market maker | freqtrade, Hummingbot, CCXT |",
          "| Build on Kalshi / Polymarket | pmxt or dr-manhattan (unified SDKs), prediction-market-analysis (data) |",
          "| Price options and compute greeks | QuantLib, py_vollib, FinancePy; optopsy for backtests |",
          "| Experiment with LLM trading agents | TradingAgents, ai-hedge-fund, RD-Agent(Q); evaluate on DeepFund-style live benchmarks |",
          "| Pull fundamentals and filings | OpenBB Platform, edgartools |",
          "| Evaluate a strategy | quantstats, alphalens-reloaded, pyfolio-reloaded |", ""]

    for key, emoji, title, intro, takeaways, cats in SECTIONS:
        sec = by_sec[key]
        L += [f"## {title}", "", intro.strip(), "", "**Key takeaways**", ""]
        L += [f"- {t}" for t in takeaways] + [""]
        order = [c for c in cats if c in sec] + [c for c in sec if c not in cats]
        for c in order:
            L += [f"### {cats.get(c, c.replace('-', ' ').title())}", ""] + tool_block(sec[c])
        L += ["[⬆ back to top](#contents)", ""]

    L += ["## Strategy research papers", "",
          f"{len(PAPERS)} papers, mostly 2024–2026, covering momentum, value and quality, earnings events, options-implied "
          f"signals, ML and LLM signals, RL, alpha mining, stat-arb, crypto and prediction markets. Only {n_code} "
          "publish code. Returns are copied **as the authors report them**. Most recent LLM and RL papers report "
          "Sharpe ratios above 2 without transaction costs or clean out-of-sample tests, so treat those as upper bounds.", "",
          "**Read these caveats first**", "",
          "- **Borrow costs erase much of the anomaly zoo.** Muravyev, Pearson & Pollet (JF 2025) find 162 anomalies "
          "average +0.14%/month gross but about −0.01%/month net of stock-borrow fees. Size short legs with real borrow data.",
          "- **The “GPT-4 beats analysts” paper was withdrawn** (Kim, Muhn & Nikolaev) after replication problems, yet it is still widely cited.",
          "- **LLM look-ahead:** models may have memorized the backtest period. Prefer forward or live tests "
          "(e.g. LiveTradeBench, DeepFund) over backtests on pre-cutoff news.",
          "- **Regime risk:** a 2026 paper finds the classic options-skew signal weakened in the 2023–2026 AI/mega-cap regime.", "",
          "### Editor’s picks for a US equity long/short book (days–weeks holding)", "",
          "| # | Strategy | Why | Key papers |", "|---|---|---|---|"]
    for i, (s, why, ref) in enumerate(TOP_STRATEGIES, 1):
        L.append(f"| {i} | **{s}** | {why} | {ref} |")
    L += [""]

    by_pc = defaultdict(list)
    for p in PAPERS:
        by_pc[p.get("category") or "other"].append(p)
    for c in [k for k in PAPER_CATS if k in by_pc] + [k for k in by_pc if k not in PAPER_CATS]:
        ps = sorted(by_pc[c], key=lambda p: -int(p.get("year") or 0))
        L += [f"### {PAPER_CATS.get(c, c)}", "",
              "| Year | Paper | Strategy | Reported return | Sharpe | Net of costs | OOS | Code |",
              "|---|---|---|---|---|:-:|:-:|:-:|"]
        for p in ps:
            code = f"[↗]({p['code_url']})" if p.get("code_url") else ""
            L.append(f"| {cell(p.get('year'))} | [{cell(p.get('title'))}]({p['url']})<br><sub>{cell(p.get('venue'))}</sub> | "
                     f"{cell(p.get('strategy'))}<br><sub>{cell(p.get('universe_period'))}</sub> | {cell(p.get('reported_return'))} | "
                     f"{cell(p.get('reported_sharpe'))} | {yesno(p.get('costs_included'))} | {yesno(p.get('out_of_sample'))} | {code} |")
        L += ["", f"<details><summary>How to recreate ({len(ps)})</summary>", ""]
        for p in ps:
            L += [f"**[{clean(p.get('title'))}]({p['url']})** ({clean(p.get('year'))})  ",
                  f"🔧 {clean(p.get('how_to_recreate')) or '—'}  "]
            if p.get("notes"):
                L.append(f"⚠️ {clean(p.get('notes'))}")
            L.append("")
        L += ["</details>", ""]
    L += ["[⬆ back to top](#contents)", ""]

    L += ["## Methodology & caveats", "",
          f"- Compiled in {SNAPSHOT} from GitHub (search, API metadata and curated lists such as awesome-quant, "
          "awesome-systematic-trading and awesome-quant-ai), public web and social search, and arXiv, SSRN and journal pages.",
          "- Star counts, last-push dates and maintenance status are point-in-time. Popular does not mean mature: several 2026 AI "
          "repos show hype-driven star growth.",
          "- Paper returns are reported, not reproduced. “Net of costs” and “OOS” reflect what each paper states "
          "(❔ = not stated). A few very recent arXiv entries were verified at abstract level only and are flagged in their notes.",
          "- **Nothing here is investment advice.** Backtested and hypothetical results do not guarantee future performance.", "",
          "## Contributing", "",
          "Found a missing project, a dead link or a wrong number? Open an issue or PR. Edit `data/tools.json` or "
          "`data/papers.json` and run `python scripts/build_readme.py` to regenerate this README. See "
          "[CONTRIBUTING.md](CONTRIBUTING.md).", "",
          "## License", "", "[CC0 1.0](LICENSE): the list is public domain. Linked projects keep their own licenses.", ""]
    (ROOT / "README.md").write_text("\n".join(L), encoding="utf-8")
    print(f"README.md: {len(L)} lines, {len(TOOLS)} projects, {len(PAPERS)} papers")


if __name__ == "__main__":
    main()
