#!/usr/bin/python

from entities.pedestrians.pedestrianSettings import *
from propagateDynamicsForCars import *
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

# walls, buildings = spawnEnvironment()
pedestrians = spawnPedestrians(nbStandardPedestrians).spawnRandomlyStandardPedestrians()
cars        = spawnCars(nbStandardCars).spawnRandomlyStandardCars()

# pedestrians[0].position = np.array([-5., -5., 0.])
# pedestrians[1].position = np.array([5., -5., 0.])
# 
# pedestrians[0].velocity = np.array([0., 0., 0.])
# pedestrians[1].velocity = np.array([0., 0., 0.])
# 
# 
# pedestrians[0].target = np.array([5., 5., 0.])
# pedestrians[1].target = np.array([-5., 5., 0.])

# print pedestrians[].position
# print pedestrians[].target

# figure  = plt.figure()
# axes    = plt.axes(xlim=(-worldLength, worldLength), ylim=(-worldWidth, worldWidth)) 
# for i in range(nbStandardPedestrians):
#     plt.plot(pedestrians[i].position[0], pedestrians[i].position[1], 'bo')
#     plt.plot(pedestrians[i].target[0], pedestrians[i].target[1], 'ro')
# for i in range(nbStandardCars):
#     car1 = matplotlib.patches.Ellipse((cars[i].position[0], cars[i].position[1]), cars[i].length, cars[i].width, angle=0., color=cars[i].color)
#     axes.add_patch(car1)
# plt.ion()
# plt.show()
# 
# newVelocity = np.zeros((nbStandardPedestrians,3)) 
# newPosition = np.zeros((nbStandardPedestrians,3)) 
# newVelocityCars = np.zeros((nbStandardCars,3)) 
# newPositionCars = np.zeros((nbStandardCars,3)) 
#  
# for t in time:
# # def animate(frames):
# #     t = time[frames]
#     plt.cla()
#     plt.xlim([-worldLength, worldLength])
#     plt.ylim([-worldWidth, worldWidth])
#     for currentPedestrian in range(nbStandardPedestrians):
#         newVelocity[currentPedestrian], newPosition[currentPedestrian] = propagateInTime(t, pedestrians[currentPedestrian], pedestrians, cars, walls, buildings)
#     for currentPedestrian in range(nbStandardPedestrians):
#         pedestrians[currentPedestrian].velocity = newVelocity[currentPedestrian]
#         pedestrians[currentPedestrian].position = newPosition[currentPedestrian]
#     for i in range(nbStandardPedestrians):         
#         plt.plot(pedestrians[i].position[0], pedestrians[i].position[1], 'bo')  
#         plt.plot(pedestrians[i].target[0], pedestrians[i].target[1], 'ro')     
#     for currentCar in range(nbStandardCars):
#         newVelocityCars[currentCar], newPositionCars[currentCar] = propagateInTime(t, cars[currentCar], pedestrians, cars, walls, buildings)
#     for currentCar in range(nbStandardCars):
#         cars[currentCar].velocity = newVelocityCars[currentCar]
#         cars[currentCar].position = newPositionCars[currentCar]
#         angle = acos(np.dot(cars[currentCar].velocity, np.array([1., 0., 0.]))/np.linalg.norm(cars[currentCar].velocity))
#         if (cars[currentCar].velocity[1] < 0.):
#             angle = -angle
#         car1 = matplotlib.patches.Ellipse((cars[currentCar].position[0], cars[currentCar].position[1]), 
#                                           cars[currentCar].length, cars[currentCar].width, angle=degrees(angle), color=cars[currentCar].color)
#         axes.add_patch(car1)
#            
#     plt.draw()
# #     time.sleep(0.05)
#     plt.pause(0.001)

figure       = plt.figure()
axes         = plt.axes(xlim=(-worldLength, worldLength), ylim=(-worldWidth, worldWidth)) 
pedDots,     = axes.plot([], [], 'bo')
# car1 = []
# for i in range(nbStandardCars):

carEllipses = [matplotlib.patches.Ellipse((cars[i].position[0], cars[i].position[1]), cars[i].length, cars[i].width, angle=0., color=cars[i].color) for i in range(nbStandardCars)]
for i in range(nbStandardCars):
    axes.add_patch(carEllipses[i])


# car0 = matplotlib.patches.Ellipse((cars[0].position[0], cars[0].position[1]), cars[0].length, cars[0].width, angle=0., color=cars[0].color)
# car1 = matplotlib.patches.Ellipse((cars[1].position[0], cars[1].position[1]), cars[1].length, cars[1].width, angle=0., color=cars[1].color)
# axes.add_patch(car0)
# axes.add_patch(car1)

newVelocity = np.zeros((nbStandardPedestrians,3)) 
newPosition = np.zeros((nbStandardPedestrians,3)) 
newVelocityCars = np.zeros((nbStandardCars,3)) 
newPositionCars = np.zeros((nbStandardCars,3)) 

def init():
    pedDots.set_data([], [])
    for i in range(nbStandardCars):
        carEllipses[i].set_visible(False)
    return pedDots, carEllipses
#     car0.set_visible(False)
#     car1.set_visible(False)
#     return pedDots, car0, car1

def animate(frames):
    if frames == 1:
        for i in range(nbStandardCars):
            carEllipses[i].set_visible(True)   
#         car0.set_visible(True)
#         car1.set_visible(True)
    t = time[frames]
    for currentPedestrian in range(nbStandardPedestrians):
        newVelocity[currentPedestrian], newPosition[currentPedestrian] = propagateInTime(t, pedestrians[currentPedestrian], pedestrians, cars, walls, buildings)
    for currentPedestrian in range(nbStandardPedestrians):
        pedestrians[currentPedestrian].velocity = newVelocity[currentPedestrian]
        pedestrians[currentPedestrian].position = newPosition[currentPedestrian]
    x = [pedestrians[i].position[0] for i in range(nbStandardPedestrians)]
    y = [pedestrians[i].position[1] for i in range(nbStandardPedestrians)]   
    pedDots.set_data(x, y)
    
    for currentCar in range(nbStandardCars):
        newVelocityCars[currentCar], newPositionCars[currentCar] = propagateInTime(t, cars[currentCar], pedestrians, cars, walls, buildings)
    for currentCar in range(nbStandardCars):
        cars[currentCar].velocity = newVelocityCars[currentCar]
        cars[currentCar].position = newPositionCars[currentCar]
        angle = acos(np.dot(cars[currentCar].velocity, np.array([1., 0., 0.]))/np.linalg.norm(cars[currentCar].velocity))
        if (cars[currentCar].velocity[1] < 0.):
            angle = -angle
        carEllipses[currentCar].angle  = degrees(angle)
        carEllipses[currentCar].center = (cars[currentCar].position[0], cars[currentCar].position[1])            
    return pedDots, carEllipses
#         if currentCar == 0:
#             car0.angle  = degrees(angle)
#             car0.center = (cars[currentCar].position[0], cars[currentCar].position[1])         
#         if currentCar == 1:
#             car1.angle  = degrees(angle)
#             car1.center = (cars[currentCar].position[0], cars[currentCar].position[1])            
#     return pedDots, car0, car1


anim=animation.FuncAnimation(figure, animate, init_func=init, frames=len(time), interval=20, blit=True)
# plt.show()
anim.save('pedestrian_test.mp4', bitrate=-1)
# plt.show()
# #  
print 'video ok'
