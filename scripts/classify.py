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
# # Classify
#
# A notebook to test the Telco model i.e. use the model to classify based on user input.
#
# ```Note:``` Gradio will do something similar to this, using this model when hosted on Hugging Face. We could also put this on a web server using something like FastAPI.
#
# ## Steps:
# 1. run orchestration.ipynb
# 1. run modeling.ipynb
# 1. this notebook to test the model.

# %%
import joblib
import pandas as pd

# %%
model_pipeline = joblib.load("data/out/telco_pipeline.pkl")

# %%
input_df = pd.DataFrame(
    [
        {
            "Total Revenue": 100000,
            "Monthly Charge": 30000,
            "Total Extra Data Charges": 3200000,
            "Latitude": 34.988922,
            "Longitude": 102.332332,
            "Number of Dependents": 3,
            "Age": 60,
            "Avg Monthly GB Download": 200000,
            "Total Refunds": 34400,
            "Avg Monthly Long Distance Charges": 2345,
            "Gender": "Male",
            "Internet Type": "Fiber Optic",
            "Total Long Distance Charges": 234.45,
            "Payment Method": "Credit Card",
            "Number of Referrals": 2,
            "Contract": "Month-to-Month",
            "Population": 63288,
            "Offer": "Offer E",
            "Tenure in Months": 27,
            "Total Charges": 635,
            "Zip Code": 90063,
        }
    ]
)
predictions = model_pipeline.predict(input_df)
print(f"Classified Label: {predictions[0]}")

# %%
probabilities = model_pipeline.predict_proba(input_df)
print(f"Probability of Class 1: {probabilities[0][1] * 100}%")
