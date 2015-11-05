'''
Created on 21 Oct 2015

@author: RolandGuichard
'''
import unittest

import matplotlib
import matplotlib.pyplot as plt

from worldParameters.worldDimensions import *
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


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()