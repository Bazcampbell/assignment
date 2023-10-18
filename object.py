# Parent class representing objects such as rocks, trees, etc.
# Input terrain on object instantiation to edit the map to include said object.
import math

import numpy as np
from enum import Enum

class ObjectType(Enum):

    Rock: int = 4
    Tree: int = 3
    Flower: int = 1
    Plant: int = 6
    Air: int = 8
    Grass: int = 7
    Tunnel: int = 0
    Water: int = 10
    Dirt: int = 2

class Object():

    def __init__(self, pos, type: ObjectType, width: int, height: int, terrain):

        self.type = type
        self.width = width
        self.height = height
        self.pos = pos

        # edit map to reflect the object
        self.plotObject(terrain)

    # Change terrain to include the object.
    def plotObject(self, terrain):
        x = self.pos[0]
        y = self.pos[1]

        # bottom left corner of object starts at pos
        # pos -> across width, up height

        mapHeight = len(terrain.terrainArray)
        # between the top of the object to the bottom (height is represented as array element in terrain array)

        for i in range(mapHeight - y - self.height, mapHeight - y):     # iterates through the y values the object will be drawn on
            for j in range(x, x + self.width):

                terrain.terrainArray[i][j] = self.type.value


class Rock(Object):

    def __init__(self, pos, width, height, terrain):

        super().__init__(pos, ObjectType.Rock, width, height, terrain)


class Flower(Object):

    def __init__(self, pos, height, terrain):

        super().__init__(pos, ObjectType.Flower, 1, height, terrain)



class Tree(Object):

    def __init__(self, pos, height, terrain):

        super().__init__(pos, ObjectType.Tree, 2, height, terrain)

    # Override super() plotObject, specific to a tree.
    def plotObject(self, terrain):

        x = self.pos[0]
        y = self.pos[1]

        # bottom left corner of object starts at pos
        # pos -> across width, up height

        mapHeight = len(terrain.terrainArray)

        # First 75% of the tree is brown to represent that trunk.
        w = math.ceil(self.height/3)
        counter = 0

        for i in range(mapHeight - y - self.height, mapHeight - y):     # iterates through the y values the object will be drawn on
            for j in range(x, x + self.width):
                if counter < w:
                    terrain.terrainArray[i][j] = ObjectType.Plant.value
                    counter += 1
                else:
                    terrain.terrainArray[i][j] = ObjectType.Tree.value



class Water(Object):

    def __init__(self, pos, terrain):

        super().__init__(pos, ObjectType.Water, 0.5, 0.5, terrain)

    def plotObject(self, terrain):

        x = self.pos[0]
        y = self.pos[1]

        terrain.terrainArray[x][y] = ObjectType.Water.value







