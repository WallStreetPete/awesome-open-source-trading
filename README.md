<div align="center">

# Awesome Open-Source Trading

**A curated map of open-source trading software and recent quant strategy research:**  
backtesting · live execution · Interactive Brokers · Kalshi & Polymarket · options & greeks · AI agents · fundamentals & data

![projects](https://img.shields.io/badge/projects-459-2ea44f) ![papers](https://img.shields.io/badge/papers-113-8a2be2) ![snapshot](https://img.shields.io/badge/snapshot-September%202026-blue) ![license](https://img.shields.io/badge/license-CC0--1.0-lightgrey)

</div>

Every project has a short explainer, what it is good at, and its limitations. Every paper lists its strategy, the return **as reported by the authors**, whether costs and out-of-sample testing were included, and how to recreate it. Full explainers and recreation notes are in [`docs/`](docs); machine-readable data is in [`data/`](data).

> **Status legend:** 🟢 active · 🟡 slow · 🟠 stale · 🔴 archived · ⚪ unknown. Stars and activity are a snapshot from September 2026.

## Contents

- 🧪 [Backtesting & quant research](#backtesting--quant-research) — 108 projects
- ⚡ [Live trading, execution & brokers](#live-trading-execution--brokers) — 69 projects
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

<sub>📖 [Full explainers & limitations →](docs/backtesting.md#backtesting-engines)</sub>

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

### Research platforms

<sub>📖 [Full explainers & limitations →](docs/backtesting.md#research-platforms)</sub>

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

### Factor research

<sub>📖 [Full explainers & limitations →](docs/backtesting.md#factor-research)</sub>

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**mlfinlab**](https://github.com/hudson-and-thames/mlfinlab) | 4.9k | Python | 🔴 | The canonical reference implementation of López de Prado's financial data structures, labeling and leakage-aware cross-validation techniques. |
| [**alphalens**](https://github.com/quantopian/alphalens) | 4.4k | Jupyter Notebook | 🔴 | The reference tool for evaluating whether a candidate alpha factor has genuine predictive power (IC, quantile spreads, decay) before building a full strategy around it. |
| [**firmai/machine-learning-asset-management**](https://github.com/firmai/machine-learning-asset-management) | 1.8k | Jupyter Notebook | 🔴 | Useful as a curated survey of ML techniques applied to asset management/factor investing, for discovering approaches and papers. |
| [**alphalens-reloaded**](https://github.com/stefan-jansen/alphalens-reloaded) | 652 | Python | 🟢 | The current standard tool for factor/signal predictive-power evaluation (IC, quantile spreads, turnover, decay) on a modern Python stack. |
| [**FactorAnalytics (R)**](https://github.com/braverock/FactorAnalytics) | 85 | R | 🟡 | Useful R-native tooling for fitting and comparing fundamental, time-series and statistical factor models feeding into risk/portfolio work. |
| [**covFactorModel (R)**](https://github.com/dppalomar/covFactorModel) | 39 | R | 🟡 | Useful as a lightweight R tool for factor-model-based covariance estimation feeding into downstream portfolio optimization. |

### Performance analytics & tearsheets

<sub>📖 [Full explainers & limitations →](docs/backtesting.md#performance-analytics--tearsheets)</sub>

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

### Portfolio optimization

<sub>📖 [Full explainers & limitations →](docs/backtesting.md#portfolio-optimization)</sub>

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

### Data tooling

<sub>📖 [Full explainers & limitations →](docs/backtesting.md#data-tooling)</sub>

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**OpenBB**](https://github.com/OpenBB-finance/OpenBB) | 73.3k | Python | 🟢 | Best as a unified, extensible data layer and research terminal to pair with a dedicated backtesting engine, rather than as the backtester itself. |
| [**tidyquant (R)**](https://github.com/business-science/tidyquant) | 915 | R | 🟢 | Best for R users who want financial data retrieval and standard performance analytics in an idiomatic, pipe-friendly tidyverse workflow. |

### Lists & other

<sub>📖 [Full explainers & limitations →](docs/backtesting.md#lists--other)</sub>

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**TradingAgents**](https://github.com/TauricResearch/TradingAgents) | 107.8k | Python | 🟢 | Interesting as a reference architecture for structuring LLM-based multi-agent investment debate/analysis pipelines, and as a starting point for LLM-augmented research workflows. |
| [**je-suis-tm/quant-trading**](https://github.com/je-suis-tm/quant-trading) | 10.8k | Python | 🟢 | Great as a library of worked strategy examples to learn from or adapt, especially for classic technical/statistical-arbitrage strategy patterns. |
| [**mplfinance**](https://github.com/matplotlib/mplfinance) | 4.4k | Python | 🟡 | The standard choice for producing publication-quality candlestick/OHLC charts from pandas OHLCV data in Python. |
| [**finplot**](https://github.com/highfestiva/finplot) | 1.2k | Python | 🟢 | Good for fast, interactive charting of large historical datasets during backtest research, where matplotlib feels sluggish. |

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

<sub>📖 [Full explainers & limitations →](docs/live_trading.md#interactive-brokers)</sub>

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

### Broker SDKs

<sub>📖 [Full explainers & limitations →](docs/live_trading.md#broker-sdks)</sub>

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

### Execution & OMS

<sub>📖 [Full explainers & limitations →](docs/live_trading.md#execution--oms)</sub>

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**pysystemtrade**](https://github.com/robcarver17/pysystemtrade) | 3.5k | Python | 🟢 | A theoretically rigorous, IBKR-connected systematic trading stack for multi-instrument (primarily futures) portfolios with strong risk/vol-targeting logic, directly usable as a reference for building a disciplined long/short risk framework. |
| [**FreqUI**](https://github.com/freqtrade/frequi) | 1.1k | Vue | 🟢 | Real-time visual monitoring and manual override of a live freqtrade bot. |
| [**go-trader (robaho)**](https://github.com/robaho/go-trader) | 521 | Go | 🟢 | Local integration testing of execution/OMS code against a simulated exchange with realistic order matching semantics. |
| [**the0**](https://github.com/alexanderwanyoike/the0) | 432 | TypeScript | 🟢 | Running heterogeneous trading bots (in any language) side-by-side under one orchestration/execution layer without forcing a specific strategy DSL. |
| [**Hummingbot Dashboard**](https://github.com/hummingbot/dashboard) | 367 | Python | 🟢 | Visual configuration/monitoring layer for Hummingbot strategies and live bot fleets. |
| [**hummingbot-api**](https://github.com/hummingbot/hummingbot-api) | 142 | Python | 🟢 | Centralized management/monitoring of many Hummingbot instances, useful for running several strategies or markets in parallel. |
| [**Espeon Trader**](https://github.com/kangykii/espeon) | 1 | Rust / TypeScript | 🟢 | Exploring how AI workflows, broker metadata, execution adapters, and auditable experiment records fit together in a local cTrader application. |

### Crypto bots

<sub>📖 [Full explainers & limitations →](docs/live_trading.md#crypto-bots)</sub>

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**ccxt**](https://github.com/ccxt/ccxt) | 44.1k | Python | 🟢 | Writing exchange-agnostic order placement, balance, and market-data code that works across dozens of crypto venues with one consistent API. |
| [**Superalgos**](https://github.com/Superalgos/Superalgos) | 5.7k | JavaScript | 🟢 | Non-coder-friendly, visual strategy design and deployment for crypto trading, with an integrated data pipeline. |
| [**Krypto/opentrader**](https://github.com/Open-Trader/opentrader) | 2.9k | TypeScript | 🟡 | DCA/grid strategy automation for crypto with a polished self-hosted web UI, appealing to a TypeScript/Node-oriented team. |
| [**pmxt (CCXT for prediction markets)**](https://github.com/pmxt-dev/pmxt) | 2.2k | TypeScript | 🟢 | Writing venue-agnostic execution code across Polymarket/Kalshi-style prediction markets. |
| [**cassandre-trading-bot**](https://github.com/cassandre-tech/cassandre-trading-bot) | 661 | Java | 🟡 | Java/Spring-native crypto bot development for teams already standardized on the Spring stack. |

### Market making

<sub>📖 [Full explainers & limitations →](docs/live_trading.md#market-making)</sub>

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**Hummingbot**](https://github.com/hummingbot/hummingbot) | 20.1k | Python | 🟢 | Production-grade crypto market making and cross-exchange arbitrage with connector abstractions handling exchange-specific order book/order-type quirks. |
| [**Krypto-trading-bot (Tribeca)**](https://github.com/ctubio/Krypto-trading-bot) | 3.7k | C++ | 🟡 | Low-latency C++ market making for crypto exchanges where Python-based bots' latency is a bottleneck. |
| [**poly-maker**](https://github.com/warproxxx/poly-maker) | 1.5k | Python | 🟢 | Automated liquidity provision on Polymarket-style prediction markets. |
| [**coinbase-market-making-bot**](https://github.com/algotrading-lab/coinbase-market-making-bot) | 113 | TypeScript | 🟢 | Simple, focused market-making automation for Coinbase specifically without the overhead of a multi-exchange framework. |
| [**PinnacleMM**](https://github.com/chizy7/PinnacleMM) | 14 | C++ | 🟢 | Reference architecture for building a low-latency C++ market-making engine from scratch. |

### FIX engines

<sub>📖 [Full explainers & limitations →](docs/live_trading.md#fix-engines)</sub>

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**QuickFIX**](https://github.com/quickfix/quickfix) | 2.0k | C++ | 🟢 | Battle-tested, standards-compliant FIX session and application-layer messaging for connecting to institutional brokers/venues that require FIX rather than a proprietary REST/socket API. |
| [**QuickFIX/J**](https://github.com/quickfix-j/quickfixj) | 1.2k | Java | 🟢 | Production-grade FIX connectivity for JVM-based OMS/EMS systems, with broad FIX version support and an active issue tracker/release cadence. |
| [**QuickFIX/Go**](https://github.com/quickfixgo/quickfix) | 897 | Go | 🟢 | Native Go FIX session/message handling for building custom order-routing gateways. |
| [**QuickFIX/n**](https://github.com/connamara/quickfixn) | 527 | C# | 🟢 | Production FIX connectivity for .NET trading infrastructure. |
| [**quickfix-python-samples**](https://github.com/rinlevan/quickfix-python-samples) | 94 | Python | 🟢 | Getting a minimal working Python FIX initiator/acceptor running quickly on top of the official QuickFIX C++/Python bindings. |

### TradingView webhook bridges

<sub>📖 [Full explainers & limitations →](docs/live_trading.md#tradingview-webhook-bridges)</sub>

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**RogerThat (TradingView -> Hummingbot bridge)**](https://github.com/TheHolyRoger/RogerThat) | 61 | Python | 🟡 | Turning TradingView Pine Script alerts into live Hummingbot order actions without writing a custom webhook receiver. |
| [**tv2alpaca**](https://github.com/Juicestus/tv2alpaca) | 2 | Python | 🔴 | Minimal reference implementation for a TradingView-to-Alpaca webhook relay. |
| [**traderouter (TradingView -> NinjaTrader 8 bridge)**](https://github.com/roydufek/traderouter) | 0 | C# | 🟢 | Low-latency TradingView alert to NinjaTrader 8 order routing with multi-account trade copying. |

### Other

<sub>📖 [Full explainers & limitations →](docs/live_trading.md#other)</sub>

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**awesome-systematic-trading**](https://github.com/wangzhe3224/awesome-systematic-trading) | 3.2k | unknown | 🟢 | Cross-referencing execution/live-trading frameworks across many languages and asset classes in one place, with explicit 'Live Trading' tagging for frameworks that actually support it (vs. backtest-only). |
| [**awesome-crypto-trading-bots**](https://github.com/botcrypto-io/awesome-crypto-trading-bots) | 2.5k | unknown | 🟢 | Quickly surveying the crypto trading bot landscape by category (frameworks, backtesting, exchange APIs, indicators). |
| [**MicroTrendsLtd/NinjaTrader8**](https://github.com/MicroTrendsLtd/NinjaTrader8) | 113 | C# | 🟡 | Extending NinjaTrader 8's own execution engine with community strategies/indicators for futures and equities day trading. |

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

<sub>📖 [Full explainers & limitations →](docs/prediction_markets.md#kalshi)</sub>

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

### Polymarket

<sub>📖 [Full explainers & limitations →](docs/prediction_markets.md#polymarket)</sub>

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

### Cross-venue & unified SDKs

<sub>📖 [Full explainers & limitations →](docs/prediction_markets.md#cross-venue--unified-sdks)</sub>

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

### Forecasting agents

<sub>📖 [Full explainers & limitations →](docs/prediction_markets.md#forecasting-agents)</sub>

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

### Data & datasets

<sub>📖 [Full explainers & limitations →](docs/prediction_markets.md#data--datasets)</sub>

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**Jon-Becker/prediction-market-analysis**](https://github.com/Jon-Becker/prediction-market-analysis) | 3.9k | Python | 🟢 | Largest known public Kalshi + Polymarket market/trade dataset, paired with an active collection framework. |
| [**poly_data**](https://github.com/warproxxx/poly_data) | 2.3k | Python | 🟢 | High-star, actively maintained data pipeline for structured Polymarket market/trade data. |
| [**prediction-market-backtesting**](https://github.com/evan-kolberg/prediction-market-backtesting) | 1.2k | Python | 🟢 | Brings prediction-market backtesting into a mature, professionally-built trading engine (NautilusTrader) rather than reinventing backtest infrastructure. |
| [**Polymarket_data (SII-WANGZJ)**](https://github.com/SII-WANGZJ/Polymarket_data) | 831 | Python | 🟢 | Extremely large (1.1B record) trade-level dataset with multiple pre-processed views, useful for behavioral/microstructure research. |
| [**polyledger**](https://github.com/nahrek/polyledger) | 623 | Python | 🟢 | Simple, portable SQL-queryable Polymarket dataset (single DuckDB file) built via a resumable indexer. |
| [**prediction-market-mcp**](https://github.com/JamesANZ/prediction-market-mcp) | 36 | TypeScript | 🟢 | Simple unified read-only data access across three major venues (Polymarket, PredictIt, Kalshi) for MCP clients. |
| [**Prediction-Markets-Data (arbbets)**](https://github.com/arbbets/Prediction-Markets-Data) | 7 | unknown | 🟢 | Rare single tool spanning four venues including the less-covered PredictIt and Limitless Exchange. |

### Sports odds

<sub>📖 [Full explainers & limitations →](docs/prediction_markets.md#sports-odds)</sub>

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**NBA-Machine-Learning-Sports-Betting**](https://github.com/kyleskom/NBA-Machine-Learning-Sports-Betting) | 1.7k | Python | 🟢 | Popular, actively maintained NBA outcome-prediction pipeline with a large existing user community for reference/comparison. |
| [**sports-betting (georgedouzas)**](https://github.com/georgedouzas/sports-betting) | 799 | Python | 🟢 | Mature, well-documented odds/value-betting modeling library with real historical datasets and scikit-learn integration. |
| [**polymarket-tennis**](https://github.com/livetennisapi/polymarket-tennis) | 315 | Python | 🟢 | Clean live-score-to-market matching pipeline specifically for tennis, a niche well-covered event-market category. |
| [**flumine**](https://github.com/betcode-org/flumine) | 245 | Python | 🟢 | Battle-tested strategy/backtest/live architecture for exchange-style betting markets, directly analogous to prediction-market CLOBs. |

### Other venues (Manifold, PredictIt, Limitless, DFlow…)

<sub>📖 [Full explainers & limitations →](docs/prediction_markets.md#other-venues-manifold-predictit-limitless-dflow)</sub>

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

<sub>📖 [Full explainers & limitations →](docs/options.md#pricing-libraries)</sub>

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

### Volatility surfaces

<sub>📖 [Full explainers & limitations →](docs/options.md#volatility-surfaces)</sub>

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**VolGAN**](https://github.com/milenavuletic/VolGAN) | 115 | Python | 🟠 | Generating plausible, arbitrage-free synthetic IV surfaces for scenario analysis and risk simulation. |
| [**crypto-volatility-surface**](https://github.com/joshuapjacob/crypto-volatility-surface) | 78 | Python | 🟠 | Turnkey, visually clean crypto (Binance) IV surface dashboard. |
| [**vol-surface-visualizer**](https://github.com/dwasse/vol-surface-visualizer) | 63 | Python | 🟠 | Simple, well-known starting point for crypto options IV surface plotting. |
| [**VolaSurfer**](https://github.com/Baerenstein/VolaSurfer) | 12 | Python | 🟢 | Multi-asset (equity + crypto) implied vol surface visualization with pluggable data sources. |
| [**Stochastic-Volatility-Inspired Model (Idriss-Afra)**](https://github.com/Idriss-Afra/Stochastic-Volatility-Inspired-Model) | 11 | Jupyter Notebook | 🟢 | Practical, currently-maintained walkthrough of fitting SVI to real listed equity option data. |
| [**Arbitrage-free SVI volatility surfaces**](https://github.com/FinancialEngineerLab/Arbitrage-free-SVI-volatility-surfaces) | 6 | Python | 🟠 | Clear, paper-faithful implementation of the arbitrage-free SVI calibration recipe. |
| [**ssvi**](https://github.com/arkonique/ssvi) | 6 | Jupyter Notebook | 🟢 | End-to-end SSVI surface calibration pipeline from raw option-chain CSVs to a fitted surface. |

### Options backtesting

<sub>📖 [Full explainers & limitations →](docs/options.md#options-backtesting)</sub>

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**optopsy**](https://github.com/goldspanlabs/optopsy) | 1.5k | Python | 🟢 | Fast, statistics-first backtesting across large families of options strategies (condors, spreads, calendars) with delta targeting. |
| [**OptionSuite**](https://github.com/sirnfs/OptionSuite) | 299 | Python | 🟢 | Bridging the backtest-to-live gap by sharing strategy logic between historical simulation and live trading. |
| [**bhav**](https://github.com/rajmaurya0904/bhav) | 26 | Python | 🟢 | Realistic-cost NSE index/stock options backtesting for the Indian market, an underserved niche in most Western tools. |
| [**optopsy-mcp**](https://github.com/goldspanlabs/optopsy-mcp) | 20 | Rust | 🟢 | Fast Rust-native options backtesting exposed as an MCP tool for AI-agent-driven research workflows. |
| [**gex-backtesting**](https://github.com/emlama/gex-backtesting) | 11 | Jupyter Notebook | 🟢 | Bridging gamma-exposure analytics with an actual 0DTE backtesting dataset/workflow. |

### Greeks & risk

<sub>📖 [Full explainers & limitations →](docs/options.md#greeks--risk)</sub>

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**deribit-position-greeks**](https://github.com/cryptarbitrage-code/deribit-position-greeks) | 47 | Python | 🟠 | Simple, direct portfolio-Greeks aggregation for Deribit BTC/ETH options accounts. |
| [**options-scanner**](https://github.com/jwolberg/options-scanner) | 36 | JavaScript | 🟢 | Multi-ticker at-a-glance view combining GEX, skew and dealer-positioning signals with LLM-assisted interpretation. |
| [**traders-edge-mcp**](https://github.com/jsconiers/traders-edge-mcp) | 2 | Python | 🟢 | Broad, key-less 0DTE risk/positioning dashboard (GEX, vanna, charm, expected move) usable directly by AI coding agents via MCP. |
| [**flashalpha-mcp**](https://github.com/FlashAlpha-lab/flashalpha-mcp) | 1 | — | 🟢 | Turning a commercial options-analytics API into an agent-callable MCP tool for GEX/Greeks/vol-surface queries. |

### Gamma exposure (GEX)

<sub>📖 [Full explainers & limitations →](docs/options.md#gamma-exposure-gex)</sub>

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

### Volatility trading

<sub>📖 [Full explainers & limitations →](docs/options.md#volatility-trading)</sub>

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**arch**](https://github.com/bashtage/arch) | 1.6k | Python | 🟢 | Rigorous statistical volatility forecasting (GARCH/EGARCH/realized vol) that feeds VRP and vol-trading signals. |
| [**eigenquant53/VRP**](https://github.com/eigenquant53/VRP) | 33 | Python | 🟠 | Concrete, backtested implementation of VIX term-structure-based volatility trading logic. |
| [**trading-volatility**](https://github.com/peterchettiar/trading-volatility) | 11 | Jupyter Notebook | 🟠 | Clear, notebook-based exposition of VIX-term-structure trading logic for learning/research. |

### Options data

<sub>📖 [Full explainers & limitations →](docs/options.md#options-data)</sub>

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**python-tradier**](https://github.com/cablehead/python-tradier) | 42 | Python | 🟠 | Historical reference for basic Tradier REST API access from Python. |
| [**options_scraper**](https://github.com/aosingh/options_scraper) | 11 | Python | 🟠 | Zero-cost, key-less access to a basic public options chain for prototyping. |
| [**tradier-api (mikecao)**](https://github.com/mikecao/tradier-api) | 10 | JavaScript | 🟠 | Only notable Node.js option for Tradier API access among the projects surveyed. |
| [**orats-python (FyZyX)**](https://github.com/FyZyX/orats-python) | 7 | Python | 🟠 | Straightforward Python access to ORATS' options-analytics and historical IV datasets. |
| [**flashalpha-python**](https://github.com/FlashAlpha-lab/flashalpha-python) | 6 | Python | 🟢 | One-stop SDK for a broad set of derived options analytics (GEX/DEX/VEX/flow/VRP) beyond raw chain data. |
| [**openbb-orats**](https://github.com/jjfantini/openbb-orats) | 4 | Python | 🟠 | Bringing commercial ORATS options data into the free, extensible OpenBB terminal ecosystem. |

### Crypto options

<sub>📖 [Full explainers & limitations →](docs/options.md#crypto-options)</sub>

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**Derbit-Volatility-Visulization**](https://github.com/pengjin2/Derbit-Volatility-Visulization) | 84 | Python | 🟠 | Well-known early reference for visualizing Deribit crypto options IV. |
| [**delta_hedge**](https://github.com/schepal/delta_hedge) | 76 | Python | 🟠 | Concrete, working example of automated delta-hedging logic against a live crypto options exchange. |
| [**deribit_data_collector**](https://github.com/schepal/deribit_data_collector) | 75 | Python | 🟠 | Simple, complete Deribit option-chain snapshotting for BTC/ETH. |
| [**deribit-rs**](https://github.com/dovahcrow/deribit-rs) | 49 | Rust | 🟠 | Idiomatic, typed Rust access to Deribit's v2 WebSocket API for low-latency crypto options systems. |
| [**deribit-historical-data**](https://github.com/RiveChen/deribit-historical-data) | 40 | Python | 🟢 | Current, working access to Deribit's historical options/futures trade-tape API. |

### Other

<sub>📖 [Full explainers & limitations →](docs/options.md#other)</sub>

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**opstrat**](https://github.com/hashABCD/opstrat) | 168 | Python | 🟠 | Quick, clean payoff-diagram plotting for any multi-leg options strategy combination. |
| [**LoopTrader**](https://github.com/pattertj/LoopTrader) | 129 | Python | 🟠 | Well-structured, extensible architecture for building custom options trading bots. |
| [**awesome-options-analytics**](https://github.com/FlashAlpha-lab/awesome-options-analytics) | 44 | — | 🟢 | A single, actively-updated jumping-off point specifically for options/derivatives analytics tools. |
| [**alpaca-options-framework**](https://github.com/milgar7969/alpaca-options-framework) | 22 | Python | 🟢 | Actively maintained, Alpaca-specific scaffolding that captures real-world API gotchas for live options bots. |
| [**thales**](https://github.com/cm-jones/thales) | 11 | C++ | 🟠 | One of the few actively-designed C++ (rather than Python) open-source options trading bots. |

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

<sub>📖 [Full explainers & limitations →](docs/ai_agents.md#llm-multi-agent-frameworks)</sub>

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

### Alpha mining

<sub>📖 [Full explainers & limitations →](docs/ai_agents.md#alpha-mining)</sub>

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**RD-Agent (incl. RD-Agent(Q))**](https://github.com/microsoft/RD-Agent) | 14.7k | Python | 🟢 | Fully automating the propose-code-backtest-refine cycle for both alpha factors and predictive models rather than just one or the other. |
| [**QuantaAlpha**](https://github.com/QuantaAlpha/QuantaAlpha) | 1.5k | Python | 🟢 | Turning a plain-language research hypothesis into an automatically evolved and backtested set of alpha factors. |
| [**AlphaGen**](https://github.com/ICT-FinD-Lab/alphagen) | 1.2k | Python | 🟢 | Producing compact, human-readable alpha expressions (rather than black-box embeddings) whose combined predictive power is explicitly optimized. |
| [**QuantEvolve**](https://github.com/tarsyang/quantevolve) | 50 | Python | 🟠 | Producing a diverse portfolio of strategy candidates spanning different risk/return profiles instead of a single best strategy. |
| [**alpha-agent (zzzhhn)**](https://github.com/zzzhhn/alpha-agent) | 1 | Python | 🟢 | A-share-specific factor discovery workflow. |

### Reinforcement learning

<sub>📖 [Full explainers & limitations →](docs/ai_agents.md#reinforcement-learning)</sub>

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**TensorTrade**](https://github.com/tensortrade-org/tensortrade) | 7.1k | Python | 🟢 | Highly modular composition of RL trading pipelines when you want fine control over exchange/reward/action abstractions. |
| [**ElegantRL**](https://github.com/AI4Finance-Foundation/ElegantRL) | 4.4k | Python | 🟢 | Fast, cloud/GPU-scalable RL training that plugs into FinRL-style trading environments. |
| [**FinRL-Trading / FinRL-X**](https://github.com/AI4Finance-Foundation/FinRL-Trading) | 3.7k | Python | 🟢 | Bridging RL-trained policies to live paper/real brokerage execution. |
| [**TradeMaster**](https://github.com/TradeMaster-NTU/TradeMaster) | 3.1k | Jupyter Notebook | 🟠 | Breadth: one platform spanning multiple markets, trading scenarios and RL algorithms with built-in evaluation/visualization. |
| [**TradingGym**](https://github.com/Yvictor/TradingGym) | 1.9k | Python | 🟠 | Simple, dependency-light Gym environment for quick RL-trading prototyping. |
| [**FinRL_DeepSeek**](https://github.com/benstaf/FinRL_DeepSeek) | 331 | Jupyter Notebook | 🟠 | A concrete, reproducible template for combining LLM-derived news sentiment/risk signals with classic RL trading (rather than pure end-to-end LLM decision-making). |

### ML trading

<sub>📖 [Full explainers & limitations →](docs/ai_agents.md#ml-trading)</sub>

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**Stock-Prediction-Models**](https://github.com/huseinzol05/Stock-Prediction-Models) | 9.5k | Jupyter Notebook | 🟠 | Breadth of example implementations for many classic and deep ML forecasting techniques applied to stocks in one place. |
| [**stockpredictionai**](https://github.com/borisbanushev/stockpredictionai) | 5.6k | JavaScript | 🟠 | Approachable, well-explained walkthrough of applying GANs to time-series price prediction. |
| [**Numerai example-scripts**](https://github.com/numerai/example-scripts) | 1.2k | Jupyter Notebook | 🟢 | A real, ongoing live proving-ground for ML models against actual market-neutral hedge fund capital, with obfuscated data avoiding overfitting-to-known-tickers. |

### Foundation models

<sub>📖 [Full explainers & limitations →](docs/ai_agents.md#foundation-models)</sub>

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**Kronos**](https://github.com/shiyu-coder/Kronos) | 39.3k | Python | 🟢 | Purpose-built representation learning/forecasting over raw candlestick data across many exchanges and assets, with released fine-tuning scripts. |
| [**TimesFM**](https://github.com/google-research/timesfm) | 33.4k | Python | 🟢 | Fast, strong zero-shot forecasts across varied frequencies/domains at large scale. |
| [**Chronos**](https://github.com/amazon-science/chronos-forecasting) | 5.9k | Python | 🟢 | Strong zero-shot forecasting performance across arbitrary time series without per-series retraining. |
| [**Moirai (uni2ts)**](https://github.com/SalesforceAIResearch/uni2ts) | 1.6k | Jupyter Notebook | 🟢 | Handling multivariate series of arbitrary dimension/frequency with one pretrained model, reducing per-series engineering. |

### MCP servers

<sub>📖 [Full explainers & limitations →](docs/ai_agents.md#mcp-servers)</sub>

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**Financial Datasets MCP Server**](https://github.com/financial-datasets/mcp-server) | 2.3k | Python | 🟠 | Clean, purpose-built tool surface for company fundamentals plus prices/news in one MCP server. |
| [**Alpaca MCP Server**](https://github.com/alpacahq/alpaca-mcp-server) | 978 | Python | 🟢 | First-party, broker-maintained MCP integration that connects an LLM agent directly to real order placement and account data. |
| [**mcp_massive (formerly mcp_polygon)**](https://github.com/massive-com/mcp_massive) | 391 | Python | 🟢 | Broad, first-party coverage of multi-asset-class market data as MCP tools for any LLM agent. |
| [**yahoo-finance-mcp**](https://github.com/Alex2Yang97/yahoo-finance-mcp) | 354 | Python | 🟢 | Free, no-API-key market/fundamentals data access for LLM agents, good for prototyping without cost. |
| [**ibkr-mcp-server (ArjunDivecha)**](https://github.com/ArjunDivecha/ibkr-mcp-server) | 35 | Python | 🟠 | Bringing a full-featured brokerage (multi-account, options, short-selling) to MCP clients, unlike the many minimal IBKR MCP forks. |

### Benchmarks

<sub>📖 [Full explainers & limitations →](docs/ai_agents.md#benchmarks)</sub>

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

### Uses Jev (TypeSafe)

<sub>📖 [Full explainers & limitations →](docs/ai_agents.md#uses-jev-typesafe)</sub>

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

### Lists & other

<sub>📖 [Full explainers & limitations →](docs/ai_agents.md#lists--other)</sub>

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**awesome-ai-in-finance**](https://github.com/georgezouq/awesome-ai-in-finance) | 6.6k | n/a | 🟢 | Broad, long-standing, well-organized index of the ML/AI-in-finance ecosystem (not LLM-agent specific like LLMQuant's list). |
| [**awesome-trading-agents (LLMQuant)**](https://github.com/LLMQuant/awesome-trading-agents) | 829 | n/a | 🟢 | Fast discovery of new LLM-trading-agent and trading-MCP-server projects as they appear. |
| [**Awesome-LLM-Quantitative-Trading-Papers**](https://github.com/Tom-roujiang/Awesome-LLM-Quantitative-Trading-Papers) | 246 | n/a | 🟢 | Tracking the academic paper trail behind this fast-moving research area. |
| [**Awesome-MFFMs**](https://github.com/Open-Finance-Lab/Awesome-MFFMs) | 47 | n/a | 🟢 | Focused index of the narrower multimodal-financial-foundation-model niche within the broader financial-LLM landscape. |

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

<sub>📖 [Full explainers & limitations →](docs/fundamental_data.md#sec-filings--xbrl)</sub>

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

### Valuation

<sub>📖 [Full explainers & limitations →](docs/fundamental_data.md#valuation)</sub>

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**Business Valuation with DCF in Python**](https://github.com/farbodbahari/Business-Valuation-with-Discounted-Cash-Flow-In-Python) | 176 | Jupyter Notebook | 🟠 | Clear, well-commented reference implementation of the classic Damodaran DCF approach for learning or adapting. |
| [**DCF Valuation Model (Monte Carlo)**](https://github.com/EmanueleSturzo/DCF-Valuation-Model) | 3 | Python | 🟢 | Producing a valuation range/distribution rather than one number, useful for risk-aware fundamental analysis. |
| [**dcfBuilder**](https://github.com/mgayatri77/dcfBuilder) | 1 | Python | 🟠 | Quickly generating an editable, Excel-native DCF scaffold from live SEC data instead of building one from scratch. |
| [**DCF Dashboard**](https://github.com/nostreet123/DCF-Dashboard) | 1 | TypeScript | 🟢 | Giving non-Excel users (or teams wanting shareable links) a browser-based DCF workflow with saved-run history. |
| [**aswath (DCF models)**](https://github.com/SimeonChan/aswath) | 0 | Python | 🟠 | Illustrating how Damodaran's spreadsheet logic translates into Python data structures. |

### Earnings transcripts

<sub>📖 [Full explainers & limitations →](docs/fundamental_data.md#earnings-transcripts)</sub>

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**Earnings-Calls-NLP**](https://github.com/cdubiel08/Earnings-Calls-NLP) | 76 | Jupyter Notebook | 🟠 | Demonstrating an end-to-end pipeline from raw transcript text to a discrete trading signal. |
| [**Stock Earnings Call Transcript NLP**](https://github.com/personal-coding/Stock-Earnings-Call-Transcript-Natural-Language-Processing) | 14 | Python | 🟠 | Tying transcript NLP features directly to a documented, published research methodology with a backtest. |
| [**Earnings Call NLP Strategy V2**](https://github.com/Vxtr10/Earnings-Call-NLP-Strategy-V2) | 2 | Jupyter Notebook | 🟠 | Broad feature-engineering menu (FinBERT + complexity + similarity) for anyone building their own transcript-alpha model. |
| [**Earnings Call NLP Lab**](https://github.com/Cubiczan/earnings-call-nlp-lab) | 0 | Python | 🟢 | Longitudinal tone/evasiveness tracking per company across many quarters, not just single-transcript sentiment scoring. |

### Ownership & insider

<sub>📖 [Full explainers & limitations →](docs/fundamental_data.md#ownership--insider)</sub>

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

### Market-data SDKs

<sub>📖 [Full explainers & limitations →](docs/fundamental_data.md#market-data-sdks)</sub>

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

### Tick & time-series storage

<sub>📖 [Full explainers & limitations →](docs/fundamental_data.md#tick--time-series-storage)</sub>

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**TimescaleDB**](https://github.com/timescale/timescaledb) | 23.6k | C | 🟢 | Getting time-series performance for OHLCV/tick data while staying on plain Postgres, so existing SQL tooling, ORMs, and BI tools keep working unchanged. |
| [**QuestDB**](https://github.com/questdb/questdb) | 17.3k | Java | 🟢 | Extremely fast ingest and SQL analytics on high-volume tick/order-book data, often positioned as a practical open-source kdb+ alternative. |
| [**Arctic (legacy)**](https://github.com/man-group/arctic) | 3.1k | Python | 🟠 | Battle-tested MongoDB-backed tick storage for teams already running Mongo infrastructure. |
| [**ArcticDB**](https://github.com/man-group/ArcticDB) | 2.5k | C++/Python | 🟢 | Storing and version-controlling large historical price/fundamentals DataFrames with pandas-native ergonomics and no separate database server to run. |
| [**DolphinDB Tutorials**](https://github.com/dolphindb/Tutorials_EN) | 28 | Python | 🟠 | kdb+-style vectorized time-series analytics without the kdb+ licensing cost, including built-in streaming engines for real-time tick processing. |

### News & sentiment

<sub>📖 [Full explainers & limitations →](docs/fundamental_data.md#news--sentiment)</sub>

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

### Alternative data

<sub>📖 [Full explainers & limitations →](docs/fundamental_data.md#alternative-data)</sub>

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**PRAW**](https://github.com/praw-dev/praw) | 4.3k | Python | 🟢 | Reliable, well-documented, actively-maintained access to Reddit's official API, avoiding fragile HTML scraping for WSB/retail-sentiment data collection. |
| [**pytrends**](https://github.com/GeneralMills/pytrends) | 3.7k | Python | 🟠 | Free, simple access to Google Trends search-volume data, the foundational input for many search-interest trading-signal studies (following academic work by Preis, Moat & Stanley). |
| [**gdeltPyR**](https://github.com/linwoodc3/gdeltPyR) | 257 | Jupyter Notebook | 🟠 | Free access to an enormous, continuously-updated global news-event and sentiment/tone database far beyond company-specific headlines. |
| [**QuiverQuant Python API**](https://github.com/Quiver-Quantitative/python-api) | 58 | Python | 🟢 | One-stop access to a very wide basket of alt-data signals (congress, lobbying, WSB, dark pools, patents) that would otherwise require building a dozen separate scrapers. |
| [**Google Trends Financial Modeling**](https://github.com/evilpegasus/google-trends-financial-modeling) | 16 | Jupyter Notebook | 🟠 | Clear, minimal worked example of turning Trends data into an index-prediction feature set. |

### Screeners

<sub>📖 [Full explainers & limitations →](docs/fundamental_data.md#screeners)</sub>

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**finvizfinance**](https://github.com/lit26/finvizfinance) | 1.7k | Python | 🟢 | Very quick fundamental screening (P/E, margins, growth, etc.) plus a bonus insider-trading feed, all from Finviz's well-curated free data. |
| [**TradingView-Screener**](https://github.com/shner-elmo/TradingView-Screener) | 1.3k | Python | 🟢 | Access to TradingView's very broad global fundamentals+technicals screening fields without needing a scraping layer of your own. |
| [**PKScreener**](https://github.com/pkjmesra/PKScreener) | 397 | Python | 🟢 | Deep coverage of NSE-specific breakout and consolidation screening logic, filling a gap most US-centric screeners don't cover. |

### Other

<sub>📖 [Full explainers & limitations →](docs/fundamental_data.md#other)</sub>

| Project | ★ | Lang | | What it's good at |
|---|---:|---|:-:|---|
| [**filib (Factor Investing Library)**](https://github.com/prmkowalski/filib) | 29 | Python | 🟠 | Quick iteration on custom fundamental factor definitions and their portfolio-level rebalancing performance. |

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

<sub>🔧 [How to recreate each →](docs/papers.md#earnings-events--pead)</sub>

| Year | Paper | Strategy | Reported return | Sharpe | Net of costs | OOS | Code |
|---|---|---|---|---|:-:|:-:|:-:|
| 2026 | [Fast Numbers, Slow Language: Bridging Quantitative and Qualitative Earnings Signals](https://arxiv.org/pdf/2606.29734)<br><sub>arXiv q-fin</sub> | Combines fast-moving numeric earnings-surprise signals with slower-to-process qualitative (text) earnings signals, likely arguing the two convey complementary and non-redundant information for post-earnings drift.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2025 | [FinCall-Surprise: A Large-Scale Multi-Modal Benchmark for Earning Surprise Prediction](https://arxiv.org/abs/2510.03965)<br><sub>arXiv q-fin/cs.CL</sub> | Benchmark dataset/task for predicting earnings surprises from multi-modal earnings-call data (audio + transcript + numeric fundamentals), used to evaluate models' ability to forecast whether next-quarter EPS beats or misses consensus.<br><sub>Large-scale earnings-call dataset (exact coverage not captured)</sub> | — | — | ❔ | ❔ |  |
| 2025 | [Extracting the Structure of Press Releases for Predicting Earnings Announcement Returns](https://arxiv.org/abs/2509.24254)<br><sub>arXiv q-fin</sub> | Uses the structural/formatting features of earnings press releases (not just their sentiment content) as a predictor of the announcement-window stock return.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2025 | [LLM-Driven Investment Models: Can Large Language Models Extract Alpha from Earnings Call Transcripts?](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6351439)<br><sub>SSRN 6351439</sub> | Uses LLM embeddings of earnings-call transcripts as investment signals, testing whether the language-derived representation contains return-predictive information beyond traditional numeric/fundamental features.<br><sub>More than 14,000 earnings-call events, 2019-2023</sub> | — | LLM-embedding-based signals reported to produce stronger risk-adjusted performance than traditional approaches, though exact Sharpe/return figures not captured in this pass | ❔ | ❔ |  |
| 2025 | [Agentic Retrieval of Topics and Insights from Earnings Calls](https://arxiv.org/html/2507.07906v1)<br><sub>arXiv q-fin</sub> | An LLM-agent pipeline (Topic Retriever + Ontologist) that discovers and maintains a hierarchical ontology of financially relevant topics across earnings calls, building a structured knowledge graph (3,200 nodes from 141 transcripts in the reported experiment) rather than a flat sentiment score.<br><sub>141 earnings-call transcripts</sub> | — | — | ❔ | ❔ |  |
| 2023 | [PEAD.txt: Post-Earnings-Announcement Drift Using Text](https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/peadtxt-postearningsannouncementdrift-using-text/5EB217BB68B5FB054FE38541BAAC4679)<br><sub>Journal of Financial and Quantitative Analysis</sub> | Defines earnings surprise using a text-based measure derived from earnings-call transcripts/press releases (rather than the standard analyst-consensus EPS surprise), and shows a long-short PEAD strategy sorted on this text-based surprise produces stronger post-earnings drift than surprise-based on numbers alone.<br><sub>US earnings announcements, 2008-2019</sub> | text-based PEAD strategy generates drift of about 1.11%-2.87% over the post-announcement window (varies by exact text specification), versus smaller drift (~1.65%) from alternative text/quintile-spread measures | — | ❌ | ❔ |  |

### Analyst revisions

<sub>🔧 [How to recreate each →](docs/papers.md#analyst-revisions)</sub>

| Year | Paper | Strategy | Reported return | Sharpe | Net of costs | OOS | Code |
|---|---|---|---|---|:-:|:-:|:-:|
| 2025 | [Corporate Earnings Calls and Analyst Beliefs](https://arxiv.org/pdf/2511.15214)<br><sub>arXiv q-fin</sub> | Studies how earnings-call content updates sell-side analyst beliefs (and by extension, subsequent forecast revisions), relevant to designing an analyst-revision-anticipation signal from call transcripts.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2023 | [Earnings Forecasts and Revisions, Price Momentum, and Fundamental Data (chapter overview of AQR-style earnings-revision composites)](https://go.factset.com/hubfs/Symposium%20Images/Guerard_EARNINGS%20FORECASTS%20AND%20REVISIONS,%20PRICE%20MOMENTUM,%20AND%20FUNDAMENTAL%20DATA.pdf)<br><sub>Book chapter / FactSet symposium material</sub> | Composite of earnings momentum (trailing EPS growth), analyst estimate revisions (recent up/down revisions to consensus), and margin growth, combined with price momentum into a 'fundamental momentum' factor used by AQR and others; long stocks with positive revision momentum, short those with negative.<br><sub>US and global equities, multi-decade practitioner use</sub> | — | — | ❔ | ❔ |  |

### Momentum

<sub>🔧 [How to recreate each →](docs/papers.md#momentum)</sub>

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

### Value & quality

<sub>🔧 [How to recreate each →](docs/papers.md#value--quality)</sub>

| Year | Paper | Strategy | Reported return | Sharpe | Net of costs | OOS | Code |
|---|---|---|---|---|:-:|:-:|:-:|
| 2025 | [A New Quality Factor Adjusted by Fraud Probability](https://www.sciencedirect.com/science/article/abs/pii/S1544612325004167)<br><sub>Finance Research Letters, Vol. 78</sub> | Modifies the standard Quality-Minus-Junk factor by down-weighting/excluding firms with a high estimated probability of financial-statement fraud (via a bivariate probit model that accounts for undetected fraud), producing a 'fraud-mitigated QMJ' (fmQMJ) factor.<br><sub>China and US equities</sub> | fmQMJ portfolio earns significant average excess returns in both China and the US, and outperforms the original QMJ factor specifically within low-size and low-book-to-market subgroups | — | ❔ | ❔ |  |
| 2019 | [Quality Minus Junk](http://www.econ.yale.edu/~shiller/behfin/2013_04-10/asness-frazzini-pedersen.pdf)<br><sub>Review of Accounting Studies (working paper circulated 2013+)</sub> | Blends multiple quality sub-scores -- profitability, growth, safety (low leverage/low earnings volatility/low beta), and payout/management quality -- into a single composite Quality-Minus-Junk (QMJ) factor; long high-quality stocks, short low-quality ('junk'), often combined with value.<br><sub>US and international equities, multi-decade sample (1957-2016 in later AQR data updates)</sub> | — | — | ❌ | ❌ |  |
| 2014 | [Betting Against Beta](https://www.aqr.com/-/media/AQR/Documents/Insights/BAB.pdf)<br><sub>Journal of Financial Economics</sub> | Constructs a leverage-adjusted, beta-neutral long-short portfolio: long low-beta stocks (levered up to unit beta), short high-beta stocks (delevered to unit beta), designed to exploit leverage-constrained investors' tendency to overweight high-beta stocks and thus underprice low-beta ones.<br><sub>US and 19 other international equity markets, plus Treasury bonds, credit and futures, multi-decade sample</sub> | — | — | ❌ | ❌ |  |
| 2013 | [The Gross Profitability Premium](https://mysimon.rochester.edu/novy-marx/research/OSoV.pdf)<br><sub>Journal of Financial Economics</sub> | Sorts stocks on gross profitability (revenue minus cost of goods sold, scaled by total assets) as a cleaner, less-manipulable profitability/quality measure than net income; long high gross-profitability stocks, short low, often combined with a value tilt ('the other side of value').<br><sub>US equities, 1963-2010</sub> | profitable-minus-unprofitable long-short spread has a Fama-French-3-factor alpha of about 0.52% per month (t-stat 4.49); a 2015 international extension found an average annual profitability premium of about 3.6% across 15 European markets, 1982-2014 | — | ❌ | ❌ |  |
| 1996 | [Do Stock Prices Fully Reflect Information in Accruals and Cash Flows About Future Earnings? (the accrual anomaly)](https://www.jstor.org/stable/248290)<br><sub>The Accounting Review</sub> | Sorts stocks on the accrual component of earnings (earnings minus operating cash flow, scaled by assets); long low-accrual (cash-flow-backed earnings) stocks, short high-accrual (earnings management-prone) stocks, based on evidence that the market underreacts to the lower persistence of accruals vs. cash flows.<br><sub>US equities, 1962-1991 (original); a 1972-2010 replication finds similar magnitude</sub> | a low-minus-high total-accruals long-short portfolio earns a significant average return of about 0.71% per month (~8.5% annualized) in a 1972-2010 replication | — | ❌ | ❌ |  |

### Fundamental composites

<sub>🔧 [How to recreate each →](docs/papers.md#fundamental-composites)</sub>

| Year | Paper | Strategy | Reported return | Sharpe | Net of costs | OOS | Code |
|---|---|---|---|---|:-:|:-:|:-:|
| 2020 | [Value Investing Research: Simple Methods to Improve the Piotroski F-Score](https://alphaarchitect.com/value-investing-research-simple-methods-to-improve-the-piotroski-f-score/)<br><sub>Alpha Architect blog</sub> | Tests simple modifications to Piotroski's original 9-signal F-Score (profitability, leverage/liquidity, operating efficiency binary signals) to improve its ability to separate future winners from losers among cheap (high book-to-market) value stocks.<br><sub>US equities (value/high-B/M universe)</sub> | — | — | ❔ | ❔ |  |

### Factor timing & crowding

<sub>🔧 [How to recreate each →](docs/papers.md#factor-timing--crowding)</sub>

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

### Short interest & borrow

<sub>🔧 [How to recreate each →](docs/papers.md#short-interest--borrow)</sub>

| Year | Paper | Strategy | Reported return | Sharpe | Net of costs | OOS | Code |
|---|---|---|---|---|:-:|:-:|:-:|
| 2025 | [Anomalies and Their Short-Sale Costs](https://onlinelibrary.wiley.com/doi/10.1111/jofi.13501)<br><sub>Journal of Finance, Vol. 80(6), pp. 3639-3694</sub> | Re-tests 162 published cross-sectional anomalies after adjusting the short leg's return for actual stock-borrow (loan) fees rather than assuming free shorting.<br><sub>US equities, borrow-fee data 2006-2019 (or similar; anomaly universe per original papers)</sub> | average long-short anomaly return is 0.14% per month before short-sale costs, but only -0.01% per month once adjusted for stock borrow fees; profits vanish even before fees if the ~12% of high-borrow-fee stock-days are excluded | — | ✅ | ❔ |  |
| 2019 | [The Loan Fee Anomaly: A Short Seller's Best Ideas](https://paperswithbacktest.com/strategies/the-loan-fee-anomaly-a-short-seller-s-best-ideas)<br><sub>SSRN / practitioner summary</sub> | Stocks with high (and rising) stock-loan/borrow fees are shorted by informed short sellers ('best ideas'); sorting stocks by borrow fee alone produces a stronger long-short return than sorting by 102 traditional anomaly signals.<br><sub>US equities, 2006-2019</sub> | portfolios formed on borrow fees provide larger long-short returns than portfolios formed on any of 102 compared anomalies over 2006-2019 | — | ❔ | ❔ |  |

### Options-implied signals

<sub>🔧 [How to recreate each →](docs/papers.md#options-implied-signals)</sub>

| Year | Paper | Strategy | Reported return | Sharpe | Net of costs | OOS | Code |
|---|---|---|---|---|:-:|:-:|:-:|
| 2026 | [Option-Implied Signals and Crash Risk: Predictability and Machine-Learning Evidence from U.S. Equity Options, 2015-2026](https://arxiv.org/html/2608.26115)<br><sub>arXiv:2608.26115</sub> | Constructs a daily firm-level panel of six option-implied signals (volatility smirk, IV spread, risk-neutral skewness proxy, term-structure slope, put-call volume/OI ratios) and tests their next-month return and crash-risk predictability across three macro regimes (2015-2019 low-vol, 2020-2022 high-vol, 2023-2026 AI/mega-cap), comparing linear regressions to XGBoost.<br><sub>12.36 million US equity firm-day observations across 10,026 underlyings, 2015-2026</sub> | — | — | ❌ | ✅ |  |
| 2026 | [Skewness Dispersion and Stock Market Returns](https://arxiv.org/pdf/2604.07870)<br><sub>arXiv:2604.07870</sub> | Constructs a market-wide dispersion-of-individual-stock-skewness measure (cross-sectional spread of firm-level option-implied or realized skewness) as a proxy for investor disagreement about tail risk, and studies its relation to aggregate/individual stock returns.<br><sub>Not fully captured (likely US equities/options)</sub> | — | — | ❔ | ❔ |  |
| 2025 | [Why Does Options Market Information Predict Stock Returns?](https://www.sciencedirect.com/science/article/pii/S0304405X25001618)<br><sub>Journal of Financial Economics</sub> | Tests whether the well-known predictive power of options-implied signals (volatility spread/skew) for equity returns survives once accounting for stock borrow fees; argues implied-vol signals largely proxy for the same informed-shorting information captured directly by borrow fees.<br><sub>US equities with listed options</sub> | once stock borrow fees are accounted for, strategies exploiting options-market-implied signals via short selling are 'much closer to break-even' | — | ✅ | ❔ |  |
| 2023 | [Cross-Sectional Variation of Option-Implied Volatility Skew](https://pubsonline.informs.org/doi/10.1287/mnsc.2023.4872)<br><sub>Management Science</sub> | Documents systematic cross-sectional variation in equity option-implied volatility skew (OTM put IV minus ATM call IV) and links it to expected stock returns and firm characteristics.<br><sub>US equity options market</sub> | — | — | ❔ | ❔ |  |

### Intraday & overnight

<sub>🔧 [How to recreate each →](docs/papers.md#intraday--overnight)</sub>

| Year | Paper | Strategy | Reported return | Sharpe | Net of costs | OOS | Code |
|---|---|---|---|---|:-:|:-:|:-:|
| 2025 | [Does Overnight News Explain Overnight Returns?](https://arxiv.org/abs/2507.04481)<br><sub>arXiv:2507.04481</sub> | Applies supervised topic modeling to 2.4 million news articles to identify which news topics are associated with abnormal overnight (close-to-open) versus intraday (open-to-close) returns, and uses topic prevalence/response differences to forecast which stocks will do well overnight and poorly intraday (or vice versa).<br><sub>US equities, roughly 30-year sample of news and returns</sub> | — | — | ❔ | ✅ |  |
| 2024 | [Reversals and the Returns to Liquidity Provision](https://www.nber.org/papers/w30917)<br><sub>Financial Analysts Journal 80(2), pp. 122-151 (NBER WP 30917)</sub> | Uses short-term price reversals to measure the returns earned by liquidity providers, showing reversal strength/persistence scales with size (smaller = stronger), volatility (higher = stronger) and inverse turnover (lower turnover = more persistent), consistent with reversal being compensation for market-making risk rather than a free-standing mispricing.<br><sub>US equities, multi-decade CRSP sample</sub> | — | — | ❔ | ❔ |  |
| 2022 | [They Still Haven't Told You: An Analysis of the Overnight/Intraday Anomaly's Robustness](https://arxiv.org/pdf/2201.00223)<br><sub>arXiv q-fin</sub> | Further scrutiny of the overnight/intraday return decomposition, examining robustness/explanations for why overnight returns dominate cumulative equity performance.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2020 | [Strikingly Suspicious Overnight and Intraday Returns](https://arxiv.org/pdf/2010.01727)<br><sub>arXiv q-fin</sub> | Documents that a large, often near-monotonic fraction of long-run US equity index (and many single-stock) returns is earned overnight (close-to-open) rather than intraday (open-to-close), and questions the stability/causes of this pattern.<br><sub>US equities/indices, multi-decade</sub> | over a recent 5-year window (Q3 2020-Q3 2025, per secondary sources), SPY close-to-open return was about +47.1% vs. +29.9% open-to-close; QQQ close-to-open was about +53.5% vs. +30.3% open-to-close | — | ❌ | ❔ |  |

### Statistical arbitrage

<sub>🔧 [How to recreate each →](docs/papers.md#statistical-arbitrage)</sub>

| Year | Paper | Strategy | Reported return | Sharpe | Net of costs | OOS | Code |
|---|---|---|---|---|:-:|:-:|:-:|
| 2026 | [Moira: Language-Driven Hierarchical Reinforcement Learning for Pair Trading](https://arxiv.org/pdf/2605.01954)<br><sub>arXiv q-fin</sub> | Uses natural-language (LLM-derived) guidance to inform a hierarchical RL pair-trading policy -- e.g., using LLM-parsed news/fundamentals to influence pair selection or regime detection within the RL hierarchy.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2024 | [Statistical Arbitrage in Multi-Pair Trading Strategy Based on Graph Clustering Algorithms in US Equities Market](https://arxiv.org/html/2406.10695v1)<br><sub>arXiv q-fin</sub> | Uses graph-clustering algorithms (rather than pairwise correlation/cointegration search) to identify groups of related US equities for a multi-pair statistical-arbitrage strategy, trading mean-reversion within/between clusters.<br><sub>US equities</sub> | — | — | ❔ | ❔ |  |
| 2024 | [Reinforcement Learning Pair Trading: A Dynamic Scaling Approach](https://arxiv.org/html/2407.16103v1)<br><sub>arXiv q-fin</sub> | RL agent learns to dynamically scale position size in a pairs-trading strategy (rather than using fixed z-score entry/exit thresholds), adapting exposure to the current spread regime.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2024 | [Advanced Statistical Arbitrage with Reinforcement Learning](https://arxiv.org/pdf/2403.12180)<br><sub>arXiv q-fin</sub> | General RL-based framework for statistical arbitrage, likely combining signal generation and execution/sizing within an RL policy.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2023 | [Select and Trade: Towards Unified Pair Trading with Hierarchical Reinforcement Learning](https://arxiv.org/pdf/2301.10724)<br><sub>arXiv q-fin</sub> | Hierarchical RL framework that jointly handles pair selection (which stocks to pair) and trade execution (when/how much to trade the spread) in a single unified pipeline, rather than treating selection and trading as separate stages.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2022 | [Detecting Data-Driven Robust Statistical Arbitrage Strategies with Deep Neural Networks](https://arxiv.org/html/2203.03179)<br><sub>arXiv q-fin</sub> | Uses a deep neural network to identify robust statistical-arbitrage strategies across multiple securities simultaneously, without requiring explicit pairwise cointegration testing.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |

### ML return prediction

<sub>🔧 [How to recreate each →](docs/papers.md#ml-return-prediction)</sub>

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

### LLM signals

<sub>🔧 [How to recreate each →](docs/papers.md#llm-signals)</sub>

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

### LLM trading agents

<sub>🔧 [How to recreate each →](docs/papers.md#llm-trading-agents)</sub>

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

### RL portfolio management

<sub>🔧 [How to recreate each →](docs/papers.md#rl-portfolio-management)</sub>

| Year | Paper | Strategy | Reported return | Sharpe | Net of costs | OOS | Code |
|---|---|---|---|---|:-:|:-:|:-:|
| 2026 | [Deep Reinforcement Learning Framework for Diversified Portfolio Management Across Global Equity Markets](https://arxiv.org/html/2605.17307v1)<br><sub>arXiv q-fin</sub> | DRL framework for portfolio allocation across global equity markets, optimizing a differential Sharpe ratio reward net of transaction costs; a related PPO variant is also used for options-hedging tasks comparable to Black-Scholes delta hedging.<br><sub>Global equities, not fully specified</sub> | — | — | ✅ | ❔ |  |
| 2025 | [HARLF: Hierarchical Reinforcement Learning and Lightweight LLM-Driven Sentiment Integration for Financial Portfolio Optimization](https://arxiv.org/abs/2507.18560)<br><sub>arXiv:2507.18560</sub> | Hierarchical RL portfolio-optimization framework: base RL agents process hybrid price+sentiment data per asset, meta-agents aggregate decisions across base agents, and a super-agent merges everything into final portfolio weights; sentiment comes from a lightweight LLM rather than a heavy full-scale model.<br><sub>Trained 2000-2017, evaluated out-of-sample 2018-2024</sub> | 26% annualized return | 1.2 | ❔ | ✅ |  |
| 2025 | [Risk-Aware Deep Reinforcement Learning for Dynamic Portfolio Optimization](https://arxiv.org/abs/2511.11481)<br><sub>arXiv q-fin</sub> | PPO-based DRL portfolio optimizer with a Sharpe-ratio-based reward plus explicit risk controls (max-drawdown and volatility constraints) layered on top of the RL policy.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2024 | [Markowitz Meets Bellman: Knowledge-Distilled Reinforcement Learning for Portfolio Management](https://arxiv.org/pdf/2405.05449)<br><sub>arXiv q-fin</sub> | Distills classic Markowitz mean-variance optimization knowledge into a Bellman/RL-based portfolio policy, combining the interpretability of mean-variance theory with RL's ability to adapt dynamically.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2024 | [Portfolio Management using Deep Reinforcement Learning](https://arxiv.org/abs/2405.01604)<br><sub>arXiv q-fin</sub> | Standard DRL portfolio-allocation model benchmarked against the Dow Jones Industrial Average.<br><sub>Dow Jones constituents</sub> | 25.87% annualized return on the test data (vs. the Dow Jones Industrial Average benchmark) | — | ❔ | ❔ |  |

### Alpha mining

<sub>🔧 [How to recreate each →](docs/papers.md#alpha-mining)</sub>

| Year | Paper | Strategy | Reported return | Sharpe | Net of costs | OOS | Code |
|---|---|---|---|---|:-:|:-:|:-:|
| 2026 | [AlphaMemo: Structured Search-Process Memory for Self-Evolving Alpha Mining Agents](https://arxiv.org/pdf/2606.20625)<br><sub>arXiv q-fin</sub> | Adds a structured memory of prior search processes/outcomes to an LLM-agent alpha-mining loop so the agent can learn from its own past search trajectories ('self-evolving') rather than searching from scratch each run.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2025 | [AlphaAgent: LLM-Driven Alpha Mining with Regularized Exploration to Counteract Alpha Decay](https://arxiv.org/abs/2502.16789)<br><sub>arXiv:2502.16789</sub> | LLM-agent-driven formulaic alpha search with three regularizers -- AST-based originality/similarity penalty vs. known factors, LLM-scored hypothesis-factor semantic alignment, and AST-based complexity control -- intended to produce decay-resistant alphas rather than overfit/curve-fit factors.<br><sub>CSI 500 (China) and S&P 500 (US), 4-year test spanning bull and bear regimes</sub> | — | — | ❔ | ✅ |  |
| 2025 | [R&D-Agent-Quant (RD-Agent(Q)): A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization](https://neurips.cc/virtual/2025/poster/121804)<br><sub>NeurIPS 2025 (Datasets and Benchmarks Track)</sub> | Two-stage multi-agent loop: a 'Research' stage generates hypotheses and factor/model tasks; a 'Development' stage (Co-STEER code-generation agent) implements and backtests them in real markets, jointly optimizing factor libraries and prediction models rather than treating them separately.<br><sub>Quant equity markets (via Qlib framework); exact universe not fully confirmed</sub> | — | — | ❔ | ❔ | [↗](https://github.com/microsoft/RD-Agent) |
| 2025 | [Market-Dependent Communication in Multi-Agent Alpha Generation](https://arxiv.org/pdf/2511.13614)<br><sub>arXiv q-fin</sub> | Studies how communication protocols between multiple alpha-generating agents should adapt to current market conditions (regime-dependent coordination) rather than using a fixed communication scheme.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2024 | [RiskMiner: Discovering Formulaic Alphas via Risk-Seeking Monte Carlo Tree Search](https://arxiv.org/abs/2402.07080)<br><sub>arXiv:2402.07080</sub> | Formulates formulaic-alpha mining as a reward-dense Markov Decision Process and solves it with a risk-seeking Monte Carlo Tree Search, aiming for alphas that are profitable under realistic backtesting rather than just high in-sample IC.<br><sub>Two real-world stock sets (markets not specified in abstract)</sub> | — | — | ❔ | ❔ |  |
| 2024 | [QuantFactor REINFORCE: Mining Steady Formulaic Alpha Factors with Variance-Bounded REINFORCE](https://arxiv.org/pdf/2409.05144)<br><sub>arXiv q-fin</sub> | Uses a variance-bounded REINFORCE policy-gradient method to mine formulaic alpha factors that are more stable/steady across time than standard RL alpha miners.<br><sub>Not captured</sub> | — | — | ❔ | ❔ |  |
| 2023 | [Generating Synergistic Formulaic Alpha Collections via Reinforcement Learning (AlphaGen)](https://arxiv.org/abs/2306.12964)<br><sub>KDD 2023 (Applied Data Science track)</sub> | Reinforcement-learning agent searches a formulaic-alpha expression space (combinations of price/volume operators) and is rewarded by the combined performance (IC) of the resulting alpha set rather than each alpha individually, producing a synergistic collection of low-correlation formulaic factors.<br><sub>CSI300 (China A-shares)</sub> | — | — | ❔ | ❔ | [↗](https://github.com/RL-MLDM/alphagen) |

### Crypto

<sub>🔧 [How to recreate each →](docs/papers.md#crypto)</sub>

| Year | Paper | Strategy | Reported return | Sharpe | Net of costs | OOS | Code |
|---|---|---|---|---|:-:|:-:|:-:|
| 2026 | [From Hypotheses to Factors: Constrained LLM Agents in Cryptocurrency Markets](https://arxiv.org/html/2604.26747v1)<br><sub>arXiv q-fin</sub> | Uses constrained LLM agents to generate and test factor hypotheses specifically for cryptocurrency markets, an application of the LLM-alpha-mining paradigm (AlphaGen/AlphaAgent-style) to crypto rather than equities.<br><sub>Cryptocurrency markets</sub> | — | — | ❔ | ❔ |  |
| 2026 | [Are Whitepaper Claims Reflected in Market Structure? A Contamination-Aware Pipeline and a Power-Limited Null (crypto whitepaper factor analysis)](https://arxiv.org/html/2601.20336v1)<br><sub>arXiv q-fin</sub> | Tests whether claims made in cryptocurrency project whitepapers (e.g., about technology, tokenomics, use-case) are reflected in subsequent market behavior/factor exposures, using a contamination-aware statistical pipeline to guard against data-snooping.<br><sub>Cryptocurrency universe with available whitepapers</sub> | — | — | ❔ | ❔ |  |
| 2025 | [Cryptocurrency as an Investable Asset Class: Coming of Age](https://arxiv.org/abs/2510.14435)<br><sub>arXiv:2510.14435</sub> | Extends the crypto three-factor model (market, size, momentum) with a value factor to form a four-factor (C-4) model; organizes crypto empirical asset-pricing regularities into seven stylized facts and argues crypto risk-adjusted performance is now broadly comparable to traditional asset classes.<br><sub>Broad cryptocurrency universe, updated through the mid-2020s</sub> | — | — | ❔ | ❔ |  |
| 2025 | [Cryptocurrency Market Risk-Managed Momentum Strategies](https://www.sciencedirect.com/science/article/abs/pii/S1544612325011377)<br><sub>Journal (via ScienceDirect)</sub> | Applies volatility-scaling/risk-management overlays to cryptocurrency momentum strategies to mitigate the severe crash risk documented in unmanaged crypto momentum.<br><sub>Cryptocurrency universe</sub> | — | — | ❔ | ❔ |  |
| 2025 | [Time Series Momentum in Cryptocurrency (crypto momentum has (not) its moments)](https://link.springer.com/article/10.1007/s11408-025-00474-9)<br><sub>Financial Markets and Portfolio Management</sub> | Studies whether cryptocurrency markets exhibit the same extended, persistent momentum-crash pattern documented in equities, finding a key structural difference.<br><sub>Cryptocurrency universe</sub> | — | — | ❔ | ❔ |  |
| 2022 | [Common Risk Factors in Cryptocurrency](https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.13119)<br><sub>Journal of Finance</sub> | Constructs cryptocurrency counterparts of standard equity return predictors and shows that a three-factor model (crypto market, crypto size, crypto momentum) captures most of the cross-sectional variation in expected cryptocurrency returns; ten crypto characteristics form significant long-short strategies largely spanned by this C-3 model.<br><sub>Broad cryptocurrency universe, sample spanning roughly 2014-2018</sub> | — | — | ❌ | ❌ |  |

### Prediction markets

<sub>🔧 [How to recreate each →](docs/papers.md#prediction-markets)</sub>

| Year | Paper | Strategy | Reported return | Sharpe | Net of costs | OOS | Code |
|---|---|---|---|---|:-:|:-:|:-:|
| 2026 | [Executable Arbitrage and Market Efficiency in Prediction Markets](https://arxiv.org/html/2608.00666v1)<br><sub>arXiv q-fin</sub> | Uses high-resolution order-book snapshots on prediction markets (e.g., Polymarket) to detect arbitrage opportunities in real time, then measures how persistent and how actually executable (against real liquidity) those opportunities are, distinguishing theoretical from tradeable mispricing.<br><sub>Polymarket (and similar) prediction markets</sub> | — | — | ✅ | ❔ |  |
| 2026 | [Arbitrage Analysis in Polymarket NBA Markets](https://arxiv.org/html/2605.00864v1)<br><sub>arXiv q-fin</sub> | Focused study of arbitrage opportunities specifically within Polymarket's NBA betting markets.<br><sub>Polymarket NBA markets</sub> | — | — | ❔ | ❔ |  |
| 2026 | [Semantic Non-Fungibility and Violations of the Law of One Price in Prediction Markets](https://arxiv.org/html/2601.01706v1)<br><sub>arXiv q-fin</sub> | Documents cross-platform (e.g., Polymarket vs. Kalshi) violations of the law of one price for economically equivalent (but not identically worded/structured) prediction-market contracts, attributing fragmentation to structural factors like differing resolution rules and institutional segmentation rather than pure inefficiency.<br><sub>Cross-platform prediction markets (Polymarket, Kalshi)</sub> | — | — | ❔ | ❔ |  |

### Other

<sub>🔧 [How to recreate each →](docs/papers.md#other)</sub>

| Year | Paper | Strategy | Reported return | Sharpe | Net of costs | OOS | Code |
|---|---|---|---|---|:-:|:-:|:-:|
| 2025 | [From Deep Learning to LLMs: A Survey of AI in Quantitative Investment](https://arxiv.org/pdf/2503.21422)<br><sub>arXiv q-fin</sub> | Survey covering the progression from classical deep-learning quant methods to LLM-based approaches across the quantitative investment pipeline (factor mining, prediction, portfolio construction, execution).<br><sub>N/A (survey)</sub> | — | — | ❔ | ❔ |  |

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
