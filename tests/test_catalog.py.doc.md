# Purpose: Test catalog loading, search, and filtering
# Docs: test_catalog.py.doc.md

## What this file does

Unit tests for `sin_marketplace.catalog`:
- Loading from local files and remote URLs
- Search by keyword, name, title, description
- Filtering by category
- Edge cases (empty, invalid JSON, not a list)

## Dependencies

- `pytest`, `respx`, `httpx`

## Usage examples

```bash
pytest tests/test_catalog.py -v
```
