Countries Data Pipeline

Pipeline Architecture:

REST API
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

Technologies used:

- Python

- Apache Spark

- REST APIs

- Parquet data lake

- SQLite warehouse

- Data quality validation