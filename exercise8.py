def countUniqueNumbers(input):
    result = 0
    for line in input:
        for number in line:
            length = len(number)
            if length in (2,3,4,7):
                result += 1
    return result

def parseInput(input):
    return [x.split('|')[1].split() for x in input]

input = open( "/Users/dennisgauss/Documents/Coding/AdventOfCode2021/input_ex8.txt" ,"r").read().split('\n')
print(countUniqueNumbers(parseInput(input)))