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
            newVelocity[currentPedestrian], newPosition[currentPedestrian] = propagateInTime(t, pedestrians[currentPedestrian], pedestrians, cars, walls, buildings)
        for currentPedestrian in range(nbStandardPedestrians):
            pedestrians[currentPedestrian].velocity = newVelocity[currentPedestrian] * pedestrianStopAtDestination(newPosition[currentPedestrian] - pedestrians[currentPedestrian].target)
            pedestrians[currentPedestrian].position = newPosition[currentPedestrian]
        for i in range(nbStandardPedestrians):         
            plt.plot(pedestrians[i].position[0], pedestrians[i].position[1], 'bo')  
            plt.plot(pedestrians[i].target[0], pedestrians[i].target[1], 'ro')     
        for currentCar in range(nbStandardCars):
            newVelocityCars[currentCar], newPositionCars[currentCar] = propagateInTime(t, cars[currentCar], pedestrians, cars, walls, buildings)
        for currentCar in range(nbStandardCars):
            cars[currentCar].velocity = newVelocityCars[currentCar] * carStopAtDestination(newPositionCars[currentCar] - cars[currentCar].target)
            cars[currentCar].position = newPositionCars[currentCar]
    
    