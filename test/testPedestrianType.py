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
        initialConditions = 'random'
        returnedPedestrian = pedestrianType(pedestrian, id, initialConditions)
        errorMessage = "Wrong input value for pedestrian"
        self.assertEqual(returnedPedestrian.type, pedestrian, errorMessage)
        errorMessage = "Wrong input value for id"
        self.assertEqual(returnedPedestrian.id, 'Pedestrian'+str(id), errorMessage)
        errorMessage = "Wrong input value for initial conditions"
        self.assertEqual(returnedPedestrian.initialConditions, 'random', errorMessage)
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()