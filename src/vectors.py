#!/usr/bin/python
from __future__ import division
from math import *
import numpy as np
import scipy as sp
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def get_closest_point_to_segment(v1, v2, vp):
    
    n = normalized_vector(v1, v2)
    v = vp - v1
    t = np.dot(v, n) / np.linalg.norm(v2 - v1)
    #t = np.dot(v, n)
    print t

    q = v1 + t * (v2 - v1)

    print q
    return q

def normalized_vector(v1, v2):
    '''Returns the normalized vector betwen two points'''
    return (v2 - v1) / np.linalg.norm(v2 - v1)


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
    
    xp = 1.
    yp = 8.

    vp = np.array([xp,yp])
    
    x1 = 2.
    y1 = 5.
    x2 = 7.
    y2 = 9.

    v1 = np.array([x1,y1])
    v2 = np.array([x2,y2])

    a = get_closest_point_to_segment(v1, v2, vp)

    plt.plot(xp, yp, 'ro')
    plt.plot(x1,y1, 'go')
    plt.plot(x2,y2,'go')
    plt.plot(a[0], a[1], 'bo')
    plt.axis('equal')
    plt.axis([-15, 15, -15, 15])
    plt.show()
