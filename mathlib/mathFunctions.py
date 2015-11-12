#!/usr/bin/python

import numpy as np

from entities.pedestrians.pedestrianSettings import *
from entities.vehicles.vehicleSettings import *

def pedestrianStopAtDestination(x):
    if (np.linalg.norm(x) < pedestrianStopAcceptance):
        return 0.
    else:
        return 1.

def carStopAtDestination(x):
    if (np.linalg.norm(x) < carStopAcceptance):
        return 1.e-8
    else:
        return 1.