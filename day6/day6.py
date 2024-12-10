def getNextPosition(matrix: list[list[str]], i: int, j: int):
    height, width = len(input), len(input[0])
    guard_direction = matrix[i][j]
    
    if guard_direction == ">":
        if j + 1 >= width:
            return ">", (i, j + 1)
        elif matrix[i][j + 1] == "#":
            return "v", (i, j)
        else:
            return ">", (i, j + 1)
    elif guard_direction == "<":
        if j - 1 < 0:
            return "<", (i, j - 1)
        elif matrix[i][j - 1] == "#":
            return "^", (i, j)
        else:
            return "<", (i, j - 1)
    elif guard_direction == "^":
        if i - 1 < 0:
            return "^", (i - 1, j)
        elif matrix[i - 1][j] == "#":
            return ">", (i, j)
        else:
            return "^", (i - 1, j)
    elif guard_direction == "v":
        if i + 1 >= height:
            return "v", (i + 1, j)
        elif matrix[i + 1][j] == "#":
            return "<", (i, j)
        else:
            return "v", (i + 1, j)
            
        

with open("./input.txt", "r") as input_file:
    input = input_file.read().splitlines()
    input = [[ch for ch in row] for row in input]
    
    height, width = len(input), len(input[0])
    
    guard_position = (-1, -1)
    for i in range(height):
        for j in range(width):
            char = input[i][j]
            if char == ">" or char == "<" or char == "^" or char == "v":
                guard_position = (i, j)
                break
        
        if guard_position != (-1, -1):
            break
    
    visited = set()
    
    while True:
        direction, position = getNextPosition(input, guard_position[0], guard_position[1])
        if position[0] >= height or position[0] < 0 or position[1] >= width or position[1] < 0:
            break
        else:
            input[guard_position[0]][guard_position[1]] = "."
            input[position[0]][position[1]] = direction    
            guard_position = position
            visited.add(position)
    
    print("Part 1: {}".format(len(visited)))