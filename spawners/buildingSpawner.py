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
		buildings[i] = buildingType('office', *buildingCoordinates)
	return buildings
		
def spawnWalls():
	walls = [None] * nbWalls
	for i in range(nbWalls):
		walls[i] = buildingType('wall', *wallCoordinates)
	return walls
	
walls, buildings = spawnEnvironment()


