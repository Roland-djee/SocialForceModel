'''
Created on 21 Oct 2015

@author: RolandGuichard
'''
import unittest

import matplotlib
import matplotlib.pyplot as plt

from world.worldParameters import *
from entities.vehicles.vehicleSettings import *
from spawners.vehicleSpawner import *

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    def testVehicleSpawnerWithRandomlyPlacedCars(self):
        numberOfCars = 15
        cars = spawnCars(numberOfCars)
        errorMessage = "Wrong input value for number of cars"
        self.assertEqual(cars.numberOfEntities, numberOfCars, errorMessage)
#         cars2 = spawnCars(numberOfCars).spawnRandomlyStandardCars()
        cars2 = spawnCars(numberOfCars).spawnRandomlyStandardCars()
        fig = plt.figure()
        ax = fig.add_subplot(111)
        for i in range(numberOfCars):
#             car1 = matplotlib.patches.Ellipse((cars2[i].position[0], cars2[i].position[1]), cars2[i].length, cars2[i].width, angle=0., color=cars2[i].color)
            car1 = matplotlib.patches.Ellipse((cars2[i].position[0], cars2[i].position[1]), cars2[i].length, cars2[i].width, angle=0., color=cars2[i].color)           
            ax.add_patch(car1)

        plt.xlim([-worldLength, worldLength])
        plt.ylim([-worldWidth, worldWidth])
        plt.show()
        pass
    
    def testCarSpawnerWithRandomlyPlacedStandardPedestriansInArea(self):
        numberOfPedestrians = 10
        car = spawnCars(numberOfPedestrians)
        errorMessage = "Wrong input value for number of pedestrians"
        self.assertEqual(car.numberOfEntities, numberOfPedestrians, errorMessage)
        bottomLeft = np.array([5., 5., 0.])
        upperRight = np.array([10., 10., 0.])
        bottomLeft2 = np.array([-15., 5., 0.])
        upperRight2 = np.array([-10., 10., 0.])
        cars2 = spawnCars(numberOfPedestrians).spawnStandardCarsInArea(bottomLeft, upperRight, bottomLeft2, upperRight2)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        
        area = matplotlib.patches.Rectangle((bottomLeft[0], bottomLeft[1]), upperRight[0]-bottomLeft[0], upperRight[1]-bottomLeft[1], color='grey')
        area2 = matplotlib.patches.Rectangle((bottomLeft2[0], bottomLeft2[1]), upperRight2[0]-bottomLeft2[0], upperRight2[1]-bottomLeft2[1], color='grey')
        ax.add_patch(area)
        ax.add_patch(area2)
        for i in range(numberOfPedestrians):
            car1 = matplotlib.patches.Ellipse((cars2[i].position[0], cars2[i].position[1]), cars2[i].length, cars2[i].width, angle=0., color=cars2[i].color)           
            ax.add_patch(car1)
        plt.xlim([-worldLength, worldLength])
        plt.ylim([-worldWidth, worldWidth])
        plt.show()
        pass



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()