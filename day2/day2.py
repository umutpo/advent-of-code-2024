def isIncreasing(level: list[int]) -> bool:
    levelCount = len(level)
    
    positives = 0
    for i in range(1, levelCount):
        if level[i] - level[i - 1] > 0:
            positives += 1
    
    return (levelCount // 2) < positives 
    

def partOne(level: list[int]) -> tuple[bool, int]:
    levelCount = len(level)
    increasing = isIncreasing(level)
    
    for index in range(levelCount - 1):
        difference = level[index + 1] - level[index]
        isSafeIfIncreasing = increasing and difference <= 3 and difference >= 1
        isSafeIfDecreasing = increasing == False and difference >= -3 and difference <= -1
        if isSafeIfIncreasing == False and isSafeIfDecreasing == False:
            return False, index
        
    return True, levelCount

with open('./input.txt', 'r') as input_file:
    levels = list(map(lambda line : list(map(lambda level : int(level), line.split())), input_file.read().splitlines()))
    levelsCount = len(levels)

    safeLevelCountPartOne = 0
    safeLevelCountPartTwo = 0
    for i in range(levelsCount):
        level = levels[i]
        isSafe, lastIndex = partOne(level)
        if isSafe:
            safeLevelCountPartOne += 1
            safeLevelCountPartTwo += 1
        else:
            for k in range(len(level)):
                isSafeSkipped, lastIndex = partOne(level[:k] + level[k + 1:])
                if isSafeSkipped:
                    safeLevelCountPartTwo += 1
                    break
    
    print("Part 1: {}".format(safeLevelCountPartOne))
    print("Part 2: {}".format(safeLevelCountPartTwo))
    