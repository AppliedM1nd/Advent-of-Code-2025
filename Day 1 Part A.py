file = open('AOC_DAY_1_DATA.txt','r')

arr = []

for line in file:
    line = line.strip().split()
    arr.append(line)

print(arr)

total = 50
count = 0
for item in arr:
    if item[0][0] == 'R':
        total += int(item[0][1:])
    else:
        total -= int(item[0][1:])
    if total % 100 == 0:
        count += 1

print(count)
