'''
Created on 13 Oct 2015

@author: RolandGuichard
'''
import unittest

import numpy as np
from math import *

from mathlib import *
from mathlib.ellipse import *

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testEllipseSemiMinorAxis(self):
        dt = 0.01
        externalVelocity = np.array([1., 1., 1.])
        position = np.array([2., 2., 2.])
        externalPosition = np.array([3., 3., 3.])
        externalTarget = np.array([4., 4., 4.])
        returnedSemiMinorAxis = ellipseSemiMinorAxis(dt, externalVelocity, position, externalPosition, externalTarget)
        expectedSemiMinorAxis = sqrt(2.01**2 - 0.01**2) * sqrt(3.) /2.
        errorMessage = "Wrong value for semi-minor axis."
        self.assertAlmostEqual(returnedSemiMinorAxis, expectedSemiMinorAxis, 7, errorMessage)
        pass
    
    def testRadiusOfEllipse(self):
        position = np.array([2., 2., 2.])
        target = np.array([4., 4., 4.])
        externalPosition = np.array([3., 3., 3.])
        length = 4.5
        width = 2.
        returnedRadiusOfEllipse = radiusOfEllipse(position, target, externalPosition, length, width)
        expectedRadiusOfEllipse = 4.5
        errorMessage = "Wrong value for radius of ellipse."
        self.assertAlmostEqual(returnedRadiusOfEllipse, expectedRadiusOfEllipse, 7, errorMessage)
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testEllipseSemiMinorAxis']
    unittest.main()