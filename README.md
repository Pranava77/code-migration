# Orders Service

A lightweight, zero-dependency Python microservice for managing orders, featuring both REST and GraphQL endpoints with token-based authentication.

## Architecture

```
auth.py  →  api.py  →  db.py
```

| Layer | File | Responsibility |
|-------|------|----------------|
| **Auth** | `auth.py` | Extracts and normalises tokens from the `Authorization` header |
| **API** | `api.py` | Routes requests to REST and GraphQL handlers |
| **Data** | `db.py` | In-memory data store for orders and tokens |
| **Parser** | `graphql_lite.py` | Minimal GraphQL query parser (no external deps) |

## Endpoints

### REST

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/orders` | List all orders |
| `GET` | `/orders/:id` | Get a single order by ID |

### GraphQL

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/graphql` | Execute a GraphQL query |

**Supported queries:**

```graphql
{ order(id: "A17") { id status total } }
{ orders { id status } }
```

**Example request body:**

```json
{ "query": "{ order(id: \"A17\") { id status total } }" }
```

## Authentication

All endpoints require a valid token in the `Authorization` header. Tokens are case-insensitive.

| Token | User |
|-------|------|
| `tok-alice` | alice |
| `tok-bob` | bob |

**Example:**

```
Authorization: tok-bob
```

## Getting Started

### Prerequisites

- Python 3.10+
- pytest

### Install dependencies

```bash
pip3 install pytest
```

### Run the tests

```bash
cd /path/to/stub
python3 -m pytest -v
```

**Expected output:**

```
tests/test_auth_alice.py::test_auth_alice_mixed_case_token_works PASSED
tests/test_graphql.py::test_order_query_with_field_selection PASSED
tests/test_graphql.py::test_order_query_partial_fields PASSED
tests/test_graphql.py::test_orders_query PASSED
tests/test_graphql.py::test_unknown_query_400 PASSED
tests/test_rest.py::test_get_order_by_id PASSED
tests/test_rest.py::test_list_orders PASSED
tests/test_rest.py::test_missing_order_404 PASSED
tests/test_rest.py::test_no_token_401 PASSED

9 passed
```

## Project Structure

```
stub/
├── api.py              # API layer: REST + GraphQL routing
├── auth.py             # Auth layer: token extraction & normalisation
├── db.py               # Data layer: in-memory orders & tokens
├── graphql_lite.py     # Minimal GraphQL query parser
├── requirements.txt    # Python dependencies
├── MIGRATION-TASK.md   # Task description
├── CLAUDE.md           # AI tool context
├── README.md           # This file
└── tests/
    ├── test_rest.py          # REST endpoint tests
    ├── test_graphql.py       # GraphQL endpoint tests
    └── test_auth_alice.py    # Auth bug regression test
```

## Design Decisions

- **Framework-free**: The `handle(method, path, headers, body)` function signature mirrors a web framework but runs with zero dependencies, keeping tests fast and simple.
- **Layered architecture**: Auth → API → DB separation ensures bugs are fixed in the right layer.
- **Case-insensitive tokens**: `auth.py` normalises tokens to lowercase; `db.py` stores keys in lowercase to match.
