"""Auth layer: header -> token. Normalises case + whitespace."""
from __future__ import annotations


def token_from_header(header: str | None) -> str | None:
    if not header:
        return None
    return header.strip().lower()
