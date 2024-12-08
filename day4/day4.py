def findXmasCountFromX(matrix: list[list[str]], i: int, k: int) -> int:
    width, height = len(matrix[0]), len(matrix)
    
    found = 0
    
    # Check south
    if i < (height - 3):
        if matrix[i + 1][k] == 'M' and matrix[i + 2][k] == 'A' and matrix[i + 3][k] == 'S':
            found += 1
        
    # Check north
    if 0 <= (i - 3):
        if matrix[i - 1][k] == 'M' and matrix[i - 2][k] == 'A' and matrix[i - 3][k] == 'S':
            found += 1
    
    # Check east
    if k < (width - 3):
        if matrix[i][k + 1] == 'M' and matrix[i][k + 2] == 'A' and matrix[i][k + 3] == 'S':
            found += 1
    
    # Check west
    if 0 <= (k - 3):
        if matrix[i][k - 1] == 'M' and matrix[i][k - 2] == 'A' and matrix[i][k - 3] == 'S':
            found += 1
    
    # Check southeast
    if i < (height - 3) and k < (width - 3):
        if matrix[i + 1][k + 1] == 'M' and matrix[i + 2][k + 2] == 'A' and matrix[i + 3][k + 3] == 'S':
            found += 1
            
    # Check southwest
    if i < (height - 3) and 0 <= (k - 3):
        if matrix[i + 1][k - 1] == 'M' and matrix[i + 2][k - 2] == 'A' and matrix[i + 3][k - 3] == 'S':
            found += 1
    
    # Check northeast
    if 0 <= (i - 3) and k < (width - 3):
        if matrix[i - 1][k + 1] == 'M' and matrix[i - 2][k + 2] == 'A' and matrix[i - 3][k + 3] == 'S':
            found += 1
    
    # Check northwest
    if 0 <= (i - 3) and 0 <= (k - 3):
        if matrix[i - 1][k - 1] == 'M' and matrix[i - 2][k - 2] == 'A' and matrix[i - 3][k - 3] == 'S':
            found += 1
    
    return found

def isXmasFromA(matrix: list[list[str]], i: int, k: int) -> int:
    width, height = len(matrix[0]), len(matrix)
    if i == height - 1 or i == 0 or k == width - 1 or k == 0:
        return 0
    
    # M . S 
    # . A .
    # M . S
    if matrix[i - 1][k - 1] == 'M' and matrix[i + 1][k + 1] == 'S' and matrix[i + 1][k - 1] == 'M' and matrix[i - 1][k + 1] == 'S':
        return 1
    
    # M . M
    # . A .
    # S . S
    if matrix[i - 1][k - 1] == 'M' and matrix[i + 1][k + 1] == 'S' and matrix[i + 1][k - 1] == 'S' and matrix[i - 1][k + 1] == 'M':
        return 1
    
    # S . S
    # . A .
    # M . M
    if matrix[i - 1][k - 1] == 'S' and matrix[i + 1][k + 1] == 'M' and matrix[i + 1][k - 1] == 'M' and matrix[i - 1][k + 1] == 'S':
        return 1
    
    # S . M
    # . A .
    # S . M
    if matrix[i - 1][k - 1] == 'S' and matrix[i + 1][k + 1] == 'M' and matrix[i + 1][k - 1] == 'S' and matrix[i - 1][k + 1] == 'M':
        return 1
    
    return 0

with open('./input.txt', 'r') as input_file:
    input = input_file.read().splitlines()
    matrix = list(map(lambda row : [char for char in row], input))
    
    foundPartOne, foundPartTwo = 0, 0
    
    width, height = len(matrix[0]), len(matrix)
    for i in range(height):
        for k in range(width):
            if matrix[i][k] == 'X':
                foundPartOne += findXmasCountFromX(matrix, i, k)
            if matrix[i][k] == "A":
                foundPartTwo += isXmasFromA(matrix, i, k)
    
    print("Part 1: {}".format(foundPartOne))
    print("Part 2: {}".format(foundPartTwo))