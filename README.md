# Countries Data Pipeline

A modular **data engineering pipeline** that ingests country data from a REST API, processes it using Spark, validates data quality, and stores it in both a **data lake (Parquet)** and a **SQLite warehouse**.

---

# Pipeline Architecture
```text
REST Countries API
↓
Extract (Python requests)
↓
Raw Data Layer (JSON)
↓
Spark Transformations
↓
Data Quality Validation
↓
Partitioned Parquet Data Lake
↓
Analytics Aggregations
↓
SQLite Warehouse
```

---

# Project Structure
```text
countries-data-pipeline/
│
├── data/
│   ├── raw/
│   │   └── countries_raw.json
│   │
│   └── processed/
│       ├── countries.parquet/
│       └── region_population/
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── extract.py
│   ├── transform_spark.py
│   ├── load.py
│   ├── data_quality.py
│   ├── spark_session.py
│   └── pipeline.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Features

## Data Extraction
- Fetches country data from REST API
- Saves raw JSON data for reproducibility

## Spark Transformations
- Uses Apache Spark for scalable processing
- Cleans and normalizes nested JSON
- Handles missing/empty values safely (e.g., capital)

## Data Quality Validation
- Ensures:
  - No empty datasets
  - No null primary keys
  - No invalid population values

## Data Lake Storage
- Writes **partitioned Parquet files** by region:



data/processed/countries.parquet/
region=Europe/
region=Asia/
region=Africa/

## Analytics Layer
- Aggregates population by region using Spark
- Stores aggregated dataset separately

## Data Warehouse
- Loads cleaned data into SQLite for querying

## Modular Design
- Separate modules for extract, transform, load, validation
- Easy to extend and maintain

## CLI Support

Run pipeline with different outputs:

```bash
python main.py --output sqlite
```

## How to Run

### 1. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the pipeline
```bash
python main.py --output sqlite
```
or

```bash
python main.py --output parquet
```