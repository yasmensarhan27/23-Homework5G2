import unittest
import pandas as pd
import numpy as np
from unittest.mock import patch
from peak_frequency import find_peak_frequency

class FindPeakFrequencyTest(unittest.TestCase):

    def test_find_peak_frequency_with_valid_data(self):
        # Create a sample dataset
        data = pd.DataFrame({'year': [2021, 2021, 2021],
                             'month': [1, 2, 3],
                             'value': [395.78, 396.15, 397.38]})

        # Calculate the expected peak frequency
        expected_cycles_per_year = 1.0

        # Calculate the actual peak frequency
        actual_cycles_per_year = find_peak_frequency(data)

        # Assert that the actual peak frequency matches the expected peak frequency
        self.assertEqual(actual_cycles_per_year, expected_cycles_per_year)

    def test_find_peak_frequency_with_high_frequency_noise(self):
        # Create a sample dataset with high-frequency noise
        data = pd.DataFrame({'year': [2021, 2021, 2021],
                             'month': [1, 2, 3],
                             'value': [395.78, 396.15, 397.38 + np.random.normal(0, 0.1)]})

        # Calculate the expected peak frequency
        expected_cycles_per_year = 1.0

        # Calculate the actual peak frequency
        actual_cycles_per_year = find_peak_frequency(data)

        # Assert that the actual peak frequency matches the expected peak frequency
        self.assertEqual(actual_cycles_per_year, expected_cycles_per_year)

    @patch('numpy.fft.fftfreq')
    def test_find_peak_frequency_with_mocked_fftfreq(self, mock_fftfreq):
        # Mock the fftfreq function to return a specific set of frequencies
        mock_fftfreq.return_value = np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])

        # Create a sample dataset
        data = pd.DataFrame({'year': [2021, 2021, 2021],
                             'month': [1, 2, 3],
                             'value': [395.78, 396.15, 397.38]})

        # Calculate the expected peak frequency
        expected_cycles_per_year = 0.2

        # Calculate the actual peak frequency
        actual_cycles_per_year = find_peak_frequency(data)

        # Assert that the actual peak frequency matches the expected peak frequency
        self.assertEqual(actual_cycles_per_year, expected_cycles_per_year)

if __name__ == '__main__':
    unittest.main()
