import math

class Alignment:

    def __init__(self, positions):
        self.positions = positions
        self.max = 0
        self.min = 0

    def determineMinMax(self):
        for position in self.positions:
            if position > self.max:
                self.max = position
            if position < self.min:
                self.min = position

    def determineCostofLocation(self, location):
        cost = 0
        distance = 0
        for position in self.positions:
            distance = abs(location - position)
            cost += (distance * (distance + 1 ) // 2)
        return cost 

    def determineCheapestLocation(self):
        self.determineMinMax()
        cheapestCost = math.inf
        for location in range(self.min,self.max):
            currentCost = self.determineCostofLocation(location)
            if currentCost < cheapestCost:
                cheapestCost = currentCost
        return cheapestCost

input = open( "/Users/dennisgauss/Documents/Coding/AdventOfCode2021/input_ex7.txt" ,"r").read().split(',')
integerInput = [int(x) for x in input]
print( Alignment(integerInput).determineCheapestLocation())