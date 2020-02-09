import numpy as np
import random
population = []
for i in range(20):
    population.append(np.random.randint(low=0, high=8, size=(9)))
#print(population)
for currentGene in range(0, len(population)):
    
    #queen[x,y]
    currentQueen = [currentGene, population[currentGene]]
    print(len(population[currentGene]))
    #print(currentQueen)
    #check all queens before current queen for threats
    for previousGene in range (0, currentGene):
        previousQueen = [previousGene, population[previousGene]]
        print(previousQueen[1][0])
        for i in range(9):
            slope = (currentQueen[1][i] - previousQueen[1][i]) / (currentQueen[0] - previousQueen[0])
            



