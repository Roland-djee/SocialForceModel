'''
Created on 12 Oct 2015

@author: RolandGuichard
'''
import unittest

import matplotlib.pyplot as plt

from worldParameters.worldDimensions import *
from entities.pedestrians.pedestrianSettings import *

from spawners.pedestrianSpawner import *

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    def testPedestrianSpawnerWithRandomlyPlacedStandardPedestrians(self):
        numberOfPedestrians = 10
        pedestrian = spawnPedestrians(numberOfPedestrians)
        errorMessage = "Wrong input value for number of pedestrians"
        self.assertEqual(pedestrian.numberOfEntities, numberOfPedestrians, errorMessage)
        pedestrians2 = spawnPedestrians(numberOfPedestrians).spawnRandomlyStandardPedestrians()
        fig = plt.figure()
        ax = fig.add_subplot(111)
        for i in range(numberOfPedestrians):
            plt.plot([pedestrians2[i].position[0]],[pedestrians2[i].position[1]], 'bo')
        plt.xlim([-worldLength, worldLength])
        plt.ylim([-worldWidth, worldWidth])
        plt.show()
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()