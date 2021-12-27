def riskLevelSum(ground):
    riskLevelSum = 0
    for y ,line in enumerate(ground):
        for x ,point in enumerate(line):
            if isLowPoint(x,y,ground):
                riskLevelSum += point + 1
    return riskLevelSum

def isLowPoint(x,y,ground):
    if all ([isPosLarger(x-1,y-1,ground[y][x], ground),
             isPosLarger(x,y-1,ground[y][x], ground),
             isPosLarger(x+1,y-1,ground[y][x], ground),
             isPosLarger(x-1,y,ground[y][x], ground),
             isPosLarger(x+1,y,ground[y][x], ground),
             isPosLarger(x-1,y+1,ground[y][x], ground),
             isPosLarger(x,y+1,ground[y][x], ground),
             isPosLarger(x+1,y+1,ground[y][x], ground)]):
       return True
    else:
        return False
        
def isPosLarger(x,y,point,ground):
    if x > len(ground[0]) - 1 or x < 0:
        return True
    elif y > len(ground) - 1 or y < 0:
        return True
    elif point < ground[y][x]:
        return True
    else:
        return False


def parseGround(input):
    return [ [ int(point) for point in line ] for line in input ]

input = open( "/Users/dennisgauss/Documents/Coding/AdventOfCode2021/input_ex9.txt" ,"r").read().split('\n')
print(riskLevelSum(parseGround(input)))
