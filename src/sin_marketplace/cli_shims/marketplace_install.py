# Purpose: CLI shim for marketplace_install
# Docs: marketplace-install.doc.md
"""CLI: marketplace-install — install a skill from the catalog.

Usage: marketplace-install <SLUG>
"""
from __future__ import annotations
import argparse
import asyncio
import sys
from ..server import marketplace_install


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="marketplace-install", description="Install a skill from the catalog.")
    parser.add_argument("slug")
    args = parser.parse_args(argv)
    try:
        print(asyncio.run(marketplace_install(args.slug)))
    except Exception as e:
        print(f"[marketplace-install] error: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
