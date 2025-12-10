with open('2025/inputs/2.txt') as f:
    line = f.read().strip()

parts = line.split(',')
ranges_list = []
for part in parts:
    start_str, end_str = part.split('-')
    ranges_list.append((int(start_str), int(end_str)))

## PART 1

count_inv_ids = 0
for start, end in ranges_list:
    for i in range(start, end):
        s = str(i)
        if len(s) % 2 == 0 :
            mid = len(s) // 2
            if s[:mid] == s[mid:]:
                count_inv_ids += i

print("PART 1 : the sum of all the invalids IDs : ", count_inv_ids)

## PART 2

count_inv_ids = 0
for start, end in ranges_list:
    for i in range(start, end):
        s = str(i)
        l = len(s)

        for j in range(2, l+1):
            if l % j != 0:
                continue
            
            block_len = l // j
            block = s[:block_len]

            if block * j == s:
                count_inv_ids += i
                break

print("PART 2 : the sum of all the invalids IDs : ", count_inv_ids)