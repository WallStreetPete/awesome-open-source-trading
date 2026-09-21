# Contributing

Thanks for helping keep this map accurate.

## Add or fix a project
1. Edit `data/tools.json`. Each entry has `name`, `url`, `section`, `category`, `language`, `stars`,
   `last_push`, `license`, `maintained` (`active` / `slow` / `stale` / `archived` / `unknown`),
   `explainer` (3–5 sentences), `good_at` (1–2 sentences), `limitations` (1 sentence) and `sources`.
2. Sections: `backtesting`, `live_trading`, `prediction_markets`, `options`, `ai_agents`, `fundamental_data`.

## Add or fix a paper
Edit `data/papers.json`. Report returns **exactly as the paper states them**. Set `costs_included` and
`out_of_sample` to `true`, `false` or `null` (not stated). Put caveats in `notes`.

## Regenerate
```bash
python scripts/build_readme.py
```
Then commit both the data change and the regenerated `README.md`.

## Guidelines
- Open source only. Commercial tools can appear only if they have a meaningful open-source component.
- Be neutral and specific. No marketing copy, no unverified performance claims.
- Nothing here is investment advice.
