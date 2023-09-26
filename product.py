# Task 3: Object Class for Product (File: product.py)

#    OOP: Create a Python class named Product in its own file. This class should have attributes relevant to the dataset (e.g., SKU_number, SoldFlag, StrengthFactor, etc.).
#    Add a constructor which takes a line of CSV data as input and parses it to initialize the attributes.

class Product:
    def __init__(self, csv_line):
        # Split the CSV line into individual values
        values = csv_line.strip().split(',')

        # SKU_number	SoldFlag	SoldCount   StrengthFactor	PriceReg	ReleaseYear	ItemCount	LowUserPrice	LowNetPrice

        # Assign values to attributes (you can adjust the indices based on your dataset)
        self.sku_number = int(values[0])
        self.sold_count = int(values[1])
        self.strength_factor = int(values[2])
        self.price_reg = float(values[3])
        self.release_year = int(values[4])
        self.item_count = int(values[5])
        self.low_user_price = float(values[6])
        self.low_net_price = float(values[7])

    def __str__(self):
        # Format the attributes in a table-like structure
        formatted = (
            f"{self.sku_number:<11} {self.sold_count:<10} {self.strength_factor:<15} {self.price_reg:<8.2f} "
            f"{self.release_year:<10} {self.item_count:<10} {self.low_user_price:<10.2f} {self.low_net_price:<10.2f}"
        )
        return formatted

