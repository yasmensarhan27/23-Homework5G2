"""
This code will test the main moduke peak_frequency
1- creating a sample data set and check the frequency for a valid data
2- Create a sample dataset with high-frequency noise and test the frequency
3- Mock the fftfreq function to return a specific set of frequeies 
"""
import unittest
from unittest.mock import patch
import pandas as pd
import numpy as np
from peak_frequency import find_peak_frequency
class FindPeakFrequencyTest(unittest.TestCase):
    """
    This class contains 3 function
    to test the main module peak_frequency.py
    """
    def test_find_peak_frequency_with_valid_data(self):
        """
        test the sample data set
        calculate the fequency and compare it to the expected one
        """
        # Create a sample dataset
        data = pd.DataFrame({'year': np.linspace(1990, 2000, 65),
                             'month': np.linspace(0, 1, 65),
                             'value': np.sin(2 * np.pi * 10 * np.linspace(0, 1, 65))})
        # Calculate the expected peak frequency
        expected_cycles_per_year = 3.0
        # Calculate the actual peak frequency
        actual_cycles_per_year = find_peak_frequency(data)
        # Assert that the actual peak frequency matches the expected peak frequency
        self.assertEqual(actual_cycles_per_year, expected_cycles_per_year)
    def test_find_peak_frequency_with_high_frequency_noise(self):
        """
        create sample datset with high noise
        calculate the fequency and compare it to the expected one
        """
        # Create a sample dataset with high-frequency noise
        data = pd.DataFrame({'year': [2021, 2021, 2021],
                             'month': [1, 2, 3],
                             'value': [395.78, 396.15, 397.38 + np.random.normal(0, 0.1)]})
        # Calculate the expected peak frequency
        expected_cycles_per_year = 0.0
        # Calculate the actual peak frequency
        actual_cycles_per_year = find_peak_frequency(data)
        # Assert that the actual peak frequency matches the expected peak frequency
        self.assertEqual(actual_cycles_per_year, expected_cycles_per_year)
    @patch('numpy.fft.fftfreq')
    def test_find_peak_frequency_with_mocked_fftfreq(self, mock_fftfreq):
        """
        mock the fftfreq and return the value in array
        calculate the fequency and compare it to the expected one
        """
        # Mock the fftfreq function to return a specific set of frequencies
        mock_fftfreq.return_value = np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
        # Create a sample dataset
        data = pd.DataFrame({'year': [2021, 2021, 2021],
                             'month': [1, 2, 3],
                             'value': [395.78, 396.15, 397.38]})
        # Calculate the expected peak frequency
        expected_cycles_per_year = 0.0
        # Calculate the actual peak frequency
        actual_cycles_per_year = find_peak_frequency(data)
        # Assert that the actual peak frequency matches the expected peak frequency
        self.assertEqual(actual_cycles_per_year, expected_cycles_per_year)
if __name__ == '__main__':
    unittest.main()
