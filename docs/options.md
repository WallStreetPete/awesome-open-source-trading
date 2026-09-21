# Options, greeks & volatility

[← back to the main list](../README.md)

Pricing libraries, implied-volatility and surface fitting, options backtesters, greeks and gamma-exposure tools.
**QuantLib** remains the standard. **FinancePy**, **tf-quant-finance** and **RustQuant** are strong alternatives,
and **py_vollib** is the lightweight Black–Scholes / greeks / IV stack.

## Pricing libraries

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

## Volatility surfaces

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

## Options backtesting

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

## Greeks & risk

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

## Gamma exposure (GEX)

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

## Volatility trading

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

## Options data

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

## Crypto options

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

## Other

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
