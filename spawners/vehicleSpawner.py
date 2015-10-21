#!/usr/bin/python

import numpy as np

from vehiclesParameters.vehicleSettings import *
from vehiclesParameters.standardCar import *

def spawnRandomCars():
    standardCars = [None] * nbStandardCars
    for i in range(nbStandardCars):
            standardCars[i]  = standardCar('standardCar', i, 'random')
    return np.array(standardCars)

cars = spawnRandomCars()