#!/usr/bin/python
from __future__ import division
from math import *
import numpy as np

# set parameters
v_0    = 1.5     # Average desired speed [m/s]
V_12_0 = 2.1     # Repulsive potential amplitude [m^2 s^-2]
sigma  = 0.3     # Potential damping parameter [m]
dt     = 0.001   # Time spacing [s]
tmax   = 30.     # Maximum propagation time [s]
t      = 0.      # Initial timing [s]
time   = np.linspace(0., tmax, int(tmax/dt) + 1) # time grid

lmax   = 50.     # world's dimension
n_agents = 1     # number of agents
