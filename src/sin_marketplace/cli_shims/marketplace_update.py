# Purpose: CLI shim for marketplace_update
# Docs: marketplace-update.doc.md
"""CLI: marketplace-update — update all skills or a specific skill.

Usage: marketplace-update [--slug SLUG]
"""
from __future__ import annotations
import argparse
import asyncio
import sys
from ..server import marketplace_update


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="marketplace-update", description="Update all skills or a specific skill.")
    parser.add_argument("--slug", default=None)
    args = parser.parse_args(argv)
    try:
        print(asyncio.run(marketplace_update(args.slug)))
    except Exception as e:
        print(f"[marketplace-update] error: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
