'''
Created on 9 Oct 2015

@author: RolandGuichard
'''
import unittest

from entities.pedestrians.pedestrianType import *

import numpy as np

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPedestrianTypeWithPedestrian(self):
        numberOfEntities = 20
        position = np.array([5., 5., 5.])
        target = np.array([10., 10., 10.])
        velocity = np.array([1., 1., 1.])
        pedtype = 'Pedestrian'
        id       = 10  
        initialConditions = 'defined'
        returnedPedestrian = pedestrian(numberOfEntities, pedtype, id, initialConditions, position, target, velocity)
        errorMessage = "Wrong input value for number of entities"
        self.assertEqual(returnedPedestrian.numberOfEntities, numberOfEntities, errorMessage)
        errorMessage = "Wrong input value for position"
        self.assertEqual(returnedPedestrian.position.all(), position.all(), errorMessage)
        errorMessage = "Wrong input value for target"
        self.assertEqual(returnedPedestrian.target.all(), target.all(), errorMessage)
        errorMessage = "Wrong input value for velocity"
        self.assertEqual(returnedPedestrian.velocity.all(), velocity.all(), errorMessage)
        errorMessage = "Wrong input value for pedestrian"
        self.assertEqual(returnedPedestrian.type, pedtype, errorMessage)
        errorMessage = "Wrong input value for id"
        self.assertEqual(returnedPedestrian.id, id, errorMessage)
        errorMessage = "Wrong input value for initial conditions"
        self.assertEqual(returnedPedestrian.initialConditions, initialConditions, errorMessage)
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()