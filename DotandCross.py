import numpy as np
n = int(input())
lst_a = []
lst_b = []

for i in range(0 ,n):
   line = [*map(int , input().split())]
   for j in line:
      lst_a.append(j)

for i in range(0 ,n):
   line = [*map(int , input().split())]
   for j in line:
      lst_b.append(j)

a = np.array(lst_a)
a.resize(n,n)
b = np.array(lst_b)
b.resize(n,n)
print(np.dot(a,b))
print(np.cross(a,b))
