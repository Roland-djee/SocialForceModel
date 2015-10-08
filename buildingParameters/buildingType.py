#!/usr/bin/python
import numpy as np

class buildingType:
    '''Defines the type of building and packages the dimensions'''
    def __init__(self, buildingType, coordinates):
        self.type = buildingType
        if (buildingType == 'wall'):
            self.coordinates = np.array(coordinates)
            self.color = 'black'
        elif (buildingType == 'office'):
            self.coordinates = np.array(coordinates)
            self.color = 'grey' 