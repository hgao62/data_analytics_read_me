# Chapter 12-1: Pandas Basics
# This script demonstrates basic operations in pandas, including creating a DataFrame
# and performing various data manipulations such as selecting columns, filtering rows,
# sorting values, adding new columns, grouping and aggregating data, and saving to CSV.

import pandas as pd


# 1. Series
# what is a series?
# A Series is a one-dimensional labeled array capable of holding any data type.
# Creating a Series
s = pd.Series([10, 20, 30], index=["a", "b", "c"])

s = pd.Series([10, 20, 30])

# 2.Creating a DataFrame
# A DataFrame is a two-dimensional labeled data structure with columns of potentially different types.
# It is similar to a spreadsheet or SQL table, or a dictionary of Series objects.
df = pd.DataFrame({"Price": [100, 200, 300], "Volume": [10, 5, 20]})


# Sample data
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Age": [24, 30, 22, 35, 28, 17],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix","Phoenix"],
    "Salary": [70000, 80000, 60000, 90000, 75000,5000],
}

# 2.Create DataFrame
df = pd.DataFrame(data)


# 3. Index：# The index is a label that uniquely identifies each row in the DataFrame.

data = {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35]}
df = pd.DataFrame(data)

# Default index is 0,1,2
print(df)
# 3.1 set custom index
df.set_index("Name", inplace=True)
print(df)
# 3.2 reset index:moves the current index back into a column and
# resets the index to the default integer index (0, 1, 2, ...).
df.reset_index(inplace=True)

# 3.3 optional:drop =True when you want to remove the index column after resetting
df.reset_index(inplace=True, drop=True)


# 4. select columns
df_selected = df[["Name", "Age"]]

# 5. filter rows
df_filtered = df[df["Age"] > 25]

# 6. sort values
df_sorted = df.sort_values(by="Salary", ascending=False)

# 7. add new column
df["Tax"] = df["Salary"] * 0.2

# 8. group by and aggregate
df_grouped = df.groupby("City").agg({"Salary": "mean", "Age": "max"}).reset_index()

# 9. Save data to csv
import os


df.to_csv("output.csv", index=False)  # Save to current working directory
os.getcwd()  # get current working directory
# Save to an absolute path
df.to_csv(r"C:\development\repo\output_abs.csv", index=False)

# 10. Read data from csv
df_read = pd.read_csv("output.csv")  # Read from current working directory
# Read from an absolute path
df_read2 = pd.read_csv(r"C:\development\repo\python_for_beginners\output_abs.csv")
