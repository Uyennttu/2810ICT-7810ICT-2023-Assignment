import unittest
from unittest.mock import Mock, call
import tkinter as tk
import pandas as pd
import demo3

# Example DataFrame for Testing
test_data = {
    'id': [1, 2, 3],
    'name': ['Test1', 'Test2', 'Test3'],
    'listing_url': ['url1', 'url2', 'url3'],
    'last_scraped': ['2019-01-01', '2019-01-02', '2019-01-03'],
    'description': ['Keyword1 Description', 'Keyword2 Description', 'Other Description']
}
dataset = pd.DataFrame(test_data)


class TestSearchKeyword(unittest.TestCase):
    def setUp(self):
        self.output_text = Mock()

    def check_output_text(self, expected_text):
        """Helper function to check the output_text."""
        try:
            self.output_text.insert.assert_called_once_with(tk.END, expected_text)
        except AssertionError:
            actual_calls = self.output_text.insert.call_args_list
            raise AssertionError(f"Expected call: [call({tk.END}, {expected_text})], Actual calls: {actual_calls}")

    def test_missing_dates(self):
        demo3.search_keyword(None, '2018-01-01', ['keyword'], self.output_text)
        self.check_output_text("Please enter valid start and end dates.\n")

    def test_start_date_greater_than_end_date(self):
        demo3.search_keyword('2019-01-02', '2018-01-01', ['keyword'], self.output_text)
        self.check_output_text("Start date cannot be greater than end date.\n")

    def test_empty_keyword(self):
        demo3.search_keyword('2018-01-01', '2019-01-02', [], self.output_text)
        self.check_output_text("Please enter at least one keyword.\n")

    def test_no_matching_listings(self):
        demo3.search_keyword('2018-01-01', '2019-01-02', ['nonexistent'], self.output_text)
        self.check_output_text("No matching listings found.\n")

    def test_matching_listings(self):
        demo3.dataset = dataset
        demo3.search_keyword('2019-01-01', '2019-01-02', ['Keyword1'], self.output_text)

        expected_text = (
            "ID: 1\n"
            "Name: Test1\n"
            "URL: url1\n"
            "Last Scraped: 2019-01-01\n\n"
        )

        self.check_output_text(expected_text)


if __name__ == '__main__':
    unittest.main()

