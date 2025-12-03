file = open('aoc_day_3.txt','r')

arr = []

for line in file:
    line = line.strip().split()
    arr.append(line)
total = 0
for item in arr:
    new = list(item[0])
    val = ''
    val += max(new)
    ind1 = new.index(max(new))
    if ind1 != len(new)-1:
        val += max(new[ind1+1:])
    else:
        new_val = max(new[:ind1])
        val = new_val + val

    total += int(val)
   
print(total)
