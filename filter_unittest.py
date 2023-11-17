import unittest
import pandas as pd
from unittest.mock import patch
import high_frequncy_cleanup

class TestLoadData(unittest.TestCase):

    @patch('requests.get')
    def test_load_data_with_valid_url(self, mock_get):
        # Mock the response from the URL
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = """site year month value
                                            A    2022  1     400.0
                                            A    2022  2     410.0
                                            A    2022  3     420.0
                                            B    2022  1     390.0
                                            B    2022  2     400.0
                                            B    2022  3     410.0""".encode('utf-8')

        # Load the data from the mocked URL
        df = high_frequency_cleanup.load_data('https://gml.noaa.gov/aftp/data/trace_gases/co2/flask/surface/txt/co2_avi_surface-flask_1_ccgg_month.txt')

        # Assert that the loaded data is a valid pandas DataFrame
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 6)
        self.assertListEqual(list(df.columns), ['site', 'year', 'month', 'value'])
        self.assertListEqual(list(df['value']), [400.0, 410.0, 420.0, 390.0, 400.0, 410.0])

    def test_load_data_with_invalid_url(self):
        # Test if an error is raised when an invalid URL is provided
        with self.assertRaises(Exception):
            high_frequency_cleanup.load_data('invalid_url')

if __name__ == '__main__':
    unittest.main()
