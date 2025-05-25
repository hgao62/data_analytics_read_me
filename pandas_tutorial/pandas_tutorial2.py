import pandas as pd

# Sample data
data = [{'Category': 'A', 'Value': '10.0', 'Date': '2023/1/1', 'Name': 'Alice', 'Age': 25.0, 'Email': 'alice@example.com', 'ID': 12345}, {'Category': 'A', 'Value': '10.0', 'Date': '2023/1/1', 'Name': 'Alice', 'Age': 25.0, 'Email': 'alice@example.com', 'ID': 12346}, {'Category': 'A', 'Value': pd.NA, 'Date': '2023/1/2', 'Name': 'Bob', 'Age': 30.0, 'Email': 'bob@example.com', 'ID': 12347}, {'Category': 'B', 'Value': 30.0, 'Date': '2023/1/1', 'Name': pd.NA, 'Age': pd.NA, 'Email': 'charlie@example.com', 'ID': 12348}, {'Category': 'B', 'Value': '40.0', 'Date': '2023/1/2', 'Name': 'David', 'Age': 40.0, 'Email': pd.NA, 'ID': 12349}, {'Category': 'C', 'Value': pd.NA, 'Date': '2023/1/1', 'Name': 'Eva', 'Age': 45.0, 'Email': 'eva@example.com', 'ID': 12350}, {'Category': 'C', 'Value': '60.0', 'Date': pd.NA, 'Name': 'Frank', 'Age': 50.0, 'Email': 'frank@example.com', 'ID': 12351}, {'Category': 'C', 'Value': '60.0', 'Date': pd.NA, 'Name': 'Frank', 'Age': 50.0, 'Email': 'frank@example.com', 'ID': 12351}]

# 1.Create DataFrame
df = pd.DataFrame(data)

#2. drop na values (only drop rows with missing values in 'Email' column)
cleaned_df = df.dropna(subset=['Email'])

#3. fill na values (fill missing values in 'Name' column with a default value)
cleaned_df["Name"] = cleaned_df["Name"].fillna("Name missing")


#4 filter data with multiple filtering conditions 
cleaned_df = cleaned_df[(cleaned_df["Age"] >= 25) & (cleaned_df["Age"] <= 40)]

#5. Convert data and data types
# 5.1(convert 'Date' column to datetime format)
cleaned_df['Date'] = pd.to_datetime(cleaned_df['Date'], format='%Y/%m/%d')

#5.2. Convert name columns to lowercase
cleaned_df['Name'] = cleaned_df['Name'].str.lower()

#5.3. Convert 'Value' column to numeric (float) type
cleaned_df['Value'] = pd.to_numeric(cleaned_df['Value'], errors='coerce')


#6. Extract year  from date column
cleaned_df['Year'] = cleaned_df['Date'].dt.year

