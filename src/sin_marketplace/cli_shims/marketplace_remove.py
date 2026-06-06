# Purpose: CLI shim for marketplace_remove
# Docs: marketplace-remove.doc.md
"""CLI: marketplace-remove — remove a skill.

Usage: marketplace-remove <SLUG>
"""
from __future__ import annotations
import argparse
import asyncio
import sys
from ..server import marketplace_remove


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="marketplace-remove", description="Remove a skill.")
    parser.add_argument("slug")
    args = parser.parse_args(argv)
    try:
        print(asyncio.run(marketplace_remove(args.slug)))
    except Exception as e:
        print(f"[marketplace-remove] error: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
