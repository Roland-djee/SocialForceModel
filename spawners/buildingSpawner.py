#!/usr/bin/python
from buildingParameters.buildingDimensions import *
from buildingParameters.buildingType import *
from worldParameters.worldDimensions import *
import matplotlib.pyplot as plt
import matplotlib

def spawnEnvironment():
	walls     = spawnWalls()
	buildings = spawnBuilding()
	return walls, buildings

def spawnBuilding():
	buildings = [None] * nbBuildings
	for i in range(nbBuildings):
		buildings[i] = buildingType('office', np.array([buildingCoordinates[4*i], buildingCoordinates[4*i+1],
												buildingCoordinates[4*i+2], buildingCoordinates[4*i+3]]))
	return buildings
		
def spawnWalls():
	walls = [None] * nbWalls
	for i in range(nbWalls):
		walls[i] = buildingType('wall', np.array([wallsCoordinates[2*i], wallsCoordinates[2*i+1]]))
	return walls
	
# walls, buildings = spawnEnvironment()
# fig = plt.figure()
# ax = fig.add_subplot(111)
# for i in range(nbWalls):
# 	plt.plot([walls[i].coordinates[0][0],walls[i].coordinates[1][0]], [walls[i].coordinates[0][1],walls[i].coordinates[1][1]], walls[i].color, linewidth=5)

# for i in range(nbBuildings):
# 	build1 = matplotlib.patches.Rectangle((buildings[i].coordinates[0][0],buildings[i].coordinates[0][1]), 20, 20, color=buildings[i].color)
# 	ax.add_patch(build1)

# plt.xlim([-worldLength, worldLength])
# plt.ylim([-worldWidth, worldWidth])
# plt.show()

