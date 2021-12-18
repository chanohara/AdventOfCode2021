class Line:
    def __init__(self, start , end):

        self.start = [int(x) for x in start]
        self.end = [int(x) for x in end]

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

    if temp[axis] > line.end[axis]:
        iterations = temp[axis] - line.end[axis] + 1
    else:
        iterations = line.end[axis] - temp[axis] + 1

    for x in range( iterations ):
        board[temp[0]][temp[1]] += 1
        if line.end[axis] > temp[axis]:
            temp[axis] += 1
        else: 
            temp[axis] -= 1

def countNumOverlaps(board):
    result = 0
    for line in board:
        for number in line:
            if number > 1:
                result += 1
    return result


def determineOverlaps( input ):
    board = [ [ 0 for y in range( 1000 ) ] for x in range( 1000 ) ]
    lines = [ parseLine(line) for line in input ]

    for line in lines:
        if line.isVerticalOrHorizontal( ) != True:
            continue
        markLineOnBoard(board,line)

    return countNumOverlaps(board)

input = open( "/Users/dennisgauss/Documents/Coding/AdventOfCode2021/input_ex5.txt" ,"r").read().split('\n')
print( determineOverlaps(input) )