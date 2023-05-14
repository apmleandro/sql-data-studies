import pandas as pd # python data manipulation and analysis library
import numpy as np #  Library with large collection of high-level mathematical functions to operate on arrays
import matplotlib.pyplot as plt #python plotting library
#import peakutils #baselining library

from scipy.optimize import curve_fit
import os # Library with operating system dependent functionality. Example: Reading data from files on the computer

#Lorentzian functions to which baseline subtracted data is fitted
# Learn more: https://lmfit.github.io/lmfit-py/builtin_models.html
def lorentzian_fcn(x, I, x0, gamma):
    return I*((gamma**2)/(((x-x0)**2)+gamma**2))
#
def two_lorentzian(x, I1, x1, gamma1, I2, x2, gamma2, y0):
    return lorentzian_fcn(x, I1, x1, gamma1) + lorentzian_fcn(x, I2, x2, gamma2) + y0

# -------- Reading data from .csv files
datafn = 'CoalChar_Hummers_33.8laser_20inttime.csv'
#bgrfn = '2019-01-09  PU012-122_bgr.csv'
data = pd.read_csv(datafn, header = 0, index_col = 0, names = ['W', 'I'])
#bgr = pd.read_csv(bgrfn, header = 0, index_col = 0, names = ['W', 'I'])

data_index = data.index.values
data_proc = (data.I.values)
data_proc = pd.DataFrame({'I': data_proc}, index = data_index)
data_proc = data_proc[800:1800]
plt.plot(data_proc)

#baseline_values = peakutils.baseline(data_proc)
#baseline_values = baseline_values.flatten()
lowval, hival = data_proc[data_proc.index.min():data_proc.index.min() + 2].values.mean(), data_proc[data_proc.index.max() - 2:data_proc.index.max()].values.mean()
low, hi = data_proc[data_proc.index.min():data_proc.index.min() + 2].index.values.mean(), data_proc[data_proc.index.max() - 2:data_proc.index.max()].index.values.mean()

y = [lowval, hival]
x = [low, hi]
m, b = np.polyfit(x, y, 1)

data_index = data_proc.index.values
data_proc = data_proc.I.values - (data_proc.index.values * m + b)
data_proc = pd.DataFrame({'I': data_proc}, index = data_index)
data_proc = data_proc[800:1800]
#data_proc = data_proc.I.values
#data_proc = pd.DataFrame({'I': data_proc-baseline_values}, index = data_index)

plt.plot(data_proc)

#Curve-fitting baseline subtracted data to lorentzian function
#I1 = Intensity peak1
#x1 = Center wavelength peak1
#gamma1 = (Full-width half-max for peak1)/2
#I2 = Intensity peak2
#x2 = Center wavelength peak2
#gamma2 = (Full-width half-max for peak2)/2
#y0 = Not sure but I guessed it to be the difference between the peak heights#

prms = [5000, 1350, 1, 6000, 1580, 0.5, 1000]    #prms = [I1, x1, gamma1, I2, x2, gamma2, y0]

#Optimal values for the prms are returned in array form via popt after lorentzian curve_fit 
popt, pcov = curve_fit(two_lorentzian, data_proc.index.values, data_proc.I.values, p0 = prms)

#Fit data is computed by passing optimal prms and x-values to two_lorentzian function
data_proc['fit'] = two_lorentzian(data_proc.index, *popt)

#G/D ratios are simply calculated by optimal_I2/optimal_I1 
ratios = popt[3]/popt[0]

# Here we plot both the baseline-subtracted data and the fit 
#plt.title('Baseline subtracted Raman-Spectra of laser processed GO thin films (spot1)')
#plt.xlabel('Wavelength (nm)')
#plt.ylabel('Intensity')


#plt.plot(data_proc)
plt.plot(data_proc.fit)

# Saving plot result
#plt.savefig('12-06-18 GO spot1 Raman.png', bbox_inches='tight')

# Quick-view of results
#plt.show()
print("The G/D ratio is", ratios)