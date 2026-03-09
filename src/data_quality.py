# This checks:
# dataset is not empty
# primary key exists
# no invalid population values


import logging


def validate_dataframe(df):

    logging.info("Running data quality checks")

    row_count = df.count()
    if row_count == 0:
        raise ValueError("Data quality failure: DataFrame is empty")

    null_codes = df.filter("country_code IS NULL").count()
    if null_codes > 0:
        raise ValueError("Data quality failure: Null country_code values found")

    negative_population = df.filter("population < 0").count()
    if negative_population > 0:
        raise ValueError("Data quality failure: Negative population values found")

    logging.info("Data quality checks passed")