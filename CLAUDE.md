# Orders service — AI tool context

- Zero-dependency Python; tests: `python -m pytest -q` (MUST pass before done)
- Style: type hints everywhere; no new dependencies
- Layers: auth.py -> api.py -> db.py (keep the separation; fix bugs in the right layer)
- /graphql uses graphql_lite.py — extend the parser there, not inline in api.py
- NEVER: edit tests to make them pass; commit secrets; touch db data shapes
