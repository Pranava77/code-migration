# Take-home — the same two tasks you watched demoed

## Task 1 · The migration (tests/test_graphql.py is red)
Add a `POST /graphql` endpoint to `api.py` supporting:
    { order(id: "A17") { id status total } }
    { orders { id status } }
Parse with the provided helper in `graphql_lite.py` (no new deps).
Make `tests/test_graphql.py` pass. Do not touch `db.py`'s data shapes.

## Task 2 · The bug hunt (tests/test_auth_alice.py is red)
Alice's valid token gets a 401. The symptom is one line; the cause spans
auth.py -> api.py -> db.py. Find it, fix it IN THE RIGHT LAYER.
NEVER edit the tests.

Use Claude Code, Cursor, or any AI tool — the tests judge the result.
