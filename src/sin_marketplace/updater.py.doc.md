# Purpose: Skill updater — check for updates and pull latest changes
# Docs: updater.py.doc.md

## What this file does

Checks whether installed skills are behind their remote
repositories and performs `git pull` to update them.

## Dependencies

- `GitPython` for repository inspection

## Important config values

- `DEFAULT_SKILLS_DIR`: `~/.config/opencode/skills`

## Why certain decisions were made

- `git.Repo.iter_commits` is used to count commits behind instead
  of parsing porcelain text to avoid locale issues.
- Errors during fetch are returned as result dicts (not exceptions)
  because a single skill failing should not block all updates.
- `update_all` and `check_all` iterate over the skills directory
  and only operate on directories containing `.git`.

## Usage examples

```python
from sin_marketplace.updater import Updater

updater = Updater()
status = updater.check_status("sin-infisical")
result = updater.update("sin-infisical")
```

## Known caveats

- Skills installed from local paths (not Git URLs) will fail
  remote checks because `origin` is not configured.
- No rollback mechanism; if a pull breaks a skill, manual recovery
  is required.
