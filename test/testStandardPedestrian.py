'''
Created on 13 Oct 2015

@author: RolandGuichard
'''
import unittest

import numpy as np

from pedestrianParameters.standardPedestrian import *
from pedestrianParameters.pedestrianSettings import *

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testStandardPedestrianWithPedestrian(self):
        pedestrian = 'standardPedestrian'
        id       = 10
        position = np.array([2., 4., 6.]) 
        velocity = np.array([1., 3., 5.]) 
        target   = np.array([10., 15., 20.]) 
        returnedPedestrian = standardPedestrian(pedestrian, id, position, velocity, target)
#         returnedPedestrian = standardPedestrian()
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
        errorMessage = "Wrong input value for desired velocity"
        self.assertEqual(returnedPedestrian.desiredVelocity, v0, errorMessage)
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testStandardPedestrian']
    unittest.main()