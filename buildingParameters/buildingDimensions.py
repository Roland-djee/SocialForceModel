#!/usr/bin/python
import numpy as np

nbWalls = 2

corner1 = np.array([-5., -2., 0.])
corner2 = np.array([2., 5., 0.])
corner3 = np.array([10., 10., 0.])
corner4 = np.array([-10., 10., 0.])

wallsCoordinates = np.array([corner1, corner2, corner3, corner4])

nbBuildings = 2

# building coordinates from the down left corner and in clockwise direction

corner1 = np.array([20., 20., 0.])
corner2 = np.array([20., 40., 0.])
corner3 = np.array([40., 40., 0.])
corner4 = np.array([40., 20., 0.])

corner5 = np.array([-40., 20., 0.])
corner6 = np.array([-40., 40., 0.])
corner7 = np.array([-20., 40., 0.])
corner8 = np.array([-20., 20., 0.])

buildingCoordinates = np.array([corner1, corner2, corner3, corner4, corner5, corner6, corner7, corner8])
