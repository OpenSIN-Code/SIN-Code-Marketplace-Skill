# Purpose: Typer CLI for human-friendly marketplace commands
# Docs: cli.py.doc.md

## What this file does

Provides a Typer-based CLI for all marketplace operations.
Wraps the Python API with Rich-formatted tables and prompts.

## Dependencies

- `typer` for CLI framework
- `rich` for formatted output

## Important config values

- None (uses the same defaults as the modules)

## Why certain decisions were made

- `typer` is used instead of `argparse` because the rest of the
  OpenSIN-Code ecosystem uses Typer (consistent UX).
- `--json` flags are provided for every command to allow scriptable
  output (used by the bash wrappers).
- `--force` bypasses confirmation for automated removal.

## Usage examples

```bash
sin-marketplace search secret
sin-marketplace install sin-infisical
sin-marketplace list --json
sin-marketplace remove sin-infisical --force
```

## Known caveats

- `sync` fetches the remote catalog every time; there is no local
  TTL cache.
- `search` without `--remote` requires a prior `sync`.
