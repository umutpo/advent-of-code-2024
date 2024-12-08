import heapq

def partOne(left: list[int], right: list[int]) -> int:
    heapq.heapify(left)
    heapq.heapify(right)
    
    distances = 0
    while len(left) > 0 and len(right) > 0:
        distances += abs(heapq.heappop(left) - heapq.heappop(right))
    
    return distances

def partTwo(left: list[int], right: list[int]) -> int:
    rightFreqs = {}
    for el in right:
        if rightFreqs.get(el) == None:
            rightFreqs[el] = 1
        else:
            rightFreqs[el] += 1
    
    total = 0
    for el in left:
        frequency = 0 if rightFreqs.get(el) == None else rightFreqs[el]
        total += el * frequency
    
    return total

with open("input.txt", "r") as input_file:
    lines = input_file.read().splitlines()

    left = []
    right = []
    for line in lines:
        numbers = line.split()
        if len(numbers) == 2:
            left.append(int(numbers[0]))
            right.append(int(numbers[1]))
    
    total = partTwo(left, right)
    distances = partOne(left, right)
    
    print("Part 1: {}".format(distances))
    print("Part 2: {}".format(total))