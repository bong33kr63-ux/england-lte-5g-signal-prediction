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
├── DATA.md             # Data sources, filenames and access requirements
├── requirements.txt    # Required Python packages
├── README.md
├── LICENSE
└── .gitignore
```

## Submitted and GitHub versions

The notebooks and processed datasets in this GitHub repository are identical to those provided with the submitted dissertation materials.

The notebooks were originally developed and successfully executed in Google Colab using files stored in Google Drive. The original notebook structure and analysis code have been retained to ensure consistency with the submitted results.

Because the notebooks retain the paths used in the original Google Drive environment, users wishing to rerun them should update the relevant file paths to match their own local or cloud directory structure.

## Recommended review order

For a concise review of the project and its reproducibility, the following order is recommended:

1. Read [`README.md`](README.md) for the project overview and execution guidance.
2. Read [`DATA.md`](DATA.md) for data sources, access requirements and file descriptions.
3. Review and, if desired, rerun [`04_exploratory_data_analysis.ipynb`](notebooks/04_exploratory_data_analysis.ipynb).
4. Review and, if desired, rerun [`06_compare_feature_sets.ipynb`](notebooks/06_compare_feature_sets.ipynb).
5. Review and, if desired, rerun [`07_analyse_final_models.ipynb`](notebooks/07_analyse_final_models.ipynb).
6. Review and, if desired, rerun [`08_run_advanced_experiments.ipynb`](notebooks/08_run_advanced_experiments.ipynb).
7. Consult Notebooks 01–03 and 05 for the complete data-construction workflow.
8. Consult [`requirements.txt`](requirements.txt) and [`LICENSE`](LICENSE) for software-environment and licensing information.

## Notebooks

| Order | Notebook | Purpose | Input requirement |
| ----: | -------- | ------- | ----------------- |
| 1 | [`01_build_lte_5g_labels.ipynb`](notebooks/01_build_lte_5g_labels.ipynb) | Builds the England grid and constructs LTE and 5G NR labels | Original Ofcom files |
| 2 | [`02_build_environmental_features.ipynb`](notebooks/02_build_environmental_features.ipynb) | Extracts satellite, land-cover, population and night-time-light variables | Notebook 1 outputs and Google Earth Engine |
| 3 | [`03_build_opencellid_features.ipynb`](notebooks/03_build_opencellid_features.ipynb) | Constructs OpenCellID-derived variables | Notebook 2 outputs and the original OpenCellID file |
| 4 | [`04_exploratory_data_analysis.ipynb`](notebooks/04_exploratory_data_analysis.ipynb) | Examines the targets, predictors and spatial patterns | Provided Dataset20 files |
| 5 | [`05_build_progressive_features.ipynb`](notebooks/05_build_progressive_features.ipynb) | Constructs the progressive feature sets, Datasets21–25 | Dataset20 and the original OpenCellID file |
| 6 | [`06_compare_feature_sets.ipynb`](notebooks/06_compare_feature_sets.ipynb) | Compares model performance across Dataset19–25 | Provided Dataset19–25 CSV files |
| 7 | [`07_analyse_final_models.ipynb`](notebooks/07_analyse_final_models.ipynb) | Evaluates and interprets the final LightGBM models | Provided Dataset25 CSV file |
| 8 | [`08_run_advanced_experiments.ipynb`](notebooks/08_run_advanced_experiments.ipynb) | Runs imbalance, binary, threshold, spatial, ablation and hierarchical experiments | Provided Dataset25 CSV file |

## Reproducing the main analyses

The original Ofcom measurement files and OpenCellID records are not redistributed in this repository because of their size and external-source status. Their official source links, expected filenames and access requirements are documented in [`DATA.md`](DATA.md).

Analysis-ready grid-level datasets are provided in `processed/`. These files allow the main analyses to be reproduced without downloading and processing the original measurement-level data.

The following notebooks can be evaluated using the provided processed datasets:

- [`04_exploratory_data_analysis.ipynb`](notebooks/04_exploratory_data_analysis.ipynb)
- [`06_compare_feature_sets.ipynb`](notebooks/06_compare_feature_sets.ipynb)
- [`07_analyse_final_models.ipynb`](notebooks/07_analyse_final_models.ipynb)
- [`08_run_advanced_experiments.ipynb`](notebooks/08_run_advanced_experiments.ipynb)

Their principal input requirements are:

| Notebook | Required processed files |
| -------- | ------------------------ |
| Notebook 04 | `dataset20_final.csv` and `dataset20_final.gpkg` |
| Notebook 06 | Dataset19–25 CSV files |
| Notebook 07 | `dataset25_final.csv` |
| Notebook 08 | `dataset25_final.csv` |

Notebook 05 does not need to be rerun for this reproduction route because its Dataset21–25 outputs are already provided in `processed/`.

The four main analysis notebooks use their required processed datasets independently and do not need to be executed in the same notebook session.

## Running the notebooks

The notebooks were developed in Google Colab and contain paths corresponding to the original Google Drive folder structure.

To rerun a notebook:

1. Download or clone this repository.
2. Place the required processed files in an accessible local or Google Drive folder.
3. Open the relevant notebook in Google Colab or another compatible Jupyter environment.
4. Update the input and output paths in the notebook setup cells to match the selected folder structure.
5. Install any missing packages listed in [`requirements.txt`](requirements.txt).
6. Run the notebook cells in order.

For example, Notebook 04 requires the supplied `dataset20_final.csv` and `dataset20_final.gpkg`, while Notebooks 07 and 08 require `dataset25_final.csv`.

Notebooks 06 and 08 perform repeated cross-validation experiments and may take considerably longer than Notebooks 04 and 07.

A fixed `random_state=42` is used where supported by the estimator. The same fold-generation procedures are retained to support comparability and reproducibility. Minor numerical differences may nevertheless occur because of differences in package versions, operating systems or computational environments.

## Reconstructing the datasets from source data

Notebooks 01–03 and 05 document the complete data-construction and feature-engineering workflow. They are not required to reproduce the main modelling results using the supplied processed datasets.

The complete data-construction sequence is:

```text
01_build_lte_5g_labels.ipynb
        ↓
02_build_environmental_features.ipynb
        ↓
03_build_opencellid_features.ipynb
        ↓
05_build_progressive_features.ipynb
```

Reconstructing the datasets from the original sources requires:

- the original Ofcom LTE and 5G NR measurement files;
- the original OpenCellID UK export;
- Google Earth Engine authentication;
- access to an enabled Google Cloud project; and
- the source-specific folder structure described in [`DATA.md`](DATA.md).

Because externally maintained datasets may be updated after the dissertation was completed, newly downloaded source files may not be identical to the versions used in the submitted analysis.

## Data and attribution

The processed datasets contain grid-level labels and predictors generated for this study. They are not copies of the raw Ofcom measurement files and should not be interpreted as independently verified counts of physical base stations.

OpenCellID-derived variables represent aggregated records from the OpenCellID database. Please consult [`DATA.md`](DATA.md) for the relevant source, licence and attribution information.

## Licence

The original project code in this repository is released under the [MIT License](LICENSE).

This licence applies to the project code and does not override the licences or terms of the external data sources. Ofcom, OpenCellID, Google Earth Engine datasets, GADM and derived data remain subject to the relevant providers' terms and attribution requirements. See [`DATA.md`](DATA.md) for details.

## Author

Bong Jun Kim  
MSc Data Science, University of Surrey

## Citation

Kim, B. J. (2026). *Predicting LTE and 5G Signal Quality Using Publicly Available Geospatial Data: A Machine Learning Study Across England*. MSc Data Science dissertation, University of Surrey.
