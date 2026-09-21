# Strategy research papers: how to recreate

[← back to the main list](../README.md)

Returns are as reported by the authors. Notes flag costs, out-of-sample status and other caveats.

## Earnings events & PEAD

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

## Analyst revisions

**[Corporate Earnings Calls and Analyst Beliefs](https://arxiv.org/pdf/2511.15214)** (2025)  
🔧 Requires earnings-call transcripts plus subsequent analyst forecast-revision data (I/B/E/S-style); measure how call content predicts the direction/magnitude of near-term analyst revisions, then trade ahead of the revision using the call-derived signal.  
⚠️ Title/abstract only; not independently verified in this pass -- included to mark the analyst-revision-from-text category, which is thinner in the recent literature than sentiment/PEAD.

**[Earnings Forecasts and Revisions, Price Momentum, and Fundamental Data (chapter overview of AQR-style earnings-revision composites)](https://go.factset.com/hubfs/Symposium%20Images/Guerard_EARNINGS%20FORECASTS%20AND%20REVISIONS,%20PRICE%20MOMENTUM,%20AND%20FUNDAMENTAL%20DATA.pdf)** (2023)  
🔧 Requires consensus EPS estimate history (I/B/E/S-style, so revision direction/magnitude can be computed) plus prices. Compute 1-3 month change in consensus EPS estimate per stock, rank cross-sectionally, go long top revision decile / short bottom, rebalance monthly; smaller-cap names show a stronger effect per the underlying literature.  
⚠️ This is a practitioner/survey-style anchor rather than a single rigorous academic paper with clean out-of-sample stats; useful mainly as a recipe (analyst-revision momentum is one of the more implementable, data-light factors if a fundamentals feed with consensus estimates is available).

## Momentum

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

## Value & quality

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

## Fundamental composites

**[Value Investing Research: Simple Methods to Improve the Piotroski F-Score](https://alphaarchitect.com/value-investing-research-simple-methods-to-improve-the-piotroski-f-score/)** (2020)  
🔧 Requires standard fundamentals (ROA, change in ROA, CFO, CFO vs. net income, change in leverage, change in current ratio, share issuance, change in gross margin, change in asset turnover); compute the 9 binary signals, sum to a 0-9 F-Score, apply within a cheap-valuation (high B/M) universe, long high F-Score / short or avoid low F-Score.  
⚠️ F-Score is one of the cheapest-to-implement fundamental composites (needs only standard financial-statement line items, no text/news); best used as a quality overlay on a value screen rather than standalone, per the original Piotroski (2000) design, which is itself the seminal anchor for this factor family.

## Factor timing & crowding

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

## Short interest & borrow

**[Anomalies and Their Short-Sale Costs](https://onlinelibrary.wiley.com/doi/10.1111/jofi.13501)** (2025)  
🔧 Requires published anomaly signals (value, momentum, quality, etc.) plus a stock-borrow-fee/loan-fee dataset (e.g., from a securities-lending data vendor). Compute standard long-short anomaly returns, then re-compute the short leg's realized return net of the contemporaneous borrow fee for each name/day.  
⚠️ Critical caveat paper for the entire anomaly literature: most published 'gross' long-short anomaly returns are not actually capturable once realistic borrow costs are included, especially in the crowded, hard-to-borrow small-cap short tail. Directly relevant to any long/short tech book -- shorting expensive-to-borrow names (e.g., heavily shorted momentum/growth names) can erase the anomaly's apparent edge.

**[The Loan Fee Anomaly: A Short Seller's Best Ideas](https://paperswithbacktest.com/strategies/the-loan-fee-anomaly-a-short-seller-s-best-ideas)** (2019)  
🔧 Requires a securities-lending/borrow-fee data feed by stock and date. Rank stocks by borrow fee level (and/or fee changes), short high-fee names, long low-fee names, rebalance monthly.  
⚠️ Because the strategy's own edge is proportional to borrow fee, the strategy is inherently expensive to implement at scale on the short side -- the 'anomaly' partly reflects the informed-shorting signal, not a free lunch; overlaps conceptually with the Muravyev et al. (2025) short-sale-cost paper above.

## Options-implied signals

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

## Intraday & overnight

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

## Statistical arbitrage

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

## ML return prediction

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

## LLM signals

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

## LLM trading agents

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

## RL portfolio management

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

## Alpha mining

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

## Crypto

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

## Prediction markets

**[Executable Arbitrage and Market Efficiency in Prediction Markets](https://arxiv.org/html/2608.00666v1)** (2026)  
🔧 Requires real-time or historical order-book-level data from prediction-market platforms (Polymarket/Kalshi APIs); scan for logically-linked contracts (e.g., complementary outcomes summing to more/less than 100%) and check whether the implied arbitrage can be filled at quoted depth net of fees.  
⚠️ Institutional-scale profit is limited: residual inefficiencies are 'structurally confined to the retail tier' per the paper's framing -- i.e., the aggregate market is close to efficient at size, even though retail-scale arbitrage remains detectable. Not directly relevant to a US tech-equity long/short book but included for completeness's scope.

**[Arbitrage Analysis in Polymarket NBA Markets](https://arxiv.org/html/2605.00864v1)** (2026)  
🔧 Requires Polymarket NBA market order-book/price data; identify logically linked contracts (e.g., moneyline vs. spread-implied probabilities) and test for exploitable mispricing net of fees.  
⚠️ Finds NBA markets are nearly efficient in aggregate, with residual inefficiencies mainly accessible only at retail scale, not institutional size.

**[Semantic Non-Fungibility and Violations of the Law of One Price in Prediction Markets](https://arxiv.org/html/2601.01706v1)** (2026)  
🔧 Requires matched-contract price data across platforms; identify semantically-equivalent contracts with different resolution language, measure price divergence, test whether the divergence is arbitrageable given platform-specific settlement risk and withdrawal/transfer frictions.  
⚠️ Finding that fragmentation is 'structural rather than incidental' implies apparent cross-platform arbitrage may not be safely executable due to resolution-rule risk, not just execution cost.

## Other

**[From Deep Learning to LLMs: A Survey of AI in Quantitative Investment](https://arxiv.org/pdf/2503.21422)** (2025)  
🔧 N/A -- survey paper; useful as a map for prioritizing which sub-literatures (alpha mining, ML prediction, LLM agents) to invest research time in.  
⚠️ Not a standalone empirical strategy paper.
