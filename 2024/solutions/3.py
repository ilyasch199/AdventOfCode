import re

with open('./inputs/3.txt', 'r') as file:
    file_content = file.read()

# PART 1
mul_pattern = r'mul\((\d+),(\d+)\)'
matches = re.finditer(mul_pattern, file_content)
total = 0

for match in matches:
    numbers = re.findall(r'\d+', match.group())
    num1, num2 = map(int, numbers)
    total+=(num1*num2)
print(f"sum of uncorrupted mul instructions : {total}") 

# PART 2
splits = re.split(r'(don\'t\(\)|do\(\))', file_content)
enabled = True
total = 0

for segment in splits:
    if segment == "don't()":
        enabled = False
    elif segment == "do()":
        enabled = True
    elif enabled:
        for match in re.finditer(mul_pattern, segment):
            num1, num2 = map(int, match.groups())
            total += num1 * num2

print(f"Sum of enabled multiplications: {total}")