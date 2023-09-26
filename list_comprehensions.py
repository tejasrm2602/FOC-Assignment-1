# Task 5: Comprehensions (File: list_comprehensions.py)
#    Use list comprehensions to create a list of SKU_numbers for products with StrengthFactor greater than a given value.


from data_manager import DataManager

# Create a DataManager instance
data_manager = DataManager()

# Load the dataset
products=data_manager.load_data("processed_sales_data.csv")

# Display the data
print("=== Original Data ===")
data_manager.display_data(products)

# Define the given strength value
given_strength = 1624425  # You can change this value as needed

# Use a list comprehension to filter SKU_numbers based on StrengthFactor
product_with_high_strength_sku_number = [product for product in products if product.strength_factor > given_strength]


# Display the data
print("\n======= products with high strength sku_number =======")
data_manager.display_data(product_with_high_strength_sku_number)

sku_numbers_with_high_strength=[product.sku_number for product in product_with_high_strength_sku_number]
# Print the resulting list
print("\n======= sku_numbers with high strength =======")
print(sku_numbers_with_high_strength)
