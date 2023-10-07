import tkinter as tk
from tkinter import ttk
import pandas as pd
import threading
from datetime import datetime


def load_data():
    global listings_dataset, calendar_dataset
    try:
        listings_dataset = pd.read_csv('listings_dec18.csv', low_memory=False)
        calendar_dataset = pd.read_csv('calendar_dec18.csv')
        calendar_dataset['date'] = pd.to_datetime(calendar_dataset['date'], errors='coerce')
    except Exception as e:
        print(f"Error loading data: {e}")


def report_all_listings(start_date, end_date, search_suburb, output_text, report_button):
    report_button.config(state=tk.DISABLED)
    output_text.insert(tk.END, "Searching...\n")
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        output_text.insert(tk.END, "Invalid date format. Please use YYYY-MM-DD format.\n")
        return

    if not search_suburb:
        output_text.insert(tk.END, "Please ensure suburb field is filled.\n")
        return

    if start_date > end_date:
        output_text.insert(tk.END, "Date range is not in order. Please check date order.\n")
        return

    # Filter rows using vectorized operations
    mask = (calendar_dataset['date'] >= start_date) & (calendar_dataset['date'] <= end_date)
    filtered_calendar_data = calendar_dataset.loc[mask]

    # Merge the listings and calendar datasets on the 'listing_id' column
    merged_data = pd.merge(filtered_calendar_data, listings_dataset, left_on='listing_id', right_on='id', how='inner')

    # Filter the merged data by suburb
    mask = merged_data['neighbourhood'].str.contains(search_suburb, case=False, na=False)
    filtered_data = merged_data.loc[mask]

    # Ensure 'date' and 'price' is available
    if 'date' not in filtered_data or 'price_x' not in filtered_data:
        output_text.insert(tk.END, "Unexpected columns after data merge, please check datasets.\n")
        return

    # Sort and Display the filtered data
    sorted_data = filtered_data.sort_values(by='date')

    if sorted_data.empty:
        output_text.insert(tk.END, "No results found.\n")
        return

    # Columns related to reviews and comments
    excluded_columns = [
        'summary', 'space', 'description', 'neighborhood_overview', 'notes', 'transit',
        'access', 'interaction', 'house_rules', 'review_scores_rating',
        'review_scores_accuracy', 'review_scores_cleanliness',
        'review_scores_checkin', 'review_scores_communication',
        'review_scores_location', 'review_scores_value', 'number_of_reviews',
        'first_review', 'last_review', 'reviews_per_month'
    ]

    for index, row in sorted_data.iterrows():
        output_msg = "Listing Details:\n"

        # Loop through all columns and add to output if not excluded
        for col in sorted_data.columns:
            if col not in excluded_columns:
                output_msg += f"{col.replace('_', ' ').capitalize()}: {row[col]}\n"

        # Insert the constructed message into the Text widget
        output_text.insert(tk.END, output_msg + "\n---\n")

        # To prevent application freezing during long iterations
        app.update_idletasks()

    report_button.config(state=tk.NORMAL)


app = tk.Tk()
app.title("Airbnb Data Analysis")

notebook = ttk.Notebook(app)
notebook.pack(padx=10, pady=10)

frame1 = ttk.Frame(notebook)
notebook.add(frame1, text="Report All Listings")

# Start Date Label and Entry
start_date_label = ttk.Label(frame1, text="Start Date (YYYY-MM-DD):")
start_date_label.grid(row=0, column=0, padx=5, pady=5)
start_date_entry = ttk.Entry(frame1)
start_date_entry.grid(row=0, column=1, padx=5, pady=5)

# End Date Label and Entry
end_date_label = ttk.Label(frame1, text="End Date (YYYY-MM-DD):")
end_date_label.grid(row=1, column=0, padx=5, pady=5)
end_date_entry = ttk.Entry(frame1)
end_date_entry.grid(row=1, column=1, padx=5, pady=5)

# Search Suburb Label and Entry
search_suburb_label = ttk.Label(frame1, text="Search Suburb:")
search_suburb_label.grid(row=2, column=0, padx=5, pady=5)
search_suburb_entry = ttk.Entry(frame1)
search_suburb_entry.grid(row=2, column=1, padx=5, pady=5)

# Output Text
output_text = tk.Text(frame1, wrap='word', height=10, width=50)
output_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

scrollbar = tk.Scrollbar(frame1, command=output_text.yview)
scrollbar.grid(row=4, column=2, sticky='nsew')

output_text['yscrollcommand'] = scrollbar.set

output_text.insert(tk.END, "Results will be displayed here.\n")

# Modify Report Button
report_button = ttk.Button(
    frame1,
    text="Generate Report",
    command=lambda: threading.Thread(
        target=report_all_listings,
        args=(start_date_entry.get(), end_date_entry.get(), search_suburb_entry.get(), output_text, report_button),
        daemon=True
    ).start()
)
report_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

load_data()
app.mainloop()
