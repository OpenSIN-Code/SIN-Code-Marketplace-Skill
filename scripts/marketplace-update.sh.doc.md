# Purpose: Update all installed skills
# Docs: marketplace-update.sh.doc.md

## What this file does

Bash wrapper around `sin-marketplace update`. Supports optional
slug argument. Falls back to installing the CLI if it is not on PATH.

## Usage examples

```bash
./scripts/marketplace-update.sh
./scripts/marketplace-update.sh sin-infisical
```

## Known caveats

- Requires the Python package to be installed.
