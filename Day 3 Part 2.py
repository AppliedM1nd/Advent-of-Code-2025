file = open('aoc_day_3.txt','r')

arr = []

for line in file:
    line = line.strip().split()
    arr.append(line)
total = 0

for item in arr:
    new = list(item[0])
    val = ''
    current = -1
    for i in range(12):
        if i != 11:
            val += max(new[current+1:-11+i])
            prev = current
            current = new[current+1:-11+i].index(max(new[current+1:-11+i])) + prev + 1
        else:
            val += max(new[current + 1:])
            
    total += int(val)
   
print(total)
