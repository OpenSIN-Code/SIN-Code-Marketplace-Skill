# SIN-Code-Marketplace-Skill — Agent Context

## Project

SIN Marketplace Skill — MCP-based skill management for OpenSIN-Code.

## Architecture

- FastMCP server (stdio) with 7 tools
- Typer CLI with 6 commands
- SQLite registry
- Git-based installer and updater
- Remote catalog from Infra-SIN-OpenCode-Stack

## Build

```bash
pip install -e ".[dev]"
pytest
```

## Test

```bash
pytest --cov=src/sin_marketplace
```

## CoDocs

Every module has a `.doc.md` companion. Keep them in sync.

## Rules

- Only `main` branch (no branches)
- Conventional commits
- All tests must pass
- 100% CoDocs coverage
