"""Data layer. Deliberately simple: dicts as the 'database'."""
from __future__ import annotations

ORDERS = {
    "A17": {"id": "A17", "status": "delayed", "total": 49.0},
    "B42": {"id": "B42", "status": "shipped", "total": 19.5},
}

# token -> user
TOKENS = {"tok-alice": "alice", "tok-bob": "bob"}


def get_order(order_id: str) -> dict | None:
    return ORDERS.get(order_id)


def list_orders() -> list[dict]:
    return list(ORDERS.values())


def user_for_token(token: str) -> str | None:
    return TOKENS.get(token)
