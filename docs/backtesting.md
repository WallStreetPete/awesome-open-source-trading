# Backtesting & quant research

[← back to the main list](../README.md)

The engines split by execution model. **Vectorized** engines (vectorbt, bt, backtesting.py) trade realism for
speed and suit parameter sweeps and signal research. **Event-driven** engines (NautilusTrader, LEAN, backtrader,
zipline-reloaded, vnpy) model order-by-order state and suit path-dependent logic, options and multi-asset books.
If you want the same strategy code to run in backtest and live, start with **NautilusTrader** or **QuantConnect LEAN**.

## Backtesting engines

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

**[OpenBacktesting](https://github.com/lucidcog/openbacktesting)** · Python · ★ 1 · last push 2026-10-14  
OpenBacktesting is a Python framework for single-asset historical backtesting. Strategies run bar by bar and expose trades and pandas-based equity and performance statistics for inspection. It includes technical indicators and parameter optimization through grid search or an optional SAMBO backend. This entry was checked on 2026-10-14; the public repository was created on 2026-10-12.

✅ *Good at:* Inspecting individual historical strategy runs and comparing parameter settings in Python.  
⚠️ *Limitations:* Early-stage project with a short public track record; it does not provide live execution or a multi-asset portfolio account.

</details>

## Research platforms

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

## Factor research

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

## Performance analytics & tearsheets

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

## Portfolio optimization

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

## Data tooling

**[OpenBB](https://github.com/OpenBB-finance/OpenBB)** · Python · ★ 73.3k · last push 2026-09-19  
OpenBB is an open-source financial data and research platform combining a Python SDK, a CLI/terminal UI, and a local REST API, with a large extensible-provider architecture that unifies many free and paid data sources (equities, options, macro, crypto) behind a consistent interface. It is primarily a data-access and research-workbench layer rather than a backtesting engine itself, but it is frequently used as the data-fetching front end that feeds into backtesting frameworks like vectorbt, backtrader or Qlib. It has grown into one of the largest and most visible open-source projects in the whole quant-finance space.

✅ *Good at:* Best as a unified, extensible data layer and research terminal to pair with a dedicated backtesting engine, rather than as the backtester itself.  
⚠️ *Limitations:* Not a backtesting engine on its own; many premium data providers still require paid API keys, and the extension ecosystem can be heavy to configure.

**[tidyquant (R)](https://github.com/business-science/tidyquant)** · R · ★ 915 · last push 2026-09-01  
tidyquant bridges financial analysis and the tidyverse, bringing together market data retrieval, xts/zoo/quantmod/TTR-style functions, and PerformanceAnalytics performance metrics into a consistent tibble-based, pipe-friendly (`%>%`) interface. It's the main reason R users doing modern tidyverse-style data analysis can do financial time-series and performance work without leaving that idiom, and it's actively maintained by Business Science alongside companion packages timetk and tibbletime.

✅ *Good at:* Best for R users who want financial data retrieval and standard performance analytics in an idiomatic, pipe-friendly tidyverse workflow.  
⚠️ *Limitations:* Not a backtesting engine itself; it's a data/analytics convenience layer that still needs quantstrat or custom logic for actual strategy simulation.

</details>

## Lists & other

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
