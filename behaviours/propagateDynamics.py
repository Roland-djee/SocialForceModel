#!/usr/bin/python

from propagateParameters import *
from forces import *

def propagateInTime(t, currentEntity, pedestrians, cars, walls, buildings):
    '''Propagates the motion of a single pedestrian in time using adapted RK4 method'''
    force = computeAllInteractingForces(currentEntity, pedestrians, cars, walls, buildings)
    return updatePositionAndVelocity(dt, t, currentEntity.velocity, currentEntity.position, force)

def updatePositionAndVelocity(dt, t, v, r, F):
    '''Update position and velocity'''
    r += dt * v
    v += dt * F
    return v, r