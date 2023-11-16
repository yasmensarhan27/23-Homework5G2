import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def find_peak_frequency(data):
"""
Function takes a pandas DataFrame `data` containing a column named 'value' to represent a time series of measurements. 

Parameters:

 Data containing date and values with date assigned in years and months.
Returns:
- cycles_per_year : float
    The estimated frequency in cycles per year.
    
- cycles_per_month : float
    The estimated frequency in cycles per month.

  """  
  def find_peak_frequency(data):
    # Assuming data is a pandas DataFrame with a column 'value' containing your data
    #sample_spacing = 1
    values = data['value'].to_numpy()

    # Perform a Fast Fourier Transform (FFT) on the data
    timestep = 1 # Calculate the time step (assuming a regular monthly sampling)
    fft_result = np.fft.fft(values)
    fft_freq = np.fft.fftfreq(len(fft_result),d= timestep)  # Compute the corresponding frequencies in cycles per month
    # Set a threshold to identify high-frequency components
    threshold = 0.01
    fft_result_raw[np.abs(frequencies_per_month_raw) > threshold] = 0 # Zero out high-frequency components
    cleaned_data_raw = np.fft.ifft(fft_result_raw)


    # Find the frequency component with the highest magnitude
    peak_frequency_index = np.argmax(np.abs(cleaned_data_raw))
    peak_frequency = np.abs(fft_freq[peak_frequency_index])

    # Convert the peak frequency to useful units

    cycles_per_season = peak_frequency
    cycles_per_year = cycles_per_season * 12  # Assuming 12 months in a year

    return cycles_per_year, cycles_per_season


data = pd.read_csv('https://gml.noaa.gov/aftp/data/trace_gases/co2/flask/surface/txt/co2_mid_surface-flask_1_ccgg_month.txt', delimiter='\s+', skiprows=54, names=['site', 'year', 'month', 'value'])
peak_frequency_year, peak_frequency_month = find_peak_frequency(data)

print("Peak Frequency (Cycles per month):", peak_frequency_month)
print("Peak Frequency (Cycles per year):", peak_frequency_year)
 
