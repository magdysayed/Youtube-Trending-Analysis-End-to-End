import pandas as pd
import json
import pyodbc

# Load the JSON file
with open('Us_category_id.json') as f:
    data = json.load(f)

category_list =[]
# Extract the category names and IDs
for item in data['items']:
    category_name = item['snippet']['title']
    category_id = int(item['id'])
    category_list.append((category_id , category_name ))

# Create a DataFrame from the category list
df_categories = pd.DataFrame(category_list, columns=['category_id', 'category_name'])

# Connect to the SQL Server database
conn= pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=.;'
    'DATABASE=YouTube_Analysis;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()
# Create the Categories table if it doesn't exist
cursor.execute('''
    IF OBJECT_ID('Categories', 'U') IS NOT NULL DROP TABLE Categories;
    CREATE TABLE Categories (
        category_id int PRIMARY KEY,
        category_name nvarchar(255)
    )
''')

# Insert the category data into the Categories table
for index, row in df_categories.iterrows():
    cursor.execute('''
        INSERT INTO Categories (category_id, category_name)
        VALUES (?, ?)
    ''', row['category_id'], row['category_name'])

# Commit the transaction and close the connection
conn.commit()
cursor.close()
conn.close()

print("Data inserted successfully into the Categories table.")