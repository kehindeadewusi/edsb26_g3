# Planned work

- grunt work: (done)
    - [x] add a pre-commit hook for Jupytext, to keep .py and .ipynb modules in sync (`.pre-commit-config.yaml`)
    - [x] add reformatting with black, isort — via ruff (`ruff` + `ruff-format` hooks, isort rules in `pyproject.toml`)
    - [x] configure notebooks and .py modules to different folders (`jupytext.toml`: `.ipynb` in `notebooks/`, `.py` mirrors and cell scripts in `scripts/`; `sandbox.py` moved there)
- first cut: join the data for telco, and run ydata-profiling for exploratory data analysis
- create an scaffold end-2-end pipeline, similar to week 3 (scaffold only)
- add first set of tests
- model!
