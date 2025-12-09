with open('2025/inputs/1.txt') as f:
    lines = [line.strip() for line in f]

rotations = [line[0] for line in lines]
numbers = [int(line[1:]) for line in lines]
dial_point = 50
zero_counter = 0

for rotation, number in zip(rotations, numbers):
    if rotation == 'R':
        dial_point += number
        dial_point %= 100
    elif rotation == 'L':
        dial_point -= number
        if dial_point < 0:
            dial_point %= 100 
    if dial_point == 0:
        zero_counter += 1

print("password is", zero_counter)