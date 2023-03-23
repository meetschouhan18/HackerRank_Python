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
    if op[0] != "pop":
        try:
            a = int(op[1])
        except:
            for i in first_set:
                b = b + int(i)
            print(b)
            break
    if op[0] == "pop":
        c = first_set.pop()
    if op[0] == "remove":
        first_set.remove(int(op[1]))
    if op[0] == "discard":
        first_set.discard(int(op[1]))
        
if b == 0:
    c = str()
    if first_set == set():
        print("0")
    else:
        c = 0
        for i in first_set:
            c = c + int(i)
        print(c)
