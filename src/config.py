import os

# Base directory of the project
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Define data paths
DATA_PATH_RAW = os.path.join(BASE_DIR, "data", "raw")
DATA_PATH_INTERIM = os.path.join(BASE_DIR, "data", "interim")
DATA_PATH_PROCESSED = os.path.join(BASE_DIR, "data", "processed")
FIGURES_PATH = os.path.join(BASE_DIR, "figures")

# Create directories if they don't exist
os.makedirs(DATA_PATH_RAW, exist_ok=True)
os.makedirs(DATA_PATH_INTERIM, exist_ok=True)
os.makedirs(DATA_PATH_PROCESSED, exist_ok=True)
os.makedirs(FIGURES_PATH, exist_ok=True)
