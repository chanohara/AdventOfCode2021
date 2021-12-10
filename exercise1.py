def depthScan( depths ):
    i = 0
    depthIncreased = 0

    while i < len(depths) - 1:
        if depths[i] < depths[i+1]:
            depthIncreased += 1
        i += 1
    
    return depthIncreased

input = list( map( int , open( "/Users/dennisgauss/Documents/Coding/AdventOfCode2021/input_ex1.txt" ,"r").read().split('\n') ) )
print( depthScan( input ) )