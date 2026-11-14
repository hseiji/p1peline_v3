import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent  # p1peline_v3/
load_dotenv(BASE_DIR / ".env")

API_URL = os.getenv("API_URL", "https://api.restcountries.com/countries/v5").rstrip("/")
API_KEY = os.getenv("REST_COUNTRIES_API_KEY")
if not API_KEY:
    raise ValueError("REST_COUNTRIES_API_KEY is not set in the environment variables.")

RAW_PATH = str(BASE_DIR / "data/raw/countries.json")
PARQUET_PATH = str(BASE_DIR / "data/processed/countries")
TABLE_NAME = "countries"

POSTGRES_URL = (
    f"postgresql+psycopg2://"
    f"{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('POSTGRES_HOST', 'db')}:"   # 'db' = service name in docker-compose
    f"{os.getenv('POSTGRES_PORT', '5432')}/"
    f"{os.getenv('POSTGRES_DB')}"
)