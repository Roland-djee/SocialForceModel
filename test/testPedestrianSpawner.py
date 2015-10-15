'''
Created on 12 Oct 2015

@author: RolandGuichard
'''
import unittest

import matplotlib.pyplot as plt

from worldParameters.worldDimensions import *
from pedestrianParameters.pedestrianSettings import *
from spawners.pedestrianSpawner import *

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    def testPedestrianSpawnerWithRandomlyPlacedStandardPedestrians(self):
        pedestrian = spawnRandomPedestrians()
        fig = plt.figure()
        ax = fig.add_subplot(111)
        for i in range(nbStandardPedestrians):
            plt.plot([pedestrian[i].position[0]],[pedestrian[i].position[1]], 'bo')
        plt.xlim([-worldLength, worldLength])
        plt.ylim([-worldWidth, worldWidth])
        plt.show()
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()