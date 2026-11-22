# Databricks notebook source
# CONFIG
bronze_table = "bronze_sales_dqm"
dq_results_table = "dq_results_dqm"

dq_rules = [
    ("customer_not_null", "customer_name IS NOT NULL"),
    ("amount_not_null", "amount IS NOT NULL"),
    ("amount_positive", "amount > 0")
]

from pyspark.sql.functions import expr, current_timestamp

df = spark.table(bronze_table)

dq_results = []

for rule_name, rule_condition in dq_rules:
    temp_df = df \
        .withColumn("rule_name", expr(f"'{rule_name}'")) \
        .withColumn("rule_condition", expr(f"'{rule_condition}'")) \
        .withColumn("status", expr(rule_condition)) \
        .withColumn("run_timestamp", current_timestamp())
    
    dq_results.append(temp_df)

final_df = dq_results[0]

for d in dq_results[1:]:
    final_df = final_df.union(d)

final_df.write.mode("overwrite").saveAsTable(dq_results_table)

display(final_df)
