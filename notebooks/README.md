# Notebook pairing layout

- `.ipynb` notebooks live here (`notebooks/`)
- Their `.py` (percent format) mirrors live in `scripts/`
- Pairs are kept in sync by the pre-commit jupytext hook — see `jupytext.toml`

Note: `.gitignore` ignores `*.ipynb`, so the `.py` mirrors are the versioned
source of truth; the `.ipynb` files stay local.
