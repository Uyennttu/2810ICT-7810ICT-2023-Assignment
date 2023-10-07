import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd

try:
    dataset = pd.read_csv('reviews_dec18.csv')
except FileNotFoundError:
    messagebox.showerror("File Error", "listings_dec18.csv not found in the current directory.")
    dataset = pd.DataFrame()


def retrieve_count(search_fields):
    if dataset.empty:
        messagebox.showerror("Error", "The dataset is empty!")
        return

    if not search_fields:
        search_fields = ['cleanliness']  # default search field

    cleanliness_keywords = ['clean', 'tidy', 'sanitary', 'unsoiled', 'swept', 'spotless', 'neat']

    count = 0
    for index, row in dataset.iterrows():
        comment = str(row.get('comments', ''))
        if comment and comment.lower() != 'nan':
            if any(keyword in comment.lower() for keyword in cleanliness_keywords):
                count += 1

    count_label.config(text=f"Count of listings: {count}")
    messagebox.showinfo("Result", f"Count of listings: {count}")


app = tk.Tk()
app.title("Airbnb Data Analysis")

notebook = ttk.Notebook(app)
notebook.pack(padx=10, pady=10)

frame4 = ttk.Frame(notebook)
notebook.add(frame4, text="Retrieve Count")

search_fields_label = ttk.Label(frame4, text="Search Fields (comma-separated):")
search_fields_label.grid(row=0, column=0, padx=5, pady=5)
search_fields_entry = ttk.Entry(frame4)
search_fields_entry.grid(row=0, column=1, padx=5, pady=5)

count_label = ttk.Label(frame4, text="Count of listings: 0")
count_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)


retrieve_count_button = ttk.Button(frame4, text="Retrieve Count",
                                   command=lambda: retrieve_count(search_fields_entry.get().split(',')))
retrieve_count_button.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

app.mainloop()
