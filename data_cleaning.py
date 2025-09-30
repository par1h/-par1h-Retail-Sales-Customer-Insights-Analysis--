import pandas as pd

# Load data
df = pd.read_csv('../data/retail_sales.csv')

# Preview data
print("Initial shape:", df.shape)
print(df.head())

# Handle missing values
df = df.dropna(subset=['Product', 'Customer_ID', 'Region', 'Sales', 'Profit'])

# Remove duplicates
df = df.drop_duplicates()

# Convert columns
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Year'] = df['Order_Date'].dt.year

# Save cleaned data
df.to_csv('../data/retail_sales_cleaned.csv', index=False)
print("Cleaned data saved!")