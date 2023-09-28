import tkinter as tk
from tkinter import ttk
#from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#import numpy as np

# Create a DataFrame from the provided dataset
dataset = pd.read_csv('D:/assigment/listings_dec18.csv')



def report_all_listings(start_date, end_date):
    # Check if start_date and end_date are not empty
        if not start_date or not end_date:
            start_date = input("Enter start date: ")
            end_date = input("Enter end date: ")

        # Check if the date range is in order
        if start_date > end_date:
            raise ValueError("Date range is not in order. Please check date order.")

        # Check if user-entered search_suburb is not empty
        search_suburb = input("Enter search suburb: ")
        if not search_suburb:
            raise ValueError("Search suburb is empty. Please provide a valid suburb.")

        # Initialize empty lists
        listings = []

        # Loop through each row of the dataset
        for index, row in dataset.iterrows():
            listing_date = row['last_scraped']
            listing_suburb = row['neighbourhood']

            # Check if the listing matches the date range and search suburb
            if start_date <= listing_date <= end_date and search_suburb in listing_suburb:
                listings.append(row)

        # Sort and format the list of listings
        sorted_listings = sorted(listings, key=lambda x: x['last_scraped'])
        
        for listing in sorted_listings:
            print(listing)


def display_prices(start_date, end_date):
        # Check if start_date and end_date are not empty
        if not start_date or not end_date:
            start_date = input("Enter start date: ")
            end_date = input("Enter end date: ")

        # Check if the date range is in order
        if start_date > end_date:
            raise ValueError("Date range is not in order. Please check date order.")

        # Initialize a dictionary to hold suburb prices and counts
        suburb_prices = {}

        # Loop through each row of the dataset
        for index, row in dataset.iterrows():
            listing_date = row['last_scraped']
            listing_suburb = row['neighbourhood']
            listing_price = row['price']

            # Check if the listing matches the date range
            if start_date <= listing_date <= end_date:
                if listing_suburb not in suburb_prices:
                    suburb_prices[listing_suburb] = {'total_price': 0, 'count': 0}
                
                suburb_prices[listing_suburb]['total_price'] += float(listing_price.strip('$').replace(',', ''))
                suburb_prices[listing_suburb]['count'] += 1

        # Calculate the mean price for each suburb
        suburb_means = {}
        for suburb, data in suburb_prices.items():
            mean_price = data['total_price'] / data['count']
            suburb_means[suburb] = mean_price

        # Sort the suburb_means dictionary alphabetically
        sorted_suburb_means = dict(sorted(suburb_means.items()))

        # Separate keys (suburbs) and values (mean prices) into arrays
        suburbs = list(sorted_suburb_means.keys())
        mean_prices = list(sorted_suburb_means.values())

        # Plot the data
        plt.figure(figsize=(10, 6))
        plt.barh(suburbs, mean_prices)
        plt.xlabel('Mean Price')
        plt.ylabel('Suburb')
        plt.title('Mean Prices by Suburb')
        plt.gca().invert_yaxis()
        plt.show()




def search_keyword(start_date, end_date, keywords):
        # Check if start_date and end_date are not empty
        if not start_date or not end_date:
            start_date = input("Enter start date: ")
            end_date = input("Enter end date: ")

        # Check if the date range is in order
        if start_date > end_date:
            raise ValueError("Date range is not in order. Please check date order.")

        # Check if user-entered keywords list is empty
        if not keywords:
            keywords = input("Enter search keywords (comma-separated): ").split(',')

        # Initialize an empty list to store matching listings
        matching_listings = []

        # Loop through each row of the dataset
        for index, row in dataset.iterrows():
            listing_date = row['last_scraped']
            listing_description = row['description']

            # Check if the listing matches the date range and keywords
            if start_date <= listing_date <= end_date:
                for keyword in keywords:
                    if keyword.strip().lower() in listing_description.lower():
                        matching_listings.append(row)

        # Sort and format the list of matching listings
        sorted_listings = sorted(matching_listings, key=lambda x: x['last_scraped'])
        
        for listing in sorted_listings:
            print(listing)



def retrieve_count(start_date, end_date, search_fields):
        # Check if start_date and end_date are not empty
        if not start_date or not end_date:
            start_date = input("Enter start date: ")
            end_date = input("Enter end date: ")

        # Check if the date range is in order
        if start_date > end_date:
            raise ValueError("Date range is not in order. Please check date order.")

        # Initialize an array with the default value 'cleanliness'
        if not search_fields:
            search_fields = ['cleanliness']

        # Initialize a count variable
        count = 0

        # Loop through each row of the dataset
        for index, row in dataset.iterrows():
            listing_date = row['last_scraped']

            # Check if the listing matches the date range and search fields
            if start_date <= listing_date <= end_date:
                for field in search_fields:
                    if field in row:
                        count += 1

        print(f"Count of listings matching search fields: {count}")



def retrieve_count_listings(start_date, end_date, search_suburb):
        # Check if start_date and end_date are not empty
        if not start_date or not end_date:
            start_date = input("Enter start date: ")
            end_date = input("Enter end date: ")

        # Check if the date range is in order
        if start_date > end_date:
            raise ValueError("Date range is not in order. Please check date order.")

        # Check if user-entered search_suburb is not empty
        if not search_suburb:
            search_suburb = input("Enter search suburb: ")

        # Initialize an empty dictionary to store suburb listing counts
        suburb_listings_count = {}

        # Loop through each row of the dataset
        for index, row in dataset.iterrows():
            listing_date = row['last_scraped']
            listing_suburb = row['neighbourhood']

            # Check if the listing matches the date range and search suburb
            if start_date <= listing_date <= end_date and search_suburb in listing_suburb:
                if search_suburb not in suburb_listings_count:
                    suburb_listings_count[search_suburb] = 1
                else:
                    suburb_listings_count[search_suburb] += 1

        # Sort and format the suburb listing counts
        sorted_counts = dict(sorted(suburb_listings_count.items()))

        for suburb, count in sorted_counts.items():
            print(f"Suburb: {suburb}, Listing Count: {count}")


# Create the main application window
app = tk.Tk()
app.title("Airbnb Data Analysis")

# Create and configure a notebook for different functions
notebook = ttk.Notebook(app)
notebook.pack(padx=10, pady=10)

# Function 1: Report All Listings
frame1 = ttk.Frame(notebook)
notebook.add(frame1, text="Report All Listings")

start_date_label = ttk.Label(frame1, text="Start Date:")
start_date_label.grid(row=0, column=0, padx=5, pady=5)
start_date_entry = ttk.Entry(frame1)
start_date_entry.grid(row=0, column=1, padx=5, pady=5)

end_date_label = ttk.Label(frame1, text="End Date:")
end_date_label.grid(row=1, column=0, padx=5, pady=5)
end_date_entry = ttk.Entry(frame1)
end_date_entry.grid(row=1, column=1, padx=5, pady=5)

search_suburb_label = ttk.Label(frame1, text="Search Suburb:")
search_suburb_label.grid(row=2, column=0, padx=5, pady=5)
search_suburb_entry = ttk.Entry(frame1)
search_suburb_entry.grid(row=2, column=1, padx=5, pady=5)

report_button = ttk.Button(frame1, text="Generate Report", command=lambda: report_all_listings(start_date_entry.get(), end_date_entry.get()))
report_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

# Function 2: Display Prices
frame2 = ttk.Frame(notebook)
notebook.add(frame2, text="Display Prices")

start_date_label_2 = ttk.Label(frame2, text="Start Date:")
start_date_label_2.grid(row=0, column=0, padx=5, pady=5)
start_date_entry_2 = ttk.Entry(frame2)
start_date_entry_2.grid(row=0, column=1, padx=5, pady=5)

end_date_label_2 = ttk.Label(frame2, text="End Date:")
end_date_label_2.grid(row=1, column=0, padx=5, pady=5)
end_date_entry_2 = ttk.Entry(frame2)
end_date_entry_2.grid(row=1, column=1, padx=5, pady=5)

display_prices_button = ttk.Button(frame2, text="Display Prices", command=lambda: display_prices(start_date_entry_2.get(), end_date_entry_2.get()))
display_prices_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

# Function 3: Search Keyword
frame3 = ttk.Frame(notebook)
notebook.add(frame3, text="Search Keyword")

start_date_label_3 = ttk.Label(frame3, text="Start Date:")
start_date_label_3.grid(row=0, column=0, padx=5, pady=5)
start_date_entry_3 = ttk.Entry(frame3)
start_date_entry_3.grid(row=0, column=1, padx=5, pady=5)

end_date_label_3 = ttk.Label(frame3, text="End Date:")
end_date_label_3.grid(row=1, column=0, padx=5, pady=5)
end_date_entry_3 = ttk.Entry(frame3)
end_date_entry_3.grid(row=1, column=1, padx=5, pady=5)

keywords_label = ttk.Label(frame3, text="Keywords (comma-separated):")
keywords_label.grid(row=2, column=0, padx=5, pady=5)
keywords_entry = ttk.Entry(frame3)
keywords_entry.grid(row=2, column=1, padx=5, pady=5)

search_keyword_button = ttk.Button(frame3, text="Search Keyword", command=lambda: search_keyword(start_date_entry_3.get(), end_date_entry_3.get(), keywords_entry.get().split(',')))
search_keyword_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

# Function 4: Retrieve Count
frame4 = ttk.Frame(notebook)
notebook.add(frame4, text="Retrieve Count")

start_date_label_4 = ttk.Label(frame4, text="Start Date:")
start_date_label_4.grid(row=0, column=0, padx=5, pady=5)
start_date_entry_4 = ttk.Entry(frame4)
start_date_entry_4.grid(row=0, column=1, padx=5, pady=5)

end_date_label_4 = ttk.Label(frame4, text="End Date:")
end_date_label_4.grid(row=1, column=0, padx=5, pady=5)
end_date_entry_4 = ttk.Entry(frame4)
end_date_entry_4.grid(row=1, column=1, padx=5, pady=5)

search_fields_label = ttk.Label(frame4, text="Search Fields (comma-separated):")
search_fields_label.grid(row=2, column=0, padx=5, pady=5)
search_fields_entry = ttk.Entry(frame4)
search_fields_entry.grid(row=2, column=1, padx=5, pady=5)

retrieve_count_button = ttk.Button(frame4, text="Retrieve Count", command=lambda: retrieve_count(start_date_entry_4.get(), end_date_entry_4.get(), search_fields_entry.get().split(',')))
retrieve_count_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

# Function 5: Retrieve Count Listings
frame5 = ttk.Frame(notebook)
notebook.add(frame5, text="Retrieve Count Listings")

start_date_label_5 = ttk.Label(frame5, text="Start Date:")
start_date_label_5.grid(row=0, column=0, padx=5, pady=5)
start_date_entry_5 = ttk.Entry(frame5)
start_date_entry_5.grid(row=0, column=1, padx=5, pady=5)

end_date_label_5 = ttk.Label(frame5, text="End Date:")
end_date_label_5.grid(row=1, column=0, padx=5, pady=5)
end_date_entry_5 = ttk.Entry(frame5)
end_date_entry_5.grid(row=1, column=1, padx=5, pady=5)

search_suburb_label_5 = ttk.Label(frame5, text="Search Suburb:")
search_suburb_label_5.grid(row=2, column=0, padx=5, pady=5)
search_suburb_entry_5 = ttk.Entry(frame5)
search_suburb_entry_5.grid(row=2, column=1, padx=5, pady=5)

retrieve_count_listings_button = ttk.Button(frame5, text="Retrieve Count Listings", command=lambda: retrieve_count_listings(start_date_entry_5.get(), end_date_entry_5.get(), search_suburb_entry_5.get()))
retrieve_count_listings_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

# Run the GUI
app.mainloop()
