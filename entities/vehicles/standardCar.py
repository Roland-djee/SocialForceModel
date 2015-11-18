#!/usr/bin/python

import numpy as np

from vehicleType import *
from vehicleSettings import *

class standardCar(vehicle):
    def __init__(self, numberOfEntities, vehType, id, initialConditions, position=np.zeros(3), target=np.zeros(3), velocity=np.zeros(3), target2=np.zeros(3)):
        super(standardCar, self).__init__(numberOfEntities, vehType, id, initialConditions, position, target, velocity, target2)
        self.desiredVelocity = v0
        self.relaxationTime  = tauAlpha
        self.length          = standardCarLength
        self.width           = standardCarWidth
        self.height          = standardCarHeight