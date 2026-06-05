# Purpose: Test MCP server tools (search, install, list, remove, info, update, sync)
# Docs: test_server.py.doc.md

## What this file does

Unit tests for `sin_marketplace.server`:
- All 7 MCP tools
- Mocked HTTP responses via `respx`
- Error handling (not found, network failure)

## Dependencies

- `pytest`, `respx`, `httpx`

## Usage examples

```bash
pytest tests/test_server.py -v
```
