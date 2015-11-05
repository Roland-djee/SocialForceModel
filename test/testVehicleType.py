'''
Created on 21 Oct 2015

@author: RolandGuichard
'''
import unittest

from entities.vehicles.vehicleSettings import *
from entities.vehicles.vehicleType import *


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testVehicleTypeWithCar(self):
        numberOfEntities = 20
        position = np.array([5., 5., 5.])
        target = np.array([10., 10., 10.])
        velocity = np.array([1., 1., 1.])
        pedtype = 'Pedestrian'
        id       = 10  
        vehType = 'car'
        id = 10
        initialConditions = 'defined'
        returnedCar = vehicle(numberOfEntities, vehType, id, initialConditions, position, target, velocity)
        errorMessage = "Wrong input value for vehicle"
        self.assertEqual(returnedCar.type, vehType, errorMessage)
        errorMessage = "Wrong input value for id"
        self.assertEqual(returnedCar.id, id, errorMessage)
        errorMessage = "Wrong input value for initial conditions"
        self.assertEqual(returnedCar.initialConditions, initialConditions, errorMessage)
        errorMessage = "Wrong input value for number of Entities"
        self.assertEqual(returnedCar.numberOfEntities, numberOfEntities, errorMessage)
        errorMessage = "Wrong input value for position"
        self.assertEqual(returnedCar.position.all(), position.all(), errorMessage)
        errorMessage = "Wrong input value for target"
        self.assertEqual(returnedCar.target.all(), target.all(), errorMessage)
        errorMessage = "Wrong input value for velocity"
        self.assertEqual(returnedCar.velocity.all(), velocity.all(), errorMessage)
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()