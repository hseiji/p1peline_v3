import os
API_URL = os.getenv("API_URL")

RAW_PATH = "data/raw/countries_raw.json"
PARQUET_PATH = "data/processed/countries.parquet"

DB_PATH = "countries.db"
TABLE_NAME = "countries"