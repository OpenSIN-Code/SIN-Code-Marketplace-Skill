# Purpose: List installed skills
# Docs: marketplace-list.sh.doc.md

## What this file does

Bash wrapper around `sin-marketplace list`. Falls back to
installing the CLI if it is not on PATH.

## Usage examples

```bash
./scripts/marketplace-list.sh
```

## Known caveats

- Requires the Python package to be installed.
