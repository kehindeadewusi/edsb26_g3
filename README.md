# Telco Churn Gate

## Project activity

![Commits last 30 days](https://img.shields.io/github/commit-activity/m/kehindeadewusi/telco-churn-gate)
![Last commit](https://img.shields.io/github/last-commit/kehindeadewusi/telco-churn-gate)
![Open PRs](https://img.shields.io/github/issues-pr/kehindeadewusi/telco-churn-gate)
![Closed PRs](https://img.shields.io/github/issues-pr-closed/kehindeadewusi/telco-churn-gate)
![Contributors](https://img.shields.io/github/contributors/kehindeadewusi/telco-churn-gate)

### Top contributors

[![Contributors](https://contrib.rocks/image?repo=kehindeadewusi/telco-churn-gate)](https://github.com/kehindeadewusi/telco-churn-gate/graphs/contributors)

Live details: [commits & pushes](https://github.com/kehindeadewusi/telco-churn-gate/commits) -
[pull requests](https://github.com/kehindeadewusi/telco-churn-gate/pulls) -
[pulse (last 30 days)](https://github.com/kehindeadewusi/telco-churn-gate/pulse/monthly) -
[contributor graph](https://github.com/kehindeadewusi/telco-churn-gate/graphs/contributors)

CHURN = customers leaving (closing their subscription)

## Setup (once)

```bash
uv sync                     # build the project environment (.venv) from pyproject.toml
uv run pre-commit install   # activate auto-formatting / sync hooks once
code .
```

## How to work in this repo

Everything lives in plain `.py` files. Blocks separated by `# %%` markers run
cell-by-cell in VS Code — click ▶ "Run Cell" next to a block, exactly like a
Jupyter notebook. Run full scripts from the terminal with:

```bash
uv run python scripts/sandbox.py
```

## What each file/folder is for (jargon-free)

| Path | Role |
|---|---|
| `pyproject.toml` | The dependency recipe: which Python + which packages the project needs |
| `uv.lock` | Frozen copy of the recipe → everyone gets identical versions. Changed deps? run `uv sync` or `uv add <pkg>` again |
| `.venv/` | Where those packages actually got installed. Gitignored — never touch, never commit |
| `scripts/` | Exploratory analysis code — commit it (e.g. `sandbox.py`) |
| `notebooks/` | Your local scratch notebooks (`.ipynb`). Gitignored: the committed "notebook" is its `.py` twin in `scripts/` |
| `jupytext.toml` | Keeps the `notebooks/*.ipynb` ↔ `scripts/*.py` twins pointed at each other |
| `.pre-commit-config.yaml` | On every commit: auto-format code and sync twin notebooks |
| `telco/` | Real project code will go here (e.g. the end-to-end pipeline) |
| `tests/` | Automated tests |
| `data/`, `models/`, `reports/`, `figures/` | Gitignored outputs; big files never get committed |

## Commit etiquette

`git commit` triggers hooks automatically. If a hook fails, red output usually
says exactly what to fix (a lint error, an unformatted file, ...). You can run
all checks any time with:

```bash
uv run pre-commit run -a
```

If you ever want the `.ipynb` of a `.py` in `scripts/`, just run:

```bash
uv run jupytext --sync scripts/<name>.py
```
