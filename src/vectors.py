#!/usr/bin/python
from __future__ import division
from math import *
import numpy as np
import scipy as sp

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
