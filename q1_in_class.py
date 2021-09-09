# -*- coding: utf-8 -*-
"""
This is the file I'll develop live to show an example workflow for 
Quiz #1 and its extensions.
"""

import numpy as np
import matplotlib.pyplot as plt

CO2_ppm_MaunaLoa = np.load("Mauna_CO2.npy")

#each data point is 14 days after previous one
n_points = CO2_ppm_MaunaLoa.size

days = np.arange(n_points)*14
years = days/365.0 + 1981

plt.plot(years, CO2_ppm_MaunaLoa)