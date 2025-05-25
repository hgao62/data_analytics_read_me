# This code demonstrates how to use the `apply` method in pandas to apply a function to each row or column of a DataFrame.

import pandas as pd

# Sample data
data = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)

# Define a simple function
def square(x):
    return x ** 2

#1. apply function to a series (column)
df['A_squared'] = df['A'].apply(square) #default axis=0 means column-wise operation

print(df)

#2. apply function to a DataFrame (row-wise)
df['sum'] = df.apply(lambda row: row['A'] + row['B'], axis=1)# axis=1 means row-wise operation