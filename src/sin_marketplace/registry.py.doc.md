# Purpose: Local registry — SQLite persistence of installed skills
# Docs: registry.py.doc.md

## What this file does

Persists metadata about installed skills in a SQLite database.
Tracks slug, name, source, destination, installation time, and
update time.

## Dependencies

- `sqlite3` (stdlib)

## Important config values

- `DEFAULT_DB_PATH`: `~/.config/opencode/sin_marketplace.db`

## Why certain decisions were made

- SQLite is used instead of a JSON file to support concurrent
  access (MCP server + CLI can run simultaneously).
- `ON CONFLICT` upserts allow idempotent installs.
- `catalog_meta` table stores sync timestamps separately.

## Usage examples

```python
from sin_marketplace.registry import Registry

registry = Registry()
registry.install({"slug": "test", "source": "...", "destination": "..."})
print(len(registry))  # 1
```

## Known caveats

- The database path is created automatically but the parent
  directory must be writable.
- `version` column is optional; most skills do not use semver.
