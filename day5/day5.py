with open("./input.txt", "r") as input_file:
    input_lines = input_file.read().splitlines()

    must_be_before = {}
    order_rules = []
    for input_line in input_lines:
        if input_line.find("|") != -1:
            before, after = list(map(lambda input: int(input), input_line.split('|')))
            if must_be_before.get(after) == None:
                must_be_before[after] = [ before ]
            else:
                must_be_before[after].append(before)
        elif input_line.find(",") != -1:
            rule = list(map(lambda input: int(input), input_line.split(',')))
            order_rules.append(rule)
    
    sum = 0
    sum2 = 0
    for rule in order_rules:
        n = len(rule)

        isCorrect = True
        for i in range(n - 1):
            dependencies = must_be_before.get(rule[i])
            if dependencies != None:
                for k in range(i + 1, n):
                    if rule[k] in dependencies:
                        isCorrect = False
                        break

        if isCorrect:
            sum += rule[n // 2]
        else:
            dependency = {}
            for i in range(n):
                dependencies = must_be_before.get(rule[i])
                dependency[rule[i]] = []
                if dependencies != None:
                    for k in range(n):
                        if i != k and rule[k] in dependencies:
                            dependency[rule[i]].append(rule[k])
            
            new_rule = []
            while len(rule) > 0:
                for rule_el in rule:
                    if len(dependency[rule_el]) == 0:
                        new_rule.append(rule_el)
                        rule.remove(rule_el)
                        for i, k in enumerate(dependency):
                            if rule_el in dependency[k]:
                                dependency[k].remove(rule_el)

            sum2 += new_rule[n // 2]

    print("Part 1: {}".format(sum))
    print("Part 2: {}".format(sum2))