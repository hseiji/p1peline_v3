import logging
from src.extract import extract_countries
from src.transform_spark import transform_with_spark
from src.load import load_to_postgres
from src.spark_session import create_spark_session
from src.data_quality import validate_dataframe


def run_pipeline(output_target):

    spark = create_spark_session()

    try:
        raw_path = extract_countries()

        cleaned_df, region_population = transform_with_spark(spark, raw_path)

        # Run data quality checks
        validate_dataframe(cleaned_df)

        if output_target == "postgres":
            load_to_postgres(cleaned_df)

        elif output_target == "parquet":
            cleaned_df.write.mode("overwrite").parquet("data/output")

        logging.info("Pipeline completed successfully")

    finally:
        spark.stop()