#!/usr/bin/python
from __future__ import division
from math import *
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

from vectors_cars import *

def pedestrian_repulsive_force(V_12_0, sigma, dt, v_ext, r, r_ext, r_k, r_kext):
    ''' Returns the repulsive force between pedestrians'''
    F = np.zeros((len(r_ext),2))
    amplitude   = V_12_0 / sigma

    for i in range(len(r_ext)):
        b           = ellipse_semiminor_axis(dt, v_ext[i], r, r_ext[i], r_kext[i])
        n12         = desired_direction(r, r_ext[i])
        expo_factor = exp(- b / sigma)
        force       = amplitude * expo_factor * n12
        F[i] = force

    return np.sum(F, axis=0)

def wall_repulsive_force(wall_begin, wall_end, U_0, R_0, r):
    B      = get_closest_point_to_segment(wall_begin, wall_end, r)
    n      = desired_direction(r, B)
    factor = U_0 / R_0
    expo   = exp(-np.linalg.norm(r - B) / R_0)
    return B, factor * expo * n
    
def ellipse_semiminor_axis(dt, v_ext, r, r_ext, r_kext):
    ''' Returns the semiminor axis of the ellipse force field defined 
    in the repulsive social force'''
    r12    = r - r_ext
    b      = np.linalg.norm(r12)
    e_beta = desired_direction(r_kext, r_ext)
    v_beta = np.linalg.norm(v_ext) * dt
    b      = b + np.linalg.norm(r12 - v_beta * e_beta)
    b      = sqrt(b**2 - v_beta**2) * 0.5
    return b

def force_to_destination(v, v_0, r, r_k):
    '''Returns the attractive force to a destination'''

    # define the desired direction
    e_alpha  = desired_direction(r_k, r)
    # define the desired velocity
    v_alpha0 = e_alpha * v_0
    # relaxation time [s]
    tau_alpha = 0.5

    return (v_alpha0 - v) / tau_alpha

#if __name__ == '__main__':
    
#    wall_begin = np.array([0.,0.])
#    wall_end   = np.array([2.,0.])

#    U_0 = 10. 
#    R_0 = 0.2


#    r1 = np.array([0.5, 1.])

#    B, f = wall_repulsive_force(wall_begin, wall_end, U_0, R_0, r1)

#    plt.arrow(wall_begin[0], wall_begin[1], wall_end[0], wall_end[1], 'blue', linewidth=4)
#    plt.plot(r1[0], r1[1], 'ro')
#    plt.plot(B[0], B[1], 'go')
#    plt.arrow(B[0], B[1], f[0] , f[1] , head_width=0.05, head_length=0.1, fc='k', ec='k')
#    plt.axis('equal')
#    plt.axis([-5, 5, -5, 5])
#    plt.show()
