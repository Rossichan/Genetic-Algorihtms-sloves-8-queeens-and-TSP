import numpy as np
import random
#计算适应度
def countThreat (population):
    threat = 0
    #count threats for each queen
    for currentGene in range(0, len(population)):

        #queen[x,y]
        currentQueen = [currentGene, population[currentGene]]
        #check all queens before current queen for threats
        for previousGene in range (0, currentGene):
            previousQueen = [previousGene, population[previousGene]]
            '''
            我感觉这里有bug，因为currnetQueen形如[1,[arr(1,2,3,4,5..9)]]。所有计算slope应当是
            currentQueen[1][i] - previousQueen[1][i]。但总是报错，必须以下形式
            '''
            slope = (currentQueen[1] - previousQueen[1]) / (currentQueen[0] - previousQueen[0])
            #check for horizental threat
            #two queens must form a line with slope 0
            if slope == 0:
                threat += 1
                break

                #check for diagonal threat
                #two queens must form a line with slop either 1 or -1
            elif slope == 1 or slope == -1:
                threat += 1
                break

    return threat

#初始化种群
def initializeRandomPopulation (populationSize, chromosomeSize): # initializing population randomly
    population = []
    for i in range(populationSize):
        population.append(np.random.randint(low=0, high=chromosomeSize-1, size=(chromosomeSize))) # using numpy library to initialize population with size of chromosome size with random values between 0 to 7

    return population

#按照适应度选择个体，淘汰适应度低的个体
def sortPopulation (population):
    #按threat升序排列
    population.sort(key=countThreat) # python built in sort with preferred function as key
    return population

#杂交
def crossover(population, crossoverCount):
    chromosomeLenght = len(population[0])  #每个个体染色体包含的基因数
    for i in range(0, crossoverCount): # run cross over as many times as we want
        #从random.choice从数组中选择一个个体。从种群中选择一个个体
        crossoverParent1 = random.choice(population) # selects first parent randomly
        crossoverParent2 = random.choice(population) # selects second parent randomly

        crossoverPoint = random.randint(1, chromosomeLenght-1) # selects point for cross over randomly between genes 1 to 6

        child1 = [] # initialize first child
        child1.extend(crossoverParent1[:crossoverPoint]) # add genes of first parent from first gene to cross over point gene
        child1.extend(crossoverParent2[crossoverPoint:]) # add genes of second parent from cross over gene to last gene
        child2 = [] # initialize second child
        child2.extend(crossoverParent2[:crossoverPoint]) # add genes of second parent from first gene to cross over point gene
        child2.extend(crossoverParent1[crossoverPoint:]) # add genes of first parent from cross over gene to last gene

        population.append(child1) # add first child to whole population
        population.append(child2) # add second child to whole population

    return population

#变异
def mutation(population, mutationCount):
    chromosomeLenght = len(population[0])
    for i in range(0, mutationCount):  # run mutation as many times as we want
        mutationParent = random.choice(population) # selects a random chromosome

        mutationPoint = random.randint(0, chromosomeLenght-1) # selects a random gene
        mutationGene = random.randint(0, chromosomeLenght-1) # selects a random value for selected gene

        child = mutationParent # create a child for mutation
        child[mutationPoint] = mutationGene # mutate

        population.append(child) # add child to whole population

    return population


