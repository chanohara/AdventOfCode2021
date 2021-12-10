def depthScan( depths ):
    
    depthIncreased = 0
    
    # Length must be at least 4 to compare 2 sliding windows
    if len(depths) < 4: 
        return
    
    i = 0
    while i < len(depths) - 3:
        windowLength = depths[i] + depths[i+1] + depths[i+2]
        nextWindowLength = depths[i+1] + depths[i+2] + depths[i+3]
        if windowLength  < nextWindowLength:
            depthIncreased += 1
        i += 1
    
    return depthIncreased


input = list( map( int , open( "/Users/dennisgauss/Documents/Coding/AdventOfCode2021/input_ex1.txt" ,"r").read().split('\n') ) )
print( depthScan( input ) )