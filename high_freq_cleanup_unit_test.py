"""
This code will test several processes:
1- importing data
2- fft frequency
3- filtering and padding
4-ifft and cleaned data
"""
#import the nessecary libraried to run the code
import unittest
from unittest.mock import patch, mock_open
import pandas as pd
import numpy as np
import io
from high_frequncy_cleanup import load_data
class TestCO2Analysis(unittest.TestCase):
    """
    This class will check if the data are imported correctly
    by testing the length of the data and the columns
    """
    def setUp(self):
        # Sample data for testing
        self.sample_url = 'https://gml.noaa.gov/aftp/data/trace_gases/co2/flask/surface/txt/co2_avi_surface-flask_1_ccgg_month.txt'
        self.sample_data = """site year month value
                              A    2022  1     400.0
                              A    2022  2     410.0
                              A    2022  3     420.0
                              B    2022  1     390.0
                              B    2022  2     400.0
                              B    2022  3     410.0"""
    @patch('pandas.read_csv', side_effect=pd.read_csv)
    def test_load_data(self, mock_read_csv):
        """
        test if the imported data are correct and as expecting
        1- the length
        2- the columns
        """
        # Test if data is loaded correctly
        mock_read_csv.return_value = pd.read_csv(io.StringIO(self.sample_data), 
                                                 delimiter="\s+", skiprows=54, 
                                                 names=['site', 'year', 'month', 'value'])
        df = load_data(self.sample_url)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 129)
        self.assertListEqual(list(df.columns), ['site', 'year', 'month', 'value'])
    @patch('pandas.read_csv', side_effect=pd.read_csv)
    def test_fft_and_frequency_analysis(self, mock_read_csv):
        # Test FFT and frequency analysis
        mock_read_csv.return_value = pd.read_csv(io.StringIO(self.sample_data),
                                                 delimiter="\s+", skiprows=54,
                                                 names=['site', 'year', 'month', 'value'])
        df = load_data(self.sample_url)
        fft_result_raw = np.fft.fft(df['value'])
        time_step = 1
        frequencies_per_month_raw = np.fft.fftfreq(len(fft_result_raw), d=time_step)
        # Add assertions for FFT and frequency analysis
        self.assertIsInstance(fft_result_raw, np.ndarray)
        self.assertIsInstance(frequencies_per_month_raw, np.ndarray)
        self.assertEqual(len(fft_result_raw), len(frequencies_per_month_raw))
    def test_high_frequency_component_removal(self):
        # Test high-frequency component removal
        fft_result_raw = np.fft.fft([1, 2, 3, 4, 5])
        frequencies_per_month_raw = np.fft.fftfreq(len(fft_result_raw), d=1)
        threshold = 0.01
        fft_result_raw[np.abs(frequencies_per_month_raw) > threshold] = 0
        # Add assertions for high-frequency component removal
        self.assertTrue(np.all(fft_result_raw[np.abs(frequencies_per_month_raw) > threshold] == 0))
    def test_inverse_fft_and_cleaned_data_plotting(self):
        
        # Test inverse FFT and cleaned data plotting
        fft_result_raw = np.fft.fft([1, 2, 3, 4, 5])
        time_step = 1
        frequencies_per_month_raw = np.fft.fftfreq(len(fft_result_raw), d=time_step)
        threshold = 0.01
        fft_result_raw[np.abs(frequencies_per_month_raw) > threshold] = 0
        cleaned_data_raw = np.fft.ifft(fft_result_raw)

        # Add assertions for inverse FFT and cleaned data plotting
        self.assertIsInstance(cleaned_data_raw, np.ndarray)
        self.assertEqual(len(cleaned_data_raw), len(fft_result_raw))

if __name__ == '__main__':
    unittest.main()
