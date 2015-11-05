#!/usr/bin/python

nbStandardPedestrians = 2

# set parameters for pedestrian-pedestrian repulsive forces from [Helbing & Molnar Phys. Rev. E 51, 4282 (1995)]
v0        = 1.5         # Average desired speed [m/s]
tauAlpha  = 0.5         # Relaxation time [s]
V12       = 2.1         # Repulsive potential amplitude [m^2 s^-2]
sigma     = 0.3         # Potential damping parameter [m]
amplitude = V12 / sigma # Pedestrian-pedestrian repulsive force amplitude [m^-1 s^-2]
