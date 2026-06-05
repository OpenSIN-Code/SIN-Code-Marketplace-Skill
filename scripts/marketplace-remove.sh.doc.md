# Purpose: Remove a skill from the marketplace
# Docs: marketplace-remove.sh.doc.md

## What this file does

Bash wrapper around `sin-marketplace remove`. Supports `--force`
flag. Falls back to installing the CLI if it is not on PATH.

## Usage examples

```bash
./scripts/marketplace-remove.sh sin-infisical
./scripts/marketplace-remove.sh sin-infisical --force
```

## Known caveats

- Requires the Python package to be installed.
