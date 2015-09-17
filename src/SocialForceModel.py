#!/usr/bin/python
from __future__ import division
from math import *
import numpy as np
import scipy as sp
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from parameters import *
from forces import *

def propagate_in_time(V_12_0, sigma, dt, t, v, v_ext, v_0, r, r_ext, r_k, r_kext, wall_begin, wall_end, U_0, R_0):
#def propagate_in_time(V_12_0, sigma, dt, t, v, v_ext, v_0, r, r_ext, r_k, r_kext):
    '''Propagates the motion of a single pedestrian in time using adapted
    RK4 method'''

    # define the force "attraction to destination"
    f_alpha0     = force_to_destination(v, v_0, r, r_k)
    # define pedestrian-pedestrian repulsive force
    f_alpha_beta = pedestrian_repulsive_force(V_12_0, sigma, dt, v_ext, r, r_ext, r_k, r_kext)
    #print 'wall_begin, wall_end, U_0, R_0, r',wall_begin, wall_end, U_0, R_0, r
    #sys.exit()

    B, f_alpha_B    = wall_repulsive_force(wall_begin, wall_end, U_0, R_0, r)
    #print f_alpha_B

    # Attractive force to destination
    Fx = f_alpha0[0] + f_alpha_beta[0] + f_alpha_B[0]
    Fy = f_alpha0[1] + f_alpha_beta[1] + f_alpha_B[1]
    #Fx = f_alpha0[0] + f_alpha_beta[0]
    #Fy = f_alpha0[1] + f_alpha_beta[1]

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



# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(j, w, z):
    #x = np.linspace(0, 2, 1000)
    #y = np.sin(2 * np.pi * (x - 0.01 * i))

    t = dt * j
    print j, w, z
    sys.exit()


    # initialize arrays
    r_k   = np.zeros((n_agents,2))
    r     = np.zeros((n_agents,2)) 
    v     = np.zeros((n_agents,2)) 
    r_i   = np.zeros((n_agents,2)) 
    v_v   = np.zeros((n_agents,2)) 
    r_new = np.zeros((n_agents,2)) 
    v_new = np.zeros((n_agents,2)) 

    x     = np.zeros((len(time)+1,n_agents))
    y     = np.zeros((len(time)+1,n_agents))

    # define destination
    for i in range(n_agents):
        r_k[i] = define_random_vector(lmax)
        r[i]   = define_random_vector(lmax)
        v[i]   = define_random_vector(lmax)
    
    # Store initial positions and velocities
    r_i = r
    v_i = v

    # Store initial posotions and velocities
    x = r_i[0][0]
    y = r_i[0][1]



    for i in range(n_agents):
        r_ext  = np.delete(r, i, axis=0)
        r_kext = np.delete(r_k, i, axis=0)
        v_ext  = np.delete(v, i, axis=0)
        v_new[i], r_new[i]  = propagate_in_time(V_12_0, sigma, dt, t, v[i], v_ext, v_0, r[i], r_ext, r_k[i], r_kext)

    # Update position and velocity
    v  = v_new
    r  = r_new

    # Store position and velocity
    x = r[0][0]
    y = r[0][1]


    #print x,y
    

    line.set_data(x, y)
    
    return line,


if __name__ == '__main__':

    # initialize arrays
    r_k   = np.zeros((n_agents,2))
    r     = np.zeros((n_agents,2)) 
    v     = np.zeros((n_agents,2)) 
    r_i   = np.zeros((n_agents,2)) 
    v_v   = np.zeros((n_agents,2)) 
    r_new = np.zeros((n_agents,2)) 
    v_new = np.zeros((n_agents,2)) 

    x     = np.zeros((len(time)+1,n_agents))
    y     = np.zeros((len(time)+1,n_agents))

    # define destination
    for i in range(n_agents):
        r_k[i] = define_random_vector(lmax)
        r[i]   = define_random_vector(lmax)
        v[i]   = define_random_vector(lmax)

    r_k[0] = [3., -1.]
    r[0]   = [-3., 2.]
    v[0]   = [0., 1.]

    # Store initial positions and velocities
    r_i = r
    v_i = v

    # Store initial posotions and velocities
    x[0] = [r_i[i][0] for i in range(n_agents)]
    y[0] = [r_i[i][1] for i in range(n_agents)]

    counter = 0
    for t in time:
        counter +=1
        for i in range(n_agents):
            r_ext  = np.delete(r, i, axis=0)
            r_kext = np.delete(r_k, i, axis=0)
            v_ext  = np.delete(v, i, axis=0)
            v_new[i], r_new[i]  = propagate_in_time(V_12_0, sigma, dt, t, v[i], v_ext, v_0, r[i], r_ext, r_k[i], r_kext, wall_begin, wall_end, U_0, R_0)
            #v_new[i], r_new[i]  = propagate_in_time(V_12_0, sigma, dt, t, v[i], v_ext, v_0, r[i], r_ext, r_k[i], r_kext)

        # Update position and velocity
        v  = v_new
        r  = r_new

        # Store position and velocity
        x[counter] = [r[i][0] for i in range(n_agents)]
        y[counter] = [r[i][1] for i in range(n_agents)]
 
 
    # Plot 
    for i in range(n_agents):
        plt.plot(r_i[i][0], r_i[i][1], 'bo')
        plt.plot(r_k[i][0], r_k[i][1], 'ro')
        plt.arrow(r_i[i][0], r_i[i][1], v_i[i][0], v_i[i][1], fc="k", ec="k", head_width=0.2, head_length=0.4)


    plt.plot([wall_begin[0], wall_end[0]], [wall_begin[1], wall_end[1]], 'black', linewidth=5)

    plt.plot(x, y, 'r-')


    plt.axis([-lmax/10, lmax/10, -lmax/10, lmax/10])
    plt.xlabel("x distance [m]")
    plt.ylabel("y distance [m]")
    plt.grid(True)

    plt.show()
    sys.exit()
    

    # First set up the figure, the axis, and the plot element we want to animate
    fig = plt.figure()
    ax = plt.axes(xlim=(-lmax/5, lmax/5), ylim=(-lmax/5, lmax/5))
    line, = ax.plot([], [], lw=2)

    w= 1
    z=10

    anim = animation.FuncAnimation(fig, animate(i,w,z), np.arange(0, 1000), init_func=init,
                               interval=20, blit=True)

    plt.show()
