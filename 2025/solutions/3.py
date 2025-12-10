with open('2025/inputs/3.txt') as f:
    lines = f.read().strip().splitlines()

## PART 1
total_output_joltage = 0

for l in lines:
    best = 0
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            num = int(l[i] + l[j])
            if num > best:
                best = num
    total_output_joltage += best

print(total_output_joltage)

## PART 2
k = 12
total_output_joltage = 0

for line in lines:
    stack = []
    to_remove = len(line) - k

    for d in line:
        while stack and to_remove > 0 and stack[-1] < d:
            stack.pop()
            to_remove -= 1

        stack.append(d)

    best = int("".join(stack[:k]))
    total_output_joltage += best

print(total_output_joltage)