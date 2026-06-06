# Purpose: CLI shim for marketplace_sync
# Docs: marketplace-sync.doc.md
"""CLI: marketplace-sync — sync catalog with Infra-SIN-OpenCode-Stack.

Usage: marketplace-sync
"""
from __future__ import annotations
import asyncio
import sys
from ..server import marketplace_sync


def main(argv: list[str] | None = None) -> int:
    try:
        print(asyncio.run(marketplace_sync()))
    except Exception as e:
        print(f"[marketplace-sync] error: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
