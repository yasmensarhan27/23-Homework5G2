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


Bibliography

[1] [Brigham, E. O. (1974). The fast Fourier transform. Prentice-Hall](http://sar.kangwon.ac.kr/gisg/FFT_book.pdf).

[2] [Fast Fourier Transform](https://mathworld.wolfram.com/FastFourierTransform.html)

[3] [Python Numerical Methods Chapter 24](https://pythonnumericalmethods.berkeley.edu/notebooks/chapter24.03-Fast-Fourier-Transform.html)

