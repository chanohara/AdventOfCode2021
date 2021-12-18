class Line:
    def __init__(self, start , end):
        if end >= start:
            self.start = [int(x) for x in start]
            self.end = [int(x) for x in end]
        else:
            self.start = [int(x) for x in end]
            self.end = [int(x) for x in start]

    def isVerticalOrHorizontal( self ):
        if self.start[0] != self.end[0] and self.start[1] != self.end[1]:
            return False
        else:
            return True

    def getAxisToIterate( self ):
        if self.start[0] == self.end[0]:
            return 1
        else:
            return 0

def parseLine(line):
    lineTuple = line.split('->')
    return Line( lineTuple[0].strip().split(',') , lineTuple[1].strip().split(',') )

def markLineOnBoard(board, line):
    axis = line.getAxisToIterate( )
    temp = line.start.copy()

    while temp[axis] <= line.end[axis]:
        board[temp[0]][temp[1]] += 1
        temp[axis] += 1

def countNumOverlaps(board):
    result = 0
    for line in board:
        for number in line:
            if number > 1:
                result += 1
    return result


def determineOverlaps( input ):
    board = [ [ int(0) for y in range( 1000 ) ] for x in range( 1000 ) ]
    lines = [ parseLine(line) for line in input ]

    for line in lines:
        if line.isVerticalOrHorizontal( ) != True:
            continue
        markLineOnBoard(board,line)

    return countNumOverlaps(board)

input = open( "/Users/dennisgauss/Documents/Coding/AdventOfCode2021/input_ex5.txt" ,"r").read().split('\n')
print( determineOverlaps(input) )