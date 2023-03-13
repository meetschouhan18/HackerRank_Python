#Tuples
#Taking number as input in tuple and showing hash value

n = int(input("Enter number of elements :- "))
o = input("Enter elements :- ")
m = o.split()
l = []
for i in m:
    l.append(int(i))
t = tuple(l)
print(t)
print(hash(t))