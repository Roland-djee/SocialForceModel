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
    print b, sBeta, rAlphaBeta
    return sqrt(b**2 - sBeta**2) * 0.5

def radiusOfEllipse(position, target, externalPosition, length, width):
    ''' Returns all the radiuses between the ellipse defining the current car and all others,
    necessary for the repulsive social force. Variable names follow [Anvari et al.]'''
    epsilon      = sqrt(length**2 - width**2) / length
    cosPhiSquare = np.dot(externalPosition - position, target - position) / (np.linalg.norm(externalPosition - position)*np.linalg.norm(target - position))
    return width / sqrt(1. - epsilon**2 * cosPhiSquare**2) 