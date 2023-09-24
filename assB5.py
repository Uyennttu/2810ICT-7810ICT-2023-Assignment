import sqlite3


def execute_query(query, params=()):
    conn = sqlite3.connect('airbnb.db')
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchone()
    conn.close()
    return result


# Get user input for the desired suburb
suburb = input("Enter the desired suburb: ")

# Define the SQL query to count reviews in the selected suburb
query = """
    SELECT COUNT(r.id)
    FROM reviews_dec18 r
    JOIN listings_dec18 l ON r.listing_id = l.id
    WHERE l.neighbourhood_cleansed = ?;
"""

# Execute the query with the selected suburb as a parameter
result = execute_query(query, (suburb,))

if result[0] is not None:
    review_count = result[0]
    print(f"The number of reviews in {suburb} is: {review_count}")
else:
    print(f"No reviews found for listings in {suburb}.")

