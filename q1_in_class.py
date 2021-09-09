# -*- coding: utf-8 -*-
"""
This is the file I'll develop live to show an example workflow for 
Quiz #1 and its extensions.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

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

def rising_sine_function(x, amplitude, freq, phase_shift, slope, intercept):
    """
    Function to create sine superimposed on line from x data.

    Parameters
    ----------
    x : numpy array
        x-axis data for which we want to evaluate function
    slope : TYPE
        DESCRIPTION.
    intercept : TYPE
        DESCRIPTION.

    Returns
    -------
    y : TYPE
        DESCRIPTION.

    """
    
    y = amplitude*np.sin(2*np.pi*freq*x + phase_shift) + slope*x + intercept
    
    return y
    
popt, pcov = curve_fit(rising_sine_function, years, CO2_ppm_MaunaLoa)
print("Freq: {:.2f}, period: {:.2f}".format(popt[1], 1./popt[1]))

plt.plot(years, rising_sine_function(years, *popt), 'r')
    