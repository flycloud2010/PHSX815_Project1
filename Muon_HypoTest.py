#! /usr/bin/env python

# Necessary Libraries
import numpy as np
import matplotlib.pyplot as plt
import statistics
import sys


#Files to Import
Hypo1 = "HypothesisLife_2p2.txt"
Hypo2 = "HypothesisLife_2p7.txt"

#Storing the values
times1 =[]
times2 =[]
need_rate1 = True
need_rate2 = True
with open(Hypo1) as ifile:
    for line in ifile:
        if need_rate1:
            need_rate1 = False
            rate1 = float(line)
            continue
        
        lineVals = line.split()
        Nmeas = len(lineVals)
        for v in lineVals:
            times1.append(float(v))

with open(Hypo2) as ifile:
    for line in ifile:
        if need_rate2:
            need_rate2 = False
            rate2 = float(line)
            continue
        
        lineVals = line.split()
        Nmeas = len(lineVals)
        
        for v in lineVals:
            
            times2.append(float(v))

# Calculating the Confidence Intervals

mean1 = np.mean(times1)
std_dev1 = np.std(times1)
sigma_11 = (mean1 - std_dev1, mean1 + std_dev1)
sigma_21 = (mean1 - 2*std_dev1, mean1 + 2*std_dev1)
sigma_31 = (mean1 - 3*std_dev1, mean1 + 3*std_dev1)

mean2 = np.mean(times2)
std_dev2 = np.std(times2)
sigma_12 = (mean2 - std_dev2, mean2 + std_dev2)
sigma_22 = (mean2 - 2*std_dev2, mean2 + 2*std_dev2)
sigma_32 = (mean2 - 3*std_dev2, mean2 + 3*std_dev2)

from scipy import stats
ci = stats.t.interval(0.95, df= len(times1)-1, loc=mean1, scale=stats.sem(times1))
c2 = stats.t.interval(0.95, df= len(times2)-1, loc=mean2, scale=stats.sem(times2))

plt.hist(times1,50,facecolor = 'r', label="H_0")
plt.hist(times2,50,facecolor='g', label="H_1")
plt.title('Muon Decay Time - Distinguishable')
plt.xlabel('Decay Time')
plt.ylabel('Probability')
plt.axvline(mean1, color='k', linestyle='--', label='H0_mean')
plt.axvline(ci[0], color='r', linestyle='--', label='95% CI H0')
plt.axvline(ci[1], color='r', linestyle='--')
#plt.axvline(sigma_11[0], color='r', linestyle='--', label='1-sigma')
#plt.axvline(sigma_11[1], color='r', linestyle='--')
#plt.axvline(sigma_21[0], color='g', linestyle='--', label='2-sigma')
#plt.axvline(sigma_21[1], color='g', linestyle='--')
#plt.axvline(sigma_31[0], color='b', linestyle='--', label='3-sigma')
#plt.axvline(sigma_31[1], color='b', linestyle='--')
plt.axvline(mean2, color='k', linestyle='-', label='H1_mean')
plt.axvline(c2[0], color='b', linestyle='-', label='95% CI H1')
plt.axvline(c2[1], color='b', linestyle='-')
#plt.axvline(sigma_12[0], color='r', linestyle='-')
#plt.axvline(sigma_12[1], color='r', linestyle='-')
#plt.axvline(sigma_22[0], color='g', linestyle='-')
#plt.axvline(sigma_22[1], color='g', linestyle='-')
#plt.axvline(sigma_32[0], color='b', linestyle='-')
#plt.axvline(sigma_32[1], color='b', linestyle='-')
plt.legend()
plt.show()