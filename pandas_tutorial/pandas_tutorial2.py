# Chapter 12-2: Data Cleaning and Transformation with Pandas
import pandas as pd

# Sample data
data = [
    {
        "Category": "A",
        "Value": "10.0",
        "Date": "2023/1/1",
        "Name": "Alice",
        "Age": 25.0,
        "Email": "alice@example.com",
        "ID": 12345,
    },
    {
        "Category": "A",
        "Value": "10.0",
        "Date": "2023/1/1",
        "Name": "Alice",
        "Age": 25.0,
        "Email": "alice@example.com",
        "ID": 12346,
    },
    {
        "Category": "A",
        "Value": pd.NA,
        "Date": "2023/1/2",
        "Name": "Bob",
        "Age": 30.0,
        "Email": "bob@example.com",
        "ID": 12347,
    },
    {
        "Category": "B",
        "Value": 30.0,
        "Date": "2023/1/1",
        "Name": pd.NA,
        "Age": pd.NA,
        "Email": "charlie@example.com",
        "ID": 12348,
    },
    {
        "Category": "B",
        "Value": "40.0",
        "Date": "2023/1/2",
        "Name": "David",
        "Age": 40.0,
        "Email": pd.NA,
        "ID": 12349,
    },
    {
        "Category": "C",
        "Value": pd.NA,
        "Date": "2023/1/1",
        "Name": "Eva",
        "Age": 45.0,
        "Email": "eva@example.com",
        "ID": 12350,
    },
    {
        "Category": "C",
        "Value": "60.0",
        "Date": pd.NA,
        "Name": "Frank",
        "Age": 50.0,
        "Email": "frank@example.com",
        "ID": 12351,
    },
    {
        "Category": "C",
        "Value": "abc", # This is a dirty value
        "Date": pd.NA,
        "Name": "Frank",
        "Age": pd.NA,
        "Email": "frank@example.com",
        "ID": 12351,
    },
]

# 1.Create DataFrame
df = pd.DataFrame(data)

# 2. drop na values (only drop rows with missing values in 'Email' column)
cleaned_df = df.dropna(subset=["Email"])

# 3. fill na values (fill missing values in 'Name' column with a default value)
cleaned_df["Name"] = cleaned_df["Name"].fillna("Name missing")


# 4 filter data with multiple filtering conditions
cleaned_df = cleaned_df[(cleaned_df["Age"] >= 25) & (cleaned_df["Age"] <= 40)]

# 5. Convert data and data types
#5.1 convert 'Name' column to string type
cleaned_df['Name'] = cleaned_df['Name'].astype("string")  # Convert 'Name' column to string type

#5.2 convert Age column to integer type
cleaned_df['Age'] = cleaned_df['Age'].astype("Int64")  # Convert 'Age' column to integer type (nullable)

# 5.3(convert 'Date' column to datetime format)
cleaned_df["Date"] = pd.to_datetime(cleaned_df["Date"], format="%Y/%m/%d") 
# format is the existing format of the date strings



# 5.4 Convert 'Value' column to numeric type when it contains dirty
# or mixed data ("N/A, "unknown", "")
cleaned_df["Value"] = pd.to_numeric(cleaned_df["Value"], errors="coerce")


cleaned_df['Value'].astype(int) # won't work because 10.0

cleaned_df['Value'].astype(float) # won't work because NA
cleaned_df['Value'] = pd.to_numeric(cleaned_df['Value'])# won't work because abc

