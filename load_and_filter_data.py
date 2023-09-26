# Task 2: Load Data and Save Filtered Dataset (File: load_and_filter_data.py)
#    File I/O: Load the raw sales analysis dataset from a CSV file. Remove the columns you identified in Task 1 and write the new dataset to a new CSV file.

import pandas as pd

# Define the file paths
input_file = 'sales_data.csv'
output_file = 'processed_sales_data.csv'

#Before Processing
# Order	File_Type	SKU_number	SoldFlag	SoldCount	MarketingType	ReleaseNumber	New_Release_Flag	StrengthFactor	PriceReg	ReleaseYear	ItemCount	LowUserPrice	LowNetPrice

#After Processing
# SKU_number    SoldCount   StrengthFactor	PriceReg	ReleaseYear	ItemCount	LowUserPrice	LowNetPrice

# List of columns to remove
columns_to_remove = ['Order', 'File_Type', 'MarketingType', 'ReleaseNumber', 'New_Release_Flag' ,'SoldFlag']


# Load the raw dataset from the CSV file
try:
    # Attempt to read the CSV file into a DataFrame
    raw_data = pd.read_csv(input_file)

except FileNotFoundError:
    print(f"Error: The file '{input_file}' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Drop the identified columns
historical_data = raw_data[raw_data['File_Type'] == 'Historical']

processed_data = historical_data.drop(columns=columns_to_remove)


integer_column_names = ['SKU_number', 'SoldCount', 'StrengthFactor', 'ReleaseYear', 'ItemCount']
processed_data[integer_column_names] = processed_data[integer_column_names].astype(int)

# Write the processed dataset to a new CSV file
processed_data.to_csv(output_file, index=False)

# Display the first few rows of the processed dataset
print(processed_data.head())
