'''
Created on 12 Oct 2015

@author: RolandGuichard
'''
import unittest

import matplotlib.pyplot as plt

from worldParameters.worldDimensions import *
from buildingParameters.buildingDimensions import *
from spawners.buildingSpawner import *

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testBuildingSpawnerWith(self):
        walls, buildings = spawnEnvironment()
        fig = plt.figure()
        ax = fig.add_subplot(111)
        for i in range(nbWalls):
            plt.plot([walls[i].endPoint1[0],walls[i].endPoint2[0]], [walls[i].endPoint1[1],walls[i].endPoint2[1]], walls[i].color, linewidth=5)

        for i in range(nbBuildings):
            build1 = matplotlib.patches.Rectangle((buildings[i].corner1[0], buildings[i].corner1[1]), 20, 20, color=buildings[i].color)
            ax.add_patch(build1)

        plt.xlim([-worldLength, worldLength])
        plt.ylim([-worldWidth, worldWidth])
        plt.show()
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()