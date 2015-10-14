#!/usr/bin/python

import numpy as np

from pedestrianParameters.pedestrianSettings import *
from pedestrianParameters.standardPedestrian import *
from worldParameters.worldDimensions import *

def spawnRandomPedestrians():
    standardPedestrians = [None] * nbStandardPedestrians
    for i in range(nbStandardPedestrians):
        position    = (np.random.rand(3) * 2. - 1.)
        position[0] = position[0] * worldLength
        position[1] = position[1] * worldWidth
        velocity    = (np.random.rand(3) * 2. - 1.)
        target      = (np.random.rand(3) * 2. - 1.)
        target[0]   = target[0] * worldLength
        target[1]   = target[1] * worldWidth
        standardPedestrians[i] = standardPedestrian(standardPedestrian, i, position, velocity, target)
    return np.array(standardPedestrians)

pedestrians = spawnRandomPedestrians()

        