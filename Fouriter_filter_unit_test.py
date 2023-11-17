import unittest
import pandas as pd
import numpy as np
from high_frequncy_cleanup import load_data

class TestCO2DataProcessing(unittest.TestCase):

    def test_load_data(self):
        # Load the CO2 data from the URL
        url = 'https://gml.noaa.gov/aftp/data/trace_gases/co2/flask/surface/txt/co2_avi_surface-flask_1_ccgg_month.txt'
        df = load_data(url)

        # Verify that the DataFrame has the expected columns
        self.assertTrue('site' in df.columns)
        self.assertTrue('year' in df.columns)
        self.assertTrue('month' in df.columns)
        self.assertTrue('value' in df.columns)

        # Verify that the DataFrame has the expected number of rows
        self.assertEqual(len(df), 139)

    def test_filter_high_frequency_noise(self):
        # Generate some CO2 data with high-frequency noise
        time_step = 1
        frequencies_per_month = np.linspace(0, 10, 100)
        noise_amplitudes = np.random.randn(100)
        noise = noise_amplitudes * np.sin(2 * np.pi * frequencies_per_month * time_step)
        co2_data = np.sin(2 * np.pi * 0.1 * time_step) + noise

        # Apply the function to filter out high-frequency noise
        threshold = 0.01
        filtered_co2_data = filter_high_frequency_noise(co2_data, threshold, time_step)

        # Verify that the high-frequency noise has been filtered out
        high_frequency_noise_amplitude = np.max(co2_data) - np.max(filtered_co2_data)
        self.assertLess(high_frequency_noise_amplitude, 0.01)

if __name__ == '__main__':
    unittest.main()
