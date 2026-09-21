# Fundamentals, market data & alternative data

[← back to the main list](../README.md)

SEC filings, valuation, transcripts, ownership, market-data SDKs, tick storage, news sentiment and alt-data.
**OpenBB Platform** is the dominant open research hub, **edgartools** is best-in-class for SEC/XBRL, and
**ArcticDB / QuestDB / TimescaleDB** are the credible open time-series stores.

## SEC filings & XBRL

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

## Valuation

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

## Earnings transcripts

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

## Ownership & insider

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

## Market-data SDKs

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

## Tick & time-series storage

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

## News & sentiment

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

## Alternative data

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

## Screeners

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

## Other

**[filib (Factor Investing Library)](https://github.com/prmkowalski/filib)** · Python · ★ 29 · last push 2022-11-12  
A lightweight factor-investing library for testing predictive fundamental/technical factors and running portfolio rebalancing based on those factors, aimed at retail-accessible factor-strategy research.

✅ *Good at:* Quick iteration on custom fundamental factor definitions and their portfolio-level rebalancing performance.  
⚠️ *Limitations:* Small, unmaintained since 2022; lacks the depth of institutional factor-model libraries.

</details>
