#!/usr/bin/python

from math import *
import numpy as np

from mathlib.vectors import normalisedDesiredDirection

def ellipseSemiMinorAxis(dt, externalVelocity, position, externalPosition, externalTarget):
    ''' Returns the semiminor axis of the ellipse force field defined in the repulsive social force.
    Variable names follow [Helbing et al. PRE 51, 5 (1995)]'''
    rAlphaBeta = position - externalPosition
    b          = np.linalg.norm(rAlphaBeta)
    eBeta      = normalisedDesiredDirection(externalTarget, externalPosition)
    sBeta      = np.linalg.norm(externalVelocity) * dt
    b          = b + np.linalg.norm(rAlphaBeta - sBeta * eBeta)
    return sqrt(b**2 - sBeta**2) * 0.5