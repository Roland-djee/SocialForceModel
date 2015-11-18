'''
Created on 12 Oct 2015

@author: RolandGuichard
'''
import unittest

import matplotlib.pyplot as plt
import matplotlib

from world.worldParameters import *
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
    
    def testPedestrianSpawnerWithRandomlyPlacedStandardPedestriansInArea(self):
        numberOfPedestrians = 10
        pedestrian = spawnPedestrians(numberOfPedestrians)
        errorMessage = "Wrong input value for number of pedestrians"
        self.assertEqual(pedestrian.numberOfEntities, numberOfPedestrians, errorMessage)
        bottomLeft = np.array([5., 5., 0.])
        upperRight = np.array([10., 10., 0.])
        bottomLeft2 = np.array([-15., 5., 0.])
        upperRight2 = np.array([-10., 10., 0.])
        pedestrians2 = spawnPedestrians(numberOfPedestrians).spawnStandardPedestriansInArea(bottomLeft, upperRight, bottomLeft2, upperRight2)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        for i in range(numberOfPedestrians):
            plt.plot([pedestrians2[i].position[0]],[pedestrians2[i].position[1]], 'bo')
            plt.plot([pedestrians2[i].target[0]],[pedestrians2[i].target[1]], 'ro')
        area = matplotlib.patches.Rectangle((bottomLeft[0], bottomLeft[1]), upperRight[0]-bottomLeft[0], upperRight[1]-bottomLeft[1], color='grey')
        area2 = matplotlib.patches.Rectangle((bottomLeft2[0], bottomLeft2[1]), upperRight2[0]-bottomLeft2[0], upperRight2[1]-bottomLeft2[1], color='grey')
        ax.add_patch(area)
        ax.add_patch(area2)
        plt.xlim([-worldLength, worldLength])
        plt.ylim([-worldWidth, worldWidth])
        plt.show()
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()