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
keyword = input("Enter a keyword to search for (e.g., 'pool', 'pet'): ")
start_date_str = input("Enter the start date (DD-MM-YYYY): ")
end_date_str = input("Enter the end date (DD-MM-YYYY): ")

# Input validation for date format
try:
    start_date = datetime.strptime(start_date_str, "%d-%m-%Y").date()
    end_date = datetime.strptime(end_date_str, "%d-%m-%Y").date()
except ValueError:
    print("Invalid date format. Please use DD-MM-YYYY format.")
    exit(1)

# Define the SQL query to retrieve listings containing the keyword within the specified date range
query = """
    SELECT *
    FROM listings_dec18 AS l
    WHERE (name LIKE ? OR summary LIKE ? OR space LIKE ? OR description LIKE ?)
    AND EXISTS (
        SELECT 1
        FROM calendar_dec18 AS c
        WHERE c.listing_id = l.id
        AND c.date >= ?
        AND c.date <= ?
    )
"""

# Execute the query with user input as parameters
params = (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%", f"%{keyword}%", start_date, end_date)
results = execute_query(query, params)

# Check if there are any results
if not results:
    print(f"No listings containing '{keyword}' found between {start_date_str} and {end_date_str}.")
else:
    print("Matching Listing Information:")
    for row in results:
        print("Listing ID:", row[0])
        print("Name:", row[4])
        print("Description:", row[6])
