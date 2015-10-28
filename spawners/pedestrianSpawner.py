#!/usr/bin/python

import numpy as np

from pedestrianParameters.pedestrianSettings import *
from pedestrianParameters.standardPedestrian import *

def spawnRandomPedestrians():
    standardPedestrians = [None] * nbStandardPedestrians
    for i in range(nbStandardPedestrians):
        standardPedestrians[i] = standardPedestrian('standardPedestrian', i, 'random')
    return np.array(standardPedestrians)

pedestrians = spawnRandomPedestrians()

        
        