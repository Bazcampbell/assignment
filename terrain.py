# Terrain class, includes map and rain functionality.
import random
from rain import Rain

class Terrain():

    def __init__(self, terrain):

        self.terrainArray = terrain
        self.rain = Rain()


    def simulateRain(self,chance):
        self.rain.simulateRain(terrain=self,chance=chance)

    def getRain(self):

        return self.rain.isRaining
