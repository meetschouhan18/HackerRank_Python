import numpy as np
lst_n = []
lst_m = []
line = input().split()
n = int(line[0])
m = int(line[1])
p = int(line[2])
for i in range(0 ,n):
   line = input().split()
   for j in line:
      lst_n.append(int(j))
for i in range(0 ,m):
   line = input().split()
   for j in line:
      lst_m.append(int(j))
x = np.array(lst_n)
x.resize(n,p)
y = np.array(lst_m)
y.resize(m,p)
print(np.concatenate((x,y),axis = 0))