import unittest
from unittest.mock import patch
import pandas as pd
import demo4


class TestRetrieveCount(unittest.TestCase):

    @patch("demo4.messagebox.showerror")
    @patch("demo4.messagebox.showinfo")
    def test_retrieve_count_empty_dataset(self, mock_showinfo, mock_showerror):
        # Mocking the dataset to be empty
        demo4.dataset = pd.DataFrame()

        demo4.retrieve_count(['cleanliness'])

        mock_showerror.assert_called_once_with("Error", "The dataset is empty!")
        mock_showinfo.assert_not_called()

    @patch("demo4.messagebox.showerror")
    @patch("demo4.messagebox.showinfo")
    def test_retrieve_count_with_data(self, mock_showinfo, mock_showerror):
        # Mocking the dataset
        data = {'comments': ['The place is clean', 'Very neat and tidy', 'dirty place']}
        demo4.dataset = pd.DataFrame(data)

        # Mocking the count_label config method
        mock_count_label = unittest.mock.MagicMock()
        demo4.count_label = mock_count_label

        demo4.retrieve_count(['cleanliness'])

        mock_showerror.assert_not_called()
        mock_showinfo.assert_called_once()
        mock_count_label.config.assert_called_once_with(text="Count of listings: 2")


if __name__ == '__main__':
    unittest.main()
