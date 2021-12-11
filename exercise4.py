def parseBoards( input ):

    bingoBoards = []
    currentBoard = []

    for line in input:
        if line == '' and len(currentBoard) != 0:
            bingoBoards.append(currentBoard.copy())
            currentBoard.clear()
        elif line != '':
            currentBoard.append(line.split())

    return bingoBoards

def markBoard( bingoNumber , bingoBoard ):
    for lineIndex, line in enumerate(bingoBoard):
        for columnIndex, number in enumerate(line):
            if number == bingoNumber:
                bingoBoard[lineIndex][columnIndex] = 'X'
                return

def checkBoardWon( bingoBoard ):

    # Check lines
    for line in bingoBoard:
        won = True 
        for number in line:
            if number != 'X':
                won = False
                break
        if won == True:
            return won
        else: 
            continue
    
    # Check columns
    column = 0
    while column < len(bingoBoard):
        won = True
        for line in bingoBoard:
            if line[column] != 'X':
                won = False
                break
        if won == True:
            return won
        else:
            column += 1



    return won

def calculateResult( bingoNumber, board ):
    sum = 0
    for line in board:
        for number in line:
            if number != 'X':
                sum += int(number)
    
    return int(bingoNumber) * int(sum)


def determineWinningBoard( bingoNumbers, bingoBoards):

    # check winners only after enough numbers called
    for number in bingoNumbers:
        for board in bingoBoards:
            markBoard(number,board)
            if checkBoardWon(board) == True:
                return calculateResult(number, board)

input = open( "/Users/dennisgauss/Documents/Coding/AdventOfCode2021/input_ex4.txt" ,"r").read().split('\n')
bingoNumbers = input[0].split(',')
input.pop(0)
bingoBoards = parseBoards( input )
print( determineWinningBoard( bingoNumbers, bingoBoards ) )
