#!/usr/bin/python

from pedestrianParameters.pedestrianSettings import *
from buildingParameters.buildingDimensions import *
from propagateDynamicsForCars import *
from propagateParameters import *
from spawners.buildingSpawner import *
from spawners.pedestrianSpawner import *
from spawners.vehicleSpawner import *
from forces import *
from matplotlib import animation
from matplotlib import pyplot as plt

def propagateInTime(t, pedestrians, currentPedestrian, walls, buildings):
    '''Propagates the motion of a single pedestrian in time using adapted RK4 method'''
    
    force = computeAllInteractingForces(pedestrians, currentPedestrian, walls, buildings)
    
#     print V12
# 
#     e = desired_direction(r_k, r)
#     # define the force "attraction to destination"
#     f_alpha0     = force_to_destination(v, v_0, r, r_k)
#     w            = field_of_vision(e, f_alpha0, phi, c)
#     f_alpha0     = w * f_alpha0
#     # define pedestrian-pedestrian repulsive force
#     f_alpha_beta = pedestrian_repulsive_force(V12, sigma, dt, v_ext, r, r_ext, r_k, r_kext)
#     w            = field_of_vision(e, -f_alpha_beta, phi, c)
#     f_alpha_beta = w * f_alpha_beta    
# 
#     #print 'wall_begin, wall_end, U_0, R_0, r',wall_begin, wall_end, U_0, R_0, r
#     #sys.exit()
# 
#     B, f_alpha_B = wall_repulsive_force(wall_begin, wall_end, U_0, R_0, r)
#     #print f_alpha_B
#     w3           = field_of_vision(e, -f_alpha_B, phi, c)
#     f_alpha_B    = w3 * f_alpha_B
# 
#     # Attractive force to destination
#     Fx = f_alpha0[0] + f_alpha_beta[0] + f_alpha_B[0]
#     Fy = f_alpha0[1] + f_alpha_beta[1] + f_alpha_B[1]
#     #Fx = f_alpha0[0] + f_alpha_beta[0]
#     #Fy = f_alpha0[1] + f_alpha_beta[1]
# 
#     # propagate in x
    v_x, r_x = RK2O(dt, t, pedestrians[currentPedestrian].velocity[0], pedestrians[currentPedestrian].position[0], force[0])
#     # propagate in y
    v_y, r_y = RK2O(dt, t, pedestrians[currentPedestrian].velocity[1], pedestrians[currentPedestrian].position[1], force[1])
    return np.array([v_x, v_y, 0.]), np.array([r_x, r_y, 0.])

def computeAllInteractingForces(pedestrians, currentPedestrian, walls, buildings):
    pedestrianTargetAttractiveForce    = computePedestrianTargetAttractiveForce(pedestrians, currentPedestrian)
    pedestrianPedestrianRepulsiveForce = computePedPedRepulsiveForce(pedestrians, currentPedestrian)
#     pedestrianPedestrianRepulsiveForce = np.array([0., 0., 0.])
#     print pedestrianPedestrianRepulsiveForce
#     sys.exit()
#     pedestrianWallRepulsiveForce       = computePedWallRepulsiveForce()
#     pedestrianVehicleRepulsiveForce    = computePedVehicleRepulsiveForce()
#     force = pedestrianPedestrianRepulsiveForce + pedestrianWallRepulsiveForce + pedestrianVehicleRepulsiveForce
#     return force
#     print pedestrianPedestrianRepulsiveForce
    force = pedestrianTargetAttractiveForce + pedestrianPedestrianRepulsiveForce
    return force

def RK2O(dt, t, v, r, F):
    '''Update position and velocity'''
    r += dt * v
    v += dt * F
    return v, r

def extractPosition(pedestrians):
    ''' Extract the nbPedestrian-1 other variables necessary'''
    x = [pedestrian.position[0] for pedestrian in pedestrians]
    y = [pedestrian.position[1] for pedestrian in pedestrians]
    return (np.array(x)), (np.array(y))

def extractTarget(pedestrians):
    ''' Extract the nbPedestrian-1 other variables necessary'''
    x = [pedestrian.target[0] for pedestrian in pedestrians]
    y = [pedestrian.target[1] for pedestrian in pedestrians]
    return (np.array(x)), (np.array(y))

# walls, buildings = spawnEnvironment()
pedestrians = spawnRandomPedestrians()
# cars        = spawnRandomCars()

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

figure  = plt.figure()
axes    = plt.axes(xlim=(-worldLength, worldLength), ylim=(-worldWidth, worldWidth)) 
for i in range(nbStandardPedestrians):
    plt.plot(pedestrians[i].position[0], pedestrians[i].position[1], 'bo')
    plt.plot(pedestrians[i].target[0], pedestrians[i].target[1], 'ro')
#     x, y = extractPosition(pedestrians)
#     xT, yT = extractTarget(pedestrians)
# scatter = axes.scatter(x, y, color='red')
# scatter = axes.scatter(xT, yT, color='blue')
for i in range(nbStandardCars):
    car1 = matplotlib.patches.Ellipse((cars[i].position[0], cars[i].position[1]), cars[i].length, cars[i].width, angle=0., color=cars[i].color)
    axes.add_patch(car1)
plt.xlim([-worldLength, worldLength])
plt.ylim([-worldWidth, worldWidth])
plt.ion()
plt.show()
# 
# sys.exit()
# 
newVelocity = np.zeros((nbStandardPedestrians,3)) 
newPosition = np.zeros((nbStandardPedestrians,3)) 
newVelocityCars = np.zeros((nbStandardCars,3)) 
newPositionCars = np.zeros((nbStandardCars,3)) 
 
for t in time:
    plt.cla()
    for currentPedestrian in range(nbStandardPedestrians):
        newVelocity[currentPedestrian], newPosition[currentPedestrian] = propagateInTime(t, pedestrians, currentPedestrian, walls, buildings)
    for currentPedestrian in range(nbStandardPedestrians):
        pedestrians[currentPedestrian].velocity = newVelocity[currentPedestrian]
        pedestrians[currentPedestrian].position = newPosition[currentPedestrian]
#     x, y = extractPosition(pedestrians)
#     positions = np.array([x, y])
#     scatter.set_offsets(positions.transpose())
    for i in range(nbStandardPedestrians):  
        plt.plot(pedestrians[i].position[0], pedestrians[i].position[1], 'bo')  
     
    for currentCar in range(nbStandardCars):
        newVelocityCars[currentCar], newPositionCars[currentCar] = propagateInTimeCars(t, cars, currentCar, walls, buildings)
#         print newVelocity[currentCar], newPosition[currentCar]
    for currentCar in range(nbStandardCars):
        cars[currentCar].velocity = newVelocityCars[currentCar]
        cars[currentCar].position = newPositionCars[currentCar]
        angle = acos(np.dot((cars[currentCar].target-cars[currentCar].position), np.array([1., 0., 0.]))/np.linalg.norm(cars[currentCar].target-cars[currentCar].position))
#         print angle
#         
#         if ((cars[currentCar].target[1] - cars[currentCar].position[1]) < 0.):
#             angle = -angle
        car1 = matplotlib.patches.Ellipse((cars[currentCar].position[0], cars[currentCar].position[1]), 
                                          cars[currentCar].length, cars[currentCar].width, angle=degrees(angle), color=cars[currentCar].color)
        axes.add_patch(car1)
     
     
     
     
    plt.draw()
#     time.sleep(0.05)
    plt.pause(0.001)

# figure  = plt.figure()
# axes    = plt.axes(xlim=(-worldLength, worldLength), ylim=(-worldWidth, worldWidth)) 
# for i in range(nbStandardCars):
#     car1 = matplotlib.patches.Ellipse((cars[i].position[0], cars[i].position[1]), cars[i].length, cars[i].width, angle=0., color=cars[i].color)
#     axes.add_patch(car1)
# plt.xlim([-worldLength, worldLength])
# plt.ylim([-worldWidth, worldWidth])
# plt.ion()
# plt.show()
# 
# # sys.exit()
# 
# newVelocity = np.zeros((nbStandardPedestrians,3)) 
# newPosition = np.zeros((nbStandardPedestrians,3)) 
# 
# for t in time:
#     for currentCar in range(nbStandardCars):
#         newVelocity[currentCar], newPosition[currentCar] = propagateInTime(t, cars, currentCar, walls, buildings)
#     for currentCar in range(nbStandardCars):
#         cars[currentCar].velocity = newVelocity[currentCar]
#         cars[currentCar].position = newPosition[currentCar]
#         car1 = matplotlib.patches.Ellipse((cars[currentCar].position[0], cars[currentCar].position[1]), cars[currentCar].length, cars[currentCar].width, angle=0., color=cars[currentCar].color)
#         axes.add_patch(car1)
#     plt.draw()
#     plt.pause(0.001)
# #      
# # anim=animation.FuncAnimation(figure, animate, frames=len(time), interval=10, blit=True)
# # anim.save('pedestrian.mp4', bitrate=-1)
# #  
# # print 'video ok'
