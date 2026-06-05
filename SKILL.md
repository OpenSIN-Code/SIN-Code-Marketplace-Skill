# SIN Marketplace Skill

OpenSIN-Code skill for managing skills via MCP and CLI.

## Triggers

- "marketplace", "install skill", "remove skill", "list skills", "update skills"
- "search skill", "skill catalog", "skill info", "sync catalog"

## When to use

Use this skill when you need to:
- Discover available skills in the OpenSIN-Code ecosystem
- Install a new skill from the catalog
- Remove an installed skill
- Update all skills to their latest versions
- Check detailed information about a specific skill
- Sync the local catalog with the remote source

## Installation

```bash
pip install -e .
```

## MCP Tools

| Tool | Description |
|------|-------------|
| `marketplace_search` | Search skills by keyword |
| `marketplace_install` | Install a skill from the catalog |
| `marketplace_list` | List installed skills |
| `marketplace_remove` | Remove a skill |
| `marketplace_info` | Show detailed info about a skill |
| `marketplace_update` | Update all skills to latest |
| `marketplace_sync` | Sync catalog with Infra-SIN-OpenCode-Stack |

## CLI

```bash
sin-marketplace search <query>
sin-marketplace install <slug>
sin-marketplace list
sin-marketplace remove <slug>
sin-marketplace update [<slug>]
sin-marketplace sync
sin-marketplace info <slug>
```

## Architecture

- `catalog.py` — Read and query Infra-SIN-OpenCode-Stack catalog
- `installer.py` — Clone repos, install dependencies, register in opencode.json
- `registry.py` — Track installed skills in SQLite
- `updater.py` — Check for updates, git pull, version comparison
- `server.py` — FastMCP server with 7 tools
- `cli.py` — Typer CLI for human interaction

## Dependencies

- fastmcp>=2.0
- httpx>=0.27
- rich>=13.0
- typer>=0.12
- GitPython>=3.1

## License

MIT — OpenSIN-Code
