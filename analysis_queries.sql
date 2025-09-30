-- Top 10 products by revenue
SELECT Product, SUM(Sales) AS Total_Revenue
FROM retail_sales
GROUP BY Product
ORDER BY Total_Revenue DESC
LIMIT 10;

-- Sales by region
SELECT Region, SUM(Sales) AS Total_Sales
FROM retail_sales
GROUP BY Region
ORDER BY Total_Sales DESC;

-- Customer segmentation (total spending)
SELECT Customer_ID, SUM(Sales) AS Total_Spent
FROM retail_sales
GROUP BY Customer_ID
ORDER BY Total_Spent DESC;

-- Discount vs profit relationship
SELECT Discount, AVG(Profit) AS Avg_Profit
FROM retail_sales
GROUP BY Discount
ORDER BY Discount;
