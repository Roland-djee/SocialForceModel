#!/usr/bin/python

from entities.pedestrians.pedestrianSettings import *
from propagateParameters import *
from spawners.buildingSpawner import *
from spawners.pedestrianSpawner import *
from spawners.vehicleSpawner import *
from forces import *
from matplotlib import animation
from matplotlib import pyplot as plt

from world.worldParameters import *

def propagateInTime(t, currentEntity, pedestrians, cars, walls, buildings):
    '''Propagates the motion of a single pedestrian in time using adapted RK4 method'''
    force = computeAllInteractingForces(currentEntity, pedestrians, cars, walls, buildings)
    return updatePositionAndVelocity(dt, t, currentEntity.velocity, currentEntity.position, force)

def updatePositionAndVelocity(dt, t, v, r, F):
    '''Update position and velocity'''
    r += dt * v
    v += dt * F
    return v, r