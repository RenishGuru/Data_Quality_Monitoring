# Databricks notebook source
# CONFIG
bronze_table = "bronze_sales_dqm"
silver_table = "silver_sales_dqm"

from pyspark.sql.functions import col

df = spark.table(bronze_table)

clean_df = df \
    .filter(col("customer_name").isNotNull()) \
    .filter(col("amount").isNotNull()) \
    .filter(col("amount") > 0)

clean_df.write.mode("overwrite").saveAsTable(silver_table)

display(clean_df)