import sqlite3
import matplotlib.pyplot as plt
import pandas as pd


def execute_query(query, params=()):
    conn = sqlite3.connect('airbnb.db')
    cursor = conn.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results


# Get user input
start_date_str = input("Enter the start date (DD-MM-YYYY): ")
end_date_str = input("Enter the end date (DD-MM-YYYY): ")

# Input validation for date format
try:
    start_date = pd.to_datetime(start_date_str, format="%d-%m-%Y")
    end_date = pd.to_datetime(end_date_str, format="%d-%m-%Y")
except ValueError:
    print("Invalid date format. Please use DD-MM-YYYY format.")
    exit(1)

# Convert the dates to strings in 'YYYY-MM-DD' format
start_date_str = start_date.strftime("%Y-%m-%d")
end_date_str = end_date.strftime("%Y-%m-%d")

# Define the SQL query to retrieve prices of properties in the specified date range
query = """
    SELECT price
    FROM calendar_dec18
    WHERE date >= ?
    AND date <= ?
"""

# Execute the query with user input as parameters
results = execute_query(query, (start_date_str, end_date_str))

# Extract prices from the query results, handling None values
prices = [float(row[0].replace('$', '').replace(',', '')) if row[0] is not None else 0 for row in results]

# Create a histogram to visualize the distribution of prices
plt.figure(figsize=(10, 6))
plt.hist(prices, bins=20, edgecolor='k', alpha=0.7)
plt.xlabel("Price (USD)")
plt.ylabel("Number of Properties")
plt.title(f"Price Distribution of Properties ({start_date_str} to {end_date_str})")
plt.grid(True)
plt.show()

