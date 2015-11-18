'''
Created on 9 Oct 2015

@author: RolandGuichard
'''
import unittest

import matplotlib.pyplot as plt
import matplotlib


from entities.pedestrians.pedestrianType import *

import numpy as np

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPedestrianTypeWithPedestrian(self):
        numberOfEntities = 20
        position = np.array([5., 5., 5.])
        target = np.array([10., 10., 10.])
        velocity = np.array([1., 1., 1.])
        pedtype = 'Pedestrian'
        id       = 10  
        initialConditions = 'defined'
        returnedPedestrian = pedestrian(numberOfEntities, pedtype, id, initialConditions, position, target, velocity)
        errorMessage = "Wrong input value for number of entities"
        self.assertEqual(returnedPedestrian.numberOfEntities, numberOfEntities, errorMessage)
        errorMessage = "Wrong input value for position"
        self.assertEqual(returnedPedestrian.position.all(), position.all(), errorMessage)
        errorMessage = "Wrong input value for target"
        self.assertEqual(returnedPedestrian.target.all(), target.all(), errorMessage)
        errorMessage = "Wrong input value for velocity"
        self.assertEqual(returnedPedestrian.velocity.all(), velocity.all(), errorMessage)
        errorMessage = "Wrong input value for pedestrian"
        self.assertEqual(returnedPedestrian.type, pedtype, errorMessage)
        errorMessage = "Wrong input value for id"
        self.assertEqual(returnedPedestrian.id, id, errorMessage)
        errorMessage = "Wrong input value for initial conditions"
        self.assertEqual(returnedPedestrian.initialConditions, initialConditions, errorMessage)
        pass

    def testPedestrianTypeWithArea(self):
        numberOfEntities = 20
        bottomLeftStartArea = np.array([5., 5., 0.])
        upperRightStartArea = np.array([10., 10., 0.])
        bottomLeftEndArea = np.array([-15., 5., 0.])
        upperRightEndArea = np.array([-10., 10., 0.])
        pedtype = 'pedestrian'
        id       = 10  
        initialConditions = 'area'
        returnedPedestrian = pedestrian(numberOfEntities, pedtype, id, initialConditions, bottomLeftStartArea, upperRightStartArea, bottomLeftEndArea, upperRightEndArea)
        errorMessage = "Wrong input value for number of entities"
        self.assertEqual(returnedPedestrian.numberOfEntities, numberOfEntities, errorMessage)
        self.assertEqual(returnedPedestrian.type, pedtype, errorMessage)
        errorMessage = "Wrong input value for id"
        self.assertEqual(returnedPedestrian.id, id, errorMessage)
        errorMessage = "Wrong input value for initial conditions"
        self.assertEqual(returnedPedestrian.initialConditions, initialConditions, errorMessage)
        
        fig = plt.figure()
        ax = fig.add_subplot(111)
        
        plt.plot([returnedPedestrian.position[0]],[returnedPedestrian.position[1]], 'bo')
        plt.plot([returnedPedestrian.target[0]],[returnedPedestrian.target[1]], 'ro')
        area1 = matplotlib.patches.Rectangle((bottomLeftStartArea[0], bottomLeftStartArea[1]), upperRightStartArea[0]-bottomLeftStartArea[0], upperRightStartArea[1]-bottomLeftStartArea[1], color='grey')
        area2 = matplotlib.patches.Rectangle((bottomLeftEndArea[0], bottomLeftEndArea[1]), upperRightEndArea[0]-bottomLeftEndArea[0], upperRightEndArea[1]-bottomLeftEndArea[1], color='grey')
        ax.add_patch(area1)
        ax.add_patch(area2)
        plt.xlim([-worldLength, worldLength])
        plt.ylim([-worldWidth, worldWidth])
        plt.show()
        
        pass



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()