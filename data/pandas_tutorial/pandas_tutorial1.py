import pandas as pd


df = pd.read_csv(r'C:\development\repo\finance_etl_simple\data\stock_data.csv')




# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 30, 22, 35, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Salary': [70000, 80000, 60000, 90000, 75000]
}

# 1.Create DataFrame
df = pd.DataFrame(data)

df2 = pd.DataFrame(data )
#2. select columns
df_selected = df[['Name', 'Age']]

print("Selected Columns:\n", df_selected)


#3. filter rows
df_filtered = df[df['Age'] > 25]
print("\nFiltered Rows:\n", df_filtered)

#4. sort values
df_sorted = df.sort_values(by='Salary', ascending=False)
print("\nSorted DataFrame:\n", df_sorted)

#5. add new column
df['Tax'] = df['Salary'] * 0.2
print("\nDataFrame with New Column:\n", df)



#6. group by and aggregate
df_grouped = df.groupby('City').agg({'Salary': 'mean', 'Age': 'max'}).reset_index()
print("\nGrouped and Aggregated DataFrame:\n", df_grouped)

#7. Save data to csv
df.to_csv('output.csv', index=False)