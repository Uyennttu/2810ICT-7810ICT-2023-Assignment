import tkinter as tk
from tkinter import ttk
import pandas as pd
import threading
from datetime import datetime

# Load dataset
dataset = pd.read_csv('listings_dec18.csv')


def report_all_listings(start_date, end_date, search_suburb, output_text):
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

    output_text.insert(tk.END, "Searching...\n")

    # Convert 'last_scraped' to datetime
    dataset['last_scraped'] = pd.to_datetime(dataset['last_scraped'], errors='coerce')

    # Filter rows using vectorized operations
    mask = (dataset['last_scraped'] >= start_date) & (dataset['last_scraped'] <= end_date) & (dataset['neighbourhood'].str.contains(search_suburb, case=False, na=False))
    filtered_data = dataset.loc[mask]

    # Sort and Display the filtered data
    sorted_data = filtered_data.sort_values(by='last_scraped')
    for index, row in sorted_data.iterrows():
        output_text.insert(tk.END, f"Name: {row['name']}, Suburb: {row['neighbourhood']}, Date: {row['last_scraped'].strftime('%Y-%m-%d')}, Price: {row['price']}\n")


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
output_text.insert(tk.END, "Results will be displayed here.\n")

# Report Button
report_button = ttk.Button(
    frame1,
    text="Generate Report",
    command=lambda: threading.Thread(
        target=report_all_listings,
        args=(start_date_entry.get(), end_date_entry.get(), search_suburb_entry.get(), output_text),
        daemon=True
    ).start()
)
report_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

app.mainloop()
