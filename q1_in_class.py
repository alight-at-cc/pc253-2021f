# -*- coding: utf-8 -*-
"""
This is the file I'll develop live to show an example workflow for 
Quiz #1 and its extensions.
"""

import numpy as np
import matplotlib.pyplot as plt

CO2_ppm_MaunaLoa = np.load("Mauna_CO2.npy")

plt.plot(CO2_ppm_MaunaLoa)