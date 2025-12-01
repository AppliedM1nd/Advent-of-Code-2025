file = open('AOC_DAY_1_DATA.txt','r')

arr = []

for line in file:
    line = line.strip().split()
    arr.append(line)

#print(arr)

total = 50
count = 0
for item in arr:
    before = total
    delta = int(item[0][1:]) * (1 if item[0][0] == 'R' else -1)
    
    click = 1 if delta > 0 else -1
    
    for i in range(abs(delta)):
        total = (total+click) % 100
        if total == 0:
            count += 1
        
print(count)
