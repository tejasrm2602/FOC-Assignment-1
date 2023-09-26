# Task 4: Data Management Class and Data Operations
# Test the DataManager class by loading the filtered dataset and displaying it in a formatted table in a script named data_manager_test.py.
# It should also demonstrate the sorting and filtering operations on at least one column.

from data_manager import DataManager

# Create a DataManager instance
data_manager = DataManager()

# Load the dataset
products=data_manager.load_data("processed_sales_data.csv")

# Display the data
print("======= Original Data =======")
data_manager.display_data(products)


# Sort the data by a specific column (e.g., StrengthFactor
print("\n======= Sorted Data by StrengthFactor =======")
sorted_products=data_manager.sort_data("strength_factor",products)
data_manager.display_data(sorted_products)

# Filter the data based on a condition (e.g., products with SoldFlag = 1 or product.sold_count != 0)
print("\n======= Filtered Data (SoldFlag = 1 or product.sold_count != 0) =======")
filtered_products=data_manager.filter_data("product.sold_count != 0",products)
data_manager.display_data(filtered_products)
