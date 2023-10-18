from gardenPlot import flipCoords
import matplotlib.pyplot as plt
import abc
from enum import Enum
import matplotlib.pyplot as plt
import random
from object import ObjectType
import math


# Animal superclass. Classes of type animal inherit from this class for usability.

class AnimalType(Enum):

    Bee: str = 'bee'
    Ant: str = 'ant'
    Butterfly: str = 'butterfly'
    Bird: str = 'bird'

# life spans for the different animals. life span of 1 means it will die in 1 step.
class LifeSpan(Enum):

    Bird: int = 10000000
    Ant: int = 5000000
    Bee: int = 500000
    Butterfly: int = 500000


class Animal():

    def __init__(self, name, pos, colour, size, lifeSpan):
        self.name = name
        self.pos = pos
        self.colour = colour
        self.size = size
        self.lifeSpan = lifeSpan
        self.life = 0


    def getPos(self):
        return self.pos

    def plotMe(self, ax, LIMITS):
        XYpos = flipCoords(self.pos, LIMITS)
        circle1 = plt.Circle(XYpos, self.size, color=self.colour)
        ax.add_patch(circle1)

    @abc.abstractmethod
    def stepChange(self, terrain):
        return

    @abc.abstractmethod
    def checkLife(self):
        return

class Ant(Animal):

    def __init__(self, name, pos, colour="Red",size=0.25):
        super().__init__(name, pos, colour, size, lifeSpan=LifeSpan.Ant.value)

    # Takes in terrain as a parameter to check for tunnels.
    def stepChange(self,terrain) -> None:

        # each step adds one arbitrary value to the animal's life.
        self.life += 1

        self.checkLife()

        attempt = 0

        validMoves = [(0,0), (1,0), (-1,0), (0,1), (0,-1)]  # Von neumann neighbourhoods

        # Cycles through moves until a valid one is found. A 0 on the terrain represents a tunnel, which is a valid move.
        while True:
            move = random.choice(validMoves)
            attempt += 1
            newPos = (self.pos[0] + move[0], self.pos[1] + move[1])

            x = newPos[0]
            y = newPos[1]

            # try different moves
            if attempt > 6:
                return

            if terrain.terrainArray[x][y] == ObjectType.Tunnel.value:
                self.pos = newPos
                return



    def checkLife(self):

        if self.life == 0:
            return

        if self.life == math.ceil(self.lifeSpan / 3):
            self.size = self.size * 1.5

        if self.life == math.ceil((self.lifeSpan / 3) * 2):
            self.size = self.size * 1.5

        if self.life > self.lifeSpan:
            self.size = 0
            self.life = 0




class Butterfly(Animal):

    def __init__(self, name, pos):

        # Butterflies of random size and colour as per instructions
        colours = ["red","green","blue","pink","black","brown","orange"]
        size = random.uniform(0.1,1)

        super().__init__(name, pos, colour=random.choice(colours),size=size, lifeSpan=LifeSpan.Butterfly.value)


    def stepChange(self,terrain):

        # each step adds one arbitrary value to the animal's life.
        self.life += 1

        validMoves = [(1,0), (1,1), (1,-1), (-1,0), (-1,1), (-1,-1), (0,0), (0,-1), (0,1)]    # Moore neighbourhood - NW,N,NE,W,C,E,SW,S,SE

        attempt = 0

        self.checkLife()

        # If it is raining and the butterfly is next to a plant or tree, stay there.
        if terrain.getRain():

            x = self.getPos()[0]
            y = self.getPos()[1]

            left = x - 1
            right = x + 1

            if terrain.terrainArray[left][y] == ObjectType.Tree.value or terrain.terrainArray[right][y] == ObjectType.Tree.value:
                return
            if terrain.terrainArray[left][y] == ObjectType.Plant.value or terrain.terrainArray[right][y] == ObjectType.Plant.value:
                return

        # Cycles through moves until a valid one is found. An 8 on the terrain represents air, which is a valid move for the butterflies.
        while True:
            move = random.choice(validMoves)

            newPos = (self.pos[0] + move[0], self.pos[1] + move[1])

            x = newPos[0]
            y = newPos[1]

            attempt += 1
             # try different moves
            if attempt > 6:
                return

            # Stops the butterflies flying outside the terrain and only through the air.
            if x >= 0 and x <=44 and y >= 0 and y <= 49:
                if terrain.terrainArray[x][y] == ObjectType.Air.value:
                    self.pos = newPos
                    return


    def checkLife(self):

        if self.life == 0:
            return

        if self.life > self.lifeSpan:

            self.size = 0
            self.life = 0


# Bird animal added.
class Bird(Animal):

    def __init__(self, name, pos, colour="black",size=0.7):
        super().__init__(name, pos, colour, size, lifeSpan=LifeSpan.Bird.value)


    def stepChange(self,terrain):

        attempt = 0
        # each step adds one arbitrary value to the animal's life.
        self.life += 1

        validMoves = [(3,0), (3,3), (3,-3), (-3, 0), (-3,3), (-3,-3), (0,0), (0,-3), (0,3)]    # Moore neighbourhood - NW,N,NE,W,C,E,SW,S,SE. Can move 3 spaces in 1 move.

        self.checkLife()

        # 50% chance they will land in a tree at the same height every move.

        if random.uniform(0,1) >= 0.5:

            x = self.getPos()[0]

            for i in range(len(terrain.terrainArray[x])):

                if terrain.terrainArray[x][i] == ObjectType.Tree.value:

                    self.pos = (x, i)

                    return

         # Cycles through moves until a valid one is found. An 8 on the terrain represents air, which is a valid move for the birds.
        while True:
            move = random.choice(validMoves)

            attempt += 1
             # try different moves
            if attempt > 6:
                return

            newPos = (self.pos[0] + move[0], self.pos[1] + move[1])

            x = newPos[0]
            y = newPos[1]

            # Stops the birds flying outside the terrain and only through the air.
            if x >= 0 and x <=44 and y >= 0 and y <= 49:
                if terrain.terrainArray[x][y] == ObjectType.Air.value:
                    self.pos = newPos
                    return


    def checkLife(self):

        if self.life == 0:
            return

        # 0.01% chance the bird dies every turn.
        if random.uniform(0,1) < 0.0001:
            self.life = 0
            self.size = 0

        if self.life == math.ceil(self.lifeSpan / 4):
               self.size = self.size * 2

        if self.life == math.ceil(self.lifeSpan / 2):
            self.size = self.size * 2

        if self.life == math.ceil((self.lifeSpan / 4) * 3):
             self.size = self.size * 1.3

        if self.life > self.lifeSpan:
            self.size = 0
            self.life = 0


# Bee class. Moves the same as butterfly
class Bee(Animal):

    def __init__(self, name, pos, colour="brown",size=0.3):
        super().__init__(name, pos, colour, size, lifeSpan=LifeSpan.Bee.value)


    def stepChange(self,terrain):

        attempt = 0
        # each step adds one arbitrary value to the animal's life.
        self.life += 1

        self.checkLife()

        # If it is raining and the bee is next to a rock, stay there.
        if terrain.getRain():
            x = self.getPos()[0]
            y = self.getPos()[1]

            left = x - 1
            right = x + 1

            if terrain.terrainArray[left][y] == ObjectType.Rock.value or terrain.terrainArray[right][y] == ObjectType.Rock.value:
                return


        validMoves = [(1,0), (1,1), (1,-1), (-1,0), (-1,1), (-1,-1), (0,0), (0,-1), (0,1)]    # Moore neighbourhood - NW,N,NE,W,C,E,SW,S,SE

         # Cycles through moves until a valid one is found. An 8 on the terrain represents air, which is a valid move for the bees.
        while True:

            move = random.choice(validMoves)

            attempt += 1
             # try different moves
            if attempt > 6:
                return

            newPos = (self.pos[0] + move[0], self.pos[1] + move[1])

            x = newPos[0]
            y = newPos[1]

            # If bee is on a flower, 80% chance they will stay on it.
            if terrain.terrainArray[x][y-1] == ObjectType.Flower.value:
                if random.uniform(0,1) <= 0.8:
                    return

            # Stops the bees flying outside the terrain and only through the air.
            if x >= 0 and x <=44 and y >= 0 and y <= 49:
                if terrain.terrainArray[x][y] == ObjectType.Air.value:
                    self.pos = newPos
                    return


    def checkLife(self):

        if self.life == 0:
            return

        if self.life > self.lifeSpan:

            self.size = 0
            self.life = 0


