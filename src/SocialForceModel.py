#!/usr/bin/python
from __future__ import division
from math import *
import numpy as np
import scipy as sp
import sys
import matplotlib.pyplot as plt

def propagate_in_time(dt, t, v, v_0, r, r_k):

    # define the force "attraction to destination"
    f_alpha0 = force_to_destination(v, v_0, r, r_k)

    # Attractive force to destination
    Fx = f_alpha0[0]
    Fy = f_alpha0[1]
    #Fx = -1.
    #Fy = 1.

    # propagate in x
    v_x, r_x = RK2O(dt, t, v[0], r[0], Fx)
    # propagate in y
    v_y, r_y = RK2O(dt, t, v[1], r[1], Fy)
    return np.array([v_x, v_y]), np.array([r_x, r_y])

def RK2O(dt, t, v, r, F):
    '''Adapted 4th order Runge-Kutta method for second order ODEs'''

    # position
    r = r + dt * v
    # velocity
    v = v + dt * F

    return v, r

def force_to_destination(v, v_0, r, r_k):
    '''Returns the attractive force to a destination'''

    # define the desired direction
    e_alpha  = desired_direction(r_k, r)
    # define the desired velocity
    v_alpha0 = e_alpha * v_0
    # relaxation time [s]
    tau_alpha = 0.5

    return (v_alpha0 - v) / tau_alpha

def desired_direction(r_k, r_alpha):
    '''Returns the normalized vector for the desired direction'''
    return (r_k - r_alpha) / np.linalg.norm(r_k - r_alpha)
    
def define_random_vector(lmax):
    ''' Returns random [x, y] coordinates between [-lmax,lmax)'''
    r = (np.random.rand(2) * 2. - 1. ) * lmax / 2.
    return r

if __name__ == '__main__':

    # world's dimension
    lmax = 50.

    # random shortest path
    r_k = define_random_vector(lmax)
    #print r_k

    # Initial position
    r_i = define_random_vector(lmax)
    v_i = define_random_vector(lmax)
    #print r_0

    # Average desired speed [m/s]
    v_0 = 1.5

    # Inital conditions 
    r  = np.array(r_i)
    v  = np.array(v_i) 
    dt = 0.001
    t  = 0.
    
    time = []
    x1 = []
    y1 = []

    time.append(t)
    x1.append(r[0])
    y1.append(r[1])

    #print x1, y1
    #sys.exit()

    while t <= 100.:
        v, r = propagate_in_time(dt, t, v, v_0, r, r_k)
        t = t + dt
        
        time.append(t)
        x1.append(r[0])
        y1.append(r[1])
        
    plt.plot(x1, y1)
    plt.arrow(r_i[0], r_i[1], v_i[0], v_i[1], fc="k", ec="k",
head_width=1, head_length=1)
    plt.plot(r_k[0], r_k[1], 'ro')
    plt.plot(r_i[0], r_i[1], 'bo')
    plt.axis([-lmax, lmax, -lmax, lmax])
    plt.xlabel("x distance [m]")
    plt.ylabel("y distance [m]")
    plt.grid(True)
    plt.show()
