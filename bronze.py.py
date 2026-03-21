# Databricks notebook source
raw_data_path = "/Volumes/workspace/default/dqm/sales.csv"
bronze_table = "bronze_sales_dqm"

from pyspark.sql.functions import current_timestamp

df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load(raw_data_path)

df = df.withColumn("ingestion_time", current_timestamp())

df.write.mode("overwrite").saveAsTable(bronze_table)

display(df)