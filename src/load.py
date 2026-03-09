# Load module to load transformed data into SQLite database

import sqlite3
import pandas as pd
import logging
from config import DB_PATH, TABLE_NAME

def load_to_sqlite(spark_df):

    logging.info("Loading data into SQLite")

    pandas_df = spark_df.toPandas()

    conn = sqlite3.connect(DB_PATH)

    pandas_df.to_sql(
        TABLE_NAME,
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    logging.info("Data loaded successfully")