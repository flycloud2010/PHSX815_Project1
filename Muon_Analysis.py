#! /usr/bin/env python

# Necessary Libraries
import numpy as np
import matplotlib.pyplot as plt
import statistics
import sys

# User Defined Functions

def Average(lst):
    return sum(lst) / len(lst)

def BubbleSort(array):
    n = len(array)

    for i in range(n):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True

        # Start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each
        # iteration, the portion of the array that you look at
        # shrinks because the remaining items have already been
        # sorted.
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                array[j], array[j + 1] = array[j + 1], array[j]

                # Since you had to swap two elements,
                # set the `already_sorted` flag to `False` so the
                # algorithm doesn't finish prematurely
                already_sorted = False

        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        if already_sorted:
            break

if __name__ == "__main__":
   
    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)
    

    Nmeas = 10
    hypo = 0
    times1 = []
    times_avg1 = []

    need_rate = True


    with open(InputFile) as ifile:
        for line in ifile:
            if need_rate:
                need_rate = False
                rate = float(line)
                continue
        
            lineVals = line.split()
            Nmeas = len(lineVals)
            t_avg = 0
            for v in lineVals:
                t_avg += float(v)
                times1.append(float(v))

            t_avg /= Nmeas
            times_avg1.append(t_avg)

    BubbleSort(times1)
    BubbleSort(times_avg1)

    variance = statistics.variance(times1)
    q25 = np.quantile(times1, 0.25)
    q50 = np.quantile(times1, 0.5)
    q75 = np.quantile(times1, 0.75)

    variance1 = statistics.variance(times_avg1)
    q125 = np.quantile(times_avg1, 0.25)
    q150 = np.quantile(times_avg1, 0.5)
    q175 = np.quantile(times_avg1, 0.75)


    plt.hist(times1, 50, density = True, facecolor='r', alpha=0.75, label='Times')
    plt.axvline(q25, color='m', linestyle='dashed', linewidth=1, label ='Q25')
    plt.axvline(q50, color='k', linestyle='dashed', linewidth=1, label ='Q50')
    plt.axvline(q75, color='y', linestyle='dashed', linewidth=1, label ='Q75')
    plt.axvline(Average(times1), color='b', linestyle='dashed', linewidth=1, label ='Times Average')
    plt.title('Cookie Time Probability')
    plt.xlabel('Time')
    plt.ylabel('Probability')
    plt.legend()
    plt.savefig(InputFile+"Times_HistogramPlot.png")
    plt.show()
    

    plt.hist(times_avg1, 50,density = True, facecolor='g', alpha=0.75, label='Average')
    plt.axvline(q125, color='m', linestyle='solid', linewidth=1, label ='Q25')
    plt.axvline(q150, color='k', linestyle='solid', linewidth=1, label ='Q50')
    plt.axvline(q175, color='y', linestyle='solid', linewidth=1, label ='Q75')
    plt.axvline(Average(times_avg1), color='b',linestyle='solid', linewidth=1, label ='Times_avg Average')
    plt.title('Cookie Time Probability')
    plt.xlabel('Time')
    plt.ylabel('Probability')
    plt.legend()
    plt.savefig(InputFile+"Times_avg_HistogramPlot.png")
    plt.show()
    

    Out = "Hypothesis"+ InputFile
    out = open(Out, 'w')
    out.write(str(rate)+" \n")
    for e in range(0,len(times_avg1)): 
        out.write(str(times_avg1[e])+"\n")
    out.close()