import sqlite3
from datetime import datetime


def execute_query(query, params=()):
    conn = sqlite3.connect('airbnb.db')
    cursor = conn.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results


# Get user input
suburb = input("Enter the desired suburb: ")
start_date_str = input("Enter the start date (DD-MM-YYYY): ")
end_date_str = input("Enter the end date (DD-MM-YYYY): ")

# Input validation for date format
try:
    start_date = datetime.strptime(start_date_str, "%d-%m-%Y").date()
    end_date = datetime.strptime(end_date_str, "%d-%m-%Y").date()
except ValueError:
    print("Invalid date format. Please use DD-MM-YYYY format.")
    exit(1)

# Define the SQL query to retrieve listings in the specified suburb and date range
query = """
    SELECT *
    FROM listings_dec18 AS l
    WHERE l.neighbourhood_cleansed = ? 
    AND EXISTS (
        SELECT 1
        FROM calendar_dec18 AS c
        WHERE c.listing_id = l.id
        AND c.date >= ?
        AND c.date <= ?
    )
"""

# Execute the query with user input as parameters
results = execute_query(query, (suburb, start_date, end_date))

# Check if there are any results
if not results:
    print(f"No listings found in {suburb} between {start_date_str} and {end_date_str}.")
else:
    print("Listing Information:")
    for row in results:
        print("Listing ID:", row[0])
        print("Name:", row[4])
        print("Description:", row[6])
