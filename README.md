🚀 Overview

This project demonstrates a Data Quality Monitoring (DQM) pipeline built using Databricks Community Edition without relying on cloud integrations. It follows the Medallion Architecture (Bronze → Silver → Gold) to ingest, clean, validate, and analyze data.

The dataset consists of 500 synthetic order records with intentional data quality issues such as:

Missing values
Negative amounts
Inconsistent data entries

This project is designed to be resume-ready and showcases practical data engineering and data governance concepts.

🏗️ Architecture
🔹 Bronze Layer (Raw Data)
Ingest raw CSV data (orders_500.csv)
No transformations applied
Data stored as-is for traceability
🔹 Silver Layer (Cleaned Data)
Data cleansing and standardization
Handle null values
Remove or flag invalid records (e.g., negative amounts)
Schema enforcement
🔹 Gold Layer (Quality Metrics & Insights)
Data Quality Checks (DQC)
Aggregated metrics:
Null count
Negative value count
Total records
Valid records
Business-ready dataset
