import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd

# Load the dataset
try:
    dataset = pd.read_csv('listings_dec18.csv')
except FileNotFoundError:
    messagebox.showerror("File Error", "listings_dec18.csv not found in the current directory.")
    dataset = pd.DataFrame()

app = tk.Tk()
app.title("Airbnb Data Analysis")

# Create and configure a notebook for different functions
notebook = ttk.Notebook(app)
notebook.pack(padx=10, pady=10)

# Frame for Apartment Bedrooms Count
frame6 = ttk.Frame(notebook)
notebook.add(frame6, text="Apartment Bedrooms Count")

# Create labels and entry fields for the suburb
suburb_label = ttk.Label(frame6, text="Suburb:")
suburb_label.grid(row=1, column=0, padx=5, pady=5)

suburb_entry = ttk.Entry(frame6)
suburb_entry.grid(row=1, column=1, padx=5, pady=5)

bedroom_label = ttk.Label(frame6, text="Number of Bedrooms:")
bedroom_label.grid(row=0, column=0, padx=5, pady=5)

bedroom_entry = ttk.Entry(frame6)
bedroom_entry.grid(row=0, column=1, padx=5, pady=5)


def count_apartment_bedrooms():
    # Extract number of bedrooms and suburb from the entry
    try:
        num_bedrooms = int(bedroom_entry.get())
        suburb = suburb_entry.get().strip()  # get suburb and remove any leading/trailing whitespace
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for bedrooms.")
        return

    if 'property_type' not in dataset.columns or 'bedrooms' not in dataset.columns or 'neighbourhood' not in dataset.columns:
        messagebox.showerror("Error", "'property_type', 'bedrooms', or 'neighbourhood' column not found in the dataset.")
        return

    # Filter the DataFrame for apartments with the specified number of bedrooms and in the specified suburb
    filtered_df = dataset[
        (dataset['property_type'] == 'Apartment') &
        (dataset['bedrooms'] == num_bedrooms) &
        (dataset['neighbourhood'].str.lower() == suburb.lower())
    ]

    # Display the result
    count = len(filtered_df)
    messagebox.showinfo("Result", f"There are {count} apartments with {num_bedrooms} bedrooms in {suburb}.")


# Define count_button before using its grid method
count_button = ttk.Button(frame6, text="Count Bedrooms", command=count_apartment_bedrooms)


count_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

app.mainloop()


