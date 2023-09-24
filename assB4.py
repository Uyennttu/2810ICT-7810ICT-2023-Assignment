import sqlite3


def execute_query(query, params=()):
    conn = sqlite3.connect('airbnb.db')
    cursor = conn.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results


# Define the cleanliness-related keywords to search for
cleanliness_keywords = ["clean", "tidy", "neat", "hygienic", "spotless"]

# Generate a SQL query to count comments containing cleanliness-related keywords
query = """
    SELECT COUNT(*)
    FROM reviews_dec18
    WHERE LOWER(comments) LIKE ?
"""

# Initialize a counter for the total number of comments mentioning cleanliness
total_cleanliness_comments = 0

# Execute the query for each cleanliness-related keyword and accumulate the counts
for keyword in cleanliness_keywords:
    keyword_count = execute_query(query, ('%' + keyword + '%',))
    total_cleanliness_comments += keyword_count[0][0]

# Print the total number of comments mentioning cleanliness
print(f"Total number of comments mentioning cleanliness: {total_cleanliness_comments}")
