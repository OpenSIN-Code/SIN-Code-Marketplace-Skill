# Purpose: Test git pull and update status checks
# Docs: test_updater.py.doc.md

## What this file does

Unit tests for `sin_marketplace.updater`:
- Update single and all skills
- Check status (behind / up to date)
- Edge cases (not installed, bare repo, invalid repo)

## Dependencies

- `pytest`, `git` CLI

## Usage examples

```bash
pytest tests/test_updater.py -v
```
