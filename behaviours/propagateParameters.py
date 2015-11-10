#!/usr/bin/python
import numpy as np

# set time-propagation parameters 
dt     = 0.05   # Time spacing [s]
tmax   = 100.     # Maximum propagation time [s]
t      = 0.      # Initial timing [s]
time   = np.linspace(0., tmax, int(tmax/dt) + 1) # time grid