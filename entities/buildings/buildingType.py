#!/usr/bin/python
import numpy as np
from buildingDimensions import wallCoordinates

class buildingType:
    '''Defines the type of building and packages the dimensions'''
    
    def __init__(self, buildingType, *wallCoordinates):
        if len(wallCoordinates) !=2 and len(wallCoordinates) !=4:
            raise 'Wrong number of coordinates in "wallsCoordinates"'
        self.type = buildingType
        if (buildingType == 'wall'):
            self.endPoint1 = wallCoordinates[0]
            self.endPoint2 = wallCoordinates[1]
            self.color = 'black'
        elif (buildingType == 'office'):
            self.corner1 = wallCoordinates[0]  
            self.corner2 = wallCoordinates[1]
            self.corner3 = wallCoordinates[2]
            self.corner4 = wallCoordinates[3]
            self.color = 'grey' 