# Purpose: Install a skill from the marketplace
# Docs: marketplace-install.sh.doc.md

## What this file does

Bash wrapper around `sin-marketplace install`. Falls back to
installing the CLI if it is not on PATH.

## Usage examples

```bash
./scripts/marketplace-install.sh sin-infisical
```

## Known caveats

- Requires the Python package to be installed.
- No error handling for invalid slugs.
