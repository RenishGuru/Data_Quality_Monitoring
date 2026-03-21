# Databricks notebook source
# CONFIG
silver_table = "silver_sales_dqm"
gold_table = "gold_sales_dqm"

from pyspark.sql.functions import sum

df = spark.table(silver_table)

gold_df = df.groupBy("order_date").agg(
    sum("amount").alias("total_sales")
)

gold_df.write.mode("overwrite").saveAsTable(gold_table)

display(gold_df)