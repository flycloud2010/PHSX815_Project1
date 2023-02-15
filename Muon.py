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
    Nmeas = 20

    #default events
    Nexp = 10000

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
        p = sys.argv.index('-Nexp')
        Nexp = int(sys.argv[p+1])
        
    if '-meas' in sys.argv:
        p = sys.argv.index('-Nmeas')
        Nmeas = int(sys.argv[p+1])

        
    if '-output' in sys.argv:
        p = sys.argv.index('-output')
        OutputFileName = sys.argv[p+1]
        doOutputFile = True

    # class instance of our Random class using seed
    Muons = Generator(seed)

    if doOutputFile:
        outfile = open(OutputFileName, 'w')
        outfile.write(str(life)+" \n")
        for e in range(0,Nexp):
            for t in range(0,Nmeas):
                outfile.write(str(test.Simulate(20,rate1,10,10))+" ")
            outfile.write(" \n")
        outfile.close()
