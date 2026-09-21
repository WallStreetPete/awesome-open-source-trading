<div align="center">

# Awesome Open-Source Trading

**A curated map of open-source trading software and recent quant strategy research:**  
backtesting · live execution · Interactive Brokers · Kalshi & Polymarket · options & greeks · AI agents · fundamentals & data

![projects](https://img.shields.io/badge/projects-458-2ea44f) ![papers](https://img.shields.io/badge/papers-113-8a2be2) ![snapshot](https://img.shields.io/badge/snapshot-September%202026-blue) ![license](https://img.shields.io/badge/license-CC0--1.0-lightgrey)

</div>

Every project has a short explainer, what it is good at, and its limitations. Every paper lists its strategy, the return **as reported by the authors**, whether costs and out-of-sample testing were included, and how to recreate it. Machine-readable data lives in [`data/`](data).

> **Status legend:** 🟢 active · 🟡 slow · 🟠 stale · 🔴 archived · ⚪ unknown. Stars and activity are a snapshot from September 2026.

## Contents

- 🧪 [Backtesting & quant research](#backtesting--quant-research) — 108 projects
- ⚡ [Live trading, execution & brokers](#live-trading-execution--brokers) — 68 projects
- 🎯 [Prediction markets (Kalshi, Polymarket & more)](#prediction-markets-kalshi-polymarket--more) — 83 projects
- 📐 [Options, greeks & volatility](#options-greeks--volatility) — 67 projects
- 🤖 [AI, agents & machine learning](#ai-agents--machine-learning) — 60 projects
- 📊 [Fundamentals, market data & alternative data](#fundamentals-market-data--alternative-data) — 72 projects
- 📚 [Strategy research papers](#strategy-research-papers) — 113 papers
- 🧭 [Methodology & caveats](#methodology--caveats)
- 🤝 [Contributing](#contributing)

## Start here

| If you want to… | Start with |
|---|---|
| Research and backtest a stock strategy in Python | vectorbt (speed) or NautilusTrader / LEAN (realism, live parity) |
| Trade live through Interactive Brokers | ib_async + ib-gateway-docker + IBC, or NautilusTrader / LEAN adapters |
| Run a crypto bot or market maker | freqtrade, Hummingbot, CCXT |
| Build on Kalshi / Polymarket | pmxt or dr-manhattan (unified SDKs), prediction-market-analysis (data) |
| Price options and compute greeks | QuantLib, py_vollib, FinancePy; optopsy for backtests |
| Experiment with LLM trading agents | TradingAgents, ai-hedge-fund, RD-Agent(Q); evaluate on DeepFund-style live benchmarks |
| Pull fundamentals and filings | OpenBB Platform, edgartools |
| Evaluate a strategy | quantstats, alphalens-reloaded, pyfolio-reloaded |

## Backtesting & quant research

The engines split by execution model. **Vectorized** engines (vectorbt, bt, backtesting.py) trade realism for
speed and suit parameter sweeps and signal research. **Event-driven** engines (NautilusTrader, LEAN, backtrader,
zipline-reloaded, vnpy) model order-by-order state and suit path-dependent logic, options and multi-asset books.
If you want the same strategy code to run in backtest and live, start with **NautilusTrader** or **QuantConnect LEAN**.

**Key takeaways**

- The original Python “big three” (backtrader, Zipline, PyAlgoTrade) are largely unmaintained upstream. Use community successors such as zipline-reloaded and its reloaded analysis stack.
- **hftbacktest** is the rare open engine that models queue position and latency on L2/L3 data. Use it for market making; skip it otherwise.
- **quantstats** is the default tearsheet, **alphalens-reloaded** the default factor validator, and **PyPortfolioOpt → Riskfolio-Lib/skfolio → cvxportfolio** a sensible ladder of portfolio-optimization depth.
- China has a large, very active parallel ecosystem (vnpy, QUANTAXIS, WonderTrader, Hikyuu, rqalpha), documented mostly in Chinese.

### Backtesting engines

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**Freqtrade**](https://github.com/freqtrade/freqtrade) | 54.6k | Python | 🟢 | Best all-in-one option for retail crypto algo-trading: strategy backtesting, hyperparameter optimization, ML feature integration (FreqAI), and live bot operation in one project. |
| [**vnpy**](https://github.com/vnpy/vnpy) | 45.5k | Python | 🟢 | Best for teams needing a complete, production-grade trading system (data, execution, risk, UI) for Chinese futures/derivatives markets, with backtesting as an integrated module. |
| [**NautilusTrader**](https://github.com/nautechsystems/nautilus_trader) | 29.2k | Rust | 🟢 | Best-in-class choice when you need a single codebase for both realistic tick-level backtesting and live production trading, especially for latency-sensitive or multi-venue strategies. |
| [**backtrader**](https://github.com/mementum/backtrader) | 23.3k | Python | 🟡 | Best for Python beginners and intermediate quants who want a batteries-included, well-documented event-driven engine with a huge base of tutorials and Stack Overflow answers. |
| [**QuantConnect LEAN**](https://github.com/QuantConnect/Lean) | 21.7k | C# | 🟢 | Best for multi-asset, multi-language (C#/Python) strategies that want an institution-grade engine with a path to a managed cloud/live-trading service if desired. |
| [**Zipline**](https://github.com/quantopian/zipline) | 20.1k | Python | 🔴 | Useful mainly for historical reference, academic coursework following older tutorials, or as the reference implementation the -reloaded forks are based on. |
| [**QUANTAXIS**](https://github.com/yutiansut/QUANTAXIS) | 11.2k | Python | 🟢 | Best for solo/small-team quants wanting a self-hosted, all-in-one data+backtest+live+visualization stack for Chinese markets. |
| [**StockSharp**](https://github.com/StockSharp/StockSharp) | 10.8k | C# | 🟢 | Best for .NET/C# shops wanting a complete, long-established trading platform (GUI tools, backtesting, live connectivity to many venues) rather than a Python library. |
| [**vectorbt**](https://github.com/polakowo/vectorbt) | 9.1k | Python | 🟢 | Best for rapid, large-scale parameter sweeps and signal research where iteration speed matters more than tick-level event realism. |
| [**Backtesting.py**](https://github.com/kernc/backtesting.py) | 9.0k | Python | 🟢 | Best for quick single-symbol strategy prototyping and clean, shareable HTML backtest reports with minimal boilerplate. |
| [**Jesse**](https://github.com/jesse-ai/jesse) | 8.6k | Python | 🟢 | Strong choice specifically for crypto strategy research and live deployment, with a smoother learning curve than Freqtrade for custom strategy logic. |
| [**rqalpha**](https://github.com/ricequant/rqalpha) | 6.8k | Python | 🟢 | Best choice for A-share/China-futures backtesting with T+1 rules, price limits and local market microstructure already modeled. |
| [**OctoBot**](https://github.com/Drakkar-Software/OctoBot) | 6.6k | Python | 🟢 | Good for users who want a GUI-driven crypto bot with pre-built strategies as well as the option to write custom logic. |
| [**WonderTrader**](https://github.com/wondertrader/wondertrader) | 6.4k | C++ | 🟢 | Strong option for higher-frequency Chinese futures/equities strategies where native C++ execution speed matters and Python bindings are still wanted for research. |
| [**hftbacktest**](https://github.com/nkaz001/hftbacktest) | 4.7k | Rust | 🟢 | The go-to open-source tool for realistic market-making and latency-sensitive HFT strategy backtesting with genuine order-book/queue-position modeling. |
| [**PyAlgoTrade**](https://github.com/gbeced/pyalgotrade) | 4.7k | Python | 🔴 | Historically significant reference implementation; still usable for simple equity/forex backtests if you don't need modern dependency support. |
| [**zvt**](https://github.com/zvtvz/zvt) | 4.3k | Python | 🟢 | Good for users who want an integrated data-to-backtest-to-visualization pipeline for Chinese equities without stitching together separate tools. |
| [**finmarketpy**](https://github.com/cuemacro/finmarketpy) | 3.8k | Python | 🟢 | Well suited to FX and macro strategy backtesting and market analysis, especially for users already using the broader Cuemacro toolchain (findatapy/chartpy). |
| [**PyBroker**](https://github.com/edtechre/pybroker) | 3.5k | Python | 🟢 | Good fit for quants blending ML model signals with rule-based logic who want built-in walk-forward validation and significance testing rather than bolting it on separately. |
| [**pysystemtrade**](https://github.com/pst-group/pysystemtrade) | 3.5k | Python | 🟢 | The reference implementation for anyone building a systematic, volatility-targeted, multi-instrument futures trading system in the CTA/trend-following tradition. |
| [**Hikyuu**](https://github.com/fasiondog/hikyuu) | 3.5k | C++ | 🟢 | Good when you need C++-level backtest speed with Python-level scripting convenience for A-share/futures strategy composition. |
| [**QSTrader**](https://github.com/mhallsmoore/qstrader) | 3.5k | Python | 🟡 | Excellent as a learning reference for how to architect an event-driven backtester with clearly separated alpha/risk/portfolio/execution layers. |
| [**bt**](https://github.com/pmorissette/bt) | 3.0k | Python | 🟢 | Well suited to systematic asset-allocation and rebalancing strategies (ETF rotation, risk parity, tactical asset allocation) rather than intraday/tick strategies. |
| [**Catalyst**](https://github.com/scrtlabs/catalyst) | 2.6k | Python | 🔴 | Historically notable as an early crypto-native zipline derivative; only useful today for reference or archaeology. |
| [**Blankly**](https://github.com/blankly-finance/blankly) | 2.5k | Python | 🟡 | Good for developers wanting a straightforward path from local backtest to paper trading to live deployment with minimal code changes. |
| [**barter-rs**](https://github.com/barter-rs/barter-rs) | 2.3k | Rust | 🟢 | Best for teams building a fully Rust-native trading stack who want backtest/live parity without a Python bridge layer. |
| [**qtpylib**](https://github.com/ranaroussi/qtpylib) | 2.3k | Python | 🔴 | Historically useful reference for an IBKR-centric event-driven backtesting/live design; still has residual usage among long-time users. |
| [**Investing Algorithm Framework**](https://github.com/coding-kitties/investing-algorithm-framework) | 2.1k | Python | 🟢 | Good for developers wanting a structured, batteries-included path from strategy scaffolding through backtest to deployed bot. |
| [**Lumibot**](https://github.com/Lumiwealth/lumibot) | 2.1k | Python | 🟢 | Best when minimizing the gap between backtested and live strategy code, across a genuinely broad set of asset classes and brokers, is the top priority. |
| [**zipline-reloaded**](https://github.com/stefan-jansen/zipline-reloaded) | 1.9k | Python | 🟢 | Best for users who already have zipline-based strategies or want the Pipeline-based cross-sectional factor workflow popularized by Quantopian, on a modern Python stack. |
| [**PandoraTrader**](https://github.com/pegasusTrader/PandoraTrader) | 1.5k | C++ | 🟢 | Good reference for building a clean, low-latency C++ CTP trading system for Chinese futures markets. |
| [**qf-lib**](https://github.com/quarkfin/qf-lib) | 969 | Python | 🟢 | Good for teams that want automated, presentation-ready PDF backtest reports as a first-class output, not just an afterthought. |
| [**basana**](https://github.com/gbeced/basana) | 866 | Python | 🟢 | Good for developers who want a modern asyncio-native crypto trading framework from an author with a long track record (PyAlgoTrade). |
| [**aat (Async Algorithmic Trading Engine)**](https://github.com/AsyncAlgoTrading/aat) | 835 | Python | 🟢 | Good fit for strategies that need to watch and trade across several exchanges concurrently using native async Python. |
| [**Spectre**](https://github.com/Heerozh/spectre) | 825 | Python | 🟡 | Good for large-universe cross-sectional factor research where GPU acceleration meaningfully speeds up factor computation and backtesting. |
| [**quanttrader (letianzj)**](https://github.com/letianzj/quanttrader) | 777 | HTML | 🟡 | Good as a readable reference implementation of event-driven backtest/live architecture, similar in spirit to backtesting.py but with live IBKR support. |
| [**Quantdom**](https://github.com/constverum/Quantdom) | 772 | Python | 🔴 | Useful if you specifically want a free desktop GUI backtester rather than a scripting library. |
| [**pylivetrader**](https://github.com/alpacahq/pylivetrader) | 685 | Python | 🔴 | Historically useful for taking a zipline/zipline-reloaded backtested algorithm live via Alpaca with minimal code changes. |
| [**trade-frame (TradeFrame)**](https://github.com/rburkholder/trade-frame) | 677 | C++ | 🟢 | Best for retail/prop developers who want a native C++ options and equities trading framework tied directly to IQFeed and IBKR TWS. |
| [**fast-trade**](https://github.com/jrmeier/fast-trade) | 595 | Python | 🟢 | Good for rapidly iterating on indicator-threshold style strategies expressed as configuration rather than code. |
| [**pyqstrat**](https://github.com/abbass2/pyqstrat) | 372 | Jupyter Notebook | 🟡 | Good for practitioners who want to see and audit every step of the simulation (useful for teaching or debugging subtle backtest bugs), including options strategies. |
| [**zipline-trader**](https://github.com/shlomiku/zipline-trader) | 330 | Python | 🟡 | Useful for teams committed to the zipline Pipeline API who want to go from backtest to live IBKR/Alpaca trading without rewriting strategy logic. |
| [**quantstrat (R)**](https://github.com/braverock/quantstrat) | 310 | R | 🟡 | The standard, most fully-featured event-driven backtesting engine for R users needing multi-asset, transaction-level simulation. |
| [**pinkfish**](https://github.com/fja05680/pinkfish) | 306 | Python | 🟢 | Good for straightforward daily-bar swing-trading backtests where a simple, easy-to-audit trade log is preferred over a heavyweight engine. |
| [**moonshot**](https://github.com/quantrocket-llc/moonshot) | 278 | Python | 🟢 | Good for QuantRocket users who want a lightweight, pandas-native vectorized backtester that shares code between research and live trading. |
| [**QuantFabric**](https://github.com/QuantFabric/QuantFabric) | 264 | CMake | 🟢 | Reference architecture for teams building production HFT connectivity to Chinese futures/bond/stock exchanges in C++. |
| [**gobacktest**](https://github.com/gobacktest/gobacktest) | 241 | Go | 🔴 | Useful as a reference architecture for Go developers wanting to understand or build an event-driven backtester, given the scarcity of Go-native options. |
| [**StrateQueue**](https://github.com/StrateQueue/StrateQueue) | 214 | Python | 🟢 | Useful for teams who've already built strategies in a specific backtesting engine's dialect and want to deploy them live without rewriting for a unified engine like Lumibot/NautilusTrader. |
| [**pineforge-engine (PineForge)**](https://github.com/pineforge-4pass/pineforge-engine) | 186 | C++ | 🟢 | The best option specifically for running PineScript strategies in a fast, offline, self-hosted engine with verified fidelity to TradingView's own backtest results. |
| [**backtrader (cloudQuant fork)**](https://github.com/cloudQuant/backtrader) | 184 | Python | 🟢 | Good choice for teams that like backtrader's API but need ongoing compatibility fixes, AI-assisted strategy tooling, or an actively responsive maintainer. |
| [**Strategems.jl**](https://github.com/JTAmos/Strategems.jl) | 167 | Julia | 🔴 | Historically notable as an early, relatively complete Julia backtesting framework; useful for reference despite being dormant. |
| [**blotter (R)**](https://github.com/braverock/blotter) | 116 | R | 🟢 | Essential companion to quantstrat for anyone doing serious R-based backtesting requiring realistic portfolio/account state tracking. |
| [**NowTrade**](https://github.com/edouardpoitras/NowTrade) | 103 | Python | 🔴 | Mainly of historical/reference interest for its criteria-based strategy definition style. |
| [**rust_bt**](https://github.com/jensnesten/rust_bt) | 87 | Rust | 🟢 | Worth evaluating for users wanting Rust-level backtest speed without adopting a large framework like NautilusTrader. |
| [**lfest-rs**](https://github.com/MathisWellmann/lfest-rs) | 82 | Rust | 🟢 | Good for testing leveraged crypto perpetual-futures strategies against realistic exchange mechanics (funding, liquidation) in a lightweight Rust simulator. |
| [**Quantitative (jeffrey-liang)**](https://github.com/jeffrey-liang/quantitative) | 66 | Python | 🔴 | Limited current utility; better served by more actively maintained alternatives for any new project. |
| [**OctoBot Script**](https://github.com/Drakkar-Software/OctoBot-Script) | 48 | TypeScript | 🟢 | Useful for OctoBot users who want to move from the GUI to a fully scriptable strategy/backtest workflow. |
| [**Fastback.jl**](https://github.com/rbeeli/Fastback.jl) | 21 | Julia | 🟢 | The main option for Julia-native quants who want compiled-language backtest speed without leaving the Julia ecosystem for Python/Rust. |
| [**zipline-extensions / moonshot (QuantRocket)**](https://github.com/quantrocket-llc/zipline-extensions) | 18 | Python | 🔴 | Only relevant to existing QuantRocket users running Zipline-based (rather than Moonshot-based) backtests. |
| [**antback**](https://github.com/ts-kontakt/antback) | 16 | Python | 🟢 | Good for users who want a small, transparent, easy-to-read backtesting core rather than a large opinionated framework. |
| [**Planar.jl**](https://github.com/BubbleParticles/Planar.jl) | 11 | Julia | 🟢 | Best current option for Julia-native crypto trading with real backtest/paper/live code-sharing and CCXT-based exchange connectivity. |
| [**yabte (Yet Another BackTesting Engine)**](https://github.com/bsdz/yabte) | 7 | Jupyter Notebook | 🟢 | Fine for very simple multi-asset backtests where a minimal, easy-to-read codebase is preferred over a full-featured framework. |

<details><summary>Explainers (62)</summary>

**[Freqtrade](https://github.com/freqtrade/freqtrade)** · Python · ★ 54.6k · last push 2026-09-21  
Freqtrade is the most popular free open-source crypto trading bot, combining a backtesting/hyperopt engine (with FreqAI, its built-in adaptive machine-learning module), a strategy plugin system, exchange connectivity via ccxt, and Telegram/REST-API/webUI control for live and dry-run trading. Its backtester is designed to closely emulate live execution (including realistic order-fill timing and configurable slippage) and supports walk-forward-style hyperparameter optimization. It has an enormous, very active community and is frequently the first recommendation for retail crypto algo-trading.

✅ *Good at:* Best all-in-one option for retail crypto algo-trading: strategy backtesting, hyperparameter optimization, ML feature integration (FreqAI), and live bot operation in one project.  
⚠️ *Limitations:* Crypto-exchange focused (via ccxt) rather than a general multi-asset backtester, and its strategy DSL is Freqtrade-specific rather than portable to other engines.

**[vnpy](https://github.com/vnpy/vnpy)** · Python · ★ 45.5k · last push 2026-09-13  
VeighNa (vnpy) is a full-featured Python quantitative trading platform, not just a backtester: it includes a CTP/multi-gateway connectivity layer for Chinese futures/options/stock exchanges, an event engine, a CTA strategy backtesting and live-trading module, spread trading, algo execution, risk management, and a Qt-based desktop UI, all built to be extended via a large plugin ('app') ecosystem. It has one of the largest and longest-running communities in the Chinese quant trading space (started 2015) and is used by both retail and institutional desks. Backtesting is one module (`vnpy_ctastrategy`/`vnpy_portfoliostrategy`) among many rather than the sole focus.

✅ *Good at:* Best for teams needing a complete, production-grade trading system (data, execution, risk, UI) for Chinese futures/derivatives markets, with backtesting as an integrated module.  
⚠️ *Limitations:* Heavier and more complex to set up than a pure backtesting library, with primary documentation and community support in Chinese.

**[NautilusTrader](https://github.com/nautechsystems/nautilus_trader)** · Rust · ★ 29.2k · last push 2026-09-21  
NautilusTrader is a high-performance, production-grade algorithmic trading platform with an event-driven backtesting engine whose core is written in Rust and exposed to Python via Cython/PyO3 bindings, so the exact same strategy code and order-matching logic run identically in backtest and live trading (eliminating the classic research/production parity gap). It models nanosecond-precision timestamps, realistic order types, multi-venue and multi-asset-class portfolios (FX, equities, futures, crypto), and ships adapters for major crypto exchanges and brokers like Interactive Brokers and Betfair. It has become one of the fastest-growing serious open-source trading engines, attracting significant institutional and prop-desk interest for its performance and correctness-first design.

✅ *Good at:* Best-in-class choice when you need a single codebase for both realistic tick-level backtesting and live production trading, especially for latency-sensitive or multi-venue strategies.  
⚠️ *Limitations:* Steeper learning curve than lightweight Python backtesters, and the Rust/Cython core makes deep customization harder without systems-level knowledge.

**[backtrader](https://github.com/mementum/backtrader)** · Python · ★ 23.3k · last push 2024-08-19  
backtrader is the most widely known pure-Python event-driven backtesting and live-trading framework, built around Cerebro (the engine), Strategy, Indicator and Analyzer classes that let you write a strategy once and run it on historical bars or against live broker feeds (Interactive Brokers, Oanda, and others via community plugins). It supports multiple data feeds and timeframes, resampling/replaying, a large indicator library, and a plotting layer built on matplotlib. Its API is mature and extremely well documented via years of blog posts and community tutorials, which is a big part of its popularity. The original repository has had no meaningful commits since mid-2024, and the community has shifted to actively maintained forks.

✅ *Good at:* Best for Python beginners and intermediate quants who want a batteries-included, well-documented event-driven engine with a huge base of tutorials and Stack Overflow answers.  
⚠️ *Limitations:* The upstream project is effectively unmaintained (no substantive commits since August 2024), so bug fixes and modern Python/pandas compatibility depend on community forks.

**[QuantConnect LEAN](https://github.com/QuantConnect/Lean)** · C# · ★ 21.7k · last push 2026-09-18  
LEAN is QuantConnect's open-source algorithmic trading engine, supporting equities, futures, options, forex and crypto with a unified data/security model, and strategies can be written in either C# or Python (via a managed Python.NET bridge). It provides realistic fill/slippage/fee models, a brokerage abstraction layer with many live adapters (Interactive Brokers, Tradier, Alpaca, and more), and the same engine backs QuantConnect's hosted cloud research/backtest/live platform used by tens of thousands of quants. It is widely regarded as one of the most institutionally credible open-source backtesters due to its emphasis on avoiding look-ahead bias and matching live-trading behavior exactly to backtests.

✅ *Good at:* Best for multi-asset, multi-language (C#/Python) strategies that want an institution-grade engine with a path to a managed cloud/live-trading service if desired.  
⚠️ *Limitations:* Running LEAN fully locally (data, Docker containers, brokerage plugins) has real setup overhead compared to lightweight pip-installable backtesters.

**[Zipline](https://github.com/quantopian/zipline)** · Python · ★ 20.1k · last push 2024-02-13  
Zipline is the event-driven backtesting engine originally built by Quantopian to power its hosted research and contest platform, and it became the de facto standard for Python algorithmic backtesting in the 2015-2020 era. It models a trading calendar, a Pipeline API for cross-sectional factor computation over a bundle of historical data, commission/slippage models, and a `TradingAlgorithm` lifecycle (`initialize`/`handle_data`) with tight integration to pyfolio, alphalens and empyrical for post-hoc analysis. Quantopian shut down in 2020 and stopped maintaining the project, freezing it on old pandas/numpy versions. It remains historically important because Qlib, rqalpha, moonshot and many others borrowed its Pipeline/algorithm design.

✅ *Good at:* Useful mainly for historical reference, academic coursework following older tutorials, or as the reference implementation the -reloaded forks are based on.  
⚠️ *Limitations:* Unmaintained and pinned to old dependency versions; use zipline-reloaded for anything new.

**[QUANTAXIS](https://github.com/yutiansut/QUANTAXIS)** · Python · ★ 11.2k · last push 2026-09-18  
QUANTAXIS is an integrated quantitative toolbox covering scheduled/distributed data collection, backtesting, paper and live trading, visualization, and multi-account management for Chinese stocks, futures and options, designed as a self-hostable local quant solution. It bundles its own database layer, a backtesting kernel, and a web-based visualization UI so a solo quant or small desk can run the entire research-to-trading loop without external SaaS dependencies. It is one of the largest and longest-running Chinese open-source quant platforms.

✅ *Good at:* Best for solo/small-team quants wanting a self-hosted, all-in-one data+backtest+live+visualization stack for Chinese markets.  
⚠️ *Limitations:* Very large surface area (data, backtest, trading, UI all bundled) makes it heavier to learn and operate than a focused backtesting library; Chinese-language-first documentation.

**[StockSharp](https://github.com/StockSharp/StockSharp)** · C# · ★ 10.8k · last push 2026-09-19  
StockSharp is a large, mature .NET algorithmic and quantitative trading platform for developing trading robots (strategies) across stock, forex, crypto and options/futures markets, including a full desktop terminal (Designer), a strategy runner (Shell/Runner), a backtesting/optimization engine, and connectors to dozens of exchanges and brokers. It is one of the most comprehensive open-source trading platforms outside the Python ecosystem, with both free open-source and paid enterprise-support tiers. Its backtesting engine supports both historical simulation and Monte Carlo-style optimization of strategy parameters.

✅ *Good at:* Best for .NET/C# shops wanting a complete, long-established trading platform (GUI tools, backtesting, live connectivity to many venues) rather than a Python library.  
⚠️ *Limitations:* C#/.NET-centric, which is a barrier for teams standardized on Python, and the full platform's breadth (GUI apps, many connectors) means a steeper initial learning curve.

**[vectorbt](https://github.com/polakowo/vectorbt)** · Python · ★ 9.1k · last push 2026-09-17  
vectorbt is a NumPy/pandas/Numba-accelerated vectorized backtesting and research toolkit built to test thousands of parameter combinations or strategy variants in seconds rather than minutes, by expressing entries/exits and portfolio simulation as array operations instead of an event loop. It includes an interactive Plotly-based visualization layer, built-in performance metrics, and utilities for signal generation, parameter grids and Monte Carlo-style robustness checks. There is a closed-source commercial successor, VectorBT PRO (vectorbt.pro), sold as a $20+/month subscription that adds a Rust simulation engine, portfolio optimization, pattern recognition, streaming indicators and much faster/broader simulation features on top of the open-source core; the open-source version remains free and is still actively developed in parallel.

✅ *Good at:* Best for rapid, large-scale parameter sweeps and signal research where iteration speed matters more than tick-level event realism.  
⚠️ *Limitations:* Vectorized simulation makes some realistic order-level effects (partial fills, complex order types, path-dependent logic) harder to express than in an event-driven engine; the most advanced features are gated behind the paid PRO version.

**[Backtesting.py](https://github.com/kernc/backtesting.py)** · Python · ★ 9.0k · last push 2026-08-05  
Backtesting.py is a small, dependency-light, single-purpose Python library for backtesting single-asset trading strategies with a very simple `Strategy`/`Backtest` API, interactive Bokeh-based HTML reports, and a built-in grid-search/heuristic optimizer. It deliberately favors simplicity and speed of iteration over the breadth of backtrader, and it's often recommended to newcomers as an easier on-ramp. It is actively maintained with a healthy release cadence.

✅ *Good at:* Best for quick single-symbol strategy prototyping and clean, shareable HTML backtest reports with minimal boilerplate.  
⚠️ *Limitations:* AGPL-3.0 licensing requires releasing source for network-served derivatives, and multi-asset/portfolio-level backtesting is not its focus (single strategy-per-instrument model).

**[Jesse](https://github.com/jesse-ai/jesse)** · Python · ★ 8.6k · last push 2026-09-17  
Jesse is an advanced crypto-focused trading framework aimed at simplifying strategy research, with a strategy API, over 300 built-in technical indicators, a fast backtesting engine, a genetic-algorithm-based optimizer, and a live/paper trading mode, plus an optional hosted dashboard product. It emphasizes correctness (avoiding common backtesting pitfalls like look-ahead bias) and developer ergonomics for crypto perpetuals/spot strategies. It is one of the more actively developed crypto-native trading frameworks.

✅ *Good at:* Strong choice specifically for crypto strategy research and live deployment, with a smoother learning curve than Freqtrade for custom strategy logic.  
⚠️ *Limitations:* Crypto-only focus; not designed for equities, futures or FX markets.

**[rqalpha](https://github.com/ricequant/rqalpha)** · Python · ★ 6.8k · last push 2026-09-18  
rqalpha is a Chinese-market-oriented, extensible and pluggable Python algorithmic trading and backtesting framework from Ricequant, supporting multiple security types (equities, futures) with a zipline-inspired algorithm lifecycle. It has a mod system that lets users swap in custom data sources, brokers, risk controls and event handlers, and it ships CTA/T0 strategy templates and a Chinese A-share trading-calendar-aware simulation engine. It remains one of the most active China-focused open backtesters.

✅ *Good at:* Best choice for A-share/China-futures backtesting with T+1 rules, price limits and local market microstructure already modeled.  
⚠️ *Limitations:* Documentation and community support are mostly in Chinese, and its architecture assumes Chinese market conventions.

**[OctoBot](https://github.com/Drakkar-Software/OctoBot)** · Python · ★ 6.6k · last push 2026-09-20  
OctoBot is an open-source crypto trading bot with a web interface, supporting technical-analysis strategies, arbitrage and social/copy trading across many exchanges, with a companion OctoBot-Script quant framework (below) for backtesting, optimization and live deployment. It emphasizes accessibility for non-programmers via its UI and a marketplace of pre-built strategies/tentacles (plugins), while still allowing custom Python strategy code for advanced users.

✅ *Good at:* Good for users who want a GUI-driven crypto bot with pre-built strategies as well as the option to write custom logic.  
⚠️ *Limitations:* Crypto-only; the plugin ('tentacle') architecture adds indirection that can be confusing for pure scripting-style backtest research.

**[WonderTrader](https://github.com/wondertrader/wondertrader)** · C++ · ★ 6.4k · last push 2026-09-01  
WonderTrader is a one-stop quant research-and-trading C++ framework covering data collection, backtesting/simulation, and live execution for Chinese futures and stock markets, designed for the performance demands of higher-frequency strategies. It exposes Python/C# wrappers over its C++ core so strategy authors don't have to write C++ directly, while still getting native execution speed for the matching/simulation engine. It is one of the most starred Chinese-language quant infrastructure projects and is used by real prop/quant shops.

✅ *Good at:* Strong option for higher-frequency Chinese futures/equities strategies where native C++ execution speed matters and Python bindings are still wanted for research.  
⚠️ *Limitations:* Documentation and community support are almost entirely Chinese-language, and the multi-component architecture (data, sim, execution) has a steep setup curve.

**[hftbacktest](https://github.com/nkaz001/hftbacktest)** · Rust · ★ 4.7k · last push 2025-12-23  
hftbacktest is a high-frequency-trading and market-making backtesting tool that models limit-order queue position, matching-engine behavior, and network/processing latency using full historical tick-by-tick trade and order-book data, rather than approximating fills at bar close like most backtesters. Originally Python+Numba, its core simulation has moved to Rust (with Python bindings) for speed while keeping a Python-friendly strategy API. It fills a gap most backtesting engines ignore: realistic microstructure effects for market-making and latency-sensitive strategies.

✅ *Good at:* The go-to open-source tool for realistic market-making and latency-sensitive HFT strategy backtesting with genuine order-book/queue-position modeling.  
⚠️ *Limitations:* Requires full L2/L3 tick and order-book history (far more data-intensive than bar-based backtesters) and has a steeper learning curve tied to market-microstructure concepts.

**[PyAlgoTrade](https://github.com/gbeced/pyalgotrade)** · Python · ★ 4.7k · last push 2023-11-13  
PyAlgoTrade is an older, once-popular event-driven backtesting library predating backtrader, supporting bar-based backtesting, paper trading and live trading against a handful of brokers, with built-in technical indicators and an optimizer for parameter sweeps. It was one of the first mainstream Python backtesting libraries and influenced the design of many later frameworks including its author's own basana. The repository is no longer actively developed.

✅ *Good at:* Historically significant reference implementation; still usable for simple equity/forex backtests if you don't need modern dependency support.  
⚠️ *Limitations:* No longer maintained; superseded in practice by basana (same author) and backtrader-family tools.

**[zvt](https://github.com/zvtvz/zvt)** · Python · ★ 4.3k · last push 2026-07-01  
zvt is a modular quant framework that uses SQL and pandas to provide a uniform, extensible way to record market data, compute factors, screen securities, backtest strategies, and monitor real-time trading, with results renderable as interactive charts. It targets Chinese A-share and some global markets and bundles its own data recorder/scheduler so it can operate largely self-contained. It combines data engineering, factor research and backtesting in one project rather than specializing in just one layer.

✅ *Good at:* Good for users who want an integrated data-to-backtest-to-visualization pipeline for Chinese equities without stitching together separate tools.  
⚠️ *Limitations:* Documentation is primarily Chinese-language and the all-in-one design is less modular if you only want the backtesting piece.

**[finmarketpy](https://github.com/cuemacro/finmarketpy)** · Python · ★ 3.8k · last push 2026-04-16  
finmarketpy (formerly pythalesians) is a Python library from Cuemacro (Saeed Amen) for backtesting trading strategies and analyzing markets, with particular strength in FX and macro/rates strategy research, technical indicator computation, and event-study style analysis. It integrates with several market-data sources and provides a `TradingModel` abstraction for building and backtesting rule-based strategies. It's maintained alongside Cuemacro's other libraries (findatapy for data, chartpy for plotting).

✅ *Good at:* Well suited to FX and macro strategy backtesting and market analysis, especially for users already using the broader Cuemacro toolchain (findatapy/chartpy).  
⚠️ *Limitations:* Smaller community than backtrader/vectorbt and documentation assumes familiarity with the author's companion libraries.

**[PyBroker](https://github.com/edtechre/pybroker)** · Python · ★ 3.5k · last push 2026-09-14  
PyBroker is a Python algorithmic trading library built specifically for combining machine-learning models with rule-based backtesting, offering fast Numba-accelerated simulation, walk-forward analysis, and bootstrapped statistical-significance testing of backtest results (to help detect overfitting/luck). It supports both classic indicator-based rules and ML model predictions as trading signals within the same backtest loop.

✅ *Good at:* Good fit for quants blending ML model signals with rule-based logic who want built-in walk-forward validation and significance testing rather than bolting it on separately.  
⚠️ *Limitations:* Smaller community than backtrader/vectorbt, and its ML-first API assumes some familiarity with scikit-learn-style model workflows.

**[pysystemtrade](https://github.com/pst-group/pysystemtrade)** · Python · ★ 3.5k · last push 2026-07-18  
pysystemtrade is the open-source implementation of the systematic futures trading framework described in Robert Carver's books 'Systematic Trading' and 'Advanced Futures Trading Strategies', modeling a full pipeline of raw price handling, forecast generation, forecast scaling/combination, position sizing via volatility targeting, and portfolio-level risk overlays. It is a real production system (Carver has traded live capital with variants of it) rather than a toy example, giving it unusual credibility for trend-following/carry-style diversified futures strategies. The repository moved from the original author's account to a group-maintained org and remains actively developed.

✅ *Good at:* The reference implementation for anyone building a systematic, volatility-targeted, multi-instrument futures trading system in the CTA/trend-following tradition.  
⚠️ *Limitations:* Steep learning curve and opinionated architecture tightly coupled to Carver's specific forecasting/sizing methodology; not a general-purpose backtester.

**[Hikyuu](https://github.com/fasiondog/hikyuu)** · C++ · ★ 3.5k · last push 2026-09-20  
Hikyuu is a high-performance quant research framework with a C++ core (bar/indicator engine) and Python bindings, providing reusable trading-system components (signal indicators, stop-loss/money-management modules, system objects) that can be freely recombined to assemble complete trading systems, then backtested with fast native execution. It targets Chinese A-share/futures markets and is one of the more performance-oriented open Chinese quant frameworks, comparable in spirit to how Hummingbot or NautilusTrader mix a fast core with a scriptable layer.

✅ *Good at:* Good when you need C++-level backtest speed with Python-level scripting convenience for A-share/futures strategy composition.  
⚠️ *Limitations:* Documentation and community are mostly Chinese-language, and the component-composition model has a learning curve.

**[QSTrader](https://github.com/mhallsmoore/qstrader)** · Python · ★ 3.5k · last push 2024-06-30  
QSTrader, from QuantStart's Michael Halls-Moore, is a modular, schedule-driven event-based backtesting framework aimed at long-short equity and ETF systematic strategies, emphasizing clean separation of alpha model, risk model, portfolio construction and execution handler components. It was designed as a teaching-quality reference architecture (it accompanies QuantStart's books and courses) rather than a maximally feature-complete production engine. Development has slowed but the codebase remains a commonly cited example of clean event-driven backtester design.

✅ *Good at:* Excellent as a learning reference for how to architect an event-driven backtester with clearly separated alpha/risk/portfolio/execution layers.  
⚠️ *Limitations:* Fewer built-in data connectors, broker integrations and indicators than backtrader or NautilusTrader, and development has slowed.

**[bt](https://github.com/pmorissette/bt)** · Python · ★ 3.0k · last push 2026-09-20  
bt is a flexible backtesting framework built on top of ffn (by the same author) that models strategies as a composable tree of `Algo` building blocks (e.g. select assets, weigh equally, rebalance) attached to `Strategy` nodes, which can be nested to build multi-strategy, multi-asset portfolios declaratively. This algo-tree design makes it easy to express typical asset-allocation and rebalancing strategies (momentum rotation, risk parity, tactical allocation) with very little code. It remains actively maintained with regular small releases.

✅ *Good at:* Well suited to systematic asset-allocation and rebalancing strategies (ETF rotation, risk parity, tactical asset allocation) rather than intraday/tick strategies.  
⚠️ *Limitations:* Vectorized/tree-based design is less natural for intraday, order-book-aware, or highly path-dependent strategies.

**[Catalyst](https://github.com/scrtlabs/catalyst)** · Python · ★ 2.6k · last push 2022-11-26  
Catalyst (originally by Enigma) was a crypto-focused fork of zipline that added exchange adapters (Bitfinex, Binance, Poloniex, etc.), crypto-specific commission/slippage models, and live trading against exchange APIs, while keeping zipline's Pipeline/algorithm structure. It was one of the first serious open-source crypto backtesters and briefly popular during the 2017-2019 crypto research wave. The repository is archived and unmaintained.

✅ *Good at:* Historically notable as an early crypto-native zipline derivative; only useful today for reference or archaeology.  
⚠️ *Limitations:* Archived and built on ancient zipline/pandas versions; does not run on modern Python without substantial patching.

**[Blankly](https://github.com/blankly-finance/blankly)** · Python · ★ 2.5k · last push 2024-12-30  
Blankly is a fully integrated backtesting, paper-trading and live-deployment framework covering crypto and equities, aimed at giving individual developers a quick path from strategy idea to a deployed bot with a consistent API across all three modes. It includes exchange/broker integrations and a simple, approachable strategy interface, similar in spirit to Lumibot but with its own architecture and cloud-deployment tooling from Blankly Finance.

✅ *Good at:* Good for developers wanting a straightforward path from local backtest to paper trading to live deployment with minimal code changes.  
⚠️ *Limitations:* Commit activity has slowed since the associated company's cloud product wound down.

**[barter-rs](https://github.com/barter-rs/barter-rs)** · Rust · ★ 2.3k · last push 2026-08-24  
Barter is an open-source Rust framework for building event-driven live-trading and backtesting systems, designed around the principle that strategies run on a near-identical engine in both modes, similarly to NautilusTrader's design philosophy but as a pure-Rust ecosystem (Barter-Data for market data, Barter-Execution for order routing, Barter-Instrument for instrument modeling). It targets developers who want Rust's performance and safety guarantees without leaving Rust for a Python research layer.

✅ *Good at:* Best for teams building a fully Rust-native trading stack who want backtest/live parity without a Python bridge layer.  
⚠️ *Limitations:* Smaller community and ecosystem than Python-first engines, and requires Rust proficiency rather than Python.

**[qtpylib](https://github.com/ranaroussi/qtpylib)** · Python · ★ 2.3k · last push 2021-09-22  
QTPyLib (Quantitative Trading Python Library) is an event-driven algo-trading framework by the author of yfinance and quantstats, built for researching, backtesting and executing strategies via Interactive Brokers, with a Blotter component for tick data recording. It was a well-regarded IBKR-focused framework in the late 2010s but has been dormant since 2021.

✅ *Good at:* Historically useful reference for an IBKR-centric event-driven backtesting/live design; still has residual usage among long-time users.  
⚠️ *Limitations:* No longer actively maintained; newer IBKR-integrated frameworks (Lumibot, NautilusTrader) are better current choices.

**[Investing Algorithm Framework](https://github.com/coding-kitties/investing-algorithm-framework)** · Python · ★ 2.1k · last push 2026-09-17  
Investing Algorithm Framework is a Python framework for developing, backtesting and deploying automated trading algorithms and bots, providing a structured project layout, data-provider abstractions, and portfolio/order management that carries over from backtest to live deployment. It's a newer, actively developed entry aimed at making the whole algorithm lifecycle (not just the backtest step) approachable.

✅ *Good at:* Good for developers wanting a structured, batteries-included path from strategy scaffolding through backtest to deployed bot.  
⚠️ *Limitations:* Smaller community than the major established frameworks (backtrader, Lean, NautilusTrader), so fewer third-party examples exist.

**[Lumibot](https://github.com/Lumiwealth/lumibot)** · Python · ★ 2.1k · last push 2026-09-21  
Lumibot is an algorithmic trading framework whose central design goal is that the exact same strategy code runs unmodified for both backtesting and live trading, across stocks, options, crypto, futures and forex, with adapters for multiple brokers (Alpaca, Interactive Brokers, Tradier, Schwab, and others). It provides a simple, Pythonic `Strategy` base class and handles scheduling, data retrieval and order routing consistently across backtest and live modes, making the transition from research to deployment low-friction. It is actively developed by Lumiwealth, which also offers a paid course/community around it.

✅ *Good at:* Best when minimizing the gap between backtested and live strategy code, across a genuinely broad set of asset classes and brokers, is the top priority.  
⚠️ *Limitations:* Backtest execution speed is not its strength (community feedback notes it can be noticeably slower than vectorized or Rust/C++-core engines for large parameter sweeps).

**[zipline-reloaded](https://github.com/stefan-jansen/zipline-reloaded)** · Python · ★ 1.9k · last push 2026-01-06  
zipline-reloaded is the community-maintained continuation of Quantopian's zipline, kept alive by Stefan Jansen (author of Machine Learning for Trading) and used as the backtesting engine throughout that book's example code. It preserves zipline's Pipeline API, bundle-based historical data ingestion and algorithm lifecycle while updating dependencies to modern pandas/numpy and fixing packaging and Python-version issues. It is paired with sibling reloaded forks of pyfolio, alphalens and empyrical to reconstruct the full Quantopian-era analysis stack. It is the closest thing to an 'official' successor to zipline for anyone who has existing zipline algorithms.

✅ *Good at:* Best for users who already have zipline-based strategies or want the Pipeline-based cross-sectional factor workflow popularized by Quantopian, on a modern Python stack.  
⚠️ *Limitations:* Development pace is modest and some newer data-source integrations lag behind commercial platforms.

**[PandoraTrader](https://github.com/pegasusTrader/PandoraTrader)** · C++ · ★ 1.5k · last push 2025-10-18  
PandoraTrader is a C++ high-frequency quantitative trading platform built around China's CTP futures API, providing a clean multi-strategy, multi-account execution architecture with clear separation between market data handling, strategy logic and order routing. It is aimed at low-latency Chinese futures trading rather than being a general vectorized/backtest-first research tool, though it includes simulation capability for strategy validation.

✅ *Good at:* Good reference for building a clean, low-latency C++ CTP trading system for Chinese futures markets.  
⚠️ *Limitations:* Narrow focus on CTP/Chinese futures connectivity, with less emphasis on rich backtesting/analytics tooling than Python-first frameworks.

**[qf-lib](https://github.com/quarkfin/qf-lib)** · Python · ★ 969 · last push 2026-08-31  
QF-Lib is a modular, event-driven Python backtesting library with data-vendor and broker integration points, portfolio-construction tooling, and automated PDF tearsheet/report generation, aimed at giving retail and small-fund quants an institutional-style research-to-report workflow. It separates data handling, event processing, and reporting cleanly, which makes it easier to swap components (e.g. data source or broker) than in more monolithic frameworks.

✅ *Good at:* Good for teams that want automated, presentation-ready PDF backtest reports as a first-class output, not just an afterthought.  
⚠️ *Limitations:* Smaller user base and ecosystem than backtrader/Lean/NautilusTrader, so fewer community-contributed integrations.

**[basana](https://github.com/gbeced/basana)** · Python · ★ 866 · last push 2026-08-09  
basana is a Python async/event-driven algorithmic trading framework focused on cryptocurrencies, written by the author of the earlier PyAlgoTrade project. It uses asyncio to drive a common event loop across live exchange websocket feeds and historical backtests, so a strategy coroutine runs unmodified in both modes. It ships exchange integrations (e.g. Binance) and basic backtesting/paper-trading support.

✅ *Good at:* Good for developers who want a modern asyncio-native crypto trading framework from an author with a long track record (PyAlgoTrade).  
⚠️ *Limitations:* Crypto-only focus and a much smaller ecosystem/community than Freqtrade or Jesse.

**[aat (Async Algorithmic Trading Engine)](https://github.com/AsyncAlgoTrading/aat)** · Python · ★ 835 · last push 2026-07-27  
aat is an asyncio-based, event-driven algorithmic trading engine with optional C++ acceleration for hot paths, designed to run the same strategy code across multiple exchanges simultaneously (live and backtest) using a pluggable exchange-adapter model. It models instruments, orders and events generically so strategies aren't tied to one venue, and supports both crypto and traditional-market adapters. It is less well known than backtrader/NautilusTrader but has a distinct focus on multi-exchange concurrency.

✅ *Good at:* Good fit for strategies that need to watch and trade across several exchanges concurrently using native async Python.  
⚠️ *Limitations:* Smaller community and documentation base than the major engines, so expect more custom adapter work.

**[Spectre](https://github.com/Heerozh/spectre)** · Python · ★ 825 · last push 2025-04-15  
Spectre is a GPU-accelerated (PyTorch/CUDA) factor-analysis and backtesting library that computes cross-sectional factors and runs vectorized portfolio backtests on the GPU for large universes, aiming at the kind of speed advantage vectorbt offers on CPU but for much larger factor-computation workloads. It supports a Pipeline-like factor DSL similar to zipline/Qlib. Development has slowed in the last year but the codebase is still functional and unique in its GPU-first design.

✅ *Good at:* Good for large-universe cross-sectional factor research where GPU acceleration meaningfully speeds up factor computation and backtesting.  
⚠️ *Limitations:* Requires a CUDA-capable GPU to get its main benefit, and the project has a much smaller community/support base than Qlib.

**[quanttrader (letianzj)](https://github.com/letianzj/quanttrader)** · HTML · ★ 777 · last push 2024-06-20  
quanttrader is an event-based backtesting and live-trading Python framework similar in design to backtesting.py, with a focus on a clean, understandable event loop and support for both historical simulation and live IBKR trading. It's a smaller but well-regarded project often cited as a readable reference implementation of the event-driven pattern.

✅ *Good at:* Good as a readable reference implementation of event-driven backtest/live architecture, similar in spirit to backtesting.py but with live IBKR support.  
⚠️ *Limitations:* Smaller community than backtesting.py or backtrader, with development having slowed since mid-2024.

**[Quantdom](https://github.com/constverum/Quantdom)** · Python · ★ 772 · last push 2022-07-06  
Quantdom is a PyQt-based desktop GUI framework for backtesting and analyzing trading strategies with visual equity curves, trade lists and metrics, aimed at users who prefer a point-and-click interface over notebooks/scripts. It bundles a strategy engine, portfolio simulator and charting UI in a single desktop app. Development stopped in 2022.

✅ *Good at:* Useful if you specifically want a free desktop GUI backtester rather than a scripting library.  
⚠️ *Limitations:* Unmaintained since 2022 and GUI-desktop-only, which limits automation and CI/reproducibility compared to scriptable engines.

**[pylivetrader](https://github.com/alpacahq/pylivetrader)** · Python · ★ 685 · last push 2022-10-04  
pylivetrader, from Alpaca, is a zipline-compatible live-trading library that lets algorithms written against zipline's `initialize`/`handle_data` API run live against Alpaca's brokerage, effectively providing the live-trading half that zipline itself never shipped. It has not been updated since 2022 as Alpaca's own tooling has evolved elsewhere.

✅ *Good at:* Historically useful for taking a zipline/zipline-reloaded backtested algorithm live via Alpaca with minimal code changes.  
⚠️ *Limitations:* No longer actively maintained; newer unified backtest/live frameworks (Lumibot, StrateQueue) are more current choices for Alpaca deployment.

**[trade-frame (TradeFrame)](https://github.com/rburkholder/trade-frame)** · C++ · ★ 677 · last push 2026-09-21  
TradeFrame is a C++17 framework and set of sample applications for testing and running automated options and equities/futures trading ideas using DTN IQFeed for real-time data and Interactive Brokers' TWS API for execution, including a built-in options Greeks/implied-volatility calculation library. It is one of the few actively maintained pure-C++ retail-oriented trading frameworks with real options pricing support baked in.

✅ *Good at:* Best for retail/prop developers who want a native C++ options and equities trading framework tied directly to IQFeed and IBKR TWS.  
⚠️ *Limitations:* Narrower community than Python frameworks and requires comfort with C++ build tooling and IBKR/IQFeed account setup.

**[fast-trade](https://github.com/jrmeier/fast-trade)** · Python · ★ 595 · last push 2026-09-14  
fast-trade is a library built with backtest portability and raw performance in mind, letting strategies be defined largely through declarative indicator/condition configuration (rather than imperative event-loop code) and executed as vectorized pandas operations for speed. It's aimed at users who want to backtest many indicator-based strategy variants quickly without hand-writing an event loop for each.

✅ *Good at:* Good for rapidly iterating on indicator-threshold style strategies expressed as configuration rather than code.  
⚠️ *Limitations:* Configuration-driven strategy definition is less flexible than full imperative strategy code for complex, stateful logic.

**[pyqstrat](https://github.com/abbass2/pyqstrat)** · Jupyter Notebook · ★ 372 · last push 2023-11-05  
pyqstrat is a fast, extensible, and deliberately transparent Python library for backtesting quantitative strategies, written by a former Morgan Stanley/JPMorgan quant, with a design philosophy of making every intermediate computation inspectable rather than hiding logic behind opaque abstractions. It supports both simple vectorized and more detailed order-level simulation and includes trade/contract abstractions for options and multi-leg strategies.

✅ *Good at:* Good for practitioners who want to see and audit every step of the simulation (useful for teaching or debugging subtle backtest bugs), including options strategies.  
⚠️ *Limitations:* Development has slowed and the primary documentation format (Jupyter notebooks) is less structured than a full docs site.

**[zipline-trader](https://github.com/shlomiku/zipline-trader)** · Python · ★ 330 · last push 2023-12-25  
zipline-trader extends the zipline-reloaded engine with live paper/real trading support against Interactive Brokers and Alpaca, something the original zipline never fully productionized. It keeps the same backtest API so a strategy validated in backtest can be deployed live with minimal code changes. Development has slowed considerably since 2023.

✅ *Good at:* Useful for teams committed to the zipline Pipeline API who want to go from backtest to live IBKR/Alpaca trading without rewriting strategy logic.  
⚠️ *Limitations:* Low recent commit activity and a much smaller user base than Lumibot or NautilusTrader for the same live-trading use case.

**[quantstrat (R)](https://github.com/braverock/quantstrat)** · R · ★ 310 · last push 2023-09-14  
quantstrat is the classic R package for transaction-oriented backtesting and simulation of trading systems, providing infrastructure for constructing multi-asset-class, multi-currency trading strategies with realistic order/position/transaction tracking via its companion `blotter` package. For roughly a decade it was the standard serious backtesting tool in the R ecosystem, comparable to backtrader/zipline in Python, and much academic and practitioner R-based systematic trading work is built on it.

✅ *Good at:* The standard, most fully-featured event-driven backtesting engine for R users needing multi-asset, transaction-level simulation.  
⚠️ *Limitations:* Development has slowed considerably and the R quant ecosystem overall has shrunk relative to Python's, so fewer new integrations/tutorials appear.

**[pinkfish](https://github.com/fja05680/pinkfish)** · Python · ★ 306 · last push 2026-09-18  
pinkfish is a lightweight backtester and 'spreadsheet library' for security analysis, aimed at swing/position trading strategies on daily bars with a simple, transparent trade-log-based simulation model rather than a full event-driven architecture. It emphasizes ease of inspection of individual trades and is commonly used in tandem with the author's stock-universe datasets.

✅ *Good at:* Good for straightforward daily-bar swing-trading backtests where a simple, easy-to-audit trade log is preferred over a heavyweight engine.  
⚠️ *Limitations:* Not designed for intraday/tick data or complex multi-leg/derivatives strategies.

**[moonshot](https://github.com/quantrocket-llc/moonshot)** · Python · ★ 278 · last push 2026-07-30  
Moonshot is the vectorized, pandas-based backtesting and trading engine that ships inside QuantRocket, a commercial quant research platform, but is itself released open source. Strategies are expressed as vectorized DataFrame operations (similar in spirit to `bt` or `zipline`'s Pipeline) which makes it fast for cross-sectional, multi-asset daily strategies, and the same strategy code can be pushed to live trading via QuantRocket's infrastructure. It is tightly coupled to QuantRocket's data bundles and Docker-based deployment model.

✅ *Good at:* Good for QuantRocket users who want a lightweight, pandas-native vectorized backtester that shares code between research and live trading.  
⚠️ *Limitations:* Designed to be used inside the QuantRocket ecosystem (Docker + commercial data subscriptions), so it is less turnkey standalone.

**[QuantFabric](https://github.com/QuantFabric/QuantFabric)** · CMake · ★ 264 · last push 2026-08-07  
QuantFabric is a Linux/C++ mid- and high-frequency trading system targeting Chinese futures, stock and bond exchanges, providing exchange gateways, a strategy runtime, and infrastructure for low-latency order routing rather than a pure research backtester. It is built primarily for production execution speed on Chinese market connectivity (CTP and similar).

✅ *Good at:* Reference architecture for teams building production HFT connectivity to Chinese futures/bond/stock exchanges in C++.  
⚠️ *Limitations:* Execution/connectivity-focused rather than research/backtesting-focused, and documentation is Chinese-first.

**[gobacktest](https://github.com/gobacktest/gobacktest)** · Go · ★ 241 · last push 2023-10-11  
gobacktest is a Go implementation of an event-driven backtesting framework, modeling the same core event-loop architecture (data handler, strategy, portfolio, execution handler) popularized by Python engines like QSTrader, but for Go developers. It is one of the few dedicated event-driven backtesting frameworks in the Go ecosystem. The repository is now archived.

✅ *Good at:* Useful as a reference architecture for Go developers wanting to understand or build an event-driven backtester, given the scarcity of Go-native options.  
⚠️ *Limitations:* Archived/unmaintained, and Go's backtesting library ecosystem overall is far thinner than Python's or even Rust's.

**[StrateQueue](https://github.com/StrateQueue/StrateQueue)** · Python · ★ 214 · last push 2026-05-19  
StrateQueue is a broker-agnostic Python library that lets you deploy strategies originally written for any major backtesting engine (backtrader, vectorbt, backtesting.py, and others) to live or paper trading with zero code changes, acting as a deployment/execution adapter layer rather than a backtester itself. It includes built-in safety controls (position limits, kill switches) aimed at reducing the risk of deploying an unmodified research strategy straight to a live account.

✅ *Good at:* Useful for teams who've already built strategies in a specific backtesting engine's dialect and want to deploy them live without rewriting for a unified engine like Lumibot/NautilusTrader.  
⚠️ *Limitations:* New project with a small community; correctness of its cross-engine adapters for edge-case strategy logic is not yet broadly battle-tested.

**[pineforge-engine (PineForge)](https://github.com/pineforge-4pass/pineforge-engine)** · C++ · ★ 186 · last push 2026-09-21  
PineForge transpiles TradingView PineScript v6 strategies into C++ and runs deterministic, offline backtests on user-provided OHLCV data, validated trade-for-trade against TradingView's own backtest output across a large corpus of open and community scripts. It fills a specific niche: letting traders who write strategies in PineScript (TradingView's DSL) get a fast, self-hosted, reproducible backtest engine without needing TradingView's own infrastructure, and it's drivable by AI agents via a bundled MCP server.

✅ *Good at:* The best option specifically for running PineScript strategies in a fast, offline, self-hosted engine with verified fidelity to TradingView's own backtest results.  
⚠️ *Limitations:* Scope is specifically PineScript replication rather than general-purpose strategy authoring, and it's a young project with a small track record outside its own validation corpus.

**[backtrader (cloudQuant fork)](https://github.com/cloudQuant/backtrader)** · Python · ★ 184 · last push 2026-09-21  
This is an actively maintained fork of backtrader that keeps the original Cerebro/Strategy/Analyzer API but adds performance work, modern pandas/numpy compatibility, an MCP server and AI-agent skills for strategy generation, and a companion web platform. It exists specifically to fill the maintenance gap left by the original mementum/backtrader repository. It also spun off fincore, a modern replacement for empyrical/pyfolio-style analytics. Because it tracks upstream's design closely, existing backtrader strategies port over with minimal changes.

✅ *Good at:* Good choice for teams that like backtrader's API but need ongoing compatibility fixes, AI-assisted strategy tooling, or an actively responsive maintainer.  
⚠️ *Limitations:* Much smaller community and less battle-tested than the original project, with far fewer third-party tutorials.

**[Strategems.jl](https://github.com/JTAmos/Strategems.jl)** · Julia · ★ 167 · last push 2021-04-06  
Strategems.jl is a Julia package for quantitative systematic trading strategy development and backtesting, one of the earlier attempts at a full Julia-native backtesting framework analogous to quantstrat in R or backtrader in Python. Development has been dormant since 2021.

✅ *Good at:* Historically notable as an early, relatively complete Julia backtesting framework; useful for reference despite being dormant.  
⚠️ *Limitations:* No longer actively maintained; Fastback.jl and Planar.jl are more current Julia alternatives.

**[blotter (R)](https://github.com/braverock/blotter)** · R · ★ 116 · last push 2024-12-14  
blotter provides the transaction infrastructure underlying quantstrat: instrument definitions, transaction records, and portfolio/account objects for multi-asset-class, multi-currency trading system simulation and research. It's the accounting/state-tracking layer that quantstrat's strategy-signal layer sits on top of.

✅ *Good at:* Essential companion to quantstrat for anyone doing serious R-based backtesting requiring realistic portfolio/account state tracking.  
⚠️ *Limitations:* Only useful in combination with quantstrat (or custom code built to its interfaces), not a standalone backtester.

**[NowTrade](https://github.com/edouardpoitras/NowTrade)** · Python · ★ 103 · last push 2017-02-08  
NowTrade is an older Python library for backtesting technical/mechanical trading strategies across stock and currency markets, with a criteria-based strategy definition style (combining indicator conditions into entry/exit rules) that predates many of the more modern frameworks. It has not been updated since 2017.

✅ *Good at:* Mainly of historical/reference interest for its criteria-based strategy definition style.  
⚠️ *Limitations:* Long unmaintained (no commits since 2017) and incompatible with modern Python/pandas without significant rework.

**[rust_bt](https://github.com/jensnesten/rust_bt)** · Rust · ★ 87 · last push 2026-01-05  
rust_bt is a high-performance, low-latency backtesting engine written in Rust for testing quantitative strategies on historical and live data, exposed with a Python-friendly interface, aimed at users who want vectorbt/NautilusTrader-style Rust-core speed in a smaller, more approachable project.

✅ *Good at:* Worth evaluating for users wanting Rust-level backtest speed without adopting a large framework like NautilusTrader.  
⚠️ *Limitations:* Young project with a small community and less proven track record than established Rust engines like NautilusTrader or Barter.

**[lfest-rs](https://github.com/MathisWellmann/lfest-rs)** · Rust · ★ 82 · last push 2026-09-04  
LFEST is a simulated leveraged perpetual-futures exchange in Rust, letting strategy authors trade a simulated matching engine that mimics real perpetual-futures mechanics (funding, leverage, liquidation) for backtesting purposes, rather than approximating fills through a simple bar-close model. It's a narrow, focused tool aimed specifically at crypto perpetuals strategy testing.

✅ *Good at:* Good for testing leveraged crypto perpetual-futures strategies against realistic exchange mechanics (funding, liquidation) in a lightweight Rust simulator.  
⚠️ *Limitations:* Narrow scope (perpetual futures simulation only) and a small, single-maintainer project.

**[Quantitative (jeffrey-liang)](https://github.com/jeffrey-liang/quantitative)** · Python · ★ 66 · last push 2019-03-03  
A small, largely dormant quantitative-finance and backtesting library covering basic strategy simulation and metric computation. Included mainly for completeness given its mention in the awesome-quant list; there is little recent activity or documentation to differentiate it from more established alternatives.

✅ *Good at:* Limited current utility; better served by more actively maintained alternatives for any new project.  
⚠️ *Limitations:* No commits since 2019 and minimal documentation.

**[OctoBot Script](https://github.com/Drakkar-Software/OctoBot-Script)** · TypeScript · ★ 48 · last push 2026-09-13  
OctoBot-Script is the quant-framework companion to OctoBot, providing a scriptable path from backtesting to parameter optimization to live trading for crypto strategies, aimed at users who want more programmatic control than the main OctoBot GUI product offers. It shares OctoBot's exchange connectivity and data layer.

✅ *Good at:* Useful for OctoBot users who want to move from the GUI to a fully scriptable strategy/backtest workflow.  
⚠️ *Limitations:* Small community and low visibility relative to the main OctoBot project; documentation is limited.

**[Fastback.jl](https://github.com/rbeeli/Fastback.jl)** · Julia · ★ 21 · last push 2026-09-05  
Fastback.jl is a backtester written in pure Julia designed to exploit Julia's compiled performance for fast strategy simulation, from an author (Rene Beeli) who also maintains related Julia quant packages (RiskPerf.jl, LightweightCharts.jl). It's one of the very few actively developed dedicated backtesting engines in the Julia ecosystem.

✅ *Good at:* The main option for Julia-native quants who want compiled-language backtest speed without leaving the Julia ecosystem for Python/Rust.  
⚠️ *Limitations:* Very small community and ecosystem compared to Python/Rust backtesting tools.

**[zipline-extensions / moonshot (QuantRocket)](https://github.com/quantrocket-llc/zipline-extensions)** · Python · ★ 18 · last push 2020-04-17  
This package provides Zipline extensions and adapters specifically for QuantRocket, letting Zipline-based backtests use QuantRocket's data bundles and infrastructure. It's a small integration-glue project rather than a standalone backtesting engine.

✅ *Good at:* Only relevant to existing QuantRocket users running Zipline-based (rather than Moonshot-based) backtests.  
⚠️ *Limitations:* Narrow integration-only scope and no longer actively updated.

**[antback](https://github.com/ts-kontakt/antback)** · Python · ★ 16 · last push 2026-08-16  
antback is a lightweight, deliberately minimal event-loop-style backtest engine that allows a function-driven imperative coding style using efficient stateful helper functions and data containers, positioned as a fast, transparent alternative to heavier frameworks for users who want to see exactly what the engine is doing at each step.

✅ *Good at:* Good for users who want a small, transparent, easy-to-read backtesting core rather than a large opinionated framework.  
⚠️ *Limitations:* Very new with minimal community adoption and documentation compared to established engines.

**[Planar.jl](https://github.com/BubbleParticles/Planar.jl)** · Julia · ★ 11 · last push 2026-09-17  
Planar.jl is a trading framework built around CCXT (via Julia bindings) for crypto exchange connectivity, with Zarr-backed OHLCV data persistence, contiguity-checked data feeds, isolated-margin position management, and a loop-based backtester that shares the same strategy code across simulation, paper and live trading modes. It's a newer but actively developed entry in the small Julia trading-framework space, notable for treating backtest/paper/live parity as a first-class design goal like NautilusTrader/Barter do in Rust.

✅ *Good at:* Best current option for Julia-native crypto trading with real backtest/paper/live code-sharing and CCXT-based exchange connectivity.  
⚠️ *Limitations:* Small community and ecosystem, and crypto-only exchange connectivity via CCXT.

**[yabte (Yet Another BackTesting Engine)](https://github.com/bsdz/yabte)** · Jupyter Notebook · ★ 7 · last push 2026-02-15  
YABTE is a small, straightforwardly named Python backtesting engine offering a simple strategy/book abstraction for multi-asset historical simulation, positioned as a lightweight alternative for users who find the major frameworks too heavyweight for simple use cases.

✅ *Good at:* Fine for very simple multi-asset backtests where a minimal, easy-to-read codebase is preferred over a full-featured framework.  
⚠️ *Limitations:* Extremely small community/adoption and limited documentation.

</details>

### Research platforms

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**Qlib**](https://github.com/microsoft/qlib) | 48.7k | Python | 🟢 | Best for ML-driven systematic equity/futures research where you want an integrated data-to-model-to-backtest-to-execution pipeline with many reference model implementations out of the box. |
| [**machine-learning-for-trading**](https://github.com/stefan-jansen/machine-learning-for-trading) | 21.0k | Jupyter Notebook | 🟢 | Excellent as a structured, end-to-end curriculum and working code reference for building an ML-based quant research pipeline from scratch. |
| [**FinRL**](https://github.com/AI4Finance-Foundation/FinRL) | 16.4k | Jupyter Notebook | 🟢 | The standard starting point for anyone researching deep reinforcement learning applied to trading/portfolio management, with ready-made environments and baselines. |
| [**gs-quant**](https://github.com/goldmansachs/gs-quant) | 13.0k | Python | 🟢 | Valuable for derivatives pricing/risk workflows and institutional-grade portfolio construction and backtesting utilities modeled on real bank quant practice. |
| [**FinRL-Meta**](https://github.com/AI4Finance-Foundation/FinRL-Meta) | 1.9k | Python | 🟢 | Useful for benchmarking RL trading algorithms across a wider and more standardized set of market environments than FinRL's own tutorials provide. |
| [**asavinov/intelligent-trading-bot**](https://github.com/asavinov/intelligent-trading-bot) | 1.9k | Python | 🟢 | Good for exploring systematic ML feature-engineering-driven signal generation as an alternative to hand-coded indicator rules. |
| [**AlphaPy**](https://github.com/ScottfreeLLC/AlphaPy) | 1.8k | Python | 🟢 | Good for quickly standing up an AutoML pipeline for return/direction prediction without hand-rolling feature engineering and model-selection code. |
| [**QuantSoftware Toolkit**](https://github.com/QuantSoftware/QuantSoftwareToolkit) | 480 | HTML | 🔴 | Historical interest for those following the original Georgia Tech CS7646 course materials. |
| [**Trading Strategy (tradingstrategy.ai)**](https://github.com/tradingstrategy-ai/getting-started) | 250 | Jupyter Notebook | 🟢 | The most complete open option for backtesting DeFi/DEX trading strategies with real on-chain historical data. |

<details><summary>Explainers (9)</summary>

**[Qlib](https://github.com/microsoft/qlib)** · Python · ★ 48.7k · last push 2026-09-17  
Qlib is Microsoft's AI-oriented quantitative investment platform covering the full pipeline from data processing and feature/factor engineering, through model training (classic ML and deep learning, including LSTM/Transformer/GNN-style models for return prediction), to backtesting, portfolio optimization, and order execution simulation. It provides an Alpha158/Alpha360 factor library, a workflow/experiment-tracking layer, and reference implementations of many published quant ML papers, making it as much a research reproducibility framework as a backtester. It is one of the highest-profile and most actively developed open-source quant research platforms, with continued corporate backing from Microsoft Research Asia.

✅ *Good at:* Best for ML-driven systematic equity/futures research where you want an integrated data-to-model-to-backtest-to-execution pipeline with many reference model implementations out of the box.  
⚠️ *Limitations:* Heavier and more opinionated than a simple backtester; its data infrastructure and workflow conventions require real onboarding investment, and China A-share data/examples are the most polished path.

**[machine-learning-for-trading](https://github.com/stefan-jansen/machine-learning-for-trading)** · Jupyter Notebook · ★ 21.0k · last push 2026-09-21  
This repository contains all the code and notebooks accompanying Stefan Jansen's 'Machine Learning for Algorithmic Trading' book, walking through the full pipeline of alpha factor research, ML model training (including deep learning and NLP on financial text), and backtesting using zipline-reloaded, alphalens-reloaded and pyfolio-reloaded. It functions less as a standalone library and more as a comprehensive, working reference implementation of an ML-driven quant research workflow, which is why it remains extremely widely referenced and starred.

✅ *Good at:* Excellent as a structured, end-to-end curriculum and working code reference for building an ML-based quant research pipeline from scratch.  
⚠️ *Limitations:* It's a book's companion codebase rather than an installable library/framework, so integrating pieces into a production system takes extra work.

**[FinRL](https://github.com/AI4Finance-Foundation/FinRL)** · Jupyter Notebook · ★ 16.4k · last push 2026-07-13  
FinRL is a deep-reinforcement-learning library for automated trading in quantitative finance (published at NeurIPS 2020), providing standardized market environments (Gym-compatible), state-of-the-art RL algorithm wrappers (PPO, DDPG, SAC, etc. via ElegantRL/Stable-Baselines3/RLlib), and end-to-end tutorials for stock, portfolio-allocation, and crypto trading tasks. It positions itself explicitly as a benchmark/research framework for RL-in-finance rather than a production backtester, and its companion FinRL-Meta project supplies additional standardized, diverse market simulation environments and datasets.

✅ *Good at:* The standard starting point for anyone researching deep reinforcement learning applied to trading/portfolio management, with ready-made environments and baselines.  
⚠️ *Limitations:* RL trading strategies trained on FinRL environments are notoriously prone to overfitting historical data and rarely transfer directly to live trading without significant extra validation.

**[gs-quant](https://github.com/goldmansachs/gs-quant)** · Python · ★ 13.0k · last push 2026-09-16  
gs-quant is Goldman Sachs' open-source Python toolkit for quantitative finance, providing derivatives pricing and risk (via the Goldman Sachs Marquee platform APIs), portfolio construction, risk analytics, backtesting utilities for systematic strategies, and data-science tooling used internally by Goldman's own quants. It can run purely locally for pricing/analytics that don't require Marquee data, or connect to Marquee for institutional market data and execution. It's notable as one of the only major sell-side banks to open-source a substantial slice of its internal quant tooling.

✅ *Good at:* Valuable for derivatives pricing/risk workflows and institutional-grade portfolio construction and backtesting utilities modeled on real bank quant practice.  
⚠️ *Limitations:* Many of the most useful data and pricing features require a (paid) Marquee API entitlement; the fully free local functionality is narrower.

**[FinRL-Meta](https://github.com/AI4Finance-Foundation/FinRL-Meta)** · Python · ★ 1.9k · last push 2026-07-13  
FinRL-Meta provides a library of dynamic, diverse market datasets and simulation environments (equities, crypto, futures) designed to let researchers build and share standardized RL-for-trading benchmarks, complementing FinRL's algorithm/tutorial focus with a stronger emphasis on environment diversity and reproducibility. It supports data-driven market replay as well as some market-simulation approaches for more robust RL policy evaluation.

✅ *Good at:* Useful for benchmarking RL trading algorithms across a wider and more standardized set of market environments than FinRL's own tutorials provide.  
⚠️ *Limitations:* Same fundamental caveat as all RL-for-trading tooling: strong in-sample RL performance does not reliably indicate real-world edge.

**[asavinov/intelligent-trading-bot](https://github.com/asavinov/intelligent-trading-bot)** · Python · ★ 1.9k · last push 2026-08-30  
Intelligent Trading Bot is a framework for automatically generating trading signals based on machine learning and systematic feature engineering, covering the data-to-feature-to-model-to-signal pipeline for crypto and other markets, with an emphasis on high-level 'feature definition' abstractions rather than raw indicator scripting. It includes basic backtesting to evaluate generated signals.

✅ *Good at:* Good for exploring systematic ML feature-engineering-driven signal generation as an alternative to hand-coded indicator rules.  
⚠️ *Limitations:* Backtesting is secondary to the ML/feature-engineering focus and is less rigorous/configurable than dedicated backtesting engines.

**[AlphaPy](https://github.com/ScottfreeLLC/AlphaPy)** · Python · ★ 1.8k · last push 2025-08-24  
AlphaPy is an automated machine learning framework built on scikit-learn, Keras, XGBoost, LightGBM and CatBoost, configured via YAML files to run classification/regression pipelines for both financial market prediction and sports-betting-style prediction problems. It automates feature engineering, model selection/tuning, and blending/ensembling, and includes a market-specific data flow (via a companion pandas-datareader-style pipeline) for financial applications.

✅ *Good at:* Good for quickly standing up an AutoML pipeline for return/direction prediction without hand-rolling feature engineering and model-selection code.  
⚠️ *Limitations:* AutoML pipelines like this can easily overfit financial data if used without careful walk-forward validation, which AlphaPy doesn't enforce by default.

**[QuantSoftware Toolkit](https://github.com/QuantSoftware/QuantSoftwareToolkit)** · HTML · ★ 480 · last push 2017-10-02  
QuantSoftware Toolkit is an early open-source Python framework designed to support portfolio construction and management, developed out of Georgia Tech's computational finance coursework (the basis for the well-known 'Machine Learning for Trading' CS7646 course before it moved to other tooling). It predates most modern backtesting libraries and is now purely of historical/educational interest.

✅ *Good at:* Historical interest for those following the original Georgia Tech CS7646 course materials.  
⚠️ *Limitations:* Abandoned since 2017 and built on very old Python conventions; not suitable for new projects.

**[Trading Strategy (tradingstrategy.ai)](https://github.com/tradingstrategy-ai/getting-started)** · Jupyter Notebook · ★ 250 · last push 2026-09-19  
Trading Strategy (tradingstrategy.ai) is a market data, backtesting, live trading and investor-management framework specifically for decentralized finance (DeFi), indexing on-chain DEX trade/liquidity data across many blockchains and exposing it through a Python SDK with backtesting notebooks. It fills a niche largely unaddressed by traditional backtesting engines: realistic simulation of DEX-based strategies including liquidity-pool dynamics and on-chain execution costs.

✅ *Good at:* The most complete open option for backtesting DeFi/DEX trading strategies with real on-chain historical data.  
⚠️ *Limitations:* Focused specifically on DeFi/on-chain markets, so it doesn't help with traditional equities/futures/FX backtesting.

</details>

### Factor research

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**mlfinlab**](https://github.com/hudson-and-thames/mlfinlab) | 4.9k | Python | 🔴 | The canonical reference implementation of López de Prado's financial data structures, labeling and leakage-aware cross-validation techniques. |
| [**alphalens**](https://github.com/quantopian/alphalens) | 4.4k | Jupyter Notebook | 🔴 | The reference tool for evaluating whether a candidate alpha factor has genuine predictive power (IC, quantile spreads, decay) before building a full strategy around it. |
| [**firmai/machine-learning-asset-management**](https://github.com/firmai/machine-learning-asset-management) | 1.8k | Jupyter Notebook | 🔴 | Useful as a curated survey of ML techniques applied to asset management/factor investing, for discovering approaches and papers. |
| [**alphalens-reloaded**](https://github.com/stefan-jansen/alphalens-reloaded) | 652 | Python | 🟢 | The current standard tool for factor/signal predictive-power evaluation (IC, quantile spreads, turnover, decay) on a modern Python stack. |
| [**FactorAnalytics (R)**](https://github.com/braverock/FactorAnalytics) | 85 | R | 🟡 | Useful R-native tooling for fitting and comparing fundamental, time-series and statistical factor models feeding into risk/portfolio work. |
| [**covFactorModel (R)**](https://github.com/dppalomar/covFactorModel) | 39 | R | 🟡 | Useful as a lightweight R tool for factor-model-based covariance estimation feeding into downstream portfolio optimization. |

<details><summary>Explainers (6)</summary>

**[mlfinlab](https://github.com/hudson-and-thames/mlfinlab)** · Python · ★ 4.9k · last push 2023-10-02  
mlfinlab implements the techniques described in Marcos Lopez de Prado's 'Advances in Financial Machine Learning', including financial data structures (dollar/volume/tick bars), fractional differentiation, triple-barrier labeling, meta-labeling, sample-weighting for overlapping labels, and purged/embargoed cross-validation designed to avoid the leakage that plagues naive financial ML backtests. It was extremely influential in popularizing rigorous financial-ML methodology, though the open-source repo's most advanced features were eventually moved behind Hudson & Thames' commercial PortfolioLab/ArbitrageLab/etc. products, and the free repo itself is no longer actively updated.

✅ *Good at:* The canonical reference implementation of López de Prado's financial data structures, labeling and leakage-aware cross-validation techniques.  
⚠️ *Limitations:* No longer actively maintained as free/open source, and many of the most advanced techniques from the book now live only in Hudson & Thames' paid products.

**[alphalens](https://github.com/quantopian/alphalens)** · Jupyter Notebook · ★ 4.4k · last push 2024-02-12  
alphalens is Quantopian's library for performance analysis of predictive alpha factors, computing information coefficient (IC), factor-quantile return spreads, turnover, and factor decay analysis to judge whether a proposed signal actually predicts future returns before committing it to a full backtest. It became the standard tool for the 'factor research' step that precedes strategy construction in the Quantopian-style workflow, and its quantile-return-tearsheet format is still the template most factor-research tools imitate.

✅ *Good at:* The reference tool for evaluating whether a candidate alpha factor has genuine predictive power (IC, quantile spreads, decay) before building a full strategy around it.  
⚠️ *Limitations:* Unmaintained and increasingly pandas-incompatible; use alphalens-reloaded instead for current work.

**[firmai/machine-learning-asset-management](https://github.com/firmai/machine-learning-asset-management)** · Jupyter Notebook · ★ 1.8k · last push 2021-12-17  
This repository is a curated collection of machine-learning techniques and code applied to asset management and factor investing (return prediction, portfolio construction, risk modeling), assembled by FirmAI as a companion reference to their broader machine-learning-for-finance curation work. It functions as a reading list plus example code rather than an installable library.

✅ *Good at:* Useful as a curated survey of ML techniques applied to asset management/factor investing, for discovering approaches and papers.  
⚠️ *Limitations:* Not maintained since 2021 and not a reusable library; it's a reference/survey collection.

**[alphalens-reloaded](https://github.com/stefan-jansen/alphalens-reloaded)** · Python · ★ 652 · last push 2025-12-15  
alphalens-reloaded is the maintained continuation of Quantopian's alphalens, providing the same IC/quantile-return/turnover/decay factor-evaluation tearsheets updated for modern pandas, and used throughout Stefan Jansen's Machine Learning for Trading examples alongside zipline-reloaded and pyfolio-reloaded.

✅ *Good at:* The current standard tool for factor/signal predictive-power evaluation (IC, quantile spreads, turnover, decay) on a modern Python stack.  
⚠️ *Limitations:* Feature set is essentially frozen at parity with the original alphalens rather than expanding with new factor-evaluation techniques.

**[FactorAnalytics (R)](https://github.com/braverock/FactorAnalytics)** · R · ★ 85 · last push 2024-12-12  
FactorAnalytics provides fitting and analysis methods for the three main classes of factor models used in portfolio construction, optimization and risk management: fundamental factor models, time-series factor models, and statistical factor models. It's part of the same R/Finance family as PerformanceAnalytics, PortfolioAnalytics, blotter and quantstrat.

✅ *Good at:* Useful R-native tooling for fitting and comparing fundamental, time-series and statistical factor models feeding into risk/portfolio work.  
⚠️ *Limitations:* Development has slowed and the R factor-modeling ecosystem is much smaller than Python's (e.g. Qlib, Spectre).

**[covFactorModel (R)](https://github.com/dppalomar/covFactorModel)** · R · ★ 39 · last push 2019-03-25  
covFactorModel provides covariance matrix estimation via statistical and fundamental factor models in R, a foundational building block for risk models used in portfolio optimization and risk parity. It comes from the same ConvexFi research group as riskParityPortfolio and sparseIndexTracking.

✅ *Good at:* Useful as a lightweight R tool for factor-model-based covariance estimation feeding into downstream portfolio optimization.  
⚠️ *Limitations:* Not actively developed (last updated 2019) and narrowly scoped to covariance estimation only.

</details>

### Performance analytics & tearsheets

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**quantstats**](https://github.com/ranaroussi/quantstats) | 7.6k | Python | 🟢 | The default choice for generating a polished, standard performance tearsheet from any returns series regardless of which backtesting engine produced it. |
| [**pyfolio**](https://github.com/quantopian/pyfolio) | 6.4k | Jupyter Notebook | 🔴 | Historically the gold-standard for rigorous, multi-faceted backtest tearsheets (risk, exposure, turnover) beyond simple return metrics. |
| [**ffn**](https://github.com/pmorissette/ffn) | 2.7k | Python | 🟢 | A solid lightweight choice for quick performance-statistics computation and reporting, especially if already using `bt`. |
| [**empyrical**](https://github.com/quantopian/empyrical) | 1.5k | Python | 🔴 | Useful as a lightweight, dependency-light source of standard performance-metric functions to build custom reporting on top of. |
| [**EigenLedger**](https://github.com/santoshlite/EigenLedger) | 1.1k | Python | 🟢 | Good for a quick, integrated portfolio backtest + optimization + risk report without stitching together multiple separate libraries. |
| [**QuantInvestStrats (qis)**](https://github.com/ArturSepp/QuantInvestStrats) | 634 | Python | 🟢 | Good for producing institutional-style factsheet reporting and risk analysis on top of an existing return series or simple backtest. |
| [**pyfolio-reloaded**](https://github.com/stefan-jansen/pyfolio-reloaded) | 616 | Jupyter Notebook | 🟢 | Best current option for teams that want pyfolio's classic detailed tearsheet style on a modern, working Python environment. |
| [**PerformanceAnalytics (R)**](https://github.com/braverock/PerformanceAnalytics) | 239 | R | 🟢 | The R-language equivalent of quantstats/pyfolio for rigorous return-series performance and risk analysis, with unusually deep coverage of academic risk/performance measures. |
| [**empyrical-reloaded**](https://github.com/stefan-jansen/empyrical-reloaded) | 122 | Python | 🟢 | The standard current choice for a dependency-light library of standard performance/risk metric functions. |
| [**jquantstats**](https://github.com/Jebel-Quant/jquantstats) | 44 | Python | 🟢 | Worth watching as a modern alternative to quantstats if you want the same tearsheet workflow with a fresher codebase. |
| [**RiskPerf.jl**](https://github.com/rbeeli/RiskPerf.jl) | 17 | Julia | 🟢 | The natural pairing with Fastback.jl for Julia-native quants who want performance/risk metrics without a Python dependency. |
| [**fincore**](https://github.com/cloudQuant/fincore) | 4 | Python | 🟢 | Worth tracking as a potential modern, actively maintained alternative to the empyrical/pyfolio family, especially for cloudQuant-backtrader users. |

<details><summary>Explainers (12)</summary>

**[quantstats](https://github.com/ranaroussi/quantstats)** · Python · ★ 7.6k · last push 2026-07-20  
QuantStats is the most widely used Python library for portfolio performance and risk analytics, generating a comprehensive HTML/PDF 'tearsheet' (Sharpe/Sortino/Calmar, drawdowns, rolling volatility, monthly return heatmaps, benchmark comparison, etc.) from a simple returns series, with almost no setup required. Because nearly every backtesting engine ultimately produces a returns/equity series, quantstats has become the de facto universal reporting layer bolted on top of backtrader, vectorbt, Zipline-derived tools, and custom backtests alike. Its simplicity and polished default reports are the main reason for its dominance over more academically thorough but less turnkey alternatives.

✅ *Good at:* The default choice for generating a polished, standard performance tearsheet from any returns series regardless of which backtesting engine produced it.  
⚠️ *Limitations:* Primarily reports on realized returns rather than deep factor/risk attribution, so it's often paired with pyfolio/alphalens/Riskfolio-Lib for deeper analysis.

**[pyfolio](https://github.com/quantopian/pyfolio)** · Jupyter Notebook · ★ 6.4k · last push 2023-12-23  
pyfolio is Quantopian's portfolio and risk analytics library, producing detailed tearsheets covering returns, risk (drawdown, VaR, tail ratios), position and exposure analysis, transaction/turnover analysis, and Bayesian performance estimation, designed to plug directly into zipline backtest output. It was, alongside empyrical and alphalens, part of the core Quantopian research stack and remains conceptually influential even though the original repo is no longer maintained since Quantopian's shutdown.

✅ *Good at:* Historically the gold-standard for rigorous, multi-faceted backtest tearsheets (risk, exposure, turnover) beyond simple return metrics.  
⚠️ *Limitations:* Unmaintained and increasingly incompatible with modern pandas; use pyfolio-reloaded instead for anything new.

**[ffn](https://github.com/pmorissette/ffn)** · Python · ★ 2.7k · last push 2026-09-20  
ffn is a general financial function library for Python from the author of `bt`, providing performance statistics, data manipulation helpers, and a convenient `GroupStats`/`PerformanceStats` reporting object that computes a broad set of standard return/risk metrics and can render simple performance reports and plots. It underlies `bt`'s reporting layer but is also commonly used standalone.

✅ *Good at:* A solid lightweight choice for quick performance-statistics computation and reporting, especially if already using `bt`.  
⚠️ *Limitations:* Less visually polished/comprehensive as a tearsheet generator compared to quantstats or pyfolio.

**[empyrical](https://github.com/quantopian/empyrical)** · Python · ★ 1.5k · last push 2024-07-26  
empyrical is a focused library of common financial risk and performance metric calculations (Sharpe, Sortino, max drawdown, alpha/beta, Calmar, VaR, etc.) originally extracted from Quantopian's Zipline/pyfolio stack so those metric functions could be reused independently. It underlies both pyfolio and quantstats-style reporting, functioning as the low-level metrics building block rather than a report generator itself.

✅ *Good at:* Useful as a lightweight, dependency-light source of standard performance-metric functions to build custom reporting on top of.  
⚠️ *Limitations:* No longer actively maintained by the original team; empyrical-reloaded and fincore are the maintained successors.

**[EigenLedger](https://github.com/santoshlite/EigenLedger)** · Python · ★ 1.1k · last push 2025-09-14  
EigenLedger (formerly Empyrial) is an open-source portfolio backtesting engine combining performance/risk analysis with portfolio optimization in a single accessible package, aimed at both retail investors and financial institutions who want a turnkey 'analyze my portfolio' workflow rather than assembling separate metrics, optimization and reporting libraries. It renders results as an easy-to-read report similar in spirit to quantstats but with an optimization layer included.

✅ *Good at:* Good for a quick, integrated portfolio backtest + optimization + risk report without stitching together multiple separate libraries.  
⚠️ *Limitations:* Less deep/customizable than combining dedicated tools (Riskfolio-Lib + quantstats) for advanced use cases.

**[QuantInvestStrats (qis)](https://github.com/ArturSepp/QuantInvestStrats)** · Python · ★ 634 · last push 2026-09-20  
QIS is a performance-analytics-focused Python library providing portfolio backtesting, risk analysis, and factsheet-style reporting, from an author (Artur Sepp) who also maintains several related trend-following and optimal-portfolio research repositories. It emphasizes producing publication-quality factsheets and risk decomposition rather than being a general-purpose event-driven backtester.

✅ *Good at:* Good for producing institutional-style factsheet reporting and risk analysis on top of an existing return series or simple backtest.  
⚠️ *Limitations:* Smaller community and narrower scope than quantstats/pyfolio; best paired with the author's related OptimalPortfolios/TrendFollowingSystems repos.

**[pyfolio-reloaded](https://github.com/stefan-jansen/pyfolio-reloaded)** · Jupyter Notebook · ★ 616 · last push 2025-12-15  
pyfolio-reloaded is the community-maintained continuation of Quantopian's pyfolio, updated for modern pandas/numpy compatibility while preserving the original detailed tearsheet functionality (returns, risk, position/exposure, transaction analysis). It is maintained by the same team behind zipline-reloaded and empyrical-reloaded, forming a coherent modernized version of the whole Quantopian analysis stack.

✅ *Good at:* Best current option for teams that want pyfolio's classic detailed tearsheet style on a modern, working Python environment.  
⚠️ *Limitations:* Development pace is modest; feature set is essentially frozen at parity with the original pyfolio rather than expanding significantly.

**[PerformanceAnalytics (R)](https://github.com/braverock/PerformanceAnalytics)** · R · ★ 239 · last push 2026-04-13  
PerformanceAnalytics is a long-standing, comprehensive R package of econometric tools for performance and risk analysis of financial return series, covering drawdown analysis, downside risk measures, higher-moment risk (skew/kurtosis-aware VaR), and dozens of standard and specialized performance ratios. It has been a foundational package in the R/Finance community for over a decade and underpins many other R packages including PortfolioAnalytics and blotter-based workflows.

✅ *Good at:* The R-language equivalent of quantstats/pyfolio for rigorous return-series performance and risk analysis, with unusually deep coverage of academic risk/performance measures.  
⚠️ *Limitations:* R-only, and its API reflects R/Finance conventions from the mid-2000s-2010s rather than a modern tidyverse-style interface.

**[empyrical-reloaded](https://github.com/stefan-jansen/empyrical-reloaded)** · Python · ★ 122 · last push 2025-12-12  
empyrical-reloaded is the maintained fork of Quantopian's empyrical, providing the same standard suite of return/risk metric functions (Sharpe, Sortino, drawdown, VaR, alpha/beta) updated for compatibility with current pandas/numpy, and used as the metrics backbone for pyfolio-reloaded and other reloaded-family tools.

✅ *Good at:* The standard current choice for a dependency-light library of standard performance/risk metric functions.  
⚠️ *Limitations:* Purely a metrics library, not a report generator, so it needs to be paired with something like pyfolio-reloaded or quantstats for visual tearsheets.

**[jquantstats](https://github.com/Jebel-Quant/jquantstats)** · Python · ★ 44 · last push 2026-09-19  
jquantstats is a modern reimplementation of quantstats' tearsheet/analytics functionality with additional features and performance improvements, aimed at users who like quantstats' report style but want a more actively refactored/modern codebase. It is new and small but directly targets the exact same well-understood use case as quantstats.

✅ *Good at:* Worth watching as a modern alternative to quantstats if you want the same tearsheet workflow with a fresher codebase.  
⚠️ *Limitations:* Very new and small community; quantstats remains the far more battle-tested default.

**[RiskPerf.jl](https://github.com/rbeeli/RiskPerf.jl)** · Julia · ★ 17 · last push 2026-09-05  
RiskPerf.jl is a quantitative risk and performance analysis package for financial time series in Julia, providing standard return/risk metric computations (analogous to empyrical/PerformanceAnalytics) natively in the Julia ecosystem, from the same author as Fastback.jl.

✅ *Good at:* The natural pairing with Fastback.jl for Julia-native quants who want performance/risk metrics without a Python dependency.  
⚠️ *Limitations:* Very small community; far less battle-tested than empyrical/quantstats.

**[fincore](https://github.com/cloudQuant/fincore)** · Python · ★ 4 · last push 2026-09-20  
fincore is a new, actively developed quantitative performance and risk analytics library billed as a modern successor to empyrical/pyfolio, offering 150+ metrics, portfolio optimization routines, Monte Carlo simulation and attribution analysis in one package, from the same team behind the cloudQuant backtrader fork. Being brand new, it has essentially no adoption yet but is worth watching given its lineage.

✅ *Good at:* Worth tracking as a potential modern, actively maintained alternative to the empyrical/pyfolio family, especially for cloudQuant-backtrader users.  
⚠️ *Limitations:* Extremely new with almost no community validation or track record yet.

</details>

### Portfolio optimization

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**PyPortfolioOpt**](https://github.com/PyPortfolio/PyPortfolioOpt) | 6.0k | Jupyter Notebook | 🟢 | The default first choice for portfolio construction/allocation problems in Python, from simple mean-variance to Black-Litterman and HRP. |
| [**Riskfolio-Lib**](https://github.com/dcajasn/Riskfolio-Lib) | 4.5k | C++ | 🟢 | Best when you need advanced/exotic risk measures (CVaR, CDaR, EVaR, risk parity, hierarchical clustering allocation) beyond classical mean-variance. |
| [**Eiten**](https://github.com/tradytics/eiten) | 3.3k | Python | 🔴 | Good for comparing several distinct portfolio-construction philosophies (eigen, min-variance, max-Sharpe, genetic) side by side quickly. |
| [**skfolio**](https://github.com/skfolio/skfolio) | 2.4k | Python | 🟢 | Best for teams already working in the scikit-learn ecosystem who want portfolio optimization to compose naturally with sklearn pipelines, cross-validation and grid search. |
| [**FinQuant**](https://github.com/fmilthaler/FinQuant) | 1.8k | Python | 🟡 | Good as an approachable, beginner-friendly entry point to portfolio optimization and Monte Carlo portfolio analysis. |
| [**cvxportfolio**](https://github.com/cvxgrp/cvxportfolio) | 1.3k | Python | 🟢 | Best when transaction-cost- and market-impact-aware multi-period optimization (not just single-period efficient frontier) is the core requirement. |
| [**deepdow**](https://github.com/jankrepl/deepdow) | 1.2k | Python | 🟡 | Good for researchers exploring end-to-end differentiable portfolio-allocation network architectures rather than a two-stage predict-then-optimize pipeline. |
| [**universal-portfolios**](https://github.com/Marigold/universal-portfolios) | 862 | Jupyter Notebook | 🟢 | The main open-source home for online portfolio-selection algorithms (Cover's Universal Portfolio and similar), a distinct academic tradition from classical Markowitz optimization. |
| [**riskparity.py**](https://github.com/convexfi/riskparity.py) | 325 | Python | 🟢 | Good when risk-parity allocation specifically, at scale, with fast convergence, is the primary requirement. |
| [**fortitudo.tech**](https://github.com/fortitudo-tech/fortitudo.tech) | 310 | Python | 🟢 | Good for practitioners specifically wanting Entropy Pooling-based views incorporation combined with CVaR optimization, an approach not covered by most other portfolio-optimization libraries. |
| [**riskParityPortfolio (R)**](https://github.com/dppalomar/riskParityPortfolio) | 122 | R | 🟡 | The standard R option for fast risk-parity portfolio construction, for teams working in R rather than Python. |
| [**PortfolioAnalytics (R)**](https://github.com/braverock/PortfolioAnalytics) | 106 | R | 🟢 | The standard R package for flexible, constraint-driven portfolio optimization when off-the-shelf mean-variance solvers aren't flexible enough. |
| [**sparseIndexTracking (R)**](https://github.com/dppalomar/sparseIndexTracking) | 59 | HTML | 🟡 | Purpose-built for cost-efficient, sparse index-replication portfolio design, a specific need not addressed by general portfolio-optimization libraries. |

<details><summary>Explainers (13)</summary>

**[PyPortfolioOpt](https://github.com/PyPortfolio/PyPortfolioOpt)** · Jupyter Notebook · ★ 6.0k · last push 2026-07-07  
PyPortfolioOpt is the most widely used Python library for portfolio optimization, covering classical mean-variance/efficient-frontier optimization, Black-Litterman views-based allocation, Hierarchical Risk Parity (HRP), CVaR/semivariance objectives, and shrinkage-based covariance estimation, all behind a clean, well-documented scikit-learn-like API. Its combination of breadth, approachable API design and thorough documentation has made it the standard starting point for anyone doing portfolio construction in Python, well beyond just quant hedge funds.

✅ *Good at:* The default first choice for portfolio construction/allocation problems in Python, from simple mean-variance to Black-Litterman and HRP.  
⚠️ *Limitations:* Focuses on single-period, largely static optimization; multi-period, transaction-cost-aware optimization (as in cvxportfolio) is out of scope.

**[Riskfolio-Lib](https://github.com/dcajasn/Riskfolio-Lib)** · C++ · ★ 4.5k · last push 2026-08-18  
Riskfolio-Lib is a comprehensive portfolio optimization and quantitative strategic asset allocation library implementing an unusually wide range of risk measures (variance, CVaR, CDaR, EVaR, worst-case, and many more) and optimization models (mean-risk, risk parity, hierarchical clustering-based, ownership/nested clustering optimization, Black-Litterman variants), going well beyond the classical mean-variance/HRP scope of PyPortfolioOpt. It is actively developed with frequent releases and has become the preferred tool for practitioners who need more exotic risk measures or constraint types than PyPortfolioOpt supports.

✅ *Good at:* Best when you need advanced/exotic risk measures (CVaR, CDaR, EVaR, risk parity, hierarchical clustering allocation) beyond classical mean-variance.  
⚠️ *Limitations:* Larger API surface and more parameters to understand than PyPortfolioOpt, with a somewhat steeper learning curve.

**[Eiten](https://github.com/tradytics/eiten)** · Python · ★ 3.3k · last push 2022-07-30  
Eiten, from Tradytics, is an open-source toolkit implementing several statistical/algorithmic portfolio-construction approaches beyond classical mean-variance: Eigen Portfolios (PCA-based), Minimum Variance Portfolios, Maximum Sharpe Ratio Portfolios, and Genetic Algorithm-based portfolio search, all in one comparative toolkit. It's popular as an accessible introduction to a diverse set of allocation philosophies rather than depth in any single one.

✅ *Good at:* Good for comparing several distinct portfolio-construction philosophies (eigen, min-variance, max-Sharpe, genetic) side by side quickly.  
⚠️ *Limitations:* No longer actively maintained, and each individual method is less deeply developed than in specialist libraries like Riskfolio-Lib.

**[skfolio](https://github.com/skfolio/skfolio)** · Python · ★ 2.4k · last push 2026-09-20  
skfolio is a portfolio-optimization library built directly on top of scikit-learn's estimator/pipeline API, so portfolio models can be composed, cross-validated, grid-searched and combined with scikit-learn preprocessing/feature steps exactly like any other sklearn estimator. It covers mean-risk, risk-budgeting, and clustering-based (HRP/HERC) allocation methods, along with proper walk-forward and cross-validation tooling adapted for the non-i.i.d. nature of financial return series. This design makes it unusually easy to plug into existing sklearn-based ML research pipelines.

✅ *Good at:* Best for teams already working in the scikit-learn ecosystem who want portfolio optimization to compose naturally with sklearn pipelines, cross-validation and grid search.  
⚠️ *Limitations:* Newer and smaller community than PyPortfolioOpt/Riskfolio-Lib, though growing quickly.

**[FinQuant](https://github.com/fmilthaler/FinQuant)** · Python · ★ 1.8k · last push 2023-11-04  
FinQuant is a program for financial portfolio management, analysis and optimization, combining efficient-frontier-style optimization with Monte Carlo simulation of possible portfolios and standard performance/risk metric reporting in one approachable package aimed at individual investors and students. It is less feature-rich than PyPortfolioOpt/Riskfolio-Lib but has a simpler, more beginner-friendly API.

✅ *Good at:* Good as an approachable, beginner-friendly entry point to portfolio optimization and Monte Carlo portfolio analysis.  
⚠️ *Limitations:* Development has slowed and its feature set is narrower than PyPortfolioOpt or Riskfolio-Lib.

**[cvxportfolio](https://github.com/cvxgrp/cvxportfolio)** · Python · ★ 1.3k · last push 2026-04-27  
cvxportfolio is a portfolio optimization and backtesting library from Stanford's convex optimization group (Stephen Boyd's lab), implementing the multi-period portfolio optimization framework described in Boyd et al.'s papers/book, with explicit, realistic modeling of transaction costs, holding costs and market-impact terms as part of the optimization objective rather than as an afterthought. It ships its own lightweight backtesting simulator specifically designed to evaluate multi-period optimization policies under realistic cost assumptions.

✅ *Good at:* Best when transaction-cost- and market-impact-aware multi-period optimization (not just single-period efficient frontier) is the core requirement.  
⚠️ *Limitations:* More mathematically demanding (requires comfort with convex optimization formulations) than PyPortfolioOpt/Riskfolio-Lib's higher-level APIs.

**[deepdow](https://github.com/jankrepl/deepdow)** · Python · ★ 1.2k · last push 2024-01-24  
deepdow connects portfolio optimization with deep learning, letting users design and train neural networks that output portfolio weights directly in a single differentiable forward pass (rather than a separate prediction step followed by a classical optimizer), with built-in backtesting utilities for evaluating the resulting allocation policies. It supports several differentiable allocation layers (e.g. softmax, analytical mean-variance layers) that can be embedded inside a larger network architecture.

✅ *Good at:* Good for researchers exploring end-to-end differentiable portfolio-allocation network architectures rather than a two-stage predict-then-optimize pipeline.  
⚠️ *Limitations:* Development has slowed, and end-to-end learned allocation policies carry the same overfitting/generalization risks as other deep-learning-for-finance approaches.

**[universal-portfolios](https://github.com/Marigold/universal-portfolios)** · Jupyter Notebook · ★ 862 · last push 2026-07-31  
universal-portfolios is a collection of algorithms for online portfolio selection, an academic subfield concerned with sequentially updating portfolio weights period-by-period to achieve strong worst-case or universal performance guarantees (e.g. Cover's Universal Portfolio, exponential-gradient, and other online-learning-derived allocation algorithms), rather than the classical batch mean-variance framework. It's a useful bridge between the online-learning/regret-minimization literature and practical portfolio backtesting.

✅ *Good at:* The main open-source home for online portfolio-selection algorithms (Cover's Universal Portfolio and similar), a distinct academic tradition from classical Markowitz optimization.  
⚠️ *Limitations:* Niche academic focus; less directly applicable to typical discretionary or ML-driven strategy construction.

**[riskparity.py](https://github.com/convexfi/riskparity.py)** · Python · ★ 325 · last push 2026-08-31  
riskparity.py provides fast, scalable algorithms specifically for designing risk parity portfolios (equalizing risk contribution across assets/asset classes), an allocation approach popularized by funds like Bridgewater's All Weather strategy. It focuses narrowly and deeply on solving the risk-parity optimization problem efficiently at scale, complementing broader libraries like Riskfolio-Lib that support risk parity as one option among many.

✅ *Good at:* Good when risk-parity allocation specifically, at scale, with fast convergence, is the primary requirement.  
⚠️ *Limitations:* Narrow single-purpose scope; needs to be combined with other tools for backtesting or broader risk analytics.

**[fortitudo.tech](https://github.com/fortitudo-tech/fortitudo.tech)** · Python · ★ 310 · last push 2026-08-20  
fortitudo.tech implements Conditional Value-at-Risk (CVaR) portfolio optimization together with Entropy Pooling, a flexible views/stress-testing framework popularized by Attilio Meucci for incorporating subjective and market-implied views into a scenario-based portfolio model without assuming normality. It targets practitioners who want views-based, tail-risk-aware allocation beyond mean-variance or plain CVaR minimization.

✅ *Good at:* Good for practitioners specifically wanting Entropy Pooling-based views incorporation combined with CVaR optimization, an approach not covered by most other portfolio-optimization libraries.  
⚠️ *Limitations:* Narrower, more specialized scope than PyPortfolioOpt/Riskfolio-Lib, requiring familiarity with the Entropy Pooling methodology.

**[riskParityPortfolio (R)](https://github.com/dppalomar/riskParityPortfolio)** · R · ★ 122 · last push 2022-11-15  
riskParityPortfolio is the R counterpart to riskparity.py, providing blazingly fast risk-parity portfolio design algorithms for R users, from the same academic optimization research group (Daniel Palomar's lab, ConvexFi). It's part of a small family of related R packages (sparseIndexTracking, covFactorModel) from the same group covering different portfolio-construction problems.

✅ *Good at:* The standard R option for fast risk-parity portfolio construction, for teams working in R rather than Python.  
⚠️ *Limitations:* Development has slowed and the R quant-finance ecosystem generally has fewer active maintainers than Python's.

**[PortfolioAnalytics (R)](https://github.com/braverock/PortfolioAnalytics)** · R · ★ 106 · last push 2026-09-19  
PortfolioAnalytics is an R package providing numerical methods and a flexible constraint/objective specification system for portfolio optimization, part of the long-running R/Finance ecosystem maintained by Brian Peterson's group (the same team behind quantstrat, blotter and PerformanceAnalytics). It supports custom objective functions and constraints beyond what closed-form mean-variance solvers allow, using random-portfolio and differential-evolution-based solvers among others.

✅ *Good at:* The standard R package for flexible, constraint-driven portfolio optimization when off-the-shelf mean-variance solvers aren't flexible enough.  
⚠️ *Limitations:* R-specific tooling with a smaller contributor base than the Python portfolio-optimization ecosystem.

**[sparseIndexTracking (R)](https://github.com/dppalomar/sparseIndexTracking)** · HTML · ★ 59 · last push 2023-05-28  
sparseIndexTracking solves the specific portfolio-construction problem of designing a sparse portfolio (using only a subset of the index's constituents) that closely tracks a target index, which is a common practical need for cost-efficient index/ETF replication. It's a niche but well-implemented R package from the ConvexFi optimization research group.

✅ *Good at:* Purpose-built for cost-efficient, sparse index-replication portfolio design, a specific need not addressed by general portfolio-optimization libraries.  
⚠️ *Limitations:* Very narrow scope (index tracking only) and R-only, with modest recent activity.

</details>

### Data tooling

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**OpenBB**](https://github.com/OpenBB-finance/OpenBB) | 73.3k | Python | 🟢 | Best as a unified, extensible data layer and research terminal to pair with a dedicated backtesting engine, rather than as the backtester itself. |
| [**tidyquant (R)**](https://github.com/business-science/tidyquant) | 915 | R | 🟢 | Best for R users who want financial data retrieval and standard performance analytics in an idiomatic, pipe-friendly tidyverse workflow. |

<details><summary>Explainers (2)</summary>

**[OpenBB](https://github.com/OpenBB-finance/OpenBB)** · Python · ★ 73.3k · last push 2026-09-19  
OpenBB is an open-source financial data and research platform combining a Python SDK, a CLI/terminal UI, and a local REST API, with a large extensible-provider architecture that unifies many free and paid data sources (equities, options, macro, crypto) behind a consistent interface. It is primarily a data-access and research-workbench layer rather than a backtesting engine itself, but it is frequently used as the data-fetching front end that feeds into backtesting frameworks like vectorbt, backtrader or Qlib. It has grown into one of the largest and most visible open-source projects in the whole quant-finance space.

✅ *Good at:* Best as a unified, extensible data layer and research terminal to pair with a dedicated backtesting engine, rather than as the backtester itself.  
⚠️ *Limitations:* Not a backtesting engine on its own; many premium data providers still require paid API keys, and the extension ecosystem can be heavy to configure.

**[tidyquant (R)](https://github.com/business-science/tidyquant)** · R · ★ 915 · last push 2026-09-01  
tidyquant bridges financial analysis and the tidyverse, bringing together market data retrieval, xts/zoo/quantmod/TTR-style functions, and PerformanceAnalytics performance metrics into a consistent tibble-based, pipe-friendly (`%>%`) interface. It's the main reason R users doing modern tidyverse-style data analysis can do financial time-series and performance work without leaving that idiom, and it's actively maintained by Business Science alongside companion packages timetk and tibbletime.

✅ *Good at:* Best for R users who want financial data retrieval and standard performance analytics in an idiomatic, pipe-friendly tidyverse workflow.  
⚠️ *Limitations:* Not a backtesting engine itself; it's a data/analytics convenience layer that still needs quantstrat or custom logic for actual strategy simulation.

</details>

### Lists & other

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**TradingAgents**](https://github.com/TauricResearch/TradingAgents) | 107.8k | Python | 🟢 | Interesting as a reference architecture for structuring LLM-based multi-agent investment debate/analysis pipelines, and as a starting point for LLM-augmented research workflows. |
| [**je-suis-tm/quant-trading**](https://github.com/je-suis-tm/quant-trading) | 10.8k | Python | 🟢 | Great as a library of worked strategy examples to learn from or adapt, especially for classic technical/statistical-arbitrage strategy patterns. |
| [**mplfinance**](https://github.com/matplotlib/mplfinance) | 4.4k | Python | 🟡 | The standard choice for producing publication-quality candlestick/OHLC charts from pandas OHLCV data in Python. |
| [**finplot**](https://github.com/highfestiva/finplot) | 1.2k | Python | 🟢 | Good for fast, interactive charting of large historical datasets during backtest research, where matplotlib feels sluggish. |

<details><summary>Explainers (4)</summary>

**[TradingAgents](https://github.com/TauricResearch/TradingAgents)** · Python · ★ 107.8k · last push 2026-09-18  
TradingAgents is a multi-agent financial research framework where separate LLM agents specialize in fundamental, technical, news and sentiment analysis, then hold a structured investment debate (bull/bear-style) and risk assessment before producing a trading decision, reproducing a research paper's multi-agent trading pipeline. It is not a backtesting engine in the traditional sense; it is a decision/analysis pipeline that can be pointed at historical or live data. Its star count has grown extremely fast, consistent with the broader 2025-2026 wave of high-visibility LLM-agent trading demos, and it should be evaluated as a research/agent-orchestration framework rather than a validated trading system.

✅ *Good at:* Interesting as a reference architecture for structuring LLM-based multi-agent investment debate/analysis pipelines, and as a starting point for LLM-augmented research workflows.  
⚠️ *Limitations:* Not a rigorous backtesting engine with realistic execution/cost modeling, and its rapid star growth (far outpacing much older, more battle-tested projects) warrants skepticism about how representative that popularity is of production usefulness.

**[je-suis-tm/quant-trading](https://github.com/je-suis-tm/quant-trading)** · Python · ★ 10.8k · last push 2026-06-20  
This is a large, popular collection of individually implemented and backtested trading strategies (pairs trading, Bollinger Bands, VIX-based, Heikin-Ashi, London breakout, and dozens more) each as a self-contained script/notebook with its own backtest and chart, rather than a unified framework. Its value is breadth of worked examples across many classic technical/statistical strategy families, making it a popular reference for learning how a given strategy idea is typically coded and evaluated.

✅ *Good at:* Great as a library of worked strategy examples to learn from or adapt, especially for classic technical/statistical-arbitrage strategy patterns.  
⚠️ *Limitations:* Not a reusable framework: each strategy is a standalone script with its own ad hoc backtest logic rather than a shared, tested engine.

**[mplfinance](https://github.com/matplotlib/mplfinance)** · Python · ★ 4.4k · last push 2024-08-08  
mplfinance is the official matplotlib utilities package for visualizing and visually analyzing financial data (candlestick, OHLC, renko, point-and-figure charts with volume and technical-indicator overlays), commonly used to render chart output from backtesting engines that don't have their own plotting layer. It's not a backtester itself but a near-universal charting dependency across the Python quant ecosystem.

✅ *Good at:* The standard choice for producing publication-quality candlestick/OHLC charts from pandas OHLCV data in Python.  
⚠️ *Limitations:* Static matplotlib-based plotting only; no interactivity compared to Plotly-based tools used by vectorbt or finplot.

**[finplot](https://github.com/highfestiva/finplot)** · Python · ★ 1.2k · last push 2026-03-30  
finplot is a performant, effortless finance-plotting library for Python built on PyQtGraph rather than matplotlib, aimed at fast, interactive rendering of large OHLCV datasets with indicator overlays, positioned as a lighter, snappier alternative to mplfinance for interactive exploration.

✅ *Good at:* Good for fast, interactive charting of large historical datasets during backtest research, where matplotlib feels sluggish.  
⚠️ *Limitations:* Smaller feature set and community than mplfinance or full charting platforms like TradingView's Lightweight Charts.

</details>

[⬆ back to top](#contents)

## Live trading, execution & brokers

Connectivity, order management and bots for running strategies live. For **Interactive Brokers**, the maintained
path is **ib_async** (successor to the archived ib_insync), with **ib-gateway-docker + IBC** for a headless gateway.
Use **NautilusTrader** or **LEAN** when you want a full engine with IBKR adapters, reconciliation and risk checks.

**Key takeaways**

- **alpaca-py** is a clean official SDK and a practical second venue or paper environment.
- In crypto, **freqtrade** (bots), **Hummingbot** (market making) and **CCXT** (exchange connectivity) are the de facto standards.
- Reserve FIX engines (the QuickFIX family) for venues that require FIX. Broker APIs cover most retail and small-fund needs.
- Gap: there is no widely adopted standalone TWAP/VWAP execution-algo library for equities. That logic lives inside the full platforms.

### Interactive Brokers

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**ib_insync**](https://github.com/erdewit/ib_insync) | 3.3k | Python | 🔴 | Historically the best-documented, most battle-tested IBKR Python wrapper; huge amount of example code and StackOverflow/tutorial coverage still exists under its name. |
| [**High-Frequency-Trading-Model-with-IB**](https://github.com/jamesmawm/High-Frequency-Trading-Model-with-IB) | 2.9k | Python | 🟡 | Learning the end-to-end shape of an IBKR-connected mean-reversion/pairs strategy, including basic risk and order management patterns. |
| [**ThetaGang**](https://github.com/brndnmtthws/thetagang) | 2.7k | Python | 🟢 | Turnkey automated wheel/covered-call/cash-secured-put strategy execution on IBKR accounts, with YAML-driven configuration. |
| [**ib_async**](https://github.com/ib-api-reloaded/ib_async) | 1.7k | Python | 🟢 | Rapid prototyping of IBKR strategies in Jupyter/scripts; clean object model for orders, positions, and streaming ticks/bars without hand-rolling the raw EClient/EWrapper callback API. |
| [**IbcAlpha/IBC**](https://github.com/IbcAlpha/IBC) | 1.6k | Java | 🟢 | Fully unattended IBKR Gateway/TWS operation: auto-login, auto-restart, auto-confirming order dialogs, and closing popups that would otherwise block headless automation. |
| [**gnzsnz/ib-gateway-docker**](https://github.com/gnzsnz/ib-gateway-docker) | 1.3k | Shell | 🟢 | Running a reliable, unattended IBKR Gateway in a container for 24/7 automated systems, with VNC access for 2FA setup and automatic daily restart handling. |
| [**rust-ibapi**](https://github.com/wboayue/rust-ibapi) | 385 | Rust | 🟢 | Low-overhead, memory-safe IBKR connectivity for latency-sensitive or embedded execution services written in Rust. |
| [**ezibpy**](https://github.com/ranaroussi/ezibpy) | 335 | Python | 🔴 | Simple synchronous helper functions for common IBKR order types when a full async framework is overkill. |
| [**UnusualAlpha/ib-gateway-docker**](https://github.com/UnusualAlpha/ib-gateway-docker) | 306 | Dockerfile | 🟢 | Lightweight headless IB Gateway containerization as an alternative to the more feature-heavy gnzsnz image. |
| [**hadrianl/ibapi (Go)**](https://github.com/hadrianl/ibapi) | 163 | Go | 🟡 | Reference implementation for Go IBKR clients predating scmhub/ibapi. |
| [**IB-Gateway Docker (UnusualAlpha alt.) / manhinhang variant**](https://github.com/manhinhang/ib-gateway-docker) | 110 | Shell | 🟢 | A minimal-footprint alternative when gnzsnz's more feature-rich image is heavier than needed. |
| [**interactive-brokers-api (REST wrapper)**](https://github.com/areed1192/interactive-brokers-api) | 103 | Python | 🟢 | Simple REST-based IBKR automation without the socket-protocol complexity of the TWS API. |
| [**scmhub/ibapi (Go)**](https://github.com/scmhub/ibapi) | 76 | Go | 🟢 | Native Go integration for teams building order-routing or risk services in Go rather than Python. |
| [**Jib.jl**](https://github.com/lbilli/Jib.jl) | 69 | Julia | 🟢 | Native IBKR connectivity for Julia-based quant research and execution stacks. |
| [**IB4m**](https://github.com/softwarespartan/IB4m) | 59 | MATLAB | 🟡 | Bridging MATLAB signal-processing/quant research code straight to IBKR execution. |
| [**ib-tws-api (Node.js)**](https://github.com/maxicus/ib-tws-api) | 59 | JavaScript | 🟡 | Integrating IBKR execution into Node-based web dashboards or serverless trading backends. |
| [**rib (R client for IBKR)**](https://github.com/lbilli/rib) | 46 | R | 🟢 | Native R connectivity for quants who run their research/backtests in R. |
| [**IBridgePy**](https://github.com/PeterPanonGit/IBridgePy) | 35 | Python | 🔴 | Historically useful for porting Quantopian/Zipline-style backtested algorithms to live IBKR execution with minimal code changes. |
| [**IBKR Web API client (ibkr_web_client)**](https://github.com/nsirons/ibkr_web_client) | 21 | Python | 🟡 | Gateway-free IBKR integration via REST/OAuth for simpler deployment topologies (no desktop app to keep alive). |
| [**IB Web API / Client Portal auth automation (schwab-ib-auto-login)**](https://github.com/johnwang9/schwab-ib-auto-login) | 2 | Python | 🟢 | Windows-native, non-Docker headless login automation for IBKR TWS/Gateway and Schwab thinkorswim side by side. |
| [**ib-gateway-docker (lylecodes IPv6/Railway fork)**](https://github.com/lylecodes/ib-gateway-docker) | 0 | Java | 🟢 | Deploying IB Gateway specifically on Railway.com or IPv6-only network environments. |

<details><summary>Explainers (21)</summary>

**[ib_insync](https://github.com/erdewit/ib_insync)** · Python · ★ 3.3k · last push 2024-03-14  
The original, hugely popular Python sync/async framework for the Interactive Brokers API, created by Ewald de Wit. It pioneered the ergonomic asyncio-based approach to IBKR automation that ib_async now continues. Archived after the author's death in 2024; still widely referenced in tutorials and blog posts but should not be used for new projects.

✅ *Good at:* Historically the best-documented, most battle-tested IBKR Python wrapper; huge amount of example code and StackOverflow/tutorial coverage still exists under its name.  
⚠️ *Limitations:* No longer maintained or patched; new projects should use ib_async instead.

**[High-Frequency-Trading-Model-with-IB](https://github.com/jamesmawm/High-Frequency-Trading-Model-with-IB)** · Python · ★ 2.9k · last push 2025-05-29  
A widely-starred educational repository (and companion O'Reilly book) demonstrating pairs-trading and mean-reversion HFT-style strategies against the IB API in Python. More of a teaching reference than production infrastructure, but frequently cited as an entry point for IBKR algo development.

✅ *Good at:* Learning the end-to-end shape of an IBKR-connected mean-reversion/pairs strategy, including basic risk and order management patterns.  
⚠️ *Limitations:* Educational-grade code, not production-hardened; uses the older ib_insync-era API style.

**[ThetaGang](https://github.com/brndnmtthws/thetagang)** · Python · ★ 2.7k · last push 2026-09-16  
A popular, actively maintained IBKR options-selling bot built on ib_async/ib_insync that automates the 'wheel' strategy (selling cash-secured puts and covered calls) with configurable delta targets, position sizing, and rolling logic. Widely referenced in r/algotrading and r/thetagang as a starting point for automated premium-selling on IBKR.

✅ *Good at:* Turnkey automated wheel/covered-call/cash-secured-put strategy execution on IBKR accounts, with YAML-driven configuration.  
⚠️ *Limitations:* Strategy-specific (options premium selling only), not a general execution framework; requires careful account/margin configuration to avoid unwanted assignment risk.

**[ib_async](https://github.com/ib-api-reloaded/ib_async)** · Python · ★ 1.7k · last push 2026-08-19  
Community-maintained fork of ib_insync, created after original author Ewald de Wit passed away in 2024. Provides a clean sync/async Python wrapper around the IB TWS/Gateway socket API, handling reqId bookkeeping, contract qualification, and streaming market data as asyncio-friendly objects. It is the de facto standard Python interface for retail/small-fund IBKR automation and is what most new IBKR tutorials now point to.

✅ *Good at:* Rapid prototyping of IBKR strategies in Jupyter/scripts; clean object model for orders, positions, and streaming ticks/bars without hand-rolling the raw EClient/EWrapper callback API.  
⚠️ *Limitations:* Still depends on IBKR's TWS/Gateway process being up and logged in (see IBC/ib-gateway-docker); inherits IBKR API quirks like pacing violations and contract ambiguity.

**[IbcAlpha/IBC](https://github.com/IbcAlpha/IBC)** · Java · ★ 1.6k · last push 2026-09-01  
IBC (formerly IBController) is the underlying automation layer that drives TWS/IB Gateway's login screens, 2FA dialogs, and daily restart prompts programmatically, eliminating the need to manually click through the desktop UI. It is the component embedded inside virtually every IB Gateway Docker image (gnzsnz, UnusualAlpha, etc.) and is also usable standalone on bare-metal/VM installs.

✅ *Good at:* Fully unattended IBKR Gateway/TWS operation: auto-login, auto-restart, auto-confirming order dialogs, and closing popups that would otherwise block headless automation.  
⚠️ *Limitations:* GitHub shows it archived/read-only for direct contributions in places, though releases continue; configuration (ibc.ini) has a learning curve and must be kept in sync with each TWS version.

**[gnzsnz/ib-gateway-docker](https://github.com/gnzsnz/ib-gateway-docker)** · Shell · ★ 1.3k · last push 2026-09-20  
The most popular Docker image bundling IB Gateway/TWS with IBC for fully headless, auto-restarting, auto-login IBKR connectivity. Actively updated almost weekly to track new IBKR Gateway releases, and widely used as the base container for cloud-hosted IBKR trading bots (Kubernetes, docker-compose, Railway, etc.).

✅ *Good at:* Running a reliable, unattended IBKR Gateway in a container for 24/7 automated systems, with VNC access for 2FA setup and automatic daily restart handling.  
⚠️ *Limitations:* Still subject to IBKR's mandatory daily restart and 2FA re-auth cadence; requires care around IBKR's paper vs live gateway config.

**[rust-ibapi](https://github.com/wboayue/rust-ibapi)** · Rust · ★ 385 · last push 2026-09-21  
A from-scratch, actively developed Rust implementation of the Interactive Brokers TWS API, reimplementing IBKR's wire protocol without depending on the official Java/C++ client. Offers both sync and async (tokio) clients, typed contract/order builders, and streaming market data. Notable for being pushed to essentially daily as of late 2026, making it one of the most current non-Python IBKR clients.

✅ *Good at:* Low-overhead, memory-safe IBKR connectivity for latency-sensitive or embedded execution services written in Rust.  
⚠️ *Limitations:* Smaller community and fewer examples than the Python ecosystem; API surface still catching up to newer TWS API features.

**[ezibpy](https://github.com/ranaroussi/ezibpy)** · Python · ★ 335 · last push 2022-07-24  
Pythonic client for the IB API written by Ran Aroussi (also author of yfinance), designed to simplify contract creation, order placement, and market data callbacks. Was popularized as the execution backend for QTPyLib and other older Python quant frameworks.

✅ *Good at:* Simple synchronous helper functions for common IBKR order types when a full async framework is overkill.  
⚠️ *Limitations:* No commits since 2022; predates many newer TWS API message versions.

**[UnusualAlpha/ib-gateway-docker](https://github.com/UnusualAlpha/ib-gateway-docker)** · Dockerfile · ★ 306 · last push 2026-09-15  
An alternative, actively maintained Docker image for IB Gateway + IBC, offering a leaner build than gnzsnz's image with its own configuration conventions; a common second choice when gnzsnz's image doesn't fit a particular deployment.

✅ *Good at:* Lightweight headless IB Gateway containerization as an alternative to the more feature-heavy gnzsnz image.  
⚠️ *Limitations:* Smaller community/support surface than gnzsnz/ib-gateway-docker.

**[hadrianl/ibapi (Go)](https://github.com/hadrianl/ibapi)** · Go · ★ 163 · last push 2023-09-27  
An earlier Go implementation of the IB API, offering a Go-native client for TWS/Gateway connectivity with support for market data, orders, and account updates.

✅ *Good at:* Reference implementation for Go IBKR clients predating scmhub/ibapi.  
⚠️ *Limitations:* Infrequent updates since 2023.

**[IB-Gateway Docker (UnusualAlpha alt.) / manhinhang variant](https://github.com/manhinhang/ib-gateway-docker)** · Shell · ★ 110 · last push 2026-09-15  
A lightweight, actively updated fork/alternative IB Gateway Docker image, part of the broader ecosystem of gnzsnz-inspired IB Gateway containers each optimizing for slightly different deployment targets (image size, cloud host quirks, IPv6 support, etc).

✅ *Good at:* A minimal-footprint alternative when gnzsnz's more feature-rich image is heavier than needed.  
⚠️ *Limitations:* Fragmented ecosystem of similar forks (gnzsnz, UnusualAlpha, manhinhang, lylecodes) means due diligence is needed to pick the best-supported one for a given cloud target.

**[interactive-brokers-api (REST wrapper)](https://github.com/areed1192/interactive-brokers-api)** · Python · ★ 103 · last push 2026-07-24  
A Python application for interacting with Interactive Brokers' Client Portal Web (REST) API, from the same author as several other broker wrapper libraries (td-ameritrade-api). Actively updated through 2026.

✅ *Good at:* Simple REST-based IBKR automation without the socket-protocol complexity of the TWS API.  
⚠️ *Limitations:* REST/Client Portal API is less feature-complete than the classic TWS socket API for advanced order types.

**[scmhub/ibapi (Go)](https://github.com/scmhub/ibapi)** · Go · ★ 76 · last push 2026-09-17  
An unofficial, actively updated Go port of the Interactive Brokers TWS API, mirroring the official Java client's EClient/EWrapper structure idiomatically in Go. Useful for building low-latency Go execution services that talk directly to TWS/Gateway.

✅ *Good at:* Native Go integration for teams building order-routing or risk services in Go rather than Python.  
⚠️ *Limitations:* Small community; less battle-tested than the Python ib_async ecosystem.

**[Jib.jl](https://github.com/lbilli/Jib.jl)** · Julia · ★ 69 · last push 2026-08-25  
A Julia implementation of the Interactive Brokers API by the same author as the R client `rib`, providing a low-level but complete socket-protocol client for TWS/Gateway usable from Julia quant research pipelines.

✅ *Good at:* Native IBKR connectivity for Julia-based quant research and execution stacks.  
⚠️ *Limitations:* Niche language ecosystem; smaller user base than Python equivalents.

**[IB4m](https://github.com/softwarespartan/IB4m)** · MATLAB · ★ 59 · last push 2022-02-07  
Interactive Brokers API bindings for MATLAB, allowing MATLAB-based quant research environments to place orders and pull data from TWS/Gateway directly.

✅ *Good at:* Bridging MATLAB signal-processing/quant research code straight to IBKR execution.  
⚠️ *Limitations:* No recent activity; MATLAB IBKR integration niche is largely superseded by Python.

**[ib-tws-api (Node.js)](https://github.com/maxicus/ib-tws-api)** · JavaScript · ★ 59 · last push 2024-05-30  
A Node.js client for the IB TWS/Gateway socket API, giving JavaScript/TypeScript backends direct access to IBKR market data and order management without a Python intermediary.

✅ *Good at:* Integrating IBKR execution into Node-based web dashboards or serverless trading backends.  
⚠️ *Limitations:* Smaller community than Python clients; last substantive update over a year old.

**[rib (R client for IBKR)](https://github.com/lbilli/rib)** · R · ★ 46 · last push 2026-08-25  
An R implementation of the Interactive Brokers API socket protocol, giving R users direct access to TWS/Gateway market data and order entry without needing a Python bridge.

✅ *Good at:* Native R connectivity for quants who run their research/backtests in R.  
⚠️ *Limitations:* Small maintainer base (one author for both R and Julia clients).

**[IBridgePy](https://github.com/PeterPanonGit/IBridgePy)** · Python · ★ 35 · last push 2015-04-17  
IBridgePy was an early product/library that let Zipline- and Quantopian-style algorithm code run against live Interactive Brokers accounts, translating the familiar `order()`/`symbol()` API into IB TWS calls. Its companion commercial product (ibridgepy.com) continued longer than this open GitHub repo, which has been dormant for a decade.

✅ *Good at:* Historically useful for porting Quantopian/Zipline-style backtested algorithms to live IBKR execution with minimal code changes.  
⚠️ *Limitations:* Repository is effectively abandoned since 2015; modern users should prefer ib_async or a framework with native IBKR adapters (nautilus_trader, backtrader).

**[IBKR Web API client (ibkr_web_client)](https://github.com/nsirons/ibkr_web_client)** · Python · ★ 21 · last push 2024-12-23  
A Python client for IBKR's newer Client Portal / Web API using OAuth1.0a authentication, as opposed to the classic TWS socket API. Relevant for teams wanting to avoid running a TWS/Gateway process at all and instead integrate against IBKR's REST+OAuth surface.

✅ *Good at:* Gateway-free IBKR integration via REST/OAuth for simpler deployment topologies (no desktop app to keep alive).  
⚠️ *Limitations:* IBKR's Web API has a narrower feature set than the full TWS API (fewer order types, market data nuances); small single-maintainer project.

**[IB Web API / Client Portal auth automation (schwab-ib-auto-login)](https://github.com/johnwang9/schwab-ib-auto-login)** · Python · ★ 2 · last push 2026-09-15  
A Windows/AutoIt-based auto-login tool for Schwab thinkorswim and IBKR TWS/Gateway, positioned as an IBC/IBCAlpha alternative for teams running Windows Task Scheduler-based automation rather than Docker/Linux, and also handling Schwab API refresh-token auto-renewal.

✅ *Good at:* Windows-native, non-Docker headless login automation for IBKR TWS/Gateway and Schwab thinkorswim side by side.  
⚠️ *Limitations:* Very young/low-adoption project (2 stars); Windows/AutoIt-specific approach is less portable than the Docker+IBC pattern most of the community uses.

**[ib-gateway-docker (lylecodes IPv6/Railway fork)](https://github.com/lylecodes/ib-gateway-docker)** · Java · ★ 0 · last push 2026-05-05  
A fork of gnzsnz/ib-gateway-docker specifically adapted for IPv6 support and deployment on Railway.com's PaaS, illustrating how the core gnzsnz image gets adapted for specific cloud hosting targets.

✅ *Good at:* Deploying IB Gateway specifically on Railway.com or IPv6-only network environments.  
⚠️ *Limitations:* Niche fork with no independent community; best thought of as a patch on top of gnzsnz's image for a specific host.

</details>

### Broker SDKs

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**robin_stocks**](https://github.com/jmfernandes/robin_stocks) | 2.1k | Python | 🟢 | Full-featured unofficial access to a Robinhood account for retail algo/scripted trading, including options and crypto. |
| [**alpaca-trade-api-python (legacy)**](https://github.com/alpacahq/alpaca-trade-api-python) | 1.9k | Python | 🔴 | Legacy compatibility for older Alpaca integrations that haven't migrated to alpaca-py yet. |
| [**pyrh**](https://github.com/robinhood-unofficial/pyrh) | 1.8k | Python | 🟡 | Historical reference implementation of unofficial Robinhood trading automation. |
| [**alpaca-py**](https://github.com/alpacahq/alpaca-py) | 1.5k | Python | 🟢 | Official, well-documented access to Alpaca's commission-free US equities/options/crypto paper and live trading, including fractional shares and easy paper-trading toggle. |
| [**Schwabdev**](https://github.com/tylerebowers/Schwabdev) | 873 | Python | 🟢 | Quick-start Schwab API access with less boilerplate than schwab-py, good streaming quote handling. |
| [**alpaca-backtrader-api**](https://github.com/alpacahq/alpaca-backtrader-api) | 702 | Python | 🟢 | Reusing existing Backtrader strategy code for live/paper trading on Alpaca with minimal changes. |
| [**alpaca-trade-api-js**](https://github.com/alpacahq/alpaca-trade-api-js) | 601 | TypeScript | 🟢 | Building Alpaca-connected trading bots or dashboards in a Node/TypeScript stack. |
| [**schwab-py**](https://github.com/alexgolec/schwab-py) | 469 | Python | 🟢 | Full-featured Schwab account/order/streaming access for retail algo traders who migrated from TD Ameritrade's tda-api after TDA's API shutdown. |
| [**alpaca-trade-api-csharp**](https://github.com/alpacahq/alpaca-trade-api-csharp) | 301 | C# | 🟢 | .NET-native Alpaca integration for teams building execution infrastructure in C#/.NET. |
| [**tastyware/tastytrade (unofficial Python SDK)**](https://github.com/tastyware/tastytrade) | 258 | Python | 🟢 | Modern async access to Tastytrade for options-focused retail algo trading, including complex multi-leg option orders. |
| [**OpenApiPy (cTrader)**](https://github.com/spotware/OpenApiPy) | 192 | Python | 🟡 | Official, vendor-supported access to any broker running the cTrader platform (widely used among retail FX/CFD brokers). |
| [**aiomql**](https://github.com/Ichinga-Samuel/aiomql) | 151 | Python | 🟢 | Building async Python trading bots against any MT5-compatible broker with higher-level strategy/risk abstractions than the raw MetaTrader5 package. |
| [**td-ameritrade-api**](https://github.com/areed1192/td-ameritrade-api) | 129 | Python | 🟡 | Reference implementation showing the TDA-to-Schwab API transition for teams migrating old TDA-based bots. |
| [**tastytrade-api-js**](https://github.com/tastytrade/tastytrade-api-js) | 107 | TypeScript | 🟢 | Official JS/TS access to Tastytrade accounts and orders. |
| [**tastytrade-sdk-python (official)**](https://github.com/tastytrade/tastytrade-sdk-python) | 106 | Python | 🔴 | Officially blessed baseline for simple Tastytrade session/auth handling. |
| [**tasty-agent**](https://github.com/ferdousbhai/tasty-agent) | 100 | Python | 🟢 | Wiring an LLM coding/trading agent directly into a live Tastytrade account for conversational portfolio management. |
| [**OpenAPI.Net (cTrader .NET)**](https://github.com/spotware/OpenAPI.Net) | 95 | C# | 🟡 | Officially supported .NET access to cTrader-connected brokers for FX/CFD algo trading. |
| [**tradier-python (phileaton)**](https://github.com/phileaton/tradier-python) | 20 | Python | ⚪ | Straightforward REST access to Tradier accounts/orders for options-focused retail bots. |
| [**uvatradier**](https://github.com/thammo4/uvatradier) | 20 | Python | ⚪ | Simplified account/order/quote handling for Tradier-based retail options and equities bots. |
| [**PyTraderMT4-MT5**](https://github.com/dizengoff/PyTraderMT4-MT5) | 20 | MQL5 | ⚪ | Bridging both legacy MT4 and current MT5 platforms to Python with minimal MQL setup for retail FX bots. |

<details><summary>Explainers (20)</summary>

**[robin_stocks](https://github.com/jmfernandes/robin_stocks)** · Python · ★ 2.1k · last push 2026-02-11  
The most widely used unofficial Robinhood API library, supporting stock, options, and crypto trading, real-time-ish quotes, portfolio performance, and tax document retrieval. Also has limited support for other brokers (TDA historically, Gemini). Remains the go-to for Robinhood automation despite Robinhood having no official public trading API.

✅ *Good at:* Full-featured unofficial access to a Robinhood account for retail algo/scripted trading, including options and crypto.  
⚠️ *Limitations:* Depends on reverse-engineered, undocumented endpoints that Robinhood can change or block without notice; using it risks account restrictions and violates Robinhood's ToS for automated trading.

**[alpaca-trade-api-python (legacy)](https://github.com/alpacahq/alpaca-trade-api-python)** · Python · ★ 1.9k · last push 2024-12-02  
The original Alpaca Python SDK, now superseded by alpaca-py and archived by Alpaca. Still referenced in a large amount of older tutorial code and third-party integrations (e.g. lumibot, alpaca-backtrader-api).

✅ *Good at:* Legacy compatibility for older Alpaca integrations that haven't migrated to alpaca-py yet.  
⚠️ *Limitations:* No longer maintained; new projects should use alpaca-py.

**[pyrh](https://github.com/robinhood-unofficial/pyrh)** · Python · ★ 1.8k · last push 2024-08-08  
An earlier, once-dominant unofficial Python framework for Robinhood trading, now largely superseded in active development by robin_stocks but still referenced in many older tutorials.

✅ *Good at:* Historical reference implementation of unofficial Robinhood trading automation.  
⚠️ *Limitations:* Slower-moving than robin_stocks; same fundamental ToS/reverse-engineering risk applies.

**[alpaca-py](https://github.com/alpacahq/alpaca-py)** · Python · ★ 1.5k · last push 2026-09-18  
Alpaca's official, current-generation unified Python SDK covering trading (stocks, options, crypto), market data, and broker API endpoints, replacing the older alpaca-trade-api-python. Actively developed by Alpaca itself with regular releases tracking new asset classes and order types.

✅ *Good at:* Official, well-documented access to Alpaca's commission-free US equities/options/crypto paper and live trading, including fractional shares and easy paper-trading toggle.  
⚠️ *Limitations:* Alpaca-specific; US-focused broker with its own margin/PDT rules and API rate limits.

**[Schwabdev](https://github.com/tylerebowers/Schwabdev)** · Python · ★ 873 · last push 2026-08-11  
A lightweight, actively developed alternative to schwab-py for the Charles Schwab API, emphasizing simplicity and minimal dependencies, with built-in token auto-refresh and streaming support. Has overtaken schwab-py in star count, suggesting it's becoming the community favorite for new Schwab integrations.

✅ *Good at:* Quick-start Schwab API access with less boilerplate than schwab-py, good streaming quote handling.  
⚠️ *Limitations:* Newer/less battle-tested at scale than schwab-py; Schwab's API itself remains less mature than IBKR's or Alpaca's for algo trading.

**[alpaca-backtrader-api](https://github.com/alpacahq/alpaca-backtrader-api)** · Python · ★ 702 · last push 2026-06-23  
Official Alpaca integration for the Backtrader framework, letting Backtrader strategies run unchanged in paper or live mode against Alpaca accounts. Bridges Alpaca's data/broker feeds into Backtrader's cerebro engine.

✅ *Good at:* Reusing existing Backtrader strategy code for live/paper trading on Alpaca with minimal changes.  
⚠️ *Limitations:* Tied to Backtrader's architecture and its single-threaded event loop model.

**[alpaca-trade-api-js](https://github.com/alpacahq/alpaca-trade-api-js)** · TypeScript · ★ 601 · last push 2026-09-18  
Alpaca's official Node.js/TypeScript client library for the Trading and Market Data APIs, actively maintained alongside the Python SDKs.

✅ *Good at:* Building Alpaca-connected trading bots or dashboards in a Node/TypeScript stack.  
⚠️ *Limitations:* Alpaca-specific; feature parity with alpaca-py can lag slightly on brand-new endpoints.

**[schwab-py](https://github.com/alexgolec/schwab-py)** · Python · ★ 469 · last push 2026-08-26  
The most established unofficial Python wrapper for the Charles Schwab (post-TD-Ameritrade-migration) trading and market-data API, written by the same author as the earlier popular tda-api library. Handles Schwab's OAuth flow, token refresh, and both REST and streaming endpoints.

✅ *Good at:* Full-featured Schwab account/order/streaming access for retail algo traders who migrated from TD Ameritrade's tda-api after TDA's API shutdown.  
⚠️ *Limitations:* Schwab's OAuth token lifecycle (refresh token expires periodically, requiring re-auth) is an operational annoyance common to all Schwab wrappers, not unique to this library.

**[alpaca-trade-api-csharp](https://github.com/alpacahq/alpaca-trade-api-csharp)** · C# · ★ 301 · last push 2026-09-21  
Alpaca's official .NET/C# SDK for trading and market data, actively maintained with commits as recent as the current date, useful for .NET-based execution services.

✅ *Good at:* .NET-native Alpaca integration for teams building execution infrastructure in C#/.NET.  
⚠️ *Limitations:* Alpaca-specific broker scope.

**[tastyware/tastytrade (unofficial Python SDK)](https://github.com/tastyware/tastytrade)** · Python · ★ 258 · last push 2026-08-07  
The most actively maintained community Python SDK for Tastytrade, fully typed and async, covering account management, options chains, order placement, and streaming quotes/account updates via Tastytrade's DXLink websocket feed. Has effectively superseded Tastytrade's own official Python SDK in community usage.

✅ *Good at:* Modern async access to Tastytrade for options-focused retail algo trading, including complex multi-leg option orders.  
⚠️ *Limitations:* Unofficial; must track Tastytrade's API changes without vendor SLA, though it does so promptly in practice.

**[OpenApiPy (cTrader)](https://github.com/spotware/OpenApiPy)** · Python · ★ 192 · last push 2024-08-07  
Spotware's official Python package for the cTrader Open API, giving programmatic access to cTrader-connected forex/CFD brokers for market data streaming and order execution using Twisted-based async networking.

✅ *Good at:* Official, vendor-supported access to any broker running the cTrader platform (widely used among retail FX/CFD brokers).  
⚠️ *Limitations:* FX/CFD-focused, not relevant to US equities; built on Twisted which is less common in modern Python async stacks (asyncio).

**[aiomql](https://github.com/Ichinga-Samuel/aiomql)** · Python · ★ 151 · last push 2026-07-26  
An actively maintained asynchronous Python framework built on top of MetaQuotes' official MetaTrader5 Python package, adding async wrappers, a strategy/backtesting scaffold, risk management helpers, and session/order utilities for MT5-connected forex/CFD brokers.

✅ *Good at:* Building async Python trading bots against any MT5-compatible broker with higher-level strategy/risk abstractions than the raw MetaTrader5 package.  
⚠️ *Limitations:* Requires a running MT5 terminal (Windows-native, though Wine/Linux workarounds exist) since MetaQuotes' underlying package only talks to a local terminal instance.

**[td-ameritrade-api](https://github.com/areed1192/td-ameritrade-api)** · Python · ★ 129 · last push 2025-01-15  
Originally an unofficial TD Ameritrade API client, repurposed/rebranded toward Schwab's REST API surface after TDA's acquisition and API sunset. Historically significant as one of the most popular TDA wrappers before the migration.

✅ *Good at:* Reference implementation showing the TDA-to-Schwab API transition for teams migrating old TDA-based bots.  
⚠️ *Limitations:* Largely superseded by schwab-py and Schwabdev for new Schwab-native development.

**[tastytrade-api-js](https://github.com/tastytrade/tastytrade-api-js)** · TypeScript · ★ 107 · last push 2026-05-17  
Tastytrade's official JavaScript/TypeScript SDK for their trading API, actively maintained for building browser or Node-based Tastytrade integrations.

✅ *Good at:* Official JS/TS access to Tastytrade accounts and orders.  
⚠️ *Limitations:* Tastytrade-specific; options/derivatives-centric platform, less relevant for pure equities long/short systems.

**[tastytrade-sdk-python (official)](https://github.com/tastytrade/tastytrade-sdk-python)** · Python · ★ 106 · last push 2026-03-13  
Tastytrade's own official Python SDK, now archived by the vendor in favor of the community-driven tastyware/tastytrade project (or direct API usage). Still functional for basic account/session/order operations.

✅ *Good at:* Officially blessed baseline for simple Tastytrade session/auth handling.  
⚠️ *Limitations:* Archived; the community fork (tastyware/tastytrade) is more actively developed and feature-complete.

**[tasty-agent](https://github.com/ferdousbhai/tasty-agent)** · Python · ★ 100 · last push 2026-09-13  
An MCP (Model Context Protocol) server that lets Claude or other LLM agents manage a Tastytrade portfolio directly -- checking positions, balances, and placing trades through natural-language tool calls. Representative of the newer wave of LLM-agent-to-broker bridges built on top of the tastyware SDK.

✅ *Good at:* Wiring an LLM coding/trading agent directly into a live Tastytrade account for conversational portfolio management.  
⚠️ *Limitations:* Young project; giving an LLM agent direct order-placement power on a live account carries obvious operational risk and needs strict guardrails.

**[OpenAPI.Net (cTrader .NET)](https://github.com/spotware/OpenAPI.Net)** · C# · ★ 95 · last push 2024-06-28  
Spotware's official .NET/Reactive Extensions (Rx) library for the cTrader Open API, the primary integration path for cBot/algorithmic strategy developers building on the cTrader platform in C#.

✅ *Good at:* Officially supported .NET access to cTrader-connected brokers for FX/CFD algo trading.  
⚠️ *Limitations:* FX/CFD/cTrader-ecosystem specific; not applicable to US equities brokers.

**[tradier-python (phileaton)](https://github.com/phileaton/tradier-python)** · Python · ★ 20 · last push unknown  
A Python client for the Tradier brokerage API covering account, market data, and trading endpoints. Tradier is popular among retail options algo traders for its developer-friendly REST API and commission structure; the Python ecosystem around it is fragmented across several small competing clients.

✅ *Good at:* Straightforward REST access to Tradier accounts/orders for options-focused retail bots.  
⚠️ *Limitations:* Small, single-maintainer project; users should compare against uvatradier and python-tradier before committing.

**[uvatradier](https://github.com/thammo4/uvatradier)** · Python · ★ 20 · last push unknown  
A Python wrapper package for the Tradier brokerage API that packages account, market-data, and order-management calls into a single pip-installable client, aiming to be more ergonomic than raw `requests` calls against Tradier's REST endpoints.

✅ *Good at:* Simplified account/order/quote handling for Tradier-based retail options and equities bots.  
⚠️ *Limitations:* Community-maintained with a small user base; Tradier's own official SDK list should be checked for the current best option.

**[PyTraderMT4-MT5](https://github.com/dizengoff/PyTraderMT4-MT5)** · MQL5 · ★ 20 · last push unknown  
An open-source bridge connecting both MetaTrader 4 and MetaTrader 5 to Python via a drag-and-drop Expert Advisor, letting Python code drive bar data downloads and live feeds/strategies without deep MQL programming.

✅ *Good at:* Bridging both legacy MT4 and current MT5 platforms to Python with minimal MQL setup for retail FX bots.  
⚠️ *Limitations:* Depends on a running MetaTrader terminal instance; MT4/MT5 are Windows-native platforms requiring extra setup on Linux/Mac.

</details>

### Execution & OMS

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**pysystemtrade**](https://github.com/robcarver17/pysystemtrade) | 3.5k | Python | 🟢 | A theoretically rigorous, IBKR-connected systematic trading stack for multi-instrument (primarily futures) portfolios with strong risk/vol-targeting logic, directly usable as a reference for building a disciplined long/short risk framework. |
| [**FreqUI**](https://github.com/freqtrade/frequi) | 1.1k | Vue | 🟢 | Real-time visual monitoring and manual override of a live freqtrade bot. |
| [**go-trader (robaho)**](https://github.com/robaho/go-trader) | 521 | Go | 🟢 | Local integration testing of execution/OMS code against a simulated exchange with realistic order matching semantics. |
| [**the0**](https://github.com/alexanderwanyoike/the0) | 432 | TypeScript | 🟢 | Running heterogeneous trading bots (in any language) side-by-side under one orchestration/execution layer without forcing a specific strategy DSL. |
| [**Hummingbot Dashboard**](https://github.com/hummingbot/dashboard) | 367 | Python | 🟢 | Visual configuration/monitoring layer for Hummingbot strategies and live bot fleets. |
| [**hummingbot-api**](https://github.com/hummingbot/hummingbot-api) | 142 | Python | 🟢 | Centralized management/monitoring of many Hummingbot instances, useful for running several strategies or markets in parallel. |

<details><summary>Explainers (6)</summary>

**[pysystemtrade](https://github.com/robcarver17/pysystemtrade)** · Python · ★ 3.5k · last push 2026-07-18  
Rob Carver's (author of 'Systematic Trading' and 'Leveraged Trading') open-source Python implementation of his systematic futures trading framework, with live execution support against Interactive Brokers. Widely respected in the quant community for its rigorous, book-grounded approach to position sizing, risk overlay, and multi-instrument portfolio construction.

✅ *Good at:* A theoretically rigorous, IBKR-connected systematic trading stack for multi-instrument (primarily futures) portfolios with strong risk/vol-targeting logic, directly usable as a reference for building a disciplined long/short risk framework.  
⚠️ *Limitations:* Originally built and tuned around futures trading (though adaptable); requires a MongoDB + Interactive Brokers + Python setup and has real infrastructure/ops overhead to run live.

**[FreqUI](https://github.com/freqtrade/frequi)** · Vue · ★ 1.1k · last push 2026-09-17  
The official web-based frontend/dashboard for freqtrade, providing live monitoring of open trades, P&L, and bot control (start/stop/force-exit) against a running freqtrade REST API instance.

✅ *Good at:* Real-time visual monitoring and manual override of a live freqtrade bot.  
⚠️ *Limitations:* freqtrade-specific, not a general-purpose OMS dashboard.

**[go-trader (robaho)](https://github.com/robaho/go-trader)** · Go · ★ 521 · last push 2026-06-30  
A financial exchange simulator written in Go, designed for algorithmic trading tests -- effectively a lightweight matching-engine/exchange stand-in that lets teams test order-routing and execution logic against a realistic (simulated) FIX/exchange environment without touching a live venue.

✅ *Good at:* Local integration testing of execution/OMS code against a simulated exchange with realistic order matching semantics.  
⚠️ *Limitations:* A testing/simulation tool, not a production execution engine itself.

**[the0](https://github.com/alexanderwanyoike/the0)** · TypeScript · ★ 432 · last push 2026-09-01  
A self-hosted execution engine for algorithmic trading bots that imposes no strategy framework at all -- each bot runs as normal application code (Python, TypeScript, Rust, C++, C#, Scala, or Haskell) inside an isolated container, with the0 handling scheduling, isolation, and orchestration rather than strategy logic.

✅ *Good at:* Running heterogeneous trading bots (in any language) side-by-side under one orchestration/execution layer without forcing a specific strategy DSL.  
⚠️ *Limitations:* Newer project (2026) with a smaller track record than established engines like nautilus_trader or Lean; being framework-agnostic means it provides less built-in OMS/risk tooling than dedicated trading platforms.

**[Hummingbot Dashboard](https://github.com/hummingbot/dashboard)** · Python · ★ 367 · last push 2025-10-27  
A web application for creating, backtesting, deploying, and managing Hummingbot instances through a UI rather than raw config files/CLI, lowering the barrier to running a Hummingbot-based strategy in production.

✅ *Good at:* Visual configuration/monitoring layer for Hummingbot strategies and live bot fleets.  
⚠️ *Limitations:* Hummingbot-specific; still requires understanding Hummingbot's underlying strategy/connector model.

**[hummingbot-api](https://github.com/hummingbot/hummingbot-api)** · Python · ★ 142 · last push 2026-09-18  
A backend REST API for orchestrating multiple Hummingbot instances -- deploying, monitoring, and controlling a fleet of market-making/execution bots programmatically rather than one-at-a-time via the CLI.

✅ *Good at:* Centralized management/monitoring of many Hummingbot instances, useful for running several strategies or markets in parallel.  
⚠️ *Limitations:* Tied to the Hummingbot ecosystem specifically.

</details>

### Crypto bots

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**ccxt**](https://github.com/ccxt/ccxt) | 44.1k | Python | 🟢 | Writing exchange-agnostic order placement, balance, and market-data code that works across dozens of crypto venues with one consistent API. |
| [**Superalgos**](https://github.com/Superalgos/Superalgos) | 5.7k | JavaScript | 🟢 | Non-coder-friendly, visual strategy design and deployment for crypto trading, with an integrated data pipeline. |
| [**Krypto/opentrader**](https://github.com/Open-Trader/opentrader) | 2.9k | TypeScript | 🟡 | DCA/grid strategy automation for crypto with a polished self-hosted web UI, appealing to a TypeScript/Node-oriented team. |
| [**pmxt (CCXT for prediction markets)**](https://github.com/pmxt-dev/pmxt) | 2.2k | TypeScript | 🟢 | Writing venue-agnostic execution code across Polymarket/Kalshi-style prediction markets. |
| [**cassandre-trading-bot**](https://github.com/cassandre-tech/cassandre-trading-bot) | 661 | Java | 🟡 | Java/Spring-native crypto bot development for teams already standardized on the Spring stack. |

<details><summary>Explainers (5)</summary>

**[ccxt](https://github.com/ccxt/ccxt)** · Python · ★ 44.1k · last push 2026-09-20  
The de facto standard unified REST/WebSocket API for 100+ crypto exchanges and prediction markets, available in Python, JavaScript/TypeScript, C#, PHP, Go, Java, and Rust. Nearly every other crypto bot framework in this catalog (freqtrade, Jesse, OctoBot, many custom bots) uses ccxt under the hood as its exchange abstraction layer.

✅ *Good at:* Writing exchange-agnostic order placement, balance, and market-data code that works across dozens of crypto venues with one consistent API.  
⚠️ *Limitations:* Unified API necessarily lags or abstracts away some exchange-specific advanced order types/features; REST-based unified calls can be higher latency than a native WebSocket-first exchange SDK.

**[Superalgos](https://github.com/Superalgos/Superalgos)** · JavaScript · ★ 5.7k · last push 2026-09-21  
A free, open-source visual crypto trading bot platform where strategies are designed as node-graphs on an integrated charting canvas rather than written as code, with built-in data mining, backtesting, paper trading, and multi-server deployment support.

✅ *Good at:* Non-coder-friendly, visual strategy design and deployment for crypto trading, with an integrated data pipeline.  
⚠️ *Limitations:* Crypto-only; the visual-programming paradigm can be harder to version-control/test than plain code for engineering-heavy teams.

**[Krypto/opentrader](https://github.com/Open-Trader/opentrader)** · TypeScript · ★ 2.9k · last push 2025-06-29  
An open-source crypto trading bot with a modern web UI supporting DCA and grid trading strategies, notable for its TypeScript stack (versus the Python-dominant crypto bot landscape) and design-forward UI.

✅ *Good at:* DCA/grid strategy automation for crypto with a polished self-hosted web UI, appealing to a TypeScript/Node-oriented team.  
⚠️ *Limitations:* Crypto-only; slower recent commit cadence than freqtrade/OctoBot.

**[pmxt (CCXT for prediction markets)](https://github.com/pmxt-dev/pmxt)** · TypeScript · ★ 2.2k · last push 2026-07-18  
A CCXT-inspired unified API specifically for prediction markets (Polymarket, Kalshi, and others), extending the 'one API, many venues' pattern that made ccxt successful to the fast-growing prediction-market execution space.

✅ *Good at:* Writing venue-agnostic execution code across Polymarket/Kalshi-style prediction markets.  
⚠️ *Limitations:* Prediction-market specific, not applicable to traditional equities/crypto spot-futures execution.

**[cassandre-trading-bot](https://github.com/cassandre-tech/cassandre-trading-bot)** · Java · ★ 661 · last push 2025-03-01  
A Spring Boot starter for building Java crypto trading bots, handling exchange connections, accounts, orders, trades, and positions so developers can focus purely on strategy logic within the familiar Spring ecosystem.

✅ *Good at:* Java/Spring-native crypto bot development for teams already standardized on the Spring stack.  
⚠️ *Limitations:* Crypto-only; activity has slowed with less frequent updates than the Python-first frameworks.

</details>

### Market making

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**Hummingbot**](https://github.com/hummingbot/hummingbot) | 20.1k | Python | 🟢 | Production-grade crypto market making and cross-exchange arbitrage with connector abstractions handling exchange-specific order book/order-type quirks. |
| [**Krypto-trading-bot (Tribeca)**](https://github.com/ctubio/Krypto-trading-bot) | 3.7k | C++ | 🟡 | Low-latency C++ market making for crypto exchanges where Python-based bots' latency is a bottleneck. |
| [**poly-maker**](https://github.com/warproxxx/poly-maker) | 1.5k | Python | 🟢 | Automated liquidity provision on Polymarket-style prediction markets. |
| [**coinbase-market-making-bot**](https://github.com/algotrading-lab/coinbase-market-making-bot) | 113 | TypeScript | 🟢 | Simple, focused market-making automation for Coinbase specifically without the overhead of a multi-exchange framework. |
| [**PinnacleMM**](https://github.com/chizy7/PinnacleMM) | 14 | C++ | 🟢 | Reference architecture for building a low-latency C++ market-making engine from scratch. |

<details><summary>Explainers (5)</summary>

**[Hummingbot](https://github.com/hummingbot/hummingbot)** · Python · ★ 20.1k · last push 2026-09-20  
An open-source framework purpose-built for deploying market-making and other liquidity-providing/arbitrage strategies across 100+ centralized and decentralized crypto exchanges. Ships with a strategy library (pure market making, cross-exchange MM, avellaneda-stoikov, arbitrage), a Docker-based deployment story, a companion Dashboard UI, and hummingbot-api for orchestrating fleets of bots.

✅ *Good at:* Production-grade crypto market making and cross-exchange arbitrage with connector abstractions handling exchange-specific order book/order-type quirks.  
⚠️ *Limitations:* Crypto-exchange focused (CEX/DEX), not applicable to traditional equities brokers like IBKR; strategy configuration has a learning curve.

**[Krypto-trading-bot (Tribeca)](https://github.com/ctubio/Krypto-trading-bot)** · C++ · ★ 3.7k · last push 2024-12-15  
A self-hosted, high-frequency crypto market-making bot written in C++ (a fork/continuation of the well-known 'Tribeca' market maker), designed for low-latency quoting across multiple crypto exchanges.

✅ *Good at:* Low-latency C++ market making for crypto exchanges where Python-based bots' latency is a bottleneck.  
⚠️ *Limitations:* Slower recent development pace; C++ build/ops complexity higher than Python alternatives like Hummingbot.

**[poly-maker](https://github.com/warproxxx/poly-maker)** · Python · ★ 1.5k · last push 2026-07-09  
An automated market-making bot for Polymarket prediction markets that maintains two-sided quotes with configurable spread/inventory parameters, reflecting the growing overlap between crypto/prediction-market bot infrastructure and traditional market-making techniques.

✅ *Good at:* Automated liquidity provision on Polymarket-style prediction markets.  
⚠️ *Limitations:* Polymarket/prediction-market specific, not applicable to equities or traditional crypto spot/futures exchanges.

**[coinbase-market-making-bot](https://github.com/algotrading-lab/coinbase-market-making-bot)** · TypeScript · ★ 113 · last push 2026-06-17  
A Coinbase-specific market-making bot that quotes both sides of the book to provide liquidity, illustrating a single-exchange, single-purpose alternative to the broader multi-exchange Hummingbot for teams that only need Coinbase.

✅ *Good at:* Simple, focused market-making automation for Coinbase specifically without the overhead of a multi-exchange framework.  
⚠️ *Limitations:* Single-exchange scope; smaller community/support than Hummingbot.

**[PinnacleMM](https://github.com/chizy7/PinnacleMM)** · C++ · ★ 14 · last push 2026-08-20  
An ultra-low-latency C++ market-making bot project actively developed as of mid-2026, aimed at demonstrating high-performance quoting architecture (lock-free data structures, custom order book) for crypto markets.

✅ *Good at:* Reference architecture for building a low-latency C++ market-making engine from scratch.  
⚠️ *Limitations:* Small, young project with limited exchange connector coverage compared to Hummingbot.

</details>

### FIX engines

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**QuickFIX**](https://github.com/quickfix/quickfix) | 2.0k | C++ | 🟢 | Battle-tested, standards-compliant FIX session and application-layer messaging for connecting to institutional brokers/venues that require FIX rather than a proprietary REST/socket API. |
| [**QuickFIX/J**](https://github.com/quickfix-j/quickfixj) | 1.2k | Java | 🟢 | Production-grade FIX connectivity for JVM-based OMS/EMS systems, with broad FIX version support and an active issue tracker/release cadence. |
| [**QuickFIX/Go**](https://github.com/quickfixgo/quickfix) | 897 | Go | 🟢 | Native Go FIX session/message handling for building custom order-routing gateways. |
| [**QuickFIX/n**](https://github.com/connamara/quickfixn) | 527 | C# | 🟢 | Production FIX connectivity for .NET trading infrastructure. |
| [**quickfix-python-samples**](https://github.com/rinlevan/quickfix-python-samples) | 94 | Python | 🟢 | Getting a minimal working Python FIX initiator/acceptor running quickly on top of the official QuickFIX C++/Python bindings. |

<details><summary>Explainers (5)</summary>

**[QuickFIX](https://github.com/quickfix/quickfix)** · C++ · ★ 2.0k · last push 2026-05-20  
The original, most widely deployed open-source FIX protocol engine, implemented in C++ with SWIG-generated bindings for Python, Ruby, and other languages (the `quickfix` PyPI package). Supports FIX 4.0 through 5.0/FIXT.1.1 and is the historical reference implementation that QuickFIX/J, QuickFIX/n, and QuickFIX/Go all derive their design from.

✅ *Good at:* Battle-tested, standards-compliant FIX session and application-layer messaging for connecting to institutional brokers/venues that require FIX rather than a proprietary REST/socket API.  
⚠️ *Limitations:* FIX protocol work is inherently config- and spec-heavy (data dictionaries, session management); C++ core with Python bindings adds a build step most other Python libraries don't require.

**[QuickFIX/J](https://github.com/quickfix-j/quickfixj)** · Java · ★ 1.2k · last push 2026-09-21  
The Java port of QuickFIX, a full-featured FIX messaging engine that remains actively maintained (commits as recent as the current date) and is very widely used in the Java/JVM institutional trading world for connecting to FIX-based brokers and ECNs.

✅ *Good at:* Production-grade FIX connectivity for JVM-based OMS/EMS systems, with broad FIX version support and an active issue tracker/release cadence.  
⚠️ *Limitations:* Same general FIX-protocol complexity/config overhead as any QuickFIX variant; JVM-specific.

**[QuickFIX/Go](https://github.com/quickfixgo/quickfix)** · Go · ★ 897 · last push 2026-09-14  
A Go implementation of the FIX protocol library, actively maintained, providing idiomatic Go APIs for building FIX initiators/acceptors -- useful for teams building high-throughput execution gateways in Go.

✅ *Good at:* Native Go FIX session/message handling for building custom order-routing gateways.  
⚠️ *Limitations:* Smaller ecosystem of examples/community support relative to QuickFIX/J or the original C++ QuickFIX.

**[QuickFIX/n](https://github.com/connamara/quickfixn)** · C# · ★ 527 · last push 2026-07-06  
The .NET implementation of the FIX protocol, maintained by Connamara Technologies, providing a mature FIX engine for C#/.NET-based OMS and execution systems.

✅ *Good at:* Production FIX connectivity for .NET trading infrastructure.  
⚠️ *Limitations:* Same FIX-protocol config/spec overhead common to the whole QuickFIX family.

**[quickfix-python-samples](https://github.com/rinlevan/quickfix-python-samples)** · Python · ★ 94 · last push 2026-05-30  
A community set of example initiator/acceptor applications using the official QuickFIX Python bindings (the `quickfix` pip package), useful as a starting template for building a Python FIX client/server against the C++ QuickFIX engine.

✅ *Good at:* Getting a minimal working Python FIX initiator/acceptor running quickly on top of the official QuickFIX C++/Python bindings.  
⚠️ *Limitations:* Example/teaching code, not a production library itself.

</details>

### TradingView webhook bridges

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**RogerThat (TradingView -> Hummingbot bridge)**](https://github.com/TheHolyRoger/RogerThat) | 61 | Python | 🟡 | Turning TradingView Pine Script alerts into live Hummingbot order actions without writing a custom webhook receiver. |
| [**tv2alpaca**](https://github.com/Juicestus/tv2alpaca) | 2 | Python | 🔴 | Minimal reference implementation for a TradingView-to-Alpaca webhook relay. |
| [**traderouter (TradingView -> NinjaTrader 8 bridge)**](https://github.com/roydufek/traderouter) | 0 | C# | 🟢 | Low-latency TradingView alert to NinjaTrader 8 order routing with multi-account trade copying. |

<details><summary>Explainers (3)</summary>

**[RogerThat (TradingView -> Hummingbot bridge)](https://github.com/TheHolyRoger/RogerThat)** · Python · ★ 61 · last push 2023-06-02  
A standalone webserver purpose-built to receive TradingView webhook alerts and forward them into a running Hummingbot instance, bridging TradingView's Pine Script alert system to crypto market-making/execution bots.

✅ *Good at:* Turning TradingView Pine Script alerts into live Hummingbot order actions without writing a custom webhook receiver.  
⚠️ *Limitations:* Narrowly scoped to Hummingbot as the downstream target; no commits in ~3 years.

**[tv2alpaca](https://github.com/Juicestus/tv2alpaca)** · Python · ★ 2 · last push 2021-03-27  
A small, simple TradingView webhook-to-Alpaca bridge translating incoming TradingView alert JSON into Alpaca order API calls -- representative of the many single-purpose TradingView-to-broker bridge scripts scattered across GitHub.

✅ *Good at:* Minimal reference implementation for a TradingView-to-Alpaca webhook relay.  
⚠️ *Limitations:* Unmaintained, toy-scale project; production use would require a rewrite with proper auth, idempotency, and error handling.

**[traderouter (TradingView -> NinjaTrader 8 bridge)](https://github.com/roydufek/traderouter)** · C# · ★ 0 · last push 2026-03-25  
A TradingView webhook bridge that executes trades on NinjaTrader 8 via a custom NT8 strategy, with fan-out trade copying across multiple accounts -- representative of the many small, single-purpose TradingView-to-broker relay services built for futures traders on NinjaTrader.

✅ *Good at:* Low-latency TradingView alert to NinjaTrader 8 order routing with multi-account trade copying.  
⚠️ *Limitations:* Very small/new project (0 stars); NinjaTrader-specific and Windows-only, mirroring the general fragmentation of TradingView bridge projects in this space.

</details>

### Other

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**awesome-systematic-trading**](https://github.com/wangzhe3224/awesome-systematic-trading) | 3.2k | unknown | 🟢 | Cross-referencing execution/live-trading frameworks across many languages and asset classes in one place, with explicit 'Live Trading' tagging for frameworks that actually support it (vs. backtest-only). |
| [**awesome-crypto-trading-bots**](https://github.com/botcrypto-io/awesome-crypto-trading-bots) | 2.5k | unknown | 🟢 | Quickly surveying the crypto trading bot landscape by category (frameworks, backtesting, exchange APIs, indicators). |
| [**MicroTrendsLtd/NinjaTrader8**](https://github.com/MicroTrendsLtd/NinjaTrader8) | 113 | C# | 🟡 | Extending NinjaTrader 8's own execution engine with community strategies/indicators for futures and equities day trading. |

<details><summary>Explainers (3)</summary>

**[awesome-systematic-trading](https://github.com/wangzhe3224/awesome-systematic-trading)** · unknown · ★ 3.2k · last push 2026-09-01  
A broad, actively maintained curated list covering systematic trading libraries across crypto, stocks, futures, options, CFDs and FX, including a dedicated 'Broker APIs' and 'Live Trading'-tagged frameworks section that surfaces projects like nautilus_trader, vnpy, pysystemtrade, aat, barter-rs, and the0.

✅ *Good at:* Cross-referencing execution/live-trading frameworks across many languages and asset classes in one place, with explicit 'Live Trading' tagging for frameworks that actually support it (vs. backtest-only).  
⚠️ *Limitations:* A list, not software; some linked entries are commercial/hosted products rather than pure open source.

**[awesome-crypto-trading-bots](https://github.com/botcrypto-io/awesome-crypto-trading-bots)** · unknown · ★ 2.5k · last push 2026-08-10  
A curated, actively updated list of open-source crypto trading bots, libraries, and frameworks -- a good discovery starting point complementary to this catalog for crypto-specific execution tooling.

✅ *Good at:* Quickly surveying the crypto trading bot landscape by category (frameworks, backtesting, exchange APIs, indicators).  
⚠️ *Limitations:* A list, not software; inclusion doesn't imply quality/maintenance vetting of every linked project.

**[MicroTrendsLtd/NinjaTrader8](https://github.com/MicroTrendsLtd/NinjaTrader8)** · C# · ★ 113 · last push 2024-08-08  
A collection of NinjaTrader 8 strategies, indicators, and trading tools built as C# NinjaScript add-ons for the proprietary NinjaTrader futures/equities platform, representative of how the NinjaTrader open-source ecosystem operates (add-ons to a closed platform rather than a standalone OSS broker connector).

✅ *Good at:* Extending NinjaTrader 8's own execution engine with community strategies/indicators for futures and equities day trading.  
⚠️ *Limitations:* NinjaTrader itself is closed-source/proprietary; these are UI-layer add-ons, not an independent OSS execution stack, and NinjaScript locks you into the Windows-only NinjaTrader platform.

</details>

[⬆ back to top](#contents)

## Prediction markets (Kalshi, Polymarket & more)

SDKs, market makers, arbitrage bots, forecasting agents and datasets for event contracts. Several of Polymarket's
official repos (including `py-clob-client` and `agents`) are **archived**. Community SDKs and “CCXT for prediction
markets” libraries (**pmxt**, **dr-manhattan**) now fill the gap.

**Key takeaways**

- **Jon-Becker/prediction-market-analysis** is the largest public Kalshi + Polymarket trade dataset, a strong first stop for research data.
- Cross-venue YES+NO arbitrage is a crowded, well-documented niche. Expect competition and fee changes.
- LLM forecasting bots cluster around Metaculus’s AI benchmarking tooling (**forecasting-tools**, **metac-bot-template**).
- Check jurisdictional access rules before trading. Kalshi is CFTC-regulated; Polymarket has restricted US retail access.

### Kalshi

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**kalshi-ai-trading-bot**](https://github.com/ryanfrigo/kalshi-ai-trading-bot) | 593 | Python | 🟢 | General-purpose scaffolding to go from idea to running Kalshi strategy quickly. |
| [**KalshiMarketMaker**](https://github.com/rodlaf/KalshiMarketMaker) | 398 | Python | 🟢 | Turnkey two-sided quoting strategy specifically tuned for Kalshi's contract structure. |
| [**kalshi-trading-bot-cli (Octagon)**](https://github.com/OctagonAI/kalshi-trading-bot-cli) | 387 | TypeScript | 🟢 | End-to-end LLM research-to-execution pipeline with explicit Kelly sizing and layered risk gates. |
| [**pykalshi**](https://github.com/arshka/pykalshi) | 125 | Python | 🟢 | Production-lean wrapper with streaming and pandas integration for building real trading systems on Kalshi. |
| [**Kalshi Starter Code (Python)**](https://github.com/Kalshi/kalshi-starter-code-python) | 99 | Python | 🟢 | Authoritative reference for Kalshi's RSA-PSS auth scheme and core REST endpoints straight from the exchange. |
| [**kalshi-market-making (QuantSC)**](https://github.com/nikhilnd/kalshi-market-making) | 82 | Jupyter Notebook | 🟠 | Clear pedagogical walk-through of market-making concepts applied to Kalshi contracts. |
| [**kalshi-cpp**](https://github.com/Reddimus/kalshi-cpp) | 74 | C++ | 🟢 | Low-latency, typed C++ access to Kalshi for teams building performance-sensitive trading engines. |
| [**kalshi-rust**](https://github.com/dpeachpeach/kalshi-rust) | 55 | Rust | 🟠 | Simple, early Rust entry point to the Kalshi REST API. |
| [**Kalshi S&P 500 Daily Bracket Trading**](https://github.com/quantgalore/kalshi-trading) | 41 | Python | 🟠 | Clear worked example of pricing daily range/bracket event contracts against a known underlying. |
| [**kalshi-rs**](https://github.com/arvchahal/kalshi-rs) | 36 | Rust | 🟢 | Wide endpoint coverage in Rust with websocket support for building fast, memory-safe Kalshi bots. |
| [**aiokalshi**](https://github.com/the-odds-company/aiokalshi) | 20 | Python | 🟢 | Async-first design for concurrent multi-market Kalshi bots. |
| [**kalshi-python-sdk (TexasCoding)**](https://github.com/TexasCoding/kalshi-python-sdk) | 6 | Python | 🟢 | Broadest documented REST + websocket endpoint coverage of any community Kalshi client, generated from the official spec. |

<details><summary>Explainers (12)</summary>

**[kalshi-ai-trading-bot](https://github.com/ryanfrigo/kalshi-ai-trading-bot)** · Python · ★ 593 · last push 2026-07-06  
A toolkit for building AI-automated trading strategies on Kalshi, packaging data access, strategy scaffolding, and execution so users can plug in their own signal or LLM logic. One of the higher-starred general-purpose Kalshi bot frameworks as of 2026.

✅ *Good at:* General-purpose scaffolding to go from idea to running Kalshi strategy quickly.  
⚠️ *Limitations:* Framework-level tool; strategy quality depends entirely on what the user plugs in.

**[KalshiMarketMaker](https://github.com/rodlaf/KalshiMarketMaker)** · Python · ★ 398 · last push 2026-04-14  
A deployable market-making bot for Kalshi that maintains two-sided quotes on selected event contracts, one of the higher-starred pure market-making implementations for the exchange. It is structured for people who want to run a simple spread-capture strategy against Kalshi's order book rather than directional bets.

✅ *Good at:* Turnkey two-sided quoting strategy specifically tuned for Kalshi's contract structure.  
⚠️ *Limitations:* Simple strategy logic with limited inventory/risk controls documented; needs tuning before live capital.

**[kalshi-trading-bot-cli (Octagon)](https://github.com/OctagonAI/kalshi-trading-bot-cli)** · TypeScript · ★ 387 · last push 2026-09-18  
An AI-native CLI for Kalshi that runs LLM-driven fundamental research on a market, generates an independent probability estimate, compares it against the live order book to compute edge, and executes trades sized with the Kelly criterion behind a 5-gate risk engine. Represents the emerging pattern of LLM-as-forecaster wired directly into exchange execution.

✅ *Good at:* End-to-end LLM research-to-execution pipeline with explicit Kelly sizing and layered risk gates.  
⚠️ *Limitations:* Relies on LLM probability estimates as ground truth, which can be systematically miscalibrated; young project.

**[pykalshi](https://github.com/arshka/pykalshi)** · Python · ★ 125 · last push 2026-07-29  
Unofficial Python client for Kalshi's prediction-market API that goes beyond the official starter code by adding websocket streaming, automatic retries/backoff, and pandas-friendly return types. It targets people building actual trading systems rather than one-off scripts, wrapping order placement, market/orderbook queries and portfolio endpoints in ergonomic interfaces. Actively updated through mid-2026.

✅ *Good at:* Production-lean wrapper with streaming and pandas integration for building real trading systems on Kalshi.  
⚠️ *Limitations:* Community-maintained and unofficial, so it can lag behind Kalshi API changes.

**[Kalshi Starter Code (Python)](https://github.com/Kalshi/kalshi-starter-code-python)** · Python · ★ 99 · last push 2025-03-07  
Kalshi's own reference implementation for authenticating (RSA-PSS signed requests) and calling the Kalshi Trade API v2 from Python. It demonstrates order placement, market data retrieval, and portfolio endpoints in a minimal script form rather than a packaged SDK. Most third-party Kalshi clients (pykalshi, kalshi-python-sdk, aiokalshi) cite this repo as their starting point. It is the canonical place to see Kalshi's expected auth flow.

✅ *Good at:* Authoritative reference for Kalshi's RSA-PSS auth scheme and core REST endpoints straight from the exchange.  
⚠️ *Limitations:* Bare-bones starter script, not a maintained SDK with retries, pagination or websocket support.

**[kalshi-market-making (QuantSC)](https://github.com/nikhilnd/kalshi-market-making)** · Jupyter Notebook · ★ 82 · last push 2023-05-18  
A university quant-club (QuantSC) research project exploring market-making strategies on Kalshi, delivered as notebooks rather than a production bot. Useful as an educational reference for how to think about quoting logic and inventory risk on event contracts.

✅ *Good at:* Clear pedagogical walk-through of market-making concepts applied to Kalshi contracts.  
⚠️ *Limitations:* Research/teaching artifact, not maintained or execution-ready.

**[kalshi-cpp](https://github.com/Reddimus/kalshi-cpp)** · C++ · ★ 74 · last push 2026-09-04  
A modern C++23 SDK for the Kalshi API offering full typed REST coverage plus real-time WebSocket streaming, RSA-PSS authentication, and an exception-free std::expected-based error-handling API. Built to be CMake/FetchContent-ready for embedding into low-latency C++ trading infrastructure rather than scripting use cases.

✅ *Good at:* Low-latency, typed C++ access to Kalshi for teams building performance-sensitive trading engines.  
⚠️ *Limitations:* Niche language choice narrows the contributor/user base relative to Python/TS clients.

**[kalshi-rust](https://github.com/dpeachpeach/kalshi-rust)** · Rust · ★ 55 · last push 2024-08-26  
An earlier Rust client/wrapper for the Kalshi trading API, one of the first community Rust SDKs for Kalshi. Provides basic REST coverage for authentication, markets, and orders.

✅ *Good at:* Simple, early Rust entry point to the Kalshi REST API.  
⚠️ *Limitations:* No commits since mid-2024; likely stale relative to current Kalshi API surface.

**[Kalshi S&P 500 Daily Bracket Trading](https://github.com/quantgalore/kalshi-trading)** · Python · ★ 41 · last push 2023-11-05  
A system for trading Kalshi's daily S&P 500 bracket (range) contracts by modeling the probability the index closes within specific bands, from the well-known QuantGalore quant-education channel. Illustrative of how to translate an options-like payoff structure into a Kalshi-specific strategy.

✅ *Good at:* Clear worked example of pricing daily range/bracket event contracts against a known underlying.  
⚠️ *Limitations:* No commits since 2023; contract specs and fee schedule referenced may be outdated.

**[kalshi-rs](https://github.com/arvchahal/kalshi-rs)** · Rust · ★ 36 · last push 2026-09-02  
A fully-featured Rust SDK integrating over 50 Kalshi API endpoints with websocket support, intended for Rust-based algorithmic trading systems that want compile-time safety and high throughput. Complements the smaller dpeachpeach/kalshi-rust wrapper with broader endpoint coverage.

✅ *Good at:* Wide endpoint coverage in Rust with websocket support for building fast, memory-safe Kalshi bots.  
⚠️ *Limitations:* Single-maintainer project; API stability and long-term support are unproven.

**[aiokalshi](https://github.com/the-odds-company/aiokalshi)** · Python · ★ 20 · last push 2025-10-09  
An asyncio-native Kalshi API client built by The Odds Company, aimed at bots that need concurrent order management and market data polling without blocking. It wraps authentication and the core trade/portfolio endpoints in async methods so it composes naturally with asyncio-based trading loops and websocket consumers.

✅ *Good at:* Async-first design for concurrent multi-market Kalshi bots.  
⚠️ *Limitations:* Smaller community and less documentation than the more popular unofficial clients.

**[kalshi-python-sdk (TexasCoding)](https://github.com/TexasCoding/kalshi-python-sdk)** · Python · ★ 6 · last push 2026-09-20  
A spec-first, actively developed Python SDK claiming near-complete coverage of the Kalshi REST API (107 of 108 documented operations across 19 resources, generated against the published OpenAPI v3.29.0 spec) plus the WebSocket API with 11 typed subscribe_* channels and escape-hatch raw access. Positioned as a more complete alternative to lighter unofficial clients for teams that want full endpoint coverage with typed models.

✅ *Good at:* Broadest documented REST + websocket endpoint coverage of any community Kalshi client, generated from the official spec.  
⚠️ *Limitations:* Very new/low-star project; unofficial and unproven in production at scale.

</details>

### Polymarket

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**Polymarket/agents**](https://github.com/Polymarket/agents) | 3.8k | Python | 🟠 | Reference architecture for wiring LLM research into Polymarket order execution, MIT-licensed and widely forked. |
| [**polymarket-cli**](https://github.com/Polymarket/polymarket-cli) | 2.9k | Rust | 🟢 | Officially supported, actively maintained terminal access to Polymarket without writing custom client code. |
| [**5min-btc-polymarket**](https://github.com/Novals83/5min-btc-polymarket) | 1.3k | Python | 🟢 | High community adoption (1,300+ stars) for a specific, popular ultra-short-duration BTC market niche. |
| [**py-clob-client**](https://github.com/Polymarket/py-clob-client) | 1.2k | Python | 🟠 | Canonical, widely-adopted Python interface to Polymarket's CLOB with correct order-signing semantics. |
| [**polybot**](https://github.com/ent0n29/polybot) | 1.0k | Java | 🟢 | Detailed HFT-oriented execution/market-data infrastructure with paper trading, unusual in choosing Java for this space. |
| [**rs-clob-client**](https://github.com/Polymarket/rs-clob-client) | 686 | Rust | 🟢 | Currently the most actively maintained official Polymarket client, well-suited to latency-sensitive execution. |
| [**polymarket-mcp-server**](https://github.com/caiovicentino/polymarket-mcp-server) | 673 | Python | 🟢 | Broad, ready-made MCP tool surface for wiring an LLM agent directly into Polymarket trading. |
| [**Polymarket-BTC-15-Minute-Trading-Bot**](https://github.com/aulekator/Polymarket-BTC-15-Minute-Trading-Bot) | 587 | Python | 🟢 | Well-documented multi-phase architecture (signals -> risk -> self-learning) for short-duration BTC prediction markets. |
| [**polymarket_lp_tool**](https://github.com/lihanyu81/polymarket_lp_tool) | 528 | Python | 🟢 | High-star, actively used LP-focused tool distinct from full directional trading bots. |
| [**polymarket-arbitrage-trading-bot (radioman)**](https://github.com/radioman/polymarket-arbitrage-trading-bot) | 522 | C++ | 🟢 | Latency-focused C++ implementation for the highly competitive 5-minute BTC/ETH market niche. |
| [**clob-client (TypeScript)**](https://github.com/Polymarket/clob-client) | 514 | TypeScript | 🟠 | Official, well-documented TypeScript entry point to Polymarket's CLOB for Node/browser-adjacent tooling. |
| [**clob-client-v2 (community)**](https://github.com/dev-polymarket/clob-client-v2) | 512 | TypeScript | 🟢 | Up-to-date TypeScript access to CLOB v2 features not present in the archived official client. |
| [**polymarket-paper-trader**](https://github.com/agent-next/polymarket-paper-trader) | 394 | Python | 🟢 | Purpose-built safe sandbox (live order books + MCP) for AI agents to develop and test Polymarket strategies before going live. |
| [**cross-market-state-fusion**](https://github.com/humanplane/cross-market-state-fusion) | 383 | Python | 🟢 | Genuinely novel technical approach: RL policy fusing an external asset's live microstructure into prediction-market trading decisions. |
| [**polyterm**](https://github.com/NYTEMODEONLY/polyterm) | 358 | Python | 🟢 | Fast, low-overhead terminal dashboard for keeping an eye on Polymarket markets. |
| [**ctf-exchange**](https://github.com/Polymarket/ctf-exchange) | 355 | Solidity | 🟠 | Ground-truth on-chain settlement logic for Polymarket markets, useful for building accurate arbitrage/settlement models. |
| [**poly-market-maker**](https://github.com/Polymarket/poly-market-maker) | 323 | Python | 🟠 | Official reference architecture for building a Polymarket-compliant market-making keeper. |
| [**polymarket-trade-engine**](https://github.com/KaustubhPatange/polymarket-trade-engine) | 316 | TypeScript | 🟢 | Dedicated execution engine abstraction for Polymarket's short-duration binary market family. |
| [**PolyWeather**](https://github.com/yangyuan-zhen/PolyWeather) | 307 | Python | 🟢 | Actively updated (through September 2026) dedicated weather-market quant analysis for Polymarket. |
| [**polymarket-terminal**](https://github.com/direkturcrypto/polymarket-terminal) | 290 | JavaScript | 🟢 | Combines three distinct tactical patterns (copy, scalp, snipe) in one integrated tool rather than three separate scripts. |
| [**polymarket-subgraph**](https://github.com/Polymarket/polymarket-subgraph) | 217 | TypeScript | 🟢 | Authoritative, queryable on-chain data schema for Polymarket trades and liquidity. |
| [**OctoBot-Prediction-Market**](https://github.com/Drakkar-Software/OctoBot-Prediction-Market) | 114 | Python | 🟢 | Leverages a mature, established bot framework (OctoBot) rather than a from-scratch implementation. |
| [**polymarket-subgraph-analytics**](https://github.com/PaulieB14/polymarket-subgraph-analytics) | 54 | unknown | 🟢 | Practical worked queries/patterns for extracting insights from Polymarket's subgraph data. |
| [**polymarket-gamma (TypeScript)**](https://github.com/0xJord4n/polymarket-gamma) | 12 | TypeScript | 🟢 | Typed, ergonomic access to Polymarket's Gamma metadata API for TypeScript projects. |

<details><summary>Explainers (24)</summary>

**[Polymarket/agents](https://github.com/Polymarket/agents)** · Python · ★ 3.8k · last push 2024-11-05  
Polymarket's own developer framework for building AI agents that trade autonomously on Polymarket: connectors for market/order data, LLM-based research and probability estimation, and order execution via the CLOB client. It is the most-starred official artifact in the prediction-market agent space and the template most community forks (poly-agents, pm_agents, PolyAgent) build on. GitHub now marks the repository archived, meaning Polymarket is no longer actively developing it.

✅ *Good at:* Reference architecture for wiring LLM research into Polymarket order execution, MIT-licensed and widely forked.  
⚠️ *Limitations:* Archived by Polymarket (no longer maintained), so it needs adaptation for current CLOB/API changes.

**[polymarket-cli](https://github.com/Polymarket/polymarket-cli)** · Rust · ★ 2.9k · last push 2026-05-26  
Polymarket's official command-line interface for browsing markets and interacting with the exchange from the terminal, built in Rust. High star count and recent activity make it one of the most credible officially-supported entry points into Polymarket tooling in 2026.

✅ *Good at:* Officially supported, actively maintained terminal access to Polymarket without writing custom client code.  
⚠️ *Limitations:* CLI-first design is less suited to embedding directly into an automated trading engine than the SDKs.

**[5min-btc-polymarket](https://github.com/Novals83/5min-btc-polymarket)** · Python · ★ 1.3k · last push 2026-04-11  
An OpenClaw skill implementing BTC 5-minute momentum trading on Polymarket's short-duration up/down markets, with configurable risk controls and optional hedge logic. Reflects the very active niche of ultra-short-duration crypto-price prediction markets, which several other projects in this catalog (aulekator's 15-minute bot, humanplane's RL fusion bot) also target.

✅ *Good at:* High community adoption (1,300+ stars) for a specific, popular ultra-short-duration BTC market niche.  
⚠️ *Limitations:* 5-minute BTC markets are extremely competitive/fee-sensitive; documented 2026 changes to Polymarket's taker delay and fees may have degraded some of these strategies' edges.

**[py-clob-client](https://github.com/Polymarket/py-clob-client)** · Python · ★ 1.2k · last push 2026-05-25  
Polymarket's official Python client for its Central Limit Order Book (CLOB), handling EIP-712 order signing, order placement/cancellation, and market/orderbook queries. It is the foundation almost every Python-based Polymarket bot in this catalog (poly-maker, homerun, arbitrage bots) builds on. The repo is archived on GitHub despite a 2026 last push, so treat it as feature-frozen.

✅ *Good at:* Canonical, widely-adopted Python interface to Polymarket's CLOB with correct order-signing semantics.  
⚠️ *Limitations:* Archived/frozen; newer CLOB features may only appear in the community clob-client-v2 or Rust/CLI clients.

**[polybot](https://github.com/ent0n29/polybot)** · Java · ★ 1.0k · last push 2026-02-20  
A reverse-engineered reimplementation of Polymarket trading strategies and high-frequency execution infrastructure, built in Java. Positioned as a study/reference of how HFT-style infrastructure could be built for Polymarket rather than a single packaged strategy.

✅ *Good at:* Detailed HFT-oriented execution/market-data infrastructure with paper trading, unusual in choosing Java for this space.  
⚠️ *Limitations:* Framed as a reverse-engineering exercise; strategy claims should be independently verified before trusting with capital.

**[rs-clob-client](https://github.com/Polymarket/rs-clob-client)** · Rust · ★ 686 · last push 2026-05-11  
Polymarket's official Rust CLOB client, providing lower-latency access to order placement and market data than the Python/TS clients for teams building performance-sensitive Rust trading infrastructure. Actively pushed through mid-2026, unlike its Python/TS siblings which are archived.

✅ *Good at:* Currently the most actively maintained official Polymarket client, well-suited to latency-sensitive execution.  
⚠️ *Limitations:* Smaller ecosystem of examples/tutorials compared to the (now archived) Python client.

**[polymarket-mcp-server](https://github.com/caiovicentino/polymarket-mcp-server)** · Python · ★ 673 · last push 2026-09-20  
An MCP (Model Context Protocol) server exposing 45 tools for Polymarket, letting Claude or other MCP-compatible LLM clients browse markets, monitor positions in real time, and place trades with stated 'enterprise-grade' safety guardrails. Represents the pattern of exposing exchange functionality directly to LLM agents via MCP rather than a bespoke agent framework.

✅ *Good at:* Broad, ready-made MCP tool surface for wiring an LLM agent directly into Polymarket trading.  
⚠️ *Limitations:* Safety-guardrail claims are self-described; independent audit of the trading-safety logic is advisable before live use.

**[Polymarket-BTC-15-Minute-Trading-Bot](https://github.com/aulekator/Polymarket-BTC-15-Minute-Trading-Bot)** · Python · ★ 587 · last push 2026-02-28  
A production-grade algorithmic trading bot for Polymarket's 15-minute BTC price prediction markets, combining multiple signal sources in a 7-phase architecture with professional risk management and self-learning capabilities. One of the more architecturally detailed short-duration crypto-market bots in the catalog.

✅ *Good at:* Well-documented multi-phase architecture (signals -> risk -> self-learning) for short-duration BTC prediction markets.  
⚠️ *Limitations:* 'Self-learning' and 'production-grade' claims are self-described and not independently verified in this survey.

**[polymarket_lp_tool](https://github.com/lihanyu81/polymarket_lp_tool)** · Python · ★ 528 · last push 2026-05-06  
A liquidity-provision tool for Polymarket, one of several higher-starred community market-making/LP utilities alongside poly-maker, aimed at users earning Polymarket's liquidity-mining/maker rewards.

✅ *Good at:* High-star, actively used LP-focused tool distinct from full directional trading bots.  
⚠️ *Limitations:* Documentation is sparse in English; description alone does not clarify how it differs from poly-maker's approach.

**[polymarket-arbitrage-trading-bot (radioman)](https://github.com/radioman/polymarket-arbitrage-trading-bot)** · C++ · ★ 522 · last push 2026-06-19  
A C++ arbitrage bot targeting BTC and ETH 5-minute Polymarket prediction markets, combining automated execution, real-time analytics, and smart-wallet copy trading in one tool. The choice of C++ suggests a latency focus relative to the more common Python/TypeScript implementations of similar 5-minute-market bots.

✅ *Good at:* Latency-focused C++ implementation for the highly competitive 5-minute BTC/ETH market niche.  
⚠️ *Limitations:* C++ raises the bar for community contribution/auditing compared to the more common scripting-language bots.

**[clob-client (TypeScript)](https://github.com/Polymarket/clob-client)** · TypeScript · ★ 514 · last push 2026-05-25  
Polymarket's official TypeScript/Node client for the CLOB, mirroring py-clob-client's functionality (order signing, placement, market data) for JS-based bots and frontends. Widely used by Node-based Polymarket trading bots and dashboards. Also marked archived on GitHub.

✅ *Good at:* Official, well-documented TypeScript entry point to Polymarket's CLOB for Node/browser-adjacent tooling.  
⚠️ *Limitations:* Archived; community successor clob-client-v2 (unofficial org) has since emerged for V2 CLOB features.

**[clob-client-v2 (community)](https://github.com/dev-polymarket/clob-client-v2)** · TypeScript · ★ 512 · last push 2026-09-18  
A community-maintained TypeScript client targeting Polymarket's V2 CLOB, filling the gap left by the official clob-client's archival. Fast-growing star count in 2026 suggests it has become a de facto successor for TS developers needing current CLOB v2 support. Note this is published under the 'dev-polymarket' org, not the official 'Polymarket' org — verify authenticity before trusting it with funds.

✅ *Good at:* Up-to-date TypeScript access to CLOB v2 features not present in the archived official client.  
⚠️ *Limitations:* Unofficial third-party org; not vetted or endorsed by Polymarket, so extra scrutiny is warranted before production use.

**[polymarket-paper-trader](https://github.com/agent-next/polymarket-paper-trader)** · Python · ★ 394 · last push 2026-08-15  
A paper-trading simulator for Polymarket built specifically for AI agents to practice against, including an MCP server, live order books, and strategy backtesting, installable via a simple npx clawhub command. Fills the important niche of letting an LLM agent iterate on strategy safely before risking real funds.

✅ *Good at:* Purpose-built safe sandbox (live order books + MCP) for AI agents to develop and test Polymarket strategies before going live.  
⚠️ *Limitations:* Paper-trading realism (slippage, fee, and fill-probability modeling) is not independently verified in this survey.

**[cross-market-state-fusion](https://github.com/humanplane/cross-market-state-fusion)** · Python · ★ 383 · last push 2026-01-03  
A reinforcement-learning agent that fuses real-time Binance futures order-flow data into Polymarket prediction-market decisions, trained on-device using Apple's MLX framework on Apple Silicon. Notable for its unusual technical approach (RL + cross-asset fusion + on-device MLX training) compared to the more common rules-based or LLM-prompted bots in this catalog.

✅ *Good at:* Genuinely novel technical approach: RL policy fusing an external asset's live microstructure into prediction-market trading decisions.  
⚠️ *Limitations:* RL trading policies are notoriously hard to validate out-of-sample; MLX/Apple Silicon requirement limits deployment portability.

**[polyterm](https://github.com/NYTEMODEONLY/polyterm)** · Python · ★ 358 · last push 2026-09-06  
A terminal user-interface application for browsing and monitoring Polymarket directly from the command line, giving traders a lightweight always-on view of markets without a browser. Actively updated through September 2026.

✅ *Good at:* Fast, low-overhead terminal dashboard for keeping an eye on Polymarket markets.  
⚠️ *Limitations:* Primarily a viewing/monitoring tool, not an execution or strategy engine.

**[ctf-exchange](https://github.com/Polymarket/ctf-exchange)** · Solidity · ★ 355 · last push 2026-05-11  
Polymarket's official Solidity smart contracts implementing the Conditional Token Framework (CTF) exchange that settles trades on-chain. It's the reference for anyone building market-making or arbitrage tooling that needs to reason precisely about on-chain settlement, fees, and negative-risk (NegRisk) market mechanics. Archived, so treated as the historical/audited reference version.

✅ *Good at:* Ground-truth on-chain settlement logic for Polymarket markets, useful for building accurate arbitrage/settlement models.  
⚠️ *Limitations:* Archived reference contracts; current production contracts may have since evolved beyond this snapshot.

**[poly-market-maker](https://github.com/Polymarket/poly-market-maker)** · Python · ★ 323 · last push 2024-07-05  
Polymarket's official 'keeper' market-making bot for the CLOB, designed to run automated liquidity provision strategies against Polymarket order books. Provided as a reference implementation for market makers rather than a fully managed service.

✅ *Good at:* Official reference architecture for building a Polymarket-compliant market-making keeper.  
⚠️ *Limitations:* No commits since mid-2024; likely needs updates for current CLOB fee/negRisk mechanics.

**[polymarket-trade-engine](https://github.com/KaustubhPatange/polymarket-trade-engine)** · TypeScript · ★ 316 · last push 2026-06-08  
An automated trading engine for Polymarket's binary prediction markets (e.g. BTC Up/Down 5-minute contracts), providing the execution plumbing that strategy logic can be layered on top of.

✅ *Good at:* Dedicated execution engine abstraction for Polymarket's short-duration binary market family.  
⚠️ *Limitations:* Positioned as execution infrastructure; strategy/signal generation is left to the user.

**[PolyWeather](https://github.com/yangyuan-zhen/PolyWeather)** · Python · ★ 307 · last push 2026-09-20  
An intelligent weather quantitative-analysis bot for Polymarket weather markets, a second independent entry (alongside suislanchez's Kalshi+Polymarket weather bot) in the increasingly well-tooled weather-derivatives-on-prediction-markets niche.

✅ *Good at:* Actively updated (through September 2026) dedicated weather-market quant analysis for Polymarket.  
⚠️ *Limitations:* Single-venue (Polymarket only) and single-niche (weather), narrower scope than cross-venue weather bots.

**[polymarket-terminal](https://github.com/direkturcrypto/polymarket-terminal)** · JavaScript · ★ 290 · last push 2026-04-03  
A terminal/dashboard tool for Polymarket combining copy trading, scalping, and sniper functionality: watching target wallets and mirroring trades, or racing to enter newly-listed markets ahead of the crowd.

✅ *Good at:* Combines three distinct tactical patterns (copy, scalp, snipe) in one integrated tool rather than three separate scripts.  
⚠️ *Limitations:* Sniper/scalper strategies are inherently latency-sensitive and adversarial, with edges likely to erode as adoption grows.

**[polymarket-subgraph](https://github.com/Polymarket/polymarket-subgraph)** · TypeScript · ★ 217 · last push 2026-02-13  
Polymarket's official Graph Protocol subgraph manifest for indexing on-chain trades, volume, users, liquidity, and market data. This is the standard way to build historical/analytics datasets from Polymarket's on-chain activity without scraping, and underlies several third-party analytics repos in this catalog.

✅ *Good at:* Authoritative, queryable on-chain data schema for Polymarket trades and liquidity.  
⚠️ *Limitations:* Requires familiarity with The Graph/subgraph tooling and a hosted or self-run indexer to query.

**[OctoBot-Prediction-Market](https://github.com/Drakkar-Software/OctoBot-Prediction-Market)** · Python · ★ 114 · last push 2026-03-30  
A free, open-source Polymarket module from the established OctoBot crypto-trading-bot project, automating copy trading and arbitrage strategies on Polymarket with OctoBot's existing simple-interface bot framework. Benefits from OctoBot's broader ecosystem (backtesting, plugin architecture) built for crypto exchanges and extended to prediction markets.

✅ *Good at:* Leverages a mature, established bot framework (OctoBot) rather than a from-scratch implementation.  
⚠️ *Limitations:* Prediction-market support is an add-on module to a crypto-focused platform, so depth may lag dedicated prediction-market bots.

**[polymarket-subgraph-analytics](https://github.com/PaulieB14/polymarket-subgraph-analytics)** · unknown · ★ 54 · last push 2025-08-02  
A guide/toolkit for building Polymarket analytics on top of the official subgraph, covering hot-market discovery, trading insight queries, and real-time data pipelines. Useful as a worked example for turning the raw subgraph schema into usable dashboards.

✅ *Good at:* Practical worked queries/patterns for extracting insights from Polymarket's subgraph data.  
⚠️ *Limitations:* Documentation/example repo rather than a packaged, versioned library.

**[polymarket-gamma (TypeScript)](https://github.com/0xJord4n/polymarket-gamma)** · TypeScript · ★ 12 · last push 2025-11-23  
A type-safe TypeScript client wrapping Polymarket's Gamma API (the read-oriented metadata API for markets, events, and tags, distinct from the CLOB trading API). Useful for building data/analytics tooling that needs typed access to market metadata without touching order execution.

✅ *Good at:* Typed, ergonomic access to Polymarket's Gamma metadata API for TypeScript projects.  
⚠️ *Limitations:* Covers only the read-only Gamma API, not CLOB trading.

</details>

### Cross-venue & unified SDKs

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**polymarket-kalshi-weather-bot**](https://github.com/suislanchez/polymarket-kalshi-weather-bot) | 757 | Python | 🟢 | Rigorous use of ensemble numerical weather forecasts to price a specific, well-understood event-market niche. |
| [**HarrierOnChain Prediction-Markets-Trading-Bot-Toolkits**](https://github.com/HarrierOnChain/Prediction-Markets-Trading-Bot-Toolkits) | 453 | Rust | 🟢 | Unified Rust execution core covering multiple strategy types (copy trade, arb, MM) across three venues with safety-first defaults. |
| [**poly-kalshi-arb**](https://github.com/taetaehoho/poly-kalshi-arb) | 446 | Rust | 🟢 | Clean, well-documented implementation of the classic YES+NO<1 cross-venue arbitrage mechanic. |
| [**polymarket-arbitrage (ImMike)**](https://github.com/ImMike/polymarket-arbitrage) | 282 | Python | 🟢 | Large-scale simultaneous market coverage (10,000+) for spotting both intra- and cross-venue mispricings. |
| [**polymarket-kalshi-btc-arbitrage-bot**](https://github.com/CarlosIbCu/polymarket-kalshi-btc-arbitrage-bot) | 250 | Python | 🟢 | Focused, fast-moving detection for one specific high-liquidity market family (BTC 1-hour brackets). |
| [**dr-manhattan**](https://github.com/guzus/dr-manhattan) | 201 | Jupyter Notebook | 🟢 | Widest documented venue coverage (5+ exchanges) among unified prediction-market APIs found in this survey. |
| [**homerun**](https://github.com/braedonsaunders/homerun) | 181 | Python | 🟢 | Most complete self-contained platform found (backtest -> paper -> live, dashboard, 25+ strategies) rather than a single-purpose bot. |
| [**prediction-market-arbitrage-bot (realfishsam)**](https://github.com/realfishsam/prediction-market-arbitrage-bot) | 178 | JavaScript | 🟢 | Simple, pmxt-based reference implementation of automated cross-venue arb execution. |
| [**predmarket**](https://github.com/ashercn97/predmarket) | 95 | Python | 🟢 | Lightweight, Python-native two-venue (Kalshi + Polymarket) unification without the broader multi-venue scope of pmxt. |
| [**truthlayer**](https://github.com/rohanthomas1202/truthlayer) | 65 | Python | 🟢 | Sophisticated LLM+embedding market-matching approach that addresses the core cross-venue arbitrage challenge of equivalence detection. |
| [**prediction-market-arb (bogdan-cvs)**](https://github.com/bogdan-cvs/prediction-market-arb) | 0 | Python | 🟢 | Rare inclusion of ForecastEx/IBKR alongside the usual crypto-native prediction venues. |

<details><summary>Explainers (11)</summary>

**[polymarket-kalshi-weather-bot](https://github.com/suislanchez/polymarket-kalshi-weather-bot)** · Python · ★ 757 · last push 2026-03-02  
A multi-platform bot trading weather temperature markets (Kalshi's KXHIGH series) and equivalent Polymarket markets using a 31-member GFS ensemble weather forecast plus BTC 5-minute microstructure signals, with Kelly-criterion sizing, signal calibration, and a React dashboard. One of the more sophisticated and well-documented niche-market strategies in the catalog, reporting up to $1.8k peak profits.

✅ *Good at:* Rigorous use of ensemble numerical weather forecasts to price a specific, well-understood event-market niche.  
⚠️ *Limitations:* Highly specialized to weather + BTC microstructure; not a general-purpose framework, and reported profits are self-reported.

**[HarrierOnChain Prediction-Markets-Trading-Bot-Toolkits](https://github.com/HarrierOnChain/Prediction-Markets-Trading-Bot-Toolkits)** · Rust · ★ 453 · last push 2026-09-07  
A set of Rust trading bots sharing one execution core across Polymarket, Kalshi and Limitless. Copy trading is described as production-ready, with nine more strategies (market making, arbitrage, sniping, spread farming) in development on the same venue-agnostic adapter stack. Ships dry-run-by-default and self-custody, and the same author/org has separate single-venue repos (Drift-BET, Limitless-Exchange) sharing the pattern.

✅ *Good at:* Unified Rust execution core covering multiple strategy types (copy trade, arb, MM) across three venues with safety-first defaults.  
⚠️ *Limitations:* Most strategies beyond copy trading are described as still in development, not yet production-ready.

**[poly-kalshi-arb](https://github.com/taetaehoho/poly-kalshi-arb)** · Rust · ★ 446 · last push 2025-12-21  
An open-sourced Kalshi-Polymarket (and Poly-Poly / Kalshi-Kalshi) arbitrage bot that takes positions on both sides of a market whenever YES and NO prices sum to less than 1, locking in a risk-free profit at settlement. The author publicly documented the mechanic and open-sourced it on X, giving unusually clear provenance for a small arb bot.

✅ *Good at:* Clean, well-documented implementation of the classic YES+NO<1 cross-venue arbitrage mechanic.  
⚠️ *Limitations:* This specific mispricing has become rarer/thinner as more bots compete for it in 2026; requires fast execution to capture.

**[polymarket-arbitrage (ImMike)](https://github.com/ImMike/polymarket-arbitrage)** · Python · ★ 282 · last push 2025-12-09  
A Polymarket/Kalshi arbitrage scanner in Python that watches 10,000+ markets simultaneously for inefficient pricing within a single platform and between the two platforms, one of the broader-scope scanners in terms of market count.

✅ *Good at:* Large-scale simultaneous market coverage (10,000+) for spotting both intra- and cross-venue mispricings.  
⚠️ *Limitations:* Scanner-focused; execution and risk management are left to the user to build out.

**[polymarket-kalshi-btc-arbitrage-bot](https://github.com/CarlosIbCu/polymarket-kalshi-btc-arbitrage-bot)** · Python · ★ 250 · last push 2026-05-09  
A real-time arbitrage bot specifically targeting Bitcoin 1-hour price markets, detecting risk-free spreads between equivalent Polymarket and Kalshi contracts. Narrow-scope but focused on one of the most liquid recurring event-market categories (short-duration BTC price brackets).

✅ *Good at:* Focused, fast-moving detection for one specific high-liquidity market family (BTC 1-hour brackets).  
⚠️ *Limitations:* Narrow scope means it offers no coverage outside BTC hourly markets.

**[dr-manhattan](https://github.com/guzus/dr-manhattan)** · Jupyter Notebook · ★ 201 · last push 2026-07-18  
Another 'CCXT for prediction markets' project, providing a unified API for market-making, trading, and data analysis across Polymarket, Kalshi, Limitless, Opinion, Predict.fun and more, with companion TypeScript (dr-manhattan-ts) and Rust (dr-manhattan-rust) ports maintained by a related author. Notebook-first delivery suggests a research/analysis orientation alongside the trading API.

✅ *Good at:* Widest documented venue coverage (5+ exchanges) among unified prediction-market APIs found in this survey.  
⚠️ *Limitations:* Primary repo is Jupyter-notebook-centric, which is less convenient for embedding in a production service than the TS/Rust ports.

**[homerun](https://github.com/braedonsaunders/homerun)** · Python · ★ 181 · last push 2026-08-21  
An open-source prediction-market trading platform spanning Polymarket and Kalshi that lets users write full Python strategies and data sources, backtest them, then run paper or live trading. Ships 25+ built-in strategies, copy trading, AI-based scoring, a real-time dashboard, and a one-click setup, making it one of the more complete self-contained platforms in the catalog rather than a single bot.

✅ *Good at:* Most complete self-contained platform found (backtest -> paper -> live, dashboard, 25+ strategies) rather than a single-purpose bot.  
⚠️ *Limitations:* Broad scope means individual strategies may be shallower than a dedicated single-strategy bot; newer project with less battle-testing.

**[prediction-market-arbitrage-bot (realfishsam)](https://github.com/realfishsam/prediction-market-arbitrage-bot)** · JavaScript · ★ 178 · last push 2026-01-16  
An arbitrage bot that detects and auto-executes buy-low/sell-high opportunities between Polymarket and Kalshi, built directly on top of the pmxt unified API. A companion scanner-only repo (prediction-markets-arbitrage-scan) from the same author strips out execution for a lighter-weight detection tool.

✅ *Good at:* Simple, pmxt-based reference implementation of automated cross-venue arb execution.  
⚠️ *Limitations:* Depends on pmxt's abstraction layer, inheriting any of its venue-specific coverage gaps.

**[predmarket](https://github.com/ashercn97/predmarket)** · Python · ★ 95 · last push 2025-10-09  
A unified Python SDK for prediction markets aiming to simplify access to both Kalshi and Polymarket behind one API for data integration and (per a related fork/rename, elsantos305/predmarket) trading workflows. Smaller-scope alternative to pmxt/dr-manhattan focused specifically on the Kalshi+Polymarket pair.

✅ *Good at:* Lightweight, Python-native two-venue (Kalshi + Polymarket) unification without the broader multi-venue scope of pmxt.  
⚠️ *Limitations:* Narrower venue coverage than pmxt or dr-manhattan (Kalshi + Polymarket only).

**[truthlayer](https://github.com/rohanthomas1202/truthlayer)** · Python · ★ 65 · last push 2026-04-20  
A real-time cross-market arbitrage scanner for Polymarket and Kalshi that uses multi-tier matching (FAISS vector similarity plus a Claude LLM pass) to match semantically-equivalent markets across venues, then computes fee-adjusted spreads with a settlement-verified scoreboard tracking actual outcomes. Notable for tackling the hard part of cross-venue arb: reliably identifying which markets are truly equivalent.

✅ *Good at:* Sophisticated LLM+embedding market-matching approach that addresses the core cross-venue arbitrage challenge of equivalence detection.  
⚠️ *Limitations:* LLM-in-the-loop matching adds latency and cost versus simpler keyword/ID-based matching schemes.

**[prediction-market-arb (bogdan-cvs)](https://github.com/bogdan-cvs/prediction-market-arb)** · Python · ★ 0 · last push 2026-03-06  
A cross-platform arbitrage tool spanning Kalshi, Polymarket, Limitless Exchange, and ForecastEx (the CME/IBKR-linked regulated event-contract venue), notable for including a traditional brokerage-connected venue alongside the crypto-native ones.

✅ *Good at:* Rare inclusion of ForecastEx/IBKR alongside the usual crypto-native prediction venues.  
⚠️ *Limitations:* Very low visibility/adoption (no stars) and ForecastEx integration requires an IBKR account and its API constraints.

</details>

### Forecasting agents

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**digital-oracle**](https://github.com/komako-workshop/digital-oracle) | 828 | Python | 🟢 | Broad multi-source (13 data feeds) macro probability synthesis, unusually high star count for a research-only skill. |
| [**Polyseer**](https://github.com/yorkeccak/Polyseer) | 666 | TypeScript | 🟢 | Fast surfacing of emergent Polymarket trading opportunities/signals for human or agent review. |
| [**polymarket-pipeline**](https://github.com/brodyautomates/polymarket-pipeline) | 366 | Python | 🟢 | Real-time news classification pipeline purpose-built to react to breaking events faster than manual traders on niche markets. |
| [**polyclaw**](https://github.com/chainstacklabs/polyclaw) | 358 | Python | 🟢 | Clean OpenClaw-native integration including hedge discovery, not just plain buy/sell execution. |
| [**oracle3**](https://github.com/YichengYang-Ethan/oracle3) | 255 | Python | 🟢 | Actuarial-grade (Wang Transform) risk-adjusted pricing model applied at scale (291K+ contracts) with unusually thorough test coverage. |
| [**Metaculus/forecasting-tools**](https://github.com/Metaculus/forecasting-tools) | 80 | Python | 🟢 | Official, actively maintained scaffolding that removes most of the Metaculus-API boilerplate from building a forecasting bot. |
| [**Metaculus/metac-bot-template**](https://github.com/Metaculus/metac-bot-template) | 66 | Python | 🟢 | Lowest-friction official starting point for a first Metaculus tournament bot. |
| [**simmer-sdk**](https://github.com/SpartanLabsXyz/simmer-sdk) | 49 | Python | 🟢 | Reusable agent-oriented harness (skills + MCP + SDK) reducing boilerplate for new forecasting/trading agents. |
| [**manifold-llm-bot**](https://github.com/ksadov/manifold-llm-bot) | 7 | Python | 🟢 | Configurable LLM-backed forecasting/trading loop specifically tuned for Manifold's play-money mechanics. |
| [**No-Stream/metaculus-bot**](https://github.com/No-Stream/metaculus-bot) | 0 | unknown | ⚪ | Independent worked example of LLM-driven forecasting logic separate from Metaculus's own template. |

<details><summary>Explainers (10)</summary>

**[digital-oracle](https://github.com/komako-workshop/digital-oracle)** · Python · ★ 828 · last push 2026-07-26  
An AI agent skill (for Claude Code, Cursor, Codex, OpenClaw) that answers macro questions -- housing, gold, BTC, geopolitics -- with probability estimates mined from 13 financial data sources including Polymarket, Kalshi, CFTC and SEC filings. Framed as a 'digital oracle' research tool rather than an execution bot, aggregating prediction-market-implied probabilities alongside traditional financial data.

✅ *Good at:* Broad multi-source (13 data feeds) macro probability synthesis, unusually high star count for a research-only skill.  
⚠️ *Limitations:* Research/answering tool only, no trade execution; quality depends on the underlying LLM's synthesis of noisy sources.

**[Polyseer](https://github.com/yorkeccak/Polyseer)** · TypeScript · ★ 666 · last push 2026-09-14  
A research/alpha-discovery tool for Polymarket that surfaces trading signals and market intelligence 'at the speed of now,' positioned as an analysis layer feeding trade ideas rather than a full execution bot. Fast-growing and actively updated in 2026.

✅ *Good at:* Fast surfacing of emergent Polymarket trading opportunities/signals for human or agent review.  
⚠️ *Limitations:* Signal-generation focus; users must add their own execution and risk layer.

**[polymarket-pipeline](https://github.com/brodyautomates/polymarket-pipeline)** · Python · ★ 366 · last push 2026-04-03  
An event-driven AI pipeline that monitors breaking news in real time, classifies its likely market impact using Claude, and automatically trades niche Polymarket markets in response. Represents the news-to-trade latency-arbitrage pattern applied to prediction markets rather than traditional securities.

✅ *Good at:* Real-time news classification pipeline purpose-built to react to breaking events faster than manual traders on niche markets.  
⚠️ *Limitations:* Effectiveness is highly dependent on Claude's news-impact classification accuracy and on Polymarket's niche-market liquidity being tradeable.

**[polyclaw](https://github.com/chainstacklabs/polyclaw)** · Python · ★ 358 · last push 2026-04-28  
A trading-enabled Polymarket skill for the OpenClaw agent framework letting an LLM agent browse markets, execute trades, track positions, and discover hedges through natural-language-driven tool calls. Representative of the OpenClaw-skill ecosystem pattern (also seen in ClawForge, PolymarketBTC15mAssistant) for wiring prediction markets into general-purpose agent runtimes.

✅ *Good at:* Clean OpenClaw-native integration including hedge discovery, not just plain buy/sell execution.  
⚠️ *Limitations:* Tied to the OpenClaw agent framework, so it is less portable to other agent runtimes without adaptation.

**[oracle3](https://github.com/YichengYang-Ethan/oracle3)** · Python · ★ 255 · last push 2026-05-08  
A prediction-market trading engine that applies a Wang Transform (a distortion-risk pricing technique borrowed from actuarial/insurance pricing theory) to price over 291,000 contracts, paper-traded across Kalshi, Polymarket, and Solana DFlow (using Jito bundles for MEV-aware execution). Backed by 633 tests, it is one of the more mathematically rigorous and best cross-venue-coverage projects in the survey, explicitly covering the Solana DFlow venue.

✅ *Good at:* Actuarial-grade (Wang Transform) risk-adjusted pricing model applied at scale (291K+ contracts) with unusually thorough test coverage.  
⚠️ *Limitations:* Paper-traded only as documented; no evidence yet of live-capital track record.

**[Metaculus/forecasting-tools](https://github.com/Metaculus/forecasting-tools)** · Python · ★ 80 · last push 2026-09-16  
Metaculus's own framework for building an AI forecasting bot to compete in its AI Benchmarking tournaments, handling Metaculus API interaction, prediction aggregation, and a benchmarking interface for comparing bot performance. It also doubles as a toolkit to help human forecasters, and is the base most tournament bots (including several in this catalog) are built on.

✅ *Good at:* Official, actively maintained scaffolding that removes most of the Metaculus-API boilerplate from building a forecasting bot.  
⚠️ *Limitations:* Tuned to Metaculus's tournament format and question types; adapting it to Kalshi/Polymarket-style binary markets requires extra glue code.

**[Metaculus/metac-bot-template](https://github.com/Metaculus/metac-bot-template)** · Python · ★ 66 · last push 2026-09-09  
Metaculus's minimal official bot template for forecasting a tournament, wired to run on a schedule (roughly every 20 minutes) to pick up new tournament questions and submit predictions. Simpler and more beginner-friendly than forecasting-tools, aimed at people entering their first AI Benchmarking tournament.

✅ *Good at:* Lowest-friction official starting point for a first Metaculus tournament bot.  
⚠️ *Limitations:* Intentionally minimal; lacks the aggregation/benchmarking features of the full forecasting-tools framework.

**[simmer-sdk](https://github.com/SpartanLabsXyz/simmer-sdk)** · Python · ★ 49 · last push 2026-09-21  
A prediction-market harness purpose-built for AI agents, bundling reusable skills, an MCP server, and a Python SDK so agent developers don't need to reimplement market discovery, order placement, or portfolio tracking for each new bot. Positions itself as infrastructure for agent builders rather than a bot itself.

✅ *Good at:* Reusable agent-oriented harness (skills + MCP + SDK) reducing boilerplate for new forecasting/trading agents.  
⚠️ *Limitations:* Infrastructure layer, not a ready-made forecasting strategy; requires building agent logic on top.

**[manifold-llm-bot](https://github.com/ksadov/manifold-llm-bot)** · Python · ★ 7 · last push 2025-05-23  
A configurable trading bot for Manifold Markets that lets users plug in an LLM to generate probability estimates and trade accordingly, similar in spirit to the earlier gpt-manifold project but built to be more configurable across models/prompts.

✅ *Good at:* Configurable LLM-backed forecasting/trading loop specifically tuned for Manifold's play-money mechanics.  
⚠️ *Limitations:* Small, single-maintainer project; play-money Manifold results don't directly validate real-money performance.

**[No-Stream/metaculus-bot](https://github.com/No-Stream/metaculus-bot)** · unknown · ★ 0 · last push unknown  
A community bot 'using LLMs to forecast events on Metaculus,' representative of the many independent tournament entrants who wrap an LLM (often with web-search/retrieval augmentation) around the official Metaculus API to generate calibrated probability forecasts for tournament questions.

✅ *Good at:* Independent worked example of LLM-driven forecasting logic separate from Metaculus's own template.  
⚠️ *Limitations:* Metadata (stars, activity) could not be confirmed in this pass; treat as a lead to verify before relying on it.

</details>

### Data & datasets

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**Jon-Becker/prediction-market-analysis**](https://github.com/Jon-Becker/prediction-market-analysis) | 3.9k | Python | 🟢 | Largest known public Kalshi + Polymarket market/trade dataset, paired with an active collection framework. |
| [**poly_data**](https://github.com/warproxxx/poly_data) | 2.3k | Python | 🟢 | High-star, actively maintained data pipeline for structured Polymarket market/trade data. |
| [**prediction-market-backtesting**](https://github.com/evan-kolberg/prediction-market-backtesting) | 1.2k | Python | 🟢 | Brings prediction-market backtesting into a mature, professionally-built trading engine (NautilusTrader) rather than reinventing backtest infrastructure. |
| [**Polymarket_data (SII-WANGZJ)**](https://github.com/SII-WANGZJ/Polymarket_data) | 831 | Python | 🟢 | Extremely large (1.1B record) trade-level dataset with multiple pre-processed views, useful for behavioral/microstructure research. |
| [**polyledger**](https://github.com/nahrek/polyledger) | 623 | Python | 🟢 | Simple, portable SQL-queryable Polymarket dataset (single DuckDB file) built via a resumable indexer. |
| [**prediction-market-mcp**](https://github.com/JamesANZ/prediction-market-mcp) | 36 | TypeScript | 🟢 | Simple unified read-only data access across three major venues (Polymarket, PredictIt, Kalshi) for MCP clients. |
| [**Prediction-Markets-Data (arbbets)**](https://github.com/arbbets/Prediction-Markets-Data) | 7 | unknown | 🟢 | Rare single tool spanning four venues including the less-covered PredictIt and Limitless Exchange. |

<details><summary>Explainers (7)</summary>

**[Jon-Becker/prediction-market-analysis](https://github.com/Jon-Becker/prediction-market-analysis)** · Python · ★ 3.9k · last push 2026-09-20  
A framework for collecting and analyzing prediction-market data that includes what is described as the largest publicly available dataset of Polymarket and Kalshi market and trade data. The single highest-starred repository found across this entire prediction-markets survey, and actively updated as of September 2026, making it the standout resource for anyone needing historical Kalshi/Polymarket data for backtesting or research.

✅ *Good at:* Largest known public Kalshi + Polymarket market/trade dataset, paired with an active collection framework.  
⚠️ *Limitations:* Dataset scale means non-trivial storage/compute needed to work with it fully; verify licensing terms before commercial reuse.

**[poly_data](https://github.com/warproxxx/poly_data)** · Python · ★ 2.3k · last push 2026-09-08  
A Polymarket data retriever that fetches, processes, and structures markets, order events, and trades into analysis-ready form. Companion project to poly-maker, widely used as the data-ingestion backbone for other Polymarket bots and research.

✅ *Good at:* High-star, actively maintained data pipeline for structured Polymarket market/trade data.  
⚠️ *Limitations:* Focused purely on data retrieval, not execution or strategy logic.

**[prediction-market-backtesting](https://github.com/evan-kolberg/prediction-market-backtesting)** · Python · ★ 1.2k · last push 2026-05-16  
An extension for NautilusTrader (a production-grade Rust-based algorithmic trading engine) adding prediction-market backtesting capability, letting users evaluate strategies against real historical Polymarket and Kalshi data inside an established, professional-grade backtesting engine rather than a bespoke one-off harness.

✅ *Good at:* Brings prediction-market backtesting into a mature, professionally-built trading engine (NautilusTrader) rather than reinventing backtest infrastructure.  
⚠️ *Limitations:* Requires learning NautilusTrader's broader framework and conventions, a bigger lift than a standalone lightweight backtester.

**[Polymarket_data (SII-WANGZJ)](https://github.com/SII-WANGZJ/Polymarket_data)** · Python · ★ 831 · last push 2026-01-01  
A dataset of 1.1 billion Polymarket trading records processed into multiple analysis-ready formats, including cleaned data, unified token perspectives, and user-level transformations, intended for market research, behavioral studies, and quantitative analysis at scale.

✅ *Good at:* Extremely large (1.1B record) trade-level dataset with multiple pre-processed views, useful for behavioral/microstructure research.  
⚠️ *Limitations:* Static snapshot (as of dataset publication) rather than a live-updating feed; scale requires substantial storage/compute.

**[polyledger](https://github.com/nahrek/polyledger)** · Python · ★ 623 · last push 2026-09-19  
A resumable Polymarket indexer that combines CLOB market metadata with on-chain Polygon trade data into a single queryable DuckDB file, letting researchers run SQL directly over Polymarket history without standing up a full indexing stack. Actively updated as of September 2026.

✅ *Good at:* Simple, portable SQL-queryable Polymarket dataset (single DuckDB file) built via a resumable indexer.  
⚠️ *Limitations:* DuckDB single-file approach may not scale to very high-frequency or very long historical ranges as gracefully as a hosted subgraph.

**[prediction-market-mcp](https://github.com/JamesANZ/prediction-market-mcp)** · TypeScript · ★ 36 · last push 2026-01-16  
A simple MCP server that grabs prediction-market data from Polymarket, PredictIt, and Kalshi in one place, giving an LLM client a single tool surface for cross-venue market discovery and price lookup rather than three separate integrations.

✅ *Good at:* Simple unified read-only data access across three major venues (Polymarket, PredictIt, Kalshi) for MCP clients.  
⚠️ *Limitations:* Read/data-only, no trading; PredictIt coverage is of limited value given that platform's restricted contract catalog.

**[Prediction-Markets-Data (arbbets)](https://github.com/arbbets/Prediction-Markets-Data)** · unknown · ★ 7 · last push 2025-07-07  
A Python script for collecting, analyzing, and visualizing prediction-market data across four venues at once: Kalshi, Polymarket, PredictIt, and Limitless, from the same author as the related Prediction-Market-Arbitrage repo. Smaller scale than the Jon-Becker or SII-WANGZJ datasets but notable for its four-venue breadth including the less-covered PredictIt and Limitless.

✅ *Good at:* Rare single tool spanning four venues including the less-covered PredictIt and Limitless Exchange.  
⚠️ *Limitations:* Low visibility/adoption (single-digit stars); scope and data depth are modest relative to the larger dataset projects.

</details>

### Sports odds

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**NBA-Machine-Learning-Sports-Betting**](https://github.com/kyleskom/NBA-Machine-Learning-Sports-Betting) | 1.7k | Python | 🟢 | Popular, actively maintained NBA outcome-prediction pipeline with a large existing user community for reference/comparison. |
| [**sports-betting (georgedouzas)**](https://github.com/georgedouzas/sports-betting) | 799 | Python | 🟢 | Mature, well-documented odds/value-betting modeling library with real historical datasets and scikit-learn integration. |
| [**polymarket-tennis**](https://github.com/livetennisapi/polymarket-tennis) | 315 | Python | 🟢 | Clean live-score-to-market matching pipeline specifically for tennis, a niche well-covered event-market category. |
| [**flumine**](https://github.com/betcode-org/flumine) | 245 | Python | 🟢 | Battle-tested strategy/backtest/live architecture for exchange-style betting markets, directly analogous to prediction-market CLOBs. |

<details><summary>Explainers (4)</summary>

**[NBA-Machine-Learning-Sports-Betting](https://github.com/kyleskom/NBA-Machine-Learning-Sports-Betting)** · Python · ★ 1.7k · last push 2026-09-12  
A long-running, high-star machine-learning project predicting NBA game outcomes and generating betting recommendations from historical stats and odds data, one of the most popular sports-betting ML repos on GitHub overall. Directly relevant as a modeling reference for pricing NBA-linked Kalshi/Polymarket event contracts.

✅ *Good at:* Popular, actively maintained NBA outcome-prediction pipeline with a large existing user community for reference/comparison.  
⚠️ *Limitations:* Single-sport (NBA) scope; not a general cross-sport modeling framework.

**[sports-betting (georgedouzas)](https://github.com/georgedouzas/sports-betting)** · Python · ★ 799 · last push 2026-07-28  
A well-established collection of sports-betting AI tools in Python providing data loaders for historical odds/results across major sports leagues, backtesting utilities, and value-betting model scaffolding (scikit-learn-compatible). One of the most mature, longest-running open-source odds-modeling libraries, directly transferable to pricing sports-linked event contracts on Kalshi/Polymarket.

✅ *Good at:* Mature, well-documented odds/value-betting modeling library with real historical datasets and scikit-learn integration.  
⚠️ *Limitations:* Built for traditional sportsbook odds, not natively aware of prediction-market-specific mechanics like negRisk or CLOB fees.

**[polymarket-tennis](https://github.com/livetennisapi/polymarket-tennis)** · Python · ★ 315 · last push 2026-09-12  
An observe-only Python toolkit that discovers tennis markets via Polymarket's Gamma API, matches them to live tennis matches, and tracks market price against live score, server, and break-point state. Explicitly framed as the data layer underneath a future Polymarket/Kalshi tennis trading bot rather than an execution system itself.

✅ *Good at:* Clean live-score-to-market matching pipeline specifically for tennis, a niche well-covered event-market category.  
⚠️ *Limitations:* Observe-only by design; no order execution included, and depends on the Gamma API's tennis market coverage.

**[flumine](https://github.com/betcode-org/flumine)** · Python · ★ 245 · last push 2026-09-07  
A betting/trading framework originally built around the Betfair Exchange, providing a strategy/backtest/live-trading architecture (streaming market data, order execution, simulated markets) analogous to what quant frameworks like Backtrader offer for stocks. Actively maintained and highly relevant as an architectural reference for building an event-market trading engine, since Betfair's exchange model closely resembles Kalshi/Polymarket's order-book structure.

✅ *Good at:* Battle-tested strategy/backtest/live architecture for exchange-style betting markets, directly analogous to prediction-market CLOBs.  
⚠️ *Limitations:* Native integration is Betfair-specific; using it for Kalshi/Polymarket requires writing a custom market-data/execution adapter.

</details>

### Other venues (Manifold, PredictIt, Limitless, DFlow…)

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**Awesome-Prediction-Market-Tools**](https://github.com/aarora4/Awesome-Prediction-Market-Tools) | 750 | unknown | 🟢 | Broad community-curated index that surfaces long-tail tools across the whole prediction-market tooling landscape. |
| [**Manifold Markets (platform)**](https://github.com/manifoldmarkets/manifold) | 517 | TypeScript | 🟢 | Complete, actively maintained, self-hostable open-source prediction-market platform (not just a client/bot). |
| [**fintool (second-state)**](https://github.com/second-state/fintool) | 315 | Rust | 🟢 | Consistent CLI/agent-tool design pattern spanning prediction markets alongside crypto and equities in one suite. |
| [**predict-fun-marketmaker**](https://github.com/ccjingeth/predict-fun-marketmaker) | 217 | TypeScript | 🟢 | Purpose-built to farm a specific venue's maker-rebate incentive program alongside ordinary spread capture. |
| [**manifoldpy**](https://github.com/vluzko/manifoldpy) | 41 | Python | 🟢 | Actively maintained, general-purpose Python access to Manifold's API. |
| [**dflow_phantom-connect-skill**](https://github.com/DFlowProtocol/dflow_phantom-connect-skill) | 40 | Shell | 🟢 | Official, org-published wallet-connect integration for building Solana DFlow-aware agent tooling. |
| [**sdk-python (Predict.fun)**](https://github.com/PredictDotFun/sdk-python) | 24 | Python | 🟢 | Officially-published, MIT-licensed SDK directly from the Predict.fun protocol team. |
| [**manifolio**](https://github.com/Will-Howard/manifolio) | 22 | TypeScript | 🟢 | Focused, well-scoped Kelly-style position-sizing calculator tailored to Manifold's specific market mechanics. |
| [**predictit-arbitrage**](https://github.com/dcadata/predictit-arbitrage) | 22 | Python | 🟠 | Historical reference for how PredictIt-specific arbitrage detection was implemented. |
| [**PyManifold**](https://github.com/bcongdon/PyManifold) | 18 | Python | 🟠 | Simple, early reference client for Manifold's API. |
| [**predictit_hedge**](https://github.com/mickbransfield/predictit_hedge) | 14 | Python | 🟢 | Specific, well-targeted logic for correlated-market hedge detection within PredictIt's contract set. |
| [**PredictIt-Python**](https://github.com/JessePresnell/PredictIt-Python) | 10 | Python | 🟠 | Simple historical reference for scraping PredictIt into a relational database. |
| [**limitless-exchange-ts-sdk**](https://github.com/limitless-labs-group/limitless-exchange-ts-sdk) | 7 | TypeScript | 🟢 | Type-safe, officially-org-published access to Limitless's CLOB and NegRisk market types. |
| [**limitless-cli**](https://github.com/limitless-labs-group/limitless-cli) | 6 | Rust | 🟢 | Direct terminal-based order placement and portfolio management for Limitless without writing custom integration code. |
| [**Drift-BET**](https://github.com/HarrierOnChain/Drift-BET) | 0 | Rust | 🟢 | Rare dedicated coverage of Drift Protocol's Solana-native BET prediction markets, an otherwise sparsely-tooled venue. |

<details><summary>Explainers (15)</summary>

**[Awesome-Prediction-Market-Tools](https://github.com/aarora4/Awesome-Prediction-Market-Tools)** · unknown · ★ 750 · last push 2026-09-03  
A curated awesome-list of prediction-market tools spanning AI agents, analytics, APIs, dashboards, copy trading, alerting, and tracking. High star count and recent activity make it a useful meta-index to cross-check against this catalog and discover niche tools not otherwise surfaced by direct GitHub search. Similar competing lists exist (e.g. Marcussy34/awesome-prediction-markets).

✅ *Good at:* Broad community-curated index that surfaces long-tail tools across the whole prediction-market tooling landscape.  
⚠️ *Limitations:* Curation quality/currency depends on community contributions; entries are not independently vetted.

**[Manifold Markets (platform)](https://github.com/manifoldmarkets/manifold)** · TypeScript · ★ 517 · last push 2026-09-20  
The full open-source codebase for Manifold Markets, a play-money prediction-market platform where anyone can create a market on any question ('a market for every question'). MIT-licensed and actively developed, it is the reference implementation for a self-hostable, community-driven prediction-market platform, distinct from the real-money venues elsewhere in this catalog.

✅ *Good at:* Complete, actively maintained, self-hostable open-source prediction-market platform (not just a client/bot).  
⚠️ *Limitations:* Play-money mechanics differ economically from real-money venues (Kalshi/Polymarket), limiting direct strategy transfer.

**[fintool (second-state)](https://github.com/second-state/fintool)** · Rust · ★ 315 · last push 2026-05-19  
A suite of Rust CLI tools for agentic trading and market intelligence, with a dedicated Polymarket binary alongside per-exchange binaries for Hyperliquid, Binance, Coinbase, and OKX, plus a shared exchange-agnostic fintool for quotes, news, and SEC filings across crypto, stocks, commodities, and prediction markets. Useful as an example of treating a prediction-market venue as one asset class among several inside a unified agent-tooling suite.

✅ *Good at:* Consistent CLI/agent-tool design pattern spanning prediction markets alongside crypto and equities in one suite.  
⚠️ *Limitations:* Polymarket is only one binary among several; depth of prediction-market-specific features may be shallower than a dedicated tool.

**[predict-fun-marketmaker](https://github.com/ccjingeth/predict-fun-marketmaker)** · TypeScript · ★ 217 · last push 2026-05-05  
A Predict.fun market-making and arbitrage bot with a desktop console, designed to place resting orders that earn Predict.fun's maker-rebate points program in addition to spread capture, reflecting how points/incentive programs shape early-stage prediction-market bot design.

✅ *Good at:* Purpose-built to farm a specific venue's maker-rebate incentive program alongside ordinary spread capture.  
⚠️ *Limitations:* Strategy value is partly tied to a points/incentive program that may change or expire, not just organic spread economics.

**[manifoldpy](https://github.com/vluzko/manifoldpy)** · Python · ★ 41 · last push 2026-07-10  
Python tools for working with the Manifold Markets API, one of the more actively maintained community clients for the platform, used as a base for several Manifold bots and analysis scripts.

✅ *Good at:* Actively maintained, general-purpose Python access to Manifold's API.  
⚠️ *Limitations:* Manifold-only; no cross-venue support.

**[dflow_phantom-connect-skill](https://github.com/DFlowProtocol/dflow_phantom-connect-skill)** · Shell · ★ 40 · last push 2026-07-23  
An official skill from the DFlow Protocol org (a Solana DEX aggregator/order-flow protocol with prediction-market-adjacent trading infrastructure) for connecting a Phantom wallet into agent workflows. Included as the clearest officially-published DFlow Protocol artifact found on GitHub relevant to Solana-based prediction/trading agents.

✅ *Good at:* Official, org-published wallet-connect integration for building Solana DFlow-aware agent tooling.  
⚠️ *Limitations:* Narrow scope (wallet connection only); does not itself provide market data or order execution against DFlow.

**[sdk-python (Predict.fun)](https://github.com/PredictDotFun/sdk-python)** · Python · ★ 24 · last push 2026-07-28  
The official Python SDK published by the PredictDotFun org to help developers interface with the Predict.fun protocol, a newer crypto-native prediction-market venue that several cross-venue projects (dr-manhattan, HarrierOnChain's toolkit) list as on their roadmap.

✅ *Good at:* Officially-published, MIT-licensed SDK directly from the Predict.fun protocol team.  
⚠️ *Limitations:* Predict.fun is a newer, smaller-volume venue than Kalshi/Polymarket, so ecosystem tooling and liquidity are both thinner.

**[manifolio](https://github.com/Will-Howard/manifolio)** · TypeScript · ★ 22 · last push 2026-07-20  
A bet-sizing tool for Manifold Markets that helps traders compute appropriately-sized positions (Kelly-style) given their bankroll and edge estimate, addressing a common gap in simple market-browsing tools.

✅ *Good at:* Focused, well-scoped Kelly-style position-sizing calculator tailored to Manifold's specific market mechanics.  
⚠️ *Limitations:* Sizing tool only, not a data source or execution bot.

**[predictit-arbitrage](https://github.com/dcadata/predictit-arbitrage)** · Python · ★ 22 · last push 2024-03-24  
A scanner for arbitrage opportunities on PredictIt, explicitly marked by its author as 'no longer active,' reflecting PredictIt's shrinking relevance since regulatory restrictions curtailed its contract count and trading activity in recent years.

✅ *Good at:* Historical reference for how PredictIt-specific arbitrage detection was implemented.  
⚠️ *Limitations:* Explicitly deprecated/inactive; PredictIt itself has faced regulatory-driven contraction, reducing the tool's practical value.

**[PyManifold](https://github.com/bcongdon/PyManifold)** · Python · ★ 18 · last push 2022-12-18  
An earlier Python API client for Manifold Markets, one of the first community wrappers around Manifold's REST API for programmatic market/bet access.

✅ *Good at:* Simple, early reference client for Manifold's API.  
⚠️ *Limitations:* No commits since late 2022; likely superseded by manifoldpy for active development.

**[predictit_hedge](https://github.com/mickbransfield/predictit_hedge)** · Python · ★ 14 · last push 2026-05-20  
A tool identifying hedge opportunities on PredictIt arising from inefficient pricing across correlated markets (e.g. related political outcome contracts), from the same author as the related predictit_538_odds comparison project. Notably still receiving updates in 2026 despite PredictIt's diminished market relevance.

✅ *Good at:* Specific, well-targeted logic for correlated-market hedge detection within PredictIt's contract set.  
⚠️ *Limitations:* PredictIt's contract catalog and liquidity have shrunk significantly under CFTC restrictions, limiting practical opportunity.

**[PredictIt-Python](https://github.com/JessePresnell/PredictIt-Python)** · Python · ★ 10 · last push 2017-05-29  
An old Python scraper that pulls PredictIt market data into a MySQL database, one of the earliest community tools for programmatic PredictIt data access. Included here as a historical/legacy reference given how few actively maintained PredictIt tools remain.

✅ *Good at:* Simple historical reference for scraping PredictIt into a relational database.  
⚠️ *Limitations:* Unmaintained since 2017; PredictIt's site/API has almost certainly changed since.

**[limitless-exchange-ts-sdk](https://github.com/limitless-labs-group/limitless-exchange-ts-sdk)** · TypeScript · ★ 7 · last push 2026-08-11  
A TypeScript SDK for Limitless Exchange (a Base-network on-chain prediction-market venue) providing type-safe access to its CLOB and NegRisk multi-outcome market types, published by the limitless-labs-group org alongside sibling Go and Rust SDKs and a Rust CLI.

✅ *Good at:* Type-safe, officially-org-published access to Limitless's CLOB and NegRisk market types.  
⚠️ *Limitations:* Limitless Exchange itself has much smaller liquidity/volume than Kalshi or Polymarket, limiting practical trading depth.

**[limitless-cli](https://github.com/limitless-labs-group/limitless-cli)** · Rust · ★ 6 · last push 2026-04-24  
A Rust CLI for Limitless Exchange enabling browsing markets, placing GTC/FOK orders, monitoring live order books, and managing a prediction-market portfolio on Base directly from the terminal, from the same org as the TS/Go/Rust SDKs.

✅ *Good at:* Direct terminal-based order placement and portfolio management for Limitless without writing custom integration code.  
⚠️ *Limitations:* Niche venue with limited liquidity; CLI-only interface is less suited to full automation than the SDKs.

**[Drift-BET](https://github.com/HarrierOnChain/Drift-BET)** · Rust · ★ 0 · last push 2026-06-24  
A trading bot for Drift Protocol's BET prediction-market product on Solana, implementing BTC arbitrage, orderbook-imbalance trading, market making, and whale-signal following. One of the very few open-source projects found targeting Drift's BET specifically, from the same org (HarrierOnChain) as the broader multi-venue toolkit.

✅ *Good at:* Rare dedicated coverage of Drift Protocol's Solana-native BET prediction markets, an otherwise sparsely-tooled venue.  
⚠️ *Limitations:* Zero community adoption signal (no stars) and Drift BET itself is a newer, lower-liquidity product than Kalshi/Polymarket.

</details>

[⬆ back to top](#contents)

## Options, greeks & volatility

Pricing libraries, implied-volatility and surface fitting, options backtesters, greeks and gamma-exposure tools.
**QuantLib** remains the standard. **FinancePy**, **tf-quant-finance** and **RustQuant** are strong alternatives,
and **py_vollib** is the lightweight Black–Scholes / greeks / IV stack.

**Key takeaways**

- **optopsy** is the most mature open options backtester.
- Gamma-exposure (GEX) dashboards are the most active niche (**gammagrid**, **gex-terminal**).
- Gap: no dominant, polished SVI/SABR surface-fitting library exists yet. The space is mostly single-author notebooks.
- Crypto-options tooling is almost entirely Deribit-specific and mostly dated.

### Pricing libraries

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**QuantLib**](https://github.com/lballabio/QuantLib) | 7.6k | C++ | 🟢 | Comprehensive, battle-tested pricing engines and term-structure/calendar infrastructure for vanilla and exotic derivatives across asset classes. |
| [**tf-quant-finance**](https://github.com/google/tf-quant-finance) | 5.5k | Python | 🟢 | Vectorized, GPU-accelerated pricing and calibration (Heston, SABR, local vol) with automatic differentiation for Greeks. |
| [**FinancePy**](https://github.com/domokane/FinancePy) | 3.2k | Python | 🟢 | Readable, Numba-accelerated pricing and risk for a wide range of vanilla and exotic option types with minimal dependencies. |
| [**RustQuant**](https://github.com/avhz/RustQuant) | 1.8k | Rust | 🟢 | Memory-safe, high-performance option pricing and stochastic-process simulation for Rust-based trading infrastructure. |
| [**PyQL**](https://github.com/enthought/pyql) | 1.3k | Cython | 🟢 | Fast, Pythonic access to QuantLib's option pricing engines with less boilerplate than SWIG bindings. |
| [**py_vollib**](https://github.com/vollib/py_vollib) | 434 | Python | 🟢 | Fast, numerically robust Black-Scholes pricing, Greeks and implied-volatility solving for European options. |
| [**QLNet**](https://github.com/amaggiulli/QLNet) | 428 | C# | 🟢 | Dependency-free, pure-.NET derivatives pricing for teams standardized on the Microsoft stack. |
| [**QuantLib-SWIG**](https://github.com/lballabio/QuantLib-SWIG) | 402 | SWIG | 🟢 | Keeping non-C++ QuantLib bindings in sync with the latest C++ pricing engines. |
| [**MibianLib**](https://github.com/yassinemaaroufi/MibianLib) | 289 | Python | 🟠 | Extremely simple, dependency-light Black-Scholes/Merton pricing and Greeks for quick scripts and tutorials. |
| [**StochVolModels**](https://github.com/ArturSepp/StochVolModels) | 237 | Python | 🟢 | Fast, validated Fourier-based pricing and calibration of Heston-family stochastic-volatility models. |
| [**PROJ_Option_Pricing_Matlab**](https://github.com/jkirkby3/PROJ_Option_Pricing_Matlab) | 211 | MATLAB | 🟠 | Reference-quality exotic-option pricing formulas and PROJ-method implementations for many payoff types. |
| [**torchquant**](https://github.com/jialuechen/torchquant) | 194 | Python | 🟢 | PyTorch-native, autodiff-based option pricing/Greeks for teams already standardized on PyTorch for ML. |
| [**py_vollib_vectorized**](https://github.com/marcdemers/py_vollib_vectorized) | 162 | Python | 🟠 | Orders-of-magnitude faster IV/Greeks computation over full option chains versus scalar py_vollib. |
| [**fypy**](https://github.com/jkirkby3/fypy) | 147 | Python | 🟠 | Academically-grounded exotic-option pricing (barrier, Asian, cliquet) under advanced jump/Levy models. |
| [**QuantLib.jl**](https://github.com/pazzo83/QuantLib.jl) | 143 | Julia | 🟠 | Demonstrating idiomatic-Julia derivatives pricing without an FFI dependency. |
| [**RQuantLib**](https://github.com/eddelbuettel/rquantlib) | 136 | C++ | 🟢 | Bringing QuantLib pricing functions into R workflows and Rcpp-based quant pipelines. |
| [**py_lets_be_rational**](https://github.com/vollib/py_lets_be_rational) | 73 | Python | 🟢 | Rational, non-iterative implied-volatility inversion that is both fast and accurate across the full moneyness range. |
| [**libitofin**](https://github.com/benbenbang/libitofin) | 57 | Rust | 🟢 | Fast, low-level numerical building blocks for pricing and risk in Rust trading systems. |
| [**black_scholes_rust**](https://github.com/danielhstahl/black_scholes_rust) | 25 | Rust | 🟢 | Minimal, fast Black-Scholes pricing/Greeks as a Rust crate dependency. |
| [**pyvolr**](https://github.com/yipjunkai/pyvolr) | 4 | Python | 🟢 | Modern, faster reimplementation of py_vollib's API for teams wanting an actively maintained alternative. |

<details><summary>Explainers (20)</summary>

**[QuantLib](https://github.com/lballabio/QuantLib)** · C++ · ★ 7.6k · last push 2026-09-18  
QuantLib is the de facto open-source standard for quantitative finance: a C++ framework covering option pricing (analytic, PDE, binomial, Monte Carlo), yield curves, day-count conventions, calendars, and fixed-income/credit/FX derivatives. It has 25+ years of development, an active core team (led by Luigi Ballabio), and bindings generated via QuantLib-SWIG for Python, Java, C#, R and more. Almost every other library on this list either wraps QuantLib or was built as a lighter alternative to it.

✅ *Good at:* Comprehensive, battle-tested pricing engines and term-structure/calendar infrastructure for vanilla and exotic derivatives across asset classes.  
⚠️ *Limitations:* Steep learning curve, verbose C++-style API even from Python, and slow to adopt newer pure-Python/Numba ergonomics.

**[tf-quant-finance](https://github.com/google/tf-quant-finance)** · Python · ★ 5.5k · last push 2026-08-06  
Google's TensorFlow-based quantitative finance library provides GPU/TPU-accelerated option pricing (Black-Scholes, local vol, Heston, SABR), Monte Carlo and PDE solvers, and volatility-surface tools, all differentiable via autograd. It is aimed at large-scale, hardware-accelerated derivatives risk and calibration workloads rather than small scripts.

✅ *Good at:* Vectorized, GPU-accelerated pricing and calibration (Heston, SABR, local vol) with automatic differentiation for Greeks.  
⚠️ *Limitations:* Heavy TensorFlow dependency and API complexity relative to lightweight libraries like py_vollib.

**[FinancePy](https://github.com/domokane/FinancePy)** · Python · ★ 3.2k · last push 2026-09-19  
FinancePy, maintained by Dominic O'Kane, is a pure-Python derivatives library covering equity, FX, rates and credit products with a strong focus on options: European/American/Asian/barrier/digital pricing, full Greeks, and volatility-surface construction. It uses Numba JIT compilation to reach near-C++ speed while staying readable Python, and is one of the most actively developed alternatives to QuantLib.

✅ *Good at:* Readable, Numba-accelerated pricing and risk for a wide range of vanilla and exotic option types with minimal dependencies.  
⚠️ *Limitations:* Smaller ecosystem/community than QuantLib and less exhaustive exotic-instrument coverage.

**[RustQuant](https://github.com/avhz/RustQuant)** · Rust · ★ 1.8k · last push 2026-09-12  
RustQuant is a rapidly growing Rust quantitative-finance library covering option pricing (Black-Scholes and beyond), stochastic processes, autodiff, and portfolio/risk tooling, aiming to bring QuantLib-like breadth with Rust's speed and safety guarantees. It has become one of the most starred Rust finance projects and is actively developed.

✅ *Good at:* Memory-safe, high-performance option pricing and stochastic-process simulation for Rust-based trading infrastructure.  
⚠️ *Limitations:* Younger project than QuantLib/FinancePy, so exotic-instrument and calibration coverage is still expanding.

**[PyQL](https://github.com/enthought/pyql)** · Cython · ★ 1.3k · last push 2026-07-17  
PyQL is Enthought's Cython-based Python wrapper around QuantLib, offering a more Pythonic, NumPy-friendly surface than the official SWIG bindings for option pricing, term structures, and instrument valuation. It predates QuantLib-Python's own pip packaging and is still used where tighter Cython performance or a different API shape is preferred.

✅ *Good at:* Fast, Pythonic access to QuantLib's option pricing engines with less boilerplate than SWIG bindings.  
⚠️ *Limitations:* Coverage lags behind full QuantLib C++ API; building from source can be fragile across QuantLib versions.

**[py_vollib](https://github.com/vollib/py_vollib)** · Python · ★ 434 · last push 2026-05-29  
py_vollib is the standard lightweight Python library for Black-Scholes-Merton option pricing, Greeks, and implied volatility, built on top of Peter Jaeckel's 'Let's Be Rational' algorithm (via py_lets_be_rational) for fast, robust IV inversion. It is widely embedded in options research notebooks, screeners and backtesters as the go-to reference pricer.

✅ *Good at:* Fast, numerically robust Black-Scholes pricing, Greeks and implied-volatility solving for European options.  
⚠️ *Limitations:* Scalar (row-by-row) API is slow on large option chains without the vectorized fork; European-style only.

**[QLNet](https://github.com/amaggiulli/QLNet)** · C# · ★ 428 · last push 2026-09-11  
QLNet is a native C# port (not a wrapper) of QuantLib, giving .NET developers option pricing, Greeks, curve building and instrument valuation without a native C++ dependency. It tracks the QuantLib feature set fairly closely and remains actively maintained by the community.

✅ *Good at:* Dependency-free, pure-.NET derivatives pricing for teams standardized on the Microsoft stack.  
⚠️ *Limitations:* Smaller contributor base than QuantLib itself, so newer QuantLib features arrive with a lag.

**[QuantLib-SWIG](https://github.com/lballabio/QuantLib-SWIG)** · SWIG · ★ 402 · last push 2026-09-17  
The official SWIG interface definitions that generate QuantLib-Python (and Java, C#, R, Guile, Ruby) bindings from the C++ core. It is what pip-installed QuantLib-Python is actually built from, and is released in lockstep with QuantLib itself.

✅ *Good at:* Keeping non-C++ QuantLib bindings in sync with the latest C++ pricing engines.  
⚠️ *Limitations:* It is a code-generation/build project, not a friendly high-level API by itself.

**[MibianLib](https://github.com/yassinemaaroufi/MibianLib)** · Python · ★ 289 · last push 2021-06-14  
Mibian is a simple, well-known Python options-pricing library implementing Black-Scholes, Black-76, Garman-Kohlhagen and Merton models with Greeks and implied volatility, historically popular as a teaching and quick-prototyping tool. This fork/mirror keeps the original PyPI 'mibian' package's source available.

✅ *Good at:* Extremely simple, dependency-light Black-Scholes/Merton pricing and Greeks for quick scripts and tutorials.  
⚠️ *Limitations:* Effectively abandoned since ~2021; slower and less numerically robust than py_vollib or FinancePy.

**[StochVolModels](https://github.com/ArturSepp/StochVolModels)** · Python · ★ 237 · last push 2026-09-20  
StochVolModels implements Fourier-transform (COS/characteristic-function) pricing, Monte Carlo validation and calibration for stochastic-volatility models including Heston and log-normal SV, giving researchers a practical way to price and calibrate European options under non-flat-vol dynamics. It is actively maintained with commits as recent as this week.

✅ *Good at:* Fast, validated Fourier-based pricing and calibration of Heston-family stochastic-volatility models.  
⚠️ *Limitations:* Focused on European options and specific SV models rather than a general-purpose derivatives library.

**[PROJ_Option_Pricing_Matlab](https://github.com/jkirkby3/PROJ_Option_Pricing_Matlab)** · MATLAB · ★ 211 · last push 2024-11-19  
A MATLAB implementation of the PROJ (Frame Projection) method for pricing a very wide range of exotic options - barrier, Asian, American, Parisian, lookback, cliquet, variance swap, swing, forward-starting - under advanced stochastic/jump models, from the same author as fypy.

✅ *Good at:* Reference-quality exotic-option pricing formulas and PROJ-method implementations for many payoff types.  
⚠️ *Limitations:* MATLAB-only (license cost) and not updated recently; better suited to research replication than live systems.

**[torchquant](https://github.com/jialuechen/torchquant)** · Python · ★ 194 · last push 2025-12-16  
torchquant reimplements derivatives pricing and hedging on PyTorch, letting users exploit autograd for Greeks and gradient-based calibration and run pricing engines on GPUs, positioning itself as a PyTorch analog to Google's TensorFlow-based tf-quant-finance.

✅ *Good at:* PyTorch-native, autodiff-based option pricing/Greeks for teams already standardized on PyTorch for ML.  
⚠️ *Limitations:* Much smaller community and narrower model coverage than tf-quant-finance or QuantLib.

**[py_vollib_vectorized](https://github.com/marcdemers/py_vollib_vectorized)** · Python · ★ 162 · last push 2024-12-02  
A drop-in vectorized layer over py_vollib that accepts NumPy arrays and pandas Series/DataFrames, letting pricing, Greeks and implied-volatility calculations run across an entire options chain in one call instead of looping row by row. It monkey-patches py_vollib so existing code gets large speedups with minimal changes.

✅ *Good at:* Orders-of-magnitude faster IV/Greeks computation over full option chains versus scalar py_vollib.  
⚠️ *Limitations:* No commits since late 2024; inherits py_vollib's European-only scope.

**[fypy](https://github.com/jkirkby3/fypy)** · Python · ★ 147 · last push 2025-02-27  
fypy is a research-oriented Python pricing library from Justin Kirkby covering vanilla and exotic option pricing beyond Black-Scholes (Levy processes, PROJ/Fourier methods) plus model calibration to market data, complementing his MATLAB PROJ_Option_Pricing project.

✅ *Good at:* Academically-grounded exotic-option pricing (barrier, Asian, cliquet) under advanced jump/Levy models.  
⚠️ *Limitations:* No commits in over a year; aimed at researchers rather than production trading systems.

**[QuantLib.jl](https://github.com/pazzo83/QuantLib.jl)** · Julia · ★ 143 · last push 2020-02-18  
A pure-Julia reimplementation of large parts of QuantLib, including option pricing engines, term structures and instruments, intended to exploit Julia's speed without C++ bindings.

✅ *Good at:* Demonstrating idiomatic-Julia derivatives pricing without an FFI dependency.  
⚠️ *Limitations:* Development stalled around 2020; incompatible with modern Julia package versions without patching.

**[RQuantLib](https://github.com/eddelbuettel/rquantlib)** · C++ · ★ 136 · last push 2026-07-26  
RQuantLib exposes core QuantLib option pricing, fixed-income and calendar functions to R via Rcpp, maintained by Dirk Eddelbuettel. It is the standard route for R users who need Black-Scholes, binomial and barrier option pricers backed by QuantLib's C++ engine.

✅ *Good at:* Bringing QuantLib pricing functions into R workflows and Rcpp-based quant pipelines.  
⚠️ *Limitations:* Exposes only a curated subset of QuantLib's full instrument/engine surface.

**[py_lets_be_rational](https://github.com/vollib/py_lets_be_rational)** · Python · ★ 73 · last push 2026-05-29  
A Python port of Peter Jaeckel's 'Let's Be Rational' algorithm for extremely fast and accurate Black-Scholes implied-volatility inversion, used internally by py_vollib. It is the numerical core other IV-fitting tools build on when they need a reference-grade solver rather than a naive Newton-Raphson loop.

✅ *Good at:* Rational, non-iterative implied-volatility inversion that is both fast and accurate across the full moneyness range.  
⚠️ *Limitations:* Low-level utility library, not meant to be used standalone for pricing or Greeks.

**[libitofin](https://github.com/benbenbang/libitofin)** · Rust · ★ 57 · last push 2026-09-21  
libitofin is a newer high-performance Rust quantitative-finance library targeting pricing, risk, and numerical tooling with a speed-and-safety focus similar to RustQuant, under very active daily development as of September 2026.

✅ *Good at:* Fast, low-level numerical building blocks for pricing and risk in Rust trading systems.  
⚠️ *Limitations:* Small community and early-stage API relative to RustQuant or QuantLib.

**[black_scholes_rust](https://github.com/danielhstahl/black_scholes_rust)** · Rust · ★ 25 · last push 2026-01-18  
A focused Rust crate implementing Black-Scholes pricing and Greeks, useful as a fast, embeddable building block for Rust-based options tools or as a WASM target for browser pricers.

✅ *Good at:* Minimal, fast Black-Scholes pricing/Greeks as a Rust crate dependency.  
⚠️ *Limitations:* Narrow scope (Black-Scholes only), no implied-volatility surface or exotic support.

**[pyvolr](https://github.com/yipjunkai/pyvolr)** · Python · ★ 4 · last push 2026-09-14  
pyvolr is a newer, actively-developed Python package with a Rust core positioning itself explicitly as a modern drop-in replacement for the increasingly stale py_vollib, offering Black-Scholes-Merton pricing, Greeks and implied volatility with better performance and maintenance.

✅ *Good at:* Modern, faster reimplementation of py_vollib's API for teams wanting an actively maintained alternative.  
⚠️ *Limitations:* Very new project with a tiny user base and unproven long-term maintenance track record.

</details>

### Volatility surfaces

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**VolGAN**](https://github.com/milenavuletic/VolGAN) | 115 | Python | 🟠 | Generating plausible, arbitrage-free synthetic IV surfaces for scenario analysis and risk simulation. |
| [**crypto-volatility-surface**](https://github.com/joshuapjacob/crypto-volatility-surface) | 78 | Python | 🟠 | Turnkey, visually clean crypto (Binance) IV surface dashboard. |
| [**vol-surface-visualizer**](https://github.com/dwasse/vol-surface-visualizer) | 63 | Python | 🟠 | Simple, well-known starting point for crypto options IV surface plotting. |
| [**VolaSurfer**](https://github.com/Baerenstein/VolaSurfer) | 12 | Python | 🟢 | Multi-asset (equity + crypto) implied vol surface visualization with pluggable data sources. |
| [**Stochastic-Volatility-Inspired Model (Idriss-Afra)**](https://github.com/Idriss-Afra/Stochastic-Volatility-Inspired-Model) | 11 | Jupyter Notebook | 🟢 | Practical, currently-maintained walkthrough of fitting SVI to real listed equity option data. |
| [**Arbitrage-free SVI volatility surfaces**](https://github.com/FinancialEngineerLab/Arbitrage-free-SVI-volatility-surfaces) | 6 | Python | 🟠 | Clear, paper-faithful implementation of the arbitrage-free SVI calibration recipe. |
| [**ssvi**](https://github.com/arkonique/ssvi) | 6 | Jupyter Notebook | 🟢 | End-to-end SSVI surface calibration pipeline from raw option-chain CSVs to a fitted surface. |

<details><summary>Explainers (7)</summary>

**[VolGAN](https://github.com/milenavuletic/VolGAN)** · Python · ★ 115 · last push 2025-03-10  
VolGAN is the reference implementation for 'VolGAN: a generative model for arbitrage-free implied volatility surfaces,' using a GAN architecture to generate realistic, no-arbitrage-consistent IV surface scenarios for risk simulation and stress testing.

✅ *Good at:* Generating plausible, arbitrage-free synthetic IV surfaces for scenario analysis and risk simulation.  
⚠️ *Limitations:* Academic research code, not a production surface-fitting tool for live option chains.

**[crypto-volatility-surface](https://github.com/joshuapjacob/crypto-volatility-surface)** · Python · ★ 78 · last push 2025-05-23  
A Streamlit-style dashboard that constructs and visualizes cryptocurrency implied-volatility surfaces from Binance options data, giving a quick interactive view of the crypto vol smile/term structure.

✅ *Good at:* Turnkey, visually clean crypto (Binance) IV surface dashboard.  
⚠️ *Limitations:* Tied to Binance options data specifically and not actively updated.

**[vol-surface-visualizer](https://github.com/dwasse/vol-surface-visualizer)** · Python · ★ 63 · last push 2022-12-08  
An early, popular volatility-surface visualizer for cryptocurrency options, plotting the IV smile/surface from exchange option-chain data.

✅ *Good at:* Simple, well-known starting point for crypto options IV surface plotting.  
⚠️ *Limitations:* Unmaintained since 2022; likely needs adaptation for current exchange APIs.

**[VolaSurfer](https://github.com/Baerenstein/VolaSurfer)** · Python · ★ 12 · last push 2025-11-25  
VolaSurfer is an implied-volatility surface visualizer supporting both equities and crypto options data providers and multiple fitting models, aimed at giving traders an interactive 3D view of the vol surface across strikes and maturities.

✅ *Good at:* Multi-asset (equity + crypto) implied vol surface visualization with pluggable data sources.  
⚠️ *Limitations:* Small, single-maintainer project with a limited set of built-in data connectors.

**[Stochastic-Volatility-Inspired Model (Idriss-Afra)](https://github.com/Idriss-Afra/Stochastic-Volatility-Inspired-Model)** · Jupyter Notebook · ★ 11 · last push 2026-09-12  
Part of an actively updated series constructing equity implied-volatility surfaces from listed option data, this repo implements the SVI parametrization specifically, with companion repos for SABR and general equity vol-surface calibration from the same author.

✅ *Good at:* Practical, currently-maintained walkthrough of fitting SVI to real listed equity option data.  
⚠️ *Limitations:* Educational/research scope rather than a hardened production library.

**[Arbitrage-free SVI volatility surfaces](https://github.com/FinancialEngineerLab/Arbitrage-free-SVI-volatility-surfaces)** · Python · ★ 6 · last push 2021-11-28  
A compact reference implementation of Gatheral & Jacquier's 'An arbitrage-free SVI volatility surface' calibration recipe, useful as a clean starting point for anyone implementing SVI parameterization from the original paper.

✅ *Good at:* Clear, paper-faithful implementation of the arbitrage-free SVI calibration recipe.  
⚠️ *Limitations:* Small, unmaintained reference script rather than a full surface-fitting library.

**[ssvi](https://github.com/arkonique/ssvi)** · Jupyter Notebook · ★ 6 · last push 2025-10-08  
Calibrates arbitrage-free implied volatility surfaces from option-chain data using the Surface SVI (SSVI) parametrization, including data preparation, fitting and visualization tools in a notebook-driven workflow.

✅ *Good at:* End-to-end SSVI surface calibration pipeline from raw option-chain CSVs to a fitted surface.  
⚠️ *Limitations:* Notebook-style research project, not packaged as an importable library.

</details>

### Options backtesting

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**optopsy**](https://github.com/goldspanlabs/optopsy) | 1.5k | Python | 🟢 | Fast, statistics-first backtesting across large families of options strategies (condors, spreads, calendars) with delta targeting. |
| [**OptionSuite**](https://github.com/sirnfs/OptionSuite) | 299 | Python | 🟢 | Bridging the backtest-to-live gap by sharing strategy logic between historical simulation and live trading. |
| [**bhav**](https://github.com/rajmaurya0904/bhav) | 26 | Python | 🟢 | Realistic-cost NSE index/stock options backtesting for the Indian market, an underserved niche in most Western tools. |
| [**optopsy-mcp**](https://github.com/goldspanlabs/optopsy-mcp) | 20 | Rust | 🟢 | Fast Rust-native options backtesting exposed as an MCP tool for AI-agent-driven research workflows. |
| [**gex-backtesting**](https://github.com/emlama/gex-backtesting) | 11 | Jupyter Notebook | 🟢 | Bridging gamma-exposure analytics with an actual 0DTE backtesting dataset/workflow. |

<details><summary>Explainers (5)</summary>

**[optopsy](https://github.com/goldspanlabs/optopsy)** · Python · ★ 1.5k · last push 2026-06-30  
Optopsy is the most popular open-source options backtesting and statistics library for Python, letting users go from a strategy question (e.g. '45-DTE SPX iron condors with a 50% profit target') to detailed performance stats quickly. It ships 38+ built-in strategy templates (verticals, condors, butterflies, calendars, diagonals), per-leg delta targeting, and a capital-tracking trade simulator. This is the actively maintained continuation of the original apryor6/optopsy project, now under goldspanlabs.

✅ *Good at:* Fast, statistics-first backtesting across large families of options strategies (condors, spreads, calendars) with delta targeting.  
⚠️ *Limitations:* Requires the user to supply historical options-chain data (e.g. OptionsDX/CBOE) rather than bundling it.

**[OptionSuite](https://github.com/sirnfs/OptionSuite)** · Python · ★ 299 · last push 2026-06-01  
OptionSuite is a modular framework for both backtesting options strategies and live trading them, designed to be extensible so users can plug in new strategies, brokers and risk rules. It is one of the few open-source projects that shares a single strategy definition between backtest and live execution modes.

✅ *Good at:* Bridging the backtest-to-live gap by sharing strategy logic between historical simulation and live trading.  
⚠️ *Limitations:* Smaller community and less polished documentation than Optopsy; broker integrations require setup work.

**[bhav](https://github.com/rajmaurya0904/bhav)** · Python · ★ 26 · last push 2026-07-19  
An open-source NSE (India) options backtesting engine built around Upstox historical data, with a realistic Indian brokerage/cost model, deterministic Parquet-based outputs, and a Next.js dashboard for reviewing results.

✅ *Good at:* Realistic-cost NSE index/stock options backtesting for the Indian market, an underserved niche in most Western tools.  
⚠️ *Limitations:* Tied to Upstox data/cost assumptions and the Indian market structure specifically.

**[optopsy-mcp](https://github.com/goldspanlabs/optopsy-mcp)** · Rust · ★ 20 · last push 2026-04-07  
A Rust rewrite of Optopsy's backtesting engine exposed through the Model Context Protocol (MCP), letting AI coding/analysis agents (e.g. Claude, Cursor) drive options backtests directly as a tool call rather than through Python scripting.

✅ *Good at:* Fast Rust-native options backtesting exposed as an MCP tool for AI-agent-driven research workflows.  
⚠️ *Limitations:* Newer project with a much smaller feature surface than the mature Python Optopsy.

**[gex-backtesting](https://github.com/emlama/gex-backtesting)** · Jupyter Notebook · ★ 11 · last push 2026-03-03  
A focused SPX 0DTE gamma-exposure analysis toolkit built on 305 days of enriched options trade data, used to backtest how GEX regimes relate to 0DTE price behavior.

✅ *Good at:* Bridging gamma-exposure analytics with an actual 0DTE backtesting dataset/workflow.  
⚠️ *Limitations:* Notebook-based research project scoped narrowly to SPX 0DTE, not a general backtesting framework.

</details>

### Greeks & risk

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**deribit-position-greeks**](https://github.com/cryptarbitrage-code/deribit-position-greeks) | 47 | Python | 🟠 | Simple, direct portfolio-Greeks aggregation for Deribit BTC/ETH options accounts. |
| [**options-scanner**](https://github.com/jwolberg/options-scanner) | 36 | JavaScript | 🟢 | Multi-ticker at-a-glance view combining GEX, skew and dealer-positioning signals with LLM-assisted interpretation. |
| [**traders-edge-mcp**](https://github.com/jsconiers/traders-edge-mcp) | 2 | Python | 🟢 | Broad, key-less 0DTE risk/positioning dashboard (GEX, vanna, charm, expected move) usable directly by AI coding agents via MCP. |
| [**flashalpha-mcp**](https://github.com/FlashAlpha-lab/flashalpha-mcp) | 1 | — | 🟢 | Turning a commercial options-analytics API into an agent-callable MCP tool for GEX/Greeks/vol-surface queries. |

<details><summary>Explainers (4)</summary>

**[deribit-position-greeks](https://github.com/cryptarbitrage-code/deribit-position-greeks)** · Python · ★ 47 · last push 2022-03-22  
A script that pulls a trader's live Deribit options positions and aggregates portfolio-level Greeks (delta, gamma, vega, theta), giving crypto options traders a quick risk snapshot without needing Deribit's own UI tools.

✅ *Good at:* Simple, direct portfolio-Greeks aggregation for Deribit BTC/ETH options accounts.  
⚠️ *Limitations:* Unmaintained since 2022 and tightly coupled to the Deribit API of that era.

**[options-scanner](https://github.com/jwolberg/options-scanner)** · JavaScript · ★ 36 · last push 2026-07-03  
An options market dashboard for scanning gamma exposure, volatility structure, skew, and dealer positioning across multiple tickers at once, with on-demand Claude AI analysis layered on top of the raw analytics.

✅ *Good at:* Multi-ticker at-a-glance view combining GEX, skew and dealer-positioning signals with LLM-assisted interpretation.  
⚠️ *Limitations:* Relies on external market-data and LLM API access; not a standalone offline analytics library.

**[traders-edge-mcp](https://github.com/jsconiers/traders-edge-mcp)** · Python · ★ 2 · last push 2026-09-16  
A 0DTE-focused SPX/SPXW options 'cockpit' exposed as an MCP server, bundling GEX, zero-gamma flip, call/put walls, max pain, 0DTE expected move, dealer DEX/vanna/charm, VIX term structure and an economic-event clock, all sourced key-less from CBOE delayed quotes and TreasuryDirect.

✅ *Good at:* Broad, key-less 0DTE risk/positioning dashboard (GEX, vanna, charm, expected move) usable directly by AI coding agents via MCP.  
⚠️ *Limitations:* Brand-new, single-maintainer project with only delayed (not real-time) data.

**[flashalpha-mcp](https://github.com/FlashAlpha-lab/flashalpha-mcp)** · — · ★ 1 · last push 2026-08-26  
An MCP server exposing real-time options analytics - gamma exposure (GEX), dealer positioning, volatility surfaces and Greeks - so any MCP-compatible AI assistant (Claude, Cursor, Windsurf) can query options risk metrics as a tool call.

✅ *Good at:* Turning a commercial options-analytics API into an agent-callable MCP tool for GEX/Greeks/vol-surface queries.  
⚠️ *Limitations:* Depends on the FlashAlpha hosted API/backend rather than being a self-contained open analytics engine.

</details>

### Gamma exposure (GEX)

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**gex-tracker**](https://github.com/Matteo-Ferrara/gex-tracker) | 216 | Python | 🟠 | Well-known, easy-to-read reference implementation of the classic GEX calculation methodology. |
| [**SPX-Gamma-Exposure**](https://github.com/jensolson/SPX-Gamma-Exposure) | 166 | Python | 🟠 | Well-documented, widely-forked reference GEX calculation specifically for SPX. |
| [**gammagrid**](https://github.com/gammagrid/gammagrid) | 66 | Python | 🟢 | No-code, self-hosted, actively-developed GEX/positioning dashboard that runs entirely on your own infrastructure. |
| [**deribit-max-pain**](https://github.com/cryptarbitrage-code/deribit-max-pain) | 42 | Python | 🟠 | Simple, direct max-pain computation for Deribit crypto options expiries. |
| [**SPX500-Gamma-Exposure-Calculator**](https://github.com/phammings/SPX500-Gamma-Exposure-Calculator) | 40 | Python | 🟠 | Simple, single-purpose script for generating an up-to-date SPX GEX chart. |
| [**gex-terminal**](https://github.com/zrack/gex-terminal) | 17 | Python | 🟢 | Lightweight, terminal-based intraday GEX and market-structure monitoring with session replay. |
| [**crypto_gamma_exposure**](https://github.com/schepal/crypto_gamma_exposure) | 17 | Jupyter Notebook | 🟠 | One of the first open studies applying equity-style GEX analysis to Bitcoin options. |
| [**gex_data**](https://github.com/GMestreM/gex_data) | 10 | Python | 🟢 | Clean separation of CBOE data retrieval from GEX computation, making it easy to swap the visualization layer. |
| [**gex-explained**](https://github.com/FlashAlpha-lab/gex-explained) | 10 | Python | 🟢 | Clear conceptual and mathematical walkthrough of GEX theory alongside working Python code. |
| [**Gex-Multi**](https://github.com/itsfabtrading/Gex-Multi) | 7 | Python | 🟢 | Multi-ticker GEX level computation (not just SPX) purely from free public CBOE data. |
| [**gex-heatmap**](https://github.com/tiz101/gex-heatmap) | 7 | Python | 🟢 | Real-time GEX heatmap delivery directly into Discord via a thinkorswim RTD data feed. |
| [**SPX_Gamma_Exposure (Nicholas-Battista)**](https://github.com/Nicholas-Battista/SPX_Gamma_Exposure) | 6 | Python | 🟠 | Zero-API-key, CSV-in/chart-out simplicity for a first GEX calculation. |

<details><summary>Explainers (12)</summary>

**[gex-tracker](https://github.com/Matteo-Ferrara/gex-tracker)** · Python · ★ 216 · last push 2023-04-08  
One of the earliest and most-starred open-source dealers' gamma exposure (GEX) trackers, computing and visualizing estimated market-maker gamma positioning from index/equity options chains, in the tradition popularized by SpotGamma-style commercial tools.

✅ *Good at:* Well-known, easy-to-read reference implementation of the classic GEX calculation methodology.  
⚠️ *Limitations:* No commits since 2023; likely needs updates for current data-source APIs.

**[SPX-Gamma-Exposure](https://github.com/jensolson/SPX-Gamma-Exposure)** · Python · ★ 166 · last push 2025-07-30  
Calculates an estimate of market-maker gamma exposure derived from S&P 500 index options, one of the most widely referenced open implementations of the SpotGamma-style GEX methodology and a common base for forks/derivatives.

✅ *Good at:* Well-documented, widely-forked reference GEX calculation specifically for SPX.  
⚠️ *Limitations:* Depends on manually-downloaded CBOE option-chain CSVs rather than a live data feed.

**[gammagrid](https://github.com/gammagrid/gammagrid)** · Python · ★ 66 · last push 2026-09-19  
GammaGrid is a self-hosted, Docker-deployable options gamma-exposure and positioning dashboard covering dealer GEX, max pain, open interest and IV surface, aimed at retail/prosumer traders who want a SpotGamma-style tool without a subscription and without writing code. It is under very active, near-daily development.

✅ *Good at:* No-code, self-hosted, actively-developed GEX/positioning dashboard that runs entirely on your own infrastructure.  
⚠️ *Limitations:* Requires the user to bring their own options-chain data source and Docker hosting.

**[deribit-max-pain](https://github.com/cryptarbitrage-code/deribit-max-pain)** · Python · ★ 42 · last push 2022-06-21  
Calculates the max-pain price (the strike at which option writers' aggregate payout is minimized) for BTC/ETH options on Deribit, a companion tool to the same author's deribit-position-greeks project.

✅ *Good at:* Simple, direct max-pain computation for Deribit crypto options expiries.  
⚠️ *Limitations:* Unmaintained since 2022; max pain itself is a contested/weak predictive signal.

**[SPX500-Gamma-Exposure-Calculator](https://github.com/phammings/SPX500-Gamma-Exposure-Calculator)** · Python · ★ 40 · last push 2024-11-11  
A script to generate the current S&P 500 gamma exposure chart from CBOE options data, in the same GEX methodology lineage as jensolson's project.

✅ *Good at:* Simple, single-purpose script for generating an up-to-date SPX GEX chart.  
⚠️ *Limitations:* Single-file script rather than a maintained, extensible tool.

**[gex-terminal](https://github.com/zrack/gex-terminal)** · Python · ★ 17 · last push 2026-09-20  
An open-source terminal UI for intraday gamma exposure, market-structure levels (walls, flip points) and replayable options research, aimed at traders who want a fast, keyboard-driven alternative to browser dashboards. Actively developed as of this week.

✅ *Good at:* Lightweight, terminal-based intraday GEX and market-structure monitoring with session replay.  
⚠️ *Limitations:* Very new/small project; terminal-only UI won't suit users wanting charts embedded in a web dashboard.

**[crypto_gamma_exposure](https://github.com/schepal/crypto_gamma_exposure)** · Jupyter Notebook · ★ 17 · last push 2020-09-12  
An early research project studying market-makers' gamma exposure specifically in Bitcoin options markets, part of a small family of Deribit-focused analytics notebooks by the same author (delta_hedge, deribit_data_collector).

✅ *Good at:* One of the first open studies applying equity-style GEX analysis to Bitcoin options.  
⚠️ *Limitations:* Research notebook from 2020, not updated for current Deribit API/market structure.

**[gex_data](https://github.com/GMestreM/gex_data)** · Python · ★ 10 · last push 2026-08-03  
A small API/pipeline to retrieve SPX option data from CBOE and compute gamma exposure, paired with a companion gex_dashboard repo for visualization, both by the same author and recently updated.

✅ *Good at:* Clean separation of CBOE data retrieval from GEX computation, making it easy to swap the visualization layer.  
⚠️ *Limitations:* Single-maintainer utility scoped to SPX/CBOE only.

**[gex-explained](https://github.com/FlashAlpha-lab/gex-explained)** · Python · ★ 10 · last push 2026-08-26  
An educational repo walking through what gamma exposure (GEX) is and how to compute it - covering the theory, math and Python code behind dealer hedging flows, gamma regimes and exposure analysis - useful as a teaching companion to the more product-focused FlashAlpha tools.

✅ *Good at:* Clear conceptual and mathematical walkthrough of GEX theory alongside working Python code.  
⚠️ *Limitations:* Educational in scope rather than a production analytics tool.

**[Gex-Multi](https://github.com/itsfabtrading/Gex-Multi)** · Python · ★ 7 · last push 2026-08-04  
Computes dealer gamma exposure levels for any stock, ETF or index from public CBOE option chains, including gamma flip, call/put walls, 0DTE sub-levels and expected-move bands, positioned as a 'own your levels' self-hosted alternative to paid GEX services.

✅ *Good at:* Multi-ticker GEX level computation (not just SPX) purely from free public CBOE data.  
⚠️ *Limitations:* Recently created with a small user base; relies on CBOE's free delayed data.

**[gex-heatmap](https://github.com/tiz101/gex-heatmap)** · Python · ★ 7 · last push 2026-03-04  
Generates a GEX (gamma exposure) heatmap from options data with Discord bot integration, sourcing quotes via thinkorswim's RTD feed for near-real-time levels delivered straight into a Discord server.

✅ *Good at:* Real-time GEX heatmap delivery directly into Discord via a thinkorswim RTD data feed.  
⚠️ *Limitations:* Requires a thinkorswim/RTD Windows setup, limiting portability.

**[SPX_Gamma_Exposure (Nicholas-Battista)](https://github.com/Nicholas-Battista/SPX_Gamma_Exposure)** · Python · ★ 6 · last push 2024-09-28  
A simple tool that takes a CSV of options data (e.g. from CBOE's free 15-minute-delayed feed) and produces a GEX chart, aimed at being an easy, no-API-key entry point into GEX analysis.

✅ *Good at:* Zero-API-key, CSV-in/chart-out simplicity for a first GEX calculation.  
⚠️ *Limitations:* Manual CSV workflow rather than an automated live pipeline.

</details>

### Volatility trading

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**arch**](https://github.com/bashtage/arch) | 1.6k | Python | 🟢 | Rigorous statistical volatility forecasting (GARCH/EGARCH/realized vol) that feeds VRP and vol-trading signals. |
| [**eigenquant53/VRP**](https://github.com/eigenquant53/VRP) | 33 | Python | 🟠 | Concrete, backtested implementation of VIX term-structure-based volatility trading logic. |
| [**trading-volatility**](https://github.com/peterchettiar/trading-volatility) | 11 | Jupyter Notebook | 🟠 | Clear, notebook-based exposition of VIX-term-structure trading logic for learning/research. |

<details><summary>Explainers (3)</summary>

**[arch](https://github.com/bashtage/arch)** · Python · ★ 1.6k · last push 2026-09-20  
Kevin Sheppard's `arch` package is the standard Python library for ARCH/GARCH-family conditional heteroskedasticity models and realized-volatility estimators, widely used to forecast volatility for variance-risk-premium and volatility-trading strategies. It is heavily used across academia and industry and remains under active development.

✅ *Good at:* Rigorous statistical volatility forecasting (GARCH/EGARCH/realized vol) that feeds VRP and vol-trading signals.  
⚠️ *Limitations:* Pure volatility-forecasting toolkit; no options pricing, Greeks, or execution logic.

**[eigenquant53/VRP](https://github.com/eigenquant53/VRP)** · Python · ★ 33 · last push 2022-12-20  
Backtests a thesis-paper strategy trading volatility based on the VIX futures term structure (contango/backwardation signals), a classic systematic volatility-carry approach.

✅ *Good at:* Concrete, backtested implementation of VIX term-structure-based volatility trading logic.  
⚠️ *Limitations:* One-off academic thesis backtest, not maintained or packaged as a reusable tool.

**[trading-volatility](https://github.com/peterchettiar/trading-volatility)** · Jupyter Notebook · ★ 11 · last push 2025-07-18  
Implements and backtests trading strategies based on the VIX term structure, exploring how contango/backwardation regimes in VIX futures can be systematically traded via VIX-linked products.

✅ *Good at:* Clear, notebook-based exposition of VIX-term-structure trading logic for learning/research.  
⚠️ *Limitations:* Research notebook rather than a live-tradable, maintained system.

</details>

### Options data

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**python-tradier**](https://github.com/cablehead/python-tradier) | 42 | Python | 🟠 | Historical reference for basic Tradier REST API access from Python. |
| [**options_scraper**](https://github.com/aosingh/options_scraper) | 11 | Python | 🟠 | Zero-cost, key-less access to a basic public options chain for prototyping. |
| [**tradier-api (mikecao)**](https://github.com/mikecao/tradier-api) | 10 | JavaScript | 🟠 | Only notable Node.js option for Tradier API access among the projects surveyed. |
| [**orats-python (FyZyX)**](https://github.com/FyZyX/orats-python) | 7 | Python | 🟠 | Straightforward Python access to ORATS' options-analytics and historical IV datasets. |
| [**flashalpha-python**](https://github.com/FlashAlpha-lab/flashalpha-python) | 6 | Python | 🟢 | One-stop SDK for a broad set of derived options analytics (GEX/DEX/VEX/flow/VRP) beyond raw chain data. |
| [**openbb-orats**](https://github.com/jjfantini/openbb-orats) | 4 | Python | 🟠 | Bringing commercial ORATS options data into the free, extensible OpenBB terminal ecosystem. |

<details><summary>Explainers (6)</summary>

**[python-tradier](https://github.com/cablehead/python-tradier)** · Python · ★ 42 · last push 2015-05-27  
One of the earliest Python clients for the Tradier brokerage/market-data API, which offers free-tier options-chain quotes and Greeks alongside equities trading - historically a popular starting point before Tradier's own SDKs matured.

✅ *Good at:* Historical reference for basic Tradier REST API access from Python.  
⚠️ *Limitations:* Unmaintained since 2015; Tradier's API has evolved significantly since.

**[options_scraper](https://github.com/aosingh/options_scraper)** · Python · ★ 11 · last push 2021-03-31  
A NASDAQ options-chain scraper that pulls free public option-chain data without requiring a broker/data-vendor API key, useful for quick, no-cost prototyping.

✅ *Good at:* Zero-cost, key-less access to a basic public options chain for prototyping.  
⚠️ *Limitations:* Fragile to NASDAQ site changes and unmaintained since 2021; no Greeks or historical data.

**[tradier-api (mikecao)](https://github.com/mikecao/tradier-api)** · JavaScript · ★ 10 · last push 2022-02-12  
A Node.js library wrapping the Tradier API, giving JavaScript/TypeScript trading tools access to Tradier's options chains and order-entry endpoints without a Python dependency.

✅ *Good at:* Only notable Node.js option for Tradier API access among the projects surveyed.  
⚠️ *Limitations:* Not actively maintained; limited endpoint coverage compared to Python wrappers.

**[orats-python (FyZyX)](https://github.com/FyZyX/orats-python)** · Python · ★ 7 · last push 2022-07-31  
A client SDK for the ORATS API, a widely used commercial provider of historical and live options data, implied volatility and Greeks, letting Python users pull ORATS datasets programmatically.

✅ *Good at:* Straightforward Python access to ORATS' options-analytics and historical IV datasets.  
⚠️ *Limitations:* Requires a paid ORATS subscription; unmaintained since 2022.

**[flashalpha-python](https://github.com/FlashAlpha-lab/flashalpha-python)** · Python · ★ 6 · last push 2026-09-09  
The official Python SDK for the FlashAlpha options-analytics API, providing a live options screener, GEX, DEX/VEX/CHEX exposures, options flow, 0DTE analytics, variance-risk-premium metrics, volatility surfaces and Greeks through one client.

✅ *Good at:* One-stop SDK for a broad set of derived options analytics (GEX/DEX/VEX/flow/VRP) beyond raw chain data.  
⚠️ *Limitations:* Requires a FlashAlpha API key/subscription; the SDK itself has no independent open dataset.

**[openbb-orats](https://github.com/jjfantini/openbb-orats)** · Python · ★ 4 · last push 2024-02-16  
An OpenBB Platform extension that connects ORATS options data into the broader open-source OpenBB terminal/SDK ecosystem, letting users query ORATS Greeks/IV data through OpenBB's unified data interface.

✅ *Good at:* Bringing commercial ORATS options data into the free, extensible OpenBB terminal ecosystem.  
⚠️ *Limitations:* Niche extension with a small user base, dependent on both OpenBB and an ORATS subscription.

</details>

### Crypto options

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**Derbit-Volatility-Visulization**](https://github.com/pengjin2/Derbit-Volatility-Visulization) | 84 | Python | 🟠 | Well-known early reference for visualizing Deribit crypto options IV. |
| [**delta_hedge**](https://github.com/schepal/delta_hedge) | 76 | Python | 🟠 | Concrete, working example of automated delta-hedging logic against a live crypto options exchange. |
| [**deribit_data_collector**](https://github.com/schepal/deribit_data_collector) | 75 | Python | 🟠 | Simple, complete Deribit option-chain snapshotting for BTC/ETH. |
| [**deribit-rs**](https://github.com/dovahcrow/deribit-rs) | 49 | Rust | 🟠 | Idiomatic, typed Rust access to Deribit's v2 WebSocket API for low-latency crypto options systems. |
| [**deribit-historical-data**](https://github.com/RiveChen/deribit-historical-data) | 40 | Python | 🟢 | Current, working access to Deribit's historical options/futures trade-tape API. |

<details><summary>Explainers (5)</summary>

**[Derbit-Volatility-Visulization](https://github.com/pengjin2/Derbit-Volatility-Visulization)** · Python · ★ 84 · last push 2020-04-05  
A visualization tool for Deribit crypto options implied volatility, one of the higher-starred early tools for viewing BTC/ETH options vol smiles and term structure.

✅ *Good at:* Well-known early reference for visualizing Deribit crypto options IV.  
⚠️ *Limitations:* Unmaintained since 2020; likely incompatible with current Deribit API without patching.

**[delta_hedge](https://github.com/schepal/delta_hedge)** · Python · ★ 76 · last push 2022-06-22  
A rebalancing tool that delta-hedges an options portfolio on the Deribit exchange, automatically adjusting a spot/futures hedge as option deltas change - a practical reference for crypto options market-makers or option sellers.

✅ *Good at:* Concrete, working example of automated delta-hedging logic against a live crypto options exchange.  
⚠️ *Limitations:* Unmaintained since 2022; production use would require significant hardening.

**[deribit_data_collector](https://github.com/schepal/deribit_data_collector)** · Python · ★ 75 · last push 2020-08-29  
A library for downloading the entire BTC and ETH options chain from Deribit, historically one of the most-used starting points for researchers building crypto options datasets before commercial vendors like Tardis/Amberdata became common.

✅ *Good at:* Simple, complete Deribit option-chain snapshotting for BTC/ETH.  
⚠️ *Limitations:* Unmaintained since 2020, likely needs updates for Deribit's current API.

**[deribit-rs](https://github.com/dovahcrow/deribit-rs)** · Rust · ★ 49 · last push 2024-07-04  
A Rust WebSocket client for the Deribit API v2, giving Rust-based crypto options trading systems typed, async access to Deribit's options/futures market data and order-entry endpoints.

✅ *Good at:* Idiomatic, typed Rust access to Deribit's v2 WebSocket API for low-latency crypto options systems.  
⚠️ *Limitations:* Not updated since mid-2024; API drift risk against Deribit's live endpoints.

**[deribit-historical-data](https://github.com/RiveChen/deribit-historical-data)** · Python · ★ 40 · last push 2026-08-02  
Downloads all options/futures trading (transaction) history via Deribit's history API, an actively maintained modern alternative to the older schepal/deribit_data_collector for building historical crypto derivatives datasets.

✅ *Good at:* Current, working access to Deribit's historical options/futures trade-tape API.  
⚠️ *Limitations:* Focused purely on data collection, with no analytics, pricing or hedging built in.

</details>

### Other

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**opstrat**](https://github.com/hashABCD/opstrat) | 168 | Python | 🟠 | Quick, clean payoff-diagram plotting for any multi-leg options strategy combination. |
| [**LoopTrader**](https://github.com/pattertj/LoopTrader) | 129 | Python | 🟠 | Well-structured, extensible architecture for building custom options trading bots. |
| [**awesome-options-analytics**](https://github.com/FlashAlpha-lab/awesome-options-analytics) | 44 | — | 🟢 | A single, actively-updated jumping-off point specifically for options/derivatives analytics tools. |
| [**alpaca-options-framework**](https://github.com/milgar7969/alpaca-options-framework) | 22 | Python | 🟢 | Actively maintained, Alpaca-specific scaffolding that captures real-world API gotchas for live options bots. |
| [**thales**](https://github.com/cm-jones/thales) | 11 | C++ | 🟠 | One of the few actively-designed C++ (rather than Python) open-source options trading bots. |

<details><summary>Explainers (5)</summary>

**[opstrat](https://github.com/hashABCD/opstrat)** · Python · ★ 168 · last push 2024-01-11  
opstrat is the most popular Python package purely for visualizing options-strategy payoff diagrams (single and multi-leg), pulling live quotes via yfinance and plotting P&L curves with matplotlib/seaborn - the closest open-source equivalent to a broker's strategy-builder payoff chart.

✅ *Good at:* Quick, clean payoff-diagram plotting for any multi-leg options strategy combination.  
⚠️ *Limitations:* Visualization-only (no backtesting or Greeks time-decay simulation); not updated since early 2024.

**[LoopTrader](https://github.com/pattertj/LoopTrader)** · Python · ★ 129 · last push 2023-02-01  
LoopTrader is an extensible framework for building automated options trading bots on top of Python, historically one of the higher-starred open-source options-bot frameworks, with pluggable strategy and broker components.

✅ *Good at:* Well-structured, extensible architecture for building custom options trading bots.  
⚠️ *Limitations:* No commits since early 2023; broker integrations likely need updating for current APIs.

**[awesome-options-analytics](https://github.com/FlashAlpha-lab/awesome-options-analytics)** · — · ★ 44 · last push 2026-08-20  
A curated 'awesome list' specifically for options analytics - tools, APIs, libraries, papers and educational resources for quantitative options trading - narrower and more current than the options section of the general awesome-quant list.

✅ *Good at:* A single, actively-updated jumping-off point specifically for options/derivatives analytics tools.  
⚠️ *Limitations:* A links list, not a tool itself; quality/accuracy of entries depends on community curation.

**[alpaca-options-framework](https://github.com/milgar7969/alpaca-options-framework)** · Python · ★ 22 · last push 2026-07-03  
A Python framework specifically for building live options trading bots on Alpaca Markets, handling asyncio/WebSocket streaming, position management, and documenting the various Alpaca options-API quirks and workarounds needed for reliable live trading.

✅ *Good at:* Actively maintained, Alpaca-specific scaffolding that captures real-world API gotchas for live options bots.  
⚠️ *Limitations:* Tightly coupled to Alpaca's brokerage API, not broker-agnostic.

**[thales](https://github.com/cm-jones/thales)** · C++ · ★ 11 · last push 2025-07-08  
Thales is a C++ options trading bot, a rarer entrant among the mostly-Python options-bot landscape, aimed at traders wanting lower-level performance and control over their execution loop.

✅ *Good at:* One of the few actively-designed C++ (rather than Python) open-source options trading bots.  
⚠️ *Limitations:* Small community, C++ raises the contribution/usage bar, and it has been quiet for over a year.

</details>

[⬆ back to top](#contents)

## AI, agents & machine learning

LLM multi-agent trading frameworks, alpha mining, reinforcement learning, market foundation models, trading MCP
servers and evaluation benchmarks. **TradingAgents**, **ai-hedge-fund**, **FinRL**, **Microsoft RD-Agent(Q)** and
**Kronos** (a foundation model trained on candlestick data) anchor the space.

**Key takeaways**

- Leakage-free live benchmarks (**DeepFund**, **Agent Market Arena**) find that even frontier LLMs struggle to make money once memorized history is taken away. Treat backtests of LLM traders with suspicion.
- Star counts in this area are often driven by virality. Weigh them against maturity.
- MCP servers now exist from Alpaca, Massive (formerly Polygon) and OpenBB, so agents can reach brokers and data directly.
- **Jev** is TypeSafe AI’s typed-judgment model (launched Sep 2026). Early trading projects use it either as the decision-maker or as a pass/reject gate on trades. See *Uses Jev*.

### LLM multi-agent frameworks

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**ai-hedge-fund**](https://github.com/virattt/ai-hedge-fund) | 63.6k | Python | 🟢 | Being an accessible, well-documented reference implementation of persona-based multi-agent equity analysis, and an early adopter of new LLM providers (Jev included). |
| [**Vibe-Trading (HKUDS)**](https://github.com/HKUDS/Vibe-Trading) | 33.7k | Python | 🟢 | Turning a plain-English strategy description into a runnable, backtested pipeline without writing factor code by hand. |
| [**TradingAgents-CN**](https://github.com/hsliuping/TradingAgents-CN) | 31.9k | Python | 🟢 | Best option for anyone wanting the TradingAgents architecture wired to Chinese market data and language. |
| [**FinGPT**](https://github.com/AI4Finance-Foundation/FinGPT) | 21.3k | Jupyter Notebook | 🟢 | Cheap, reproducible fine-tuning recipes for turning a small open LLM into a finance-sentiment or next-week-direction forecaster. |
| [**FinRobot**](https://github.com/AI4Finance-Foundation/FinRobot) | 8.0k | Jupyter Notebook | 🟢 | Producing structured equity-research-style reports and forecasts by chaining data-retrieval, analysis and LLM-reasoning agents. |
| [**FinMem-LLM-StockTrading**](https://github.com/pipiku915/FinMem-LLM-StockTrading) | 960 | Python | 🟠 | Demonstrating how structured, decayed memory retrieval improves an LLM trading agent's consistency versus stateless prompting. |
| [**AgenticTrading (FinAgent Orchestration Framework)**](https://github.com/Open-Finance-Lab/AgenticTrading) | 760 | Python | 🟢 | Reusable DAG-based agent orchestration and memory primitives that other trading-agent projects can build on rather than a single fixed strategy. |
| [**Stockagent**](https://github.com/MingyuJ666/Stockagent) | 704 | Python | 🟢 | Studying emergent price/behavior dynamics from many interacting LLM 'investors' rather than optimizing a single trading policy. |
| [**agents-for-openbb**](https://github.com/OpenBB-finance/agents-for-openbb) | 390 | Python | 🟢 | Reference implementation for wiring a custom LLM agent into a real financial analyst workspace UI. |
| [**vibetrading (VibeTradingLabs)**](https://github.com/VibeTradingLabs/vibetrading) | 93 | Python | 🟠 | A lighter-weight alternative implementation of the natural-language-to-strategy pattern with exchange deployment hooks. |
| [**FinCon**](https://github.com/The-FinAI/FinCon) | 67 | n/a | 🟠 | The paper's manager/analyst/risk-control hierarchy design is widely cited as a template for financial multi-agent systems. |
| [**StockSim**](https://github.com/harrypapadakis/StockSim) | 38 | Python | 🟠 | Giving LLM trading-agent researchers a dual-mode (live order book + fast historical) evaluation harness rather than a single fixed backtest. |
| [**Vibe-Trade (spyderweb47)**](https://github.com/spyderweb47/Vibe-Trade) | 15 | TypeScript | 🟠 | Packaging a full agentic trading stack (planner + backtester + multi-provider LLM + UI) into one easy local install. |
| [**AlphaAgentsV2**](https://github.com/LAKSHYAJAIN16/AlphaAgentsV2) | 1 | Python | 🟢 | The only readily available runnable approximation of BlackRock's published multi-agent stock-selection design. |

<details><summary>Explainers (14)</summary>

**[ai-hedge-fund](https://github.com/virattt/ai-hedge-fund)** · Python · ★ 63.6k · last push 2026-09-18  
virattt's ai-hedge-fund runs a set of LLM agents modeled on well-known investor personas (Buffett, Munger, Wood, Ackman, etc.) plus fundamentals/sentiment/valuation/risk-management agents that vote to produce a portfolio decision, for research/education not live trading. It is one of the most-starred entries in this whole space and is where the new TypeSafe 'Jev' model was first wired in as an LLM provider (v2.3.0, Sept 18 2026: `--model jev-1.13.0` after setting `TYPESAFE_API_KEY`), alongside 'aihf' running on Massive (formerly Polygon.io) market data.

✅ *Good at:* Being an accessible, well-documented reference implementation of persona-based multi-agent equity analysis, and an early adopter of new LLM providers (Jev included).  
⚠️ *Limitations:* Explicitly for research/education only; the investor 'personalities' are prompt-engineered heuristics, not validated models of those investors' actual processes.

**[Vibe-Trading (HKUDS)](https://github.com/HKUDS/Vibe-Trading)** · Python · ★ 33.7k · last push 2026-09-19  
Vibe-Trading lets a user describe a trading strategy idea in natural language and an LLM agent pipeline handles data collection (Yahoo Finance, Binance, Tushare, etc.), feature engineering across 460+ built-in alpha factors, and backtesting with transaction costs/slippage, exposing 54 MCP tools for any MCP client. It is explicitly research/backtesting-only (no live execution) and, alongside HKUDS/AI-Trader, is part of a very fast-growing family of 'vibe coding for trading' repos from the same HKU lab that hit tens of thousands of stars within days of release.

✅ *Good at:* Turning a plain-English strategy description into a runnable, backtested pipeline without writing factor code by hand.  
⚠️ *Limitations:* Extremely new with unusually rapid star growth typical of viral/hype AI repos in 2026 — treat star count with caution until independently verified for quality/longevity; explicitly not for live trading.

**[TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN)** · Python · ★ 31.9k · last push 2026-07-24  
A large, actively maintained Chinese-language enhancement of TauricResearch/TradingAgents that adds Tushare/AkShare A-share data sources, Chinese-language analyst reports, and China market regulatory context, plus Docker deployment. It has surpassed the original in stars within the Chinese quant community and spawned several further forks (TradingAgents-CN-lite, tradingagent_a for A-shares).

✅ *Good at:* Best option for anyone wanting the TradingAgents architecture wired to Chinese market data and language.  
⚠️ *Limitations:* Diverges from upstream TradingAgents in ways that make merging fixes back and forth hard to track; many competing CN forks fragment the ecosystem.

**[FinGPT](https://github.com/AI4Finance-Foundation/FinGPT)** · Jupyter Notebook · ★ 21.3k · last push 2026-09-14  
FinGPT is AI4Finance's open-source financial LLM effort: instruction-tuned/LoRA-adapted open models for sentiment analysis, robo-advising, and its widely used FinGPT-Forecaster (LLaMA-2 fine-tuned to output DOW30 stock-move predictions with reasoning from news and financials). Models are published to HuggingFace and it underpins several downstream trading-signal projects.

✅ *Good at:* Cheap, reproducible fine-tuning recipes for turning a small open LLM into a finance-sentiment or next-week-direction forecaster.  
⚠️ *Limitations:* Forecaster accuracy is dataset/period-specific and prone to look-ahead leakage if not evaluated carefully; not itself an execution system.

**[FinRobot](https://github.com/AI4Finance-Foundation/FinRobot)** · Jupyter Notebook · ★ 8.0k · last push 2026-09-11  
FinRobot is AI4Finance's open-source agent platform layering financial chain-of-thought prompting, a multi-source LLM scheduler, and concrete applications (equity research report generation, market forecasting, trading strategy agents) on top of AutoGen-style multi-agent orchestration. It is positioned as a broader platform than a single trading strategy, aimed at financial analysts as well as traders.

✅ *Good at:* Producing structured equity-research-style reports and forecasts by chaining data-retrieval, analysis and LLM-reasoning agents.  
⚠️ *Limitations:* Heavier and more notebook-driven than TradingAgents; less focused specifically on live trade execution.

**[FinMem-LLM-StockTrading](https://github.com/pipiku915/FinMem-LLM-StockTrading)** · Python · ★ 960 · last push 2024-08-18  
FinMem is a research LLM trading agent with a layered (working/episodic/semantic) memory module and a configurable 'character design' (risk profile) that decides trades from streamed news and price data, from the paper 'FinMem: A Performance-Enhanced LLM Trading Agent with Layered Memory and Character Design'. It is one of the most-cited early single-agent LLM trading memory designs and influenced FinAgent and FinCon's memory components.

✅ *Good at:* Demonstrating how structured, decayed memory retrieval improves an LLM trading agent's consistency versus stateless prompting.  
⚠️ *Limitations:* Not updated since mid-2024; single-ticker/single-agent scope compared to newer multi-agent frameworks.

**[AgenticTrading (FinAgent Orchestration Framework)](https://github.com/Open-Finance-Lab/AgenticTrading)** · Python · ★ 760 · last push 2026-09-21  
AgenticTrading, from Open Finance Lab (Columbia-affiliated group behind the FinRL/FinRL-Contest ecosystem), provides a general multi-agent architecture with memory systems and DAG-based planning components for building trading agents, distinct from NTU's academic 'FinAgent' paper of the same informal name.

✅ *Good at:* Reusable DAG-based agent orchestration and memory primitives that other trading-agent projects can build on rather than a single fixed strategy.  
⚠️ *Limitations:* Very actively churning (daily pushes as of Sept 2026) with sparse top-level documentation, making it harder to evaluate maturity from the repo alone.

**[Stockagent](https://github.com/MingyuJ666/Stockagent)** · Python · ★ 704 · last push 2026-06-16  
StockAgent (paper: 'When AI Meets Finance', arXiv:2407.18957, published in ACM TIST) is an LLM-driven multi-agent simulation where each agent role-plays an investor with distinct behavioral traits, trading against each other in an event-driven simulated real-world stock market to study how macro events, company news, and behavioral biases move simulated prices.

✅ *Good at:* Studying emergent price/behavior dynamics from many interacting LLM 'investors' rather than optimizing a single trading policy.  
⚠️ *Limitations:* It's a simulation/behavioral-economics research tool, not a strategy meant for live capital.

**[agents-for-openbb](https://github.com/OpenBB-finance/agents-for-openbb)** · Python · ★ 390 · last push 2026-07-01  
Official OpenBB example repo showing how to build and register custom AI agents (LLM-backed research/analysis assistants) that plug into the OpenBB Workspace, complementing OpenBB's MCP server extension.

✅ *Good at:* Reference implementation for wiring a custom LLM agent into a real financial analyst workspace UI.  
⚠️ *Limitations:* A scaffolding/example repo rather than a ready-made trading strategy agent.

**[vibetrading (VibeTradingLabs)](https://github.com/VibeTradingLabs/vibetrading)** · Python · ★ 93 · last push 2026-03-23  
An independent, smaller 'vibe trading' framework where users describe strategies in natural language and AI agents generate, backtest, and deploy executable code across exchanges — same concept as HKUDS/Vibe-Trading but a separate, much smaller project/organization.

✅ *Good at:* A lighter-weight alternative implementation of the natural-language-to-strategy pattern with exchange deployment hooks.  
⚠️ *Limitations:* Low activity since March 2026 and far smaller community than the HKUDS project of a similar name.

**[FinCon](https://github.com/The-FinAI/FinCon)** · n/a · ★ 67 · last push 2026-02-27  
FinCon (NeurIPS 2024) proposes a manager-analyst hierarchy of LLM agents with 'conceptual verbal reinforcement' — a self-critiquing mechanism that episodically updates a shared textual belief system instead of numeric RL rewards. The GitHub repo exists mainly as a placeholder: the authors stated the data agent depends on commercial APIs that block a full open release, and only single-agent components/datasets have been published.

✅ *Good at:* The paper's manager/analyst/risk-control hierarchy design is widely cited as a template for financial multi-agent systems.  
⚠️ *Limitations:* Full multi-agent code has not been publicly released; the repo is effectively a stub pointing to single-agent sub-projects.

**[StockSim](https://github.com/harrypapadakis/StockSim)** · Python · ★ 38 · last push 2025-07-15  
StockSim is an open-source simulation platform purpose-built to evaluate LLMs in realistic financial decision-making, offering both real-time order-book simulation and high-throughput historical backtesting with multi-agent coordination across multiple instruments.

✅ *Good at:* Giving LLM trading-agent researchers a dual-mode (live order book + fast historical) evaluation harness rather than a single fixed backtest.  
⚠️ *Limitations:* Small, academic-scale project with limited recent activity and adoption compared to TradingAgents/StockAgent.

**[Vibe-Trade (spyderweb47)](https://github.com/spyderweb47/Vibe-Trade)** · TypeScript · ★ 15 · last push 2026-04-22  
A single-install (pipx) AI trading agent built around a 'drop a SKILL.md, declare your tools, ship' pattern, bundling a planner, pattern detection, strategy backtesting, 9 LLM providers, multi-agent simulation and a Next.js web UI.

✅ *Good at:* Packaging a full agentic trading stack (planner + backtester + multi-provider LLM + UI) into one easy local install.  
⚠️ *Limitations:* Tiny single-contributor project with minimal external validation.

**[AlphaAgentsV2](https://github.com/LAKSHYAJAIN16/AlphaAgentsV2)** · Python · ★ 1 · last push 2026-09-18  
BlackRock's AlphaAgents paper (arXiv:2508.11152) describes a three-agent (fundamental/sentiment/valuation) LLM system for equity stock selection but released no code. AlphaAgentsV2 is a from-scratch community reimplementation explicitly built to fix what its author considers weaknesses in the original evaluation (look-ahead contamination, no controls, tiny single-sector sample, unmeasured debate/bias-mitigation claims).

✅ *Good at:* The only readily available runnable approximation of BlackRock's published multi-agent stock-selection design.  
⚠️ *Limitations:* Brand-new, single-contributor, essentially untested reimplementation, not an official BlackRock release.

</details>

### Alpha mining

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**RD-Agent (incl. RD-Agent(Q))**](https://github.com/microsoft/RD-Agent) | 14.7k | Python | 🟢 | Fully automating the propose-code-backtest-refine cycle for both alpha factors and predictive models rather than just one or the other. |
| [**QuantaAlpha**](https://github.com/QuantaAlpha/QuantaAlpha) | 1.5k | Python | 🟢 | Turning a plain-language research hypothesis into an automatically evolved and backtested set of alpha factors. |
| [**AlphaGen**](https://github.com/ICT-FinD-Lab/alphagen) | 1.2k | Python | 🟢 | Producing compact, human-readable alpha expressions (rather than black-box embeddings) whose combined predictive power is explicitly optimized. |
| [**QuantEvolve**](https://github.com/tarsyang/quantevolve) | 50 | Python | 🟠 | Producing a diverse portfolio of strategy candidates spanning different risk/return profiles instead of a single best strategy. |
| [**alpha-agent (zzzhhn)**](https://github.com/zzzhhn/alpha-agent) | 1 | Python | 🟢 | A-share-specific factor discovery workflow. |

<details><summary>Explainers (5)</summary>

**[RD-Agent (incl. RD-Agent(Q))](https://github.com/microsoft/RD-Agent)** · Python · ★ 14.7k · last push 2026-09-15  
Microsoft's RD-Agent automates the research-and-development loop (propose hypothesis, implement, test, refine) for data-driven AI; its quant-finance instantiation, RD-Agent(Q), is the first data-centric multi-agent framework that jointly co-optimizes factors and models on top of Qlib, reported to reach up to 2x higher annualized returns than classical factor libraries using 70% fewer factors. It is explicitly stated as a research tool, not investment advice.

✅ *Good at:* Fully automating the propose-code-backtest-refine cycle for both alpha factors and predictive models rather than just one or the other.  
⚠️ *Limitations:* Heavy dependency on Qlib and an LLM backend; Microsoft states it is not ready for real financial investment or advice.

**[QuantaAlpha](https://github.com/QuantaAlpha/QuantaAlpha)** · Python · ★ 1.5k · last push 2026-06-29  
QuantaAlpha combines LLM intelligence with evolutionary strategies to mine, evolve and validate quantitative alpha factors from a natural-language research direction, with a 'self-evolving trajectories' mechanism for refining candidate factors over generations.

✅ *Good at:* Turning a plain-language research hypothesis into an automatically evolved and backtested set of alpha factors.  
⚠️ *Limitations:* Newer project without a peer-reviewed paper backing its claims; validation methodology should be checked before trusting reported performance.

**[AlphaGen](https://github.com/ICT-FinD-Lab/alphagen)** · Python · ★ 1.2k · last push 2026-06-04  
AlphaGen (KDD 2023) generates sets of formulaic (symbolic-expression) alpha factors via reinforcement learning, optimizing for factors that work synergistically together rather than mining each alpha independently, with a Qlib-based backtest/trade-decision demo. Also mirrored as RL-MLDM/alphagen.

✅ *Good at:* Producing compact, human-readable alpha expressions (rather than black-box embeddings) whose combined predictive power is explicitly optimized.  
⚠️ *Limitations:* Formulaic-alpha search space and RL training make it computationally heavier than simple factor libraries; China-market (baostock) data defaults require adaptation for other markets.

**[QuantEvolve](https://github.com/tarsyang/quantevolve)** · Python · ★ 50 · last push 2025-05-30  
An implementation (fork of OpenEvolve) of the QuantEvolve idea (arXiv:2510.18569): an evolutionary multi-agent framework combining quality-diversity optimization with hypothesis-driven strategy generation, organizing a population of strategies on a multi-dimensional grid (Sharpe, turnover, drawdown, category, etc.) to maintain a diverse set of effective strategies instead of converging on one.

✅ *Good at:* Producing a diverse portfolio of strategy candidates spanning different risk/return profiles instead of a single best strategy.  
⚠️ *Limitations:* Community fork of a research idea, not the (unreleased) original paper's own codebase; limited recent maintenance.

**[alpha-agent (zzzhhn)](https://github.com/zzzhhn/alpha-agent)** · Python · ★ 1 · last push 2026-09-08  
A small multi-agent system for automated quantitative factor discovery specifically targeting China A-share markets, using LLM agents to propose and evaluate candidate factors.

✅ *Good at:* A-share-specific factor discovery workflow.  
⚠️ *Limitations:* Very new, single-star, essentially unvalidated project.

</details>

### Reinforcement learning

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**TensorTrade**](https://github.com/tensortrade-org/tensortrade) | 7.1k | Python | 🟢 | Highly modular composition of RL trading pipelines when you want fine control over exchange/reward/action abstractions. |
| [**ElegantRL**](https://github.com/AI4Finance-Foundation/ElegantRL) | 4.4k | Python | 🟢 | Fast, cloud/GPU-scalable RL training that plugs into FinRL-style trading environments. |
| [**FinRL-Trading / FinRL-X**](https://github.com/AI4Finance-Foundation/FinRL-Trading) | 3.7k | Python | 🟢 | Bridging RL-trained policies to live paper/real brokerage execution. |
| [**TradeMaster**](https://github.com/TradeMaster-NTU/TradeMaster) | 3.1k | Jupyter Notebook | 🟠 | Breadth: one platform spanning multiple markets, trading scenarios and RL algorithms with built-in evaluation/visualization. |
| [**TradingGym**](https://github.com/Yvictor/TradingGym) | 1.9k | Python | 🟠 | Simple, dependency-light Gym environment for quick RL-trading prototyping. |
| [**FinRL_DeepSeek**](https://github.com/benstaf/FinRL_DeepSeek) | 331 | Jupyter Notebook | 🟠 | A concrete, reproducible template for combining LLM-derived news sentiment/risk signals with classic RL trading (rather than pure end-to-end LLM decision-making). |

<details><summary>Explainers (6)</summary>

**[TensorTrade](https://github.com/tensortrade-org/tensortrade)** · Python · ★ 7.1k · last push 2026-02-19  
TensorTrade is a modular, composable Python framework (predates and parallels FinRL) for building, training, evaluating and deploying robust RL trading agents, with pluggable exchanges, reward schemes, action schemes and observation pipelines.

✅ *Good at:* Highly modular composition of RL trading pipelines when you want fine control over exchange/reward/action abstractions.  
⚠️ *Limitations:* Development pace has slowed compared to FinRL's ecosystem; smaller active community.

**[ElegantRL](https://github.com/AI4Finance-Foundation/ElegantRL)** · Python · ★ 4.4k · last push 2026-02-20  
ElegantRL is AI4Finance's massively parallel, GPU-heavy DRL library (lightweight, stable, scalable) used as the training backend behind several FinRL trading agents when large-scale/parallel training is needed.

✅ *Good at:* Fast, cloud/GPU-scalable RL training that plugs into FinRL-style trading environments.  
⚠️ *Limitations:* General-purpose RL library, not finance-specific out of the box; needs FinRL/FinRL-Meta for market environments.

**[FinRL-Trading / FinRL-X](https://github.com/AI4Finance-Foundation/FinRL-Trading)** · Python · ★ 3.7k · last push 2026-09-18  
Rebranded as 'FinRL-X: An AI-Native Modular Infrastructure for Quantitative Trading', this is AI4Finance's newer production-oriented layer connecting FinRL policies to live broker integrations (e.g. Alpaca) rather than just backtesting.

✅ *Good at:* Bridging RL-trained policies to live paper/real brokerage execution.  
⚠️ *Limitations:* Newer/rebranded component with less battle-testing than core FinRL; live-trading RL carries substantial financial risk.

**[TradeMaster](https://github.com/TradeMaster-NTU/TradeMaster)** · Jupyter Notebook · ★ 3.1k · last push 2025-06-04  
TradeMaster (NTU) is a first-of-its-kind unified platform covering the full RL-for-trading pipeline — data, 15 RL algorithms, six trading scenarios (order execution, portfolio management, etc.), and visualization/evaluation tools — across China A-shares, US stocks, crypto and forex.

✅ *Good at:* Breadth: one platform spanning multiple markets, trading scenarios and RL algorithms with built-in evaluation/visualization.  
⚠️ *Limitations:* No pushes since mid-2025, so newer RL algorithms/market data integrations are not being added.

**[TradingGym](https://github.com/Yvictor/TradingGym)** · Python · ★ 1.9k · last push 2024-02-11  
An early, widely-referenced OpenAI-Gym-style trading and backtesting environment for training RL agents (or simple rule-based algorithms), predating FinRL and still used as a lightweight environment in many RL-trading tutorials.

✅ *Good at:* Simple, dependency-light Gym environment for quick RL-trading prototyping.  
⚠️ *Limitations:* Not actively maintained; superseded in features by FinRL/FinRL-Meta/TensorTrade for serious work.

**[FinRL_DeepSeek](https://github.com/benstaf/FinRL_DeepSeek)** · Jupyter Notebook · ★ 331 · last push 2025-04-08  
Code for 'FinRL-DeepSeek: LLM-Infused Risk-Sensitive Reinforcement Learning for Trading Agents' (arXiv:2502.07393), which extends CVaR-PPO by injecting LLM-generated (DeepSeek-V3/Qwen2.5/Llama-3.3) sentiment and risk signals from financial news into the RL agent's reward shaping, backtested on Nasdaq-100. It formed the basis of Task 1 in the FinRL Contest 2025.

✅ *Good at:* A concrete, reproducible template for combining LLM-derived news sentiment/risk signals with classic RL trading (rather than pure end-to-end LLM decision-making).  
⚠️ *Limitations:* Backtested on one index/period; not updated since April 2025.

</details>

### ML trading

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**Stock-Prediction-Models**](https://github.com/huseinzol05/Stock-Prediction-Models) | 9.5k | Jupyter Notebook | 🟠 | Breadth of example implementations for many classic and deep ML forecasting techniques applied to stocks in one place. |
| [**stockpredictionai**](https://github.com/borisbanushev/stockpredictionai) | 5.6k | JavaScript | 🟠 | Approachable, well-explained walkthrough of applying GANs to time-series price prediction. |
| [**Numerai example-scripts**](https://github.com/numerai/example-scripts) | 1.2k | Jupyter Notebook | 🟢 | A real, ongoing live proving-ground for ML models against actual market-neutral hedge fund capital, with obfuscated data avoiding overfitting-to-known-tickers. |

<details><summary>Explainers (3)</summary>

**[Stock-Prediction-Models](https://github.com/huseinzol05/Stock-Prediction-Models)** · Jupyter Notebook · ★ 9.5k · last push 2023-04-16  
A large, very popular grab-bag of machine learning and deep learning approaches to stock forecasting and simple trading bots/simulations (LSTMs, GAs, RL, attention models, etc.) — widely used as a learning reference despite being an unmaintained collection rather than a coherent framework.

✅ *Good at:* Breadth of example implementations for many classic and deep ML forecasting techniques applied to stocks in one place.  
⚠️ *Limitations:* Unmaintained since 2023; individual notebooks vary widely in rigor and many overfit small samples — treat as educational examples, not vetted strategies.

**[stockpredictionai](https://github.com/borisbanushev/stockpredictionai)** · JavaScript · ★ 5.6k · last push 2025-08-19  
A very widely shared single notebook/write-up demonstrating a GAN (LSTM generator, CNN discriminator) approach to predicting stock price movements, popular as an educational deep-dive despite being one illustrative example rather than a robust methodology.

✅ *Good at:* Approachable, well-explained walkthrough of applying GANs to time-series price prediction.  
⚠️ *Limitations:* Widely criticized in the ML-for-trading community as overfit/oversold results on a small sample; not a validated trading strategy.

**[Numerai example-scripts](https://github.com/numerai/example-scripts)** · Jupyter Notebook · ★ 1.2k · last push 2026-08-22  
Official starter scripts/notebooks for the Numerai tournament, where data scientists submit ML models on obfuscated financial features to a crowd-sourced hedge fund that stakes real capital on aggregated predictions — a genuinely live, real-money application of ML trading at scale.

✅ *Good at:* A real, ongoing live proving-ground for ML models against actual market-neutral hedge fund capital, with obfuscated data avoiding overfitting-to-known-tickers.  
⚠️ *Limitations:* Only the starter kit is open; the actual fund's model-selection/staking mechanics and most competitors' models are private.

</details>

### Foundation models

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**Kronos**](https://github.com/shiyu-coder/Kronos) | 39.3k | Python | 🟢 | Purpose-built representation learning/forecasting over raw candlestick data across many exchanges and assets, with released fine-tuning scripts. |
| [**TimesFM**](https://github.com/google-research/timesfm) | 33.4k | Python | 🟢 | Fast, strong zero-shot forecasts across varied frequencies/domains at large scale. |
| [**Chronos**](https://github.com/amazon-science/chronos-forecasting) | 5.9k | Python | 🟢 | Strong zero-shot forecasting performance across arbitrary time series without per-series retraining. |
| [**Moirai (uni2ts)**](https://github.com/SalesforceAIResearch/uni2ts) | 1.6k | Jupyter Notebook | 🟢 | Handling multivariate series of arbitrary dimension/frequency with one pretrained model, reducing per-series engineering. |

<details><summary>Explainers (4)</summary>

**[Kronos](https://github.com/shiyu-coder/Kronos)** · Python · ★ 39.3k · last push 2026-04-13  
Kronos (AAAI 2026) is the first open-source foundation model trained specifically on the 'language' of financial markets — K-line (OHLCV candlestick) sequences from 45+ global exchanges — using a two-stage tokenizer + autoregressive transformer design built to handle the high-noise, non-stationary character of market data, unlike general-purpose TSFMs. It has a live BTC/USDT forecast demo and has become the most-starred entry in this whole catalog.

✅ *Good at:* Purpose-built representation learning/forecasting over raw candlestick data across many exchanges and assets, with released fine-tuning scripts.  
⚠️ *Limitations:* A forecasting/representation model, not a trading strategy or execution system; predicting noisy financial series remains fundamentally hard regardless of pretraining.

**[TimesFM](https://github.com/google-research/timesfm)** · Python · ★ 33.4k · last push 2026-09-15  
Google Research's TimesFM is a decoder-only pretrained forecasting foundation model, one of the largest and most popular general time-series foundation models; like Chronos it is commonly applied (with mixed results) to financial time series in research and hobbyist projects.

✅ *Good at:* Fast, strong zero-shot forecasts across varied frequencies/domains at large scale.  
⚠️ *Limitations:* General-purpose, not trained on financial microstructure specifics; performance on noisy financial series needs independent validation.

**[Chronos](https://github.com/amazon-science/chronos-forecasting)** · Python · ★ 5.9k · last push 2026-09-17  
Amazon's Chronos tokenizes time-series values and trains a language-model architecture (T5-style) on them for zero-shot probabilistic forecasting; it is one of the most-used general time-series foundation models and is frequently benchmarked/fine-tuned by researchers on financial price series despite not being finance-specific.

✅ *Good at:* Strong zero-shot forecasting performance across arbitrary time series without per-series retraining.  
⚠️ *Limitations:* Not finance-specialized (no market microstructure/exchange awareness), so raw zero-shot use on prices needs careful evaluation against a naive baseline.

**[Moirai (uni2ts)](https://github.com/SalesforceAIResearch/uni2ts)** · Jupyter Notebook · ★ 1.6k · last push 2026-06-02  
Salesforce's uni2ts is the training/inference codebase behind the Moirai family of universal time-series forecasting transformers (now Moirai 2.0), handling arbitrary frequency/dimensionality series in one architecture and ranking near the top of the GIFT-Eval leaderboard; used in finance research as a general zero-shot forecaster alongside Chronos/TimesFM.

✅ *Good at:* Handling multivariate series of arbitrary dimension/frequency with one pretrained model, reducing per-series engineering.  
⚠️ *Limitations:* Same caveat as other general TSFMs: not finance-native, and market data's non-stationarity/regime shifts remain a known weak point for all of these models.

</details>

### MCP servers

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**Financial Datasets MCP Server**](https://github.com/financial-datasets/mcp-server) | 2.3k | Python | 🟠 | Clean, purpose-built tool surface for company fundamentals plus prices/news in one MCP server. |
| [**Alpaca MCP Server**](https://github.com/alpacahq/alpaca-mcp-server) | 978 | Python | 🟢 | First-party, broker-maintained MCP integration that connects an LLM agent directly to real order placement and account data. |
| [**mcp_massive (formerly mcp_polygon)**](https://github.com/massive-com/mcp_massive) | 391 | Python | 🟢 | Broad, first-party coverage of multi-asset-class market data as MCP tools for any LLM agent. |
| [**yahoo-finance-mcp**](https://github.com/Alex2Yang97/yahoo-finance-mcp) | 354 | Python | 🟢 | Free, no-API-key market/fundamentals data access for LLM agents, good for prototyping without cost. |
| [**ibkr-mcp-server (ArjunDivecha)**](https://github.com/ArjunDivecha/ibkr-mcp-server) | 35 | Python | 🟠 | Bringing a full-featured brokerage (multi-account, options, short-selling) to MCP clients, unlike the many minimal IBKR MCP forks. |

<details><summary>Explainers (5)</summary>

**[Financial Datasets MCP Server](https://github.com/financial-datasets/mcp-server)** · Python · ★ 2.3k · last push 2025-06-05  
An MCP server for the Financial Datasets stock market API, giving LLM agents tools for income statements, balance sheets, cash flow statements, current/historical stock and crypto prices, and company news — a popular, lightweight fundamentals-data MCP used by several of the LLM-trading-agent projects in this catalog for grounding.

✅ *Good at:* Clean, purpose-built tool surface for company fundamentals plus prices/news in one MCP server.  
⚠️ *Limitations:* No commits since mid-2025 despite strong star count; check for maintained forks before depending on it in production.

**[Alpaca MCP Server](https://github.com/alpacahq/alpaca-mcp-server)** · Python · ★ 978 · last push 2026-09-15  
Alpaca's official MCP server exposes trading (stocks, ETFs, crypto, options), account/portfolio data, and market data analysis as MCP tools so any MCP-compatible LLM client (Claude, IDEs, etc.) can research and place trades in plain English against a real (paper or live) brokerage.

✅ *Good at:* First-party, broker-maintained MCP integration that connects an LLM agent directly to real order placement and account data.  
⚠️ *Limitations:* Ties an LLM directly to a real brokerage account — meaningful operational/financial risk if used for live (non-paper) trading without guardrails.

**[mcp_massive (formerly mcp_polygon)](https://github.com/massive-com/mcp_massive)** · Python · ★ 391 · last push 2026-06-11  
The official MCP server for Massive.com (the rebrand of Polygon.io) financial market data, exposing stock/options/forex/crypto aggregates, real-time and historical trades/quotes, snapshots, fundamentals and reference data as MCP tools. The polygon-io/mcp_polygon GitHub path now redirects here following the Polygon → Massive rebrand.

✅ *Good at:* Broad, first-party coverage of multi-asset-class market data as MCP tools for any LLM agent.  
⚠️ *Limitations:* Requires a paid Massive/Polygon API key for most non-trivial usage tiers; several third-party forks (stockseas/polygon-mcp, EternisAI/mcp_polygon) exist and can drift out of sync.

**[yahoo-finance-mcp](https://github.com/Alex2Yang97/yahoo-finance-mcp)** · Python · ★ 354 · last push 2026-09-19  
A community MCP server wrapping Yahoo Finance data (historical prices, company info, financial statements, options data, market news) so it can be queried by any MCP client without a paid API key.

✅ *Good at:* Free, no-API-key market/fundamentals data access for LLM agents, good for prototyping without cost.  
⚠️ *Limitations:* Depends on Yahoo Finance's unofficial data endpoints, which are subject to change/rate-limiting/ToS risk.

**[ibkr-mcp-server (ArjunDivecha)](https://github.com/ArjunDivecha/ibkr-mcp-server)** · Python · ★ 35 · last push 2025-07-23  
One of the more feature-complete of many community Interactive Brokers MCP servers, providing multi-account support, real-time market data, portfolio management, short-selling analysis and trading operations for Claude Desktop/Code via the IBKR API. Numerous parallel implementations exist (GaoChX/ibkr-mcp-server, omdv/ibkr-mcp-server, jinyiabc/ibkr-mcp, code-rabi/interactive-brokers-mcp, etc.) since IBKR has no official MCP server.

✅ *Good at:* Bringing a full-featured brokerage (multi-account, options, short-selling) to MCP clients, unlike the many minimal IBKR MCP forks.  
⚠️ *Limitations:* Unofficial/community-maintained (IBKR itself does not publish an MCP server) and requires a running TWS/IB Gateway; the IBKR MCP ecosystem is fragmented across many near-duplicate small repos of varying quality.

</details>

### Benchmarks

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**AI-Trader (HKUDS)**](https://github.com/HKUDS/AI-Trader) | 22.4k | Python | 🟢 | Rigorous, contamination-resistant, multi-market live evaluation methodology for autonomous trading agents. |
| [**FinNLP**](https://github.com/AI4Finance-Foundation/FinNLP) | 1.5k | Jupyter Notebook | 🟠 | Financial data-scraping/NLP-preprocessing building blocks reused across the AI4Finance ecosystem. |
| [**PIXIU / FinBen**](https://github.com/The-FinAI/PIXIU) | 886 | Jupyter Notebook | 🟠 | Comprehensive, standardized evaluation tasks/datasets for judging any financial LLM's competence, not just trading decisions. |
| [**DeepFund**](https://github.com/HKUSTDial/DeepFund) | 296 | Python | 🟢 | Honestly exposing that most current LLMs are not yet good active fund managers, by removing the historical-data leakage that inflates backtested LLM trading results. |
| [**InvestLM**](https://github.com/AbaciNLP/InvestLM) | 156 | Python | 🟠 | Showing that careful small-scale instruction curation (rather than massive data) can produce a competitive financial-domain LLM. |
| [**Agent Trading Arena**](https://github.com/MTMQuantAI/Agent-Trading-Arena) | 145 | Python | 🟢 | Isolating and testing an LLM agent's raw numerical/quantitative reasoning in a market context, independent of memorized market priors. |
| [**INVESTOR-BENCH**](https://github.com/felis33/INVESTOR-BENCH) | 30 | Python | 🟠 | Systematic, multi-asset-class comparison of many LLM backbones' decision-making quality in one accessible platform. |
| [**FinAI-Contest**](https://github.com/Open-Finance-Lab/FinAI-Contest) | 8 | Jupyter Notebook | 🟢 | Standardized, competition-driven tasks/baselines that make RL+LLM trading-agent submissions directly comparable year over year. |
| [**FinTral**](https://github.com/UBC-NLP/fintral) | 8 | n/a | 🟠 | One of the few open multimodal (chart/table-aware, not just text) financial LLM benchmarks in this space. |
| [**Agent Market Arena**](https://github.com/The-FinAI/Agent_Market_Arena) | 7 | Python | 🟢 | Ongoing, leakage-resistant, real-time comparison of trading agents/backbone LLMs rather than a one-off historical backtest. |

<details><summary>Explainers (10)</summary>

**[AI-Trader (HKUDS)](https://github.com/HKUDS/AI-Trader)** · Python · ★ 22.4k · last push 2026-06-11  
AI-Trader (paper arXiv:2512.10971, from HKU) is described as the first fully-automated, live, and data-uncontaminated evaluation for LLM financial-decision agents across US stocks, A-shares and crypto at multiple trading frequencies, under a 'minimal information' paradigm where agents must independently search/verify/synthesize live information. Findings: general intelligence doesn't reliably translate to trading skill, and risk control drives cross-market robustness.

✅ *Good at:* Rigorous, contamination-resistant, multi-market live evaluation methodology for autonomous trading agents.  
⚠️ *Limitations:* Same rapid, hype-driven star growth pattern seen across HKUDS's other trading repos (Vibe-Trading) — worth verifying independently rather than trusting star count as a maturity signal.

**[FinNLP](https://github.com/AI4Finance-Foundation/FinNLP)** · Jupyter Notebook · ★ 1.5k · last push 2024-07-01  
AI4Finance's toolkit for democratizing internet-scale financial data collection and NLP preprocessing (news, filings, social sentiment) that feeds into FinGPT/FinRL-style downstream trading and forecasting pipelines.

✅ *Good at:* Financial data-scraping/NLP-preprocessing building blocks reused across the AI4Finance ecosystem.  
⚠️ *Limitations:* Data-source scrapers can break as sites change terms/structure; not updated since mid-2024.

**[PIXIU / FinBen](https://github.com/The-FinAI/PIXIU)** · Jupyter Notebook · ★ 886 · last push 2025-03-04  
PIXIU introduces the first open financial LLMs alongside instruction-tuning data and the FinBen evaluation benchmark suite, aiming to holistically assess financial LLMs; it underlies much of the academic financial-LLM benchmarking landscape (FinMA models, FinBen leaderboard tasks).

✅ *Good at:* Comprehensive, standardized evaluation tasks/datasets for judging any financial LLM's competence, not just trading decisions.  
⚠️ *Limitations:* No commits since March 2025; newer benchmarks (Agent Market Arena, AI-Trader, TraderBench) have since targeted the live/agentic trading gap PIXIU doesn't cover.

**[DeepFund](https://github.com/HKUSTDial/DeepFund)** · Python · ★ 296 · last push 2026-03-18  
DeepFund (NeurIPS 2025, 'Time Travel is Cheating') is a multi-agent live benchmark that trades against real-time, post-training-cutoff market data specifically to prevent LLMs from 'time-traveling' using memorized historical data; testing 9 flagship LLMs (including DeepSeek-V3 and Claude 3.7 Sonnet) showed most incur net trading losses in this leakage-free setting.

✅ *Good at:* Honestly exposing that most current LLMs are not yet good active fund managers, by removing the historical-data leakage that inflates backtested LLM trading results.  
⚠️ *Limitations:* Currently limited universe (a handful of stocks); scaling to hundreds of tickers with realistic frictions is future work per the authors.

**[InvestLM](https://github.com/AbaciNLP/InvestLM)** · Python · ★ 156 · last push 2024-11-12  
InvestLM (LLaMA-65B fine-tuned on a small, carefully curated financial instruction dataset spanning CFA exam questions, SEC filings, and quant-finance StackExchange discussions) was rated by hedge fund managers and analysts as comparable to GPT-3.5/GPT-4/Claude-2 on investment Q&A, demonstrating that small curated datasets can rival large commercial models for financial understanding.

✅ *Good at:* Showing that careful small-scale instruction curation (rather than massive data) can produce a competitive financial-domain LLM.  
⚠️ *Limitations:* A financial-understanding/Q&A model, not a trading-decision agent; not updated since late 2024.

**[Agent Trading Arena](https://github.com/MTMQuantAI/Agent-Trading-Arena)** · Python · ★ 145 · last push 2026-06-09  
Agent Trading Arena (EMNLP 2025) studies numerical understanding in LLM-based agents via a closed-loop, prior-free, human-like trading environment for self-play-capable financial agents; its follow-up 'DecoupledMarket' work was accepted to ICML 2026.

✅ *Good at:* Isolating and testing an LLM agent's raw numerical/quantitative reasoning in a market context, independent of memorized market priors.  
⚠️ *Limitations:* Research-benchmark scope (numerical reasoning), not a full live-trading evaluation like AMA or AI-Trader.

**[INVESTOR-BENCH](https://github.com/felis33/INVESTOR-BENCH)** · Python · ★ 30 · last push 2025-09-13  
INVESTORBENCH (ACL 2025) is the first benchmark specifically for LLM-agent financial decision-making, covering single equities, crypto and ETFs, testing 13 different backbone LLMs across diverse market environments and tasks with curated open multimodal datasets.

✅ *Good at:* Systematic, multi-asset-class comparison of many LLM backbones' decision-making quality in one accessible platform.  
⚠️ *Limitations:* Static/historical benchmark (not live), so susceptible to the same look-ahead-leakage concerns that live arenas like AMA/DeepFund were built to address.

**[FinAI-Contest](https://github.com/Open-Finance-Lab/FinAI-Contest)** · Jupyter Notebook · ★ 8 · last push 2025-12-11  
Hosts the task definitions and baselines (including FinRL-DeepSeek as Task 1) for the annual FinRL/FinAI Contest run by Open Finance Lab, used to benchmark new RL/LLM trading-agent submissions against standardized tasks like crypto trading with LLM-derived signals.

✅ *Good at:* Standardized, competition-driven tasks/baselines that make RL+LLM trading-agent submissions directly comparable year over year.  
⚠️ *Limitations:* Primarily a contest scaffold (docs/baselines) rather than a polished standalone product.

**[FinTral](https://github.com/UBC-NLP/fintral)** · n/a · ★ 8 · last push 2024-06-05  
FinTral (ACL Findings 2024) is a Mistral-7B-based multimodal financial LLM family handling text, numerical, tabular and image data, evaluated on a purpose-built benchmark of 9 tasks/25 datasets; the DPO+tools&retrieval variant reportedly beats GPT-3.5 on all tasks and GPT-4 on 5 of 9.

✅ *Good at:* One of the few open multimodal (chart/table-aware, not just text) financial LLM benchmarks in this space.  
⚠️ *Limitations:* Minimal GitHub activity/adoption (single-digit stars) despite the strong paper results — code/checkpoints availability should be double-checked before relying on it.

**[Agent Market Arena](https://github.com/The-FinAI/Agent_Market_Arena)** · Python · ★ 7 · last push 2026-01-22  
AMA is billed as the first lifelong, real-time benchmark for LLM trading agents across markets, combining a Market Intelligence Stream (verified data + expert-reviewed news summaries), an Agent Execution Protocol running four reference agents (InvestorAgent, TradeAgent, HedgeFundAgent, DeepFundAgent), and a live performance dashboard, evaluated across GPT-4o/4.1, Claude 3.5-haiku/Sonnet-4, and Gemini 2.0-flash.

✅ *Good at:* Ongoing, leakage-resistant, real-time comparison of trading agents/backbone LLMs rather than a one-off historical backtest.  
⚠️ *Limitations:* Very low star count/visibility so far relative to its ambition; live benchmarks like this are inherently harder to reproduce than static ones.

</details>

### Uses Jev (TypeSafe)

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**QuantDinger**](https://github.com/OpenByteInc/QuantDinger) | 11.9k | Python | 🟢 | Using Jev not as the whole decision engine but as a lightweight, auditable sanity-check gate layered on top of an existing strategy/backtesting platform — arguably a more defensible pattern than letting Jev decide trades outright. |
| [**jev-trader (jarrodwatts)**](https://github.com/jarrodwatts/jev-trader) | 1.6k | TypeScript | 🟢 | Demonstrating Jev's core pitch — sub-second, typed, probabilistic decisions — in a genuinely latency-sensitive trading loop (one decision per ~300ms blockchain block). |
| [**awesome-typesafe**](https://github.com/AbdelStark/awesome-typesafe) | 404 | CSS | 🟢 | The best single starting point for tracking the fast-growing Jev/TypeSafe ecosystem, including its finance/trading applications. |
| [**jev-trade (aowang-ai)**](https://github.com/aowang-ai/jev-trade) | 57 | TypeScript | 🟢 | Extending the single-market Jev-trading pattern to a multi-asset, isolated-risk sleeve structure. |
| [**jev_stock**](https://github.com/sosopop/jev_stock) | 11 | Python | 🟢 | Applying Jev's typed-judgment pattern to a non-US, non-crypto market (Hong Kong equities). |
| [**jev-trader (buberlo)**](https://github.com/buberlo/jev-trader) | 1 | Python | 🟢 | A more granular decomposition of a trading decision into several narrow, independently-calibrated Jev judgments rather than one monolithic call. |
| [**jev-crypto-scout**](https://github.com/yasdelayu/jev-crypto-scout) | 0 | Python | 🟢 | Illustrating a lower-risk application pattern: Jev as a news-classification filter feeding a human/other-system decision, rather than an autonomous executor. |
| [**jev-signals-lab**](https://github.com/Gamma-Software/jev-signals-lab) | 0 | HTML | 🟢 | Exploring how many independent, narrow Jev judgments can be combined per snapshot into a richer signal set. |
| [**jev-typesafe-real-financial-use-cases**](https://github.com/IslamBaraka90/jev-typesafe-real-financial-use-cases) | 0 | JavaScript | 🟢 | A broad, graded sanity-check suite for evaluating Jev's reliability across many discrete financial judgment types before trusting it in a live system. |

<details><summary>Explainers (9)</summary>

**[QuantDinger](https://github.com/OpenByteInc/QuantDinger)** · Python · ★ 11.9k · last push 2026-09-20  
QuantDinger is a broader open-source 'AI Trading OS' (crypto/stocks/forex, agent/vibe trading, Python strategy authoring, backtesting, paper/live trading, and a multi-tenant trading-SaaS scaffold with billing) that integrates Jev System One as an optional, auditable PASS/REJECT gate in front of strategy and quick-trade entry orders.

✅ *Good at:* Using Jev not as the whole decision engine but as a lightweight, auditable sanity-check gate layered on top of an existing strategy/backtesting platform — arguably a more defensible pattern than letting Jev decide trades outright.  
⚠️ *Limitations:* Very rapid star growth (nearly 12k stars within days) is a red flag typical of the current wave of hype-driven AI-trading repos; the platform is broad/ambitious (SaaS billing etc.) which increases surface area to evaluate before trusting it.

**[jev-trader (jarrodwatts)](https://github.com/jarrodwatts/jev-trader)** · TypeScript · ★ 1.6k · last push 2026-09-17  
The most-starred and apparently reference implementation of a Jev-powered trading bot: it makes one AI trade decision every Monad blockchain block (~300ms) by having TypeSafe's Jev model read the Kuru MON-USDC order book and answer a simple buy/sell/hold judgment, posting post-only limit orders in Bun/TypeScript with a dry-run mode and an SSE live dashboard. Jev itself is TypeSafe AI's first 'System One' model, launched Sept 15 2026 with $40M led by DCVC and built by Diogo Almeida (co-inventor of RLHF/InstructGPT); it returns typed, calibrated-probability judgments over program state in 70-500ms rather than generating free text, via api.typesafe.ai/v1/systemone and the TYPESAFE_API_KEY env var.

✅ *Good at:* Demonstrating Jev's core pitch — sub-second, typed, probabilistic decisions — in a genuinely latency-sensitive trading loop (one decision per ~300ms blockchain block).  
⚠️ *Limitations:* Days-old project on a niche L1 (Monad) DEX (Kuru); Jev only judges a snapshot order book and cannot itself validate whether the resulting trades are actually profitable long-run.

**[awesome-typesafe](https://github.com/AbdelStark/awesome-typesafe)** · CSS · ★ 404 · last push 2026-09-21  
The main community-curated index of official TypeSafe resources and third-party Jev/'System One model' projects (SDKs, agent tooling, workflows, and application examples including several of the trading repos in this catalog), updated daily as of Sept 2026 given how new the Jev ecosystem is. Related lists exist under similar names (Anil-matcha/awesome-jev-by-typesafe, AnotiaWang/awesome-jev, luantak/awesome-jev-by-typesafe).

✅ *Good at:* The best single starting point for tracking the fast-growing Jev/TypeSafe ecosystem, including its finance/trading applications.  
⚠️ *Limitations:* General-purpose Jev list, not finance-specific, and — like everything Jev-related — only days old with unproven long-term curation quality.

**[jev-trade (aowang-ai)](https://github.com/aowang-ai/jev-trade)** · TypeScript · ★ 57 · last push 2026-09-19  
A Hyperliquid perpetuals-exchange port of the Jev-trader pattern, running five isolated 'sleeves' (BTC/ETH/SOL/DOGE/BNB) each using Jev's typed judgments to decide long/short positioning.

✅ *Good at:* Extending the single-market Jev-trading pattern to a multi-asset, isolated-risk sleeve structure.  
⚠️ *Limitations:* Days old, single contributor, live-money framing (Hyperliquid) with minimal track record.

**[jev_stock](https://github.com/sosopop/jev_stock)** · Python · ★ 11 · last push 2026-09-17  
An experimental framework using Jev to forecast short-term stock price direction for Hong Kong-listed stocks from structured market data pulled via AKShare.

✅ *Good at:* Applying Jev's typed-judgment pattern to a non-US, non-crypto market (Hong Kong equities).  
⚠️ *Limitations:* Explicitly experimental; days old with no track record.

**[jev-trader (buberlo)](https://github.com/buberlo/jev-trader)** · Python · ★ 1 · last push 2026-09-19  
A Python redesign of the Jev-trader concept as a 24/7 market-making system, structuring the decision as six atomic Jev judgments (regime, direction, toxic flow, liquidity stress, quote environment, inventory pressure) with deterministic state and hard risk vetoes rather than one single buy/sell call.

✅ *Good at:* A more granular decomposition of a trading decision into several narrow, independently-calibrated Jev judgments rather than one monolithic call.  
⚠️ *Limitations:* Single-star, days-old, unverified project.

**[jev-crypto-scout](https://github.com/yasdelayu/jev-crypto-scout)** · Python · ★ 0 · last push 2026-09-20  
A crypto screening tool that combines code-computed quant signals (from CoinGecko) with Jev-based news judgment (sentiment/catalyst/confirmed classification) — explicitly described by its author as screening, 'not a trading bot', a more conservative use of Jev than the direct-execution projects above.

✅ *Good at:* Illustrating a lower-risk application pattern: Jev as a news-classification filter feeding a human/other-system decision, rather than an autonomous executor.  
⚠️ *Limitations:* Zero stars, brand new, unproven signal quality.

**[jev-signals-lab](https://github.com/Gamma-Software/jev-signals-lab)** · HTML · ★ 0 · last push 2026-09-19  
A 'paper-only' proof-of-concept researching trading signals derived from 12 independent Jev questions asked per market snapshot — explicitly framed as research, not a live or even backtested trading system.

✅ *Good at:* Exploring how many independent, narrow Jev judgments can be combined per snapshot into a richer signal set.  
⚠️ *Limitations:* Zero stars, explicitly paper/POC-only, no execution or even backtest component per its own description.

**[jev-typesafe-real-financial-use-cases](https://github.com/IslamBaraka90/jev-typesafe-real-financial-use-cases)** · JavaScript · ★ 0 · last push 2026-09-20  
Fifty worked financial use cases for Jev (ledgers, fraud detection, wallets, portfolios, trades, filings, strategies) where each demo is graded against data with a known correct answer, functioning as an informal accuracy benchmark for Jev's typed judgments on finance-adjacent tasks rather than a trading system itself.

✅ *Good at:* A broad, graded sanity-check suite for evaluating Jev's reliability across many discrete financial judgment types before trusting it in a live system.  
⚠️ *Limitations:* Self-graded demo repo, not an independently peer-reviewed benchmark; zero stars and days old.

</details>

### Lists & other

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**awesome-ai-in-finance**](https://github.com/georgezouq/awesome-ai-in-finance) | 6.6k | n/a | 🟢 | Broad, long-standing, well-organized index of the ML/AI-in-finance ecosystem (not LLM-agent specific like LLMQuant's list). |
| [**awesome-trading-agents (LLMQuant)**](https://github.com/LLMQuant/awesome-trading-agents) | 829 | n/a | 🟢 | Fast discovery of new LLM-trading-agent and trading-MCP-server projects as they appear. |
| [**Awesome-LLM-Quantitative-Trading-Papers**](https://github.com/Tom-roujiang/Awesome-LLM-Quantitative-Trading-Papers) | 246 | n/a | 🟢 | Tracking the academic paper trail behind this fast-moving research area. |
| [**Awesome-MFFMs**](https://github.com/Open-Finance-Lab/Awesome-MFFMs) | 47 | n/a | 🟢 | Focused index of the narrower multimodal-financial-foundation-model niche within the broader financial-LLM landscape. |

<details><summary>Explainers (4)</summary>

**[awesome-ai-in-finance](https://github.com/georgezouq/awesome-ai-in-finance)** · n/a · ★ 6.6k · last push 2026-09-08  
One of the longest-running and most-starred curated lists of LLMs, deep-learning strategies and tools for financial markets, covering data, ML/RL trading, papers and companies.

✅ *Good at:* Broad, long-standing, well-organized index of the ML/AI-in-finance ecosystem (not LLM-agent specific like LLMQuant's list).  
⚠️ *Limitations:* General AI-in-finance scope, so it's less focused specifically on the agentic/LLM-trading niche this catalog targets.

**[awesome-trading-agents (LLMQuant)](https://github.com/LLMQuant/awesome-trading-agents)** · n/a · ★ 829 · last push 2026-08-13  
A curated, actively updated list of LLM-driven trading agents, MCP servers, and agent skills for market research, strategy and execution — a good discovery entry point for this entire space.

✅ *Good at:* Fast discovery of new LLM-trading-agent and trading-MCP-server projects as they appear.  
⚠️ *Limitations:* A links list, not software; inclusion in the list does not itself imply quality/reliability.

**[Awesome-LLM-Quantitative-Trading-Papers](https://github.com/Tom-roujiang/Awesome-LLM-Quantitative-Trading-Papers)** · n/a · ★ 246 · last push 2026-07-24  
A curated collection specifically of research papers (with links to available code/benchmarks) on LLM-based quantitative trading and investment research — useful for tracing which of the papers referenced elsewhere in this catalog (FinAgent, FinCon, AlphaAgents, etc.) actually have released code.

✅ *Good at:* Tracking the academic paper trail behind this fast-moving research area.  
⚠️ *Limitations:* Papers-focused; many linked papers still lack public code (as seen with FinAgent/FinCon in this catalog).

**[Awesome-MFFMs](https://github.com/Open-Finance-Lab/Awesome-MFFMs)** · n/a · ★ 47 · last push 2026-03-06  
A curated tracking list specifically for Multimodal Financial Foundation Models (MFFMs) — chart/table/text-aware financial foundation models like FinTral — companion to the 'Multimodal Financial Foundation Models: Progress, Prospects, and Challenges' survey (arXiv:2506.01973).

✅ *Good at:* Focused index of the narrower multimodal-financial-foundation-model niche within the broader financial-LLM landscape.  
⚠️ *Limitations:* Small, low-star tracking list; the field it surveys is itself nascent with few production-ready models.

</details>

[⬆ back to top](#contents)

## Fundamentals, market data & alternative data

SEC filings, valuation, transcripts, ownership, market-data SDKs, tick storage, news sentiment and alt-data.
**OpenBB Platform** is the dominant open research hub, **edgartools** is best-in-class for SEC/XBRL, and
**ArcticDB / QuestDB / TimescaleDB** are the credible open time-series stores.

**Key takeaways**

- Polygon.io is now **Massive** (`massive-com/client-python`). IEX Cloud shut down in 2024.
- **FinBERT** is still the default financial-sentiment baseline.
- Gaps: no open source for earnings-call transcripts (they are paywalled), and satellite or other exotic alt-data is almost entirely proprietary.

### SEC filings & XBRL

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**edgartools**](https://github.com/dgunning/edgartools) | 2.7k | Python | 🟢 | Turning arbitrary company filings and XBRL facts into clean pandas DataFrames with almost no boilerplate; ideal foundation for automated fundamental-data pipelines and Form 4/13F ownership tracking. |
| [**sec-edgar-downloader**](https://github.com/jadchaar/sec-edgar-downloader) | 716 | Python | 🟢 | Simple, reliable bulk retrieval of raw filing documents for later parsing or archival. |
| [**python-edgar**](https://github.com/edgarminers/python-edgar) | 355 | Python | 🟠 | Building a comprehensive local index of historical filings quickly. |
| [**pysec**](https://github.com/lukerosiak/pysec) | 346 | Python | 🟠 | Historical reference implementation for XBRL-to-SQL extraction patterns. |
| [**sec-api-python**](https://github.com/janlukasschroeder/sec-api-python) | 320 | Python | 🟢 | One API for many filing types (including full-text search across all EDGAR filings), useful when you don't want to build your own scraping/parsing pipeline. |
| [**Arelle**](https://github.com/Arelle/Arelle) | 241 | Python | 🟢 | Rigorous, spec-compliant XBRL/iXBRL parsing and validation, including custom taxonomy extensions used by non-US filers. |
| [**python-xbrl**](https://github.com/greedo/python-xbrl) | 234 | Python | 🟢 | Simple, dependency-light XBRL parsing when Arelle is too heavy. |
| [**py-xbrl**](https://github.com/manusimidt/py-xbrl) | 152 | Python | 🟢 | Parsing Inline XBRL (the format SEC now requires for most filings) directly, which many older libraries do not handle well. |
| [**python-for-dera-financial-datasets**](https://github.com/sec-gov/python-for-dera-financial-datasets) | 106 | Python | 🟢 | Ground-truth reference for correctly interpreting SEC's own bulk data set schema. |
| [**secfsdstools**](https://github.com/HansjoergW/sec-fincancial-statement-data-set) | 84 | Python | 🟢 | Cross-sectional analysis across thousands of companies at once using SEC's own pre-aggregated bulk datasets, avoiding per-filing scraping entirely. |
| [**sec-downloader**](https://github.com/Elijas/sec-downloader) | 60 | Python | 🟢 | Fine-grained control over which documents within a filing package get downloaded, saving bandwidth/storage. |
| [**sec-edgar-toolkit**](https://github.com/stefanoamorelli/sec-edgar-toolkit) | 38 | Python | 🟢 | Cross-language (Python + TS) access to the same EDGAR/XBRL data model for full-stack apps. |
| [**py-sec-xbrl**](https://github.com/zhaolewen/py-sec-xbrl) | 25 | Python | 🟠 | Alternative parsing strategy worth checking when other libraries choke on a particular filer's taxonomy. |
| [**sec-data**](https://github.com/baimmm6767/sec-data) | 2 | Python | 🟢 | Producing analyst-ready Excel financial statements directly from raw XBRL, including the tricky Q4-by-subtraction calculation. |

<details><summary>Explainers (14)</summary>

**[edgartools](https://github.com/dgunning/edgartools)** · Python · ★ 2.7k · last push 2026-09-21  
edgartools is the most actively developed Python library for reading SEC EDGAR filings as structured Python objects rather than raw HTML/XML. It parses 10-K, 10-Q, 8-K, Forms 3/4/5, 13F, and investment-adviser (ADV) filings, standardizes XBRL financial statements into DataFrames, and includes a built-in MCP server so LLM agents can query filings directly. No API key or rate limit is required beyond SEC's own fair-use policy.

✅ *Good at:* Turning arbitrary company filings and XBRL facts into clean pandas DataFrames with almost no boilerplate; ideal foundation for automated fundamental-data pipelines and Form 4/13F ownership tracking.  
⚠️ *Limitations:* Relies entirely on SEC's own data quality/tagging consistency, so pre-XBRL (pre-2009) filings and non-standard taxonomies are harder to normalize.

**[sec-edgar-downloader](https://github.com/jadchaar/sec-edgar-downloader)** · Python · ★ 716 · last push 2026-06-22  
sec-edgar-downloader is a focused, widely-used utility for bulk-downloading raw SEC filings (10-K, 10-Q, 8-K, and dozens of other form types) by ticker or CIK, handling EDGAR's pagination and rate limits. It is a common building block that other tools (e.g., Elijas/sec-downloader) wrap for more advanced filtering.

✅ *Good at:* Simple, reliable bulk retrieval of raw filing documents for later parsing or archival.  
⚠️ *Limitations:* Only downloads documents; does no XBRL/financial-statement extraction itself.

**[python-edgar](https://github.com/edgarminers/python-edgar)** · Python · ★ 355 · last push 2024-05-11  
Downloads the full SEC EDGAR filings index going back to 1993, letting users build a local catalog of every filing by company/date/form-type without scraping the live site. Useful as a foundation layer before fetching individual documents.

✅ *Good at:* Building a comprehensive local index of historical filings quickly.  
⚠️ *Limitations:* Only fetches the index, not filing content; last updated 2024 with no recent activity.

**[pysec](https://github.com/lukerosiak/pysec)** · Python · ★ 346 · last push 2014-01-22  
One of the earliest popular Python SEC/XBRL parsers, compiling EDGAR filings into a SQL database and extracting ~50 key accounting terms. Historically influential but effectively abandoned since 2014.

✅ *Good at:* Historical reference implementation for XBRL-to-SQL extraction patterns.  
⚠️ *Limitations:* Unmaintained for over a decade; will break on modern filing formats and taxonomies.

**[sec-api-python](https://github.com/janlukasschroeder/sec-api-python)** · Python · ★ 320 · last push 2026-04-13  
Official Python SDK for the commercial sec-api.io service, giving access to 20M+ filings, insider trades, 13F holdings, financial statements, executive comp, enforcement actions, XBRL-to-JSON conversion, and real-time filing streaming through a single hosted API. The SDK itself is open source even though the backend requires a paid API key beyond a free tier.

✅ *Good at:* One API for many filing types (including full-text search across all EDGAR filings), useful when you don't want to build your own scraping/parsing pipeline.  
⚠️ *Limitations:* Free tier is limited; heavy usage requires a paid subscription, unlike edgartools or sec-edgar-downloader which are fully free against SEC's own servers.

**[Arelle](https://github.com/Arelle/Arelle)** · Python · ★ 241 · last push 2026-09-20  
Arelle is a full end-to-end open-source XBRL platform certified by XBRL International as a validating processor, available as a desktop GUI, CLI, Python API, and web service. It underpins much of the SEC's own XBRL validation tooling and can render Inline XBRL filings, validate taxonomies, and run custom Formula/XULE business rules. Many downstream SEC-data tools use Arelle as their parsing engine.

✅ *Good at:* Rigorous, spec-compliant XBRL/iXBRL parsing and validation, including custom taxonomy extensions used by non-US filers.  
⚠️ *Limitations:* Steep learning curve and heavier setup than lightweight wrapper libraries; overkill for simple 'get me revenue by quarter' use cases.

**[python-xbrl](https://github.com/greedo/python-xbrl)** · Python · ★ 234 · last push 2026-04-21  
A lightweight, general-purpose XBRL instance-document parser for Python, usable beyond just SEC filings. Still receives occasional updates, making it one of the more durable lightweight XBRL parsing options.

✅ *Good at:* Simple, dependency-light XBRL parsing when Arelle is too heavy.  
⚠️ *Limitations:* Less actively developed than edgartools; lacks SEC-specific conveniences like ticker/CIK lookup or filing search.

**[py-xbrl](https://github.com/manusimidt/py-xbrl)** · Python · ★ 152 · last push 2026-09-13  
A actively-maintained Python parser for both XBRL and Inline XBRL (iXBRL) documents, built primarily around SEC instance documents but usable for any XBRL 2.1/iXBRL 1.1-compliant filing worldwide (e.g., European ESEF filings).

✅ *Good at:* Parsing Inline XBRL (the format SEC now requires for most filings) directly, which many older libraries do not handle well.  
⚠️ *Limitations:* GPL-3.0 license is copyleft, which can complicate use inside proprietary commercial products.

**[python-for-dera-financial-datasets](https://github.com/sec-gov/python-for-dera-financial-datasets)** · Python · ★ 106 · last push 2026-01-21  
Official example code published by the SEC itself (sec-gov org) demonstrating how to load and analyze the DERA Financial Statement and Notes Data Sets with pandas. Serves as the canonical reference implementation that community tools like secfsdstools build on.

✅ *Good at:* Ground-truth reference for correctly interpreting SEC's own bulk data set schema.  
⚠️ *Limitations:* Educational example scripts, not a packaged/maintained library — needs to be adapted for production use.

**[secfsdstools](https://github.com/HansjoergW/sec-fincancial-statement-data-set)** · Python · ★ 84 · last push 2025-09-20  
secfsdstools works directly against the SEC's quarterly 'Financial Statement Data Sets' bulk downloads (not the per-filing XBRL API), providing standardizers that map raw tags into consistent balance-sheet, income-statement, and cash-flow-statement structures across companies. It supports daily incremental updates as of v2.4+.

✅ *Good at:* Cross-sectional analysis across thousands of companies at once using SEC's own pre-aggregated bulk datasets, avoiding per-filing scraping entirely.  
⚠️ *Limitations:* Smaller community; standardization logic needs periodic maintenance as SEC taxonomies evolve.

**[sec-downloader](https://github.com/Elijas/sec-downloader)** · Python · ★ 60 · last push 2025-10-24  
Built on top of sec-edgar-downloader, adding a more ergonomic search-and-glob-pattern interface for finding and downloading specific filing documents (e.g., only the primary 10-K document, not exhibits).

✅ *Good at:* Fine-grained control over which documents within a filing package get downloaded, saving bandwidth/storage.  
⚠️ *Limitations:* Thin wrapper — inherits any limitations of the underlying sec-edgar-downloader.

**[sec-edgar-toolkit](https://github.com/stefanoamorelli/sec-edgar-toolkit)** · Python · ★ 38 · last push 2026-08-18  
A newer, actively updated toolkit offering both Python and TypeScript/JavaScript SDKs for SEC EDGAR data, with comprehensive parsing for 10-K/10-Q/8-K forms, XBRL extraction, and real-time filing retrieval. Targets developers who need the same data model available in both a Python backend and a JS/TS frontend or Node service.

✅ *Good at:* Cross-language (Python + TS) access to the same EDGAR/XBRL data model for full-stack apps.  
⚠️ *Limitations:* Small community and star count so far; AGPL license is more restrictive for commercial redistribution than MIT alternatives.

**[py-sec-xbrl](https://github.com/zhaolewen/py-sec-xbrl)** · Python · ★ 25 · last push 2020-05-22  
A Python 3 SEC EDGAR/XBRL parser focused on making raw XBRL XML more accessible for analysis, similar in scope to python-xbrl but with a different tag-extraction approach.

✅ *Good at:* Alternative parsing strategy worth checking when other libraries choke on a particular filer's taxonomy.  
⚠️ *Limitations:* Unmaintained since 2020.

**[sec-data](https://github.com/baimmm6767/sec-data)** · Python · ★ 2 · last push 2026-09-12  
A newer (2026) open-source engine that converts SEC quarterly filings into modeling-ready CSV/Excel financials, including segment-level data, filing-aware XBRL tag mapping, automated accounting repairs, and Q4-derivation (since companies don't file a standalone Q4 10-Q).

✅ *Good at:* Producing analyst-ready Excel financial statements directly from raw XBRL, including the tricky Q4-by-subtraction calculation.  
⚠️ *Limitations:* Very new project with minimal community adoption/testing so far.

</details>

### Valuation

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**Business Valuation with DCF in Python**](https://github.com/farbodbahari/Business-Valuation-with-Discounted-Cash-Flow-In-Python) | 176 | Jupyter Notebook | 🟠 | Clear, well-commented reference implementation of the classic Damodaran DCF approach for learning or adapting. |
| [**DCF Valuation Model (Monte Carlo)**](https://github.com/EmanueleSturzo/DCF-Valuation-Model) | 3 | Python | 🟢 | Producing a valuation range/distribution rather than one number, useful for risk-aware fundamental analysis. |
| [**dcfBuilder**](https://github.com/mgayatri77/dcfBuilder) | 1 | Python | 🟠 | Quickly generating an editable, Excel-native DCF scaffold from live SEC data instead of building one from scratch. |
| [**DCF Dashboard**](https://github.com/nostreet123/DCF-Dashboard) | 1 | TypeScript | 🟢 | Giving non-Excel users (or teams wanting shareable links) a browser-based DCF workflow with saved-run history. |
| [**aswath (DCF models)**](https://github.com/SimeonChan/aswath) | 0 | Python | 🟠 | Illustrating how Damodaran's spreadsheet logic translates into Python data structures. |

<details><summary>Explainers (5)</summary>

**[Business Valuation with DCF in Python](https://github.com/farbodbahari/Business-Valuation-with-Discounted-Cash-Flow-In-Python)** · Jupyter Notebook · ★ 176 · last push 2024-12-24  
A well-regarded educational notebook implementing stock and asset valuation via discounted cash flow, explicitly following Aswath Damodaran's NYU valuation methodology (WACC, terminal value, sensitivity tables).

✅ *Good at:* Clear, well-commented reference implementation of the classic Damodaran DCF approach for learning or adapting.  
⚠️ *Limitations:* Static notebook, not a live-data-connected tool; financial inputs must be entered manually.

**[DCF Valuation Model (Monte Carlo)](https://github.com/EmanueleSturzo/DCF-Valuation-Model)** · Python · ★ 3 · last push 2026-04-08  
A 5-year DCF valuation model in Python that goes beyond a single-point estimate, adding Monte Carlo simulation, sensitivity/scenario analysis, comparable-company analysis, and exit-multiple valuation in one workbook-style tool.

✅ *Good at:* Producing a valuation range/distribution rather than one number, useful for risk-aware fundamental analysis.  
⚠️ *Limitations:* Small, newer project without a large user base to validate edge cases.

**[dcfBuilder](https://github.com/mgayatri77/dcfBuilder)** · Python · ★ 1 · last push 2022-09-21  
Given a NYSE/NASDAQ ticker, dcfBuilder pulls historical financials via SEC's EDGAR API and auto-populates a Damodaran-style DCF model into an Excel workbook, replicating the structure of Aswath Damodaran's publicly-shared valuation spreadsheets.

✅ *Good at:* Quickly generating an editable, Excel-native DCF scaffold from live SEC data instead of building one from scratch.  
⚠️ *Limitations:* Unmaintained since 2022; a single-contributor student-style project without ongoing support.

**[DCF Dashboard](https://github.com/nostreet123/DCF-Dashboard)** · TypeScript · ★ 1 · last push 2026-09-18  
An open-source DCF valuation workbench pairing a Next.js browser UI with a Python compute engine, turning spreadsheet-style DCF work into a reproducible web workflow with scenario comparison and optional Monte Carlo ranges.

✅ *Good at:* Giving non-Excel users (or teams wanting shareable links) a browser-based DCF workflow with saved-run history.  
⚠️ *Limitations:* Very new/low adoption; full-stack (Next.js + Python) setup is heavier than a single script or notebook.

**[aswath (DCF models)](https://github.com/SimeonChan/aswath)** · Python · ★ 0 · last push 2015-04-23  
An early Python3 attempt to reimplement Aswath Damodaran's public DCF valuation spreadsheets as code, named directly after him. Historically notable as one of the first such ports.

✅ *Good at:* Illustrating how Damodaran's spreadsheet logic translates into Python data structures.  
⚠️ *Limitations:* Essentially abandoned since 2015; no stars/community.

</details>

### Earnings transcripts

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**Earnings-Calls-NLP**](https://github.com/cdubiel08/Earnings-Calls-NLP) | 76 | Jupyter Notebook | 🟠 | Demonstrating an end-to-end pipeline from raw transcript text to a discrete trading signal. |
| [**Stock Earnings Call Transcript NLP**](https://github.com/personal-coding/Stock-Earnings-Call-Transcript-Natural-Language-Processing) | 14 | Python | 🟠 | Tying transcript NLP features directly to a documented, published research methodology with a backtest. |
| [**Earnings Call NLP Strategy V2**](https://github.com/Vxtr10/Earnings-Call-NLP-Strategy-V2) | 2 | Jupyter Notebook | 🟠 | Broad feature-engineering menu (FinBERT + complexity + similarity) for anyone building their own transcript-alpha model. |
| [**Earnings Call NLP Lab**](https://github.com/Cubiczan/earnings-call-nlp-lab) | 0 | Python | 🟢 | Longitudinal tone/evasiveness tracking per company across many quarters, not just single-transcript sentiment scoring. |

<details><summary>Explainers (4)</summary>

**[Earnings-Calls-NLP](https://github.com/cdubiel08/Earnings-Calls-NLP)** · Jupyter Notebook · ★ 76 · last push 2023-05-09  
Applies NLP and logistic regression to earnings call transcripts to generate buy/sell/hold classifications, one of the more-starred educational examples of transcript-driven trading signal research.

✅ *Good at:* Demonstrating an end-to-end pipeline from raw transcript text to a discrete trading signal.  
⚠️ *Limitations:* Research/educational scope only; not production-hardened or continuously updated with new transcripts.

**[Stock Earnings Call Transcript NLP](https://github.com/personal-coding/Stock-Earnings-Call-Transcript-Natural-Language-Processing)** · Python · ★ 14 · last push 2023-08-30  
Implements and backtests an investment strategy based on NLP analysis of earnings call transcripts, explicitly modeled on published S&P Global research papers on transcript-based signals.

✅ *Good at:* Tying transcript NLP features directly to a documented, published research methodology with a backtest.  
⚠️ *Limitations:* Single-author research project without ongoing maintenance.

**[Earnings Call NLP Strategy V2](https://github.com/Vxtr10/Earnings-Call-NLP-Strategy-V2)** · Jupyter Notebook · ★ 2 · last push 2023-11-19  
Expands earnings-call transcript prediction across multiple industries using FinBERT sentiment, text-complexity metrics, keyword filtering, and TF-IDF/cosine-similarity features to predict post-earnings stock moves.

✅ *Good at:* Broad feature-engineering menu (FinBERT + complexity + similarity) for anyone building their own transcript-alpha model.  
⚠️ *Limitations:* Research notebook, not a packaged/reusable library; unmaintained since 2023.

**[Earnings Call NLP Lab](https://github.com/Cubiczan/earnings-call-nlp-lab)** · Python · ★ 0 · last push 2026-09-21  
A lightweight, auditable app analyzing earnings call transcripts for sentiment, management tone, confidence, and evasiveness, with longitudinal tracking of the same company's tone across multiple quarters.

✅ *Good at:* Longitudinal tone/evasiveness tracking per company across many quarters, not just single-transcript sentiment scoring.  
⚠️ *Limitations:* Brand-new project (actively pushed as of this week) with no track record yet.

</details>

### Ownership & insider

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**Senate Stock Watcher (data)**](https://github.com/timothycarambat/senate-stock-watcher-data) | 100 | Python | 🟠 | Free, structured historical dataset of Senate trades that many downstream projects (e.g., congress_stock_trading) build on. |
| [**openinsiderData**](https://github.com/sd3v/openinsiderData) | 84 | Python | 🟢 | Getting OpenInsider's pre-cleaned, pre-aggregated insider-transaction database in bulk for offline analysis. |
| [**congress_stock_trading**](https://github.com/burd5/congress_stock_trading) | 32 | Python | 🟠 | Turning raw disclosure data into visual member-level performance comparisons. |
| [**insider-trading-analyzer**](https://github.com/wescules/insider-trading-analyzer) | 8 | Python | 🟢 | Filtering the huge volume of routine insider filings down to a smaller high-signal subset before backtesting. |
| [**WhalePortfolioAnalyzer**](https://github.com/J700070/WhalePortfolioAnalyzer) | 3 | Python | 🟠 | Quick, low-effort access to curated 13F summaries via the Dataroma aggregator instead of raw EDGAR parsing. |
| [**InsiderTrack**](https://github.com/mrgutierrezmario/insidertrack) | 1 | Python | 🟢 | A ready-to-self-host web app (not just a script) covering all three ownership-disclosure sources in one UI. |
| [**insider-tracker (aroo-stack)**](https://github.com/aroo-stack/insider-tracker) | 0 | HTML | 🟢 | Combining insider (Form 4) and institutional (13F) signals into one cluster-detection and backtest workflow. |
| [**investor-tracker**](https://github.com/roreyshen/investor-tracker) | 0 | Python | 🟢 | Zero-infrastructure-cost deployment (GitHub Actions only) for real-time insider + congressional trade alerts. |
| [**13f-dashboard**](https://github.com/zhuy9/13f-dashboard) | 0 | TypeScript | 🟢 | Aggregating signal across many 13F filers simultaneously (e.g., 'how many top funds bought X this quarter') rather than viewing one fund at a time. |
| [**whale-watch**](https://github.com/won-topiaa/whale-watch) | 0 | HTML | 🟢 | Zero-cost, always-current mirror of a small set of closely-watched investor portfolios without needing a paid WhaleWisdom subscription. |
| [**insider-scanner**](https://github.com/Czarnak/insider-scanner) | 0 | Python | 🟢 | Cross-checking insider trade data across two independent free sources instead of relying on a single aggregator. |

<details><summary>Explainers (11)</summary>

**[Senate Stock Watcher (data)](https://github.com/timothycarambat/senate-stock-watcher-data)** · Python · ★ 100 · last push 2021-03-16  
The open data repository behind senatestockwatcher.com, publishing JSON files scraped from the Senate's eFD (electronic Financial Disclosure) system covering every reported senator stock trade. Widely used as a free upstream data source by other congressional-trading trackers.

✅ *Good at:* Free, structured historical dataset of Senate trades that many downstream projects (e.g., congress_stock_trading) build on.  
⚠️ *Limitations:* Data pipeline hasn't been actively updated since 2021; House disclosures are not covered (Senate only).

**[openinsiderData](https://github.com/sd3v/openinsiderData)** · Python · ★ 84 · last push 2026-08-30  
A Python scraper for OpenInsider.com, the popular free aggregator of SEC Form 4 insider-trading filings, letting users pull its full underlying database rather than browsing the website manually.

✅ *Good at:* Getting OpenInsider's pre-cleaned, pre-aggregated insider-transaction database in bulk for offline analysis.  
⚠️ *Limitations:* Depends on OpenInsider's site structure remaining stable; no official license specified.

**[congress_stock_trading](https://github.com/burd5/congress_stock_trading)** · Python · ★ 32 · last push 2025-07-28  
Visualizes congressional stock trades (combining Senate and House stock-watcher style data) with performance-return metrics and member-by-member breakdowns.

✅ *Good at:* Turning raw disclosure data into visual member-level performance comparisons.  
⚠️ *Limitations:* No license specified; last updated mid-2025 with unclear ongoing maintenance.

**[insider-trading-analyzer](https://github.com/wescules/insider-trading-analyzer)** · Python · ★ 8 · last push 2025-06-02  
Downloads Form 4 (insider transactions) and Form 144 (proposed sale of restricted securities) SEC filings, filters for statistically high-signal trades, cross-references broader market signals, and supports backtesting the resulting strategy.

✅ *Good at:* Filtering the huge volume of routine insider filings down to a smaller high-signal subset before backtesting.  
⚠️ *Limitations:* Moderate adoption (single digit stars); backtest methodology should be independently validated before live use.

**[WhalePortfolioAnalyzer](https://github.com/J700070/WhalePortfolioAnalyzer)** · Python · ★ 3 · last push 2021-11-13  
Analyzes large fund portfolios based on 13F filings extracted from Dataroma (rather than parsing EDGAR directly), surfacing latest buys and top holdings per manager.

✅ *Good at:* Quick, low-effort access to curated 13F summaries via the Dataroma aggregator instead of raw EDGAR parsing.  
⚠️ *Limitations:* Depends on Dataroma's site structure remaining stable; unmaintained since 2021.

**[InsiderTrack](https://github.com/mrgutierrezmario/insidertrack)** · Python · ★ 1 · last push 2026-09-21  
A full-stack (FastAPI + React + PostgreSQL) application tracking congressional trades, corporate-insider Form 4 filings, and 13F whale trades from official sources, scoring each trade per ticker and checking outcomes against subsequent market moves.

✅ *Good at:* A ready-to-self-host web app (not just a script) covering all three ownership-disclosure sources in one UI.  
⚠️ *Limitations:* Requires running a multi-service stack (FastAPI/React/Postgres/Docker) rather than a simple pip-installable library.

**[insider-tracker (aroo-stack)](https://github.com/aroo-stack/insider-tracker)** · HTML · ★ 0 · last push 2026-09-17  
Pulls SEC EDGAR Form 4 insider transactions and 13F institutional-holdings filings directly, then detects cluster buy/sell signals and C-suite open-market buying, backtesting the resulting signals against historical price overlays.

✅ *Good at:* Combining insider (Form 4) and institutional (13F) signals into one cluster-detection and backtest workflow.  
⚠️ *Limitations:* Very new, no license specified, and no stars yet to gauge real-world reliability.

**[investor-tracker](https://github.com/roreyshen/investor-tracker)** · Python · ★ 0 · last push 2026-09-21  
Tracks SEC Form 4 insider trades and congressional STOCK Act disclosures together, sending Discord/SMS alerts, and is designed to run entirely free on GitHub Actions with no server required.

✅ *Good at:* Zero-infrastructure-cost deployment (GitHub Actions only) for real-time insider + congressional trade alerts.  
⚠️ *Limitations:* Alerting-focused rather than analytical; brand-new with no community track record.

**[13f-dashboard](https://github.com/zhuy9/13f-dashboard)** · TypeScript · ★ 0 · last push 2026-09-16  
A 13F institutional-holdings tracker that fetches SEC EDGAR filings, maps CUSIPs to tickers, and derives cross-manager consensus signals (not just per-fund holdings), storing results in Google Cloud Storage/Firestore via automated GitHub Actions pipelines.

✅ *Good at:* Aggregating signal across many 13F filers simultaneously (e.g., 'how many top funds bought X this quarter') rather than viewing one fund at a time.  
⚠️ *Limitations:* Tied to Google Cloud (Firestore/GCS) for storage, adding external infra dependency; brand-new project.

**[whale-watch](https://github.com/won-topiaa/whale-watch)** · HTML · ★ 0 · last push 2026-09-20  
A static, WhaleWisdom/Dataroma-style site tracking the 13F portfolios of ten well-known 'super investors,' automatically pulling fresh 13F data from SEC EDGAR via Python scripts on a daily GitHub Actions schedule.

✅ *Good at:* Zero-cost, always-current mirror of a small set of closely-watched investor portfolios without needing a paid WhaleWisdom subscription.  
⚠️ *Limitations:* Fixed to a curated list of ~10 investors rather than the full universe of 13F filers.

**[insider-scanner](https://github.com/Czarnak/insider-scanner)** · Python · ★ 0 · last push 2026-09-18  
A free insider-trading tracker that can run scrapers against both secform4.com and openinsider.com, giving redundancy across two independent free insider-data aggregators.

✅ *Good at:* Cross-checking insider trade data across two independent free sources instead of relying on a single aggregator.  
⚠️ *Limitations:* Very new project with no community track record yet.

</details>

### Market-data SDKs

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**yfinance**](https://github.com/ranaroussi/yfinance) | 25.3k | Python | 🟢 | Zero-cost, zero-signup historical price and basic fundamentals data for prototyping, research, and education. |
| [**alpha_vantage (python wrapper)**](https://github.com/RomelTorres/alpha_vantage) | 4.9k | Python | 🟢 | Easy access to a genuinely free-tier fundamentals + technicals API without needing a broker account. |
| [**pandas-datareader**](https://github.com/pydata/pandas-datareader) | 3.3k | Python | 🟢 | Quick, dependency-light access to macro/economic series (especially FRED) alongside basic price history. |
| [**findatapy**](https://github.com/cuemacro/findatapy) | 2.1k | Python | 🟢 | Swapping data vendors without rewriting analysis code, especially useful for teams with access to enterprise sources like Bloomberg alongside free ones. |
| [**Massive (Polygon.io) Python client**](https://github.com/massive-com/client-python) | 1.5k | Python | 🟢 | Institutional-grade tick and aggregate market data with low-latency websocket streaming and async REST support. |
| [**yahooquery**](https://github.com/dpguthrie/yahooquery) | 920 | Python | 🟢 | Bulk/async retrieval across many tickers at once and access to some Yahoo endpoints (e.g., fund/ETF holdings, screener) yfinance doesn't expose. |
| [**twelvedata-python**](https://github.com/twelvedata/twelvedata-python) | 782 | Python | 🟢 | Stable, officially-supported REST+WebSocket data as a drop-in replacement when yfinance breaks. |
| [**Nasdaq Data Link Python client**](https://github.com/Nasdaq/data-link-python) | 625 | Python | 🟢 | One client covering a huge marketplace of niche/alternative datasets (many still free) beyond plain-vanilla price data. |
| [**tiingo-python**](https://github.com/hydrosquall/tiingo-python) | 319 | Python | 🟢 | Reliable EOD price history and a built-in news feed in one client, at a low-cost tier compared to enterprise vendors. |
| [**databento-python**](https://github.com/databento/databento-python) | 302 | Python | 🟢 | High-fidelity tick/order-book historical data with usage-based pricing, appealing to quants who don't want a fixed enterprise contract. |
| [**EODHD APIs Python Financial Library**](https://github.com/EodHistoricalData/EODHD-APIs-Python-Financial-Library) | 92 | Python | 🟢 | Broad global-exchange fundamentals coverage (not just US equities) at relatively affordable pricing. |
| [**pyEX**](https://github.com/iexcloud/pyEX) | 48 | Python | 🟠 | Historically strong, well-documented client covering equities, options, and economic data in one package. |
| [**QuantRocket client**](https://github.com/quantrocket-llc/quantrocket-client) | 32 | Python | 🟢 | Unifying fundamentals (via Sharadar) with price data and backtesting in a single self-hosted platform. |
| [**fmp-data**](https://github.com/MehdiZare/fmp-data) | 30 | Python | 🟢 | One of the most complete and current FMP wrappers, with fundamentals as a first-class module rather than an afterthought. |
| [**py-fmpapi**](https://github.com/tidy-finance/py-fmpapi) | 5 | Python | 🟢 | Polars-native (rather than pandas) financial data workflows, useful for performance-sensitive fundamentals pipelines. |
| [**fmp-wrapper**](https://github.com/cccdenhart/fmp-wrapper) | 0 | Python | 🟠 | Minimal, easy-to-read reference implementation if you want to write your own FMP client from scratch. |

<details><summary>Explainers (16)</summary>

**[yfinance](https://github.com/ranaroussi/yfinance)** · Python · ★ 25.3k · last push 2026-09-17  
The single most popular free Python market-data library, scraping/downloading Yahoo Finance's price history, fundamentals, dividends, splits, options chains, and financial statements for any ticker with no API key. It has survived multiple Yahoo backend redesigns (most notably the disruptive Feb 2025 change) thanks to an active maintenance community.

✅ *Good at:* Zero-cost, zero-signup historical price and basic fundamentals data for prototyping, research, and education.  
⚠️ *Limitations:* Unofficial/scraping-based — breaks whenever Yahoo changes its backend, and is unsuitable for production systems needing guaranteed uptime or terms-of-service-compliant redistribution.

**[alpha_vantage (python wrapper)](https://github.com/RomelTorres/alpha_vantage)** · Python · ★ 4.9k · last push 2026-07-26  
The de facto standard Python wrapper for the free/freemium Alpha Vantage API, covering equities, forex, crypto, technical indicators, and fundamental data (earnings, income statement, balance sheet) with a simple pandas-friendly interface.

✅ *Good at:* Easy access to a genuinely free-tier fundamentals + technicals API without needing a broker account.  
⚠️ *Limitations:* Alpha Vantage's free tier has strict rate limits (historically 25 requests/day for fundamentals-heavy use), which the wrapper does not remove.

**[pandas-datareader](https://github.com/pydata/pandas-datareader)** · Python · ★ 3.3k · last push 2026-07-21  
A long-standing PyData-ecosystem library that extracts data from a wide range of internet sources (FRED, World Bank, Stooq, Nasdaq Data Link, and formerly Yahoo/Google Finance) directly into pandas DataFrames with one consistent API.

✅ *Good at:* Quick, dependency-light access to macro/economic series (especially FRED) alongside basic price history.  
⚠️ *Limitations:* Yahoo/Google Finance readers were deprecated after those free endpoints broke; remaining sources are mostly macro/reference data rather than deep equity fundamentals.

**[findatapy](https://github.com/cuemacro/findatapy)** · Python · ★ 2.1k · last push 2026-07-02  
A Python library that abstracts over many different market-data sources (Bloomberg, Refinitiv Eikon, Quandl/Nasdaq Data Link, Yahoo, ALFRED/FRED, etc.) behind one unified ticker/field naming convention, so downstream code doesn't need to know which vendor actually served the data.

✅ *Good at:* Swapping data vendors without rewriting analysis code, especially useful for teams with access to enterprise sources like Bloomberg alongside free ones.  
⚠️ *Limitations:* Best value requires access to the paid enterprise sources (Bloomberg/Eikon) it's designed to normalize; free-source-only usage is a smaller slice of its value proposition.

**[Massive (Polygon.io) Python client](https://github.com/massive-com/client-python)** · Python · ★ 1.5k · last push 2026-07-09  
Official Python client for Massive.com's REST and WebSocket API (Massive is the rebrand of the well-known Polygon.io data vendor), covering real-time and historical data for stocks, options, forex and crypto, including websocket streaming, corporate actions, and reference/fundamentals endpoints.

✅ *Good at:* Institutional-grade tick and aggregate market data with low-latency websocket streaming and async REST support.  
⚠️ *Limitations:* Full historical tick-level and real-time data requires a paid plan; free tier is delayed/limited.

**[yahooquery](https://github.com/dpguthrie/yahooquery)** · Python · ★ 920 · last push 2025-05-15  
An alternative unofficial Yahoo Finance wrapper often recommended alongside or instead of yfinance, exposing a broader set of Yahoo's undocumented endpoints (screeners, fund holdings, key statistics, financial statements) with async request support for bulk multi-ticker pulls.

✅ *Good at:* Bulk/async retrieval across many tickers at once and access to some Yahoo endpoints (e.g., fund/ETF holdings, screener) yfinance doesn't expose.  
⚠️ *Limitations:* Same unofficial-scraping fragility as yfinance since both depend on Yahoo's undocumented backend.

**[twelvedata-python](https://github.com/twelvedata/twelvedata-python)** · Python · ★ 782 · last push 2026-08-12  
Official Python client and WebSocket SDK for Twelve Data, covering stocks, forex, crypto, ETFs and technical indicators globally, with a generous free tier frequently recommended as a yfinance alternative after Yahoo's scraping instability.

✅ *Good at:* Stable, officially-supported REST+WebSocket data as a drop-in replacement when yfinance breaks.  
⚠️ *Limitations:* Deep fundamentals (multi-year statements, XBRL-level detail) are thinner than SEC-native or FMP-style providers.

**[Nasdaq Data Link Python client](https://github.com/Nasdaq/data-link-python)** · Python · ★ 625 · last push 2026-09-15  
The official client for Nasdaq Data Link (the rebranded Quandl), providing access to a large marketplace of free and paid economic, alternative, and financial datasets through one RESTful interface and Python package.

✅ *Good at:* One client covering a huge marketplace of niche/alternative datasets (many still free) beyond plain-vanilla price data.  
⚠️ *Limitations:* Data quality/coverage varies hugely by individual dataset publisher within the marketplace; premium datasets require separate paid subscriptions.

**[tiingo-python](https://github.com/hydrosquall/tiingo-python)** · Python · ★ 319 · last push 2025-12-14  
Python client for the Tiingo financial data API, providing end-of-day and intraday price data plus a news/article feed, emphasizing data redundancy and transparency across multiple upstream sources.

✅ *Good at:* Reliable EOD price history and a built-in news feed in one client, at a low-cost tier compared to enterprise vendors.  
⚠️ *Limitations:* Fundamentals coverage is thinner than OpenBB/FMP-style providers; primarily a prices+news client.

**[databento-python](https://github.com/databento/databento-python)** · Python · ★ 302 · last push 2026-09-17  
Official Python client for Databento, a newer institutional-grade market data vendor offering live and historical data across MBO, MBP, top-of-book, OHLCV, and last-sale schemas for US equities, options and futures, billed pay-as-you-go rather than flat subscriptions.

✅ *Good at:* High-fidelity tick/order-book historical data with usage-based pricing, appealing to quants who don't want a fixed enterprise contract.  
⚠️ *Limitations:* Pay-per-use can get expensive at scale for full order-book history; equities-and-derivatives focus rather than deep fundamentals.

**[EODHD APIs Python Financial Library](https://github.com/EodHistoricalData/EODHD-APIs-Python-Financial-Library)** · Python · ★ 92 · last push 2026-08-28  
Official Python library for EODHD (EOD Historical Data), covering end-of-day and intraday prices, fundamentals, options, and macro/economic data for global markets (60+ exchanges) at a lower price point than many US-only vendors.

✅ *Good at:* Broad global-exchange fundamentals coverage (not just US equities) at relatively affordable pricing.  
⚠️ *Limitations:* Data depth/accuracy on smaller international exchanges is less battle-tested than US-focused providers.

**[pyEX](https://github.com/iexcloud/pyEX)** · Python · ★ 48 · last push 2024-01-16  
A pandas-friendly Python interface to IEX and IEX Cloud APIs, supporting streaming, premium data, points/economic data, and technical indicators, with transparent request caching to conserve API credits.

✅ *Good at:* Historically strong, well-documented client covering equities, options, and economic data in one package.  
⚠️ *Limitations:* IEX Cloud (the hosted API this wraps) shut down in August 2024, so this client has no functioning backend to call against anymore — kept here only as a historical/reference entry.

**[QuantRocket client](https://github.com/quantrocket-llc/quantrocket-client)** · Python · ★ 32 · last push 2026-09-17  
The CLI and Python client for QuantRocket, a Docker-based quantitative research and trading platform that aggregates multiple data vendors (IBKR, Sharadar fundamentals, Alpaca, EDI, etc.) behind one interface with Zipline/Moonshot backtesting integration.

✅ *Good at:* Unifying fundamentals (via Sharadar) with price data and backtesting in a single self-hosted platform.  
⚠️ *Limitations:* QuantRocket itself (the server component this talks to) is a paid product; the open client alone is not very useful without it.

**[fmp-data](https://github.com/MehdiZare/fmp-data)** · Python · ★ 30 · last push 2026-09-18  
A modern, actively-maintained Python client for the Financial Modeling Prep API, organized into specialized modules for company profiles, market data, fundamentals, technicals, intelligence (news/sentiment), and institutional (13F/insider) data.

✅ *Good at:* One of the most complete and current FMP wrappers, with fundamentals as a first-class module rather than an afterthought.  
⚠️ *Limitations:* Requires a Financial Modeling Prep API key; free tier is rate-limited and missing some premium fundamentals endpoints.

**[py-fmpapi](https://github.com/tidy-finance/py-fmpapi)** · Python · ★ 5 · last push 2025-10-18  
Part of the well-regarded 'Tidy Finance' teaching/research ecosystem, this client wraps the Financial Modeling Prep API and returns Polars DataFrames, covering all published FMP endpoints and parameters.

✅ *Good at:* Polars-native (rather than pandas) financial data workflows, useful for performance-sensitive fundamentals pipelines.  
⚠️ *Limitations:* Smaller community than fmp-data; still requires an FMP API key.

**[fmp-wrapper](https://github.com/cccdenhart/fmp-wrapper)** · Python · ★ 0 · last push 2020-05-01  
One of the earlier simple Python wrappers for the Financial Modeling Prep API, returning results as pandas DataFrames.

✅ *Good at:* Minimal, easy-to-read reference implementation if you want to write your own FMP client from scratch.  
⚠️ *Limitations:* Unmaintained since 2020; superseded by fmp-data and py-fmpapi.

</details>

### Tick & time-series storage

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**TimescaleDB**](https://github.com/timescale/timescaledb) | 23.6k | C | 🟢 | Getting time-series performance for OHLCV/tick data while staying on plain Postgres, so existing SQL tooling, ORMs, and BI tools keep working unchanged. |
| [**QuestDB**](https://github.com/questdb/questdb) | 17.3k | Java | 🟢 | Extremely fast ingest and SQL analytics on high-volume tick/order-book data, often positioned as a practical open-source kdb+ alternative. |
| [**Arctic (legacy)**](https://github.com/man-group/arctic) | 3.1k | Python | 🟠 | Battle-tested MongoDB-backed tick storage for teams already running Mongo infrastructure. |
| [**ArcticDB**](https://github.com/man-group/ArcticDB) | 2.5k | C++/Python | 🟢 | Storing and version-controlling large historical price/fundamentals DataFrames with pandas-native ergonomics and no separate database server to run. |
| [**DolphinDB Tutorials**](https://github.com/dolphindb/Tutorials_EN) | 28 | Python | 🟠 | kdb+-style vectorized time-series analytics without the kdb+ licensing cost, including built-in streaming engines for real-time tick processing. |

<details><summary>Explainers (5)</summary>

**[TimescaleDB](https://github.com/timescale/timescaledb)** · C · ★ 23.6k · last push 2026-09-20  
TimescaleDB packages time-series capabilities (automatic time-based partitioning via 'hypertables', continuous aggregates, compression) as a PostgreSQL extension, letting teams keep using standard SQL/Postgres tooling for financial tick and candlestick data. Timescale publishes official tutorials for ingesting real-time financial websocket data and analyzing tick data with candlestick views.

✅ *Good at:* Getting time-series performance for OHLCV/tick data while staying on plain Postgres, so existing SQL tooling, ORMs, and BI tools keep working unchanged.  
⚠️ *Limitations:* Not as raw-fast at extreme tick-level ingest/query rates as purpose-built engines like QuestDB or kdb+; some advanced features are gated behind the non-fully-open Timescale License.

**[QuestDB](https://github.com/questdb/questdb)** · Java · ★ 17.3k · last push 2026-09-21  
A high-performance, open-source time-series database purpose-built for fast ingest and low-latency SQL queries over tick data, order books, trades, and post-trade analytics, storing data natively as (and now natively querying) Parquet files.

✅ *Good at:* Extremely fast ingest and SQL analytics on high-volume tick/order-book data, often positioned as a practical open-source kdb+ alternative.  
⚠️ *Limitations:* Not a Python-native library — it's a standalone database server requiring separate deployment/operations, with SQL rather than a Python DSL as the primary interface.

**[Arctic (legacy)](https://github.com/man-group/arctic)** · Python · ★ 3.1k · last push 2024-04-08  
The original Man Group tick/time-series datastore, built on top of MongoDB, that ArcticDB was designed to succeed. Still widely referenced and used in older production systems.

✅ *Good at:* Battle-tested MongoDB-backed tick storage for teams already running Mongo infrastructure.  
⚠️ *Limitations:* In maintenance mode — Man Group's active development effort has moved to ArcticDB.

**[ArcticDB](https://github.com/man-group/ArcticDB)** · C++/Python · ★ 2.5k · last push 2026-09-21  
ArcticDB, built by hedge fund Man Group, is a high-performance serverless DataFrame database purpose-built for Python data science, reading/writing pandas DataFrames directly to S3 or LMDB via a fast C++ engine. It supports schemaless writes, time-travel versioning, and querying billions of rows of time-series/tick data efficiently.

✅ *Good at:* Storing and version-controlling large historical price/fundamentals DataFrames with pandas-native ergonomics and no separate database server to run.  
⚠️ *Limitations:* The Business Source License restricts offering ArcticDB itself as a hosted database service commercially, though normal in-house use is free.

**[DolphinDB Tutorials](https://github.com/dolphindb/Tutorials_EN)** · Python · ★ 28 · last push 2024-03-05  
Official English-language tutorials for DolphinDB, a distributed time-series database and programming language commonly marketed as an open(-core) alternative to kdb+ for tick data storage, streaming, and quantitative analytics, with a free community edition.

✅ *Good at:* kdb+-style vectorized time-series analytics without the kdb+ licensing cost, including built-in streaming engines for real-time tick processing.  
⚠️ *Limitations:* DolphinDB itself (the database engine) is not fully open source — the community edition has scale limits, and this repo is only the tutorials, not the engine.

</details>

### News & sentiment

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**newspaper3k**](https://github.com/codelucas/newspaper) | 15.2k | Python | 🟢 | Robust full-text extraction and metadata parsing from almost any news site, a common building block before running FinBERT or other sentiment models on scraped articles. |
| [**FinBERT (ProsusAI)**](https://github.com/ProsusAI/finBERT) | 2.2k | Jupyter Notebook | 🟠 | Being the standard, widely-reused pretrained model checkpoint that dozens of downstream sentiment pipelines (earnings-call NLP, news scoring, WSB analysis) build on. |
| [**Stocker**](https://github.com/dwallach1/Stocker) | 154 | Python | 🟠 | Simple ticker-to-headline-sentiment pipeline without needing a paid news API. |
| [**wallstreetbets-sentiment-analysis**](https://github.com/asad70/wallstreetbets-sentiment-analysis) | 148 | Python | 🟠 | Fast, simple ticker-mention-frequency + sentiment scoring for r/wallstreetbets specifically. |
| [**finance-news-aggregator**](https://github.com/areed1192/finance-news-aggregator) | 147 | Python | 🟢 | Consolidating multiple business-news RSS/API sources into one normalized feed for downstream sentiment scoring. |
| [**wsbtickerbot**](https://github.com/RyanElliott10/wsbtickerbot) | 134 | Python | 🟠 | Historical reference for a PRAW-based ticker-extraction-and-classification pipeline. |
| [**stock-news (Yahoo RSS sentiment PoC)**](https://github.com/primus852/stock-news) | 20 | Python | 🟠 | Very lightweight starting point for RSS-feed-based sentiment scoring. |
| [**Financial News Aggregator (S&P 500)**](https://github.com/gitEricsson/Financial-News-Aggregator) | 0 | Jupyter Notebook | 🟢 | Producing a large, ready-made historical news dataset spanning the full S&P 500 rather than one ticker at a time. |

<details><summary>Explainers (8)</summary>

**[newspaper3k](https://github.com/codelucas/newspaper)** · Python · ★ 15.2k · last push 2026-09-15  
A widely-used, high-star general news and article full-text/metadata extraction library (not finance-specific) that underpins many custom financial-news scraping and sentiment pipelines by handling article discovery, boilerplate removal, and metadata parsing across arbitrary news sites.

✅ *Good at:* Robust full-text extraction and metadata parsing from almost any news site, a common building block before running FinBERT or other sentiment models on scraped articles.  
⚠️ *Limitations:* Not finance-aware out of the box — no ticker tagging or financial-sentiment scoring; that logic must be added on top.

**[FinBERT (ProsusAI)](https://github.com/ProsusAI/finBERT)** · Jupyter Notebook · ★ 2.2k · last push 2022-09-09  
The original, most widely-cited FinBERT: a BERT model further pre-trained on a large financial corpus and fine-tuned for 3-class (positive/neutral/negative) financial sentiment classification, published on the Hugging Face model hub. It remains the de facto baseline for financial-text sentiment work despite the repo itself being dormant.

✅ *Good at:* Being the standard, widely-reused pretrained model checkpoint that dozens of downstream sentiment pipelines (earnings-call NLP, news scoring, WSB analysis) build on.  
⚠️ *Limitations:* The GitHub repo hasn't been updated since 2022; newer, larger LLMs now often outperform it on nuanced financial sentiment, though it remains a fast, cheap baseline.

**[Stocker](https://github.com/dwallach1/Stocker)** · Python · ★ 154 · last push 2020-10-02  
A financial web scraper and sentiment classifier that generates Google News queries for a given ticker, scrapes and parses the resulting articles, and classifies their sentiment.

✅ *Good at:* Simple ticker-to-headline-sentiment pipeline without needing a paid news API.  
⚠️ *Limitations:* Relies on scraping Google News results, which is fragile against layout/policy changes; unmaintained since 2020.

**[wallstreetbets-sentiment-analysis](https://github.com/asad70/wallstreetbets-sentiment-analysis)** · Python · ★ 148 · last push 2021-10-03  
One of the most-starred WSB sentiment tools: finds the most-mentioned ticker on r/wallstreetbets and scores sentiment using VADER's SentimentIntensityAnalyzer, a popular reference implementation for retail-sentiment research after the 2021 meme-stock episode.

✅ *Good at:* Fast, simple ticker-mention-frequency + sentiment scoring for r/wallstreetbets specifically.  
⚠️ *Limitations:* VADER is a general-purpose lexicon sentiment tool, not finance-tuned like FinBERT, and the project is unmaintained since 2021.

**[finance-news-aggregator](https://github.com/areed1192/finance-news-aggregator)** · Python · ★ 147 · last push 2026-04-19  
A Python news aggregator focused specifically on business and market news sources, part of a broader well-regarded series of finance-API tooling by the same author (Sigma Coding).

✅ *Good at:* Consolidating multiple business-news RSS/API sources into one normalized feed for downstream sentiment scoring.  
⚠️ *Limitations:* Aggregation only — no built-in sentiment scoring; needs to be paired with a model like FinBERT.

**[wsbtickerbot](https://github.com/RyanElliott10/wsbtickerbot)** · Python · ★ 134 · last push 2018-10-11  
A Reddit bot using PRAW that scrapes r/wallstreetbets over rolling 24-hour windows, tallies mentioned tickers, and classifies them into bullish/neutral/bearish buckets.

✅ *Good at:* Historical reference for a PRAW-based ticker-extraction-and-classification pipeline.  
⚠️ *Limitations:* One of the oldest WSB scrapers (2018); unmaintained and likely needs updates for the current Reddit API/PRAW versions.

**[stock-news (Yahoo RSS sentiment PoC)](https://github.com/primus852/stock-news)** · Python · ★ 20 · last push 2019-07-16  
A proof-of-concept that scrapes the Yahoo Finance RSS feed and analyzes headline/summary sentiment, packaged as a small pip-installable module.

✅ *Good at:* Very lightweight starting point for RSS-feed-based sentiment scoring.  
⚠️ *Limitations:* Explicitly labeled a PoC; unmaintained since 2019 and Yahoo RSS feeds have since changed.

**[Financial News Aggregator (S&P 500)](https://github.com/gitEricsson/Financial-News-Aggregator)** · Jupyter Notebook · ★ 0 · last push 2026-02-23  
A production-grade scraper that builds a structured, queryable dataset of financial news for all 500 S&P 500 companies from Google News and Yahoo Finance, covering five years (2020-2025) of history for ML training or quant research.

✅ *Good at:* Producing a large, ready-made historical news dataset spanning the full S&P 500 rather than one ticker at a time.  
⚠️ *Limitations:* New project with no stars yet; scraping-based sourcing carries the usual fragility/ToS risk.

</details>

### Alternative data

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**PRAW**](https://github.com/praw-dev/praw) | 4.3k | Python | 🟢 | Reliable, well-documented, actively-maintained access to Reddit's official API, avoiding fragile HTML scraping for WSB/retail-sentiment data collection. |
| [**pytrends**](https://github.com/GeneralMills/pytrends) | 3.7k | Python | 🟠 | Free, simple access to Google Trends search-volume data, the foundational input for many search-interest trading-signal studies (following academic work by Preis, Moat & Stanley). |
| [**gdeltPyR**](https://github.com/linwoodc3/gdeltPyR) | 257 | Jupyter Notebook | 🟠 | Free access to an enormous, continuously-updated global news-event and sentiment/tone database far beyond company-specific headlines. |
| [**QuiverQuant Python API**](https://github.com/Quiver-Quantitative/python-api) | 58 | Python | 🟢 | One-stop access to a very wide basket of alt-data signals (congress, lobbying, WSB, dark pools, patents) that would otherwise require building a dozen separate scrapers. |
| [**Google Trends Financial Modeling**](https://github.com/evilpegasus/google-trends-financial-modeling) | 16 | Jupyter Notebook | 🟠 | Clear, minimal worked example of turning Trends data into an index-prediction feature set. |

<details><summary>Explainers (5)</summary>

**[PRAW](https://github.com/praw-dev/praw)** · Python · ★ 4.3k · last push 2026-09-18  
The Python Reddit API Wrapper is the standard, actively-maintained library nearly every r/wallstreetbets and retail-sentiment scraper (including wsbtickerbot and wallstreetbets-sentiment-analysis in this catalog) is built on top of, providing authenticated access to subreddits, posts, and comments.

✅ *Good at:* Reliable, well-documented, actively-maintained access to Reddit's official API, avoiding fragile HTML scraping for WSB/retail-sentiment data collection.  
⚠️ *Limitations:* Requires a registered Reddit API application and complying with Reddit's API terms/rate limits (which tightened significantly in 2023).

**[pytrends](https://github.com/GeneralMills/pytrends)** · Python · ★ 3.7k · last push 2024-08-10  
The most widely-used unofficial pseudo-API for Google Trends, used across finance and beyond to pull search-interest-over-time and related-query data by keyword or ticker as an alternative-data input into market models.

✅ *Good at:* Free, simple access to Google Trends search-volume data, the foundational input for many search-interest trading-signal studies (following academic work by Preis, Moat & Stanley).  
⚠️ *Limitations:* Unofficial and scraping-based, so it periodically breaks when Google changes endpoints; the repo has had limited maintenance activity, and several newer forks/alternatives exist for reliability.

**[gdeltPyR](https://github.com/linwoodc3/gdeltPyR)** · Jupyter Notebook · ★ 257 · last push 2023-11-30  
Python framework for retrieving GDELT (Global Database of Events, Language, and Tone) v1/v2 data — a massive, free, 15-minute-updated global news-event and tone database spanning over 100 languages — useful as a macro/geopolitical alternative-data source for cross-asset and country-level signals.

✅ *Good at:* Free access to an enormous, continuously-updated global news-event and sentiment/tone database far beyond company-specific headlines.  
⚠️ *Limitations:* GDELT's raw data volume and noise require significant downstream filtering to be useful for single-stock signals; client unmaintained since 2023.

**[QuiverQuant Python API](https://github.com/Quiver-Quantitative/python-api)** · Python · ★ 58 · last push 2026-05-07  
Official Python client for QuiverQuant, an alternative-data aggregator exposing congressional trading, corporate lobbying, government contracts, patents, off-exchange (dark-pool) short volume, Wikipedia page-view interest, Reddit/WallStreetBets mentions, and insider transactions all mapped to tickers through one API and token.

✅ *Good at:* One-stop access to a very wide basket of alt-data signals (congress, lobbying, WSB, dark pools, patents) that would otherwise require building a dozen separate scrapers.  
⚠️ *Limitations:* The underlying QuiverQuant service is a paid product (from ~$10/month) — the open client is just the access layer, not the free data itself.

**[Google Trends Financial Modeling](https://github.com/evilpegasus/google-trends-financial-modeling)** · Jupyter Notebook · ★ 16 · last push 2020-12-08  
Uses pytrends-sourced Google Trends search-volume data as an alternative-data feature to predict broad index movements, a compact reference example of the search-trends-as-alpha approach.

✅ *Good at:* Clear, minimal worked example of turning Trends data into an index-prediction feature set.  
⚠️ *Limitations:* Small research notebook, not a reusable pipeline; unmaintained since 2020.

</details>

### Screeners

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**finvizfinance**](https://github.com/lit26/finvizfinance) | 1.7k | Python | 🟢 | Very quick fundamental screening (P/E, margins, growth, etc.) plus a bonus insider-trading feed, all from Finviz's well-curated free data. |
| [**TradingView-Screener**](https://github.com/shner-elmo/TradingView-Screener) | 1.3k | Python | 🟢 | Access to TradingView's very broad global fundamentals+technicals screening fields without needing a scraping layer of your own. |
| [**PKScreener**](https://github.com/pkjmesra/PKScreener) | 397 | Python | 🟢 | Deep coverage of NSE-specific breakout and consolidation screening logic, filling a gap most US-centric screeners don't cover. |

<details><summary>Explainers (3)</summary>

**[finvizfinance](https://github.com/lit26/finvizfinance)** · Python · ★ 1.7k · last push 2026-08-29  
A popular Python library wrapping Finviz.com, exposing its stock screener filters, fundamental ratios, insider trading data, and news/sentiment pages through a simple pandas-returning API.

✅ *Good at:* Very quick fundamental screening (P/E, margins, growth, etc.) plus a bonus insider-trading feed, all from Finviz's well-curated free data.  
⚠️ *Limitations:* Unofficial scraper of Finviz's site, so heavy/rapid usage risks throttling or breakage if Finviz changes its HTML.

**[TradingView-Screener](https://github.com/shner-elmo/TradingView-Screener)** · Python · ★ 1.3k · last push 2026-09-20  
Lets users build TradingView-style stock/crypto/forex screeners programmatically in Python, querying TradingView's own screener backend for fundamentals and technicals across global markets with a fluent filter/query API.

✅ *Good at:* Access to TradingView's very broad global fundamentals+technicals screening fields without needing a scraping layer of your own.  
⚠️ *Limitations:* Depends on TradingView's unofficial backend endpoints, which can change without notice.

**[PKScreener](https://github.com/pkjmesra/PKScreener)** · Python · ★ 397 · last push 2026-09-20  
An advanced, actively-maintained free stock screener for India's NSE exchange, identifying potential breakout stocks, consolidation patterns, and chart-pattern setups, with active daily development.

✅ *Good at:* Deep coverage of NSE-specific breakout and consolidation screening logic, filling a gap most US-centric screeners don't cover.  
⚠️ *Limitations:* India/NSE-focused only, not useful out-of-the-box for US or other-market fundamental screening.

</details>

### Other

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**filib (Factor Investing Library)**](https://github.com/prmkowalski/filib) | 29 | Python | 🟠 | Quick iteration on custom fundamental factor definitions and their portfolio-level rebalancing performance. |

<details><summary>Explainers (1)</summary>

**[filib (Factor Investing Library)](https://github.com/prmkowalski/filib)** · Python · ★ 29 · last push 2022-11-12  
A lightweight factor-investing library for testing predictive fundamental/technical factors and running portfolio rebalancing based on those factors, aimed at retail-accessible factor-strategy research.

✅ *Good at:* Quick iteration on custom fundamental factor definitions and their portfolio-level rebalancing performance.  
⚠️ *Limitations:* Small, unmaintained since 2022; lacks the depth of institutional factor-model libraries.

</details>

[⬆ back to top](#contents)

## Strategy research papers

113 papers, mostly 2024–2026, covering momentum, value and quality, earnings events, options-implied signals, ML and LLM signals, RL, alpha mining, stat-arb, crypto and prediction markets. Only 7 publish code. Returns are copied **as the authors report them**. Most recent LLM and RL papers report Sharpe ratios above 2 without transaction costs or clean out-of-sample tests, so treat those as upper bounds.

**Read these caveats first**

- **Borrow costs erase much of the anomaly zoo.** Muravyev, Pearson & Pollet (JF 2025) find 162 anomalies average +0.14%/month gross but about −0.01%/month net of stock-borrow fees. Size short legs with real borrow data.
- **The “GPT-4 beats analysts” paper was withdrawn** (Kim, Muhn & Nikolaev) after replication problems, yet it is still widely cited.
- **LLM look-ahead:** models may have memorized the backtest period. Prefer forward or live tests (e.g. LiveTradeBench, DeepFund) over backtests on pre-cutoff news.
- **Regime risk:** a 2026 paper finds the classic options-skew signal weakened in the 2023–2026 AI/mega-cap regime.

### Editor’s picks for a US equity long/short book (days–weeks holding)

| # | Strategy | Why | Key papers |
|---|---|---|---|
| 1 | **Text-based post-earnings drift** | Earnings-call and press-release text measures of surprise drift for weeks and beat numeric-surprise-only PEAD. | PEAD.txt (JFQA 2023), earnings-call NLP papers |
| 2 | **Analyst estimate-revision momentum** | Cheap and implementable with consensus-estimate history. It works best in less-covered names. | Fundamental-momentum literature |
| 3 | **Crash-aware cross-sectional momentum** | Classic 3–12 month momentum with volatility scaling to survive momentum crashes. | Jegadeesh–Titman (1993), Daniel–Moskowitz (2016) |
| 4 | **Short-term reversal as liquidity provision** | A days-horizon strategy that pays for providing liquidity. It is sensitive to costs, so model spreads. | Dai, Medhat, Novy-Marx & Rizova (2024) |
| 5 | **Overnight vs. intraday decomposition** | Most index gains accrue overnight. It is cheap to test with OHLC data, but partly arbitraged. | Overnight-returns papers |
| 6 | **Options-implied skew, regime-conditioned** | A classic cross-sectional signal, but a 2026 paper finds it weakened in the AI/mega-cap regime. | Tian & Wu; JFE 2025; arXiv 2608.26115 |
| 7 | **Fine-tuned LLM news sentiment** | Real incremental information, but reported Sharpe ratios are inflated by look-ahead. Test forward. | Lopez-Lira & Tang (2023), FinDPO, newsflow fine-tuning |
| 8 | **ML cross-sectional prediction + text** | Small per-stock R² still produces meaningful long–short spreads. Add news embeddings. | Gu–Kelly–Xiu (2020), Chen–Pelger–Zhu (2023) |
| 9 | **Factor timing & decay monitoring** | An overlay that decides which sleeves to lean into as regimes change. | Deep-learning factor-timing papers |
| 10 | **Automated alpha mining** | Generate formulaic alphas with RL or LLM search, then feed them into an ML or timing layer. | AlphaGen (KDD 2023), RD-Agent(Q) (NeurIPS 2025) |

### Earnings events & PEAD

| Year | Paper | Strategy | Reported return | Sharpe | Net of costs | OOS | Code |
|---|---|---|---|---|:-:|:-:|:-:|
| 2026 | [Fast Numbers, Slow Language: Bridging Quantitative and Qualitative Earnings Signals](https://arxiv.org/pdf/2606.29734)<br><sub>arXiv q-fin</sub> | Combines fast-moving numeric earnings-surprise signals with slower-to-process qualitative (text) earnings signals, likely arguing the two convey complementary and non-redundant information for post-earnings drift.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2025 | [FinCall-Surprise: A Large-Scale Multi-Modal Benchmark for Earning Surprise Prediction](https://arxiv.org/abs/2510.03965)<br><sub>arXiv q-fin/cs.CL</sub> | Benchmark dataset/task for predicting earnings surprises from multi-modal earnings-call data (audio + transcript + numeric fundamentals), used to evaluate models' ability to forecast whether next-quarter EPS beats or misses consensus.<br><sub>Large-scale earnings-call dataset (exact coverage not captured)</sub> | — | — | ❔ | ❔ |  |
| 2025 | [Extracting the Structure of Press Releases for Predicting Earnings Announcement Returns](https://arxiv.org/abs/2509.24254)<br><sub>arXiv q-fin</sub> | Uses the structural/formatting features of earnings press releases (not just their sentiment content) as a predictor of the announcement-window stock return.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2025 | [LLM-Driven Investment Models: Can Large Language Models Extract Alpha from Earnings Call Transcripts?](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6351439)<br><sub>SSRN 6351439</sub> | Uses LLM embeddings of earnings-call transcripts as investment signals, testing whether the language-derived representation contains return-predictive information beyond traditional numeric/fundamental features.<br><sub>More than 14,000 earnings-call events, 2019-2023</sub> | — | LLM-embedding-based signals reported to produce stronger risk-adjusted performance than traditional approaches, though exact Sharpe/return figures not captured in this pass | ❔ | ❔ |  |
| 2025 | [Agentic Retrieval of Topics and Insights from Earnings Calls](https://arxiv.org/html/2507.07906v1)<br><sub>arXiv q-fin</sub> | An LLM-agent pipeline (Topic Retriever + Ontologist) that discovers and maintains a hierarchical ontology of financially relevant topics across earnings calls, building a structured knowledge graph (3,200 nodes from 141 transcripts in the reported experiment) rather than a flat sentiment score.<br><sub>141 earnings-call transcripts</sub> | — | — | ❔ | ❔ |  |
| 2023 | [PEAD.txt: Post-Earnings-Announcement Drift Using Text](https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/peadtxt-postearningsannouncementdrift-using-text/5EB217BB68B5FB054FE38541BAAC4679)<br><sub>Journal of Financial and Quantitative Analysis</sub> | Defines earnings surprise using a text-based measure derived from earnings-call transcripts/press releases (rather than the standard analyst-consensus EPS surprise), and shows a long-short PEAD strategy sorted on this text-based surprise produces stronger post-earnings drift than surprise-based on numbers alone.<br><sub>US earnings announcements, 2008-2019</sub> | text-based PEAD strategy generates drift of about 1.11%-2.87% over the post-announcement window (varies by exact text specification), versus smaller drift (~1.65%) from alternative text/quintile-spread measures | — | ❌ | ❔ |  |

<details><summary>How to recreate (6)</summary>

**[Fast Numbers, Slow Language: Bridging Quantitative and Qualitative Earnings Signals](https://arxiv.org/pdf/2606.29734)** (2026)  
🔧 Requires numeric EPS-surprise data plus earnings-call/press-release text; build separate numeric and text-derived surprise scores, combine (e.g., via regression or simple z-score average), and test PEAD strategy performance of the combined signal vs. either alone.  
⚠️ Title/abstract only; not independently verified in this pass.

**[FinCall-Surprise: A Large-Scale Multi-Modal Benchmark for Earning Surprise Prediction](https://arxiv.org/abs/2510.03965)** (2025)  
🔧 Requires earnings-call audio+transcript plus consensus EPS estimates; train a multi-modal model (text + audio prosody features + numeric fundamentals) to classify beat/miss, then convert predictions into a pre-earnings or post-earnings trading signal.  
⚠️ Primarily a benchmark/dataset paper rather than a live trading-strategy paper; useful as a data-construction template if Massive has earnings-call audio or transcripts.

**[Extracting the Structure of Press Releases for Predicting Earnings Announcement Returns](https://arxiv.org/abs/2509.24254)** (2025)  
🔧 Requires a corpus of earnings press releases with structural metadata (section ordering, length, presence of tables, etc.) plus announcement-window returns; fit a model using structural features (possibly LLM-parsed) to predict return direction/magnitude, trade around the announcement.  
⚠️ Title/abstract only; not independently verified in this pass.

**[LLM-Driven Investment Models: Can Large Language Models Extract Alpha from Earnings Call Transcripts?](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6351439)** (2025)  
🔧 Requires a large earnings-call transcript corpus (14k+ events) plus post-call returns; embed each transcript with an LLM embedding model, use the embedding (possibly reduced via PCA or a small supervised head) as a cross-sectional predictor, form long-short deciles post-call.  
⚠️ Consistent with the broader finding across this literature that LLM-derived text representations of earnings calls carry incremental information over numeric surprise alone; but note training-data-cutoff/look-ahead risk if the embedding model was pretrained on data overlapping 2019-2023 transcripts.

**[Agentic Retrieval of Topics and Insights from Earnings Calls](https://arxiv.org/html/2507.07906v1)** (2025)  
🔧 Requires earnings-call transcripts; run an LLM pipeline to extract and cluster topics into an ontology, then use topic-level features (e.g., emergence of a new risk topic, or topic sentiment) as trading signals -- this is more of a research/NLP-infrastructure paper than a ready-made trading rule.  
⚠️ Small sample (141 transcripts); this is a topic-extraction/knowledge-representation contribution rather than a validated trading strategy with reported returns.

**[PEAD.txt: Post-Earnings-Announcement Drift Using Text](https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/peadtxt-postearningsannouncementdrift-using-text/5EB217BB68B5FB054FE38541BAAC4679)** (2023)  
🔧 Requires earnings-call transcripts or press releases plus standard EPS-surprise data and post-announcement daily returns. Construct a text-based surprise score (e.g., via a trained classifier or embedding similarity to prior calls), sort firms into deciles at announcement, hold 20-60 trading days, rebalance each earnings season.  
⚠️ A foundational text-based-PEAD paper feeding much of the later LLM-earnings-call literature; drift is measured gross of costs and pre-dates modern LLM embeddings, so a news + transcript feed with an LLM embedding could likely reproduce or extend it.

</details>

### Analyst revisions

| Year | Paper | Strategy | Reported return | Sharpe | Net of costs | OOS | Code |
|---|---|---|---|---|:-:|:-:|:-:|
| 2025 | [Corporate Earnings Calls and Analyst Beliefs](https://arxiv.org/pdf/2511.15214)<br><sub>arXiv q-fin</sub> | Studies how earnings-call content updates sell-side analyst beliefs (and by extension, subsequent forecast revisions), relevant to designing an analyst-revision-anticipation signal from call transcripts.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2023 | [Earnings Forecasts and Revisions, Price Momentum, and Fundamental Data (chapter overview of AQR-style earnings-revision composites)](https://go.factset.com/hubfs/Symposium%20Images/Guerard_EARNINGS%20FORECASTS%20AND%20REVISIONS,%20PRICE%20MOMENTUM,%20AND%20FUNDAMENTAL%20DATA.pdf)<br><sub>Book chapter / FactSet symposium material</sub> | Composite of earnings momentum (trailing EPS growth), analyst estimate revisions (recent up/down revisions to consensus), and margin growth, combined with price momentum into a 'fundamental momentum' factor used by AQR and others; long stocks with positive revision momentum, short those with negative.<br><sub>US and global equities, multi-decade practitioner use</sub> | — | — | ❔ | ❔ |  |

<details><summary>How to recreate (2)</summary>

**[Corporate Earnings Calls and Analyst Beliefs](https://arxiv.org/pdf/2511.15214)** (2025)  
🔧 Requires earnings-call transcripts plus subsequent analyst forecast-revision data (I/B/E/S-style); measure how call content predicts the direction/magnitude of near-term analyst revisions, then trade ahead of the revision using the call-derived signal.  
⚠️ Title/abstract only; not independently verified in this pass -- included to mark the analyst-revision-from-text category, which is thinner in the recent literature than sentiment/PEAD.

**[Earnings Forecasts and Revisions, Price Momentum, and Fundamental Data (chapter overview of AQR-style earnings-revision composites)](https://go.factset.com/hubfs/Symposium%20Images/Guerard_EARNINGS%20FORECASTS%20AND%20REVISIONS,%20PRICE%20MOMENTUM,%20AND%20FUNDAMENTAL%20DATA.pdf)** (2023)  
🔧 Requires consensus EPS estimate history (I/B/E/S-style, so revision direction/magnitude can be computed) plus prices. Compute 1-3 month change in consensus EPS estimate per stock, rank cross-sectionally, go long top revision decile / short bottom, rebalance monthly; smaller-cap names show a stronger effect per the underlying literature.  
⚠️ This is a practitioner/survey-style anchor rather than a single rigorous academic paper with clean out-of-sample stats; useful mainly as a recipe (analyst-revision momentum is one of the more implementable, data-light factors if a fundamentals feed with consensus estimates is available).

</details>

### Momentum

| Year | Paper | Strategy | Reported return | Sharpe | Net of costs | OOS | Code |
|---|---|---|---|---|:-:|:-:|:-:|
| 2025 | [Quantpedia: aggregated ETF/momentum composite strategy backtest](https://quantpedia.com/quantpedia-in-june-2025/)<br><sub>Quantpedia blog/database</sub> | Combines three momentum-style 'legs' into a single composite long-short strategy, selectively going long top-performing ETFs while shorting a small number of the weakest.<br><sub>Global ETFs (asset classes), period not fully specified</sub> | 5.99% annualized return for the long-short composite variant | 0.55 | ❔ | ❔ |  |
| 2025 | [Winners vs. Losers: Momentum-Based Strategies with Intertemporal Choice for ESG Portfolios](https://arxiv.org/html/2505.24250v1)<br><sub>arXiv q-fin</sub> | Introduces a state-dependent momentum framework integrating ESG regime-switching with tail-risk-aware reward-risk metrics across three asset universes including the Russell 3000, examining whether policy/ESG sentiment drives cross-sectional return continuation.<br><sub>Three universes including the Russell 3000</sub> | — | — | ❔ | ❔ |  |
| 2023 | [Spatio-Temporal Momentum: Jointly Learning Time-Series and Cross-Sectional Strategies](https://arxiv.org/abs/2302.10175)<br><sub>Journal of Financial Data Science / arXiv:2302.10175</sub> | A single neural network (even a simple one-layer network) is trained jointly across assets to produce both time-series and cross-sectional momentum signals simultaneously, sharing information across the cross-section instead of fitting per-asset models.<br><sub>46 actively-traded US equities and 12 equity index futures</sub> | — | reported to retain performance advantage over single-asset TSMOM/cross-sectional benchmarks; exact Sharpe not captured in this pass | ✅ | ✅ |  |
| 2023 | [Deep Inception Networks: A General End-to-End Framework for Multi-Asset Quantitative Strategies](https://arxiv.org/pdf/2307.05522)<br><sub>arXiv q-fin</sub> | Applies an Inception-style (multi-scale convolutional) deep-learning architecture end-to-end across multiple assets for quantitative trend/momentum-style strategies, aiming to capture patterns at multiple time scales simultaneously.<br><sub>Multi-asset futures universe (not fully specified)</sub> | — | — | ❔ | ❔ |  |
| 2023 | [Few-Shot Learning Patterns in Financial Time-Series for Trend-Following Strategies](https://arxiv.org/pdf/2310.10500)<br><sub>arXiv q-fin</sub> | Applies few-shot learning techniques to identify recurring price patterns useful for trend-following, aiming to adapt quickly to new instruments/regimes with limited data.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2023 | [Constructing Time-Series Momentum Portfolios with Deep Multi-Task Learning](https://arxiv.org/pdf/2306.13661)<br><sub>arXiv q-fin</sub> | Uses a multi-task learning architecture (shared representation across related prediction tasks, e.g., multiple horizons or multiple instruments) to construct time-series momentum portfolios.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2021 | [Trading with the Momentum Transformer: An Intelligent and Interpretable Architecture](https://arxiv.org/abs/2112.08534)<br><sub>arXiv (Journal of Financial Data Science)</sub> | Attention-based transformer trend-following model with an added change-point detection (CPD) module that flags regime shifts, feeding into position sizing; outputs positions directly (Sharpe-optimized) rather than return forecasts.<br><sub>Diversified futures portfolio, backtested 1995-2020</sub> | — | adding CPD module improves Sharpe ratio by about one-third over 1995-2020, and by about two-thirds over the more recent 2015-2020 subperiod, net of transaction costs | ✅ | ✅ | [↗](https://github.com/kieranjwood/trading-momentum-transformer) |
| 2021 | [Trend-Following Strategies via Dynamic Momentum Learning](https://arxiv.org/pdf/2106.08420)<br><sub>arXiv:2106.08420</sub> | Learns a dynamic (time-varying) momentum lookback/weighting scheme rather than a fixed lookback window, adapting trend-following signal construction to changing market dynamics.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2019 | [Enhancing Time-Series Momentum Strategies Using Deep Neural Networks (Deep Momentum Networks)](https://arxiv.org/abs/1904.04912)<br><sub>arXiv / Journal of Financial Data Science</sub> | Deep Momentum Networks: an LSTM directly outputs a trading-rule position (not just a return forecast) that is trained end-to-end to maximize a differentiable Sharpe-ratio objective, replacing hand-crafted trend/vol-scaling rules.<br><sub>88 continuous futures contracts across asset classes, ~1990-2015</sub> | — | Sharpe-optimized LSTM improves on traditional TSMOM by more than 2x gross of costs; still outperforms with 2-3bps transaction costs | ✅ | ✅ | [↗](https://github.com/kieranjwood/trading-momentum-transformer) |
| 2016 | [Momentum Crashes](https://www.sciencedirect.com/science/article/pii/S0304405X16301490)<br><sub>Journal of Financial Economics</sub> | Documents that momentum strategies occasionally suffer large, persistent crashes (notably 2009), concentrated in past-loser portfolios during market rebounds following high-volatility periods, and proposes dynamically scaling momentum exposure by forecasted variance/market-state to avoid crash periods.<br><sub>US equities, 1926-2013</sub> | — | — | ❌ | ❌ |  |
| 2012 | [Time Series Momentum](https://www.sciencedirect.com/science/article/pii/S0304405X11002613)<br><sub>Journal of Financial Economics</sub> | For each of 58 futures/forwards (equities, bonds, currencies, commodities), go long if trailing 12-month excess return is positive, short if negative; volatility-scale each position and combine into a diversified portfolio.<br><sub>58 liquid futures/forward contracts across asset classes, 1985-2009</sub> | positive time-series momentum return for essentially every contract; diversified TSMOM portfolio Sharpe reported well above 1 | diversified portfolio Sharpe ratio > 1 (exact figure not captured from this pass) | ❌ | ❌ |  |
| 1993 | [Returns to Buying Winners and Selling Losers: Implications for Stock Market Efficiency](https://www.jstor.org/stable/2328882)<br><sub>Journal of Finance</sub> | Rank US stocks on trailing 3-12 month returns; go long past winners and short past losers, holding 3-12 months, skipping a short formation-to-holding gap.<br><sub>US stocks (NYSE/AMEX), 1965-1989</sub> | approx. 1% per month (about 12% annualized) for 6-month formation/6-month holding long-short | — | ❌ | ❌ |  |

<details><summary>How to recreate (12)</summary>

**[Quantpedia: aggregated ETF/momentum composite strategy backtest](https://quantpedia.com/quantpedia-in-june-2025/)** (2025)  
🔧 Requires only daily ETF prices across asset classes (equity, bond, commodity, currency ETFs); compute momentum ranks per leg, combine into a composite score, go long top ETFs / short bottom ETF(s), rebalance monthly; the strategy is invested less than half the days each month (partial time-in-market by design).  
⚠️ A modest absolute Sharpe (0.55) reflects that this is a diversifying, low-turnover overlay rather than a high-conviction alpha strategy; more relevant to asset-allocation books than a tech-equity long/short book.

**[Winners vs. Losers: Momentum-Based Strategies with Intertemporal Choice for ESG Portfolios](https://arxiv.org/html/2505.24250v1)** (2025)  
🔧 Requires standard momentum signal construction plus an ESG-regime classification (e.g., based on ESG-related news flow/policy sentiment) and a tail-risk-aware position-sizing rule (similar in spirit to Daniel-Moskowitz dynamic scaling).  
⚠️ Title/abstract only for detailed numbers; relevant if the target book incorporates ESG/policy-sentiment tilts alongside momentum.

**[Spatio-Temporal Momentum: Jointly Learning Time-Series and Cross-Sectional Strategies](https://arxiv.org/abs/2302.10175)** (2023)  
🔧 Daily prices for a modest cross-section (dozens of names) suffice; construct a pooled training set of lagged returns across assets, train one shared network to output per-asset positions, apply LASSO/turnover regularization, and test robustness at 5-10bps costs.  
⚠️ Small universe (46 stocks) — capacity and generalization to broader US equity universes untested here.

**[Deep Inception Networks: A General End-to-End Framework for Multi-Asset Quantitative Strategies](https://arxiv.org/pdf/2307.05522)** (2023)  
🔧 Requires daily multi-asset price history; build multi-scale convolutional feature extractors (parallel kernels at different lookback lengths) feeding a position-sizing output layer trained end-to-end (e.g., Sharpe-loss as in the DMN papers).  
⚠️ Title/abstract only; not independently verified in this pass -- grouped with the broader deep-trend-following literature (DMN, Momentum Transformer).

**[Few-Shot Learning Patterns in Financial Time-Series for Trend-Following Strategies](https://arxiv.org/pdf/2310.10500)** (2023)  
🔧 Requires daily price data across a broad instrument set for meta-training, then a few-shot fine-tuning step on a new/target instrument with limited history.  
⚠️ Title/abstract only; not independently verified in this pass.

**[Constructing Time-Series Momentum Portfolios with Deep Multi-Task Learning](https://arxiv.org/pdf/2306.13661)** (2023)  
🔧 Requires multi-asset daily price data; define related auxiliary tasks (e.g., predicting returns at multiple horizons, or across related instruments) trained jointly with a shared encoder, use the shared representation to size TSMOM positions.  
⚠️ Title/abstract only; not independently verified in this pass.

**[Trading with the Momentum Transformer: An Intelligent and Interpretable Architecture](https://arxiv.org/abs/2112.08534)** (2021)  
🔧 Continuous daily futures data; build change-point-detection features (Gaussian process based) plus price/volatility features; train transformer with attention over lookback window, Sharpe-ratio loss, walk-forward retraining across regimes (including COVID).  
⚠️ Improvement is measured against the authors' own DMN/TSMOM baselines, not against a simple buy-and-hold; capacity and crowding for futures trend-followers are separate concerns not addressed here.

**[Trend-Following Strategies via Dynamic Momentum Learning](https://arxiv.org/pdf/2106.08420)** (2021)  
🔧 Requires daily multi-asset price data; replace the fixed-lookback trend signal with a learned, time-varying weighting function over past returns (e.g., via a small neural net or attention layer), train to maximize a Sharpe-like objective.  
⚠️ Title/abstract only; not independently verified in this pass.

**[Enhancing Time-Series Momentum Strategies Using Deep Neural Networks (Deep Momentum Networks)](https://arxiv.org/abs/1904.04912)** (2019)  
🔧 Requires continuous daily futures price series (~88 contracts) and engineered features (returns/vol at multiple lookbacks, MACD-style indicators). Train an LSTM per instrument or pooled, with a differentiable Sharpe loss; walk-forward retrain and combine positions with vol targeting.  
⚠️ One of the most-cited deep-learning trend-following papers; basis for the later Momentum Transformer. Reported outperformance narrows sharply once realistic costs and capacity constraints are included.

**[Momentum Crashes](https://www.sciencedirect.com/science/article/pii/S0304405X16301490)** (2016)  
🔧 Requires only daily/monthly prices. Construct standard 12-month momentum long-short portfolio, compute rolling realized market volatility, scale gross momentum exposure down (or hedge the short-loser leg) when past volatility is high and the market has recently been down (bear-market-rebound risk state), rebalance monthly.  
⚠️ Seminal anchor for momentum crash risk and dynamic risk-managed momentum; directly relevant to any momentum sleeve in a tech-heavy book, since past-loser short legs are exactly where crash risk concentrates during sharp market rebounds (e.g., post-drawdown tech rallies).

**[Time Series Momentum](https://www.sciencedirect.com/science/article/pii/S0304405X11002613)** (2012)  
🔧 Needs daily futures/continuous-contract prices (equities alone insufficient for full replication, but the sign-of-trailing-return + vol-scaling rule can be applied to any daily price series, including single-name equities or sector ETFs). Rebalance monthly.  
⚠️ Seminal anchor for time-series momentum / trend-following; in-sample period, gross of costs. Basis for most modern deep-learning TSMOM papers below.

**[Returns to Buying Winners and Selling Losers: Implications for Stock Market Efficiency](https://www.jstor.org/stable/2328882)** (1993)  
🔧 Daily/monthly close prices only. Compute trailing J-month cumulative return per stock, sort into deciles, go long top decile / short bottom decile, hold K months with monthly overlapping rebalancing. Fully doable with daily price history alone.  
⚠️ Seminal anchor paper for cross-sectional momentum; in-sample discovery period, no transaction costs. Momentum crashes (2009) and post-2000s decay are well documented in follow-on literature.

</details>

### Value & quality

| Year | Paper | Strategy | Reported return | Sharpe | Net of costs | OOS | Code |
|---|---|---|---|---|:-:|:-:|:-:|
| 2025 | [A New Quality Factor Adjusted by Fraud Probability](https://www.sciencedirect.com/science/article/abs/pii/S1544612325004167)<br><sub>Finance Research Letters, Vol. 78</sub> | Modifies the standard Quality-Minus-Junk factor by down-weighting/excluding firms with a high estimated probability of financial-statement fraud (via a bivariate probit model that accounts for undetected fraud), producing a 'fraud-mitigated QMJ' (fmQMJ) factor.<br><sub>China and US equities</sub> | fmQMJ portfolio earns significant average excess returns in both China and the US, and outperforms the original QMJ factor specifically within low-size and low-book-to-market subgroups | — | ❔ | ❔ |  |
| 2019 | [Quality Minus Junk](http://www.econ.yale.edu/~shiller/behfin/2013_04-10/asness-frazzini-pedersen.pdf)<br><sub>Review of Accounting Studies (working paper circulated 2013+)</sub> | Blends multiple quality sub-scores -- profitability, growth, safety (low leverage/low earnings volatility/low beta), and payout/management quality -- into a single composite Quality-Minus-Junk (QMJ) factor; long high-quality stocks, short low-quality ('junk'), often combined with value.<br><sub>US and international equities, multi-decade sample (1957-2016 in later AQR data updates)</sub> | — | — | ❌ | ❌ |  |
| 2014 | [Betting Against Beta](https://www.aqr.com/-/media/AQR/Documents/Insights/BAB.pdf)<br><sub>Journal of Financial Economics</sub> | Constructs a leverage-adjusted, beta-neutral long-short portfolio: long low-beta stocks (levered up to unit beta), short high-beta stocks (delevered to unit beta), designed to exploit leverage-constrained investors' tendency to overweight high-beta stocks and thus underprice low-beta ones.<br><sub>US and 19 other international equity markets, plus Treasury bonds, credit and futures, multi-decade sample</sub> | — | — | ❌ | ❌ |  |
| 2013 | [The Gross Profitability Premium](https://mysimon.rochester.edu/novy-marx/research/OSoV.pdf)<br><sub>Journal of Financial Economics</sub> | Sorts stocks on gross profitability (revenue minus cost of goods sold, scaled by total assets) as a cleaner, less-manipulable profitability/quality measure than net income; long high gross-profitability stocks, short low, often combined with a value tilt ('the other side of value').<br><sub>US equities, 1963-2010</sub> | profitable-minus-unprofitable long-short spread has a Fama-French-3-factor alpha of about 0.52% per month (t-stat 4.49); a 2015 international extension found an average annual profitability premium of about 3.6% across 15 European markets, 1982-2014 | — | ❌ | ❌ |  |
| 1996 | [Do Stock Prices Fully Reflect Information in Accruals and Cash Flows About Future Earnings? (the accrual anomaly)](https://www.jstor.org/stable/248290)<br><sub>The Accounting Review</sub> | Sorts stocks on the accrual component of earnings (earnings minus operating cash flow, scaled by assets); long low-accrual (cash-flow-backed earnings) stocks, short high-accrual (earnings management-prone) stocks, based on evidence that the market underreacts to the lower persistence of accruals vs. cash flows.<br><sub>US equities, 1962-1991 (original); a 1972-2010 replication finds similar magnitude</sub> | a low-minus-high total-accruals long-short portfolio earns a significant average return of about 0.71% per month (~8.5% annualized) in a 1972-2010 replication | — | ❌ | ❌ |  |

<details><summary>How to recreate (5)</summary>

**[A New Quality Factor Adjusted by Fraud Probability](https://www.sciencedirect.com/science/article/abs/pii/S1544612325004167)** (2025)  
🔧 Requires fundamentals plus a fraud-probability model (e.g., an F-score/M-score-style probit or logit model estimated on known historical fraud cases, extended with a bivariate specification for undetected fraud); compute standard QMJ, then re-weight/exclude high-fraud-probability names before forming the long-short portfolio.  
⚠️ Directly relevant caution for small-cap/low-B/M value-quality strategies (exactly where accounting fraud risk concentrates); a fraud-probability overlay is a reasonable, implementable robustness layer on top of any fundamentals-based quality/value screen if audit/litigation/restatement data is available.

**[Quality Minus Junk](http://www.econ.yale.edu/~shiller/behfin/2013_04-10/asness-frazzini-pedersen.pdf)** (2019)  
🔧 Requires fundamentals (profitability ratios, leverage, earnings/ROE volatility, payout ratio) plus price-derived beta; z-score and average the four quality sub-components per firm, rank cross-sectionally, go long top quality decile / short bottom, rebalance monthly-to-quarterly. AQR publishes a monthly QMJ factor return series for direct benchmarking.  
⚠️ One of the most widely used quality composites in practice; AQR provides the constructed factor series publicly for validation. Gross of costs, published construction may already be crowded/lower-Sharpe out of the original sample.

**[Betting Against Beta](https://www.aqr.com/-/media/AQR/Documents/Insights/BAB.pdf)** (2014)  
🔧 Requires only prices (to estimate rolling betas) -- no fundamentals needed. Estimate each stock's rolling beta (e.g., 1-year daily or 5-year monthly), rank into low/high-beta portfolios, weight to be beta-neutral overall (lever the low-beta leg, delever the high-beta leg), rebalance monthly.  
⚠️ Original paper reports the strategy's return 'rivals those of all the standard asset pricing factors...in terms of economic magnitude, statistical significance and robustness,' per author framing -- but subsequent literature (e.g., 'Betting Against Betting Against Beta,' 'The Volatility Puzzle of the Beta Anomaly,' 2025) has challenged both the magnitude and the leverage-constraint explanation. Gross of costs; gross-leverage assumptions (using leverage to reach unit beta) are not costless in practice (financing/margin costs).

**[The Gross Profitability Premium](https://mysimon.rochester.edu/novy-marx/research/OSoV.pdf)** (2013)  
🔧 Only needs fundamentals (revenue, COGS, total assets) plus prices -- no text/news required. Compute gross profitability = (Revenue - COGS) / Total Assets per firm per fiscal year, rank cross-sectionally at each rebalance (typically annual, aligned to fiscal-year-end + reporting lag), go long top decile / short bottom decile, hold ~1 year (or blend with a monthly price-based tilt).  
⚠️ Seminal quality/profitability anchor; combines well with value (low P/B, high gross profitability = 'quality value'). Gross of costs, largely in-sample discovery period; profitability premium has been shown to decay/compress post-publication like most anomalies.

**[Do Stock Prices Fully Reflect Information in Accruals and Cash Flows About Future Earnings? (the accrual anomaly)](https://www.jstor.org/stable/248290)** (1996)  
🔧 Only needs fundamentals (net income, cash flow from operations, total assets) -- no prices needed for signal construction. Compute accruals = (Net Income - CFO) / Total Assets per firm-year, rank cross-sectionally at fiscal-year-end (with reporting lag), go long low-accrual decile / short high-accrual decile, hold ~1 year, rebalance annually.  
⚠️ Classic anchor anomaly; closely related to and partially subsumed by gross-profitability/quality factors in later literature (accruals and R&D both sit in the 'earnings vs. gross-profit wedge'). Gross of costs; well-documented decay since publication.

</details>

### Fundamental composites

| Year | Paper | Strategy | Reported return | Sharpe | Net of costs | OOS | Code |
|---|---|---|---|---|:-:|:-:|:-:|
| 2020 | [Value Investing Research: Simple Methods to Improve the Piotroski F-Score](https://alphaarchitect.com/value-investing-research-simple-methods-to-improve-the-piotroski-f-score/)<br><sub>Alpha Architect blog</sub> | Tests simple modifications to Piotroski's original 9-signal F-Score (profitability, leverage/liquidity, operating efficiency binary signals) to improve its ability to separate future winners from losers among cheap (high book-to-market) value stocks.<br><sub>US equities (value/high-B/M universe)</sub> | — | — | ❔ | ❔ |  |

<details><summary>How to recreate (1)</summary>

**[Value Investing Research: Simple Methods to Improve the Piotroski F-Score](https://alphaarchitect.com/value-investing-research-simple-methods-to-improve-the-piotroski-f-score/)** (2020)  
🔧 Requires standard fundamentals (ROA, change in ROA, CFO, CFO vs. net income, change in leverage, change in current ratio, share issuance, change in gross margin, change in asset turnover); compute the 9 binary signals, sum to a 0-9 F-Score, apply within a cheap-valuation (high B/M) universe, long high F-Score / short or avoid low F-Score.  
⚠️ F-Score is one of the cheapest-to-implement fundamental composites (needs only standard financial-statement line items, no text/news); best used as a quality overlay on a value screen rather than standalone, per the original Piotroski (2000) design, which is itself the seminal anchor for this factor family.

</details>

### Factor timing & crowding

| Year | Paper | Strategy | Reported return | Sharpe | Net of costs | OOS | Code |
|---|---|---|---|---|:-:|:-:|:-:|
| 2026 | [Measuring Strategy-Decay Risk: Minimum Regime Performance and the Durability of Systematic Investing](https://arxiv.org/pdf/2604.08356)<br><sub>arXiv:2604.08356</sub> | Introduces Minimum Regime Performance (MRP) -- the lowest realized risk-adjusted return of a strategy across historical market regimes -- as a robustness/durability metric to complement (and sometimes contradict) standard full-sample Sharpe ratio for systematic factor strategies.<br><sub>A broad universe of established factor strategies (specific factors not fully captured)</sub> | — | — | ❔ | ❔ | [↗](https://github.com/nolanalexander/minimum_regime_performance) |
| 2025 | [Machine Learning Enhanced Multi-Factor Quantitative Trading: A Cross-Sectional Portfolio Optimization Approach with Bias Correction](https://www.arxiv.org/pdf/2507.07107)<br><sub>arXiv:2507.07107 (q-fin.PM)</sub> | Combines multiple cross-sectional equity factors with a machine-learning bias-correction layer and portfolio optimization to size long-short positions.<br><sub>Not fully confirmed; test period reported as roughly 2021-2024</sub> | annualized return of about 20.4% cited in secondary search summaries for the 2021-2024 test window | Sharpe ratio around 2.01 cited for the same window | ❔ | ❔ |  |
| 2025 | [The Many Facets of Stock Momentum: Distinguishing Factor and Stock Components](https://www.tandfonline.com/doi/full/10.1080/0015198X.2025.2562790)<br><sub>Financial Analysts Journal</sub> | Decomposes stock momentum into a factor-momentum component and a residual stock-specific component internationally, testing whether Ehsani-Linnainmaa's 'factor momentum explains stock momentum' finding holds outside the US.<br><sub>International equity markets</sub> | — | — | ❔ | ❔ |  |
| 2025 | [Not All Factors Crowd Equally: Modeling, Measuring, and Trading on Alpha Decay](https://arxiv.org/abs/2512.11913)<br><sub>arXiv:2512.11913 (WITHDRAWN by author)</sub> | Proposed a hyperbolic alpha-decay model (alpha(t) = K/(1+lambda*t)) fit to eight Fama-French factors, and tested a crowding-based factor-selection strategy meant to trade on differential decay/crowding across factors.<br><sub>Eight Fama-French factors, 1963-2024</sub> | — | crowding-based factor-selection Sharpe of 0.22 vs. 0.39 for a plain factor-momentum benchmark; out-of-sample alpha of 0.30 vs. 0.15 reported in one specification; momentum showed 0.38x the crash probability of a 1.7-1.8x higher crash probability for crowded reversal strategies | ❔ | ✅ |  |
| 2024 | [Multi-Factor Timing with Deep Learning](https://doi.org/10.2139/ssrn.4698640)<br><sub>SSRN 4698640 / Journal of Financial Data Science</sub> | Uses a multi-task neural network (MT) to capture commonalities across six well-known equity factors (market, size, value, profitability, investment, momentum) and a dynamic multi-task network (DMT) to extract macro/financial 'states,' predicting the sign of each factor's next-month return from 272 inputs (123 macro + 149 financial) to time factor exposure.<br><sub>US equity factor portfolios, multi-decade sample (not fully specified)</sub> | — | — | ❔ | ❔ |  |
| 2024 | [Multifactor Timing with Deep Learning](https://academic.oup.com/jfec/article/24/3/nbag006/8658726)<br><sub>Journal of Financial Econometrics</sub> | Uses LSTMs to detect cycles/regimes and time five well-known factor portfolios (SMB, HML, RMW, CMA, MOM), exploiting the LSTM's ability to capture longer-memory macro-financial dynamics than simple linear timing rules.<br><sub>US equity factor portfolios, January 1965 - December 2021 (57 years)</sub> | — | — | ❔ | ❔ |  |
| 2024 | [Optimal Factor Timing in a High-Dimensional Setting](https://www.google.com/search?q=Lehnherr+Mehta+Nagel+Optimal+Factor+Timing+High-Dimensional)<br><sub>Working paper (NBER-affiliated authors)</sub> | Applies machine learning combined with mean-variance optimization to time a large number of equity factors simultaneously when both the number of factors and the number of candidate factor-timing predictors are large (a high-dimensional shrinkage/regularization problem).<br><sub>US equity factor zoo (many factors), period not fully captured</sub> | — | — | ❔ | ❔ |  |
| 2024 | [Dynamic Factor Allocation Leveraging Regime-Switching Signals](https://arxiv.org/pdf/2410.14841)<br><sub>arXiv q-fin</sub> | Dynamically allocates across equity style factors using explicit regime-switching signals (e.g., an HMM or similar regime-detection model) rather than continuous macro predictors.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2024 | [Sector Rotation by Factor Model and Fundamental Analysis](https://arxiv.org/pdf/2401.00001)<br><sub>arXiv q-fin</sub> | Combines a factor model with fundamental analysis to time sector rotation decisions (over/underweighting sectors) rather than individual stock selection.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2022 | [Is Factor Momentum More than Stock Momentum?](https://arxiv.org/abs/2009.04824)<br><sub>Journal of Finance (working paper version arXiv:2009.04824)</sub> | Shows that momentum in factor returns themselves (buying factors that have recently done well, shorting those that have done poorly) explains most forms of individual-stock momentum (standard momentum, industry momentum, industry-adjusted momentum), suggesting stock momentum is largely 'factor momentum in disguise.'<br><sub>US equity factor portfolios, multi-decade sample</sub> | — | — | ❔ | ❔ |  |

<details><summary>How to recreate (10)</summary>

**[Measuring Strategy-Decay Risk: Minimum Regime Performance and the Durability of Systematic Investing](https://arxiv.org/pdf/2604.08356)** (2026)  
🔧 Requires long factor-return histories spanning multiple identifiable macro regimes (e.g., dot-com, GFC, 2010s low-vol bull, 2022 rate-hike regime, current AI/mega-cap regime); split returns by regime, compute Sharpe within each, report the minimum across regimes as MRP, compare strategy rankings under MRP vs. full-sample Sharpe.  
⚠️ Key finding: strategies with higher long-run Sharpe ratios do not always have higher MRP -- i.e., some high-average-Sharpe factors are fragile in specific regimes. Directly useful methodology for stress-testing any of the momentum/value/quality signals in this list against a 2026 AI-mega-cap-concentration regime. Code is public on GitHub.

**[Machine Learning Enhanced Multi-Factor Quantitative Trading: A Cross-Sectional Portfolio Optimization Approach with Bias Correction](https://www.arxiv.org/pdf/2507.07107)** (2025)  
🔧 Requires daily prices plus a standard multi-factor characteristic panel (value, momentum, quality, etc.); fit an ML bias-correction model on factor scores, form long-short cross-sectional portfolio, rebalance periodically. Numbers here are from search snippets, not independently verified against the PDF body — re-confirm before use.  
⚠️ Could not extract full methodology/results section via automated fetch (PDF body did not render key results); treat reported 20.4%/Sharpe 2.01 as unverified pending a direct read of the paper.

**[The Many Facets of Stock Momentum: Distinguishing Factor and Stock Components](https://www.tandfonline.com/doi/full/10.1080/0015198X.2025.2562790)** (2025)  
🔧 Requires international factor-return panels plus stock-level momentum signals; decompose stock momentum returns into factor-momentum-explained and residual components via spanning regressions across countries.  
⚠️ Finds factor momentum exists internationally but fails to fully explain price or industry momentum outside specific markets -- a useful counterweight to the pure 'factor momentum subsumes stock momentum' narrative for a global/non-US-only interpretation.

**[Not All Factors Crowd Equally: Modeling, Measuring, and Trading on Alpha Decay](https://arxiv.org/abs/2512.11913)** (2025)  
🔧 Requires the eight Fama-French factor series (public data); fit hyperbolic/linear/exponential decay curves to each factor's rolling Sharpe or alpha over time, build a crowding proxy, and test whether avoiding/favoring crowded factors improves risk-adjusted return.  
⚠️ IMPORTANT CAVEAT: this paper was WITHDRAWN by the author, who states 'empirical validation in Sections 5-7 is insufficient to support global applicability claims.' The crowding-based strategy is explicitly reported to underperform (Sharpe 0.22) the simple factor-momentum benchmark (0.39), i.e., a negative result for the proposed approach -- do not use the specific numbers here as validated findings; included mainly as a cautionary data point on factor crowding/decay methodology.

**[Multi-Factor Timing with Deep Learning](https://doi.org/10.2139/ssrn.4698640)** (2024)  
🔧 Requires standard Fama-French-style factor return series plus a broad macro+financial predictor panel (272 series); train a multi-task network to predict next-month sign of each factor, tilt factor exposure (over/underweight) accordingly, rebalance monthly.  
⚠️ Feasible largely with public factor data (Ken French library) plus macro series (FRED); firm-level fundamentals/news not required. Exact backtest performance numbers not retrieved in this pass.

**[Multifactor Timing with Deep Learning](https://academic.oup.com/jfec/article/24/3/nbag006/8658726)** (2024)  
🔧 Requires the standard Fama-French five-factor series (public, Ken French data library) plus macro series; train an LSTM to detect regime/cycle and produce a factor-timing signal (over/underweight each factor), rebalance monthly, backtest over the 1965-2021 window with walk-forward splits.  
⚠️ By the same authors as 'Deep Learning in Asset Pricing'; directly reproducible with public Fama-French data, no proprietary fundamentals needed. Exact numeric performance not retrieved in this pass.

**[Optimal Factor Timing in a High-Dimensional Setting](https://www.google.com/search?q=Lehnherr+Mehta+Nagel+Optimal+Factor+Timing+High-Dimensional)** (2024)  
🔧 Requires a broad factor-return panel (dozens to hundreds of published factors, e.g., from an academic factor zoo replication like Chen-Zimmermann) plus a wide set of macro/financial timing predictors; apply regularized mean-variance factor timing (e.g., shrinkage estimators, machine-learning-based conditional expected-return models).  
⚠️ Exact URL/venue not fully confirmed in this pass (working paper, not yet pinned to a stable arXiv/SSRN id found); flagged for follow-up citation check.

**[Dynamic Factor Allocation Leveraging Regime-Switching Signals](https://arxiv.org/pdf/2410.14841)** (2024)  
🔧 Requires factor-return series plus a regime-switching model (e.g., Markov-switching or HMM) fit to macro/market-state variables; tilt factor weights based on the detected regime, rebalance monthly.  
⚠️ Title/abstract only; not independently verified in this pass.

**[Sector Rotation by Factor Model and Fundamental Analysis](https://arxiv.org/pdf/2401.00001)** (2024)  
🔧 Requires sector-level price and fundamental aggregates; build a factor-timing model that predicts sector-relative performance, rotate sector weights monthly/quarterly.  
⚠️ Title/abstract only; not independently verified in this pass.

**[Is Factor Momentum More than Stock Momentum?](https://arxiv.org/abs/2009.04824)** (2022)  
🔧 Requires a broad panel of factor return series (dozens of published anomaly/factor portfolios); compute each factor's own trailing momentum, form a factor-momentum long-short portfolio (long recently-winning factors, short recently-losing factors), compare its explanatory power for stock-level momentum via spanning regressions.  
⚠️ Influential but debated -- later work (2024-2025, e.g., Quoniam's 'Many Facets of Stock Momentum') finds factor momentum does not fully explain price/industry momentum internationally, suggesting the original US result may not generalize cleanly.

</details>

### Short interest & borrow

| Year | Paper | Strategy | Reported return | Sharpe | Net of costs | OOS | Code |
|---|---|---|---|---|:-:|:-:|:-:|
| 2025 | [Anomalies and Their Short-Sale Costs](https://onlinelibrary.wiley.com/doi/10.1111/jofi.13501)<br><sub>Journal of Finance, Vol. 80(6), pp. 3639-3694</sub> | Re-tests 162 published cross-sectional anomalies after adjusting the short leg's return for actual stock-borrow (loan) fees rather than assuming free shorting.<br><sub>US equities, borrow-fee data 2006-2019 (or similar; anomaly universe per original papers)</sub> | average long-short anomaly return is 0.14% per month before short-sale costs, but only -0.01% per month once adjusted for stock borrow fees; profits vanish even before fees if the ~12% of high-borrow-fee stock-days are excluded | — | ✅ | ❔ |  |
| 2019 | [The Loan Fee Anomaly: A Short Seller's Best Ideas](https://paperswithbacktest.com/strategies/the-loan-fee-anomaly-a-short-seller-s-best-ideas)<br><sub>SSRN / practitioner summary</sub> | Stocks with high (and rising) stock-loan/borrow fees are shorted by informed short sellers ('best ideas'); sorting stocks by borrow fee alone produces a stronger long-short return than sorting by 102 traditional anomaly signals.<br><sub>US equities, 2006-2019</sub> | portfolios formed on borrow fees provide larger long-short returns than portfolios formed on any of 102 compared anomalies over 2006-2019 | — | ❔ | ❔ |  |

<details><summary>How to recreate (2)</summary>

**[Anomalies and Their Short-Sale Costs](https://onlinelibrary.wiley.com/doi/10.1111/jofi.13501)** (2025)  
🔧 Requires published anomaly signals (value, momentum, quality, etc.) plus a stock-borrow-fee/loan-fee dataset (e.g., from a securities-lending data vendor). Compute standard long-short anomaly returns, then re-compute the short leg's realized return net of the contemporaneous borrow fee for each name/day.  
⚠️ Critical caveat paper for the entire anomaly literature: most published 'gross' long-short anomaly returns are not actually capturable once realistic borrow costs are included, especially in the crowded, hard-to-borrow small-cap short tail. Directly relevant to any long/short tech book -- shorting expensive-to-borrow names (e.g., heavily shorted momentum/growth names) can erase the anomaly's apparent edge.

**[The Loan Fee Anomaly: A Short Seller's Best Ideas](https://paperswithbacktest.com/strategies/the-loan-fee-anomaly-a-short-seller-s-best-ideas)** (2019)  
🔧 Requires a securities-lending/borrow-fee data feed by stock and date. Rank stocks by borrow fee level (and/or fee changes), short high-fee names, long low-fee names, rebalance monthly.  
⚠️ Because the strategy's own edge is proportional to borrow fee, the strategy is inherently expensive to implement at scale on the short side -- the 'anomaly' partly reflects the informed-shorting signal, not a free lunch; overlaps conceptually with the Muravyev et al. (2025) short-sale-cost paper above.

</details>

### Options-implied signals

| Year | Paper | Strategy | Reported return | Sharpe | Net of costs | OOS | Code |
|---|---|---|---|---|:-:|:-:|:-:|
| 2026 | [Option-Implied Signals and Crash Risk: Predictability and Machine-Learning Evidence from U.S. Equity Options, 2015-2026](https://arxiv.org/html/2608.26115)<br><sub>arXiv:2608.26115</sub> | Constructs a daily firm-level panel of six option-implied signals (volatility smirk, IV spread, risk-neutral skewness proxy, term-structure slope, put-call volume/OI ratios) and tests their next-month return and crash-risk predictability across three macro regimes (2015-2019 low-vol, 2020-2022 high-vol, 2023-2026 AI/mega-cap), comparing linear regressions to XGBoost.<br><sub>12.36 million US equity firm-day observations across 10,026 underlyings, 2015-2026</sub> | — | — | ❌ | ✅ |  |
| 2026 | [Skewness Dispersion and Stock Market Returns](https://arxiv.org/pdf/2604.07870)<br><sub>arXiv:2604.07870</sub> | Constructs a market-wide dispersion-of-individual-stock-skewness measure (cross-sectional spread of firm-level option-implied or realized skewness) as a proxy for investor disagreement about tail risk, and studies its relation to aggregate/individual stock returns.<br><sub>Not fully captured (likely US equities/options)</sub> | — | — | ❔ | ❔ |  |
| 2025 | [Why Does Options Market Information Predict Stock Returns?](https://www.sciencedirect.com/science/article/pii/S0304405X25001618)<br><sub>Journal of Financial Economics</sub> | Tests whether the well-known predictive power of options-implied signals (volatility spread/skew) for equity returns survives once accounting for stock borrow fees; argues implied-vol signals largely proxy for the same informed-shorting information captured directly by borrow fees.<br><sub>US equities with listed options</sub> | once stock borrow fees are accounted for, strategies exploiting options-market-implied signals via short selling are 'much closer to break-even' | — | ✅ | ❔ |  |
| 2023 | [Cross-Sectional Variation of Option-Implied Volatility Skew](https://pubsonline.informs.org/doi/10.1287/mnsc.2023.4872)<br><sub>Management Science</sub> | Documents systematic cross-sectional variation in equity option-implied volatility skew (OTM put IV minus ATM call IV) and links it to expected stock returns and firm characteristics.<br><sub>US equity options market</sub> | — | — | ❔ | ❔ |  |

<details><summary>How to recreate (4)</summary>

**[Option-Implied Signals and Crash Risk: Predictability and Machine-Learning Evidence from U.S. Equity Options, 2015-2026](https://arxiv.org/html/2608.26115)** (2026)  
🔧 Requires a full US equity options chain history (implied vols by strike/expiry, volume, open interest) plus daily equity prices, 2015-2026. Build the six option-implied features per name-day, run regime-split regressions and XGBoost, then form monthly-rebalanced long-short deciles per signal per regime.  
⚠️ Directly relevant and cautionary for a tech-heavy US long/short book: the classic vol-skew signal has weakened to statistical insignificance (and even reversed sign at longer horizons) in the recent 'AI/mega-cap concentration' regime (2023-2026), which is exactly the current market backdrop -- suggesting naive skew-based signals need regime-conditioning or should be de-weighted for mega-cap tech names today. No transaction costs modeled.

**[Skewness Dispersion and Stock Market Returns](https://arxiv.org/pdf/2604.07870)** (2026)  
🔧 Requires cross-sectional option-implied (or realized) skewness estimates per stock per day; compute the dispersion (e.g., cross-sectional std dev) of skewness across the universe each day/month as a market-timing or factor-conditioning signal.  
⚠️ Could not extract the empirical results section (PDF metadata only); flagged for a follow-up direct read before using any performance claim.

**[Why Does Options Market Information Predict Stock Returns?](https://www.sciencedirect.com/science/article/pii/S0304405X25001618)** (2025)  
🔧 Requires options data (implied vols by strike/maturity, put-call skew) plus stock borrow-fee data. Compute standard vol-spread/skew factor, form long-short portfolio, then recompute net of realized borrow fee for the short leg.  
⚠️ Directly ties the options-implied and short-interest literatures together; important caveat for any options-skew signal used in a long/short book -- gross backtest Sharpe from skew/vol-spread signals likely overstates net-of-borrow-cost performance.

**[Cross-Sectional Variation of Option-Implied Volatility Skew](https://pubsonline.informs.org/doi/10.1287/mnsc.2023.4872)** (2023)  
🔧 Requires listed-options implied-vol surfaces by underlying/date; compute the OTM-put-vs-ATM-call skew per name per day, sort into deciles, form a long-short equity portfolio (short high negative skew / long low skew, or vice versa per the paper's sign convention), rebalance monthly.  
⚠️ Seminal-ish anchor for the options-skew-predicts-returns literature; see Muravyev et al. and the JFE 2025 paper above for the borrow-fee counter-evidence.

</details>

### Intraday & overnight

| Year | Paper | Strategy | Reported return | Sharpe | Net of costs | OOS | Code |
|---|---|---|---|---|:-:|:-:|:-:|
| 2025 | [Does Overnight News Explain Overnight Returns?](https://arxiv.org/abs/2507.04481)<br><sub>arXiv:2507.04481</sub> | Applies supervised topic modeling to 2.4 million news articles to identify which news topics are associated with abnormal overnight (close-to-open) versus intraday (open-to-close) returns, and uses topic prevalence/response differences to forecast which stocks will do well overnight and poorly intraday (or vice versa).<br><sub>US equities, roughly 30-year sample of news and returns</sub> | — | — | ❔ | ✅ |  |
| 2024 | [Reversals and the Returns to Liquidity Provision](https://www.nber.org/papers/w30917)<br><sub>Financial Analysts Journal 80(2), pp. 122-151 (NBER WP 30917)</sub> | Uses short-term price reversals to measure the returns earned by liquidity providers, showing reversal strength/persistence scales with size (smaller = stronger), volatility (higher = stronger) and inverse turnover (lower turnover = more persistent), consistent with reversal being compensation for market-making risk rather than a free-standing mispricing.<br><sub>US equities, multi-decade CRSP sample</sub> | — | — | ❔ | ❔ |  |
| 2022 | [They Still Haven't Told You: An Analysis of the Overnight/Intraday Anomaly's Robustness](https://arxiv.org/pdf/2201.00223)<br><sub>arXiv q-fin</sub> | Further scrutiny of the overnight/intraday return decomposition, examining robustness/explanations for why overnight returns dominate cumulative equity performance.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2020 | [Strikingly Suspicious Overnight and Intraday Returns](https://arxiv.org/pdf/2010.01727)<br><sub>arXiv q-fin</sub> | Documents that a large, often near-monotonic fraction of long-run US equity index (and many single-stock) returns is earned overnight (close-to-open) rather than intraday (open-to-close), and questions the stability/causes of this pattern.<br><sub>US equities/indices, multi-decade</sub> | over a recent 5-year window (Q3 2020-Q3 2025, per secondary sources), SPY close-to-open return was about +47.1% vs. +29.9% open-to-close; QQQ close-to-open was about +53.5% vs. +30.3% open-to-close | — | ❌ | ❔ |  |

<details><summary>How to recreate (4)</summary>

**[Does Overnight News Explain Overnight Returns?](https://arxiv.org/abs/2507.04481)** (2025)  
🔧 Requires a large historical news corpus plus split overnight/intraday return series. Fit supervised topic models (e.g., seeded LDA or an LLM-based topic classifier) to link topics to return components, then form a daily long-short overnight-return-forecast portfolio entering near the close and exiting at the next open.  
⚠️ Confirms and extends a long literature (Lou-Polk-Skouras 'Tug of War', NY Fed 'Overnight Drift') documenting that most US equity index gains accrue overnight rather than intraday; a standard news + price feed could reproduce the topic-modeling approach, though exact performance figures were not retrievable from the abstract alone.

**[Reversals and the Returns to Liquidity Provision](https://www.nber.org/papers/w30917)** (2024)  
🔧 Requires daily prices, volume/turnover and market-cap data (fundamentals not needed). Sort stocks by prior-day/week return within size/volatility/turnover buckets, go long recent losers / short recent winners (classic short-term reversal), and examine how the reversal's magnitude interacts with the three characteristics.  
⚠️ Reframes the classic short-term-reversal anomaly as compensation for bearing inventory risk as a liquidity provider -- implies realistic implementation must account for the same market-making costs (bid-ask spread, adverse selection) that generate the 'anomaly' in the first place, so gross backtest returns likely substantially overstate net edge for an outside participant.

**[They Still Haven't Told You: An Analysis of the Overnight/Intraday Anomaly's Robustness](https://arxiv.org/pdf/2201.00223)** (2022)  
🔧 Same OHLC-only recreation as the overnight/intraday papers above.  
⚠️ Title/abstract only; included for category completeness.

**[Strikingly Suspicious Overnight and Intraday Returns](https://arxiv.org/pdf/2010.01727)** (2020)  
🔧 Only needs daily open/close/prior-close prices (no fundamentals or text). Compute close-to-open and open-to-close return series per name/index, compare cumulative performance, and construct a strategy that holds overnight and is flat/hedged intraday (or the reverse) to isolate the effect.  
⚠️ One of the most directly and cheaply implementable anomalies on this list (needs only OHLC prices), but it is extremely well known and crowded by 2026; net-of-cost edge for a pure overnight-hold strategy on liquid large-caps is likely thin given borrow/financing costs of holding overnight and the well-documented decay of such 'anomalies' once publicized.

</details>

### Statistical arbitrage

| Year | Paper | Strategy | Reported return | Sharpe | Net of costs | OOS | Code |
|---|---|---|---|---|:-:|:-:|:-:|
| 2026 | [Moira: Language-Driven Hierarchical Reinforcement Learning for Pair Trading](https://arxiv.org/pdf/2605.01954)<br><sub>arXiv q-fin</sub> | Uses natural-language (LLM-derived) guidance to inform a hierarchical RL pair-trading policy -- e.g., using LLM-parsed news/fundamentals to influence pair selection or regime detection within the RL hierarchy.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2024 | [Statistical Arbitrage in Multi-Pair Trading Strategy Based on Graph Clustering Algorithms in US Equities Market](https://arxiv.org/html/2406.10695v1)<br><sub>arXiv q-fin</sub> | Uses graph-clustering algorithms (rather than pairwise correlation/cointegration search) to identify groups of related US equities for a multi-pair statistical-arbitrage strategy, trading mean-reversion within/between clusters.<br><sub>US equities</sub> | — | — | ❔ | ❔ |  |
| 2024 | [Reinforcement Learning Pair Trading: A Dynamic Scaling Approach](https://arxiv.org/html/2407.16103v1)<br><sub>arXiv q-fin</sub> | RL agent learns to dynamically scale position size in a pairs-trading strategy (rather than using fixed z-score entry/exit thresholds), adapting exposure to the current spread regime.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2024 | [Advanced Statistical Arbitrage with Reinforcement Learning](https://arxiv.org/pdf/2403.12180)<br><sub>arXiv q-fin</sub> | General RL-based framework for statistical arbitrage, likely combining signal generation and execution/sizing within an RL policy.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2023 | [Select and Trade: Towards Unified Pair Trading with Hierarchical Reinforcement Learning](https://arxiv.org/pdf/2301.10724)<br><sub>arXiv q-fin</sub> | Hierarchical RL framework that jointly handles pair selection (which stocks to pair) and trade execution (when/how much to trade the spread) in a single unified pipeline, rather than treating selection and trading as separate stages.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2022 | [Detecting Data-Driven Robust Statistical Arbitrage Strategies with Deep Neural Networks](https://arxiv.org/html/2203.03179)<br><sub>arXiv q-fin</sub> | Uses a deep neural network to identify robust statistical-arbitrage strategies across multiple securities simultaneously, without requiring explicit pairwise cointegration testing.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |

<details><summary>How to recreate (6)</summary>

**[Moira: Language-Driven Hierarchical Reinforcement Learning for Pair Trading](https://arxiv.org/pdf/2605.01954)** (2026)  
🔧 Requires daily price data plus a news/text feed; use an LLM to extract features/context that condition a hierarchical RL pair-selection-and-trading policy.  
⚠️ Title/abstract only; not independently verified in this pass -- notable as one of the few papers blending LLM text signals directly into a stat-arb/pairs framework.

**[Statistical Arbitrage in Multi-Pair Trading Strategy Based on Graph Clustering Algorithms in US Equities Market](https://arxiv.org/html/2406.10695v1)** (2024)  
🔧 Requires daily price/return data for a broad US equity universe; build a correlation/co-movement graph, cluster via a graph algorithm (e.g., Louvain community detection), form pairs/baskets within clusters, trade mean-reversion of the spread (z-score entry/exit rules), rebalance/rebuild clusters periodically.  
⚠️ Directly implementable with daily prices alone (no fundamentals/news needed) -- one of the more turnkey stat-arb approaches on this list for a tech-heavy long/short book, since large tech/semis clusters are a natural fit for graph-based pair discovery.

**[Reinforcement Learning Pair Trading: A Dynamic Scaling Approach](https://arxiv.org/html/2407.16103v1)** (2024)  
🔧 Requires a cointegrated pair's spread history; train an RL agent (e.g., DQN/PPO) whose action is position size (not just binary long/short) as a function of the current spread z-score and recent spread volatility.  
⚠️ Title/abstract only; not independently verified in this pass.

**[Advanced Statistical Arbitrage with Reinforcement Learning](https://arxiv.org/pdf/2403.12180)** (2024)  
🔧 Requires daily multi-asset price data; construct a stat-arb feature set (spreads, z-scores across candidate pairs/baskets), train an RL agent to trade the resulting mean-reversion signals.  
⚠️ Title/abstract only; not independently verified in this pass.

**[Select and Trade: Towards Unified Pair Trading with Hierarchical Reinforcement Learning](https://arxiv.org/pdf/2301.10724)** (2023)  
🔧 Requires daily price history for a broad equity universe; a high-level RL policy selects candidate pairs (from correlation/cointegration/co-movement features), a low-level RL policy executes the spread-trading decision, trained jointly or in alternation.  
⚠️ Title/abstract only; not independently verified in this pass.

**[Detecting Data-Driven Robust Statistical Arbitrage Strategies with Deep Neural Networks](https://arxiv.org/html/2203.03179)** (2022)  
🔧 Requires multi-asset daily price history; train a neural network to directly output a statistical-arbitrage trading strategy (portfolio weights over time) optimized for a robust arbitrage-style objective, rather than first testing pairwise cointegration.  
⚠️ Title/abstract only; not independently verified in this pass.

</details>

### ML return prediction

| Year | Paper | Strategy | Reported return | Sharpe | Net of costs | OOS | Code |
|---|---|---|---|---|:-:|:-:|:-:|
| 2026 | [Adaptive Financial Transformer with Regime-Gated Attention for Stock Return Prediction](https://arxiv.org/pdf/2606.29347)<br><sub>arXiv q-fin</sub> | Transformer architecture whose attention mechanism is gated by a detected market regime, aiming to adapt cross-sectional return-prediction behavior to bull/bear/high-vol/low-vol conditions.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2026 | [Vector-Quantized Discrete Latent Factors Meet Financial Priors: Dynamic Cross-Sectional Stock Ranking Prediction for Portfolio Construction](https://arxiv.org/pdf/2605.13407)<br><sub>arXiv q-fin</sub> | Uses vector-quantized (discrete) latent factor representations, combined with financial-domain priors, to produce a dynamic cross-sectional stock ranking used for portfolio construction.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2026 | [From Index to Equity: Pre-Training Transformers for Stock Return Prediction](https://arxiv.org/pdf/2605.23962)<br><sub>arXiv q-fin</sub> | Pre-trains a transformer on index-level (aggregate) return data before fine-tuning on individual-equity return prediction, aiming to transfer broad market-dynamics knowledge to the harder single-stock prediction task.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2026 | [A Hybrid LSTM-XGBoost Framework for Multi-Horizon Stock Return Prediction Across Diversified Equity Portfolios](https://arxiv.org/html/2609.13125)<br><sub>arXiv q-fin</sub> | Two-stage model: an LSTM captures sequential/temporal dynamics, whose output feeds an XGBoost gradient-boosted regressor for the final multi-horizon return prediction, tested on a diversified panel of 14 US equities across six sectors.<br><sub>14 US equities across six industry sectors</sub> | — | — | ❔ | ❔ |  |
| 2025 | [Interpretable Deep Learning for Stock Returns](https://arxiv.org/pdf/2512.16251v2)<br><sub>arXiv q-fin</sub> | Concept-bottleneck deep-learning framework that forces the model to route through human-interpretable intermediate 'concepts' (synthesized predictors) before producing a cross-sectional return forecast, aiming to combine deep-learning power with interpretability, particularly for long-horizon predictions.<br><sub>US equities, not fully specified</sub> | — | — | ❔ | ❔ |  |
| 2025 | [On Evaluating Loss Functions for Stock Ranking: An Empirical Analysis With Transformer Model](https://arxiv.org/html/2510.14156v1)<br><sub>arXiv q-fin</sub> | Empirically compares different loss functions (pointwise regression vs. pairwise/listwise ranking losses) for training a transformer to rank stocks cross-sectionally, relevant to portfolio-construction-oriented (rather than pure return-forecast) model training.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2025 | [Gradient Boosting Decision Tree with LSTM for Investment Prediction](https://arxiv.org/html/2505.23084v1)<br><sub>arXiv q-fin</sub> | Combines gradient-boosted decision trees with an LSTM component for investment-return prediction, similar in spirit to the LSTM-XGBoost hybrid above.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2024 | [One Factor to Bind the Cross-Section of Returns](https://arxiv.org/pdf/2404.08129)<br><sub>arXiv q-fin</sub> | Proposes a single learned nonlinear factor (via machine learning on firm characteristics) that spans/explains cross-sectional stock return variation better than standard multi-factor benchmarks.<br><sub>US equities (exact sample period not captured)</sub> | — | — | ❔ | ❔ |  |
| 2024 | [SARF: Enhancing Stock Market Prediction with Sentiment-Augmented Random Forest](https://arxiv.org/pdf/2410.07143)<br><sub>arXiv q-fin</sub> | Random-forest stock-prediction model augmented with sentiment features (likely from news/social text) alongside standard price/technical features.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2023 | [Deep Learning in Asset Pricing](https://arxiv.org/abs/1904.00745)<br><sub>Management Science</sub> | Conditional-autoencoder deep neural network estimates a nonlinear, time-varying asset pricing (SDF) model for individual stock returns using firm characteristics and macro conditioning variables, trained with a no-arbitrage / pricing-error objective and adversarially-constructed test portfolios.<br><sub>US equities, CRSP sample spanning multiple decades</sub> | — | outperforms benchmark factor models out-of-sample on Sharpe ratio of the mean-variance efficient factor portfolio, explained variation, and pricing errors (exact numeric Sharpe not captured in this pass) | ❌ | ✅ |  |
| 2020 | [Empirical Asset Pricing via Machine Learning](https://academic.oup.com/rfs/article/33/5/2223/5758276)<br><sub>Review of Financial Studies (NBER WP 25398)</sub> | Compares linear, penalized linear, PCR/PLS, boosted trees, random forests and neural networks for predicting individual US stock returns from ~900 firm-characteristic/macro interaction predictors; builds long-short decile portfolios sorted on each model's fitted return.<br><sub>US equities, 1957-2016 (out-of-sample tests from 1987)</sub> | — | — | ❌ | ✅ |  |

<details><summary>How to recreate (11)</summary>

**[Adaptive Financial Transformer with Regime-Gated Attention for Stock Return Prediction](https://arxiv.org/pdf/2606.29347)** (2026)  
🔧 Requires a firm-characteristics/price panel plus a regime classifier (e.g., HMM or simple vol-based regime label); condition the transformer's attention gating on the regime label, train/test with walk-forward regime coverage.  
⚠️ Title/abstract only; not independently verified in this pass.

**[Vector-Quantized Discrete Latent Factors Meet Financial Priors: Dynamic Cross-Sectional Stock Ranking Prediction for Portfolio Construction](https://arxiv.org/pdf/2605.13407)** (2026)  
🔧 Requires a firm-characteristics/price panel; implement a VQ-VAE-style discrete latent-factor model with financial-prior regularization, rank stocks by predicted latent-factor exposure, form long-short portfolio.  
⚠️ Title/abstract only; not independently verified in this pass.

**[From Index to Equity: Pre-Training Transformers for Stock Return Prediction](https://arxiv.org/pdf/2605.23962)** (2026)  
🔧 Requires both index-level and single-stock price/characteristics data; pre-train on the (larger, cleaner) index-level series, fine-tune on the individual-stock cross-section, compare to training from scratch.  
⚠️ Title/abstract only; not independently verified in this pass.

**[A Hybrid LSTM-XGBoost Framework for Multi-Horizon Stock Return Prediction Across Diversified Equity Portfolios](https://arxiv.org/html/2609.13125)** (2026)  
🔧 Requires daily OHLCV for the target names; train the LSTM feature extractor, feed its hidden representation (or forecast) as an additional input to XGBoost, predict returns at multiple horizons (e.g., 1d/5d/20d), backtest a simple long/short or long-only rule per horizon.  
⚠️ Very small universe (14 names); more a methodology demonstration than a scalable strategy claim. No cost/Sharpe figures retrieved.

**[Interpretable Deep Learning for Stock Returns](https://arxiv.org/pdf/2512.16251v2)** (2025)  
🔧 Requires a firm-characteristics panel; implement a concept-bottleneck architecture (characteristics -> interpretable concept layer -> return forecast), compare long-horizon (e.g., 1-year) return prediction R2/decile spread vs. a standard black-box neural net.  
⚠️ Interpretability-focused variant of Gu-Kelly-Xiu-style ML prediction; exact performance numbers not retrieved in this pass.

**[On Evaluating Loss Functions for Stock Ranking: An Empirical Analysis With Transformer Model](https://arxiv.org/html/2510.14156v1)** (2025)  
🔧 Requires a firm-characteristics/price panel; train the same transformer architecture under different loss functions (MSE, pairwise ranking loss, listwise loss like ListMLE), compare resulting long-short portfolio performance.  
⚠️ Useful methodological reference for how loss-function choice (not just architecture) affects the practical long-short performance of an ML stock-ranking model.

**[Gradient Boosting Decision Tree with LSTM for Investment Prediction](https://arxiv.org/html/2505.23084v1)** (2025)  
🔧 Same general recreation pattern as the LSTM-XGBoost hybrid paper.  
⚠️ Title/abstract only; not independently verified in this pass.

**[One Factor to Bind the Cross-Section of Returns](https://arxiv.org/pdf/2404.08129)** (2024)  
🔧 Not independently verified beyond title/abstract; would need firm characteristics panel + nonlinear factor-extraction model (e.g., autoencoder or IPCA) trained on returns and characteristics, tested out-of-sample by decade.  
⚠️ Included for category completeness; details not independently confirmed — treat as a lead to re-check the full text before relying on it.

**[SARF: Enhancing Stock Market Prediction with Sentiment-Augmented Random Forest](https://arxiv.org/pdf/2410.07143)** (2024)  
🔧 Requires price/technical features plus a sentiment score feed; train a random forest classifier/regressor combining both feature sets, compare to price-only baseline.  
⚠️ Title/abstract only; not independently verified in this pass.

**[Deep Learning in Asset Pricing](https://arxiv.org/abs/1904.00745)** (2023)  
🔧 Requires firm-characteristics panel + macro series + returns; implement a conditional autoencoder (characteristics -> latent factor loadings, and factors themselves estimated from returns) trained via a no-arbitrage loss. Feasible only with a rich fundamentals+macro dataset, not prices alone.  
⚠️ Highly cited but methodologically complex; identifies price trend, liquidity and value as top firm characteristics driving the learned factors. Academic backtest, not live/cost-adjusted.

**[Empirical Asset Pricing via Machine Learning](https://academic.oup.com/rfs/article/33/5/2223/5758276)** (2020)  
🔧 Needs a broad firm-characteristics panel (~94 characteristics x macro interactions) plus monthly returns (e.g., CRSP + Compustat equivalent, or a proprietary fundamentals+prices feed like Massive). Standard pipeline: expanding-window training, refit annually, rank-sort predicted returns into deciles, long top/short bottom.  
⚠️ Landmark ML-in-finance paper; R2 numbers are tiny in absolute terms (predictability is real but weak) — long-short portfolio Sharpe gains come from ranking, not point-forecast accuracy. Gross of costs.

</details>

### LLM signals

| Year | Paper | Strategy | Reported return | Sharpe | Net of costs | OOS | Code |
|---|---|---|---|---|:-:|:-:|:-:|
| 2026 | [Adversarial News and Lost Profits: Manipulating Headlines in LLM-Driven Algorithmic Trading](https://arxiv.org/html/2601.13082v1)<br><sub>arXiv q-fin</sub> | Studies adversarial manipulation of news headlines to fool LLM-driven trading systems, and separately reports a baseline LLM-integrated trading system's cumulative return during a testing period, arguing sentiment signals from financial LLMs add non-redundant predictive information.<br><sub>Not captured</sub> | cumulative return of 19.22% during the (unspecified) testing period for the baseline LLM-integrated trading system | — | ❔ | ❔ |  |
| 2026 | [Impact of LLM News Sentiment Analysis on Stock Price Movement Prediction](https://arxiv.org/html/2602.00086v1)<br><sub>arXiv q-fin</sub> | Examines LLM-based news sentiment analysis for five large-cap tech names (Microsoft, Amazon, Apple, Netflix, Tesla) using over 96,000 news articles through March 2025, testing sentiment's ability to predict stock price movement.<br><sub>MSFT, AMZN, AAPL, NFLX, TSLA, through March 2, 2025</sub> | — | — | ❔ | ❔ |  |
| 2026 | [A Review of Large Language Models for Stock Price Forecasting from a Hedge-Fund Perspective](https://arxiv.org/pdf/2605.05211)<br><sub>arXiv q-fin (IEEE CAI 2026)</sub> | Survey specifically framed around practical hedge-fund use of LLMs for stock forecasting -- sentiment extraction from news, financial-report/earnings-call analysis, and multi-agent trading systems.<br><sub>N/A (survey)</sub> | — | — | ❔ | ❔ |  |
| 2025 | [FinDPO: Financial Sentiment Analysis for Algorithmic Trading through Preference Optimization of LLMs](https://arxiv.org/abs/2507.18417)<br><sub>arXiv:2507.18417</sub> | Fine-tune an LLM with Direct Preference Optimization (DPO) on financial sentiment data, then convert its discrete sentiment predictions into continuous, rankable scores ('logit-to-score') to drive a sentiment-based long-short trading strategy.<br><sub>Not fully specified in abstract</sub> | 67% annualized return | 2.0 | ✅ | ✅ |  |
| 2025 | [Sentiment-Aware Stock Price Prediction with Transformer and LLM-Generated Formulaic Alpha](https://arxiv.org/html/2508.04975v1)<br><sub>arXiv q-fin</sub> | Uses an LLM to generate adaptive formulaic alphas from historical price/technical/sentiment features, which then feed a Transformer model that predicts next-day stock prices.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2025 | [Event-Aware Sentiment Factors from LLM-Augmented Financial Tweets: A Transparent Framework for Interpretable Quant Trading](https://arxiv.org/html/2508.07408v1)<br><sub>arXiv q-fin</sub> | Constructs event-aware sentiment factors from financial tweets/social media using LLM augmentation, emphasizing an interpretable/transparent factor-construction pipeline rather than an opaque end-to-end model.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2025 | [Backtesting Sentiment Signals for Trading: Evaluating the Viability of Alpha Generation from Sentiment Analysis](https://arxiv.org/pdf/2507.03350)<br><sub>arXiv q-fin</sub> | Meta-analysis/backtesting study specifically evaluating whether sentiment-analysis-derived signals actually generate viable alpha once tested rigorously (as opposed to just being statistically significant in-sample).<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2025 | [Exploring the Synergy of Quantitative Factors and Newsflow Representations from Large Language Models for Stock Return Prediction](https://arxiv.org/pdf/2510.15691)<br><sub>arXiv q-fin</sub> | Combines traditional quantitative factors with LLM-derived newsflow representations, testing whether the two are complementary (synergistic) for stock return prediction rather than redundant.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2025 | [Large Language Models and Futures Price Factors in China](https://arxiv.org/pdf/2509.23609)<br><sub>arXiv:2509.23609</sub> | Uses LLMs (GPT-class models) to construct pricing factors for Chinese commodity/financial futures markets, an application of the LLM-factor-mining paradigm outside single-name equities.<br><sub>Chinese futures markets</sub> | — | — | ❔ | ❔ |  |
| 2024 | [Sentiment Trading with Large Language Models](https://arxiv.org/abs/2412.19245)<br><sub>Finance Research Letters, Vol. 62, 105227 (arXiv:2412.19245)</sub> | Compare BERT, an OPT/GPT-3-class LLM, FinBERT, and the Loughran-McDonald dictionary for classifying sentiment in news articles; form daily long-short portfolios on the resulting sentiment scores and predict next-day returns.<br><sub>965,375 news articles, January 2010 - June 2023, US stocks</sub> | — | long-short strategy Sharpe ratios: OPT 3.05, BERT 2.11, FinBERT 2.07, Loughran-McDonald dictionary 1.23 | ❌ | ❔ |  |
| 2024 | [Financial Statement Analysis with Large Language Models](https://arxiv.org/abs/2407.17866)<br><sub>arXiv:2407.17866 (working paper, University of Chicago Booth)</sub> | Give GPT-4 standardized, anonymized financial statements (no narrative/industry context) and ask it to predict the direction of future earnings changes; use GPT's predictions to form a long-short trading strategy and compare to human analysts and a narrow ML model.<br><sub>Not verifiable (paper withdrawn)</sub> | — | originally claimed a higher Sharpe ratio and alpha than analyst- or ML-based strategies; not verifiable | ❔ | ❔ |  |
| 2024 | [Fine-Tuning Large Language Models for Stock Return Prediction Using Newsflow](https://arxiv.org/pdf/2407.18103)<br><sub>arXiv q-fin</sub> | Fine-tunes an LLM (rather than using zero-shot prompting) on historical newsflow paired with realized returns to directly predict stock return direction/magnitude.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2023 | [Can ChatGPT Forecast Stock Price Movements? Return Predictability and Large Language Models](https://arxiv.org/abs/2304.07619)<br><sub>arXiv:2304.07619 / SSRN</sub> | Feed news headlines to GPT and other LLMs, prompting a good/bad/unclear sentiment classification for the stock's price; aggregate into a numeric daily 'ChatGPT score' per stock and go long high-score / short low-score names.<br><sub>US equities, news headlines through 2023 (with a post-training-cutoff subsample used as an out-of-sample test)</sub> | — | — | ❌ | ✅ |  |

<details><summary>How to recreate (13)</summary>

**[Adversarial News and Lost Profits: Manipulating Headlines in LLM-Driven Algorithmic Trading](https://arxiv.org/html/2601.13082v1)** (2026)  
🔧 Requires a news feed and an LLM sentiment-classification pipeline feeding a trading rule; the adversarial component additionally requires generating/testing manipulated headline variants to probe robustness.  
⚠️ Primarily a security/robustness paper (highlighting that LLM trading systems can be manipulated via crafted headlines) -- the 19.22% baseline return is incidental context, not the paper's main contribution, and period/universe were not confirmed.

**[Impact of LLM News Sentiment Analysis on Stock Price Movement Prediction](https://arxiv.org/html/2602.00086v1)** (2026)  
🔧 Requires a news feed (e.g., via AlphaVantage or similar) for the target mega-cap tech names plus daily prices; score each article's sentiment via an LLM, aggregate to a daily score per name, test predictive power for next-day price movement direction.  
⚠️ Directly relevant universe (mega-cap tech) for a tech-heavy long/short book, but the paper covers only 5 names -- too narrow to draw a diversified factor conclusion; treat as a proof-of-concept rather than a scalable strategy.

**[A Review of Large Language Models for Stock Price Forecasting from a Hedge-Fund Perspective](https://arxiv.org/pdf/2605.05211)** (2026)  
🔧 N/A -- survey paper.  
⚠️ Useful practitioner-oriented framing/checklist reference rather than a standalone empirical result.

**[FinDPO: Financial Sentiment Analysis for Algorithmic Trading through Preference Optimization of LLMs](https://arxiv.org/abs/2507.18417)** (2025)  
🔧 Needs labeled financial sentiment text data to fine-tune via DPO, plus a news/text feed at inference time. Convert model logits to a continuous score, rank stocks daily, form long-short portfolio, apply ~5bps assumed transaction costs. DPO fine-tuning requires ML infra beyond a pure signals pipeline.  
⚠️ Reported 5bps costs are a modeling assumption, not measured live costs; 67%/Sharpe 2.0 is a backtest figure and should be treated as an upper bound given typical alpha decay for sentiment strategies once crowded.

**[Sentiment-Aware Stock Price Prediction with Transformer and LLM-Generated Formulaic Alpha](https://arxiv.org/html/2508.04975v1)** (2025)  
🔧 Requires price/technical data plus a sentiment feed; use an LLM to propose formulaic alpha combinations (similar to AlphaGen's operator search but LLM-driven rather than RL-driven), feed the resulting alpha values into a Transformer for final next-day price/return prediction.  
⚠️ Title/abstract only; not independently verified in this pass.

**[Event-Aware Sentiment Factors from LLM-Augmented Financial Tweets: A Transparent Framework for Interpretable Quant Trading](https://arxiv.org/html/2508.07408v1)** (2025)  
🔧 Requires a financial-tweet/social-media feed; use an LLM to tag tweets with event types and sentiment, aggregate into a per-stock daily factor, form long-short deciles, rebalance daily.  
⚠️ Title/abstract only; not independently verified in this pass. Twitter/social data may not be part of a standard price + fundamentals + news feed -- would need a separate social-data source.

**[Backtesting Sentiment Signals for Trading: Evaluating the Viability of Alpha Generation from Sentiment Analysis](https://arxiv.org/pdf/2507.03350)** (2025)  
🔧 Requires a sentiment-scoring pipeline and price data; apply rigorous backtesting standards (walk-forward, cost-adjustment, multiple-testing correction) to sentiment-derived signals rather than a single in-sample test.  
⚠️ Useful as a methodological check on the many optimistic sentiment-trading papers in this list -- worth reading in full before trusting any single sentiment-Sharpe number reported elsewhere.

**[Exploring the Synergy of Quantitative Factors and Newsflow Representations from Large Language Models for Stock Return Prediction](https://arxiv.org/pdf/2510.15691)** (2025)  
🔧 Requires a standard factor panel (value/momentum/quality/etc.) plus a news feed; generate LLM embeddings of newsflow, combine with factor scores in a joint prediction model (e.g., gradient boosting or a small neural net), compare combined vs. factor-only vs. news-only performance.  
⚠️ Directly relevant design pattern for a Massive-data-based book: combining a classic multi-factor panel with LLM-derived news embeddings is likely to be one of the more promising near-term directions given the broader literature's finding that text adds incremental (non-redundant) information over numeric factors alone.

**[Large Language Models and Futures Price Factors in China](https://arxiv.org/pdf/2509.23609)** (2025)  
🔧 Requires Chinese futures price/fundamental data; use an LLM to propose/evaluate candidate pricing factors (similar in spirit to AlphaGen/AlphaAgent but for futures rather than equities), backtest resulting factors.  
⚠️ Not directly applicable to a US tech-equity book, but the LLM-factor-construction methodology is transferable across asset classes.

**[Sentiment Trading with Large Language Models](https://arxiv.org/abs/2412.19245)** (2024)  
🔧 Needs a large historical news-article corpus timestamped to publication plus daily prices. Score each article's sentiment with an LLM, aggregate to a daily per-stock score, sort into long-short deciles, rebalance daily/next-day-open. Feasible with a standard news feed plus any off-the-shelf or fine-tuned LLM/FinBERT.  
⚠️ No transaction costs, no explicit out-of-sample split described, and no discussion of the LLM's training-data cutoff relative to the 2010-2023 news sample — meaning some of the underlying LLM (OPT/BERT) may have been pretrained on data overlapping the test period, a look-ahead risk common to LLM finance papers. Sharpe ratios this high for a pure sentiment factor should be treated with caution pending independent replication.

**[Financial Statement Analysis with Large Language Models](https://arxiv.org/abs/2407.17866)** (2024)  
🔧 Conceptually: feed structured financial-statement line items (no text) to an LLM with a fixed prompt asking for earnings-direction forecasts, backtest a portfolio long predicted-up / short predicted-down firms. Requires only fundamentals data, no news/text needed.  
⚠️ IMPORTANT CAVEAT: this widely-cited paper was formally withdrawn from arXiv by the authors after a co-author found data/analysis inconsistencies while attempting to replicate it ('we have temporarily withdrawn the working paper from circulation while we review the research findings'). Do not rely on the originally-reported GPT-4-beats-analysts numbers without independent verification; treat as a cautionary example of the LLM-finance replication crisis.

**[Fine-Tuning Large Language Models for Stock Return Prediction Using Newsflow](https://arxiv.org/pdf/2407.18103)** (2024)  
🔧 Requires a large historical news corpus matched to subsequent returns for supervised fine-tuning; fine-tune an open LLM on this task, then apply to new/held-out news for a return-prediction signal.  
⚠️ Title/abstract only; not independently verified in this pass. Fine-tuning approach (vs. zero-shot ChatGPT scoring) is a meaningfully different and likely more robust design than the original Lopez-Lira/Tang zero-shot approach.

**[Can ChatGPT Forecast Stock Price Movements? Return Predictability and Large Language Models](https://arxiv.org/abs/2304.07619)** (2023)  
🔧 Needs a timestamped news-headline feed plus daily prices. Prompt an LLM per headline for a -1/0/+1 sentiment score, aggregate scores per stock per day, form daily long-short decile portfolios on the score, hold 1 day (or a few days for the drift component). Directly implementable with a standard news + price feed.  
⚠️ Landmark paper showing LLM sentiment has real short-horizon predictive power, but by the authors' own account, publicizing the signal erodes it ('returns decline as adoption rises') — a live LLM-based headline strategy in 2026 should expect materially decayed edge versus 2023 figures. No cost-adjustment; hit-rate/day, not $ return.

</details>

### LLM trading agents

| Year | Paper | Strategy | Reported return | Sharpe | Net of costs | OOS | Code |
|---|---|---|---|---|:-:|:-:|:-:|
| 2026 | [CLQT: A Closed-Loop, Cost-Aware, Strategy-Consistent Benchmark for Diagnostic Evaluation of LLM Portfolio-Management Agents](https://arxiv.org/pdf/2606.29771)<br><sub>arXiv q-fin</sub> | A diagnostic benchmark explicitly incorporating transaction costs and strategy-consistency checks (does the agent's stated reasoning match its actual trades?) for evaluating LLM portfolio-management agents, addressing gaps in earlier cost-agnostic benchmarks.<br><sub>Not captured</sub> | — | — | ✅ | ❔ |  |
| 2026 | [From Knowing to Doing: A Memory-Controlled Benchmark for LLM Trading Agents on Stock Markets](https://arxiv.org/pdf/2605.28359)<br><sub>arXiv q-fin</sub> | Benchmark isolating the effect of an LLM trading agent's memory design (what/how much history it retains) on trading performance, controlling for memory as an experimental variable.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2026 | [LATTICE: Evaluating Decision Support Utility of Crypto Agents](https://arxiv.org/pdf/2604.26235)<br><sub>arXiv q-fin</sub> | Evaluates LLM agents specifically as decision-support tools for cryptocurrency trading (rather than as fully autonomous traders), measuring the utility of their recommendations to a human/hybrid decision process.<br><sub>Cryptocurrency markets</sub> | — | — | ❔ | ❔ |  |
| 2026 | [Agentic Trading: When LLM Agents Meet Financial Markets](https://arxiv.org/html/2605.19337v1)<br><sub>arXiv q-fin</sub> | Broad survey/framework paper on agentic (autonomous, multi-step, tool-using) LLM trading, likely synthesizing the TradingAgents/FinMem/StockBench-style literature into a general taxonomy.<br><sub>N/A (survey)</sub> | — | — | ❔ | ❔ |  |
| 2025 | [MarketSenseAI 2.0: Enhancing Stock Analysis through LLM Agents](https://arxiv.org/abs/2502.00415)<br><sub>arXiv:2502.00415 (under review, Financial Innovation)</sub> | Multi-agent LLM pipeline using retrieval-augmented generation over SEC filings, earnings calls, macro reports, price data and news to generate stock-selection/portfolio decisions.<br><sub>S&P 100, 2023-2024 (primary); S&P 500, 2024 (validation)</sub> | cumulative return of 125.9% vs. 73.5% for the S&P 100 index over 2023-2024 | — | ❔ | ❔ |  |
| 2025 | [StockBench: Can LLM Agents Trade Stocks Profitably in Real-World Markets?](https://arxiv.org/abs/2510.02209)<br><sub>arXiv:2510.02209</sub> | Contamination-free, continuously-updated multi-stock trading benchmark: LLM agents receive daily prices, fundamentals and news and must issue sequential buy/sell/hold decisions over a multi-month window; evaluated via cumulative return, max drawdown and Sortino ratio against a buy-and-hold baseline.<br><sub>Multi-stock, multi-month live/continuously-updated window (state-of-the-art proprietary models GPT-5/Claude-4 and open models Qwen3/Kimi-K2/GLM-4.5 tested)</sub> | buy-and-hold baseline achieves a modest 0.4% return over the test window (max drawdown -15.2%, Sortino 0.0155); several LLM agents deliver returns above 2% | — | ❔ | ✅ |  |
| 2025 | [When Agents Trade: Live Multi-Market Trading Benchmark for LLM Agents (Agent Market Arena)](https://arxiv.org/abs/2510.11695)<br><sub>arXiv (ACM Web Conference 2026)</sub> | Lifelong, real-time multi-market benchmark for LLM trading agents; implements four agent architectures (InvestorAgent, TradeAgent, HedgeFundAgent, DeepFundAgent with memory) tested across five LLM backbones (GPT-4o, GPT-4.1, Claude-3.5-haiku, Claude-sonnet-4, Gemini-2.0-flash) live on crypto and stock markets.<br><sub>Live crypto and stock markets, single named case includes TSLA</sub> | InvestorAgent with GPT-4.1 achieved a 40.83% cumulative return on TSLA over the live test window | — | ❔ | ✅ |  |
| 2025 | [AlphaAgents: Large Language Model based Multi-Agents for Equity Portfolio Construction](https://arxiv.org/html/2508.11152v1)<br><sub>arXiv q-fin</sub> | Multi-agent LLM framework analyzing diverse inputs (earnings calls, financial ratios, market data) collaboratively to construct an equity portfolio for an investment team.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2025 | [The Evolution of Alpha in Finance: Harnessing Human Insight and LLM Agents](https://arxiv.org/pdf/2505.14727)<br><sub>arXiv q-fin</sub> | Survey/position paper on combining human quant researcher insight with LLM agents for alpha generation across the pipeline (idea generation, factor construction, evaluation).<br><sub>N/A (survey)</sub> | — | — | ❔ | ❔ |  |
| 2025 | [LiveTradeBench: Seeking Real-World Alpha with Large Language Models](https://arxiv.org/pdf/2511.03628)<br><sub>arXiv q-fin</sub> | A live (real-time, forward-testing) benchmark for evaluating whether LLM-based trading strategies can generate genuine, non-backtested alpha, addressing the look-ahead/contamination concerns endemic to backtested LLM trading papers.<br><sub>Live markets, forward-testing window (not fully specified)</sub> | — | — | ❔ | ✅ |  |
| 2024 | [TradingAgents: Multi-Agents LLM Financial Trading Framework](https://arxiv.org/abs/2412.20138)<br><sub>arXiv:2412.20138</sub> | Simulates a trading-firm org chart with specialized LLM agents (fundamental, sentiment and technical analysts; bull/bear researchers who debate; a risk-management team; a trader agent) that synthesize the debate into buy/sell/hold decisions for individual stocks.<br><sub>Not fully specified</sub> | — | reports 'notable improvements' in cumulative return, Sharpe ratio and maximum drawdown vs. baseline (non-agentic) models, but exact figures not captured in this pass | ❔ | ❔ | [↗](https://github.com/TauricResearch/TradingAgents) |
| 2024 | [InvestorBench: A Benchmark for Financial Decision-Making Tasks with LLM-based Agent](https://arxiv.org/abs/2412.18174)<br><sub>arXiv (ACL 2025)</sub> | Benchmark suite evaluating LLM-based agents on financial decision-making across single-name stocks, cryptocurrencies and ETFs, using 13 different backbone LLMs, with a simulated retail-investor agent-environment loop.<br><sub>Historical data through roughly 2021 (per comparisons in later benchmarks like StockBench)</sub> | — | — | ❔ | ❔ |  |
| 2024 | [FinBen: A Holistic Financial Benchmark for Large Language Models](https://arxiv.org/abs/2402.12659)<br><sub>arXiv / NeurIPS Datasets & Benchmarks</sub> | Aggregates 42 datasets across 24 financial NLP tasks (information extraction, QA, forecasting, sentiment, etc.) to broadly evaluate LLM financial-text capability, evaluating 21 models including GPT-4/ChatGPT/Gemini.<br><sub>Multiple financial NLP datasets, not a trading backtest</sub> | — | — | ❔ | ❔ |  |
| 2023 | [FinMem: A Performance-Enhanced LLM Trading Agent with Layered Memory and Character Design](https://arxiv.org/abs/2311.13743)<br><sub>arXiv cs.CL/q-fin</sub> | Single-stock LLM trading agent with a layered memory system (working memory plus long-term memory with different retention horizons) and a configurable 'risk character,' used to summarize multi-source information (news, prices, fundamentals) into trading decisions.<br><sub>Individual stocks, backtest period not fully captured</sub> | — | reported to significantly outperform other LLM trading agents on cumulative return and Sharpe ratio in its own comparisons | ❔ | ❔ | [↗](https://github.com/pipiku915/FinMem-LLM-StockTrading) |
| 2023 | [TradingGPT: Multi-Agent System with Layered Memory and Distinct Characters for Enhanced Financial Trading Performance](https://arxiv.org/pdf/2309.03736)<br><sub>arXiv q-fin/cs.CL</sub> | Debate-driven multi-agent LLM trading system where agents with distinct 'characters'/risk profiles debate a trading decision, aiming to improve sentiment classification robustness and reduce single-agent hallucination/bias.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |

<details><summary>How to recreate (15)</summary>

**[CLQT: A Closed-Loop, Cost-Aware, Strategy-Consistent Benchmark for Diagnostic Evaluation of LLM Portfolio-Management Agents](https://arxiv.org/pdf/2606.29771)** (2026)  
🔧 Requires a portfolio-simulation environment with explicit transaction-cost modeling and a mechanism to check consistency between an LLM agent's stated rationale and its executed trades.  
⚠️ Notable for explicitly building in cost-awareness, which most LLM-agent trading papers in this list omit or under-specify -- a good template/checklist for evaluating any LLM-agent component before adding it to a real book.

**[From Knowing to Doing: A Memory-Controlled Benchmark for LLM Trading Agents on Stock Markets](https://arxiv.org/pdf/2605.28359)** (2026)  
🔧 Requires a stock-trading LLM-agent simulation harness (similar to StockBench/TradingAgents) with configurable memory modules (no memory, short window, full history, summarized long-term memory), compare performance across memory configurations.  
⚠️ Useful ablation-style reference for whether memory design (as in FinMem) is actually the source of performance gains claimed in earlier LLM-agent papers, or a confound.

**[LATTICE: Evaluating Decision Support Utility of Crypto Agents](https://arxiv.org/pdf/2604.26235)** (2026)  
🔧 Requires crypto price/news data and an LLM-agent decision-support pipeline; measure whether human (or hybrid human-agent) decisions improve when informed by the agent's output vs. a baseline without it.  
⚠️ Title/abstract only; not independently verified in this pass.

**[Agentic Trading: When LLM Agents Meet Financial Markets](https://arxiv.org/html/2605.19337v1)** (2026)  
🔧 N/A -- survey paper.  
⚠️ Not a standalone empirical strategy; useful as a landscape/taxonomy reference.

**[MarketSenseAI 2.0: Enhancing Stock Analysis through LLM Agents](https://arxiv.org/abs/2502.00415)** (2025)  
🔧 Needs SEC filings, earnings-call transcripts, macro data feeds, news, and daily prices, plus an LLM/RAG pipeline to synthesize a per-stock recommendation, rebalanced periodically (monthly-ish based on filing cadence). Heavy infra: multiple agents, RAG retrieval, orchestration.  
⚠️ 125.9% vs 73.5% is an extraordinary 2-year outperformance for a live LLM strategy; treat with skepticism absent transaction-cost, capacity and true out-of-sample (vs backtested-with-hindsight) disclosure. 2023-2024 was a strong bull/AI-momentum market that may flatter any long-biased LLM stock-picker.

**[StockBench: Can LLM Agents Trade Stocks Profitably in Real-World Markets?](https://arxiv.org/abs/2510.02209)** (2025)  
🔧 Requires daily prices, fundamentals and news for a stock universe, plus an LLM agent loop that ingests this daily and outputs buy/sell/hold; compute cumulative return, max drawdown, Sortino vs. buy-and-hold. This is essentially a template directly reproducible with a standard price + news data feed and any LLM API.  
⚠️ Key finding: most LLM agents struggle to beat simple buy-and-hold, and static financial-knowledge benchmark performance does not translate into trading skill -- an important sobering data point against over-trusting LLM-agent trading claims elsewhere in this list. Test-period market conditions (a period with a low 0.4% buy-and-hold return) likely favored active agents mechanically; results may not generalize to strongly trending markets.

**[When Agents Trade: Live Multi-Market Trading Benchmark for LLM Agents (Agent Market Arena)](https://arxiv.org/abs/2510.11695)** (2025)  
🔧 Requires live/near-live price, fundamentals and news feeds for the target markets, plus an implementation of the four agent archetypes (varying risk style and memory use) run against multiple LLM backbones; track live cumulative return per agent-model pair.  
⚠️ Key finding: agent architecture (not the underlying LLM) is the primary driver of performance differences -- risk-taking vs. conservative agent design matters more than swapping GPT-4o for Claude or Gemini. A single-stock 40.83% TSLA return over an unspecified short live window is a striking but low-sample-size result; do not extrapolate to a diversified book.

**[AlphaAgents: Large Language Model based Multi-Agents for Equity Portfolio Construction](https://arxiv.org/html/2508.11152v1)** (2025)  
🔧 Requires earnings-call transcripts, fundamentals, and prices; implement specialized agents (fundamental, market, risk) that jointly vote/aggregate into portfolio weights.  
⚠️ Title/abstract only; not independently verified in this pass.

**[The Evolution of Alpha in Finance: Harnessing Human Insight and LLM Agents](https://arxiv.org/pdf/2505.14727)** (2025)  
🔧 N/A -- survey paper; useful as a map of the LLM-alpha-generation landscape rather than an implementable strategy.  
⚠️ Not a standalone empirical strategy paper.

**[LiveTradeBench: Seeking Real-World Alpha with Large Language Models](https://arxiv.org/pdf/2511.03628)** (2025)  
🔧 Requires a live/streaming price+news+fundamentals feed and an LLM agent decision loop run forward in real time (not backtested on historical data the LLM may have seen during pretraining); track realized P&L going forward from the benchmark's launch date.  
⚠️ Forward/live testing is the most credible way to sidestep LLM training-data-cutoff look-ahead risk that plagues most other LLM-signal papers in this list; worth prioritizing this design pattern (paper trading forward, not backtesting on pre-cutoff historical news) when evaluating any LLM-based signal for the target book.

**[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://arxiv.org/abs/2412.20138)** (2024)  
🔧 Needs prices, fundamentals, news/sentiment feeds. Build role-specialized LLM agent prompts (fundamental/sentiment/technical analyst, bull/bear debate, risk manager, trader), orchestrate a daily decision loop per stock, and backtest the resulting buy/hold/sell signal.  
⚠️ Popular open-source multi-agent trading framework (widely forked); like most LLM-agent trading papers, backtest windows are short and cost/capacity treatment is not rigorously disclosed in the abstract.

**[InvestorBench: A Benchmark for Financial Decision-Making Tasks with LLM-based Agent](https://arxiv.org/abs/2412.18174)** (2024)  
🔧 Not a trading strategy per se but a benchmark harness: implement/adapt the InvestorBench environment (public tasks/data splits) and plug in candidate LLM backbones to compare agent decision quality.  
⚠️ Later work (StockBench, 2025) notes InvestorBench relies on historical data only up to ~2021 and is largely single-stock, motivating newer 'live/continuously updated' benchmarks below.

**[FinBen: A Holistic Financial Benchmark for Large Language Models](https://arxiv.org/abs/2402.12659)** (2024)  
🔧 Not directly a trading strategy; useful as an evaluation harness for any LLM-based text-processing component (sentiment, summarization, forecasting) that would feed into a downstream trading signal.  
⚠️ FinBen finds current LLMs handle basic financial text processing well but struggle at advanced reasoning/market forecasting tasks -- relevant caution for relying on off-the-shelf LLM 'forecasts' rather than fine-tuned or ensembled signals.

**[FinMem: A Performance-Enhanced LLM Trading Agent with Layered Memory and Character Design](https://arxiv.org/abs/2311.13743)** (2023)  
🔧 Requires news + price + fundamentals per stock; implement a layered memory buffer (short-term 'working memory' plus decaying long-term memory) feeding an LLM decision prompt each day, with a configurable risk-aversion parameter.  
⚠️ One of the earliest and most-cited 'LLM agent with memory' trading papers (late 2023); single-stock backtests of this era are widely noted to be short-horizon and susceptible to hindsight/overfitting in agent prompt design.

**[TradingGPT: Multi-Agent System with Layered Memory and Distinct Characters for Enhanced Financial Trading Performance](https://arxiv.org/pdf/2309.03736)** (2023)  
🔧 Similar recreation pattern to TradingAgents/FinMem: multiple LLM personas debate, an aggregator agent decides.  
⚠️ Title/abstract only; grouped with FinMem/TradingAgents as an early multi-agent LLM trading paper.

</details>

### RL portfolio management

| Year | Paper | Strategy | Reported return | Sharpe | Net of costs | OOS | Code |
|---|---|---|---|---|:-:|:-:|:-:|
| 2026 | [Deep Reinforcement Learning Framework for Diversified Portfolio Management Across Global Equity Markets](https://arxiv.org/html/2605.17307v1)<br><sub>arXiv q-fin</sub> | DRL framework for portfolio allocation across global equity markets, optimizing a differential Sharpe ratio reward net of transaction costs; a related PPO variant is also used for options-hedging tasks comparable to Black-Scholes delta hedging.<br><sub>Global equities, not fully specified</sub> | — | — | ✅ | ❔ |  |
| 2025 | [HARLF: Hierarchical Reinforcement Learning and Lightweight LLM-Driven Sentiment Integration for Financial Portfolio Optimization](https://arxiv.org/abs/2507.18560)<br><sub>arXiv:2507.18560</sub> | Hierarchical RL portfolio-optimization framework: base RL agents process hybrid price+sentiment data per asset, meta-agents aggregate decisions across base agents, and a super-agent merges everything into final portfolio weights; sentiment comes from a lightweight LLM rather than a heavy full-scale model.<br><sub>Trained 2000-2017, evaluated out-of-sample 2018-2024</sub> | 26% annualized return | 1.2 | ❔ | ✅ |  |
| 2025 | [Risk-Aware Deep Reinforcement Learning for Dynamic Portfolio Optimization](https://arxiv.org/abs/2511.11481)<br><sub>arXiv q-fin</sub> | PPO-based DRL portfolio optimizer with a Sharpe-ratio-based reward plus explicit risk controls (max-drawdown and volatility constraints) layered on top of the RL policy.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2024 | [Markowitz Meets Bellman: Knowledge-Distilled Reinforcement Learning for Portfolio Management](https://arxiv.org/pdf/2405.05449)<br><sub>arXiv q-fin</sub> | Distills classic Markowitz mean-variance optimization knowledge into a Bellman/RL-based portfolio policy, combining the interpretability of mean-variance theory with RL's ability to adapt dynamically.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2024 | [Portfolio Management using Deep Reinforcement Learning](https://arxiv.org/abs/2405.01604)<br><sub>arXiv q-fin</sub> | Standard DRL portfolio-allocation model benchmarked against the Dow Jones Industrial Average.<br><sub>Dow Jones constituents</sub> | 25.87% annualized return on the test data (vs. the Dow Jones Industrial Average benchmark) | — | ❔ | ❔ |  |

<details><summary>How to recreate (5)</summary>

**[Deep Reinforcement Learning Framework for Diversified Portfolio Management Across Global Equity Markets](https://arxiv.org/html/2605.17307v1)** (2026)  
🔧 Requires multi-market equity price history; train a PPO/differential-Sharpe DRL agent with an explicit transaction-cost term in the reward, evaluate across multiple global equity markets for diversification benefit.  
⚠️ Title/abstract only; not independently verified numerically in this pass.

**[HARLF: Hierarchical Reinforcement Learning and Lightweight LLM-Driven Sentiment Integration for Financial Portfolio Optimization](https://arxiv.org/abs/2507.18560)** (2025)  
🔧 Requires multi-asset price history plus a news/sentiment feed for the LLM component. Train base RL agents (e.g., PPO/DDPG) per asset or asset group on hybrid state (price features + sentiment score), then train meta- and super-agent aggregation layers on top, backtest 2018-2024 out-of-sample.  
⚠️ Reported to outperform equal-weighted and S&P 500 benchmarks over 2018-2024; no explicit transaction-cost disclosure found -- treat the 26%/1.2 Sharpe figures as likely gross of costs pending confirmation.

**[Risk-Aware Deep Reinforcement Learning for Dynamic Portfolio Optimization](https://arxiv.org/abs/2511.11481)** (2025)  
🔧 Requires multi-asset price history; implement PPO with a differentiable Sharpe-like reward and explicit drawdown/vol penalty terms, train/test with walk-forward splits.  
⚠️ Notably, the paper's own finding is negative/cautionary: the DRL agent stabilizes volatility but suffers degraded risk-adjusted returns due to over-conservative policy convergence -- a useful counter-example to more optimistic RL-portfolio papers on this list.

**[Markowitz Meets Bellman: Knowledge-Distilled Reinforcement Learning for Portfolio Management](https://arxiv.org/pdf/2405.05449)** (2024)  
🔧 Requires multi-asset returns/covariance estimates; train an RL policy with a reward/regularization term that pulls it toward the Markowitz-optimal weights, allowing deviation when the RL value function suggests an edge.  
⚠️ Title/abstract only; not independently verified in this pass.

**[Portfolio Management using Deep Reinforcement Learning](https://arxiv.org/abs/2405.01604)** (2024)  
🔧 Requires Dow-30-style multi-asset price history; implement a standard actor-critic or PPO DRL portfolio agent, benchmark cumulative return against buy-and-hold DJIA.  
⚠️ A 30-name, well-known large-cap universe is a small, low-capacity-constrained test bed; 25.87% annualized outperformance in a single backtest window should not be taken as a stable, repeatable edge without walk-forward, cost-adjusted validation.

</details>

### Alpha mining

| Year | Paper | Strategy | Reported return | Sharpe | Net of costs | OOS | Code |
|---|---|---|---|---|:-:|:-:|:-:|
| 2026 | [AlphaMemo: Structured Search-Process Memory for Self-Evolving Alpha Mining Agents](https://arxiv.org/pdf/2606.20625)<br><sub>arXiv q-fin</sub> | Adds a structured memory of prior search processes/outcomes to an LLM-agent alpha-mining loop so the agent can learn from its own past search trajectories ('self-evolving') rather than searching from scratch each run.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2025 | [AlphaAgent: LLM-Driven Alpha Mining with Regularized Exploration to Counteract Alpha Decay](https://arxiv.org/abs/2502.16789)<br><sub>arXiv:2502.16789</sub> | LLM-agent-driven formulaic alpha search with three regularizers -- AST-based originality/similarity penalty vs. known factors, LLM-scored hypothesis-factor semantic alignment, and AST-based complexity control -- intended to produce decay-resistant alphas rather than overfit/curve-fit factors.<br><sub>CSI 500 (China) and S&P 500 (US), 4-year test spanning bull and bear regimes</sub> | — | — | ❔ | ✅ |  |
| 2025 | [R&D-Agent-Quant (RD-Agent(Q)): A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization](https://neurips.cc/virtual/2025/poster/121804)<br><sub>NeurIPS 2025 (Datasets and Benchmarks Track)</sub> | Two-stage multi-agent loop: a 'Research' stage generates hypotheses and factor/model tasks; a 'Development' stage (Co-STEER code-generation agent) implements and backtests them in real markets, jointly optimizing factor libraries and prediction models rather than treating them separately.<br><sub>Quant equity markets (via Qlib framework); exact universe not fully confirmed</sub> | — | — | ❔ | ❔ | [↗](https://github.com/microsoft/RD-Agent) |
| 2025 | [Market-Dependent Communication in Multi-Agent Alpha Generation](https://arxiv.org/pdf/2511.13614)<br><sub>arXiv q-fin</sub> | Studies how communication protocols between multiple alpha-generating agents should adapt to current market conditions (regime-dependent coordination) rather than using a fixed communication scheme.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2024 | [RiskMiner: Discovering Formulaic Alphas via Risk-Seeking Monte Carlo Tree Search](https://arxiv.org/abs/2402.07080)<br><sub>arXiv:2402.07080</sub> | Formulates formulaic-alpha mining as a reward-dense Markov Decision Process and solves it with a risk-seeking Monte Carlo Tree Search, aiming for alphas that are profitable under realistic backtesting rather than just high in-sample IC.<br><sub>Two real-world stock sets (markets not specified in abstract)</sub> | — | — | ❔ | ❔ |  |
| 2024 | [QuantFactor REINFORCE: Mining Steady Formulaic Alpha Factors with Variance-Bounded REINFORCE](https://arxiv.org/pdf/2409.05144)<br><sub>arXiv q-fin</sub> | Uses a variance-bounded REINFORCE policy-gradient method to mine formulaic alpha factors that are more stable/steady across time than standard RL alpha miners.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2023 | [Generating Synergistic Formulaic Alpha Collections via Reinforcement Learning (AlphaGen)](https://arxiv.org/abs/2306.12964)<br><sub>KDD 2023 (Applied Data Science track)</sub> | Reinforcement-learning agent searches a formulaic-alpha expression space (combinations of price/volume operators) and is rewarded by the combined performance (IC) of the resulting alpha set rather than each alpha individually, producing a synergistic collection of low-correlation formulaic factors.<br><sub>CSI300 (China A-shares)</sub> | — | — | ❔ | ❔ | [↗](https://github.com/RL-MLDM/alphagen) |

<details><summary>How to recreate (7)</summary>

**[AlphaMemo: Structured Search-Process Memory for Self-Evolving Alpha Mining Agents](https://arxiv.org/pdf/2606.20625)** (2026)  
🔧 Same alpha-mining harness as AlphaGen/RD-Agent(Q), plus a persistent memory store (e.g., vector DB of past search states/rewards) that the LLM agent queries/updates each iteration.  
⚠️ Very recent (2026 arXiv id); not independently verified in this pass, included for completeness of the alpha-mining agent trend.

**[AlphaAgent: LLM-Driven Alpha Mining with Regularized Exploration to Counteract Alpha Decay](https://arxiv.org/abs/2502.16789)** (2025)  
🔧 Requires daily price/fundamental data for the target universe and an LLM to propose/evaluate candidate alpha formulas; iterate a generate-evaluate-regularize loop (originality, alignment, complexity) and backtest each surviving formula. Feasible with standard daily price data plus an LLM API, but requires building the regularization/search harness.  
⚠️ Abstract only claims qualitative 'resistance to alpha decay' and outperformance of baselines; no numeric IC, return or Sharpe figures were retrievable, so treat any performance claim as unverified pending full-text read.

**[R&D-Agent-Quant (RD-Agent(Q)): A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization](https://neurips.cc/virtual/2025/poster/121804)** (2025)  
🔧 Requires the open-source RD-Agent + Qlib stack, an LLM backend (e.g., GPT-4o-mini), and market data compatible with Qlib's data layer; run the Research/Development agent loop end-to-end (fully automated) to mine factors and jointly tune a downstream prediction model, then backtest in Qlib.  
⚠️ Reports RD-Agent(Q) achieves up to 2x the annualized return of classical factor libraries using 70% fewer factors, at very low compute cost (all experiments reportedly under $10). Code and framework are public, making this one of the more directly reproducible papers in this list -- but results are on Qlib's standard market setups, and the ARR is a backtest IC-driven metric, not a live P&L.

**[Market-Dependent Communication in Multi-Agent Alpha Generation](https://arxiv.org/pdf/2511.13614)** (2025)  
🔧 Requires a multi-agent alpha-mining harness (like AlphaGen/RD-Agent) plus a regime-classification layer that changes how/whether agents share information depending on detected market state.  
⚠️ Title/abstract only; not independently verified in this pass.

**[RiskMiner: Discovering Formulaic Alphas via Risk-Seeking Monte Carlo Tree Search](https://arxiv.org/abs/2402.07080)** (2024)  
🔧 Requires daily price/fundamental data and an operator library for alpha expressions; implement MCTS with a risk-seeking value estimate over the expression tree, and evaluate mined alphas with a realistic backtest (costs, turnover) as the paper claims to do.  
⚠️ Abstract claims outperformance of state-of-the-art alpha-mining benchmarks under 'realistic trading settings,' but no numeric IC/return/Sharpe figures were retrievable in this pass -- flagged for follow-up before relying on it.

**[QuantFactor REINFORCE: Mining Steady Formulaic Alpha Factors with Variance-Bounded REINFORCE](https://arxiv.org/pdf/2409.05144)** (2024)  
🔧 Same general alpha-mining recreation pattern as AlphaGen/RiskMiner: operator-library expression search, RL training with a variance-penalized reward, backtest mined factors on daily price/fundamental data.  
⚠️ Details not independently verified beyond title in this research pass; included for category completeness only.

**[Generating Synergistic Formulaic Alpha Collections via Reinforcement Learning (AlphaGen)](https://arxiv.org/abs/2306.12964)** (2023)  
🔧 Requires daily OHLCV data and an operator library (rank, delay, correlation, ts_mean, etc.); define an RL environment where actions build alpha expression trees, reward = combined IC of the mined alpha set on a rolling training window, then backtest the mined factors via a standard factor-based long-short portfolio (e.g., top/bottom decile). Original codebase is public.  
⚠️ Predecessor to RD-Agent(Q) and AlphaAgent; strong influence on the alpha-mining literature. Results are China A-share-specific (CSI300); direct transfer to US tech-heavy universe unverified. No explicit cost/capacity discussion found.

</details>

### Crypto

| Year | Paper | Strategy | Reported return | Sharpe | Net of costs | OOS | Code |
|---|---|---|---|---|:-:|:-:|:-:|
| 2026 | [From Hypotheses to Factors: Constrained LLM Agents in Cryptocurrency Markets](https://arxiv.org/html/2604.26747v1)<br><sub>arXiv q-fin</sub> | Uses constrained LLM agents to generate and test factor hypotheses specifically for cryptocurrency markets, an application of the LLM-alpha-mining paradigm (AlphaGen/AlphaAgent-style) to crypto rather than equities.<br><sub>Cryptocurrency markets</sub> | — | — | ❔ | ❔ |  |
| 2026 | [Are Whitepaper Claims Reflected in Market Structure? A Contamination-Aware Pipeline and a Power-Limited Null (crypto whitepaper factor analysis)](https://arxiv.org/html/2601.20336v1)<br><sub>arXiv q-fin</sub> | Tests whether claims made in cryptocurrency project whitepapers (e.g., about technology, tokenomics, use-case) are reflected in subsequent market behavior/factor exposures, using a contamination-aware statistical pipeline to guard against data-snooping.<br><sub>Cryptocurrency universe with available whitepapers</sub> | — | — | ❔ | ❔ |  |
| 2025 | [Cryptocurrency as an Investable Asset Class: Coming of Age](https://arxiv.org/abs/2510.14435)<br><sub>arXiv:2510.14435</sub> | Extends the crypto three-factor model (market, size, momentum) with a value factor to form a four-factor (C-4) model; organizes crypto empirical asset-pricing regularities into seven stylized facts and argues crypto risk-adjusted performance is now broadly comparable to traditional asset classes.<br><sub>Broad cryptocurrency universe, updated through the mid-2020s</sub> | — | — | ❔ | ❔ |  |
| 2025 | [Cryptocurrency Market Risk-Managed Momentum Strategies](https://www.sciencedirect.com/science/article/abs/pii/S1544612325011377)<br><sub>Journal (via ScienceDirect)</sub> | Applies volatility-scaling/risk-management overlays to cryptocurrency momentum strategies to mitigate the severe crash risk documented in unmanaged crypto momentum.<br><sub>Cryptocurrency universe</sub> | — | — | ❔ | ❔ |  |
| 2025 | [Time Series Momentum in Cryptocurrency (crypto momentum has (not) its moments)](https://link.springer.com/article/10.1007/s11408-025-00474-9)<br><sub>Financial Markets and Portfolio Management</sub> | Studies whether cryptocurrency markets exhibit the same extended, persistent momentum-crash pattern documented in equities, finding a key structural difference.<br><sub>Cryptocurrency universe</sub> | — | — | ❔ | ❔ |  |
| 2022 | [Common Risk Factors in Cryptocurrency](https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.13119)<br><sub>Journal of Finance</sub> | Constructs cryptocurrency counterparts of standard equity return predictors and shows that a three-factor model (crypto market, crypto size, crypto momentum) captures most of the cross-sectional variation in expected cryptocurrency returns; ten crypto characteristics form significant long-short strategies largely spanned by this C-3 model.<br><sub>Broad cryptocurrency universe, sample spanning roughly 2014-2018</sub> | — | — | ❌ | ❌ |  |

<details><summary>How to recreate (6)</summary>

**[From Hypotheses to Factors: Constrained LLM Agents in Cryptocurrency Markets](https://arxiv.org/html/2604.26747v1)** (2026)  
🔧 Requires crypto price/volume/on-chain data plus an LLM agent harness constrained to propose economically-motivated hypotheses (not just curve-fit formulas) before translating them into testable factors.  
⚠️ Title/abstract only; not independently verified in this pass.

**[Are Whitepaper Claims Reflected in Market Structure? A Contamination-Aware Pipeline and a Power-Limited Null (crypto whitepaper factor analysis)](https://arxiv.org/html/2601.20336v1)** (2026)  
🔧 Requires a corpus of crypto whitepapers plus market data; extract claims via LLM parsing, test for correlation/predictive power against realized returns/volume, with an explicit multiple-testing correction ('power-limited null') to avoid false positives.  
⚠️ Methodologically notable for explicitly guarding against the data-snooping/multiple-testing problem endemic to this literature -- a useful template regardless of the specific crypto-whitepaper application.

**[Cryptocurrency as an Investable Asset Class: Coming of Age](https://arxiv.org/abs/2510.14435)** (2025)  
🔧 Requires daily crypto price/volume/on-chain data; add a value factor (e.g., based on network-value-to-transactions or a price-to-fundamental-usage ratio) to the existing C-3 factors, re-test spanning of characteristic-sorted portfolios.  
⚠️ The new crypto value premium is plausibly driven by compensation for on-chain-activity risk per the authors; crypto momentum, while profitable, is subject to severe crash risk requiring volatility management (see related crypto-momentum-crash literature).

**[Cryptocurrency Market Risk-Managed Momentum Strategies](https://www.sciencedirect.com/science/article/abs/pii/S1544612325011377)** (2025)  
🔧 Requires daily crypto prices; compute trailing momentum signal per coin, scale position size inversely to recent realized volatility (vol targeting), form long-short or long-only momentum portfolio, compare crash frequency/severity to unmanaged momentum.  
⚠️ Consistent with equity-momentum literature (volatility-managed momentum reduces crash risk); crypto momentum crashes are noted elsewhere to differ structurally from equity momentum crashes (crypto lacks the same extended-crash pattern per one 2025 study).

**[Time Series Momentum in Cryptocurrency (crypto momentum has (not) its moments)](https://link.springer.com/article/10.1007/s11408-025-00474-9)** (2025)  
🔧 Requires daily crypto price history; construct standard time-series momentum signal, examine drawdown/crash episodes and their persistence relative to the equity-momentum-crash literature (e.g., Daniel-Moskowitz 2016).  
⚠️ Key finding: crypto markets lack the extended, prolonged momentum crashes seen in equities, a notable divergence from the classic equity 'momentum crashes' result (Daniel & Moskowitz 2016) used as context here.

**[Common Risk Factors in Cryptocurrency](https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.13119)** (2022)  
🔧 Requires daily crypto price/volume/market-cap history across a broad coin universe. Compute crypto-market excess return, crypto-size (small-minus-big market cap) and crypto-momentum (trailing-return-sorted) factors; form and backtest additional long-short characteristic portfolios, test whether the C-3 model spans them via time-series regression.  
⚠️ Seminal anchor for crypto factor investing; standard equity factor models (FF3/Carhart4/FF5) do not explain crypto cross-sectional returns, motivating crypto-specific factors. Gross of costs; crypto exchange/borrow costs and extreme volatility materially affect implementability.

</details>

### Prediction markets

| Year | Paper | Strategy | Reported return | Sharpe | Net of costs | OOS | Code |
|---|---|---|---|---|:-:|:-:|:-:|
| 2026 | [Executable Arbitrage and Market Efficiency in Prediction Markets](https://arxiv.org/html/2608.00666v1)<br><sub>arXiv q-fin</sub> | Uses high-resolution order-book snapshots on prediction markets (e.g., Polymarket) to detect arbitrage opportunities in real time, then measures how persistent and how actually executable (against real liquidity) those opportunities are, distinguishing theoretical from tradeable mispricing.<br><sub>Polymarket (and similar) prediction markets</sub> | — | — | ✅ | ❔ |  |
| 2026 | [Arbitrage Analysis in Polymarket NBA Markets](https://arxiv.org/html/2605.00864v1)<br><sub>arXiv q-fin</sub> | Focused study of arbitrage opportunities specifically within Polymarket's NBA betting markets.<br><sub>Polymarket NBA markets</sub> | — | — | ❔ | ❔ |  |
| 2026 | [Semantic Non-Fungibility and Violations of the Law of One Price in Prediction Markets](https://arxiv.org/html/2601.01706v1)<br><sub>arXiv q-fin</sub> | Documents cross-platform (e.g., Polymarket vs. Kalshi) violations of the law of one price for economically equivalent (but not identically worded/structured) prediction-market contracts, attributing fragmentation to structural factors like differing resolution rules and institutional segmentation rather than pure inefficiency.<br><sub>Cross-platform prediction markets (Polymarket, Kalshi)</sub> | — | — | ❔ | ❔ |  |

<details><summary>How to recreate (3)</summary>

**[Executable Arbitrage and Market Efficiency in Prediction Markets](https://arxiv.org/html/2608.00666v1)** (2026)  
🔧 Requires real-time or historical order-book-level data from prediction-market platforms (Polymarket/Kalshi APIs); scan for logically-linked contracts (e.g., complementary outcomes summing to more/less than 100%) and check whether the implied arbitrage can be filled at quoted depth net of fees.  
⚠️ Institutional-scale profit is limited: residual inefficiencies are 'structurally confined to the retail tier' per the paper's framing -- i.e., the aggregate market is close to efficient at size, even though retail-scale arbitrage remains detectable. Not directly relevant to a US tech-equity long/short book but included for completeness's scope.

**[Arbitrage Analysis in Polymarket NBA Markets](https://arxiv.org/html/2605.00864v1)** (2026)  
🔧 Requires Polymarket NBA market order-book/price data; identify logically linked contracts (e.g., moneyline vs. spread-implied probabilities) and test for exploitable mispricing net of fees.  
⚠️ Finds NBA markets are nearly efficient in aggregate, with residual inefficiencies mainly accessible only at retail scale, not institutional size.

**[Semantic Non-Fungibility and Violations of the Law of One Price in Prediction Markets](https://arxiv.org/html/2601.01706v1)** (2026)  
🔧 Requires matched-contract price data across platforms; identify semantically-equivalent contracts with different resolution language, measure price divergence, test whether the divergence is arbitrageable given platform-specific settlement risk and withdrawal/transfer frictions.  
⚠️ Finding that fragmentation is 'structural rather than incidental' implies apparent cross-platform arbitrage may not be safely executable due to resolution-rule risk, not just execution cost.

</details>

### Other

| Year | Paper | Strategy | Reported return | Sharpe | Net of costs | OOS | Code |
|---|---|---|---|---|:-:|:-:|:-:|
| 2025 | [From Deep Learning to LLMs: A Survey of AI in Quantitative Investment](https://arxiv.org/pdf/2503.21422)<br><sub>arXiv q-fin</sub> | Survey covering the progression from classical deep-learning quant methods to LLM-based approaches across the quantitative investment pipeline (factor mining, prediction, portfolio construction, execution).<br><sub>N/A (survey)</sub> | — | — | ❔ | ❔ |  |

<details><summary>How to recreate (1)</summary>

**[From Deep Learning to LLMs: A Survey of AI in Quantitative Investment](https://arxiv.org/pdf/2503.21422)** (2025)  
🔧 N/A -- survey paper; useful as a map for prioritizing which sub-literatures (alpha mining, ML prediction, LLM agents) to invest research time in.  
⚠️ Not a standalone empirical strategy paper.

</details>

[⬆ back to top](#contents)

## Methodology & caveats

- Compiled in September 2026 from GitHub (search, API metadata and curated lists such as awesome-quant, awesome-systematic-trading and awesome-quant-ai), public web and social search, and arXiv, SSRN and journal pages.
- Star counts, last-push dates and maintenance status are point-in-time. Popular does not mean mature: several 2026 AI repos show hype-driven star growth.
- Paper returns are reported, not reproduced. “Net of costs” and “OOS” reflect what each paper states (❔ = not stated). A few very recent arXiv entries were verified at abstract level only and are flagged in their notes.
- **Nothing here is investment advice.** Backtested and hypothetical results do not guarantee future performance.

## Contributing

Found a missing project, a dead link or a wrong number? Open an issue or PR. Edit `data/tools.json` or `data/papers.json` and run `python scripts/build_readme.py` to regenerate this README. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[CC0 1.0](LICENSE): the list is public domain. Linked projects keep their own licenses.
