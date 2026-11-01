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
# # Cleaning
#
# The cleaning module will centralize cleaning logic so that it can be easily reused by the model as part of it's pipeline.
#
# ## TODO
# 1. Implement further cleaning based on EDA
# 1. Make custom attribute transformers. This will provide an easy way to apply different cleaning options and hyperparameters via the pipeline.
# 1. Consider a mean inputer for all numerical, good for future "suddenly missing" values. An alternative would be to validate future input and prevent running the pipeline when values are missing or invalid.

# %% [markdown]
# ## insights from EDA:
# 1. Numericals: No missing numerical. In this first cut, we'll just scale all numericals
#     1. Age
#     1. Number of Dependents
#     1. Number of Referrals
#     1. Tenure in Months
#     1. Avg Monthly Long Distance Charges
#     1. Avg Monthly GB Download
#     1. Monthly Charge
#     1. Total Charges
#     1. Total Refunds
#     1. Total Extra Data Charges
#     1. Total Long Distance Charges
#     1. Total Revenue
#     1. Zip Code: Probably drop in favour of Longitude and Latitude
#     1. Latitude
#     1. Longitude
#     1. Population
# 1. 2 Texts:
#     1. Customer ID
#     1. City: We will drop city in favour of Longitude and Latitude, these provide more context. `remainder=drop` can take care of this.
# 1. 5 Categorical:
#     1. Gender: Nominal
#     1. Offer: Nominal, OneHot encode
#     1. Internet Type, Nominal?
#     1. Contract: Ordinal
#     1. Payment Method: Nominal, OneHot encode
# 1. 18 Booleans:
#     1. Under 30: Drop in favour of age
#     1. Senior Citizen: Can be dropped in favour of age
#     1. Married
#     1. Dependents
#     1. Referred a Friend
#     1. Phone Service
#     1. Multiple Lines
#     1. Internet Service
#     1. Online Security
#     1. Online Backup
#     1. Device Protection Plan
#     1. Premium Tech Support
#     1. Streaming TV
#     1. Streaming Movies
#     1. Streaming Music
#     1. Unlimited Data
#     1. Paperless Billing
#     1. Churn Label*: Target
#
#
# ## Quick Cleaning
#
# 1. Offer: Categorical, Has 55% missing values. The requirement wants the missing values preserved.
# 1. Internet Type: Categorical, 21.7% missing, Correlated with bool Internet Service
# 1. State: Categorical, Constant, California. Now dropped in preprocessing
#
# ## Currently Ignoring
# 1. Zip Code: Correlated with Latitude and Longitude and currently pretending to be numerical.
# 1. Combined or derived columns: If we decide on these, we'll write a custom transformer that can easily be plugged into the workflow.

# %% [markdown]
# ## Return Type
#
# The cleaning phase will return a pipeline; the same pipeline will be employed during training and production classification.

# %%
NUMERICALS = [ 
    'Age', 'Number of Dependents', 'Number of Referrals',
    'Tenure in Months', 'Avg Monthly Long Distance Charges',
    'Avg Monthly GB Download', 'Monthly Charge', 'Total Charges', 
    'Total Refunds', 'Total Extra Data Charges', 'Total Long Distance Charges',
    'Total Revenue', 'Zip Code', 'Latitude', 'Longitude', 'Population'
]

TEXTS = ['CITY']

CATEGORICAL_NOMINALS = [
    'Gender', 'Offer', 'Internet Type', 'Payment Method',
]

CATEGORICAL_ORDINALS = [
    'Contract'
]

BOOLEANS = [
    'Under 30', 'Senior Citizen', 'Married', 
    'Dependents', 'Referred a Friend', 'Phone Service',
    'Multiple Lines', 'Internet Service', 'Online Security', 
    'Online Backup', 'Device Protection Plan', 'Premium Tech Support',
    'Streaming TV', 'Streaming Movies', 'Streaming Music',
    'Unlimited Data', 'Paperless Billing',
]

TARGET = 'Churn Label'


# %%
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# %%
# numeric pipelines
num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy="median")), # we'll impute numericals in case of missing in later trainings or fail loudly in pre-processing.
    ('std_scaler', StandardScaler())
])

# %%
preprocessor = ColumnTransformer(
    transformers=[
        ('num', num_pipeline, NUMERICALS),
        ('nominals', OneHotEncoder(), CATEGORICAL_NOMINALS),
        # ('keep_as_is', 'passthrough', CATEGORICAL_ORDINALS), # TODO: enhance these as necessary, encode differently
        ('ordinals', OneHotEncoder(), CATEGORICAL_ORDINALS),
    ], 
    remainder='drop'
)
