# Data

The raw files are not included in this repository. The Ofcom files are large, and the OpenCellID download is subject to the provider's current access and attribution requirements.

## Files to download

| Data | Filename used by the notebooks | Download page |
|---|---|---|
| Ofcom 4G LTE measurements for 2025 | `4g-lte-2025-mobile-signal-measurement-data.csv` | [Ofcom signal measurement data](https://www.ofcom.org.uk/phones-and-broadband/coverage-and-speeds/mobile-signal-strength-measurement-data?language=en) |
| Ofcom 5G NR measurements for 2025 | `5g-nr-2025-mobile-signal-measurement-data.csv` | [Ofcom signal measurement data](https://www.ofcom.org.uk/phones-and-broadband/coverage-and-speeds/mobile-signal-strength-measurement-data?language=en) |
| OpenCellID UK export (MCC 234) | `234_raw.csv` | [OpenCellID downloads](https://opencellid.org/downloads/) |

Downloading a country export from OpenCellID may require an account and API token. Please check the current [server usage policy](https://wiki.opencellid.org/wiki/Server_usage_policy) before downloading or redistributing the data.

## Google Drive layout

Place the downloaded files as shown below:

```text
MyDrive/
└── england-lte-5g-signal-prediction/
    └── data/
        └── raw/
            ├── ofcom/
            │   ├── 4g-lte-2025-mobile-signal-measurement-data.csv
            │   └── 5g-nr-2025-mobile-signal-measurement-data.csv
            └── opencellid/
                └── 234_raw.csv
```

## Data accessed through Google Earth Engine

Notebook 2 accesses these sources directly:

- Copernicus Sentinel-1 GRD
- Copernicus Sentinel-2 Surface Reflectance Harmonized
- ESA WorldCover 2021
- WorldPop population data
- VIIRS monthly night-time-light data

The England boundary is downloaded from GADM 4.1 by Notebook 1. Google Earth Engine authentication and an enabled Cloud project are required for Notebook 2.

## Notes

- Ofcom measurements were collected along roads, so their spatial distribution is uneven.
- OpenCellID is crowdsourced and is not a complete list of operational base stations.
- The notebooks create the intermediate and final datasets in numerical order.
- Ofcom measurement counts are used to examine label reliability. They are not included as model predictors.

Please refer to each provider's current terms before redistributing raw or derived data.
