from pyspark.sql.functions import (
    col, element_at, current_date, sum, count, size, when, explode, trim
)

def transform_with_spark(spark, raw_path):

    # Read raw JSON (the file is a single JSON document, not one record per line)
    raw = spark.read.option("multiLine", True).json(raw_path)

    # The countries live in data.objects, so turn that array into one row per country
    df = raw.select(explode(col("data.objects")).alias("c"))

    # Normalize and clean data
    transformed_df = (
        df.select(
            col("c.codes.alpha_3").alias("country_code"),
            col("c.names.common").alias("country_name"),
            col("c.region").alias("region"),
            # Safe extraction of first capital
            when(size(col("c.capitals")) > 0, element_at(col("c.capitals"), 1))
                .otherwise(None).alias("capital"),
            col("c.population").alias("population"),
        )
        .withColumn("ingestion_date", current_date())
    )

    # Drop invalid rows (null OR empty-string codes)
    transformed_df = transformed_df.filter(
        col("country_code").isNotNull() & (trim(col("country_code")) != "")
    ).cache()  # Cache for performance if used multiple times

    # -------------------------
    # Aggregation - Region
    # -------------------------
    region_population = (
        transformed_df
        .groupBy("region")
        .agg(sum("population").alias("total_population"))
    )

    return transformed_df, region_population