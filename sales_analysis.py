import pandas as pd
# Mock dataset representing multi-region transactions
transaction_data = {
   'Region': ['North', 'South', 'East', 'West', 'North', 'East'],
   'Category': ['Electronics', 'Clothing', 'Electronics', 'Home', 'Clothing', 'Home'],
   'Sales_Revenue':,
   'Operating_Cost': [9000, 4500, 13000, 8500, 5000, 7000]
}
print("=== Generating Regional Sales Performance Report ===")
df = pd.DataFrame(transaction_data)
# Calculate financial performance benchmarks
df['Net_Profit'] = df['Sales_Revenue'] - df['Operating_Cost']
df['Profit_Margin_%'] = round((df['Net_Profit'] / df['Sales_Revenue']) * 100, 1)
# Group metrics by geographic region for executive review
regional_summary = df.groupby('Region')[['Sales_Revenue', 'Net_Profit']].sum().reset_index()
print("\n📊 Regional Performance Matrices:")
print(regional_summary.to_string(index=False))
