#Nested List
#print names of students who scored second lowest in alphabetical order

dict = {}
sample = {}
l = []
m = 100
n = int(input('Enter number of students :- '))
for i in range(0 , n):
    name = input("Enter Name :- ")
    marks = float(input('Enter Marks :- '))
    dict[name] = marks
    sample[name] = marks
    l.append(marks)
for key,value in sample.items():
    if m >= value:
        name1 = key
        marks1 = value
        m = value
j = len(l)
for i in range(0, j-1):
    if m in l:
        l.remove(m)
m = 100
second = []
for i in l:
    if m >= i:
        m = i
for key,value in sample.items():
    if value == m:
        second.append(key)
second.sort()
for i in second:
    print(i)