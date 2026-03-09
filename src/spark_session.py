# Spark Transformation Module

from pyspark.sql import SparkSession

def create_spark_session():
    spark = (
        SparkSession.builder
        .appName("CountriesDataPipeline")
        .master("local[*]")
        .getOrCreate()
    )

    return spark