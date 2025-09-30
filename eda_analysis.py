import pandas as pd
import numpy as np

# Load cleaned data
df = pd.read_csv('../data/retail_sales_cleaned.csv')

# Summary stats
print(df.describe())

# Top products by revenue
top_products = df.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Products by Sales:\n", top_products)

# Regional revenue
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
print("\nSales by Region:\n", region_sales)

# Discount-profit correlation
corr = df['Discount'].corr(df['Profit'])
print("\nCorrelation between Discount and Profit:", round(corr, 2))

# Save summary
summary = {
    'top_products': top_products.to_dict(),
    'region_sales': region_sales.to_dict(),
    'discount_profit_corr': corr
}

pd.Series(summary).to_json('../data/eda_summary.json')
