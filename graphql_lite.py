"""A deliberately tiny GraphQL-query parser — just enough for two query shapes.

Supports:  { order(id: "A17") { id status total } }
           { orders { id status } }
No dependencies; this is teaching scaffolding, not a GraphQL implementation.
"""
from __future__ import annotations

import re

ORDER_RE = re.compile(
    r'\{\s*order\s*\(\s*id:\s*"(?P<id>[^"]+)"\s*\)\s*\{(?P<fields>[^}]*)\}\s*\}')
ORDERS_RE = re.compile(r"\{\s*orders\s*\{(?P<fields>[^}]*)\}\s*\}")


def parse(query: str) -> tuple[str, dict]:
    """Returns ("order", {"id":..., "fields":[...]}) or ("orders", {"fields":[...]})."""
    if m := ORDER_RE.search(query):
        return "order", {"id": m["id"], "fields": m["fields"].split()}
    if m := ORDERS_RE.search(query):
        return "orders", {"fields": m["fields"].split()}
    raise ValueError("unsupported query")
