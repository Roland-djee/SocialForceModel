'''
Created on 21 Oct 2015

@author: RolandGuichard
'''
import unittest

from vehiclesParameters.vehicleType import *
from nltk.downloader import ErrorMessage


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testVehicleTypeWithCar(self):
        vehicle = 'car'
        id = 10
        initialConditions = 'random'
        length = 4
        width  = 2
        height = 2
        returnedCar = vehicleType(vehicle, id, initialConditions, length, width, height)
        errorMessage = "Wrong input value for vehicle"
        self.assertEqual(returnedCar.type, vehicle, errorMessage)
        errorMessage = "Wrong input value for id"
        self.assertEqual(returnedCar.id, vehicle + str(id), errorMessage)
        errorMessage = "Wrong input value for initial conditions"
        self.assertEqual(returnedCar.initialConditions, initialConditions, errorMessage)
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