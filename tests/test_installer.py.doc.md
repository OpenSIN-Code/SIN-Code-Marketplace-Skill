# Purpose: Test skill installation, removal, and opencode.json registration
# Docs: test_installer.py.doc.md

## What this file does

Unit tests for `sin_marketplace.installer`:
- Cloning from local git repos
- Overwriting existing installs
- Registering in opencode.json
- Removing skills and cleaning config

## Dependencies

- `pytest`, `git` CLI

## Usage examples

```bash
pytest tests/test_installer.py -v
```
