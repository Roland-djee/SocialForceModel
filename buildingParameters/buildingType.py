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
            self.x1 = wallsCoordinates[0][0]
            self.y1 = wallsCoordinates[0][1]
            self.x2 = wallsCoordinates[1][0]
            self.y2 = wallsCoordinates[1][1]
            self.color = 'black'
        elif (buildingType == 'office'):
            self.corner1x = wallsCoordinates[0][0]
            self.corner1y = wallsCoordinates[0][1]
            self.corner2x = wallsCoordinates[1][0]
            self.corner2y = wallsCoordinates[1][1]
            self.corner3x = wallsCoordinates[2][0]
            self.corner3y = wallsCoordinates[2][1]
            self.corner4x = wallsCoordinates[3][0]
            self.corner4y = wallsCoordinates[3][1]
            self.color = 'grey' 