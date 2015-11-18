'''
Created on 21 Oct 2015

@author: RolandGuichard
'''
import unittest

from entities.vehicles.vehicleSettings import *
from entities.vehicles.vehicleType import *

import matplotlib
import matplotlib.pyplot as plt

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
    
    def testVehicleTypeWithArea(self):
        numberOfEntities = 20
        bottomLeftStartArea = np.array([5., 5., 0.])
        upperRightStartArea = np.array([10., 10., 0.])
        bottomLeftEndArea = np.array([-15., 5., 0.])
        upperRightEndArea = np.array([-10., 10., 0.])
        vehicletype = 'standardCar'
        id       = 10  
        initialConditions = 'area'
        returnedvehicle = vehicle(numberOfEntities, vehicletype, id, initialConditions, bottomLeftStartArea, upperRightStartArea, bottomLeftEndArea, upperRightEndArea)
        errorMessage = "Wrong input value for number of entities"
        self.assertEqual(returnedvehicle.numberOfEntities, numberOfEntities, errorMessage)
        self.assertEqual(returnedvehicle.type, vehicletype, errorMessage)
        errorMessage = "Wrong input value for id"
        self.assertEqual(returnedvehicle.id, id, errorMessage)
        errorMessage = "Wrong input value for initial conditions"
        self.assertEqual(returnedvehicle.initialConditions, initialConditions, errorMessage)
        
        fig = plt.figure()
        ax = fig.add_subplot(111)
        
        
        area1 = matplotlib.patches.Rectangle((bottomLeftStartArea[0], bottomLeftStartArea[1]), upperRightStartArea[0]-bottomLeftStartArea[0], upperRightStartArea[1]-bottomLeftStartArea[1], color='grey')
        area2 = matplotlib.patches.Rectangle((bottomLeftEndArea[0], bottomLeftEndArea[1]), upperRightEndArea[0]-bottomLeftEndArea[0], upperRightEndArea[1]-bottomLeftEndArea[1], color='grey')
        ax.add_patch(area1)
        ax.add_patch(area2)
        car1 = matplotlib.patches.Ellipse((returnedvehicle.position[0], returnedvehicle.position[1]), 4., 2., angle=0., color=returnedvehicle.color)  
        ax.add_patch(car1)
        plt.xlim([-worldLength, worldLength])
        plt.ylim([-worldWidth, worldWidth])
        plt.show()
        
        pass



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()