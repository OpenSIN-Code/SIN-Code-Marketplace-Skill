# Purpose: Catalog reader — fetch and query the canonical skills catalog
# Docs: catalog.py.doc.md

## What this file does

Reads and queries the canonical skills catalog from the
Infra-SIN-OpenCode-Stack repository. Supports both remote
(HTTP) and local (JSON file) sources.

## Dependencies

- `httpx` for async HTTP requests
- `json` / `pathlib` for local file I/O

## Important config values

- `CATALOG_URL`: Raw GitHub URL to `catalog.json`
- `DEFAULT_TIMEOUT`: 30 seconds for HTTP requests

## Why certain decisions were made

- Uses `httpx.AsyncClient` instead of `requests` because the MCP server
  is async-native (FastMCP).
- Search is substring-based (not tokenized) to keep the tool simple
  and predictable.
- `Catalog` is a plain class (not a singleton) to allow testing
  with multiple instances.

## Usage examples

```python
from sin_marketplace.catalog import Catalog

catalog = Catalog()
await catalog.load_remote()
results = catalog.search("secret")
```

## Known caveats

- No caching logic here; caching is handled by the caller (`server.py`).
- Does not validate the schema of individual catalog entries.
