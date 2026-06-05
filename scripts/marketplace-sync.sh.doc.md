# Purpose: Sync marketplace catalog with Infra-SIN-OpenCode-Stack
# Docs: marketplace-sync.sh.doc.md

## What this file does

Bash wrapper around `sin-marketplace sync`. Fetches the latest
catalog from the canonical source. Falls back to installing the
CLI if it is not on PATH.

## Usage examples

```bash
./scripts/marketplace-sync.sh
```

## Known caveats

- Requires the Python package to be installed.
- Needs network access to GitHub raw content.
