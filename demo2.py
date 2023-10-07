import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox  # Added messagebox for user alerts


def load_data():
    listings = pd.read_csv('listings_dec18.csv', low_memory=False)
    calendar = pd.read_csv('calendar_dec18.csv', parse_dates=['date'], low_memory=False)
    return listings, calendar


def display_prices(start_date, end_date, frame, top_n, listings_df, calendar_df):
    listings_subset = listings_df[['id', 'neighbourhood']]
    calendar_subset = calendar_df[
        (calendar_df['date'] >= start_date) & (calendar_df['date'] <= end_date)
        ][['listing_id', 'date', 'price']]
    calendar_subset['price'] = calendar_subset['price'].replace('[\$,]', '', regex=True).astype(float)

    merged_data = pd.merge(calendar_subset, listings_subset, left_on='listing_id', right_on='id', how='inner')
    suburb_means = merged_data.groupby('neighbourhood')['price'].mean()
    sorted_suburb_means = suburb_means.sort_values(ascending=False).head(top_n)

    if sorted_suburb_means.empty:
        messagebox.showerror("Error", "No data to plot.")  # GUI feedback
        return

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.barh(sorted_suburb_means.index, sorted_suburb_means.values)
    ax.set(xlabel='Mean Price ($)', ylabel='Suburb',
           title='Mean Prices by Suburb from {} to {}'.format(start_date.strftime('%Y-%m-%d'),
                                                              end_date.strftime('%Y-%m-%d')))
    ax.invert_yaxis()

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=4, column=0, columnspan=2, padx=5, pady=5)


def on_submit():
    try:
        start_date = datetime.strptime(start_date_entry.get(), "%Y-%m-%d")
        end_date = datetime.strptime(end_date_entry.get(), "%Y-%m-%d")
        top_n = int(top_n_entry.get())
        display_prices(start_date, end_date, frame, top_n, listings, calendar)
    except ValueError as ve:
        messagebox.showerror("Error", "Invalid input: {}".format(ve))  # GUI feedback


# Load data
listings, calendar = load_data()

root = tk.Tk()
root.title('Price Visualization')

frame = ttk.Frame(root, padding='5 5 5 5')
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

ttk.Label(frame, text='Start date (YYYY-MM-DD):').grid(column=0, row=0, sticky=tk.W)
start_date_entry = ttk.Entry(frame, width=15)
start_date_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))

ttk.Label(frame, text='End date (YYYY-MM-DD):').grid(column=0, row=1, sticky=tk.W)
end_date_entry = ttk.Entry(frame, width=15)
end_date_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

ttk.Label(frame, text='Top N neighbourhoods:').grid(column=0, row=2, sticky=tk.W)
top_n_entry = ttk.Entry(frame, width=5)
top_n_entry.grid(column=1, row=2, sticky=(tk.W, tk.E))
top_n_entry.insert(0, '5')

submit_button = ttk.Button(frame, text='Submit', command=on_submit)
submit_button.grid(column=1, row=3, sticky=tk.W)

root.mainloop()
