import unittest
from unittest.mock import patch
import pandas as pd
import demo5


# The logic to test, separated from GUI code
def count_apartments(dataset, num_bedrooms, suburb):
    if 'property_type' not in dataset.columns or 'bedrooms' not in dataset.columns or 'neighbourhood' not in dataset.columns:
        raise ValueError("'property_type', 'bedrooms', or 'neighbourhood' column not found in the dataset.")

    # Ensure that the arguments are of the expected type
    if not isinstance(num_bedrooms, int) or not isinstance(suburb, str):
        raise TypeError("Invalid input: num_bedrooms must be an integer, and suburb must be a string.")

    filtered_df = dataset[
        (dataset['property_type'] == 'Apartment') &
        (dataset['bedrooms'] == num_bedrooms) &
        (dataset['neighbourhood'].str.lower() == suburb.lower())
        ]
    return len(filtered_df)


class TestApartmentCounting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a sample dataset
        data = {'property_type': ['Apartment', 'House', 'Apartment', 'Apartment'],
                'bedrooms': [2, 3, 2, 1],
                'neighbourhood': ['Sydney', 'Manly', 'Pittwater', 'Sydney']}
        cls.dataset = pd.DataFrame(data)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            count_apartments(self.dataset, 'two', 'Sydney')

    def test_non_existent_suburb(self):
        count = count_apartments(self.dataset, 2, 'NonExistentSuburb')
        self.assertEqual(count, 0, "The count for a non-existent suburb should be 0.")

    def test_non_existent_bedroom_count(self):
        count = count_apartments(self.dataset, 99, 'Sydney')
        self.assertEqual(count, 0, "The count for a non-existent bedroom count should be 0.")

    def test_zero_bedroom_apartments(self):
        count = count_apartments(self.dataset, 0, 'Sydney')
        self.assertEqual(count, 0, "The count for apartments with 0 bedrooms should be 0.")

    def test_case_insensitive_suburb_matching(self):
        count = count_apartments(self.dataset, 2, 'sydney')
        self.assertEqual(count, 1, "The function should match suburbs case-insensitively.")


if __name__ == '__main__':
    unittest.main()