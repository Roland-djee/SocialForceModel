#!/usr/bin/python

# class pedestrianType:
class pedestrianType(object):
    '''Defines the type of pedestrian and packages the coordinates'''
    def __init__(self, pedType, coordinates, velocity, target):
        self.type     = pedType
        self.position = coordinates
        self.velocity = velocity
        self.target   = target
        self.color    = 'blue'    