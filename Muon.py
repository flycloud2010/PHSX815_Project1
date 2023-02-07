#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np
import matplotlib.pyplot as plt
# import our Generator class file
sys.path.append(".")
from Generator import Generator

# main function for Muon simulator
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number]" % sys.argv[0])
        sys.exit(1)

    # default seed print(test.Simulate(20,2.2e-6,10,10))
    seed = 5555

    # default simulation time. 
    simtime = 20

    #default events
    events = 10000

    # default Muon lifetime
    life = 2.2e-6

    # default detector size
    x = 10
    y = 10
    # output file defaults
    doOutputFile = False

    # read the user-provided seed from the command line (if there)
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
    if '-life' in sys.argv:
        p = sys.argv.index('-life')
        life = float(sys.argv[p+1])
        
    if '-events' in sys.argv:
        p = sys.argv.index('-sim')
        simtim = int(sys.argv[p+1])
        
    if '-x' in sys.argv:
        p = sys.argv.index('-x')
        x = int(sys.argv[p+1])

    if '-y' in sys.argv:
        p = sys.argv.index('-y')
        y = int(sys.argv[p+1])
        
    if '-output' in sys.argv:
        p = sys.argv.index('-output')
        OutputFileName = sys.argv[p+1]
        doOutputFile = True

    # class instance of our Random class using seed
    Muons = Generator(seed)

    #Lists to store values
    xcoord=[]
    ycoord=[]
    decay_times=[]
    detection=[]

    for i in range(events):
        values = Muons.Simulate(simtime, life, x,y)
        xcoord.append(values[1][0])
        ycoord.append(values[1][1])
        detection.append(values[0][0])
        decay_times.append(values[0][1])
    
    plt.hist(decay_times,  50, facecolor='r', alpha=0.75, label='Decay Events')

    # plot formating options
    plt.xlabel('Decay Times')
    plt.ylabel('Events')
    plt.title('Muon Lifetime')
    plt.grid(True)
    plt.legend()
    #ax = plt.gca()
    #ax.set_ylim([0.8, 1.2])
    # show figure (program only ends once closed
    plt.show()
    plt.savefig("MuonDecay_Histogram.png")


    # Writing to a file
    f = open("Simulation_Data.csv", "w")
    f.write("Event Number,Lifetime,X_Pos, Y_Pos, Time of Detection\n")
    for i in range(events):
        f.write(i,',',decay_times[i],',',xcoord[i],',',ycoord[i],',',detection[i],'\n')

    f.close()
