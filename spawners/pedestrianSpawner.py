#!/usr/bin/python
import numpy as np
from pedestrianParameters.pedestrianSettings import *
from pedestrianParameters.pedestrianType import pedestrianType
from worldParameters.worldDimensions import *

def spawnRandomPedestrians():
    pedestrian = [None] * nbPedestrians
    for i in range(nbPedestrians):
        position    = (np.random.rand(3) * 2. - 1.)
        position[0] = position[0] * worldLength
        position[1] = position[1] * worldWidth
        velocity    = (np.random.rand(3) * 2. - 1.)
        target      = (np.random.rand(3) * 2. - 1.)
        target[0]   = target[0] * worldLength
        target[1]   = target[1] * worldWidth
        pedestrian[i] = pedestrianType(pedestrian, position, velocity, target)
    return pedestrian

pedestrian = spawnRandomPedestrians()

        