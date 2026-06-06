# Purpose: CLI shim for marketplace_search
# Docs: marketplace-search.doc.md
"""CLI: marketplace-search — search skills by name, category, or keyword.

Usage: marketplace-search <QUERY>
"""
from __future__ import annotations
import argparse
import asyncio
import sys
from ..server import marketplace_search


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="marketplace-search", description="Search skills by name, category, or keyword.")
    parser.add_argument("query")
    args = parser.parse_args(argv)
    try:
        print(asyncio.run(marketplace_search(args.query)))
    except Exception as e:
        print(f"[marketplace-search] error: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
