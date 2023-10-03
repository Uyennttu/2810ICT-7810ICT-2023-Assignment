import tkinter as tk
from tkinter import ttk
import pandas as pd
from datetime import datetime
import threading

dataset = pd.read_csv('listings_dec18.csv')


def search_keyword(start_date, end_date, keywords, output_text):
    if not start_date or not end_date:
        output_text.insert(tk.END, "Please enter valid start and end dates.\n")
        return

    if start_date > end_date:
        output_text.insert(tk.END, "Start date cannot be greater than end date.\n")
        return

    if not keywords:
        output_text.insert(tk.END, "Please enter at least one keyword.\n")
        return

    matching_listings = []
    for index, row in dataset.iterrows():
        listing_date = str(row.get('last_scraped', ''))
        listing_description = str(row.get('description', ''))

        if start_date <= listing_date <= end_date:
            for keyword in keywords:
                if keyword.strip().lower() in listing_description.lower():
                    matching_listings.append(row)
                    break

    sorted_listings = sorted(matching_listings, key=lambda x: x.get('last_scraped', ''))

    if not sorted_listings:
        output_text.insert(tk.END, "No matching listings found.\n")
        return

    for listing in sorted_listings:
        id = listing.get('id')
        name = listing.get('name')
        url = listing.get('listing_url')
        last_scraped = listing.get('last_scraped')
        output_text.insert(tk.END, f"ID: {id}\nName: {name}\nURL: {url}\nLast Scraped: {last_scraped}\n\n")


app = tk.Tk()
app.title("Airbnb Data Analysis")


notebook = ttk.Notebook(app)
notebook.pack(padx=10, pady=10)

frame3 = ttk.Frame(notebook)
notebook.add(frame3, text="Search Keyword")

start_date_label_2 = ttk.Label(frame3, text="Start Date (YYYY-MM-DD):")
start_date_label_2.grid(row=0, column=0, padx=5, pady=5)
keywords_entry = ttk.Entry(frame3)
keywords_entry.grid(row=2, column=1, padx=5, pady=5)

end_date_label_2 = ttk.Label(frame3, text="End Date (YYYY-MM-DD):")
end_date_label_2.grid(row=1, column=0, padx=5, pady=5)
output_text = tk.Text(frame3, height=10, width=50)
output_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

start_date_entry_3 = ttk.Entry(frame3)
start_date_entry_3.grid(row=0, column=1, padx=5, pady=5)

end_date_entry_3 = ttk.Entry(frame3)
end_date_entry_3.grid(row=1, column=1, padx=5, pady=5)

keywords_label = ttk.Label(frame3, text="Keywords (comma-separated):")
keywords_label.grid(row=2, column=0, padx=5, pady=5)
search_keyword_button = ttk.Button(frame3, text="Search Keyword",
                                   command=lambda: threading.Thread(target=search_keyword, args=(
                                       start_date_entry_3.get(), end_date_entry_3.get(),
                                       keywords_entry.get().split(','), output_text)).start())
search_keyword_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

app.mainloop()
