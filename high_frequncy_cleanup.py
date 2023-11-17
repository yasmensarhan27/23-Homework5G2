"""
This code will:
1- load data form the station as dataframe
2- plot graph of the data we have
3- calculate the fft
4- filter the data
5- take ifft
6- plot the data from ifft
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def load_data(url):
    """
    Load CO2 concentration data from a given URL.
    Parameters:
    - url (str): The URL pointing to the CO2 concentration data file.
    Returns:
    - pd.DataFrame: A DataFrame containing the loaded data.
    """
    # Load the data
    df = pd.read_csv(url, delimiter="\s+", skiprows=54, names=['site', 'year', 'month', 'value'])
    return df
# URL for CO2 concentration data
url = 'https://gml.noaa.gov/aftp/data/trace_gases/co2/flask/surface/txt/co2_avi_surface-flask_1_ccgg_month.txt'
# Load data
df = load_data(url)
# Plot the raw data
plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 1)
plt.plot(df['value'][1:])
plt.title('Raw CO2 Monthly Average Data')
plt.xlabel('Time (Months)')
plt.ylabel('CO2 Concentration')
# Apply FFT to the raw data
fft_result_raw = np.fft.fft(df['value'][1:])
# Calculate the time step (assuming a regular monthly sampling)
time_step = 1  # If the data is monthly, the time step is 1 month
# Compute the corresponding frequencies in cycles per month
frequencies_per_month_raw = np.fft.fftfreq(len(fft_result_raw), d=time_step)
# Plot the raw spectrum
plt.subplot(2, 2, 3)
plt.plot(frequencies_per_month_raw, np.abs(fft_result_raw))
plt.title('Raw Frequency Spectrum')
plt.xlabel('Frequency (Cycles per Month)')
plt.ylabel('Amplitude')
# Set a threshold to identify high-frequency components
threshold = 0.01
# Zero out high-frequency components
fft_result_raw[np.abs(frequencies_per_month_raw) > threshold] = 0
# Plot the modified raw spectrum
plt.subplot(2, 2, 4)
plt.plot(frequencies_per_month_raw, np.abs(fft_result_raw))
plt.title('Modified Raw Frequency Spectrum (High-frequency components zeroed)')
plt.xlabel('Frequency (Cycles per Month)')
plt.ylabel('Amplitude')
# Apply inverse FFT to the modified raw data
cleaned_data_raw = np.fft.ifft(fft_result_raw)
# Plot the cleaned raw data with explicit time values on the x-axis
plt.subplot(2, 1, 2)
plt.plot(df['value'].index, cleaned_data_raw.real)
plt.title('Cleaned Raw CO2 Monthly Average Data')
plt.xlabel('Time (Months)')
plt.ylabel('CO2 Concentration')
plt.tight_layout()
plt.show()
