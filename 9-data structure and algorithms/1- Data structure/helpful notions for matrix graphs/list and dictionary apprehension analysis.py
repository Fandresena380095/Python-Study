l = []

def add(x):
    for row in l:
        row.append(x)
    l.append([x] * (len(l)+1))
    print(l)



add(0)
add(0)
add(0)
add(0)

indices = {'A':0,'B':1,'C':2,'D':3}

for v,i in indices.items():
    print(v+' ',end='')
    for x in range(len(l)):
        print(l[i][x], end=" ")
    print()


