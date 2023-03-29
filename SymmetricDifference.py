first_set = set()
l = []
second_set = set()
n = int(input())
first_line = input()
first_num = first_line.split()

for i in first_num:
    first_set.add(int(i))
    
m = int(input())
second_line = input()
second_num = second_line.split()

for i in second_num:
    second_set.add(int(i))
    
total = first_set.symmetric_difference(second_set)

for i in total:
    l.append(i)
    
l.sort()

for i in l:
    print(i)
