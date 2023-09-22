import sqlite3
import pandas as pd
import os

# Define paths to CSV files and the SQLite database file
csv_files = ['calendar_dec18.csv', 'reviews_dec18.csv', 'listings_dec18.csv']
db_file = 'airbnb.db'

# Create a SQLite database connection
conn = sqlite3.connect(db_file)

# Loop through CSV files and convert them to database tables
for csv_file in csv_files:
    if not os.path.exists(csv_file):
        print(f"CSV file '{csv_file}' not found.")
        continue

    # Extract table name from the CSV file name (without the extension)
    table_name = os.path.splitext(os.path.basename(csv_file))[0]

    # Read CSV data into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Write the DataFrame to the SQLite database
    df.to_sql(table_name, conn, index=False, if_exists='replace')
    print(f"Converted '{csv_file}' to table '{table_name}' in the database.")

print("All CSV files have been converted to the SQLite database.")

