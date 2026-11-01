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
# # Exploratory Data Analysis
#
# A quick data profile using `fg-data-profiling`, formerly `y-data-profiling`
#
# Note: We pass in the training split, not the entire split. This avoids leakage and taking decisions on the whole dataset.
#
# Note: This can be used directly by creating a dataframe and calling the explore function. See bottom cell. 
#
# ## TODO/Quesiton:
# 1. Do we want to do EDA other than just offloading to fg-data-profiling?
#

# %%
import pandas as pd
from data_profiling import ProfileReport

def explore(df: pd.DataFrame, output="data/out/report.html"):
    profile = ProfileReport(df, title="Profiling Report")
    profile.to_file(output)
    profile.to_notebook_iframe()


# %%

import matplotlib.pyplot as plt

df = pd.read_excel("data/out/telco.xlsx")
explore(df=df)

# %% [markdown]
# ## Hypothesis Generation
#
# ### TODO:
#
# 1. Data profiling highlights
# 1. Outline the relationships between the features and targets

# %%
# cool = retained, warm = churned
churn_colors = {'No': '#2a78d6', 'Yes': '#eb6834'}

ax = None
for label, color in churn_colors.items():
    ax = df[df['Churn Label'] == label].plot(
        kind='scatter',
        x='Longitude',
        y='Latitude',
        c=color,
        s=8,
        alpha=0.35,
        figsize=(7, 8),
        ax=ax,
    )

ax.set_title('Churn by location')
ax.legend(
    handles=[
        plt.Line2D([], [], marker='o', linestyle='', color=color, label=f'Churn Label = {label}')
        for label, color in churn_colors.items()
    ],
    frameon=False,
)
