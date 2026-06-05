# Purpose: Test CLI commands for search, install, list, remove, update, sync, info
# Docs: test_cli.py.doc.md

## What this file does

Unit tests for `sin_marketplace.cli`:
- All CLI commands via Typer's CliRunner
- Error handling for missing catalogs
- JSON output flag

## Dependencies

- `pytest`, `typer`

## Usage examples

```bash
pytest tests/test_cli.py -v
```
