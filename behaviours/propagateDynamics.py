#!/usr/bin/python

from pedestrianParameters.pedestrianSettings import *
from buildingParameters.buildingDimensions import *
from propagateParameters import *
from spawners.buildingSpawner import *
from spawners.pedestrianSpawner import *
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
    force = pedestrianTargetAttractiveForce + pedestrianPedestrianRepulsiveForce
    return force

def RK2O(dt, t, v, r, F):
    '''Adapted 4th order Runge-Kutta method for second order ODEs'''
    # position
    r = r + dt * v
    # velocity
    v = v + dt * F
    return v, r

# walls, buildings = spawnEnvironment()
pedestrians      = spawnRandomPedestrians()
currentPedestrian = 5

print pedestrians[currentPedestrian].velocity, pedestrians[currentPedestrian].position
print pedestrians[currentPedestrian].target

figure  = plt.figure()
axes    = plt.axes(xlim=(-worldLength, worldLength), ylim=(-worldWidth, worldWidth)) 
for i in range(nbStandardPedestrians):
    scatter = axes.scatter(pedestrians[i].position[0], pedestrians[i].position[1], color=pedestrians[i].color)
# scatter = plt.plot(pedestrians[currentPedestrian].target[0], pedestrians[currentPedestrian].target[1])
scatter = axes.scatter(pedestrians[currentPedestrian].target[0], pedestrians[currentPedestrian].target[1], color='red')
# scatter, = plt.plot([], [])
# scatter
# plt.show()
# sys.exit()

# def init():
# #     scatter.set_data(pedestrians[currentPedestrian].position[0], pedestrians[currentPedestrian].position[1])
#     scatter = axes.scatter(pedestrians[currentPedestrian].position[0], pedestrians[currentPedestrian].position[1])  
#     return scatter

def animate(frame):
#     updatePositions(pedestrians)
    t = time[frame]
    pedestrians[currentPedestrian].velocity, pedestrians[currentPedestrian].position = propagateInTime(t, pedestrians, currentPedestrian, walls, buildings)
    newPosition = (pedestrians[currentPedestrian].position[0], pedestrians[currentPedestrian].position[1])
    scatter.set_offsets(newPosition)
    return scatter
    
anim=animation.FuncAnimation(figure, animate, frames=len(time), interval=100, blit=True)
# anim.save('pedestrian.mp4', bitrate=-1, extra_args=['libx264'])
anim.save('pedestrian.mp4', bitrate=-1)
# plt.show()
print 'video ok'

sys.exit()

for t in time:
    pedestrians[currentPedestrian].velocity, pedestrians[currentPedestrian].position = propagateInTime(pedestrians, currentPedestrian, walls, buildings)
    print pedestrians[currentPedestrian].velocity, pedestrians[currentPedestrian].position

