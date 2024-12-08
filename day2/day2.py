def partOne(level: list[int]) -> tuple[bool, int]:
    levelCount = len(level)
    increasing = True if level[0] - level[levelCount - 1] < 0 else False
    
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

        print("Trying {}".format(level))
        if isSafe:
            print("\tSafe on first try")
            safeLevelCountPartOne += 1
            safeLevelCountPartTwo += 1
        else:
            newLevel = level[:lastIndex] + level[lastIndex + 1:]
            print("\tTrying again with {}".format(newLevel))
            
            isSafeSkipped = partOne(level[:lastIndex] + level[lastIndex + 1:])
            if isSafeSkipped:
                print("\tSafe on second try")
                safeLevelCountPartTwo += 1
    
    print("Part 1: {}".format(safeLevelCountPartOne))
    print("Part 2: {}".format(safeLevelCountPartTwo))
    