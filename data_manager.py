# Task 4: Data Management Class and Data Operations (File: data_manager.py)
#
#    OOP: Create a DataManager class in its own file with methods for the following:
#        Loading the filtered dataset from the new CSV file
#        Displaying data in a formatted table
#        Sorting data based on a column name (e.g., StrengthFactor)
#        Filtering data based on a given condition (e.g., products with SoldFlag = 1)
#
#    Note: This should be done using raw python, not third-party libraries.

# data_manager.py

from product import Product

class DataManager:
    def load_data(self, file_path):
        products = []
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines[1:]:  # Skip the header line
                product = Product(line.strip())
                products.append(product)
        return products

    def display_data(self,products):
        print('SKU_number  SoldCount StrengthFactor PriceReg ReleaseYear ItemCount LowUserPrice LowNetPrice')
        for product in products:
            print(product)


    def sort_data(self, column_name,products):
        sorted_products = sorted(products, key=lambda x: getattr(x, column_name))
        return sorted_products

    def filter_data(self, condition,products):
        filtered_products =  [product for product in products if eval(condition)]
        return filtered_products

