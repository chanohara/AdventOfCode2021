def calculateGammaRate( input ):

    sumArray = [0 for digit in input[0]]
    gammaArray = sumArray

    for binary in input:
        i = 0
        for digit in binary:
            sumArray[i] += int(digit)
            i += 1

    i = 0
    for digit in sumArray:
        if digit > len(input) * 0.5:
            gammaArray[i] = 1
        else:
            gammaArray[i] = 0
        i += 1

    return gammaArray


def calculateEpsilonFromGamma( gamma ):

    return [ 1 if int(digit) == 0 else 0 for digit in str(gamma)]



input = open( "/Users/dennisgauss/Documents/Coding/AdventOfCode2021/input_ex3.txt" ,"r").read().split('\n')

gamma = int("".join(map(str, calculateGammaRate( input ))))
epsilon = int("".join(map(str, calculateEpsilonFromGamma( gamma ))))

print("Power Consumption: " , int(str(gamma),2) * int(str(epsilon),2))