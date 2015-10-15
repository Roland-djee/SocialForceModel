#!/usr/bin/python

# class pedestrianType:
class pedestrianType(object):
    '''Defines the type of pedestrian and packages the coordinates'''
    def __init__(self, pedType, id, initialConditions):
        self.type              = pedType
        self.id                = 'Pedestrian' + str(id)
        self.initialConditions = initialConditions
        self.color             = 'blue' 
