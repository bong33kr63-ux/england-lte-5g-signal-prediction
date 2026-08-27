"""Shared file locations for the Google Colab notebooks.

Change PROJECT_ROOT if the repository is stored elsewhere in Google Drive.
"""

from pathlib import Path


PROJECT_ROOT = Path(
    "/content/drive/MyDrive/england-lte-5g-signal-prediction"
)

RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
OFCOM_DATA_DIR = RAW_DATA_DIR / "ofcom"
OPENCELLID_DATA_DIR = RAW_DATA_DIR / "opencellid"

BUILD_DIR = PROJECT_ROOT / "data" / "processed"
RESULTS_DIR = PROJECT_ROOT / "results"
FIGURES_DIR = RESULTS_DIR / "figures"

LTE_FILE = (
    OFCOM_DATA_DIR
    / "4g-lte-2025-mobile-signal-measurement-data.csv"
)
NR_FILE = (
    OFCOM_DATA_DIR
    / "5g-nr-2025-mobile-signal-measurement-data.csv"
)
OPENCELLID_FILE = OPENCELLID_DATA_DIR / "234_raw.csv"
