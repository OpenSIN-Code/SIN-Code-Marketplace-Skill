# Purpose: CLI shim package for sin-marketplace MCP tools
# Docs: __init__.doc.md
"""CLI shim package for sin-marketplace — thin argparse wrappers
around each tool in sin_marketplace.server. The original tools are
async, so each shim wraps the call in `asyncio.run`."""
