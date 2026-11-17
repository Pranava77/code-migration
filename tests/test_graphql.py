"""The migration's definition of done: /graphql answers both query shapes."""
import json

from api import handle

AUTH = {"Authorization": "tok-bob"}


def _gql(query: str):
    return handle("POST", "/graphql", AUTH, json.dumps({"query": query}))


def test_order_query_with_field_selection():
    status, body = _gql('{ order(id: "A17") { id status total } }')
    assert status == 200
    assert body["data"]["order"] == {"id": "A17", "status": "delayed", "total": 49.0}


def test_order_query_partial_fields():
    status, body = _gql('{ order(id: "B42") { status } }')
    assert body["data"]["order"] == {"status": "shipped"}


def test_orders_query():
    status, body = _gql("{ orders { id status } }")
    assert status == 200
    assert {"id": "A17", "status": "delayed"} in body["data"]["orders"]
    assert all(set(o) == {"id", "status"} for o in body["data"]["orders"])


def test_unknown_query_400():
    status, _ = _gql("{ customers { id } }")
    assert status == 400
