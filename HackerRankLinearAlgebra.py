import numpy as np
n = int(input())
l = []
for i in range(0 ,n):
   line = [*map(float , input().split())]
   for j in line:
      l.append(j)
x = np.array(l)
x.resize(n,n)
b = np.linalg.det(x)
print(round(b,2))