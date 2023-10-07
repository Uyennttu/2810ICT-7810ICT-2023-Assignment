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


def update_output_text(text):
    output_text.insert(tk.END, text)
    output_text.yview(tk.END)


def search_keyword(start_date, end_date, keywords, output_text):
    global calendar_dataset
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        app.after(0, update_output_text, "Invalid date format. Please use YYYY-MM-DD format.\n")
        return

    if not keywords:
        app.after(0, update_output_text, "Please enter at least one keyword.\n")
        return

    mask = (calendar_dataset['date'] >= start_date) & (calendar_dataset['date'] <= end_date)
    filtered_calendar_data = calendar_dataset.loc[mask]
    merged_data = pd.merge(filtered_calendar_data, listings_dataset, left_on='listing_id', right_on='id', how='inner')

    matching_listings = []
    for index, row in merged_data.iterrows():
        listing_description = str(row.get('description', ''))

        for keyword in keywords:
            if keyword.strip().lower() in listing_description.lower():
                matching_listings.append(row)
                break

    # Clear the existing text in output_text
    app.after(0, output_text.delete, 1.0, tk.END)

    sorted_listings = sorted(matching_listings, key=lambda x: x.get('date', ''))
    total_matches = len(sorted_listings)

    print(f"Number of matching listings: {total_matches}")

    if not sorted_listings:
        app.after(0, update_output_text, "No matching listings found.\n")
        return

    # Limit and concatenate the results
    display_limit = 5
    results_text = ""

    for i, listing in enumerate(sorted_listings[:display_limit]):
        id = listing.get('id')
        name = listing.get('name')
        url = listing.get('listing_url')
        date = listing.get('date')
        description = listing.get('description')
        results_text += f"ID: {id}\nName: {name}\nURL: {url}\nDate: {date}\nDescription: {description}\n"

    # Update the GUI once with concatenated results
    app.after(0, update_output_text,
              results_text + f"\nDisplaying {min(display_limit, total_matches)} of {total_matches} matching listings.")


load_data()

app = tk.Tk()
app.title("Airbnb Data Analysis")

notebook = ttk.Notebook(app)
notebook.pack(padx=10, pady=10)

frame3 = ttk.Frame(notebook)
notebook.add(frame3, text="Search Keyword")

start_date_label_2 = ttk.Label(frame3, text="Start Date (YYYY-MM-DD):")
start_date_label_2.grid(row=0, column=0, padx=5, pady=5)
start_date_entry_3 = ttk.Entry(frame3)
start_date_entry_3.grid(row=0, column=1, padx=5, pady=5)

end_date_label_2 = ttk.Label(frame3, text="End Date (YYYY-MM-DD):")
end_date_label_2.grid(row=1, column=0, padx=5, pady=5)
end_date_entry_3 = ttk.Entry(frame3)
end_date_entry_3.grid(row=1, column=1, padx=5, pady=5)

keywords_label = ttk.Label(frame3, text="Keywords (comma-separated):")
keywords_label.grid(row=2, column=0, padx=5, pady=5)
keywords_entry = ttk.Entry(frame3)
keywords_entry.grid(row=2, column=1, padx=5, pady=5)

search_keyword_button = ttk.Button(frame3, text="Search Keyword",
                                   command=lambda: threading.Thread(target=search_keyword, args=(
                                       start_date_entry_3.get(), end_date_entry_3.get(),
                                       keywords_entry.get().split(','), output_text)).start())
search_keyword_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

output_text = tk.Text(frame3, height=10, width=50)
output_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

app.mainloop()

