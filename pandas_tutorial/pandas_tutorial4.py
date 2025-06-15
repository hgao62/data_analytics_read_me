# Chapter 12-4 This code demonstrates how to use the `apply` method in pandas to apply a function to each row or column of a DataFrame.

import pandas as pd
import numpy as np

# Sample data
data = {"A": [1, 2, 3, 4], "B": [5, 6, 7, 8]}
df = pd.DataFrame(data)


# Define a simple function
def square(x):
    return x**2

# 1. apply function to a series (column)
df["A_squared"] = df["A"].apply(square)  # default axis=0 means column-wise operation

def sum_columns(row):
    return row["A"] + row["B"]
# 2. apply function to a DataFrame (row-wise)
df["sum"] = df.apply(
    sum_columns, axis=1
)  # axis=1 means row-wise operation

#2.1 apply function to DataFrame (column-wise)
data = {
    "Math": [85, 90, 78, 92, np.nan],
    "English": [88, 79, 85, 91, 76],
    "Science": [90, 94, np.nan, 88, 84],
    "History": [75, 85, 89, 90, 73]
}

df = pd.DataFrame(data)

def get_diff(col:pd.Series):
    return col.max() - col.min()

df.apply(get_diff, axis=0)

# 3 Aggregation with groupby

data = {"Category": ["A", "A", "B", "B", "C", "C"], "Value": [10, 20, 30, 40, 50, 60]}
df = pd.DataFrame(data)

# Group by 'Category' and calculate the mean of 'Value' for each group
group_mean = df.groupby("Category")["Value"].mean().reset_index(name="frequency")
group_max = df.groupby("Category")["Value"].max().reset_index(name="Max value")


# 12.5 Aggregation with groupby and multiple columns
# Sample data
data = {
    "Store": ["A", "A", "B", "B", "C", "C"],
    "Sales": [100, 150, 200, 250, 300, 350],
    "Quantity": [1, 2, 3, 4, 5, 6],
}

df = pd.DataFrame(data)

# Group by 'Store' and aggregate using dictionary syntax
grouped = df.groupby("Store").agg(
    {
        "Sales": "sum",  # Total Sales
        "Quantity": "sum",  # Total Quantity
    }
)

# Display the aggregated DataFrame
print("\nAggregated DataFrame:")
print(grouped)

grouped_reset = (
    df.groupby("Store")
    .agg(
        {
            "Sales": "sum",  # Total Sales
            "Quantity": "sum",  # Total Quantity
        }
    )
    .reset_index()
)

grouped_reset.columns = ["Store", "Total_Sales", "Total_Quantity"]


# 12.5 Aggregation with groupby and multiple functions on same column
grouped = (
    df.groupby("Store")
    .agg(
        {
            "Sales": ["sum", "mean"],  # Total and Average Sales
            "Quantity": ["sum", "mean"],  # Total and Average Quantity
        }
    )
    .reset_index()
)

grouped.columns = ["Store","Total_Sales","Average_Sales","Total_Quantity","Average_Quantity"]
