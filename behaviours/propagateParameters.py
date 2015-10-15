#!/usr/bin/python
import numpy as np

# set time-propagation parameters 
dt     = 0.01   # Time spacing [s]
tmax   = 10.     # Maximum propagation time [s]
t      = 0.      # Initial timing [s]
time   = np.linspace(0., tmax, int(tmax/dt) + 1) # time grid