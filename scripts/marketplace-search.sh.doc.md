# Purpose: Search skills in the marketplace catalog
# Docs: marketplace-search.sh.doc.md

## What this file does

Bash wrapper around `sin-marketplace search`. Falls back to
installing the CLI if it is not on PATH.

## Usage examples

```bash
./scripts/marketplace-search.sh secret
./scripts/marketplace-search.sh secret --remote
```

## Known caveats

- Requires the Python package to be installed (`pip install -e .`).
- The `--remote` flag is passed positionally as the second argument.
