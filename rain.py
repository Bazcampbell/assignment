import random
from object import Object, ObjectType
  # Class to simulate rain. Random chance for rain, and random 'flow' of rain.

class Rain():

    def __init__(self):
        self.isRaining = False


    def simulateRain(self,terrain, chance):

        print("### simulating rain ###")

        validSpot = []
        # Rain can flow in these valid spots.
        for row in range(len(terrain.terrainArray)):
            for col in range(len(terrain.terrainArray[row])):
                w = terrain.terrainArray[row][col]
                if w == ObjectType.Air.value:

                    validSpot.append((row, col))

        rainChance = random.uniform(0,1)

        # Chance of rain.
        if rainChance < chance:
            self.isRaining = True

            # The intensity of the rain
            flow = random.randint(5,60)
            for i in range(flow):
                pos = random.choice(validSpot)
                Water(pos, terrain)
        print("Raining: " + str(self.isRaining))


class Water():

    def __init__(self, pos, terrain):

        self.pos = pos
        self.terrain = terrain

        self.plotObject(self.terrain)

    def plotObject(self, terrain):

        x = self.pos[0]
        y = self.pos[1]
        terrain.terrainArray[x][y] = ObjectType.Water.value




