#!/usr/bin/python

from pedestrianSettings import *
from pedestrianType import *

class standardPedestrian(pedestrian):
    def __init__(self, numberOfEntities, pedType, id, initialConditions, position=np.zeros(3), target=np.zeros(3), velocity=np.zeros(3), target2=np.zeros(3)):
        super(standardPedestrian, self).__init__(numberOfEntities, pedType, id, initialConditions, position, target, velocity, target2)
        self.desiredVelocity = v0
        self.relaxationTime  = tauAlpha