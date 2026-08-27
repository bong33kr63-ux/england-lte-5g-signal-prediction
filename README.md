# Predicting LTE and 5G Signal Quality Across England

Machine-learning prediction of LTE and 5G signal quality across England using publicly available geospatial data.

## Overview

This repository contains the data-processing and modelling notebooks developed for the MSc Data Science dissertation:

> **Predicting LTE and 5G Signal Quality Using Publicly Available Geospatial Data: A Machine Learning Study Across England**

The study integrates Ofcom LTE and 5G NR measurements with satellite, land-cover, population, night-time-light, cellular-infrastructure, and geographic data on a common 1 km × 1 km grid. Random Forest, XGBoost, and LightGBM models are evaluated for three-class signal-quality prediction and Poor-signal detection.

## Key Results

- The final dataset contains 4,985 labelled-union grid cells and 35 predictors.
- Class-weighted LightGBM achieved mean five-fold CV Macro-F1 scores of 0.4845 for LTE and 0.5348 for 5G NR.
- Poor-signal prediction was substantially more difficult for LTE, where Poor observations represented 2.43% of the labelled sample.
- Spatial Block Cross-Validation reduced mean Macro-F1 to 0.4210 for LTE and 0.4519 for 5G NR at the principal 50 km block size.
- Geographic context was the most consistently useful predictor group in the ablation experiments.

## Repository Structure

```text
england-lte-5g-signal-prediction/
├── notebooks/       # Data construction, EDA, feature engineering and modelling
├── README.md        # Project overview and execution guide
├── DATA.md          # Data sources and expected file locations
├── requirements.txt # Python dependencies
└── .gitignore
```

## Notebook Workflow

| Order | Notebook | Purpose |
|---:|---|---|
| 1 | `01_build_lte_5g_labels.ipynb` | Construct the England grid and LTE/5G NR labels |
| 2 | `02_build_environmental_features.ipynb` | Extract Sentinel, land-cover, population and night-light features |
| 3 | `03_build_opencellid_features.ipynb` | Add OpenCellID infrastructure features |
| 4 | `04_exploratory_data_analysis.ipynb` | Explore class balance, predictor relationships and spatial patterns |
| 5 | `05_build_progressive_features.ipynb` | Construct Datasets21–25 through progressive feature engineering |
| 6 | `06_compare_feature_sets.ipynb` | Compare models across progressive feature sets |
| 7 | `07_analyse_final_models.ipynb` | Analyse final LightGBM models and feature importance |
| 8 | `08_run_advanced_experiments.ipynb` | Run imbalance, binary, threshold, spatial, ablation and hierarchical experiments |

## Data Availability

Large raw datasets are not included because of file-size and redistribution constraints. See `DATA.md` for the required sources, filenames, and directory structure.

## Reproducibility

The notebooks were developed in Google Colab and should be run in numerical order. A fixed random state of 42 is used wherever supported. Some stages require Google Earth Engine authentication and access to the raw Ofcom and OpenCellID files.

Detailed setup instructions and repository-relative path configuration will be added before the repository is made public.

## Author

**Bong Jun Kim**  
MSc Data Science, University of Surrey

## Citation

If you use this repository, please cite the associated dissertation:

> Kim, B. J. (2026). *Predicting LTE and 5G Signal Quality Using Publicly Available Geospatial Data: A Machine Learning Study Across England*. MSc Data Science dissertation, University of Surrey.
