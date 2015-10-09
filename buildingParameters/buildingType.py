#!/usr/bin/python
import numpy as np
from buildingDimensions import wallsCoordinates

class buildingType:
    '''Defines the type of building and packages the dimensions'''
    
    def __init__(self, buildingType, *wallsCoordinates):
        if len(wallsCoordinates) !=2 and len(wallsCoordinates) !=4:
            raise 'Wrong number of coordinates in "wallsCoordinates"'
        self.type = buildingType
        if (buildingType == 'wall'):
            self.endPoint1 = wallsCoordinates[0]
            self.endPoint2 = wallsCoordinates[1]
            self.color = 'black'
        elif (buildingType == 'office'):
            self.corner1 = wallsCoordinates[0]  
            self.corner2 = wallsCoordinates[1]
            self.corner3 = wallsCoordinates[2]
            self.corner4 = wallsCoordinates[3]
            self.color = 'grey' 