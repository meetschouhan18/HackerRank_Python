import numpy as np
n,m = map(int , input().split())
l = []
for i in range(0 ,n):
   lst = [*map(int , input().split())]
   for j in lst:
      l.append(j)
x = np.array(l)
x.resize(n,m)
sum_x = np.sum(x, axis = 0)
prod_x = np.prod(sum_x)
print(prod_x)
print(sum_x)