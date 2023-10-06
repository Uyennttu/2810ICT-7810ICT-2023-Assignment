import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime

# Load the dataset and suppress low_memory warning
dataset = pd.read_csv('listings_summary_dec18.csv', low_memory=False)


def display_prices(start_date, end_date, frame, top_n):
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format, please enter dates in YYYY-MM-DD format.")
        return

    if start_date > end_date:
        print("Start date cannot be greater than end date.")
        return

    suburb_prices = {}
    for index, row in dataset.iterrows():
        listing_date = datetime.strptime(row['last_scraped'], '%Y-%m-%d')
        listing_suburb = str(row['neighbourhood']) if pd.notna(row['neighbourhood']) else 'Unknown'
        listing_price = row['price']

        if start_date <= listing_date <= end_date:
            if listing_suburb not in suburb_prices:
                suburb_prices[listing_suburb] = {'total_price': 0, 'count': 0}

            suburb_prices[listing_suburb]['total_price'] += float(listing_price.strip('$').replace(',', ''))
            suburb_prices[listing_suburb]['count'] += 1

    suburb_means = {suburb: data['total_price'] / data['count'] for suburb, data in suburb_prices.items()}
    sorted_suburb_means = dict(sorted(suburb_means.items(), key=lambda item: item[1], reverse=True)[:top_n])

    if not sorted_suburb_means:
        print("No data to plot.")
        return

    suburbs = list(sorted_suburb_means.keys())
    mean_prices = list(sorted_suburb_means.values())

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.barh(suburbs, mean_prices)
    ax.set(xlabel='Mean Price ($)', ylabel='Suburb', title='Mean Prices by Suburb from {} to {}'.format(start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')))
    ax.invert_yaxis()  # To display the highest value at the top in the horizontal bar chart

    canvas = FigureCanvasTkAgg(fig, master=frame)  # A tk.DrawingArea
    canvas.draw()
    canvas.get_tk_widget().grid(row=4, column=0, columnspan=2, padx=5, pady=5)


# GUI Setup
app = tk.Tk()
app.title("Airbnb Data Analysis")

notebook = ttk.Notebook(app)
notebook.pack(padx=10, pady=10)

frame2 = ttk.Frame(notebook)
notebook.add(frame2, text="Display Prices")

# Start Date
ttk.Label(frame2, text="Start Date (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5)
start_date_entry_2 = ttk.Entry(frame2)
start_date_entry_2.grid(row=0, column=1, padx=5, pady=5)

# End Date
ttk.Label(frame2, text="End Date (YYYY-MM-DD):").grid(row=1, column=0, padx=5, pady=5)
end_date_entry_2 = ttk.Entry(frame2)
end_date_entry_2.grid(row=1, column=1, padx=5, pady=5)

# Top N Dropdown
ttk.Label(frame2, text="Top N Suburbs:").grid(row=2, column=0, padx=5, pady=5)
top_n_values = [str(i) for i in range(1, 21)]
top_n_var = tk.StringVar(value=top_n_values[9])
top_n_dropdown = ttk.Combobox(frame2, textvariable=top_n_var, values=top_n_values)
top_n_dropdown.grid(row=2, column=1, padx=5, pady=5)

# Display Prices Button
display_prices_button = ttk.Button(
    frame2,
    text="Display Prices",
    command=lambda: display_prices(
        start_date_entry_2.get(),
        end_date_entry_2.get(),
        frame2,
        int(top_n_var.get())
    )
)
display_prices_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

app.mainloop()


