# Import necessary modules
# Task 6: Save and Load Data (File: save_and_load_data.py)
#    File I/O: Save the filtered and sorted data back to disk in JSON format using the DataManager class.
#    File I/O: Load and save the Product objects to disk using pickle.

import json
import pickle
from data_manager import DataManager

# Create a DataManager instance
data_manager = DataManager()

# Load the dataset
products=data_manager.load_data("processed_sales_data.csv")

# Display the data
print("======= Original Data =======")
data_manager.display_data(products)


# Filter the data based on a condition (e.g., products with SoldFlag = 1)
print("\n======= Filtered Data (SoldFlag = 1 or product.sold_count != 0) =======")
filtered_products=data_manager.filter_data("product.sold_count != 0",products)
data_manager.display_data(filtered_products)

# Sort the data by a specific column (e.g., StrengthFactor
print("\n======= Sorted Data by StrengthFactor of Filtered Data (SoldFlag = 1) =======")
filtered_sorted_products=data_manager.sort_data("strength_factor",filtered_products)
data_manager.display_data(filtered_sorted_products)



# Convert the list of Product objects into a list of dictionaries
product_data = []
for product in filtered_sorted_products:
    product_data.append({
        'sku_number': product.sku_number,
        'sold_count': product.sold_count,
        'strength_factor': product.strength_factor,
        'price_reg': product.price_reg,
        'release_year': product.release_year,
        'item_count': product.item_count,
        'low_user_price': product.low_user_price,
        'low_net_price': product.low_net_price
    })

# Save the list of dictionaries to JSON
with open('filtered_sorted_data.json', 'w') as json_file:
    json.dump(product_data, json_file,indent=4)






# save and load Product objects using pickle

# Save Product objects to disk using pickle
with open('products.pkl', 'wb') as pickle_file:
    pickle.dump(filtered_sorted_products, pickle_file)

# Load Product objects from disk using pickle
with open('products.pkl', 'rb') as pickle_file:
    products_from_pickle_file = pickle.load(pickle_file)

print("\n======= Products Objects from Pickle file =======")
data_manager.display_data(products_from_pickle_file)

