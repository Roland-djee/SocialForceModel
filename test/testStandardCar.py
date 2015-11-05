'''
Created on 21 Oct 2015

@author: RolandGuichard
'''
import unittest

import numpy as np

from entities.vehicles.standardCar import *

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testStandardCarWithCar(self):
        numberOfEntities = 20
        position = np.array([5., 5., 5.])
        target = np.array([10., 10., 10.])
        velocity = np.array([1., 1., 1.])
        car = 'standardCar'
        id       = 10
        initialConditions = 'random'
        length = 4.5
        width  = 2
        height = 0
        returnedCar = standardCar(numberOfEntities, car, id, initialConditions, position, target, velocity)
        errorMessage = "Wrong input value for car"
        self.assertEqual(returnedCar.type, car, errorMessage)
        errorMessage = "Wrong input value for id"
        self.assertEqual(returnedCar.id, id, errorMessage)
        errorMessage = "Wrong input value for initial conditions"
        self.assertEqual(returnedCar.initialConditions, initialConditions, errorMessage)
#         errorMessage = "Wrong input value for position"
#         self.assertEqual(returnedcar.position.all(), position.all(), errorMessage)
#         errorMessage = "Wrong input value for velocity"
#         self.assertEqual(returnedcar.velocity.all(), velocity.all(), errorMessage)
#         errorMessage = "Wrong input value for target"
#         self.assertEqual(returnedcar.target.all(), target.all(), errorMessage)
        errorMessage = "Wrong input value for desired velocity"
        self.assertEqual(returnedCar.desiredVelocity, v0, errorMessage)
        errorMessage = "Wrong input value for relaxtion time"
        self.assertEqual(returnedCar.relaxationTime, tauAlpha, errorMessage)
        errorMessage = "Wrong input value for initial length"
        self.assertEqual(returnedCar.length, length, errorMessage)
        errorMessage = "Wrong input value for initial width"
        self.assertEqual(returnedCar.width, width, errorMessage)
        errorMessage = "Wrong input value for initial height"
        self.assertEqual(returnedCar.height, height, errorMessage)
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()