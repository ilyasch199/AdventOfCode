rules = []
updates = []
with open("./inputs/5.txt", "r") as file:
    is_update = False
    for line in file:
        line = line.strip()
        if not line:
            is_update = True
            continue
        if is_update:
            updates.append([int(num) for num in line.split(",")])
        else:
            rules.append([int(num) for num in line.split("|")])

# PART 1
sum_middle = 0
for update in updates:
    valid = True
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[1]) < update.index(rule[0]):
                valid = False
                break
    
    if valid:
        middle = update[len(update) // 2]
        sum_middle += middle

print(f"Sum of middle numbers from valid updates: {sum_middle}")

# PART 2
sum_middle = 0
for update in updates:
    needs_correction = False
    
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[1]) < update.index(rule[0]):
                needs_correction = True
                break
    
    if needs_correction:
        deps = {x: set() for x in update}
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                deps[rule[1]].add(rule[0])
        
        result = []
        visited = set()
        
        def topo_sort(n):
            visited.add(n)
            for dep in deps[n]:
                if dep not in visited:
                    topo_sort(dep)
            result.append(n)
            
        for n in update:
            if n not in visited:
                topo_sort(n)
                
        sum_middle += result[len(result)//2]

print(f"Sum of middle numbers from incorrectly-ordered updates: {sum_middle}")
