import re

with open('./input.txt', 'r') as input_file:
    input = input_file.read()
    
    doIter = re.finditer("do()", input)
    doIndices = [m.start(0) for m in doIter]
    
    dontIter = re.finditer("don't()", input)
    dontIndices = [m.start(0) for m in dontIter]
    
    iter = re.finditer(r"mul\([0-9]{1,3},[0-9]{1,3}\)", input)
    indices = [m.start(0) for m in iter]
    
    currentDo = True
    
    sum = 0
    for startingIndex in indices:
        if len(doIndices) > 0:
            if startingIndex > doIndices[0]:
                currentDo = True
                doIndices.pop(0)
        
        if len(dontIndices) > 0:
            if startingIndex > dontIndices[0]:
                currentDo = False
                dontIndices.pop(0)            
        
        if currentDo:
            closingIndex = input.find(")", startingIndex)
            numberStr = input[startingIndex + 4 : closingIndex]
            numbers = list(map(lambda num : int(num), numberStr.split(",")))
            sum += (numbers[0] * numbers[1])
    
    print("Part 1: {}".format(sum))