#!/usr/bin/python
from entities.entities import *
import numpy as np
from vehicleSettings import *

from world.worldParameters import *
# class vehicleType:
class vehicle(entities):
    '''Defines the type of vehicle and packages the coordinates'''
    def __init__(self, numberOfEntities, vehType, id, initialConditions, position=np.zeros(3), target=np.zeros(3), velocity=np.zeros(3)):
        super(vehicle, self).__init__(numberOfEntities)
        self.type              = vehType
        self.id                = id
        self.initialConditions = initialConditions
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
        if (initialConditions == 'defined'):
            self.position = position
            self.velocity = velocity
            self.target   = target
        self.color             = 'green'
        self.movementStatus    = 'driving'
