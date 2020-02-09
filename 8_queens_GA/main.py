# Application of genetic algorithm on 8queen problem

from geneticAlgorithm import initializeRandomPopulation, crossover, mutation, sortPopulation, countThreat
from queenBoard import printBoard

populationSize = 20 # 一个种群中的个体数
chromosomeSize = 9 # Number of queens (genes in each chromosome)
iterations = 1000 # Number of iterations that genetic algorithm runs
mutationCount = 5 # Number of mutations in each iteration
crossoverCount = 5 # Number of crossovers in each iteration

population = initializeRandomPopulation(populationSize, chromosomeSize) # Initialize population (chromosomes)20*9

for iteration in range(0, iterations): # run from iteration 0 to total number of iterations defined above
    population = crossover(population, crossoverCount) # Apply genetic algorithm cross over, over the population
    population = mutation(population, mutationCount) # Apply genetic algorithm mutation, over the population
    population = sortPopulation(population) # sort the population by their value for selection part
    population = population[:populationSize] # select top chromosomes of population

#越靠前适应度越高
print("position vector of queens: " + str(population[0]))
print("number of queens threats: " + str(countThreat(population[0])))

printBoard(population[0], chromosomeSize)


