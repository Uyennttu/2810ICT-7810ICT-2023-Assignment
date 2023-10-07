import unittest
from unittest.mock import patch, MagicMock
import demo2
from demo2 import display_prices
import pandas as pd
from datetime import datetime


class TestDisplayPrices(unittest.TestCase):

    # 1. Test for invalid date format
    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            display_prices('invalid_date', '2023-12-31', None, 5, None, None)

    # 2. Test for invalid date range (end date before start date)
    def test_invalid_date_range(self):
        with self.assertRaises(ValueError):
            display_prices('2023-12-31', '2023-01-01', None, 5, None, None)

    @patch('demo2.plt.subplots')
    @patch('demo2.FigureCanvasTkAgg')
    def test_valid_dates_and_top_n(self, mock_FigureCanvasTkAgg, mock_subplots):
        # Create a dummy frame
        mock_frame = MagicMock()
        # Create a mock subplot
        mock_subplot = MagicMock()
        # Set return values for mocked functions
        mock_subplots.return_value = (mock_subplot, MagicMock())
        # Create some dummy data
        mock_listings_df = pd.DataFrame({
            'id': [1, 2, 3],
            'neighbourhood': ['A', 'B', 'C']
        })
        mock_calendar_df = pd.DataFrame({
            'listing_id': [1, 2, 3],
            'date': [datetime(2023, 1, 1), datetime(2023, 1, 2), datetime(2023, 1, 3)],
            'price': ['$100', '$200', '$300']
        })
        # Test
        demo2.display_prices('2023-01-01', '2023-12-31', mock_frame, 5, mock_listings_df, mock_calendar_df)
        # Check if subplots are called
        mock_subplots.assert_called_once()

    # 4. Test no data to plot
    @patch('demo2.messagebox.showerror')
    def test_no_data_to_plot(self, mock_showerror):
        # Your setup seems logical. It depends on how your actual function determines there’s no data to plot.
        # Ensure that your function would indeed consider this data as "no data to plot".
        mock_listings_df = pd.DataFrame({
            'id': [1, 2, 3],
            'neighbourhood': ['A', 'B', 'C']
        })
        mock_calendar_df = pd.DataFrame({
            'listing_id': [1, 2, 3],
            'date': [datetime(2021, 1, 1), datetime(2021, 1, 2), datetime(2021, 1, 3)],
            'price': ['$100', '$200', '$300']
        })
        # Test
        display_prices('2023-01-01', '2023-12-31', None, 5, mock_listings_df, mock_calendar_df)
        # Check if error messagebox was shown
        mock_showerror.assert_called_with("Error", "No data to plot.")


if __name__ == '__main__':
    unittest.main()
