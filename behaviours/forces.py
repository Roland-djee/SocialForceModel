#!/usr/bin/python
from __future__ import division
from math import *
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

from spawners.pedestrianSpawner import *
from spawners.vehicleSpawner import *
from entities.pedestrians.pedestrianSettings import *
from propagateParameters import *
from mathlib.ellipse import ellipseSemiMinorAxis, radiusOfEllipse

from mathlib.vectors import *

def computeCarTargetAttractiveForce(cars, currentCar):
    '''Returns the attractive force to a destination'''
    eAlpha  = normalisedDesiredDirection(cars[currentCar].target, cars[currentCar].position)
    vAlpha0 = eAlpha * cars[currentCar].desiredVelocity
    return (vAlpha0 - cars[currentCar].velocity) / cars[currentCar].relaxationTime

def computeCarCarRepulsiveForce(cars, currentCar):
    ''' Returns the repulsive force between all other cars and the current one, discarding the form factor [Anvari et al.]'''
    externalVelocities, externalPositions, externalTargets, externalIds, normalizedAlphaBetaVectors = extractExternalVariablesForCars(cars, currentCar)
    radiusesOfEllipses = np.array([radiusOfEllipse(cars[currentCar].position, cars[currentCar].target, eP, cars[currentCar].length, cars[currentCar].width) for eP in externalPositions]) 
#     print radiusesOfEllipses
    radiusesOfEllipsesFromExternalCars = [radiusOfEllipse(eP, eT, cars[currentCar].position, cars[eC].length, cars[eC].width) for eP, eT, eC in zip(externalPositions, externalTargets, externalIds)]
#     print radiusesOfEllipsesFromExternalCars
    distanceBetweenCentersOfCars = [np.linalg.norm(eC - cars[currentCar].position) for eC in externalPositions]
    sumOfRadiuses = radiusesOfEllipses + radiusesOfEllipsesFromExternalCars - distanceBetweenCentersOfCars
#     print sumOfRadiuses
#     return 
    return amplitudeAlphaU * sum([exp(sumOfRadiuses[i]/BAlphaU) * normalizedAlphaBetaVectors[i] for i in range(len(sumOfRadiuses))])

def computePedestrianTargetAttractiveForce(pedestrians, currentPedestrian):
    '''Returns the attractive force to a destination'''
    eAlpha  = normalisedDesiredDirection(pedestrians[currentPedestrian].target, pedestrians[currentPedestrian].position)
    vAlpha0 = eAlpha * pedestrians[currentPedestrian].desiredVelocity
    return (vAlpha0 - pedestrians[currentPedestrian].velocity) / pedestrians[currentPedestrian].relaxationTime

def computePedPedRepulsiveForce(pedestrians, currentPedestrian):
    ''' Returns the repulsive force between all other pedestrians and the current one'''
    externalVelocities, externalPositions, externalTargets, normalizedAlphaBetaVectors = extractExternalVariablesForPedestrians(pedestrians, currentPedestrian)
    semiMinorAxes = np.array([ellipseSemiMinorAxis(dt, eV, pedestrians[currentPedestrian].position, eP, eT) for eV, eP, eT in zip(externalVelocities, externalPositions, externalTargets)]) 
    return amplitude * sum([exp(-semiMinorAxes[i]/sigma) * normalizedAlphaBetaVectors[i] for i in range(len(semiMinorAxes))])

def extractExternalVariablesForCars(cars, currentCar):
    ''' Extract the nbCars-1 other variables necessary'''
    excludingCar = 'standardCar' + str(currentCar)
    externalVelocities = [car.velocity for car in cars if car.id != excludingCar]
    externalPositions  = [car.position for car in cars if car.id != excludingCar]
    externalTargets    = [car.target for car in cars if car.id != excludingCar]
    externalIds        = [car for car in range(len(cars)) if car != currentCar]
    normalizedAlphaBetaVectors = [normalisedDesiredDirection(cars[currentCar].position, externalPosition) for externalPosition in externalPositions]
    return externalVelocities, externalPositions, externalTargets, externalIds, normalizedAlphaBetaVectors
    
def extractExternalVariablesForPedestrians(pedestrians, currentPedestrian):
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

# cars      = spawnCars(5).spawnRandomlyStandardCars()
# force = computeCarCarRepulsiveForce(cars, 5)
    
    
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
