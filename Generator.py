#! /usr/bin/env python

# Necessary Libraries
import numpy as np
import matplotlib.pyplot as plt
import math

#################################
# Generator Class
#################################

class Generator:

    # initialization method for Random class
    def __init__(self, seed = 5555):
        self.seed = seed
        self.m_v = np.uint64(4101842887655102017)
        self.m_w = np.uint64(1)
        self.m_u = np.uint64(1)
        
        self.m_u = np.uint64(self.seed) ^ self.m_v
        self.int64()
        self.m_v = self.m_u
        self.int64()
        self.m_w = self.m_v
        self.int64()

    # function returns a random 64 bit integer
    def int64(self):
        with np.errstate(over='ignore'):
            self.m_u = np.uint64(self.m_u * np.uint64(2862933555777941757) + np.uint64(7046029254386353087))
        self.m_v ^= self.m_v >> np.uint64(17)
        self.m_v ^= self.m_v << np.uint64(31)
        self.m_v ^= self.m_v >> np.uint64(8)
        self.m_w = np.uint64(np.uint64(4294957665)*(self.m_w & np.uint64(0xffffffff))) + np.uint64((self.m_w >> np.uint64(32)))
        x = np.uint64(self.m_u ^ (self.m_u << np.uint64(21)))
        x ^= x >> np.uint64(35)
        x ^= x << np.uint64(4)
        with np.errstate(over='ignore'):
            return (x + self.m_v)^self.m_w

    # function returns a random floating point number between (0, 1) (uniform)
    def rand(self):
        return 5.42101086242752217E-20 * self.int64()

        # function returns a random double (0 to infty) according to an exponential distribution
    def Exponential(self, beta=1.):
      # make sure beta is consistent with an exponential
      if beta <= 0.:
        beta = 1.

      R = self.rand();

      while R <= 0.:
        R = self.rand()

      X = -math.log(R)*beta

      return X

    # function returns a time period for the detection
    def Time(self, simtime, life_avg = 2.2e-6):
        # Making sure the simulation time is within range
        if simtime <0:
            return 0
        factor = len(str(simtime))
        
        # time for the detection counting from first frame
        
        time1 = math.ceil(self.rand() * (10**factor))
        while time1 > simtime:
            time1 = math.ceil(self.rand() * (10**factor))
        

    
        time2 = self.Exponential(life_avg)
        return [time1,time2]

    def Cord(self, x =10, y = 10):
        if x<0 or y<0:
            return [10,10]
        
        xfactor = len(str(x))

        xr = math.ceil(self.rand() * (10**xfactor))
        while xr > x:
            xr = math.ceil(self.rand() * (10**xfactor))
        
        yfactor = len(str(y))

        yr = math.ceil(self.rand() * (10**yfactor))
        while yr > y:
            yr = math.ceil(self.rand() * (10**yfactor))

        return [xr,yr]

    def Simulate(self, simtime, life_avg, x, y):
        Cord = self.Cord(x,y)
        sim = self.Time(simtime,life_avg)
        return [sim, Cord]
