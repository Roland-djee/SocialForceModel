#!/usr/bin/python

import numpy as np

from vehiclesParameters.vehicleType import *
from vehiclesParameters.vehicleSettings import *
from worldParameters.worldDimensions import *

class standardCar(vehicleType):
    def __init__(self, vehType, id, initialConditions):
        super(standardCar, self).__init__(vehType, id, initialConditions, standardCarLength, standardCarWidth, standardCarHeight)
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