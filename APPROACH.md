# The approach

```
TODO: Merged into the README file.
```

In the case of the Telco churn project, preparing the model and making use of it in production requires planning for the common steps and separating the training orchestrations.

To maintain a clean and stable system, the project is split into the following:

1. Data Orchestration: During training, we are joining 5 static excel spreadsheets which is not the case in production. The data orchestration stage covers joining the input files.
1. ML Preprocessing: The ML pipeline expects a unified matrix (Pandas DataFrame or Numpy Arrays) where every row represents one observation for classification. This preprocessing will be applied on production requests which would not expect to perform joins and file system operations.

## Stage 1: Data Orchestration
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
        ('encode_city', OneHotEncoder(handle_unknown='ignore'), ['City']),
        ('scale_numeric', StandardScaler(), ['Age', 'Usage']),
        ('keep_as_is', 'passthrough', ['Latitude', 'Longitude'])
    ],
    remainder='drop' # drop unlisted columns
)

# bundle preprocessor and model
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', OurFinalClassifier())
])

# train and Save
model_pipeline.fit(X_train_raw, y_train)
joblib.dump(model_pipeline, 'ml_pipeline.pkl')
```

## Stage 3: Production usage

```
Input could come from an API, Streaming or Batch
```

```python
production_input = pd.DataFrame([{
    'Customer ID': 9921,            # Will be dropped by remainder='drop'
    'City': 'California',           # Will be encoded
    'Age': 34,                      # Will be scaled
    'Longitude': 34.29023,          # Will be kept as-is
    'Latitude': 102.38923,          # Will be kept as-is
    'junk_column_1': 'xyz'          # Will be dropped by remainder='drop'
}])

predictions = model_pipeline.predict(production_input)
```
