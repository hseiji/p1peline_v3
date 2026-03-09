# Extract module

import requests
import json
import logging
from config import API_URL, RAW_PATH

def extract_countries():
    logging.info("Extracting data from API")

    response = requests.get(API_URL, timeout=30)
    response.raise_for_status()

    data = response.json()

    with open(RAW_PATH, "w") as f:
        json.dump(data, f)

    logging.info("Raw data saved")

    return RAW_PATH