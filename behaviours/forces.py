#!/usr/bin/python
from __future__ import division
from math import *
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

from spawners.pedestrianSpawner import *
from pedestrianParameters.pedestrianSettings import *
from propagateParameters import *
from mathlib.ellipse import ellipseSemiMinorAxis

from mathlib.vectors import *

def computePedestrianTargetAttractiveForce(pedestrians, currentPedestrian):
    '''Returns the attractive force to a destination'''
    eAlpha  = normalisedDesiredDirection(pedestrians[currentPedestrian].target, pedestrians[currentPedestrian].position)
    vAlpha0 = eAlpha * pedestrians[currentPedestrian].desiredVelocity
    return (vAlpha0 - pedestrians[currentPedestrian].velocity) / pedestrians[currentPedestrian].relaxationTime

def computePedPedRepulsiveForce(pedestrians, currentPedestrian):
    ''' Returns the repulsive force between all other pedestrians and the current one'''
    externalVelocities, externalPositions, externalTargets, normalizedAlphaBetaVectors = extractExternalVariables(pedestrians, currentPedestrian)
    semiMinorAxes = np.array([ellipseSemiMinorAxis(dt, eV, pedestrians[currentPedestrian].position, eP, eT) for eV, eP, eT in zip(externalVelocities, externalPositions, externalTargets)]) 
    return amplitude * sum([exp(-semiMinorAxes[i]/sigma) * normalizedAlphaBetaVectors[i] for i in range(len(semiMinorAxes))])
    
def extractExternalVariables(pedestrians, currentPedestrian):
    ''' Extract the nbPedestrian-1 other variables necessary'''
    excludingPedestrian = 'Pedestrian' + str(currentPedestrian)
    externalVelocities = [pedestrian.velocity for pedestrian in pedestrians if pedestrian.id != excludingPedestrian]
    externalPositions  = [pedestrian.position for pedestrian in pedestrians if pedestrian.id != excludingPedestrian]
    externalTargets    = [pedestrian.target   for pedestrian in pedestrians if pedestrian.id != excludingPedestrian]
    normalizedAlphaBetaVectors = [normalisedDesiredDirection(pedestrians[currentPedestrian].position, externalPosition) for externalPosition in externalPositions]
    return externalVelocities, externalPositions, externalTargets, normalizedAlphaBetaVectors
    
# pedestrians      = spawnRandomPedestrians()
# print [pedestrians[i].id for i in range(10)]
# print [pedestrians[i].velocity for i in range(10)]
# print [pedestrians[i].position for i in range(10)]
# print [pedestrians[i].target for i in range(10)]
# force = computePedPedRepulsiveForce(pedestrians, 5)
# print force
    
    
#     F = np.zeros((len(r_ext),2))
#     
#     for i in range(len(r_ext)):
#         b           = ellipse_semiminor_axis(dt, v_ext[i], r, r_ext[i], r_kext[i])
#         n12         = desired_direction(r, r_ext[i])
#         expo_factor = exp(- b / sigma)
#         force       = amplitude * expo_factor * n12
#         F[i] = force
    

#     return np.sum(F, axis=0)
#     return 0. 



# def wall_repulsive_force(wall_begin, wall_end, U_0, R_0, r):
#     B      = get_closest_point_to_segment(wall_begin, wall_end, r)
#     n      = desired_direction(r, B)
#     factor = U_0 / R_0
#     expo   = exp(-np.linalg.norm(r - B) / R_0)
#     return B, factor * expo * n
#     

# 
# def force_to_destination(v, v_0, r, r_k):
#     '''Returns the attractive force to a destination'''
# 
#     # define the desired direction
#     e_alpha  = desired_direction(r_k, r)
#     # define the desired velocity
#     v_alpha0 = e_alpha * v_0
#     # relaxation time [s]
#     tau_alpha = 0.5
# 
#     return (v_alpha0 - v) / tau_alpha

#if __name__ == '__main__':
    
#    wall_begin = np.array([0.,0.])
#    wall_end   = np.array([2.,0.])

#    U_0 = 10. 
#    R_0 = 0.2


#    r1 = np.array([0.5, 1.])

#    B, f = wall_repulsive_force(wall_begin, wall_end, U_0, R_0, r1)

#    plt.arrow(wall_begin[0], wall_begin[1], wall_end[0], wall_end[1], 'blue', linewidth=4)
#    plt.plot(r1[0], r1[1], 'ro')
#    plt.plot(B[0], B[1], 'go')
#    plt.arrow(B[0], B[1], f[0] , f[1] , head_width=0.05, head_length=0.1, fc='k', ec='k')
#    plt.axis('equal')
#    plt.axis([-5, 5, -5, 5])
#    plt.show()
