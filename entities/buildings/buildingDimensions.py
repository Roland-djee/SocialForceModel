#!/usr/bin/python
import numpy as np

# set parameters for pedestrian-wall repulsive forces from [Helbing & Molnar Phys. Rev. E 51, 4282 (1995)]
U0 = 10.        # Wall repulsive potential amplitude [m^2 s^2]
R0 = 0.2        # Wall damping parameter [m]

nbWalls = 1

corner1 = np.array([-5., -2., 0.])
corner2 = np.array([2., 5., 0.])

wallCoordinates = np.array([corner1, corner2])

nbBuildings = 1

# building coordinates from the down left corner and in clockwise direction

corner1 = np.array([20., 20., 0.])
corner2 = np.array([20., 40., 0.])
corner3 = np.array([40., 40., 0.])
corner4 = np.array([40., 20., 0.])

corner5 = np.array([-40., 20., 0.])
corner6 = np.array([-40., 40., 0.])
corner7 = np.array([-20., 40., 0.])
corner8 = np.array([-20., 20., 0.])

buildingCoordinates = np.array([corner1, corner2, corner3, corner4])
