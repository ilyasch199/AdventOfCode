with open('2025/inputs/1.txt') as f:
    lines = [line.strip() for line in f]

rotations = [line[0] for line in lines]
numbers = [int(line[1:]) for line in lines]

## PART 1
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

print("PART 1 : password is", zero_counter)

## PART 2
dial_point = 50
zero_counter = 0

for rotation, number in zip(rotations, numbers):
    if rotation == 'R':
        offset = (100 - dial_point) % 100
        first_k = offset if offset != 0 else 100
    else:
        offset = dial_point % 100
        first_k = offset if offset != 0 else 100

    if number > 1 and first_k <= number - 1:
        hits_mid = 1 + ((number - 1) - first_k) // 100
        zero_counter += hits_mid

    if rotation == 'R':
        dial_point = (dial_point + number) % 100
    else:
        dial_point = (dial_point - number) % 100

    if dial_point == 0:
        zero_counter += 1

print("PART 1 : password is", zero_counter)