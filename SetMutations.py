first_set = set()
b = 0
second_set = set()
n = int(input())
first_line = input()
first_num = first_line.split()

for i in first_num:
    first_set.add(int(i))
    
m = int(input())

for i in range(0 , m):
    operation = input()
    op = operation.split()
    
    if op[0] == "intersection_update":
        line1 = input()
        data = line1.split()

        for j in data:
            second_set.add(int(j))
            
        first_set.intersection_update(second_set)
        second_set = set()
        
    if op[0] == "update":
        line1 = input()
        data = line1.split()
    
        for j in data:
            second_set.add(int(j))
            
        first_set.update(second_set)
        second_set = set()
        
    if op[0] == "symmetric_difference_update":
        line1 = input()
        data = line1.split()
        
        for j in data:
            second_set.add(int(j))
            
        first_set.symmetric_difference_update(second_set)
        second_set = set()
        
    if op[0] == "difference_update":
        line1 = input()
        data = line1.split()
        
        for j in data:
            second_set.add(int(j))
            
        first_set.difference_update(second_set)
        second_set = set()
        
if b == 0:
    c = str()
    if first_set == set():
        print("0")
    else:
        c = 0
        for i in first_set:
            c = c + int(i)
        print(c)
