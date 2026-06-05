# Purpose: FastMCP server exposing 7 marketplace tools
# Docs: server.py.doc.md

## What this file does

Runs a FastMCP stdio server that exposes 7 marketplace tools
for AI agents. This is the primary integration point for
OpenCode and other MCP clients.

## Dependencies

- `fastmcp` for MCP server

## Important config values

- `CATALOG_URL` (imported from `catalog.py`)

## Why certain decisions were made

- FastMCP is used instead of raw `mcp` SDK because it provides
  decorator-based tool registration (cleaner code).
- All tools return JSON strings instead of plain text to allow
  programmatic parsing by agents.
- `_get_catalog` helper auto-fetches from remote if local cache
  is missing.

## Usage examples

```python
from sin_marketplace.server import mcp
mcp.run()  # starts stdio server
```

## Known caveats

- The server runs on stdio (not SSE/HTTP) because OpenCode expects
  stdio transport for local MCP servers.
- No authentication or rate limiting; relies on local execution.
