'''
Created on 21 Oct 2015

@author: RolandGuichard
'''
import unittest

import matplotlib
import matplotlib.pyplot as plt

from worldParameters.worldDimensions import *
from vehiclesParameters.vehicleSettings import *
from spawners.vehicleSpawner import *

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testVehicleSpawnerWithRandomlyPlacedCars(self):
        cars = spawnRandomCars()
        fig = plt.figure()
        ax = fig.add_subplot(111)
        for i in range(nbStandardCars):
            car1 = matplotlib.patches.Ellipse((cars[i].position[0], cars[i].position[1]), cars[i].length, cars[i].width, angle=0., color=cars[i].color)
            ax.add_patch(car1)

        plt.xlim([-worldLength, worldLength])
        plt.ylim([-worldWidth, worldWidth])
        plt.show()
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()