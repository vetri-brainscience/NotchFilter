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

N=1000
fs= 1000 # Sample frequency (Hz)
Ts= 1.0/float(fs)
f050 = 50.0  #Hz, Notch filter
f0100= 100.0
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


w050 = f050/(fs/2)  # Normalized Frequency
# Design notch filter
b50, a50 = signal.iirnotch(w050, Q)
y2 = signal.filtfilt(b50, a50, y1, padlen=150)
yf = fft(y2)

w0100 = f0100/(fs/2)  # Normalized Frequency
# Design notch filter
b100, a100 = signal.iirnotch(w0100, Q)
y3 = signal.filtfilt(b100, a100, y2, padlen=150)
yf = fft(y3)

xf = np.linspace(0.0, 1.0/(2.0*Ts), N//2)
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))

plt.xlim([0, 120])
plt.ylim([-0.1, 1.0])
plt.grid()
plt.show()
