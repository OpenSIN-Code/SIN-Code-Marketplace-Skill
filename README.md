> ## ⚠️ DEPRECATED — This skill has been merged into [sin-code-bundle](https://github.com/OpenSIN-Code/SIN-Code-Bundle)
>
> As of v0.9.3 (2026-06-06), this standalone skill is now a subcommand of the `sin-code-bundle` CLI:
>
> | Old | New |
> |-----|-----|
> | standalone skill | `sin marketplace` |
>
> **Migrate now:** `pip install --upgrade sin-code-bundle`
>
> This repo is archived; no further updates will be made.
> See [issue #29](https://github.com/OpenSIN-Code/SIN-Code-Bundle/issues/29) for the consolidation rationale.

# SIN Marketplace Skill

SIN Marketplace Skill — MCP-based skill management for the OpenSIN-Code ecosystem.

## Overview

This skill provides a **FastMCP server** and **CLI** for discovering, installing,
removing, and updating OpenSIN-Code skills. It syncs with the canonical catalog
from the [Infra-SIN-OpenCode-Stack](https://github.com/OpenSIN-Code/Infra-SIN-OpenCode-Stack)
repository.

## Architecture

```
OpenCode Agent
    ↓ MCP stdio
FastMCP Server (sin-marketplace)
    ↓ HTTP / SQLite
Catalog ← Infra-SIN-OpenCode-Stack/skills/catalog.json
Installer ← git clone + pip install
Registry ← SQLite (~/.config/opencode/sin_marketplace.db)
Updater ← git pull + diff
```

## MCP Tools

| Tool | Description |
|------|-------------|
| `marketplace_search` | Search skills by keyword across name, title, description |
| `marketplace_install` | Clone a skill repo and register it in opencode.json |
| `marketplace_list` | List all installed skills from the SQLite registry |
| `marketplace_remove` | Remove a skill from disk and registry |
| `marketplace_info` | Show detailed info about a skill (catalog + installed) |
| `marketplace_update` | Check for updates and git pull (single or all) |
| `marketplace_sync` | Fetch latest catalog from Infra-SIN-OpenCode-Stack |

## CLI Commands

```bash
# Search
sin-marketplace search <query> [--remote]

# Install
sin-marketplace install <slug>

# List
sin-marketplace list

# Remove
sin-marketplace remove <slug> [--force]

# Update
sin-marketplace update [<slug>] [--check]

# Sync catalog
sin-marketplace sync

# Info
sin-marketplace info <slug>
```

## Installation

```bash
pip install -e .
```

## Tests

```bash
pytest
```

## CoDocs

Every module has a `.doc.md` companion. See `src/sin_marketplace/*.doc.md`.

## License

MIT — OpenSIN-Code
