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
    #print 'f12', f_alpha_beta
    #sys.exit()
    f_alpha_beta = [0., 0.]
    #sys.exit()

    # Attractive force to destination
    Fx = f_alpha0[0] + f_alpha_beta[0]
    Fy = f_alpha0[1] + f_alpha_beta[1]
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

def pedestrian_repulsive_force(V_12_0, sigma, dt, v_ext, r, r_ext, r_k, r_kext):
    ''' Returns the repulsive force between pedestrians'''
    F = []
    F_final = []
    #F_final = np.array([])


    print 'r'
    print r

    print 'r_ext'
    print r_ext

    for i in range(len(r_ext)):
        #print i
        b           = ellipse_semiminor_axis(dt, v_ext[i], r, r_ext[i], r_kext[i])
        #print b
        amplitude   = V_12_0 / sigma
        #print amplitude 
        expo_factor = exp(- b / sigma)
        #print expo_factor
        n12         = desired_direction(r, r_ext[i])
        F.append(amplitude * expo_factor * n12)
    
    #print 'F', F[0][0]
    #sys.exit()

    F_final.append(F[0][0] + F[1][0])
    F_final.append(F[0][1] + F[1][1])
    
    #print 'F_final', F_final
    #sys.exit()

    return np.array(F_final)


def ellipse_semiminor_axis(dt, v_ext, r, r_ext, r_kext):
    ''' Returns the semiminor axis of the ellipse force field defined 
    in the repulsive social force'''
    r12    = r_ext - r
    b      = np.linalg.norm(r12)
    print 'r12', r12
    #print 'r_ext, r_kext',r_ext, r_kext
    e_beta = desired_direction(r_ext, r_kext)
    v_beta = np.linalg.norm(v_ext) * dt
    b      = b + np.linalg.norm(r12 - v_beta * dt * e_beta)
    #print 'b', b
    #print 'v_beta', v_beta
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

    # random shortest path or destination
    r_k1 = define_random_vector(lmax)
    r_k2 = define_random_vector(lmax)
    r_k3 = define_random_vector(lmax)

    # defined destination
    #r_k1 = [10., 10.]
    #r_k2 = [-10., 10]
    #r_k2 = r_k1
    #r_k2 = r_k1
    #r_k3 = [10., -10.]
    #print r_k

    # Random initial position and velocity
    r_i1 = define_random_vector(lmax)
    v_i1 = define_random_vector(lmax)
    r_i2 = define_random_vector(lmax)
    v_i2 = define_random_vector(lmax)
    r_i3 = define_random_vector(lmax)
    v_i3 = define_random_vector(lmax)
    print r_i1, r_i2, r_i3
    print v_i1, v_i2, v_i3
    

    # Defined intial position and velocity
    #r_i1 = [-10, -10]
    #v_i1 = [0., 0.]
    #v_i1 = [0., 0.]
    #r_i2 = [10., -10.]
    #v_i2 = [0., 0.]
    #v_i2 = [0., 0.]
    #r_i3 = [0., 0.]
    #v_i3 = [0., 5.]
    #v_i3 = [0., 0.]

    # Average desired speed [m/s]
    v_0    = 1.5
    # Repulsive potential amplitude [m^2 s^-2] 
    V_12_0 = 2.1
    #V_12_0 = 5.
    # Potential damping parameter [m]
    sigma  = 0.3
    #sigma = 0.01

    # Inital conditions 
    r1  = np.array(r_i1)
    v1  = np.array(v_i1) 
    r2  = np.array(r_i2)
    v2  = np.array(v_i2) 
    r3  = np.array(r_i3)
    v3  = np.array(v_i3) 
    dt = 0.001
    t  = 0.
    
    time = []
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    x3 = []
    y3 = []


    time.append(t)
    x1.append(r1[0])
    y1.append(r1[1])
    x2.append(r2[0])
    y2.append(r2[1])
    x3.append(r3[0])
    y3.append(r3[1])

    #print x1, y1
    #sys.exit()

    while t <= 50.:
        v_ext1  = [v2, v3]
        r_ext1  = [r2, r3]
        r_kext1 = [r_k2, r_k3]
        v1, r1  = propagate_in_time(V_12_0, sigma, dt, t, v1, v_ext1, v_0, r1, r_ext1, r_k1, r_kext1)
        v_ext2  = [v1,v3]
        r_ext2  = [r1,r3]
        r_kext2 = [r_k1, r_k3]
        v2, r2 = propagate_in_time(V_12_0, sigma, dt, t, v2, v_ext2, v_0, r2, r_ext2, r_k2, r_kext2)
        v_ext3 = [v1,v2]
        r_ext3 = [r1,r2]
        r_kext3 = [r_k1, r_k2]
        v3, r3 = propagate_in_time(V_12_0, sigma, dt, t, v3, v_ext3, v_0, r3, r_ext3, r_k3, r_kext3)
        t = t + dt

        sys.exit()
        
        time.append(t)
        x1.append(r1[0])
        y1.append(r1[1])
        x2.append(r2[0])
        y2.append(r2[1])
        x3.append(r3[0])
        y3.append(r3[1])

    #print y2
    #sys.exit()

        
    plt.plot(x1, y1, 'r-')
    plt.plot(x2, y2, 'b-')
    plt.plot(x3, y3, 'g-')
    plt.arrow(r_i1[0], r_i1[1], v_i1[0], v_i1[1], fc="k", ec="k", head_width=1, head_length=1)
    plt.arrow(r_i2[0], r_i2[1], v_i2[0], v_i2[1], fc="k", ec="k", head_width=1, head_length=1)
    plt.arrow(r_i3[0], r_i3[1], v_i3[0], v_i3[1], fc="k", ec="k", head_width=1, head_length=1)
    plt.plot(r_k1[0], r_k1[1], 'ro')
    plt.plot(r_k2[0], r_k2[1], 'ro')
    plt.plot(r_k3[0], r_k3[1], 'ro')
    plt.plot(r_i1[0], r_i1[1], 'bo')
    plt.plot(r_i2[0], r_i2[1], 'bo')
    plt.plot(r_i3[0], r_i3[1], 'bo')
    plt.axis([-lmax, lmax, -lmax, lmax])
    plt.xlabel("x distance [m]")
    plt.ylabel("y distance [m]")
    plt.grid(True)
    plt.show()
