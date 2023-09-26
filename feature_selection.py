# Task 1: Feature Selection (File: feature_selection.py)
# 1. Data Science Thinking: Before loading the dataset, identify up to 5 columns that you will remove and 2 columns that are most important.
# Provide a written justification explaining your choices.

# These columns are not needed

# Order
# File_Type
# MarketingType
# ReleaseNumber
# New_Release_Flag
# SoldFlag

# These columns are not needed

# Order : This column appears to be an identifier or a sequence number for the records. It doesn't provide any meaningful information for analysis.
# File_Type: As we are analysing the sales of historical data after getting those Historical rows File_TYpe column is not required
# MarketingType: This column appears to represent the marketing type for the products, this information might not be relevant.
# ReleaseNumber: This column seems to be a numerical identifier. it represents a specific version or release of a product and is not essential for the analysis
# New_Release_Flag: This binary flag indicates whether a product is a new release or not. this information is not crucial to analysis, it can be considered less useful.
# SoldFlag: SoldCount" that represents the number of items sold, then the "SoldFlag" column, which likely contains binary values indicating whether an item was sold

# important columns should considered for Analysis
# SoldCount: This column represents the quantity of products sold in each transaction. It is a crucial metric for any sales analysis because it directly quantifies the number of products sold. we can use this column to calculate various sales-related metrics, such as total sales, average sales per transaction, or sales trends over time.
# StrengthFactor It's possible that it could be a specific metric or calculation used within a particular company or industry to assess the performance or effectiveness of a sales team or strategy.
# PriceReg: The "PriceReg" column represents the regular price of the product. Price is a fundamental factor in sales analysis, as it directly influences revenue and profit margins. we can use this column to calculate the total revenue, profit margins, and pricing strategies' effectiveness. Analyzing price alongside the "SoldCount" can help to understand the relationship between pricing and sales volume.

