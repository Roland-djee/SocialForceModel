#!/usr/bin/python
from __future__ import division
from math import *
import numpy as np

# set parameters
v_0    = 1.5     # Average desired speed [m/s]
V_12_0 = 2.1     # Repulsive potential amplitude [m^2 s^-2]
sigma  = 0.3     # Potential damping parameter [m]
dt     = 0.001   # Time spacing [s]
tmax   = 10.     # Maximum propagation time [s]
t      = 0.      # Initial timing [s]
time   = np.linspace(0., tmax, int(tmax/dt) + 1) # time grid

lmax   = 100.     # worldParameters's dimension
n_agents = 1     # number of agents

wall_begin = np.array([-1.,0.]) # Wall beginning corrdinates
wall_end   = np.array([2.,1.]) # Wall end coordinates

U_0 = 10.        # Wall repulsive potential amplitude [m^2 s^2]
R_0 = 0.2        # Wall damping parameter [m]

phi = 100        # Field of vision acceptance angle [degrees] 
phi = phi * np.pi / 180. # [radians]
c   = 0.5        # Damping parameter

