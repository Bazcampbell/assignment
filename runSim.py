from userInput import userInput
from object import *
from animal import *

# Class to handle user input and pass through to parameters


# Function to handle object creation
def objectInput(terrain) -> list:

    objects = []

    while True:

        object = userInput.getInput("Enter object name: rock, flower, tree or enter nothing if done: ")

        if object == "":
            return objects

        if object.lower() == "rock":
            pos = userInput.getInput("Enter object position as x, y: ").split(',')
            pos = (int(pos[0]),int(pos[1]))
            width = int(userInput.getInput("Enter width of rock: "))
            height = int(userInput.getInput("Enter height of rock: "))
            objects.append(Rock(pos,width,height,terrain))

        if object.lower() == 'tree':
            pos = userInput.getInput("Enter object position as x, y: ").split(',')
            pos = (int(pos[0]),int(pos[1]))
            height = int(userInput.getInput("Enter height of tree: "))
            objects.append(Tree(pos,height,terrain))

        elif object.lower() == 'flower':
            pos = userInput.getInput("Enter object position as x, y: ").split(',')
            pos = (int(pos[0]),int(pos[1]))
            height = int(userInput.getInput("Enter height of flower: "))
            objects.append(Flower(pos,height,terrain))



def parametersInput(terrain):

    print("### Starting Simulation ###")

    steps = int(userInput.getInput("How many simulation steps? "))

    rainChance = int(userInput.getInput("Chance of rain as a % ? "))

    terrain.simulateRain(rainChance / 100)

    return steps

def animalInput():

    animals = []
    counter = 0

    while True:
        counter += 1
        animal = userInput.getInput("Enter animal name: Ant, Bird, Bee, Butterfly or enter nothing if done: ")

        if animal == "":
            return animals

        pos = userInput.getInput("Enter position as (x,y): ").split(',')
        pos = (int(pos[1]),int(pos[0]))

        if animal.lower() == AnimalType.Bird.value:
            bird = Bird(f"Bird{counter}",pos)
            animals.append(bird)

        elif animal.lower() == AnimalType.Bee.value:
            bee = Bee(name=f"Bee{counter}",pos=pos)
            animals.append(bee)

        elif animal.lower() == AnimalType.Butterfly.value:
            butterfly = Butterfly(f"Butterfly{counter}",pos)
            animals.append(butterfly)

        elif animal.lower() == AnimalType.Ant.value:
            ant = Ant(f"Ant{counter}",pos)
            animals.append(ant)








