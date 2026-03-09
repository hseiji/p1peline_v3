import logging
from extract import extract_countries
from transform_spark import transform_with_spark
from load import load_to_sqlite
from spark_session import create_spark_session
from data_quality import validate_dataframe


def run_pipeline(output_target):

    spark = create_spark_session()

    try:
        raw_path = extract_countries()

        cleaned_df, region_population = transform_with_spark(spark, raw_path)

        # Run data quality checks
        validate_dataframe(cleaned_df)

        if output_target == "sqlite":
            load_to_sqlite(cleaned_df)

        elif output_target == "parquet":
            cleaned_df.write.mode("overwrite").parquet("data/output")

        logging.info("Pipeline completed successfully")

    finally:
        spark.stop()