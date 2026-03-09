API_URL = (
    "https://restcountries.com/v3.1/all"
    "?fields=cca3,name,region,capital,population"
)

RAW_PATH = "data/raw/countries_raw.json"
PARQUET_PATH = "data/processed/countries.parquet"

DB_PATH = "countries.db"
TABLE_NAME = "countries"