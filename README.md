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
uv run python scripts/orchestration.py # creates an intermediate file, see data/out
uv run python scripts/modeling.py # creates a model, see data/out
uv run python scripts/classify.py # a sample classification

uv run python scripts/eda.py # EDA, with fg-data-profiling
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

## Workflow

Preparing the model and making use of it in production requires planning for the common steps and separating the training orchestrations:

1. Data Orchestration: During training, we join 5 static excel spreadsheets which is not the case in production. The data orchestration stage covers joining the input files.
1. ML Preprocessing: In production, the ML pipeline expects a unified matrix (Pandas DataFrame or Numpy Arrays) where every row represents one observation for classification. We do not expect to perform joins and file system operations. Preprocessing is automatically applied to production requests as part of fulfiling requests.

### Stage 1: Data Orchestration
```python
def create_dataset(demo, loc, pop, serv, status):
    # Join data sources
    df_demo = pd.read_excel(demo)
    df_loc = pd.read_excel(loc)
    df_pop = pd.read_excel(pop)
    df_serv = pd.read_excel(serv)
    df_status = pd.read_excel(status)

    # Merge into a single flat DataFrame
    base_df = df_tx.merge(df_demo, df_loc, df_pop, df_serv ...)
    final_df = base_df.join(pop, on='zip_code')
    return final_df

# Training Phase
X_train_raw = create_dataset("demo.xlsx", "loc.xlsx", "pop.xlsx", "serv.xlsx", "status.xlsx")

```

### Stage 2: Training

```python
preprocessor = ColumnTransformer(
    transformers=[
        ("encode_city", OneHotEncoder(handle_unknown="ignore"), ["City"]),
        ("scale_numeric", StandardScaler(), ["Age", "Usage"]),
        ("keep_as_is", "passthrough", ["Latitude", "Longitude"]),
    ],
    remainder="drop",  # drop unlisted columns
)

# bundle preprocessor and model
model_pipeline = Pipeline(
    steps=[("preprocessor", preprocessor), ("classifier", OurFinalClassifier())]
)

# train and Save
model_pipeline.fit(X_train_raw, y_train)
joblib.dump(model_pipeline, "ml_pipeline.pkl")
```

## Stage 3: Production usage
```
Input could come from an API, Streaming or Batch
```

```python
production_input = pd.DataFrame(
    [
        {
            "Customer ID": 9921,  # Will be dropped by remainder='drop'
            "City": "California",  # Will be encoded
            "Age": 34,  # Will be scaled
            "Longitude": 34.29023,  # Will be kept as-is
            "Latitude": 102.38923,  # Will be kept as-is
            "junk_column_1": "xyz",  # Will be dropped by remainder='drop'
        }
    ]
)

predictions = model_pipeline.predict(production_input)
```
