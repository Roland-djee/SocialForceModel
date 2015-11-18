#!/usr/bin/python

from spawners.pedestrianSpawner import *
from spawners.vehicleSpawner import *

from matplotlib import pyplot as plt
import matplotlib

from behaviours.propagateParameters import *
from behaviours.propagateDynamics import *

from world.worldParameters import *

from mathlib.mathFunctions import *

nbStandardPedestrians = 20
nbStandardCars = 0

bottomLeftStartArea = np.array([5., 5., 0.])
upperRightStartArea = np.array([10., 10., 0.])
bottomLeftEndArea = np.array([-15., 5., 0.])
upperRightEndArea = np.array([-10., 10., 0.])

pedestrians = spawnPedestrians(nbStandardPedestrians).spawnStandardPedestriansInArea(bottomLeftStartArea, upperRightStartArea, bottomLeftEndArea, upperRightEndArea)

bottomLeftStartArea = np.array([5., 15., 0.])
upperRightStartArea = np.array([10., 20., 0.])
bottomLeftEndArea = np.array([-15., 15., 0.])
upperRightEndArea = np.array([-10., 20., 0.])

cars        = spawnCars(nbStandardCars).spawnStandardCarsInArea(bottomLeftStartArea, upperRightStartArea, bottomLeftEndArea, upperRightEndArea)

figure  = plt.figure()
axes    = plt.axes(xlim=(-worldLength, worldLength), ylim=(-worldWidth, worldWidth)) 
for i in range(nbStandardPedestrians):
    plt.plot(pedestrians[i].position[0], pedestrians[i].position[1], 'bo')
    plt.plot(pedestrians[i].target[0], pedestrians[i].target[1], 'ro')
for i in range(nbStandardCars):
    car = matplotlib.patches.Ellipse((cars[i].position[0], cars[i].position[1]), cars[i].length, cars[i].width, angle=0., color=cars[i].color)
    axes.add_patch(car)
plt.ion()
plt.show()
# sys.exit()

newVelocity = np.zeros((nbStandardPedestrians,3)) 
newPosition = np.zeros((nbStandardPedestrians,3)) 
newVelocityCars = np.zeros((nbStandardCars,3)) 
newPositionCars = np.zeros((nbStandardCars,3)) 

walls = 0.
buildings = 0.

for t in time:
    plt.cla()
    plt.xlim([-worldLength, worldLength])
    plt.ylim([-worldWidth, worldWidth])
    for currentPedestrian in range(nbStandardPedestrians):
        newVelocity[currentPedestrian], newPosition[currentPedestrian] = propagateInTime(dt, pedestrians[currentPedestrian], pedestrians, cars, walls, buildings)
    for currentPedestrian in range(nbStandardPedestrians):
        pedestrians[currentPedestrian].updateVelocity(newVelocity[currentPedestrian])
        if (np.linalg.norm(newPosition[currentPedestrian] - pedestrians[currentPedestrian].target) < pedestrianStopAcceptance):
            pedestrians[currentPedestrian].updatePosition(pedestrians[currentPedestrian].origin)
        else:
            pedestrians[currentPedestrian].updatePosition(newPosition[currentPedestrian])
    for i in range(nbStandardPedestrians):         
        plt.plot(pedestrians[i].position[0], pedestrians[i].position[1], 'bo')  
        plt.plot(pedestrians[i].target[0], pedestrians[i].target[1], 'ro')    
         
    for currentCar in range(nbStandardCars):
        newVelocityCars[currentCar], newPositionCars[currentCar] = propagateInTime(dt, cars[currentCar], pedestrians, cars, walls, buildings)
    for currentCar in range(nbStandardCars):
        cars[currentCar].updateVelocity(newVelocityCars[currentCar])
        if (np.linalg.norm(newPositionCars[currentCar] - cars[currentCar].target) < carStopAcceptance):
            cars[currentCar].updatePosition(cars[currentCar].origin)
        else:
            cars[currentCar].updatePosition(newPositionCars[currentCar])
        angle = acos(np.dot(cars[currentCar].velocity, np.array([1., 0., 0.]))/np.linalg.norm(cars[currentCar].velocity))
        if (cars[currentCar].velocity[1] < 0.):
            angle = -angle
        car = matplotlib.patches.Ellipse((cars[currentCar].position[0], cars[currentCar].position[1]), 
                                          cars[currentCar].length, cars[currentCar].width, angle=degrees(angle), color=cars[currentCar].color)
        axes.add_patch(car)

    newVelocity = np.zeros((nbStandardPedestrians,3)) 
    newPosition = np.zeros((nbStandardPedestrians,3)) 
    newVelocityCars = np.zeros((nbStandardCars,3)) 
    newPositionCars = np.zeros((nbStandardCars,3)) 
               
    plt.draw()
    plt.pause(0.001)