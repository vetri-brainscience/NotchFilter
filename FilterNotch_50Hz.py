#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 21:04:42 2018

@author: vetri
"""
import numpy as np
from scipy import signal
from scipy.fftpack import fft
import matplotlib.pyplot as plt
#Note: this is the second comment-added from github
#Note: only this comment was added
N=1000
fs=  1000 # Sample frequency (Hz)
Ts= 1.0/float(fs) #Sampling interval (sec)
f0 = 50.0  #Hz, Notch filter
Q = 10

t = np.linspace(0.0, N*Ts, N)
xlow = np.sin(2 * np.pi * 50 * t)
xhigh = np.sin(2 * np.pi * 100 * t)
y1 = xlow + 0.5 * xhigh
yf = fft(y1)
xf = np.linspace(0.0, 1.0/(2.0*Ts), N//2)
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))

plt.xlim([0, 120])
plt.ylim([-0.1, 1.0])
plt.grid()
plt.show()


w0 = f0/(fs/2)  # Normalized Frequency
# Design notch filter
b, a = signal.iirnotch(w0, Q)
y2 = signal.filtfilt(b, a, y1, padlen=150)
yf = fft(y2)
xf = np.linspace(0.0, 1.0/(2.0*Ts), N//2)
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))

plt.xlim([0, 120])
plt.ylim([-0.1, 1.0])
plt.grid()
plt.show()
