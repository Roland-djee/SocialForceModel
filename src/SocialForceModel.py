#!/usr/bin/python
from __future__ import division
from math import *
import numpy as np
import scipy as sp
import sys
import matplotlib.pyplot as plt

from spawners.buildingSpawner import *
from spawners.pedestrianSpawner import *
from spawners.vehicleSpawner import *

from behaviours.propagateDynamics import *

from mathlib.mathFunctions import *

if __name__ == '__main__':
    
    pedestrians = spawnPedestrians(nbStandardPedestrians).spawnRandomlyStandardPedestrians()
    cars        = spawnCars(nbStandardCars).spawnRandomlyStandardCars()
    
    newVelocity = np.zeros((nbStandardPedestrians,3)) 
    newPosition = np.zeros((nbStandardPedestrians,3)) 
    newVelocityCars = np.zeros((nbStandardCars,3)) 
    newPositionCars = np.zeros((nbStandardCars,3)) 
    
    for t in time:
        for currentPedestrian in range(nbStandardPedestrians):
            newVelocity[currentPedestrian], newPosition[currentPedestrian] = propagateInTime(dt, pedestrians[currentPedestrian], pedestrians, cars, walls, buildings)
        for currentPedestrian in range(nbStandardPedestrians):
            pedestrians[currentPedestrian].velocity = newVelocity[currentPedestrian] * pedestrianStopAtDestination(newPosition[currentPedestrian] - pedestrians[currentPedestrian].target)
            pedestrians[currentPedestrian].position = newPosition[currentPedestrian]
        for currentCar in range(nbStandardCars):
            newVelocityCars[currentCar], newPositionCars[currentCar] = propagateInTime(dt, cars[currentCar], pedestrians, cars, walls, buildings)
        for currentCar in range(nbStandardCars):
            cars[currentCar].velocity = newVelocityCars[currentCar] * carStopAtDestination(newPositionCars[currentCar] - cars[currentCar].target)
            cars[currentCar].position = newPositionCars[currentCar]
    
    