# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.6
#   kernelspec:
#     display_name: edsb26-g3 (3.13.7)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Model Training & Evaluation
#
# ## TODO:
# 1. Baseline Selection
# 1. Model Selection
# 1. Hyperparameter Tuning
# 1. Evaluation Metrics

# %%
# pick up edits to cleaning.py (and friends) without restarting the kernel
# %load_ext autoreload
# %autoreload 2

import numpy as np
import pandas as pd

np.random.seed(42)  # 42 the ultimate

# %%
df = pd.read_excel("data/out/telco.xlsx")  # TODO: change to import and call a function.

# %% [markdown]
# ## Splitting into Train/Test Set
# We have very few records in our database, 7043, so we cannot rely on random sampling to avoid a sampling bias.
# Our churn label has 73.5% False and 26.5% True (churned), so we would use `Stratified Sampling` on our train/test split.
#
# ```
# See profiling output in data/out/report.html
# ```
#

# %%
from sklearn.model_selection import train_test_split

train_split, test_split = train_test_split(
    df, test_size=0.2, stratify=df["Churn Label"], random_state=42
)

# %%
print(len(train_split))
print(len(test_split))

# %%
import joblib
from cleaning import preprocessor
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

# %%
model_pipeline = Pipeline(
    steps=[("preprocessor", preprocessor), ("classifier", RandomForestClassifier())]
)

# quick model, no validation set, no hyperparameter tuning
X_train = train_split.drop("Churn Label", axis=1)
y_train = train_split["Churn Label"].copy()

# %%
model_pipeline.fit(X_train, y_train)
joblib.dump(model_pipeline, "data/out/telco_pipeline.pkl")
