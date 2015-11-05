#!/usr/bin/python

from entities.buildings.buildingType import *
from entities.buildings.buildingDimensions import *

from world.worldParameters import *
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


