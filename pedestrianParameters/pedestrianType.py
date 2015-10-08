#!/usr/bin/python

import numpy as np

class pedestrianType:
    '''Defines the type of pedestrian and packages the coordinates'''
    def __init__(self, pedestrianType, coordinates, velocity, target):
        self.type     = pedestrianType
        self.position = coordinates
        self.velocity = velocity
        self.target   = target
        self.color    = 'blue'
        