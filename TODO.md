# Planned work

- grunt work: (done)
    - [x] add a pre-commit hook for Jupytext, to keep .py and .ipynb modules in sync (`.pre-commit-config.yaml`)
    - [x] add reformatting with black, isort — via ruff (`ruff` + `ruff-format` hooks, isort rules in `pyproject.toml`)
    - [x] configure notebooks and .py modules to different folders (`jupytext.toml`: `.ipynb` in `notebooks/`, `.py` mirrors and cell scripts in `scripts/`; `sandbox.py` moved there)
- first cut: 
    - [x] training data orchestration: join the data for telco
    - [x] run fg-data-profiling for exploratory data analysis
    - [x] scaffold a first classification model: good for getting the CICD going
- deployment
    - [ ] deploy model to Hugging face
- presentation
    - [ ] add a gradio app
- model v1:
    - [ ] align model to expectations, similar to week 3
    - [ ] implement model hyperparameter tuning, cross fold, gridsearch...
- tests
    - [ ] add first set of tests
    - [ ] include tests in CICD pipeline
- report:
    - [ ] report outline
    - [ ] report v1

# Project Outline

Appendix B of Aurélien Géron's "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow" outlines an 8-step project checklist:

1. Frame the Problem and Look at the Big Picture

- Define the objective in business terms.
- Explain how the solution will be used.
- Identify current solutions or workarounds (if any).
- Frame the problem (supervised/unsupervised, online/offline, batch/streaming, classification/regression, etc.).
- Determine how performance will be measured and verify alignment with business goals.
- Establish the minimum performance needed to reach the business objective.
- Look for comparable problems and consider reusing experience or tools.
- Determine if human expertise is available.
- Note how you would solve the problem manually.
- List and verify current assumptions.

2. Get the Data

- Automate data acquisition where possible.
- List needed data and estimate the volume required.
- Document data sources and storage space requirements.
- Check legal obligations and obtain necessary access authorizations.
- Create a dedicated workspace with sufficient storage.
- Acquire the data.
- Convert data into an easily manipulable format (without altering content).
- Anonymize or protect sensitive and personal information.
- Inspect data types and structures (time series, geographical, tabular, etc.).
- Sample a test set, set it aside safely, and avoid data snooping.

3. Explore the Data

- Consult a field expert for guidance if possible.
- Create an exploratory copy of the data (downsample if necessary).
- Build a Jupyter notebook to log exploration steps.
- Analyze each attribute, its characteristics, and missing values.
- Visualize data distributions and correlations.
- Document key insights and patterns.

4. Prepare the Data

- Write functions to clean data (handle missing values, drop or impute outliers).
- Perform feature selection (drop uninformative attributes).
- Conduct feature engineering (decompose features, add transformations).
- Perform feature scaling (standardize or normalize numerical features).
- Automate transformation pipelines for all data preparation steps.

5. Shortlist Promising Models

- Train a wide variety of quick, baseline models using standard parameters.
- Measure and compare performance using cross-validation.
- Analyze the most significant variables and error patterns for each algorithm.
- Perform a rapid round of feature engineering and selection.
- Shortlist the top 3 to 5 most promising models.

6. Fine-Tune the System

- Fine-tune hyperparameters using techniques like random search or Bayesian optimization.
- Try ensemble methods to combine your best models.
- Evaluate the finalized model on the test set to estimate generalization error (do not retrain or tweak based on test results).

7. Present Your Solution

- Document your entire workflow and findings.
- Create a compelling presentation highlighting the big picture and business value.
- Explain how the solution meets the original business objectives.
- Share key visualizations and takeaways.

8. Launch, Monitor, and Maintain

- Prepare your solution for production (export models, connect to inputs/outputs).
- Write monitoring code to detect model drift or performance degradation.
- Set up automated or periodic data pipelines and model retraining.

Reference source: Aurelien Géron's Hands-On ML Appendix B on O'Reilly 
