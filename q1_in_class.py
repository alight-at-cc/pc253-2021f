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

CO2_unc = 5.0
#plt.plot(years, CO2_ppm_MaunaLoa)
plt.errorbar(years, CO2_ppm_MaunaLoa, yerr=5.0, errorevery=20)

fit, cov = np.polyfit(years, CO2_ppm_MaunaLoa, 1, cov=True)

fit_func = np.poly1d(fit)
plt.errorbar(years, fit_func(years), yerr=np.sqrt(cov[0,0]), errorevery=10)

plt.xlabel("Year")
plt.ylabel("$CO_2$ Concentration (ppm)")
plt.title("Mauna Loa $CO_2$ concentration increases at {:.2f} ppm/yr".format(fit[0]))