from itertools import product

test_values = []
remaining_numbers = []

with open("./inputs/7.txt", "r") as file:
    for line in file:
        first_part, rest = line.split(":")
        test_values.append(int(first_part.strip()))
        remaining_numbers.append(list(map(int, rest.strip().split())))

# PART 1
total_cal_results = 0
is_valid = False

for i in range(len(test_values)):
    is_valid = False 
    combinations = list(product("+*", repeat=len(remaining_numbers[i]) - 1))
    for operators in combinations:
        result = remaining_numbers[i][0]
        for j, operator in enumerate(operators):
            if operator == "+":
                result += remaining_numbers[i][j + 1]
            elif operator == "*":
                result *= remaining_numbers[i][j + 1]
        if result == test_values[i]:
            total_cal_results += result
            is_valid = True
            break

print(f"total calibration result : {total_cal_results}")

# PART 2 
total_cal_results = 0
is_valid = False

for i in range(len(test_values)):
    is_valid = False 
    combinations = list(product(["+", "*", "||"], repeat=len(remaining_numbers[i]) - 1))
    for operators in combinations:
        result = remaining_numbers[i][0]
        for j, operator in enumerate(operators):
            if operator == "+":
                result += remaining_numbers[i][j + 1]
            elif operator == "*":
                result *= remaining_numbers[i][j + 1]
            elif operator == "||":
                result = int(str(result) + str(remaining_numbers[i][j + 1]))
        if result == test_values[i]:
            total_cal_results += result
            is_valid = True
            break

print(f"total calibration result : {total_cal_results}")