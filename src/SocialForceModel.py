#!/usr/bin/python
from __future__ import division
from math import *
import numpy as np
import scipy as sp
import sys
import matplotlib.pyplot as plt

def propagate_in_time(V_12_0, sigma, dt, t, v, v_ext, v_0, r, r_ext, r_k, r_kext):
    '''Propagates the motion of a single pedestrian in time using adapted
    RK4 method'''

    # define the force "attraction to destination"
    f_alpha0     = force_to_destination(v, v_0, r, r_k)
    # define pedestrian-pedestrian repulsive force
    f_alpha_beta = pedestrian_repulsive_force(V_12_0, sigma, dt, v_ext, r, r_ext, r_k, r_kext)

    # Attractive force to destination
    Fx = f_alpha0[0] + f_alpha_beta[0]
    Fy = f_alpha0[1] + f_alpha_beta[1]

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

def pedestrian_repulsive_force(V_12_0, sigma, dt, v_ext, r, r_ext, r_k, r_kext):
    ''' Returns the repulsive force between pedestrians'''
    F = np.zeros((len(r_ext),2))
    amplitude   = V_12_0 / sigma

    for i in range(len(r_ext)):
        b           = ellipse_semiminor_axis(dt, v_ext[i], r, r_ext[i], r_kext[i])
        n12         = desired_direction(r, r_ext[i])
        expo_factor = exp(- b / sigma)
        force = amplitude * expo_factor * n12
        F[i] = force

    return np.sum(F, axis=0)


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

def desired_direction(r_k, r_alpha):
    '''Returns the normalized vector for the desired direction'''
    #print 'r_k', r_k
    #print 'r_alpha', r_alpha
    #sys.exit()
    return (r_k - r_alpha) / np.linalg.norm(r_k - r_alpha)
    
def define_random_vector(lmax):
    ''' Returns random [x, y] coordinates between [-lmax,lmax)'''
    r = (np.random.rand(2) * 2. - 1. ) * lmax / 2.
    return r

if __name__ == '__main__':

    # world's dimension
    lmax = 50.
    # number of agents
    n_agents = 3

    # initialize arrays
    r_k   = np.zeros((n_agents,2))
    r     = np.zeros((n_agents,2)) 
    v     = np.zeros((n_agents,2)) 
    r_i   = np.zeros((n_agents,2)) 
    v_v   = np.zeros((n_agents,2)) 
    r_new = np.zeros((n_agents,2)) 
    v_new = np.zeros((n_agents,2)) 

    # define destination
    for i in range(n_agents):
        r_k[i] = define_random_vector(lmax)
        r[i]   = define_random_vector(lmax)
        v[i]   = define_random_vector(lmax)

    r_i = r
    v_i = v

    # Set parameters
    v_0    = 1.5     # Average desired speed [m/s]
    V_12_0 = 2.1     # Repulsive potential amplitude [m^2 s^-2]
    sigma  = 0.3     # Potential damping parameter [m]
    dt = 0.001       # Time spacing [s]
    t  = 0.          # Initial timing [s]
    
    time = []

    x1 = []
    y1 = []
    x2 = []
    y2 = []
    x3 = []
    y3 = []


    time.append(t)
    x1.append(r[0][0])
    y1.append(r[0][1])
    x2.append(r[1][0])
    y2.append(r[1][1])
    x3.append(r[2][0])
    y3.append(r[2][1])

    #print x1, y1
    #sys.exit()

    while t <= 20.:
        for i in range(n_agents):
            
            #v_ext1  = [v2, v3]
            r_ext  = np.delete(r, i, axis=0)
            r_kext = np.delete(r_k, i, axis=0)
            v_ext  = np.delete(v, i, axis=0)
            #print 'v_ext', v_ext
            v_new[i], r_new[i]  = propagate_in_time(V_12_0, sigma, dt, t, v[i], v_ext, v_0, r[i], r_ext, r_k[i], r_kext)
            #print 'new v', v_new
            #sys.exit()
            #r_ext1  = [r2, r3]
            #r_kext1 = [r_k2, r_k3]

        v  = v_new
        r  = r_new
        t += dt

        #sys.exit()

        time.append(t)
        x1.append(r[0][0])
        y1.append(r[0][1])
        x2.append(r[1][0])
        y2.append(r[1][1])
        x3.append(r[2][0])
        y3.append(r[2][1])



    for i in range(n_agents):
        plt.plot(r_i[i][0], r_i[i][1], 'bo')
        plt.plot(r_k[i][0], r_k[i][1], 'ro')
        plt.arrow(r_i[i][0], r_i[i][1], v_i[i][0], v_i[1][1], fc="k", ec="k", head_width=1, head_length=1)
        plt.plot(r, y1, 'r-')

    plt.axis([-lmax, lmax, -lmax, lmax])
    plt.xlabel("x distance [m]")
    plt.ylabel("y distance [m]")
    plt.grid(True)

    plt.show()



    #plt.plot(x1, y1, 'r-')
    #plt.plot(x2, y2, 'b-')
    #plt.plot(x3, y3, 'g-')
    #plt.arrow(r_i1[0], r_i1[1], v_i1[0], v_i1[1], fc="k", ec="k", head_width=1, head_length=1)
    #plt.arrow(r_i2[0], r_i2[1], v_i2[0], v_i2[1], fc="k", ec="k", head_width=1, head_length=1)
    #plt.arrow(r_i3[0], r_i3[1], v_i3[0], v_i3[1], fc="k", ec="k", head_width=1, head_length=1)
    #plt.plot(r_k1[0], r_k1[1], 'ro')
    #plt.plot(r_k2[0], r_k2[1], 'ro')
    #plt.plot(r_k3[0], r_k3[1], 'ro')
    #plt.plot(r_i1[0], r_i1[1], 'bo')
    #plt.plot(r_i2[0], r_i2[1], 'bo')
    #plt.plot(r_i3[0], r_i3[1], 'bo')
    plt.show()
