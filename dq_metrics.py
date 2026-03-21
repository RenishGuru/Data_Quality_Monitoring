# Databricks notebook source
# CONFIG
dq_results_table = "dq_results"

from pyspark.sql.functions import count, when, col

df = spark.table(dq_results_table)

metrics_df = df.groupBy("rule_name").agg(
    count("*").alias("total"),
    count(when(col("status") == True, True)).alias("passed"),
    count(when(col("status") == False, True)).alias("failed")
)

display(metrics_df)