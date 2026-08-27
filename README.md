# Predicting LTE and 5G Signal Quality Across England

This repository contains the code used for my MSc Data Science dissertation at the University of Surrey:

> *Predicting LTE and 5G Signal Quality Using Publicly Available Geospatial Data: A Machine Learning Study Across England*

## About the project

The project examines whether public geospatial data can help predict LTE and 5G NR signal-quality classes across England. Ofcom signal measurements were aggregated to a 1 km × 1 km grid and combined with satellite, land-cover, population, night-time-light, OpenCellID and geographic variables.

I compared Random Forest, XGBoost and LightGBM for three signal classes: Excellent, Good and Poor. The later experiments focus on the difficulty of identifying Poor-signal grids and on how well the models generalise to geographically separate areas.

## Main results

- The final dataset contains 4,985 grid cells with at least one LTE or 5G NR label and 35 predictors.
- Class-weighted LightGBM produced mean five-fold CV Macro-F1 scores of 0.4845 for LTE and 0.5348 for 5G NR.
- Poor LTE observations account for only 2.43% of the LTE-labelled grids, making this class particularly difficult to predict.
- With 50 km spatial blocks, mean Macro-F1 fell to 0.4210 for LTE and 0.4519 for 5G NR.
- The ablation experiments showed that geographic context was the most consistently useful predictor group.

## Files

```text
england-lte-5g-signal-prediction/
├── notebooks/       # Eight notebooks, in execution order
├── DATA.md          # Data sources and file locations
├── requirements.txt # Python packages
├── README.md
└── .gitignore
```

## Notebooks

| Order | Notebook | What it does |
|---:|---|---|
| 1 | `01_build_lte_5g_labels.ipynb` | Builds the England grid and creates LTE and 5G NR labels |
| 2 | `02_build_environmental_features.ipynb` | Extracts Sentinel, land-cover, population and night-time-light variables |
| 3 | `03_build_opencellid_features.ipynb` | Adds OpenCellID variables |
| 4 | `04_exploratory_data_analysis.ipynb` | Examines the targets, predictors and spatial patterns |
| 5 | `05_build_progressive_features.ipynb` | Builds the progressive feature sets, Datasets21–25 |
| 6 | `06_compare_feature_sets.ipynb` | Compares model performance across the feature sets |
| 7 | `07_analyse_final_models.ipynb` | Examines the final LightGBM models |
| 8 | `08_run_advanced_experiments.ipynb` | Runs the imbalance, binary, threshold, spatial, ablation and hierarchical experiments |

## Running the notebooks

The notebooks were written in Google Colab and should be run in numerical order. They use `random_state=42` where the estimator supports it.

The raw Ofcom and OpenCellID files are too large to include here. `DATA.md` gives the source links, filenames and Google Drive layout. Notebook 2 also requires Google Earth Engine authentication and access to an enabled Cloud project.

## Author

Bong Jun Kim  
MSc Data Science, University of Surrey

## Citation

Kim, B. J. (2026). *Predicting LTE and 5G Signal Quality Using Publicly Available Geospatial Data: A Machine Learning Study Across England*. MSc Data Science dissertation, University of Surrey.
