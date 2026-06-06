# Purpose: CLI shim for marketplace_list
# Docs: marketplace-list.doc.md
"""CLI: marketplace-list — list installed skills.

Usage: marketplace-list
"""
from __future__ import annotations
import asyncio
import sys
from ..server import marketplace_list


def main(argv: list[str] | None = None) -> int:
    try:
        print(asyncio.run(marketplace_list()))
    except Exception as e:
        print(f"[marketplace-list] error: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
