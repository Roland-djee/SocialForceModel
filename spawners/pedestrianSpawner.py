#!/usr/bin/python

import numpy as np

from entities.pedestrians.standardPedestrian import *


from spawners.worldSpawner import *

class spawnPedestrians(worldSpawner):
    def __init__(self, numberOfEntities):
        super(spawnPedestrians, self).__init__(numberOfEntities)
    def spawnRandomlyStandardPedestrians(self):
        standardPedestrians = [None] * self.numberOfEntities
        for i in range(self.numberOfEntities):
            standardPedestrians[i] = standardPedestrian(self.numberOfEntities, 'standardPedestrian', i, 'random')
        return np.array(standardPedestrians)

# pedestrians = spawnRandomPedestrians()

        
        