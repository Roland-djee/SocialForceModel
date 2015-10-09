#!/usr/bin/python

import json
from pprint import pprint
import os
from msilib import Control
import numpy as np


class Reader(object):

    def setTimePropagationParameters(self):
        tmax = self.__allData["PedestrianSimulator"][
            "data"]["timePropagationParameters"]["tmax"]["value"]
        dt = self.__allData["PedestrianSimulator"][
            "data"]["timePropagationParameters"]["dt"]["value"]
        time = np.linspace(0., tmax, int(tmax / dt) + 1)
        self.__allData["PedestrianSimulator"]["data"][
            "timePropagationParameters"]["time"] = {}
        self.__allData["PedestrianSimulator"]["data"][
            "timePropagationParameters"]["time"]["value"] = time
        self.__allData["PedestrianSimulator"]["data"][
            "timePropagationParameters"]["time"]["description"] = "time grid"

    def Model(self):
        self.readData()
        self.setTimePropagationParameters()

    def Control(self):
        pass

    def View(self):
        print "so far:"
        pprint(self.__allData)

    def __init__(self, inputFilename="UserInterface/testInput.json"):
        print "Pedestrian Simulator started at", os.getcwd()
        if inputFilename == None:
            raise SystemExit("Not input file was specified!")

        self.__inputFilename = inputFilename

        self.Model()
        self.View()

    def readData(self):
        print "Reading input file ", self.__inputFilename
        with open(self.__inputFilename) as data_file:
            data = json.load(data_file)

            self.__allData = data


if __name__ == "__main__":

    R1 = Reader()
