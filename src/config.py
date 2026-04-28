import os

API_URL   = os.getenv("API_URL", "https://restcountries.com/v3.1/all")
RAW_PATH  = "data/raw/countries.json"
PARQUET_PATH = "data/processed/countries"
TABLE_NAME = "countries"

POSTGRES_URL = (
    f"postgresql+psycopg2://"
    f"{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"db:"                          # matches the service name in docker-compose
    f"{os.getenv('POSTGRES_PORT', '5432')}/"
    f"{os.getenv('POSTGRES_DB')}"
)