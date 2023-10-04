import unittest
from unittest.mock import patch
import pandas as pd
from demo2 import display_prices


class TestDisplayPrices(unittest.TestCase):

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError) as context:
            display_prices("2018/12/01", "2019/12/31", None, 5)
        self.assertEqual(str(context.exception), "Invalid date format, please enter dates in YYYY-MM-DD format.")

    def test_invalid_date_order(self):
        with self.assertRaises(ValueError) as context:
            display_prices("2019-12-31", "2018-12-01", None, 5)
        self.assertEqual(str(context.exception), "Start date cannot be greater than end date.")

    @patch("matplotlib.pyplot.subplots")
    @patch("matplotlib.backends.backend_tkagg.FigureCanvasTkAgg")
    def test_valid_dates_and_top_n(self, mock_FigureCanvasTkAgg, mock_subplots):
        dataset = pd.DataFrame({
            'last_scraped': ['2022-12-01', '2022-12-02', '2022-12-03'],
            'neighbourhood': ['Sydney', 'Manly', 'Pittwater'],
            'price': ['$300', '$200', '$100']
        })
        # setup your mocks as needed
        display_prices("2022-12-01", "2022-12-03", None, 2)
        # assert calls to your mocks as needed

    @patch("matplotlib.pyplot.subplots")
    @patch("matplotlib.backends.backend_tkagg.FigureCanvasTkAgg")
    def test_no_data_to_plot(self, mock_FigureCanvasTkAgg, mock_subplots):
        dataset = pd.DataFrame({
            'last_scraped': ['2022-12-01', '2022-12-02', '2022-12-03'],
            'neighbourhood': ['Sydney', 'Manly', 'Pittwater'],
            'price': ['$300', '$200', '$100']
        })

        display_prices("2023-12-01", "2023-12-03", None, 2)


if __name__ == '__main__':
    unittest.main()


