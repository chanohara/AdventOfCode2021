def calculateFishPop(days, population):
    for day in range(int(days)):
        temp = population.copy()
        population[8] = temp[0]
        population[7] = temp[8]
        population[6] = temp[7] + temp[0]
        population[5] = temp[6]
        population[4] = temp[5]
        population[3] = temp[4]
        population[2] = temp[3]
        population[1] = temp[2]
        population[0] = temp[1]

    totalPopulation = 0
    for pop in population:
        totalPopulation += pop 
    return totalPopulation 

def createStartPop(input):
    population = [0 for x in range(9)]

    for fish in input[0].split(','):
        population[int(fish)] += 1
    return population

input = open( "/Users/dennisgauss/Documents/Coding/AdventOfCode2021/input_ex6.txt" ,"r").read().split('\n')
print( calculateFishPop(256,createStartPop(input)) )