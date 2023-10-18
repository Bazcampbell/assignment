import matplotlib.pyplot as plt
import numpy as np
import csv
from rain import Rain
import garden
from terrain import Terrain
from runSim import *
from garden import *
from runDemo import runDemo


def getSubgrid(t, pos):
    rmin = pos[0] - 1
    rmax = pos[0] + 1
    cmin = pos[1] - 1
    cmax = pos[1] + 1
    #print(rmin, rmax, cmin, cmax)
    sub = t[rmin:rmax, cmin:cmax]
    return sub


# takes CSV file name as input, outputs a 2D array as a nested list. Converts str -> int
def readMap(file: str) -> list:
    map = []

    with open(file, mode='r') as file:
        reader = csv.reader(file)

        for row in reader:
            map.append(row)

        for r in range(len(map)):
            for c in range(len(map[r])):
                map[r][c] = int(map[r][c])

    return map


# function to calculate limits of the map plot.
def limits(map: list) -> tuple:
    rows = len(map)
    cols = len(map[0])

    return (rows, cols)


def main():

    timestep = 0

    LIMITS = (50,50)
    map = readMap('garden3.csv')
    terrain = Terrain(np.array(map))

    plt.figure(figsize=(8, 8))  # size of the plot printout
    ax = plt.axes()
    ax.set_aspect("equal")

    demo = int(input("Press 1 to run demo or 2 to manually enter parameters: "))


    if demo == 2:
        steps = runSim.parametersInput(terrain)
        runSim.objectInput(terrain)
        animals = runSim.animalInput()

    elif demo == 1:

        animals = runDemo()

        R = Rock((5,30),10,5,terrain)
        T = Tree((30,30),10,terrain)
        F = Flower((10,30),5,terrain)

        steps = 1000
        rainChance = 50
        terrain.simulateRain(rainChance / 100)
    else:
        print("Wrong input")

    plt.imshow(terrain.terrainArray)


    # step change
    for step in range(steps):
        timestep += 1
        for i in animals:
            i.stepChange(terrain)
#
    # plot animals
    for animal in animals:
        animal.plotMe(ax, LIMITS)


    plt.title(f"Time Step: {timestep}", fontsize="18")
    plt.set_cmap('terrain_r')
    plt.grid()
    plt.show()
    # plt.pause(1)
    # plt.cla()


if __name__ == "__main__":
    main()
