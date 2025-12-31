import sqlite3
import pandas as pd
import os

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_PATH = os.path.join(BASE_DIR, "Data", "SQLite.db")
REPORT_PATH = os.path.join(BASE_DIR, "Reports", "daily_operations_report.xlsx")

FAILURE_THRESHOLD = 5  # percentage

# Connect to database
conn = sqlite3.connect(DB_PATH)

# Load SQL queries
with open(os.path.join(BASE_DIR, "Sql", "daily_metrics.sql"), "r") as f:
    daily_metrics_query = f.read()

with open(os.path.join(BASE_DIR, "Sql", "orders_without_payment.sql")) as f:
    no_payment_query = f.read()

with open(os.path.join(BASE_DIR, "Sql", "failed_payments.sql")) as f:
    failed_payment_query = f.read()

with open(os.path.join(BASE_DIR, "Sql", "daily_failure_rate.sql"), "r") as f:
    failure_rate_query = f.read()

# Execute queries
daily_metrics_df = pd.read_sql_query(daily_metrics_query, conn)
no_payment_df = pd.read_sql_query(no_payment_query, conn)
failed_payment_df = pd.read_sql_query(failed_payment_query, conn)
failure_rate_df = pd.read_sql_query(failure_rate_query, conn)

# Apply alert logic
failure_rate_df["ALERT"] = failure_rate_df["failure_percentage"].apply(
    lambda x: "YES" if x > FAILURE_THRESHOLD else "NO"
)

df_alerts = failure_rate_df[failure_rate_df["ALERT"] == "YES"]

# Write to Excel
with pd.ExcelWriter(REPORT_PATH, engine="openpyxl") as writer:
    daily_metrics_df.to_excel(writer, sheet_name="Daily Metrics", index=False)
    no_payment_df.to_excel(writer, sheet_name="No Payment Orders", index=False)
    failed_payment_df.to_excel(writer, sheet_name="Failed Payments", index=False)
    failure_rate_df.to_excel(writer, sheet_name="Daily Failure Rate", index=False)
    df_alerts.to_excel(writer, sheet_name="⚠ Alerts", index=False)


conn.close()

print("✅ Daily operations report generated successfully.")
