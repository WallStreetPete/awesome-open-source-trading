# Live trading, execution & brokers

[← back to the main list](../README.md)

Connectivity, order management and bots for running strategies live. For **Interactive Brokers**, the maintained
path is **ib_async** (successor to the archived ib_insync), with **ib-gateway-docker + IBC** for a headless gateway.
Use **NautilusTrader** or **LEAN** when you want a full engine with IBKR adapters, reconciliation and risk checks.

## Interactive Brokers

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

## Broker SDKs

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

## Execution & OMS

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

**[matching-engine](https://github.com/rekurt/matching-engine)** · Rust · ★ 1 · last push 2026-10-10  
A single-node Rust service for matching spot orders with price-time priority. Prices and quantities use fixed-point arithmetic, and clients connect through a binary protocol over TCP or Unix domain sockets. Optional write-ahead logging, snapshots and recovery retain matching decisions when persistence is enabled. The source-only v0.1.0 release includes a Go client, integration examples and operations documentation.

✅ *Good at:* Providing spot-order matching for an execution platform that supplies account and settlement infrastructure.  
⚠️ *Limitations:* Account balances, reserved funds, settlement, replication and failover are external, and journals have no online compaction.

</details>

## Crypto bots

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

## Market making

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

## FIX engines

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

## TradingView webhook bridges

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

## Other

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
