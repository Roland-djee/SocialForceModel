#!/usr/bin/python

from pedestrianParameters.pedestrianSettings import *
from buildingParameters.buildingDimensions import *
from propagateParameters import *
from spawners.buildingSpawner import *
from spawners.pedestrianSpawner import *
from forces import *

def propagateInTime(pedestrians, walls, buildings):
    '''Propagates the motion of a single pedestrian in time using adapted RK4 method'''
    
    force = computeAllInteractingForces(pedestrians, walls, buildings)
    
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
#     v_x, r_x = RK2O(dt, t, v[0], r[0], Fx)
#     # propagate in y
#     v_y, r_y = RK2O(dt, t, v[1], r[1], Fy)
#     return np.array([v_x, v_y]), np.array([r_x, r_y])

def computeAllInteractingForces(pedestrians, walls, buildings):
    pedestrianPedestrianRepulsiveForce = computePedPedRepulsiveForce(pedestrians)
#     pedestrianWallRepulsiveForce       = computePedWallRepulsiveForce()
#     pedestrianVehicleRepulsiveForce    = computePedVehicleRepulsiveForce()
#     force = pedestrianPedestrianRepulsiveForce + pedestrianWallRepulsiveForce + pedestrianVehicleRepulsiveForce
#     return force
    force = 0.
    return force

def RK2O(dt, t, v, r, F):
    '''Adapted 4th order Runge-Kutta method for second order ODEs'''
    # position
    r = r + dt * v
    # velocity
    v = v + dt * F
    return v, r

walls, buildings = spawnEnvironment()
pedestrians      = spawnRandomPedestrians()

v_new, r_new = propagateInTime(pedestrians, walls, buildings)

