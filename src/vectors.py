#!/usr/bin/python
from __future__ import division
from math import *
import numpy as np
import scipy as sp
import sys
import matplotlib.pyplot as plt

def field_of_vision(e, f, phi, c):
    ''' Returns the weight factor associated with the field of vision'''
    dot_prod = np.dot(e, f)
    if (dot_prod >= np.linalg.norm(f) * cos(phi)):
        return 1
    else:
        return c

def get_closest_point_to_segment(v1, v2, vp):
    ''' Returns the coordinates of the closest point on a segment'''
    n = normalized_vector(v1, v2)
    v = vp - v1
    t = np.dot(v, n) / np.linalg.norm(v2 - v1)
    if (0. <= t <= 1.):
        return v1 + t * (v2 - v1)
    elif (t > 1.):
        return v2
    elif (t < 0.):
        return v1
    
def normalized_vector(v1, v2):
    '''Returns the normalized vector betwen two points'''
    return (v2 - v1) / np.linalg.norm(v2 - v1)

def desired_direction(r_k, r):
    '''Returns the normalized vector for the desired direction'''
    return (r_k - r) / np.linalg.norm(r_k - r)
    
def define_random_vector(lmax):
    ''' Returns random [x, y] coordinates between [-lmax,lmax)'''
    r = (np.random.rand(2) * 2. - 1. ) * lmax / 2.
    return r

#if __name__ == '__main__':
    
#    xp = 10.
#    yp = 10.

#    vp = np.array([xp,yp])
    
#    x1 = 2.
#    y1 = 5.
#    x2 = 7.
#    y2 = 9.

#    v1 = np.array([x1,y1])
#    v2 = np.array([x2,y2])

#    phi = 100 
#    phi = phi * np.pi / 180.
#    c   = 0.5

#    r   = np.array([0., 0.])
#    r_k = np.array([5., 5.])

#    e = desired_direction(r_k, r)
#    print 'e', e
#    f = np.array([0., -1.])
#    weight = field_of_vision(e, f, phi, c)
#    print weight

#    a = get_closest_point_to_segment(v1, v2, vp)

#    plt.plot(xp, yp, 'ro')
#    plt.plot(x1,y1, 'go')
#    plt.plot(x2,y2,'go')
 #   plt.plot(a[0], a[1], 'bo')
#    plt.axis('equal')
#    plt.axis([-15, 15, -15, 15])
#    plt.show()
