import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def find_peak_frequency(data):
    # Assuming data is a pandas DataFrame with a column 'value' containing data
    sample_spacing = 1
    values = data['value'].to_numpy()

    # Perform a Fast Fourier Transform (FFT) on the data
    fft_result = np.fft.fft(values)
    fft_freq = np.fft.fftfreq(len(values), d=sample_spacing)  # Frequency values corresponding to FFT result

    # Find the frequency component with the highest magnitude
    peak_frequency_index = np.argmax(np.abs(fft_result))
    peak_frequency = np.abs(fft_freq[peak_frequency_index])

    # Convert the peak frequency to useful units
    cycles_per_month = peak_frequency
    cycles_per_year = cycles_per_month * 12 #Multiply by 12 for monthly data

    return cycles_per_year, cycles_per_month

data = pd.read_csv(''https://gml.noaa.gov/aftp/data/trace_gases/co2/flask/surface/txt/co2_avi_surface-flask_1_ccgg_month.txt',delimiter='\s+',skiprows = 54, names = ['site','year','month','value'])
peak_frequency_year, peak_frequency_month = find_peak_frequency(data)

print("Peak Frequency (Cycles per month):", peak_frequency_month)
print("Peak Frequency (Cycles per year):", peak_frequency_year)
