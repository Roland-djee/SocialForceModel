#!/usr/bin/python

import numpy as np

from pedestrianParameters.pedestrianType import *
from pedestrianParameters.pedestrianSettings import *
from worldParameters.worldDimensions import *

class standardPedestrian(pedestrianType):
    def __init__(self, pedType, id, initialConditions):
        super(standardPedestrian, self).__init__(pedType, id, initialConditions)
        self.desiredVelocity = v0
        self.relaxationTime  = tauAlpha
        if (initialConditions == 'random'):
            position      = (np.random.rand(3) * 2. - 1.)
            position[0]   = position[0] * worldLength
            position[1]   = position[1] * worldWidth
            position[2]   = 0.
            self.position = position
            velocity      = (np.random.rand(3) * 2. - 1.)
            velocity[0]   = velocity[0] * v0
            velocity[1]   = np.sqrt(v0**2 - velocity[0]**2)
            velocity[2]   = 0.
            self.velocity = velocity
            target        = (np.random.rand(3) * 2. - 1.)
            target[0]     = target[0] * worldLength
            target[1]     = target[1] * worldWidth
            target[2]     = 0.
            self.target   = target 