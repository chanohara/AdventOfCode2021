import math

def getSumOfDigits( input ):

    sum = 0
    for digit in input:
        sum += int(digit)
    
    return sum

def getMostCommonDigit( input ):

    sum = getSumOfDigits( input )

    if sum > len(input) * 0.5:
        mostCommonDigit = 1
    elif sum < len(input) * 0.5: 
        mostCommonDigit = 0
    else: 
        mostCommonDigit = 1

    return mostCommonDigit

def getLeastCommonDigit( input ):

    return 0 if int( getMostCommonDigit( input ) ) == 1 else 1


def calculateOxygenRating( input ):
    temp = input.copy()
    i = 0
    while i < len(input[0]):

        # get most common didget at position
        mostCommonDidget = getMostCommonDigit([x[i] for x in temp])

        j = 0
        while j < len(temp):
            if int(temp[j][i]) != mostCommonDidget:
                temp.pop(j)
            else:
                j += 1

        if len(temp) == 1:
            break
        else:
            i += 1

    return temp[0]

def calculateCO2Rating( input ):
    temp = input.copy()
    i = 0
    while i < len(input[0]):

        # get least common didget at position
        leastCommonDidget = getLeastCommonDigit([x[i] for x in temp])

        j = 0
        while j < len(temp):
            if int(temp[j][i]) != leastCommonDidget:
                temp.pop(j)
            else:
                j += 1

        if len(temp) == 1:
            break
        else:
            i += 1

    return temp[0]

input = open( "/Users/dennisgauss/Documents/Coding/AdventOfCode2021/input_ex3.txt" ,"r").read().split('\n')

oxygenRating = calculateOxygenRating( input )
co2Rating = calculateCO2Rating( input )


print( int(oxygenRating, 2) * int(co2Rating, 2) )