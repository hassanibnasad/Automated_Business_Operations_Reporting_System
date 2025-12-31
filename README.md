# Automated Business Operations & Reporting System

## 📌 Overview
This project simulates a real-world operations reporting system used by Operations, MIS, and Application Support teams.

It automates:
- Daily operational metrics
- Payment failure analysis
- Anomaly detection
- Alert generation for high failure days

## 🛠 Tech Stack
- Python
- SQLite
- SQL
- Pandas
- OpenPyXL

## 📊 Key Features
- Multi-sheet Excel reporting
- SQL-driven business metrics
- Automated alert logic for payment failures
- Modular SQL query structure
- Production-style folder organization

## 🚨 Alert Logic
- Flags days where payment failure rate exceeds a defined threshold (e.g., >5%)
- Generates a dedicated Alerts sheet for quick action

## 📁 Project Structure
- Data/        → SQLite database
- Scripts/     → Python automation scripts
- Sql/         → Modular SQL queries
- Reports/     → Generated Excel reports

## ▶️ How to Run
```bash
python Scripts/generate_report.py
