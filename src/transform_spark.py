from pyspark.sql.functions import col, element_at, current_date, sum
from config import PARQUET_PATH


def transform_with_spark(spark, raw_path):

    # Read raw JSON
    df = spark.read.json(raw_path)

    # Normalize and clean data
    transformed_df = (
        df.select(
            col("cca3").alias("country_code"),
            col("name.common").alias("country_name"),
            col("region"),
            element_at(col("capital"), 1).alias("capital"),
            col("population")
        )
        .withColumn("ingestion_date", current_date())
    )

    # Drop invalid rows
    transformed_df = transformed_df.dropna(subset=["country_code"])

    # -------------------------
    # Write cleaned dataset
    # -------------------------
    transformed_df.write \
        .mode("overwrite") \
        .partitionBy("region") \
        .parquet(PARQUET_PATH)

    # -------------------------
    # Aggregation example
    # -------------------------
    region_population = (
        transformed_df
        .groupBy("region")
        .agg(sum("population").alias("total_population"))
    )

    print("\nPopulation by Region")
    region_population.show()

    region_population.write \
        .mode("overwrite") \
        .parquet("data/processed/region_population")

    return transformed_df, region_population