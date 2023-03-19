import numpy as np
lst = []
line = input().split()
n = int(line[0])
m = int(line[1])
for i in range(0 ,int(line[0])):
   line = input().split()
   for j in line:
      lst.append(int(j))
x = np.array(lst)
y = x.reshape(n,m)
print(np.transpose(y))
print(x)