first_set = set()
second_set = set()
line = input()
l = line.split()
for j in l:
    first_set.add(int(j))
n = int(input())
p = 0
for i in range(0 , n):
    line1 = input()
    l1 = line1.split()
    for j in l1:
        second_set.add(int(j))
for j in second_set:
    if j in first_set:
        p += 1
if p == len(second_set):
    print("True")
else:
    print("False")