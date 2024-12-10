matrix = []
with open("./inputs/6.txt", "r") as file:
    for line in file:
        sign = list(line.strip())
        matrix.append(sign)

# PART 1
def find_start_position(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '^':
                return i, j
    return None, None

def get_next_position(current_pos, direction):
    row, col = current_pos
    if direction == '^':
        return (row - 1, col)
    elif direction == '>':
        return (row, col + 1)
    elif direction == 'v':
        return (row + 1, col)
    else:
        return (row, col - 1)

def turn_right(direction):
    directions = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    return directions[direction]

def is_valid_position(pos, matrix):
    row, col = pos
    return (0 <= row < len(matrix) and 
            0 <= col < len(matrix[0]))

start_row, start_col = find_start_position(matrix)

visited = set()
current_pos = (start_row, start_col)
direction = '^'
visited.add(current_pos)

matrix_copy = [row[:] for row in matrix]
matrix_copy[start_row][start_col] = '.'

while True:
    next_pos = get_next_position(current_pos, direction)        
    if not is_valid_position(next_pos, matrix_copy):
        break           
    next_row, next_col = next_pos       
    if matrix_copy[next_row][next_col] == '#':
        direction = turn_right(direction)
    else:
        current_pos = next_pos
        visited.add(current_pos)    

print(f"{len(visited)} distinct positions")

# PART 2
