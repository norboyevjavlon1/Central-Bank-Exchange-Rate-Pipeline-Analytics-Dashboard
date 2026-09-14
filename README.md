# Central-Bank-Exchange-Rate-Pipeline-Analytics-Dashboard
# Automated Central Bank Exchange Rate Pipeline & Analytics Dashboard

## 📌 Project Overview
This project is an end-to-end data engineering and business intelligence solution. It automates the extraction of daily currency exchange rates from the Central Bank, loads the transformed data into a Microsoft SQL Server database, and provides interactive visualizations through a Power BI dashboard. 

The pipeline runs completely hands-free on a daily schedule, ensuring the BI reports always reflect the most up-to-date economic data.

## 🛠️ Tech Stack
* **Data Extraction:** Python (Requests, Pandas)
* **Database & Storage:** Microsoft SQL Server (SSMS)
* **Automation:** Windows Task Scheduler
* **Data Visualization & Analytics:** Power BI, DAX

## ⚙️ Architecture & Workflow
1. **Extract:** A Python script connects to the Central Bank's API/website to fetch daily foreign exchange rates.
2. **Transform:** Data is cleaned, formatted, and structured within Python using Pandas to ensure database compatibility.
3. **Load:** The script executes SQL `INSERT` statements to load the processed records into a relational SQL Server database.
4. **Automate:** Windows Task Scheduler triggers the Python executable daily at a specific time.
5. **Visualize:** Power BI connects directly to the SQL Server database, utilizing custom DAX measures to track currency volatility, historical trends, and percentage changes.

## 📊 Dashboard Highlights
<img width="1296" height="734" alt="image" src="https://github.com/user-attachments/assets/2ba4ed36-f1fc-4646-8797-7b9c6a0bcdaf" />
<img width="843" height="584" alt="image" src="https://github.com/user-attachments/assets/5eb99ae5-84d1-473e-9ec2-63b6d5a1eae9" />


* **Trend Analysis:** Tracks the historical performance of major currencies.
* **Volatility Metrics:** Calculates daily variance and percentage changes using DAX.
* **Dynamic Filtering:** Allows users to filter by specific date ranges and currency types.

