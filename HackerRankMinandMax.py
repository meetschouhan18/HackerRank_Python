import numpy as np
n,m = map(int , input().split())
l = []
for i in range(0 ,n):
   line = [*map(int , input().split())]
   for j in line:
      l.append(j)
x = np.array(l)
x.resize(n,m)
min_x = np.min(x , axis = 1)
print(np.max(min_x))