import pandas as pd
import re

def convert_to_sql_timestamp(date_str):
    if pd.isna(date_str):
        return None  # Return None for null values
    
    # Extract date, time, and timezone using regex
    match = re.match(r'(\w{3} \w{3} \d{2} \d{4} \d{2}:\d{2}:\d{2}).*\((\w+)\)', date_str)
    if match:
        date_time, timezone = match.groups()
        # Convert to SQL timestamp format
        sql_date = pd.to_datetime(date_time).strftime('%Y-%m-%d %H:%M:%S')
        return f"{sql_date} {timezone}"
    return date_str  # Return original string if no match

# Specify column types
column_types = {
    'year': pd.Int64Dtype(),
    'condition': pd.Int64Dtype(), 
    'odometer': pd.Int64Dtype(),
    'mmr': pd.Int64Dtype(),
    'sellingprice': pd.Int64Dtype(),  # You can adjust these types according to the actual data
    # Add other columns as needed
}

# Load the data
data = pd.read_csv('car_prices.csv', dtype=column_types)

# Apply the conversion function to the 'saledate' column
data['saledate'] = data['saledate'].apply(convert_to_sql_timestamp)

# Save cleaned data to a new CSV
data.to_csv('car_prices_clean.csv', index=False)

# Print a sample to verify
print(data['saledate'].head())

# Print the number of null values after conversion
print(f"Number of null values in 'saledate' column: {data['saledate'].isnull().sum()}")