
# Countries Data Pipeline (with Spark & PostgreSQL)

This project is a modular data engineering pipeline that:
- Ingests country data from a REST API
- Processes and cleans the data using Apache Spark
- Validates data quality
- Stores the results in either a PostgreSQL database or as Parquet files (data lake)

It is fully containerized with Docker and orchestrated using Docker Compose for easy setup and reproducibility.


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
PostgreSQL Warehouse
```

---


# Project Structure

```text
p1peline_v3/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── config.py
│   ├── extract.py
│   ├── transform_spark.py
│   ├── load.py
│   ├── data_quality.py
│   ├── spark_session.py
│   └── pipeline.py
├── main.py
├── requirements.txt
├── .env
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# Features

data/processed/countries.parquet/

## Features

- **Data Extraction:** Fetches country data from REST API and saves raw JSON for reproducibility.
- **Spark Transformations:** Cleans and normalizes nested JSON, handles missing values, and aggregates population by region.
- **Data Quality Validation:** Ensures no empty datasets, no null primary keys, and valid population values.
- **Data Lake Storage:** Writes partitioned Parquet files by region to `data/processed/countries`.
- **PostgreSQL Warehouse:** Loads cleaned data into a PostgreSQL database for analytics and querying.
- **Modular Design:** Separate modules for extract, transform, load, and validation.
- **CLI Support:** Choose output target (PostgreSQL or Parquet) via command-line argument.

or

# Quickstart (with Docker Compose)

1. Copy `.env.example` to `.env` and set your API and database credentials if needed.
2. Build and start the pipeline and database:

  ```bash
  docker compose up --build
  ```

3. The pipeline will run and load data into PostgreSQL by default. To output Parquet files instead, edit the `command` in `docker-compose.yml`:

  ```yaml
  command: ["python", "main.py", "--output", "parquet"]
  ```

4. To stop and remove containers and volumes:

  ```bash
  docker compose down -v
  ```

# Running Locally (without Docker)

1. Create a virtual environment and install dependencies:

  ```bash
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```

2. Set environment variables (or use a `.env` file with python-dotenv).

3. Run the pipeline:

  ```bash
  python main.py --output postgres
  # or
  python main.py --output parquet
  ```

# Environment Variables

Set these in your `.env` file:

```
API_URL=https://restcountries.com/v3.1/all?fields=cca3,name,region,capital,population
POSTGRES_USER=pipeline_user
POSTGRES_PASSWORD=yourpassword
POSTGRES_DB=pipeline_db
POSTGRES_PORT=5432
```

# Requirements

- Python 3.10+
- Docker & Docker Compose (for containerized runs)
- Spark, pandas, SQLAlchemy, psycopg2-binary

# License

MIT