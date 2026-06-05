# Purpose: End-to-end integration tests for full marketplace workflow
# Docs: test_integration.py.doc.md

## What this file does

Integration tests combining Catalog + Installer + Registry + Updater:
- Full install → register → list → update → remove workflow
- Sync and search
- Idempotent install

## Dependencies

- `pytest`, `git` CLI

## Usage examples

```bash
pytest tests/test_integration.py -v
```
