def depthScan( depths ):
    i = 0
    depthIncreased = 0

    while i < len(depths) - 1:
        if depths[i] < depths[i+1]:
            depthIncreased += 1
        i += 1
    
    print("Depth Increase: " + str(depthIncreased))


depthScan( [1,23,4,26,36,80,79,90])