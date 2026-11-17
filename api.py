"""API layer: legacy REST endpoints. (Your task: add /graphql — see MIGRATION-TASK.md)

Framework-free on purpose: handle(method, path, headers, body) -> (status, json)
so tests run with zero dependencies. (In the session's story this is 'the Flask
app'; the shape is identical.)
"""
from __future__ import annotations

import json

from auth import token_from_header
from db import get_order, list_orders, user_for_token
from graphql_lite import parse


def _pick(row: dict, fields: list[str]) -> dict:
    return {f: row[f] for f in fields if f in row}


def handle(method: str, path: str, headers: dict, body: str = ""):
    token = token_from_header(headers.get("Authorization"))
    user = user_for_token(token) if token else None
    if user is None:
        return 401, {"error": "unauthorized"}

    # ---- legacy REST ----
    if method == "GET" and path.startswith("/orders/"):
        order = get_order(path.split("/")[-1])
        return (200, order) if order else (404, {"error": "not found"})
    if method == "GET" and path == "/orders":
        return 200, list_orders()

    # ---- GraphQL ----
    if method == "POST" and path == "/graphql":
        try:
            payload: dict = json.loads(body)
            kind, params = parse(payload["query"])
        except (ValueError, KeyError):
            return 400, {"error": "bad query"}

        if kind == "order":
            row = get_order(params["id"])
            if row is None:
                return 404, {"error": "not found"}
            return 200, {"data": {"order": _pick(row, params["fields"])}}

        if kind == "orders":
            rows = list_orders()
            return 200, {"data": {"orders": [_pick(r, params["fields"]) for r in rows]}}

    return 404, {"error": "no route"}
