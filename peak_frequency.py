"""
This code will perform:
1- the fast fourier transform to the data
3- take the output from the cleaned and filtered data
(removes the first peak at zero to get some reasonable frequency of the data)
2- choose the best peak for the frequency calculation
"""
# import the necessary libraries to run the code
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#import data from the chosen noaa station
data = pd.read_csv('https://gml.noaa.gov/aftp/data/trace_gases/co2/flask/surface/txt/co2_avi_surface-flask_1_ccgg_month.txt',
                   delimiter="\s+", skiprows=54, names=['site', 'year', 'month', 'value'])
def find_peak_frequency(data):
    """
    Function takes a pandas DataFrame `data`
    containing a column named 'value' to represent a time series of measurements. 
    Parameters:
    - data : pandas DataFrame
        Data containing date and values with date assigned in years and months.
    Returns:
    - cycles_per_year : float
        The estimated frequency in cycles per year.
    """
    values = data['value'][1:].to_numpy()
    # Perform a Fast Fourier Transform (FFT) on the data
    timestep = 1  # Calculate the time step (assuming a regular monthly sampling)
    fft_result = np.fft.fft(values)
    # Compute the corresponding frequencies in cycles per month
    fft_freq = np.fft.fftfreq(len(fft_result), d=timestep)
    # Set a threshold to identify high-frequency components
    threshold = 0.01
    for index, value in enumerate(fft_result):
        if np.abs(fft_freq[index]) > threshold:
            fft_result[index] = 0
    #fft_result[np.abs(fft_freq) > threshold] = 0  # Zero out high-frequency components
    cleaned_data = np.fft.ifft(fft_result)
    # Find the frequency component with the highest magnitude
    peak_frequency_index = np.argmax(np.abs(cleaned_data))
    peak_frequency = np.abs(fft_freq[peak_frequency_index])
    # Convert the peak frequency to useful units
    cycles_per_year = peak_frequency * 12  # Assuming 12 months in a year
    return cycles_per_year
#apply the find_frequency peak function to the data
cycles_per_year = find_peak_frequency(data)
# print the frequency in reasonable unit
print("Peak Frequency (Cycles per year):", cycles_per_year)
