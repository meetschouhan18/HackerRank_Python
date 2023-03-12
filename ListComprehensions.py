x = int(input())
y = int(input())
z = int(input())
n = int(input())
l = []
li = []
a = 0

for i in range(0 , x+1):
    for j in range(0 , y+1):
        for k in range(0 , z+1):
            a = i + j + k
            if a == n:
                a = 0
            else:
                l.append(i)
                l.append(j)
                l.append(k)
            if l != []:
                li.append(l)
            l = []

print(li)
