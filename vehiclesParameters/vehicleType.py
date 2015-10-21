#!/usr/bin/python

# class vehicleType:
class vehicleType(object):
    '''Defines the type of vehicle and packages the coordinates'''
    def __init__(self, vehType, id, initialConditions, length, width, height):
        self.type              = vehType
        self.id                = vehType + str(id)
        self.initialConditions = initialConditions
        self.length            = length
        self.width             = width
        self.height            = height
        self.color             = 'green' 
