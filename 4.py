matrix = []
with open("./inputs/4.txt", "r") as file:
    for line in file:
        letters = list(line.strip())
        matrix.append(letters)

# PART 1
word = "XMAS"
rows = len(matrix)
cols = len(matrix[0]) if rows > 0 else 0
directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (1, 1),
    (-1, -1),
    (1, -1), 
    (-1, 1),
]

def is_valid(x, y):
    return 0 <= x < rows and 0 <= y < cols

def search_from(x, y, dx, dy):
    for i in range(len(word)):
        nx, ny = x + i * dx, y + i * dy
        if not is_valid(nx, ny) or matrix[nx][ny] != word[i]:
            return False
    return True

count = 0
for r in range(rows):
    for c in range(cols):
        for dx, dy in directions:
            if search_from(r, c, dx, dy):
                count += 1

print(f"Total occurrences of '{word}': {count}")

# PART 2
def is_valid(chars):
    return ''.join(chars) in ['MAS', 'SAM']

rows = len(matrix)
cols = len(matrix[0])
count = 0

for i in range(1, rows-1):
    for j in range(1, cols-1):
        if matrix[i][j] != 'A':
            continue
            
        top_left = [matrix[i-1][j-1], matrix[i][j], matrix[i+1][j+1]]
        top_right = [matrix[i-1][j+1], matrix[i][j], matrix[i+1][j-1]]
        
        if ((is_valid(top_right) and is_valid(top_left[::-1])) or
            (is_valid(top_left) and is_valid(top_right[::-1]))):
            count += 1

print(f"Number of X-MAS patterns found: {count}")