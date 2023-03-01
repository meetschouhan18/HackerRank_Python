line = input()
q = []
group_a = []
group_b = []
num = line.split()
for i in range(0 , int(num[0])):
    a = input()
    group_a.append(a)
for i in range(0 , int(num[1])):
    b = input()
    group_b.append(b)
for i in group_b:
    c = 0
    b = str()
    while c != len(group_a):
        if i == group_a[c]:
            b = b + str(c+1) + " "
        c = c + 1
    if i not in group_a:
        b = str(-1)
    p = b.split()
    q.append(" ".join(p))
print("\n".join(q))