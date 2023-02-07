#! /usr/bin/env python

# Necessary Libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Generator import Generator

#################################
# Detector Class
#################################

class Detector:
    
    # Initialization method for Detector Class
    def __init__(self, seed,N=10,simtime =20, life=2.2e-6,x=10, y=10):
        self.seed = seed
        self.simtime = simtime
        self.N = N
        self.x = x
        self.y = y
        self.life = life
        self.xs = []
        self.ys = []
        self.simtimes = []
        self.lifes = []

    # Function takes values of Muon coordinate,
    # decay electron coordinate, and decay time
    def Extract(self, x):
        
        self.xs.append(x[1][0])
        self.ys.append(x[1][1])
        self.simtimes.append(x[0][0])
        self.lifes.append(x[0][1])

    def RunSimulate(self):
        Muons = Generator(self.seed)
        for i in range(self.N):
            values = Muons.Simulate(self.simtime, self.life,self.x, self.y)
            self.Extract(values)

    def animate(self, i):
        self.RunSimulate()
        plt.clf()
        for j in range(len(self.simtimes)):
            if i >= self.simtimes[j]:
                plt.scatter(self.xs[j], self.ys[j], color='red')
            elif i >= self.simtimes[j] - self.lifes[j]:
                plt.scatter(self.xs[j], self.ys[j], color='blue')
        
    def run(self):
        fig, ax = plt.subplots()
        anim = animation.FuncAnimation(fig, self.animate, frames=self.simtime, repeat=False)
        plt.show()
        writer = animation.FFMpegWriter(fps=1, bitrate=1800)
        anim.save('animation.mp4', writer=writer)



        
        