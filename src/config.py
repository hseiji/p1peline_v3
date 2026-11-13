import os

API_URL   = os.getenv("API_URL", "https://restcountries.com/v5/all")
API_KEY   = os.getenv("REST_COUNTRIES_API_KEY")
if not API_KEY:
    raise ValueError("REST_COUNTRIES_API_KEY is not set in the environment variables.")
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