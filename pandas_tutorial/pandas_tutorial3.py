import pandas as pd
df1 = pd.DataFrame({'symbol': ['AAPL', 'GOOG'], 'price': [150, 2800]})
df2 = pd.DataFrame({'symbol': ['AAPL', 'GOOG'], 'volume': [100, 50]})

print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:") 
print(df2)
# 1. Merge the two DataFrames on the 'symbol' column using an inner join
# Merge the two DataFrames on the 'symbol' column
merged1 = pd.merge(df1, df2, on='symbol',how='inner')
print("\nMerged DataFrame:")
print(merged1)

#2. Merge the two DataFrames on the 'symbol' column using left join(keep all rows from df1)

df1 = pd.DataFrame({'symbol': ['AAPL', 'GOOG','META'], 'price': [150, 280,600]})
df2 = pd.DataFrame({'symbol': ['AAPL', 'GOOG'], 'volume': [100, 50]})

print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:") 
print(df2)
# 1. Merge the two DataFrames on the 'symbol' column using an inner join
# Merge the two DataFrames on the 'symbol' column
merged2 = pd.merge(df1, df2, on='symbol',how='left')
print("\nMerged DataFrame:")
print(merged2)



#3. Merge the two DataFrames on different columns using inner join

df1 = pd.DataFrame({'ticker': ['AAPL', 'GOOG','META'], 'price': [150, 280,600]})
df2 = pd.DataFrame({'symbol': ['AAPL', 'GOOG'], 'volume': [100, 50]})

print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:") 
print(df2)
# 1. Merge the two DataFrames on the 'symbol' column using an inner join
# Merge the two DataFrames on the 'symbol' column
merged2 = pd.merge(df1, df2, left_on='ticker', right_on='symbol', how='inner')
# Merge the two DataFrames on the 'symbol' column
print("\nMerged DataFrame:")
print(merged2)

import numpy as np
#4. add new column based on condition(add a new column 'valuation' based on the condition of price/earnings ratio)
df1 = pd.DataFrame({'symbol': ['AAPL', 'GOOG','META'], 'price': [150, 280,600], 'earnings': [50, 60, 30]})
df1['valuation'] = np.where(df1['price'] / df1['earnings'] > 10, 'overvalued', 'undervalued')