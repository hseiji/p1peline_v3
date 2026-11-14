import logging
from src.config import PARQUET_PATH, REGION_POP_PATH
from src.extract import extract_countries
from src.transform_spark import transform_with_spark
from src.load import load_to_postgres
from src.spark_session import create_spark_session
from src.data_quality import validate_dataframe

VALID_TARGETS = ("postgres", "parquet")

def run_pipeline(output_target):

    if output_target not in VALID_TARGETS:
        raise ValueError(f"Unknown output target '{output_target}', expected one of {VALID_TARGETS}")

    spark = create_spark_session()

    try:
        raw_path = extract_countries()

        cleaned_df, region_population = transform_with_spark(spark, raw_path)

        # Run data quality checks
        validate_dataframe(cleaned_df)

        print(f"Total countries: {cleaned_df.count()}")
        print("\nPopulation by Region")
        region_population.show()

        if output_target == "postgres":
            load_to_postgres(cleaned_df)

        elif output_target == "parquet":
            cleaned_df.write.mode("overwrite").partitionBy("region").parquet(PARQUET_PATH)
            region_population.write.mode("overwrite").parquet(REGION_POP_PATH)

        logging.info("Pipeline completed successfully")

    finally:
        spark.stop()