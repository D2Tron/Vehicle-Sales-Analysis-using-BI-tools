# Vehicle Sales Analysis Project

## Overview
This project analyzes vehicle sales data using a PostgreSQL database and Power BI for visualization. It includes the original dataset, a cleaned version, and a SQL dump containing the schema and data.

## Files Included
- **Dataset**: [car_prices.csv](/car_prices.csv)
- **Cleaned Dataset**: [car_prices_clean.csv](/car_prices_clean.csv)  
  Use the provided Python script (`data_cleaning.py`) to generate this file.
- **SQL Dump**: [SalesAnalysisDB_backup.sql](SalesAnalysisDB_backup.sql)  
  This file contains the schema and data. You can import it into PostgreSQL to set up your database.

## Setup Instructions

### 1. Create PostgreSQL Database
- Open your PostgreSQL client (e.g., pgAdmin).
- Create a new database named `SalesAnalysisDB`.

### 2. Import SQL Dump
- Use the following command to import the SQL dump:
  ```bash
  psql -U your_username -d SalesAnalysisDB -f path/to/sql_dump.sql
Replace `your_username` with your PostgreSQL username and adjust the path to where the SQL dump file is located.

### 3. Access the Cleaned Dataset
- The cleaned dataset can be generated using the provided Python script:
  ```bash
  python data_cleaning.py
### 4. SQL Queries
- The SQL queries used in this project are not included at this time but will be provided in a future update. These queries can be run to further analyze the vehicle sales data once added.

### 5. Visualization
After saving the query results as CSV files, you can connect these files to Power BI to create visualizations based on the vehicle sales data.

## Notes
- Ensure that you have PostgreSQL installed and running on your machine.
- The cleaned dataset script may require additional libraries. Make sure to install any dependencies using pip, if necessary.

Feel free to explore the dataset and modify the SQL queries as needed!
