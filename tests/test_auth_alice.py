"""The planted-bug test: Alice's perfectly valid token must work.

Bug (in the stub): auth.py lower-cases the token, db.py stored mixed-case keys,
api.py looks up strictly -> 401 for Alice. Fix belongs in the DATA layer
(normalise keys at definition), not by weakening this test.
"""
from api import handle


def test_auth_alice_mixed_case_token_works():
    status, body = handle("GET", "/orders/A17", {"Authorization": " Tok-Alice "})
    assert status == 200
    assert body["id"] == "A17"
