'''
Created on 9 Oct 2015

@author: RolandGuichard
'''
import unittest

from pedestrianParameters.pedestrianType import *

import numpy as np

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPedestrianTypeWithPedestrian(self):
        pedestrian = 'pedestrian'
        id       = 10  
        position = np.array([2., 4., 6.]) 
        velocity = np.array([1., 3., 5.]) 
        target   = np.array([10., 15., 20.]) 
        returnedPedestrian = pedestrianType(pedestrian, id, position, velocity, target)
        errorMessage = "Wrong input value for pedestrian"
        self.assertEqual(returnedPedestrian.type, pedestrian, errorMessage)
        errorMessage = "Wrong input value for id"
        self.assertEqual(returnedPedestrian.id, 'Pedestrian'+str(id), errorMessage)
        errorMessage = "Wrong input value for position"
        self.assertEqual(returnedPedestrian.position.all(), position.all(), errorMessage)
        errorMessage = "Wrong input value for velocity"
        self.assertEqual(returnedPedestrian.velocity.all(), velocity.all(), errorMessage)
        errorMessage = "Wrong input value for target"
        self.assertEqual(returnedPedestrian.target.all(), target.all(), errorMessage)
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()