# Data

This document describes the original external data sources, the filenames used by the notebooks and the analysis-ready processed datasets included in this repository.

## Data availability

The original Ofcom LTE and 5G NR measurement files and the original OpenCellID UK export are not included in this repository. The Ofcom files are several gigabytes in size, while access to the OpenCellID export is subject to the provider's current account, access and attribution requirements.

To support reproduction of the principal analyses without requiring the original large files, the processed grid-level datasets used in the dissertation are provided in `processed/`.

## Original data to download

| Data | Filename used by the notebooks | Source |
| ---- | ------------------------------ | ------ |
| Ofcom 4G LTE measurements for 2025 | `4g-lte-2025-mobile-signal-measurement-data.csv` | [Ofcom 2025 LTE ZIP download](https://www.ofcom.org.uk/siteassets/resources/documents/phones-telecoms-and-internet/coverage/mobile-signal-strength-measurement-data-from-spectrum-assurance-vehicles/4g-lte-2025-mobile-signal-measurement-data.zip?v=413277) |
| Ofcom 5G NR measurements for 2025 | `5g-nr-2025-mobile-signal-measurement-data.csv` | [Ofcom 2025 5G NR ZIP download](https://www.ofcom.org.uk/siteassets/resources/documents/phones-telecoms-and-internet/coverage/mobile-signal-strength-measurement-data-from-spectrum-assurance-vehicles/5g-nr-2025-mobile-signal-measurement-data.zip?v=413278) |
| OpenCellID UK export (MCC 234) | `234_raw.csv` | [OpenCellID country downloads](https://opencellid.org/downloads/) |

The Ofcom LTE and 5G NR entries are listed on the official [Ofcom mobile signal-strength measurement data page](https://www.ofcom.org.uk/phones-and-broadband/coverage-and-speeds/mobile-signal-strength-measurement-data) as:

- **4G LTE mobile signal strength measurement data (2025)** — last updated 6 March 2026;
- **5G NR mobile signal strength measurement data (2025)** — last updated 6 March 2026.

After downloading the Ofcom ZIP archives, extract the CSV files and retain the filenames shown in the table above.

Downloading an OpenCellID country export may require an account and API access token. Users should consult the current [OpenCellID download page](https://opencellid.org/downloads/) and [server usage policy](https://wiki.opencellid.org/wiki/Server_usage_policy) before downloading or redistributing the data.

## Original Google Drive layout

The notebooks were developed and executed using the following Google Drive structure:

```text
MyDrive/
└── Dissertation/
    ├── Ofcom dataset/
    │   ├── 4g-lte-2025-mobile-signal-measurement-data.csv
    │   └── 5g-nr-2025-mobile-signal-measurement-data.csv
    ├── OpencellID/
    │   └── 234_raw.csv
    └── Experiments/
        └── 최종실험(수정)/
            └── Dataset_Build/
                ├── 00_Grid/
                ├── 01_Ofcom/
                ├── 02_Sentinel1/
                ├── 03_Sentinel2/
                ├── 04_WorldCover/
                ├── 05_Population/
                ├── 06_Nightlight/
                ├── 07_OpenCellID/
                └── 08_Final_Datasets/
```

The paths above document the environment used to produce the submitted results. Users do not need to reproduce the same folder names exactly, but they must update the relevant path variables in each notebook to match their own local or cloud directory structure.

## Processed datasets included in this repository

The following analysis-ready files are provided in `processed/`:

```text
processed/
├── dataset19_s1_s2_worldcover_population_nightlight.csv
├── dataset20_final.csv
├── dataset20_final.gpkg
├── dataset21_final.csv
├── dataset22_final.csv
├── dataset23_final.csv
├── dataset24_final.csv
└── dataset25_final.csv
```

These files contain 4,985 grid cells with at least one LTE or 5G NR label. Dataset25 contains the complete set of 35 predictors used in the final modelling experiments.

The processed files support the following notebooks:

| Notebook | Required processed files |
| -------- | ------------------------ |
| `04_exploratory_data_analysis.ipynb` | `dataset20_final.csv` and `dataset20_final.gpkg` |
| `06_compare_feature_sets.ipynb` | Dataset19–25 CSV files |
| `07_analyse_final_models.ipynb` | `dataset25_final.csv` |
| `08_run_advanced_experiments.ipynb` | `dataset25_final.csv` |

These four notebooks can be evaluated without the original Ofcom or OpenCellID files after their input paths have been updated to the location of the supplied processed datasets.

## Complete data-construction workflow

The complete reconstruction route is:

```text
01_build_lte_5g_labels.ipynb
        ↓
02_build_environmental_features.ipynb
        ↓
03_build_opencellid_features.ipynb
        ↓
05_build_progressive_features.ipynb
```

The external requirements are:

- Notebook 01 requires the original Ofcom LTE and 5G NR measurement files.
- Notebook 02 requires the outputs of Notebook 01 and Google Earth Engine access.
- Notebook 03 requires the output of Notebook 02 and the original OpenCellID UK export.
- Notebook 05 requires Dataset20 and the original OpenCellID UK export.

Notebook 04 is an exploratory-analysis notebook and is not a required data-construction step.

Because externally maintained datasets may be updated over time, newly downloaded source files may not be identical to the versions used in the submitted dissertation.

## Data accessed through Google Earth Engine

Notebook 02 accesses the following datasets through Google Earth Engine:

| Dataset | Earth Engine collection ID |
| ------- | -------------------------- |
| Copernicus Sentinel-1 GRD | `COPERNICUS/S1_GRD` |
| Copernicus Sentinel-2 Surface Reflectance Harmonized | `COPERNICUS/S2_SR_HARMONIZED` |
| ESA WorldCover 2021 | `ESA/WorldCover/v200` |
| WorldPop population data | `WorldPop/GP/100m/pop` |
| VIIRS monthly night-time-light data | `NOAA/VIIRS/DNB/MONTHLY_V1/VCMSLCFG` |

Google Earth Engine authentication and access to a Google Cloud project with the Earth Engine API enabled are required for Notebook 02.

The Google Cloud project ID appearing in Notebook 02 corresponds to the environment used for the original analysis. A user reproducing the workflow should replace it with the ID of a Google Cloud project to which they have access and for which the Earth Engine API has been enabled.

The England administrative boundary is downloaded from [GADM version 4.1](https://geodata.ucdavis.edu/gadm/gadm4.1/gpkg/gadm41_GBR.gpkg) by Notebook 01.

## Data limitations

- Ofcom measurements were collected along roads using spectrum assurance vehicles, so their spatial distribution is uneven and does not represent uniform nationwide sampling.
- Ofcom measurement counts were used to evaluate label reliability but were excluded from the model predictors.
- OpenCellID is a crowdsourced database and is not a complete or independently verified inventory of operational base stations.
- OpenCellID record counts should be interpreted as proxies for reported cellular-infrastructure presence rather than verified counts of physical base stations.
- Aggregation to a 1 km × 1 km grid removes variation within individual grid cells.

## Licensing and attribution

The original data remain subject to the terms, licences and attribution requirements of their respective providers.

OpenCellID identifies its data as licensed under the Creative Commons Attribution-ShareAlike 4.0 International licence and requires appropriate attribution. Further information is available from the [OpenCellID download page](https://opencellid.org/downloads/).

The repository's [`LICENSE`](LICENSE) file applies to the original project code unless explicitly stated otherwise. It does not replace or override the licences and usage conditions of Ofcom, OpenCellID, Google Earth Engine datasets, GADM or any other external data provider.

Users should consult each provider's current terms before downloading, using or redistributing raw or derived data.
