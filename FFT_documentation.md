# Fourier Transform:

Difference between FFT and DFT:
The Fast Fourier Transform (FFT) is a mathematical algorithm that computes the Discrete Fourier Transform (DFT) of a sequence in a fast and efficient manner. 
The DFT is a transformation that decomposes a sequence into its constituent frequencies. 

## Background

The DFT is defined as follows:

$$X[k] = \sum_{n=0}^{N-1} x[n] * exp(-2{\pi}ikn/N)$$ [1](http://sar.kangwon.ac.kr/gisg/FFT_book.pdf)
where:

X[k] is the kth Fourier coefficient
x[n] is the nth input sample
N is the length of the input sequence
The DFT can be computed directly using the above formula, but this is a computationally expensive process. The FFT is an algorithm that computes the DFT in a much more efficient manner.

## Algorithm

The FFT is based on the Cooley-Tukey algorithm[2](https://mathworld.wolfram.com/FastFourierTransform.html)
, which is a recursive algorithm that decomposes the DFT into a series of smaller DFTs. The Cooley-Tukey algorithm is based on the following identity:

$$X[k] = X[k0] + W^N * X[k0 + N/2]$$ [1](http://sar.kangwon.ac.kr/gisg/FFT_book.pdf) 
where:

W is the complex exponential exp(-2πi/N)
k0 is an integer between 0 and N/2
The FFT algorithm uses this identity to recursively decompose the DFT into a series of smaller DFTs. The smaller DFTs are then computed using a direct implementation of the DFT formula.

## Applications [1](http://sar.kangwon.ac.kr/gisg/FFT_book.pdf)

The FFT is a powerful algorithm that has a wide variety of applications. It is an essential tool for signal processing, image processing, and scientific computing.

The FFT is used in a wide variety of applications, including:

Signal processing: The FFT is used to analyze and process signals, such as audio and speech signals.
Image processing: The FFT is used to analyze and process images, such as filtering and compressing images.
Scientific computing: The FFT is used to solve a wide variety of scientific computing problems, such as solving differential equations and simulating physical systems.

# Process:
## Code explanation:
### Frquency:
--------------
Step 1: Import Libraries and Load Data
The code starts by importing the necessary libraries, namely numpy and pandas. It then loads the CO2 concentration data from a NOAA website into a pandas DataFrame named data.

Step 2: Define Function to Find Peak Frequency
A function named ```find_peak_frequency()``` is defined to identify the dominant frequency in the time series data. It takes a pandas DataFrame data containing a 'value' column representing the time series.

Step 3: Perform Fast Fourier Transform (FFT)
The function extracts the 'value' column from the DataFrame and converts it to a NumPy array. It then performs an FFT on the time series data using the ```np.fft.fft()``` function. The FFT converts the data from the time domain to the frequency domain, where periodic variations can be identified.

Step 4: Compute Frequencies and Filter High-Frequency Components
The function calculates the time step, assumed to be 1 month for monthly data, and computes the corresponding frequencies in cycles per month using ```np.fft.fftfreq()```. It then sets a threshold to identify high-frequency components in the spectrum. The amplitudes of frequencies above the threshold are set to zero, effectively removing high-frequency noise from the data.

Step 5: Apply Inverse FFT and Find Peak Frequency
The function applies the inverse FFT (IFFT) to the filtered frequency data using ```np.fft.ifft()```, converting it back to the time domain. It then finds the frequency component with the highest magnitude using ```np.argmax()``` and calculates the corresponding frequency in cycles per year.

Step 6: Return Peak Frequency
The function returns the estimated peak frequency in cycles per year, representing the dominant periodicity in the time series data.

Step 7: Apply Function to Data and Print Peak Frequency
The function ```find_peak_frequency()``` is applied to the loaded data data, and the estimated peak frequency in cycles per year is stored in the variable cycles_per_year. Finally, the peak frequency is printed to the console with a descriptive message.

### filtering:
---------------
Step 1: Load Data from URL
The code starts with a function ```load_data()``` that takes a URL as input and returns a pandas DataFrame containing the CO2 concentration data. The function reads the data from the specified URL, skipping the first 54 rows, and parses the data into a DataFrame with columns for 'site', 'year', 'month', and 'value'.

Step 2: Load Data and Plot Raw Data
The code then defines the URL for the CO2 concentration data and calls the ```load_data()``` function to load the data into a DataFrame named df. It then creates a figure and subplots for displaying the raw data. The raw data is plotted as a time series with time (in months) on the x-axis and CO2 concentration on the y-axis.

Step 3: Apply FFT and Calculate Time Step
The code next applies the Fast Fourier Transform (FFT) to the raw CO2 concentration data using the ```np.fft.fft()``` function. The FFT converts the time series data into the frequency domain, where periodic variations in the data can be identified. The time step, assumed to be 1 month for monthly data, is calculated.

Step 4: Compute Frequencies and Plot Raw Spectrum
The code computes the corresponding frequencies in cycles per month using the ```np.fft.fftfreq()``` function. The raw spectrum, representing the amplitudes of the frequencies, is plotted with frequency on the x-axis and amplitude on the y-axis.

Step 5: Set Threshold and Zero Out High-Frequency Components
A threshold value is set to identify high-frequency components in the spectrum. The code then sets the amplitudes of frequencies above the threshold to zero, effectively removing high-frequency noise from the data.

Step 6: Plot Modified Raw Spectrum and Apply Inverse FFT
The modified raw spectrum, with high-frequency components removed, is plotted to visualize the filtered data in the frequency domain. The inverse FFT (IFFT) is applied to the modified raw spectrum using the ```np.fft.ifft()``` function. The IFFT converts the filtered frequency data back into the time domain.

Step 7: Plot Cleaned Raw Data
The cleaned raw data, obtained from the IFFT, is plotted as a time series with explicit time values on the x-axis and CO2 concentration on the y-axis. This represents the smoothed CO2 concentration data after removing high-frequency noise.


## Plots and graphs:

![Unknown-6](https://github.com/yasmensarhan27/23-Homework5G2/assets/38404107/38af2d25-d3eb-437d-81d5-d48d2b4f29fe)
![Unknown-7](https://github.com/yasmensarhan27/23-Homework5G2/assets/38404107/7a79fbe5-42bd-4573-8358-d7f85b4c3fa7)

## Linting and Unit test:
The Unit test successfully passed with some warnings.
<img width="883" alt="Screen Shot 2023-11-17 at 4 29 02 AM" src="https://github.com/yasmensarhan27/23-Homework5G2/assets/38404107/e21b5edc-4fea-4152-bef7-1edc825ca237">

The linting after fixing trials reached 8.69/10:

<img width="415" alt="Screen Shot 2023-11-17 at 4 43 13 AM" src="https://github.com/yasmensarhan27/23-Homework5G2/assets/38404107/2fbf1f50-da91-488e-894b-1fb8b76fe0d8">

## Bibliography

[1] [Brigham, E. O. (1974). The fast Fourier transform. Prentice-Hall](http://sar.kangwon.ac.kr/gisg/FFT_book.pdf).

[2] [Fast Fourier Transform](https://mathworld.wolfram.com/FastFourierTransform.html)

[3] [Python Numerical Methods Chapter 24](https://pythonnumericalmethods.berkeley.edu/notebooks/chapter24.03-Fast-Fourier-Transform.html)

