# %%
import pandas as pd
from utils import print_centered_header

# %%
demographics = pd.read_excel('data/Telco_customer_churn_demographics.xlsx')
demographics.head()

# %%
demographics.info()

# %%
demographics.describe()

# %%
print_centered_header("Demographics")
print(f"shape: {demographics.shape}")
print(f"unique customer ids: {demographics["Customer ID"].nunique()}")

# %%
locations = pd.read_excel('data/Telco_customer_churn_location.xlsx')
locations.head()

# %%
locations.info()

# %%
locations.describe()

# %%
print_centered_header("Locations")
print(f"shape: {locations.shape}")
print(f"unique customer ids: {locations["Customer ID"].nunique()}")

# %%
population = pd.read_excel('data/Telco_customer_churn_population.xlsx')
population.head()

# %%
population.info()

# %%
population.describe()

# %%
print_centered_header("Population")
print(f"shape: {population.shape}")
print(f"unique zip codes: {population["Zip Code"].nunique()}")

# %%
services = pd.read_excel('data/Telco_customer_churn_services.xlsx')
services.head()

# %%
services.info()

# %%
services.describe()

# %%
print_centered_header("Services")
print(f"shape: {services.shape}")
print(f"unique customer ids: {services["Customer ID"].nunique()}")

# %%
status = pd.read_excel('data/Telco_customer_churn_status.xlsx')
status.head()

# %%
status.info()

# %%
status.describe()

# %%
print_centered_header("Status")
print(f"shape: {status.shape}")
print(f"unique customer ids: {status["Customer ID"].nunique()}")

# %% [markdown]
# ## Highlights:
#
# 1. Demographics is unique, one row for every customer identified by Customer ID
# 1. Locations include the physical locations of the customer, identified by one unique Customer ID per record.
# 1. Population holds population count per Zip Code. It is linked to customer degraphics by the Zip Code.
# 1. Services hold the plans a customer is subscribed to, one unique record per customer. 
# 1. Status contain the target of the prediction. The other features are leaky and the training would fit to them.
#
# ```
# We will presume Demographics all the records must be present for the customer i.e. every customer will have an entry in Demographics, Location, Services and Status. We will also presume that every customer has a location which is joined to the Population dataset by the Zip Code
# ```

# %%
demographics.head(3)

# %%
demographics.set_index("Customer ID", inplace=True)
demographics.drop(columns=["Count"], inplace=True)
print(len(demographics))
demographics.head(3)

# %%
services.set_index("Customer ID", inplace=True)
services.drop(columns=["Count", "Quarter"], inplace=True)
len(services)
services.head(3)

# %%
status.head(3)

# %% [markdown]
# ## Status
# Includes the target `Churn Label`, but also contains features that are leakages i.e. 
#
# 1. Correlated to Churn
# 1. Known after a churn
# 1. A prediction of churn by some other means
#
# We drop the following:
# 1. Count: The same for all customers
# 1. Quarter: The same for all customers
# 1. Satisfaction Score: Correlated with churn
# 1. Customer Status: Post Churn
# 1. Churn Value: Similar to the Churn label
# 1. Churn Score: A prediction by another model
# 1. CLTV: Some prediction by an internal system, a `model`
# 1. Churn Category: Known after a churn
# 1. Churn Reason: Known after a churn

# %%
status.drop(
    columns=[
        "Count", 
        "Quarter", 
        "Satisfaction Score", 
        "Customer Status", 
        "Churn Value", 
        "Churn Score", 
        "CLTV", 
        "Churn Category",
        "Churn Reason"
    ], 
    inplace=True
)
status.set_index("Customer ID", inplace=True)
status.head(3)

# %% [markdown]
# ## Locations
#
# We drop the following columns:
#
# 1. Count: The same for all customers
# 1. State: The same for all customers
# 1. Country: The same for all customers
# 1. Lat Long: The same as the latitude and longitude joined together. (Should be easier to manipulate them separately if necessary)
#

# %%
locations.drop(columns=["Count", "Country", "State", "Lat Long"], inplace=True)
locations.set_index("Customer ID", inplace=True)
locations.head(3)

# %% [markdown]
# ## Population

# %%
population.set_index("Zip Code")
population.drop(columns=["ID"], inplace=True)
population.head(3)

# %% [markdown]
# ## Merge
#
# One simple dataframe for further exploration

# %%
df = pd.concat([demographics, status, services, locations], axis=1)
df = pd.merge(df.reset_index(), population, on="Zip Code")
print(len(df))
df.head(3)

# %%
df.columns

# %%
df.to_excel("data/out/telco.xlsx", index=False)
