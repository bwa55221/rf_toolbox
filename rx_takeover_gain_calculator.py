# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 09:53:56 2023

@author: ARDISSON

this script plots the cascaded noise figure as a function of gain, for a two device system

it intends to show the user the amount of required takeover gain needed to
adequately reduce noise figure degradation

"""

import numpy as np
import matplotlib.pyplot as plt

# dB
gain = np.arange(0, 30.5, 0.5)
nf1 = 5
nf2 = 15

# linear
linear_gain = [10**(i/10) for i in gain]
f1 = 10**(nf1/10)
f2 = 10**(nf2/10)

f_tot = [(f1 + (f2-1)/i) for i in linear_gain]

nf_tot = [10*np.log10(i) for i in f_tot]

plt.rcParams['figure.dpi'] = 400
plt.scatter(gain, nf_tot)
plt.grid()
# plt.ylim(15, 20)
plt.xlabel('Takeover Gain (dB)')
plt.ylabel('Cascaded Noise Figure (dB)')
plt.title('Analysis of Required Takeover Gain\nfor Minimum System Noise Figure Contribution')
# plt.text(12, 8, 'First Device Noise Figure = 5 dB\n\nSecond Device Noise Figure = 15 dB')
plt.show()
