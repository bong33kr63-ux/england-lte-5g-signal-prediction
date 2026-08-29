# Predicting LTE and 5G Signal Quality Across England

This repository contains the code and analysis-ready datasets used for my MSc Data Science dissertation at the University of Surrey:

> *Predicting LTE and 5G Signal Quality Using Publicly Available Geospatial Data: A Machine Learning Study Across England*

## About the project

This project examines whether publicly available geospatial data can help predict LTE and 5G NR signal-quality classes across England. Ofcom signal measurements were aggregated to a 1 km × 1 km grid and combined with satellite, land-cover, population, night-time-light, OpenCellID and geographic variables.

Random Forest, XGBoost and LightGBM were compared for three signal-quality classes: Excellent, Good and Poor. Further experiments examined minority-class detection, decision thresholds, geographical generalisation, feature-group ablation and hierarchical classification.

## Main results

- The final dataset contains 4,985 grid cells with at least one LTE or 5G NR label and 35 predictors.
- Class-weighted LightGBM achieved mean five-fold CV Macro-F1 scores of 0.4845 for LTE and 0.5348 for 5G NR.
- Poor LTE observations represent only 2.43% of the LTE-labelled grids, making this class particularly difficult to identify.
- Using 50 km spatial blocks, mean Macro-F1 decreased to 0.4210 for LTE and 0.4519 for 5G NR.
- The ablation experiments indicated that geographic context was the most consistently useful predictor group.

## Repository structure

```text
england-lte-5g-signal-prediction/
├── notebooks/          # Eight notebooks documenting the complete workflow
├── processed/          # Analysis-ready datasets for core reproduction
├── DATA.md             # Raw-data sources and expected filenames
├── config.py           # Shared file and directory settings
├── requirements.txt    # Required Python packages
├── README.md
├── LICENSE
└── .gitignore
```

## Notebooks

| Order | Notebook | Purpose | Input requirement |
| ----: | -------- | ------- | ----------------- |
| 1 | `01_build_lte_5g_labels.ipynb` | Builds the England grid and constructs LTE and 5G NR labels | Original Ofcom files |
| 2 | `02_build_environmental_features.ipynb` | Extracts satellite, land-cover, population and night-time-light variables | Notebook 1 outputs and Google Earth Engine |
| 3 | `03_build_opencellid_features.ipynb` | Constructs OpenCellID-derived variables | Notebook 2 outputs and the original OpenCellID file |
| 4 | `04_exploratory_data_analysis.ipynb` | Examines the targets, predictors and spatial patterns | Provided processed data |
| 5 | `05_build_progressive_features.ipynb` | Constructs the progressive feature sets, Datasets21–25 | Dataset20 and the original OpenCellID file |
| 6 | `06_compare_feature_sets.ipynb` | Compares model performance across Dataset19–25 | Provided processed data |
| 7 | `07_analyse_final_models.ipynb` | Evaluates and interprets the final LightGBM models | Provided processed data |
| 8 | `08_run_advanced_experiments.ipynb` | Runs imbalance, binary, threshold, spatial, ablation and hierarchical experiments | Provided processed data |

## Reproducing the main analyses

The original Ofcom measurement files and OpenCellID records are not redistributed in this repository because of their size and external-source status. Their official source links, expected filenames and access requirements are documented in `DATA.md`.

Analysis-ready grid-level datasets are provided in `processed/`. These files allow the dissertation's main analyses to be reproduced without downloading the original measurement-level data.

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

The following notebooks can then be run using the provided processed datasets:

```text
04_exploratory_data_analysis.ipynb
06_compare_feature_sets.ipynb
07_analyse_final_models.ipynb
08_run_advanced_experiments.ipynb
```

Notebook 5 is not required for this reproduction route because its Dataset21–25 outputs are already included in `processed/`.

The four notebooks load their required processed datasets independently. They do not need to be executed in the same notebook session.

## Google Colab setup

The notebooks were developed in Google Colab. The repository setup cells and shared paths are defined through `config.py`.

To reproduce the main analyses in Colab, use the complete repository rather than uploading individual notebooks. The notebooks require both `config.py` and the datasets contained in `processed/`.

A fixed `random_state=42` is used where supported by the estimator. The same fold-generation procedures are retained to support comparability and reproducibility.

## Reconstructing the datasets from source data

Notebooks 01–03 and 05 document the complete data-construction and feature-engineering workflow. They are not required to reproduce the main modelling results provided in Notebooks 04, 06, 07 and 08.

Reconstructing the datasets from the original sources requires:

- the original Ofcom LTE and 5G NR measurement files;
- the original OpenCellID UK export;
- Google Earth Engine authentication;
- access to an enabled Google Cloud project; and
- the source-specific folder structure described in `DATA.md`.

Because external datasets may be updated after the dissertation was completed, newly downloaded source files may not be identical to the versions used in the submitted analysis.

## Data and attribution

The processed datasets contain grid-level labels and predictors generated for this study. They should not be interpreted as raw Ofcom measurements or verified counts of physical base stations.

OpenCellID-derived variables represent aggregated records from the OpenCellID database. Please consult `DATA.md` for the relevant source, licence and attribution information.

## Author

Bong Jun Kim  
MSc Data Science, University of Surrey

## Citation

Kim, B. J. (2026). *Predicting LTE and 5G Signal Quality Using Publicly Available Geospatial Data: A Machine Learning Study Across England*. MSc Data Science dissertation, University of Surrey.
