"""Shared file locations for the project notebooks."""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent

# Replace this with the ID of a Google Cloud project that has
# the Earth Engine API enabled.
EARTH_ENGINE_PROJECT = "your-google-cloud-project-id"

RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
OFCOM_DATA_DIR = RAW_DATA_DIR / "ofcom"
OPENCELLID_DATA_DIR = RAW_DATA_DIR / "opencellid"

BUILD_DIR = PROJECT_ROOT / "work"
PROCESSED_DATA_DIR = PROJECT_ROOT / "processed"
if not PROCESSED_DATA_DIR.exists():
    alternative_processed_dir = PROJECT_ROOT / "data" / "processed"
    if alternative_processed_dir.exists():
        PROCESSED_DATA_DIR = alternative_processed_dir
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
