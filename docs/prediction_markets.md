# Prediction markets (Kalshi, Polymarket & more)

[← back to the main list](../README.md)

SDKs, market makers, arbitrage bots, forecasting agents and datasets for event contracts. Several of Polymarket's
official repos (including `py-clob-client` and `agents`) are **archived**. Community SDKs and “CCXT for prediction
markets” libraries (**pmxt**, **dr-manhattan**) now fill the gap.

## Kalshi

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

## Polymarket

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

## Cross-venue & unified SDKs

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

## Forecasting agents

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

## Data & datasets

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

## Sports odds

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

## Other venues (Manifold, PredictIt, Limitless, DFlow…)

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
