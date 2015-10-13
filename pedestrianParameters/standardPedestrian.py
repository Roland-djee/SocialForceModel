#!/usr/bin/python

from pedestrianParameters.pedestrianType import *
from pedestrianParameters.pedestrianSettings import *

class standardPedestrian(pedestrianType):
    def __init__(self, pedType, coordinates, velocity, target):
        super(standardPedestrian, self).__init__(pedType, coordinates, velocity, target)
        self.desiredVelocity = v0
    