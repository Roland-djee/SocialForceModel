#!/usr/bin/python

from spawners.pedestrianSpawner import *
from spawners.vehicleSpawner import *

from matplotlib import pyplot as plt

import matplotlib

pedestrians = spawnPedestrians(nbStandardPedestrians).spawnRandomlyStandardPedestrians()
cars        = spawnCars(nbStandardCars).spawnRandomlyStandardCars()

figure  = plt.figure()
axes    = plt.axes(xlim=(-worldLength, worldLength), ylim=(-worldWidth, worldWidth)) 
for i in range(nbStandardPedestrians):
    plt.plot(pedestrians[i].position[0], pedestrians[i].position[1], 'bo')
    plt.plot(pedestrians[i].target[0], pedestrians[i].target[1], 'ro')
for i in range(nbStandardCars):
    car = matplotlib.patches.Ellipse((cars[i].position[0], cars[i].position[1]), cars[i].length, cars[i].width, angle=0., color=cars[i].color)
    axes.add_patch(car)
plt.show()