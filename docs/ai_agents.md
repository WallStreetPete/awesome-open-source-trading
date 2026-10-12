# AI, agents & machine learning

[← back to the main list](../README.md)

LLM multi-agent trading frameworks, alpha mining, reinforcement learning, market foundation models, trading MCP
servers and evaluation benchmarks. **TradingAgents**, **ai-hedge-fund**, **FinRL**, **Microsoft RD-Agent(Q)** and
**Kronos** (a foundation model trained on candlestick data) anchor the space.

## LLM multi-agent frameworks

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

## Alpha mining

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

## Reinforcement learning

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

## ML trading

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

## Foundation models

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

## MCP servers

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

**[Invokely MCP connector](https://github.com/estevecastells/invokely-mcp-connector)** · JavaScript · ★ 0 · last push 2026-10-12  
This MIT-licensed local stdio adapter connects MCP clients to Invokely's hosted official-statistics service. It discovers the hosted tool schemas and forwards requests; its statistics tools search indicators, resolve places, retrieve values or series, compare places, and rank locations. Results include the period, unit, source, and citation across US states and counties, EU countries and regions, Spanish municipalities, and World Bank country and world indicators. The Free plan includes 500 MCP calls per month and full series history; REST data queries require Builder, Pro, or prepaid credits.

✅ *Good at:* Lets local MCP clients query cited official statistics across supported geographies for macroeconomic context in financial research.  
⚠️ *Limitations:* This repository contains the MIT adapter, not the hosted backend; Invokely provides economic statistics rather than market prices or trade execution, and its no-account MCP trial is limited to 25 calls per day per IP.

</details>

## Benchmarks

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

## Uses Jev (TypeSafe)

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

## Lists & other

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
