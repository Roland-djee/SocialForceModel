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
    '''4th order Runge-Kutta method for second order ODEs'''

    dt2 = dt * 0.5 
    k1  = v
    k1  = dt * k1
    k2  = v
    k2  = dt * k2
    k3  = v
    k3  = dt * k3
    k4  = v
    k4  = dt * k4
    r   = r + (k1 + 2.*(k2 + k3) + k4) / 6.

    k1  = F
    k1  = dt * k1
    k2  = F
    k2  = dt * k2
    k3  = F
    k3  = dt * k3
    k4  = F
    k4  = dt * k4
    v   = v + (k1 + 2.*(k2 + k3) + k4) / 6.
    return v, r

def f_r(t, v):
    ''' Sets the ODE on the position to be solved by RK4'''
    return v

def f_v(t, F):
    ''' Sets the ODE on the velocity to be solved by RK4'''
    return F

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
    return np.array((r_k - r_alpha) / abs(r_k - r_alpha))
    
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
    r_0 = define_random_vector(lmax)
    #print r_0

    # Average desired speed [m/s]
    v_0 = 1.5

    # Inital conditions 
    r  = np.array(r_0)
    v  = np.array([0., -10.]) 
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
    plt.plot(r_k[0], r_k[1], 'ro')
    plt.plot(r_0[0], r_0[1], 'bo')
    plt.axis([-lmax, lmax, -lmax, lmax])
    plt.xlabel("x distance [m]")
    plt.ylabel("y distance [m]")
    plt.grid(True)
    plt.show()
