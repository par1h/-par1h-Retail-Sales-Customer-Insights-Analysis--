import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('../data/retail_sales_cleaned.csv')

# 1. Top 10 Products by Profit
top_products = df.groupby('Product')['Profit'].sum().sort_values(ascending=False).head(10)
top_products.plot(kind='bar', figsize=(10, 5), title='Top 10 Products by Profit')
plt.tight_layout()
plt.savefig('../data/top_products_profit.png')

# 2. Sales by Region
region_sales = df.groupby('Region')['Sales'].sum()
region_sales.plot(kind='pie', autopct='%1.1f%%', figsize=(6, 6), title='Sales Distribution by Region')
plt.ylabel('')
plt.tight_layout()
plt.savefig('../data/sales_by_region.png')

# 3. Discount vs Profit
plt.figure(figsize=(7, 5))
plt.scatter(df['Discount'], df['Profit'], alpha=0.5)
plt.title('Discount vs Profit')
plt.xlabel('Discount')
plt.ylabel('Profit')
plt.tight_layout()
plt.savefig('../data/discount_vs_profit.png')

print("All visualizations saved!")