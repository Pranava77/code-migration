from api import handle

AUTH = {"Authorization": "tok-bob"}


def test_get_order_by_id():
    status, body = handle("GET", "/orders/A17", AUTH)
    assert status == 200 and body["status"] == "delayed"


def test_list_orders():
    status, body = handle("GET", "/orders", AUTH)
    assert status == 200 and len(body) == 2


def test_missing_order_404():
    status, _ = handle("GET", "/orders/ZZZ", AUTH)
    assert status == 404


def test_no_token_401():
    status, _ = handle("GET", "/orders", {})
    assert status == 401
