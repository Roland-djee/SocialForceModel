'''
Created on 9 Oct 2015

@author: RolandGuichard
'''
import unittest

from buildingParameters.buildingType import *

import numpy as np


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testBuildingTypeForAWall(self):
        corner1 = np.array([-5., -2., 0.])
        corner2 = np.array([2., 5., 0.])
        wallCoordinates = np.array([corner1, corner2])   
        returnedWall = buildingType('wall', *wallCoordinates)
        errorMessage = "Wrong input value for x1"
        self.assertEqual(returnedWall.x1, corner1[0], errorMessage)
        errorMessage = "Wrong input value for y1"
        self.assertEqual(returnedWall.y1, corner1[1], errorMessage)
        errorMessage = "Wrong input value for x1"
        self.assertEqual(returnedWall.x2, corner2[0], errorMessage)
        errorMessage = "Wrong input value for x1"
        self.assertEqual(returnedWall.y2, corner2[1], errorMessage)
        pass
    
    def testBuildingTypeForAnOffice(self):
        corner1 = np.array([20., 20., 0.])
        corner2 = np.array([20., 40., 0.])
        corner3 = np.array([40., 40., 0.])
        corner4 = np.array([40., 20., 0.])
        OfficesCoordinates = np.array([corner1, corner2, corner3, corner4])   
        returnedOffice = buildingType('office', *OfficesCoordinates)
        errorMessage = "Wrong input value for x1"
        self.assertEqual(returnedOffice.corner1x, corner1[0], errorMessage)
        errorMessage = "Wrong input value for y1"
        self.assertEqual(returnedOffice.corner1y, corner1[1], errorMessage)
        errorMessage = "Wrong input value for x1"
        self.assertEqual(returnedOffice.corner2x, corner2[0], errorMessage)
        errorMessage = "Wrong input value for x1"
        self.assertEqual(returnedOffice.corner2y, corner2[1], errorMessage)
        errorMessage = "Wrong input value for x1"
        self.assertEqual(returnedOffice.corner3x, corner3[0], errorMessage)
        errorMessage = "Wrong input value for y1"
        self.assertEqual(returnedOffice.corner3y, corner3[1], errorMessage)
        errorMessage = "Wrong input value for x1"
        self.assertEqual(returnedOffice.corner4x, corner4[0], errorMessage)
        errorMessage = "Wrong input value for x1"
        self.assertEqual(returnedOffice.corner4y, corner4[1], errorMessage)
        pass
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testBuildingTypeForAOffice']
    unittest.main()