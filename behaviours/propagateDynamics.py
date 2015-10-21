#!/usr/bin/python

from pedestrianParameters.pedestrianSettings import *
from buildingParameters.buildingDimensions import *
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
    '''Adapted 4th order Runge-Kutta method for second order ODEs'''
    # position
    r = r + dt * v
    # velocity
    v = v + dt * F
    return v, r

def extractPosition(pedestrians):
    ''' Extract the nbPedestrian-1 other variables necessary'''
    x = [pedestrian.position[0] for pedestrian in pedestrians]
    y = [pedestrian.position[1] for pedestrian in pedestrians]
    return (np.array(x)), (np.array(y))

# walls, buildings = spawnEnvironment()
pedestrians = spawnRandomPedestrians()
cars        = spawnRandomCars()

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
# axes    = plt.axes(xlim=(-10, 10), ylim=(-10, 10)) 
x, y = extractPosition(pedestrians)
scatter = axes.scatter(x, y, color='red')
for i in range(nbStandardCars):
    car1 = matplotlib.patches.Ellipse((cars[i].position[0], cars[i].position[1]), cars[i].length, cars[i].width, angle=0., color=cars[i].color)
    axes.add_patch(car1)
    
plt.xlim([-worldLength, worldLength])
plt.ylim([-worldWidth, worldWidth])
plt.show()

sys.exit()

newVelocity = np.zeros((nbStandardPedestrians,3)) 
newPosition = np.zeros((nbStandardPedestrians,3)) 

# def animate(frame):
#     t = time[frame]
#     for currentPedestrian in range(nbStandardPedestrians):
#         newVelocity[currentPedestrian], newPosition[currentPedestrian] = propagateInTime(t, pedestrians, currentPedestrian, walls, buildings)
#     for currentPedestrian in range(nbStandardPedestrians):
#         pedestrians[currentPedestrian].velocity = newVelocity[currentPedestrian]
#         pedestrians[currentPedestrian].position = newPosition[currentPedestrian]
#     x, y = extractPosition(pedestrians)
#     positions = np.array([x, y])
#     scatter.set_offsets(positions.transpose())
#     return scatter
#     
# anim=animation.FuncAnimation(figure, animate, frames=len(time), interval=10, blit=True)
# anim.save('pedestrian.mp4', bitrate=-1)
# 
# print 'video ok'
