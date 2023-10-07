import unittest
from unittest.mock import Mock
import demo1


class TestReportAllListings(unittest.TestCase):

    def setUp(self):
        self.output_text = Mock()
        self.report_button = Mock()

    def test_invalid_date_format(self):
        demo1.report_all_listings('01-10-2018', '01-10-2019', 'sydney', self.output_text, self.report_button)
        expected_error_message = "Invalid date format. Please use YYYY-MM-DD format.\n"
        self.output_text.insert.assert_called_with('end', expected_error_message)

    def test_date_range_out_of_order(self):
        demo1.report_all_listings('2019-01-10', '2018-01-01', 'sydney', self.output_text, self.report_button)
        expected_error_message = "Date range is not in order. Please check date order.\n"
        self.output_text.insert.assert_called_with('end', expected_error_message)

    def test_empty_suburb(self):
        demo1.report_all_listings('2018-01-01', '2019-01-10', '', self.output_text, self.report_button)
        expected_error_message = "Please ensure suburb field is filled.\n"
        self.output_text.insert.assert_called_with('end', expected_error_message)

    def test_no_matching_data(self):
        demo1.report_all_listings('2100-01-01', '2100-01-02', 'Toronto', self.output_text, self.report_button)
        expected_error_message = "No results found.\n"
        self.output_text.insert.assert_called_with('end', expected_error_message)


if __name__ == '__main__':
    unittest.main()
