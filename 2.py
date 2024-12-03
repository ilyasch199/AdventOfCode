matrix = []
with open("./inputs/2.txt", "r") as file:
    for line in file:
        numbers = list(map(int, line.split()))
        matrix.append(numbers)

# PART 1
safe = 0
for row in matrix:
    increasing = all(row[i] < row[i + 1] for i in range(len(row) - 1))
    decreasing = all(row[i] > row[i + 1] for i in range(len(row) - 1))

    if (increasing or decreasing) and all(1 <= abs(row[i + 1] - row[i]) <= 3 for i in range(len(row) - 1)):
        safe+=1

print(f"Part 1 : {safe}")

# PART 2
safe = 0 
for row in matrix:
    # Same as Part 1
    increasing = all(row[i] < row[i + 1] for i in range(len(row) - 1))
    decreasing = all(row[i] > row[i + 1] for i in range(len(row) - 1))
    if (increasing or decreasing) and all(1 <= abs(row[i + 1] - row[i]) <= 3 for i in range(len(row) - 1)):
        safe += 1
        continue
    
    # Check each row with 1 single level missing
    for j  in range(len(row)):
        modified_row = row[:j] + row[j+1:]
        increasing = all(modified_row[i] < modified_row[i + 1] for i in range(len(modified_row) - 1))
        decreasing = all(modified_row[i] > modified_row[i + 1] for i in range(len(modified_row) - 1))

        if (increasing or decreasing) and all(1 <= abs(modified_row[i + 1] - modified_row[i]) <= 3 for i in range(len(modified_row) - 1)):
            safe += 1
            break

print(f"Part 2 : {safe}")
