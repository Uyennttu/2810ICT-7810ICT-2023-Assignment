import unittest
from unittest.mock import patch, Mock
import pandas as pd
from demo3 import search_keyword


class TestSearchKeyword(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up class-level resources (runs once per class)."""
        cls.mock_listings_data = pd.DataFrame({
            'id': [1],
            'description': ['test'],
            'name': ['Test Name'],
            'listing_url': ['http://test.url']
        })
        cls.mock_calendar_data = pd.DataFrame({
            'listing_id': [1],
            'date': [pd.Timestamp('2023-01-01')],
        })

    def setUp(self):
        """Set up common test resources (runs before each test method)."""
        self.output_text = Mock()

    def run_search_keyword(self, start_date, end_date, keyword):
        """Helper method to run search_keyword and handle common mock setups."""
        with patch('demo3.calendar_dataset', autospec=True) as mock_calendar, \
                patch('demo3.listings_dataset', autospec=True) as mock_listings:
            mock_listings.return_value = self.mock_listings_data
            mock_calendar.return_value = self.mock_calendar_data

            return search_keyword(start_date, end_date, keyword, self.output_text)

    def test_input_validations(self):
        """Test input validation scenarios."""
        test_cases = [
            (None, None, ['key'], ValueError, "Missing dates"),
            ('2023-12-31', '2023-01-01', ['key'], ValueError, "Start date after end date"),
            ('2023-01-01', '2023-12-31', [], ValueError, "Empty keyword"),
        ]

        for start_date, end_date, keyword, expected_exception, msg in test_cases:
            with self.subTest(msg=msg), self.assertRaises(expected_exception):
                self.run_search_keyword(start_date, end_date, keyword)

    def test_no_matching_list(self):
        """Test scenario where no listings match the keyword."""
        self.run_search_keyword('2023-01-01', '2023-12-31', ['non-existent-key'])

        self.output_text.delete.assert_called_once_with(1.0, "end")
        self.output_text.insert.assert_called_once_with("end", "No matching listings found.\n")

    def test_matching_list(self):
        """Test scenario where listings match the keyword."""
        self.run_search_keyword('2023-01-01', '2023-12-31', ['test'])

        self.output_text.delete.assert_called_once_with(1.0, "end")
        self.output_text.insert.assert_called_once_with(
            "end",
            "ID: 1\nName: Test Name\nURL: http://test.url\nDate: 2023-01-01 00:00:00\nDescription: test\n\nDisplaying 1 of 1 matching listings."
        )


if __name__ == "__main__":
    unittest.main()
