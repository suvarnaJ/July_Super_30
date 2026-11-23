l = [10,20,30,40,4,5,3,78,49,3,5]
dupl = []

for i in l:
    if l.count(i) > 1 and i not in dupl:
        dupl.append(i)

print("Duplicate ibers:", dupl)