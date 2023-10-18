from animal import *

def runDemo():

    animals = []

    for i in range(5):
        animals.append(Ant(name=f"A{i}", pos=(40, 28 + (i * 2))))  # sequential starting points.
        animals.append(Butterfly(name=f"B{i}", pos=(5, 10 + (i * 7))))
        animals.append(Bird(name=f"Bird{i}", pos=(10,5 + (i * 7))))
        animals.append(Bee(name=f"Bee{i}", pos=(10, 5 + (i * 4))))

    return animals

