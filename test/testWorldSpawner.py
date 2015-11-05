'''
Created on 29 Oct 2015

@author: RolandGuichard
'''
import unittest

from spawners.worldSpawner import *

class testClass:
    pass
    
class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testWorldSpawner(self):
        numberOfEntities = 10
#         spawnBuildings   = worldSpawner(NumberOfEntities).buildingSpawner()
        spawnWorld   = worldSpawner(numberOfEntities)
        ErrorMessage1 = "Wrong number of Entities for world Spawner"
#         spawnPedestrians = worldSpawner.pedestrianSpawner()
#         spawnCars        = worldSpawner.vehicleSpawner() 
#         ErrorMessage1 = "Wrong type for building spawner"
#         ErrorMessage2 = "Wrong type for pedestrian spawner"
#         ErrorMessage3 = "Wrong type for car spawner"
        self.assertEqual(spawnWorld.numberOfEntities, numberOfEntities, ErrorMessage1)
#         self.assertEqual(type(spawnBuildings), 'classobj', ErrorMessage1)
#         self.assertEqual(type(spawnPedestrians), 'classobj', ErrorMessage2)
#         self.assertEqual(type(spawnCars), 'classobj', ErrorMessage3)
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testWorldSpawner']
    unittest.main()