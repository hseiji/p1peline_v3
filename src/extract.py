# Extract module

import requests
import json
import logging
import os
from src.config import API_URL, RAW_PATH, API_KEY

logger = logging.getLogger(__name__)
PAGE_SIZE = 100  # API maximum

def extract_countries():
    logging.info("Extracting data from API")
    url = API_URL.rstrip("/")
    headers = {"Authorization": f"Bearer {API_KEY}"}
    countries, offset = [], 0

    while True:
        response = requests.get(
            url, 
            headers=headers,
            params={"limit": PAGE_SIZE, "offset": offset},  # API maximum (if the API supports pagination)
            timeout=30
        )
        response.raise_for_status()
        payload = response.json()

        if payload.get("success") is False or not isinstance(payload.get("data"), dict):
                    raise RuntimeError(f"API returned an error: {payload.get('errors')}")

        page = payload["data"]["objects"]
        countries.extend(page)

        if len(page) < PAGE_SIZE:  # last page
            break
        offset += PAGE_SIZE

    os.makedirs(os.path.dirname(RAW_PATH), exist_ok=True)
    with open(RAW_PATH, "w") as f:
        json.dump({"data": {"objects": countries}}, f)

    logger.info("Raw data saved (%d countries)", len(countries))

    return RAW_PATH