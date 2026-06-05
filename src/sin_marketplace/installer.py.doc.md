# Purpose: Skill installer — clone, setup, and register skills
# Docs: installer.py.doc.md

## What this file does

Clones skill repositories from Git, runs any setup scripts,
installs Python dependencies, and registers the skill in
`~/.config/opencode/opencode.json`.

## Dependencies

- `GitPython` for cloning repositories
- `subprocess` for running setup scripts

## Important config values

- `DEFAULT_SKILLS_DIR`: `~/.config/opencode/skills`
- `OPENCODE_CONFIG`: `~/.config/opencode/opencode.json`

## Why certain decisions were made

- `shutil.rmtree` before re-cloning ensures clean installs.
- `pip install -e` is used for editable installs when `pyproject.toml`
  or `setup.py` exists.
- `opencode.json` is modified atomically (read → modify → write) to
  prevent corruption.

## Usage examples

```python
from sin_marketplace.installer import Installer

installer = Installer()
record = installer.install(
    slug="sin-infisical",
    source="https://github.com/OpenSIN-Code/sin-infisical",
)
```

## Known caveats

- `install.sh` failures are logged as warnings, not errors.
- The git clone is shallow (`depth=1`) to minimize network traffic.
