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
        errorMessage = "Wrong input value for corner1"
        self.assertEqual(returnedWall.endPoint1.all(), corner1.all(), errorMessage)
        errorMessage = "Wrong input value for corner2"
        self.assertEqual(returnedWall.endPoint2.all(), corner2.all(), errorMessage)
        pass
    
    def testBuildingTypeForAnOffice(self):
        corner1 = np.array([20., 20., 0.])
        corner2 = np.array([20., 40., 0.])
        corner3 = np.array([40., 40., 0.])
        corner4 = np.array([40., 20., 0.])
        OfficesCoordinates = np.array([corner1, corner2, corner3, corner4])   
        returnedOffice = buildingType('office', *OfficesCoordinates)
        errorMessage = "Wrong input value for corner1"
        self.assertEqual(returnedOffice.corner1.all(), corner1.all(), errorMessage)
        errorMessage = "Wrong input value for corner2"
        self.assertEqual(returnedOffice.corner2.all(), corner2.all(), errorMessage)
        errorMessage = "Wrong input value for corner3"
        self.assertEqual(returnedOffice.corner3.all(), corner3.all(), errorMessage)
        errorMessage = "Wrong input value for corner4"
        self.assertEqual(returnedOffice.corner4.all(), corner4.all(), errorMessage)
        pass
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testBuildingTypeForAOffice']
    unittest.main()