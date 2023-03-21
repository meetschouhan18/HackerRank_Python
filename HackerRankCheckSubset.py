n = int(input())
p = 0
first_set = set()
second_set = set()
for i in range(0 , n):
    num1 = int(input())
    line1 = input()
    l1 = line1.split()
    for j in l1:
        first_set.add(int(j))
    num2 = int(input())
    line2 = input()
    l2 = line2.split()
    for j in l2:
        second_set.add(int(j))
    for j in first_set:
        if j in second_set:
            p = p + 1
    if p == len(first_set):
        print("True")
    else:
        print("False")
    first_set = set()
    second_set = set()
    p = 0