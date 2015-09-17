#!/usr/bin/python
from __future__ import division
from math import *
import numpy as np
import scipy as sp

from vectors import *

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

def wall_repulsive_force():
    return
    

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
