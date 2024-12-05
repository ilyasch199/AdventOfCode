import os

cwd = os.getcwd()
with open(cwd + '/inputs/1.txt', 'r') as file:
    data = file.readlines()
    col1 = []
    col2 = []
    for line in data:
        values = line.strip().split()
        if len(values) == 2:
            col1.append(int(values[0]))
            col2.append(int(values[1]))

# PART 1 
distances = []
col1.sort()
col2.sort()

for i in range(len(col1)):
    distances.append(abs(col1[i]-col2[i]))
print(f"Total sum of distances : {sum(distances)}")

# PART 2 
similarity = []
for c in col1:
    similarity.append(c*col2.count(c))
print(f"Total sum of similarities : {sum(similarity)}")
