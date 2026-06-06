# Purpose: CLI shim for marketplace_info
# Docs: marketplace-info.doc.md
"""CLI: marketplace-info — show detailed info about a skill.

Usage: marketplace-info <SLUG>
"""
from __future__ import annotations
import argparse
import asyncio
import sys
from ..server import marketplace_info


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="marketplace-info", description="Show detailed info about a skill.")
    parser.add_argument("slug")
    args = parser.parse_args(argv)
    try:
        print(asyncio.run(marketplace_info(args.slug)))
    except Exception as e:
        print(f"[marketplace-info] error: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
