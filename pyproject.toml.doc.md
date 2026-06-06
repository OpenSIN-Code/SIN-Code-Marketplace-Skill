# sin-marketplace/pyproject.toml

**Purpose:** Build configuration and package metadata for the
`sin-marketplace-skill` Python package. Defines dependencies, the
MCP server entry point, and PyPI classifier metadata.

**Source file:** `pyproject.toml` (TOML)

**Header excerpt:**

```
# Purpose: SIN Marketplace Skill package metadata and dependencies
# Docs: pyproject.toml.doc.md
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

---

## What it does

Declares the package as a standard PEP 621 Python project with the
Hatchling build backend. Pins the minimum Python version (3.10),
exposes the MCP server CLI entry point, and lists the runtime and
development dependencies.

## Dependencies

| Group | Package | Why |
|---|---|---|
| runtime | `fastmcp>=2.0` | MCP server framework (3.x compatible) |
| runtime | `httpx>=0.25` | HTTP client for the marketplace API |
| runtime | `rich>=13.0` | Terminal output formatting |
| runtime | `typer>=0.9` | CLI argument parsing |
| dev | `pytest>=7.0` | Test runner |
| dev | `pytest-asyncio>=0.21` | Async test support |
| dev | `pytest-cov>=4.0` | Coverage reporting |

## Important config

- `name = "sin-marketplace-skill"` — package name on PyPI.
- `version = "0.1.0"` — bump on every release (current: 0.1.1).
- `[project.scripts]` — exposes `sin-marketplace` CLI binary which
  starts the MCP server over stdio.

## Why these decisions

- **Hatchling, not setuptools** — faster builds, no `setup.py` needed.
- **`fastmcp>=2.0`** — needs fastmcp 3.x API (`add_tool()` method,
  not the removed `mcp.tool(fn)` function-call).
- **`requires-python = ">=3.10"`** — matches the opencode baseline.

## Usage example

```bash
# Build wheel + sdist
python3 -m build

# Install in editable mode for development
pip install -e .[dev]

# Run the MCP server
sin-marketplace
```

## Known caveats

- **No `[project.optional-dependencies].all`** — every dependency is
  always required. Don't add heavy optional deps without thinking
  through cold-start latency.
