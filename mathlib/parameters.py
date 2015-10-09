#!/usr/bin/python
from __future__ import division
from math import *
import numpy as np




lmax   = 100.     # worldParameters's dimension
n_agents = 1     # number of agents

wall_begin = np.array([-1.,0.]) # Wall beginning corrdinates
wall_end   = np.array([2.,1.]) # Wall end coordinates



phi = 100        # Field of vision acceptance angle [degrees] 
phi = phi * np.pi / 180. # [radians]
c   = 0.5        # Damping parameter

