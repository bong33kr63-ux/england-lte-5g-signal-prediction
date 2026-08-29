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

## Recommended review order

For a concise review of the project and its reproducibility, the following order is recommended:

1. Read [`README.md`](README.md) for the project overview and execution instructions.
2. Read [`DATA.md`](DATA.md) for data sources, access requirements and file descriptions.
3. Run [`04_exploratory_data_analysis.ipynb`](notebooks/04_exploratory_data_analysis.ipynb).
4. Run [`06_compare_feature_sets.ipynb`](notebooks/06_compare_feature_sets.ipynb).
5. Run [`07_analyse_final_models.ipynb`](notebooks/07_analyse_final_models.ipynb).
6. Run [`08_run_advanced_experiments.ipynb`](notebooks/08_run_advanced_experiments.ipynb).
7. Consult Notebooks 01–03 and 05 for the complete data-construction workflow.
8. Consult [`requirements.txt`](requirements.txt), [`config.py`](config.py) and [`LICENSE`](LICENSE) for environment, path and licensing information.

## Notebooks

| Order | Notebook | Purpose | Input requirement |
| ----: | -------- | ------- | ----------------- |
| 1 | [`01_build_lte_5g_labels.ipynb`](notebooks/01_build_lte_5g_labels.ipynb) | Builds the England grid and constructs LTE and 5G NR labels | Original Ofcom files |
| 2 | [`02_build_environmental_features.ipynb`](notebooks/02_build_environmental_features.ipynb) | Extracts satellite, land-cover, population and night-time-light variables | Notebook 1 outputs and Google Earth Engine |
| 3 | [`03_build_opencellid_features.ipynb`](notebooks/03_build_opencellid_features.ipynb) | Constructs OpenCellID-derived variables | Notebook 2 outputs and the original OpenCellID file |
| 4 | [`04_exploratory_data_analysis.ipynb`](notebooks/04_exploratory_data_analysis.ipynb) | Examines the targets, predictors and spatial patterns | Provided processed data |
| 5 | [`05_build_progressive_features.ipynb`](notebooks/05_build_progressive_features.ipynb) | Constructs the progressive feature sets, Datasets21–25 | Dataset20 and the original OpenCellID file |
| 6 | [`06_compare_feature_sets.ipynb`](notebooks/06_compare_feature_sets.ipynb) | Compares model performance across Dataset19–25 | Provided processed data |
| 7 | [`07_analyse_final_models.ipynb`](notebooks/07_analyse_final_models.ipynb) | Evaluates and interprets the final LightGBM models | Provided processed data |
| 8 | [`08_run_advanced_experiments.ipynb`](notebooks/08_run_advanced_experiments.ipynb) | Runs imbalance, binary, threshold, spatial, ablation and hierarchical experiments | Provided processed data |

## Reproducing the main analyses

The original Ofcom measurement files and OpenCellID records are not redistributed in this repository because of their size and external-source status. Their official source links, expected filenames and access requirements are documented in [`DATA.md`](DATA.md).

Analysis-ready grid-level datasets are provided in `processed/`. These files allow the dissertation's main analyses to be reproduced without downloading the original measurement-level data.

The following notebooks can be run using the provided processed datasets:

- [`04_exploratory_data_analysis.ipynb`](notebooks/04_exploratory_data_analysis.ipynb)
- [`06_compare_feature_sets.ipynb`](notebooks/06_compare_feature_sets.ipynb)
- [`07_analyse_final_models.ipynb`](notebooks/07_analyse_final_models.ipynb)
- [`08_run_advanced_experiments.ipynb`](notebooks/08_run_advanced_experiments.ipynb)

Notebook 5 is not required for this reproduction route because its Dataset21–25 outputs are already included in `processed/`.

The four notebooks load their required processed datasets independently. They do not need to be executed in the same notebook session.

## Running the main analyses in Google Colab

The main analysis notebooks can be opened directly in Google Colab:

- [Open Notebook 04 in Google Colab](https://colab.research.google.com/github/bong33kr63-ux/england-lte-5g-signal-prediction/blob/main/notebooks/04_exploratory_data_analysis.ipynb)
- [Open Notebook 06 in Google Colab](https://colab.research.google.com/github/bong33kr63-ux/england-lte-5g-signal-prediction/blob/main/notebooks/06_compare_feature_sets.ipynb)
- [Open Notebook 07 in Google Colab](https://colab.research.google.com/github/bong33kr63-ux/england-lte-5g-signal-prediction/blob/main/notebooks/07_analyse_final_models.ipynb)
- [Open Notebook 08 in Google Colab](https://colab.research.google.com/github/bong33kr63-ux/england-lte-5g-signal-prediction/blob/main/notebooks/08_run_advanced_experiments.ipynb)

After opening a notebook, select **Runtime → Run all**. The first setup cell downloads the repository to the temporary Colab runtime and loads the required files from `processed/`. Google Drive access and the original Ofcom and OpenCellID files are not required for these four notebooks.

The notebooks are independent and do not need to be executed in the same Colab session. Notebooks 06 and 08 perform repeated cross-validation experiments and may take considerably longer than Notebooks 04 and 07.

A fixed `random_state=42` is used where supported by the estimator. The same fold-generation procedures are retained to support comparability and reproducibility.

## Local execution

For local execution, clone the complete repository:

```bash
git clone https://github.com/bong33kr63-ux/england-lte-5g-signal-prediction.git
cd england-lte-5g-signal-prediction
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

The complete repository should be retained because the notebooks require both `config.py` and the datasets contained in `processed/`.

## Reconstructing the datasets from source data

Notebooks 01–03 and 05 document the complete data-construction and feature-engineering workflow. They are not required to reproduce the main modelling results provided in Notebooks 04, 06, 07 and 08.

Reconstructing the datasets from the original sources requires:

- the original Ofcom LTE and 5G NR measurement files;
- the original OpenCellID UK export;
- Google Earth Engine authentication;
- access to an enabled Google Cloud project; and
- the source-specific folder structure described in [`DATA.md`](DATA.md).

Because external datasets may be updated after the dissertation was completed, newly downloaded source files may not be identical to the versions used in the submitted analysis.

## Data and attribution

The processed datasets contain grid-level labels and predictors generated for this study. They should not be interpreted as raw Ofcom measurements or verified counts of physical base stations.

OpenCellID-derived variables represent aggregated records from the OpenCellID database. Please consult [`DATA.md`](DATA.md) for the relevant source, licence and attribution information.

## Author

Bong Jun Kim  
MSc Data Science, University of Surrey

## Citation

Kim, B. J. (2026). *Predicting LTE and 5G Signal Quality Using Publicly Available Geospatial Data: A Machine Learning Study Across England*. MSc Data Science dissertation, University of Surrey.
