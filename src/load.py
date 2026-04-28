# Load module to load transformed data into SQLite database

import pandas as pd
import logging
from sqlalchemy import create_engine
from src.config import TABLE_NAME, POSTGRES_URL

def load_to_postgres(spark_df):

    logging.info("Loading data into PostgreSQL")

    # ok for small datasets, for larger ones we would want to batch this or use a more efficient method
    pandas_df = spark_df.toPandas()

    engine = create_engine(POSTGRES_URL)

    # todo: option to incrementally load data instead of replacing the table (will do this for next project with better API)
    pandas_df.to_sql(
        TABLE_NAME,
        engine,
        if_exists="replace",
        index=False
    )



    logging.info("Data loaded successfully")