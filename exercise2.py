def calculatePosition( navigationCommands ):
    horizontalPosition = 0
    depth = 0

    for command in navigationCommands:
        commandVals = command.split(" ")

        if commandVals[0] == 'forward':
            horizontalPosition += int(commandVals[1])
        elif commandVals[0] == 'up':
            depth -= int(commandVals[1])
        else:
            depth += int(commandVals[1])

    print("Horizontal: " , str(horizontalPosition) , " Depth: " , str(depth))


input = open( "/Users/dennisgauss/Documents/Coding/AdventOfCode2021/input_ex2.txt" ,"r").read().split('\n')
result = calculatePosition( input )   

