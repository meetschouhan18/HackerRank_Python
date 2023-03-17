import numpy as np
np.set_printoptions(legacy = "1.13",sign = " ")
n,m = map(int , input().split())
l = []
for i in range(0 ,n):
   lst = [*map(int , input().split())]
   for j in lst:
      l.append(j)
x = np.array(l)
x.resize(n,m)
print(np.mean(x , axis = 1))
print(np.var(x , axis = 0))
print(np.std(x))