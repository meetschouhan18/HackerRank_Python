#List

list = []
n = int(input("Enter Number of operations to perform :- "))

for i in range(0, n):
    o = input("")
    line = o.split()
    op = line[:1]
    operation = ''.join(map(str, op))
    if operation == 'insert':
        pos = line[1:2]
        position = int(''.join(map(str,pos)))
        elem = line[2:]
        element = int(''.join(map(str,elem)))
        list.insert(position, element)
    if operation == 'print':
        print(list)
    if operation == 'remove':
        elem = line[1:2]
        element = int(''.join(map(str,elem)))
        list.remove(element)
    if operation == 'append':
        elem = line[1:2]
        element = int(''.join(map(str,elem)))
        list.append(element)
    if operation == 'sort':
        list.sort()
    if operation == 'pop':
        index = len(list)
        list.pop(index - 1)
    if operation == 'reverse':
        list.reverse()
