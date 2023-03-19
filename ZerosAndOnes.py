import numpy as np

line = input().split()
n = int(line[0])
m = int(line[1])

if len(line) == 2:
   a = np.zeros([n,m],int)
   b = np.ones([n,m],int)
   print(a)
   print(b)

elif len(line) == 3:
   p = int(line[2])
   a = np.zeros([n,m,p],int)
   b = np.ones([n,m,p],int)
   print(a)
   print(b)

else:
   p = int(line[2])
   q = int(line[3])
   a = np.zeros([n,m,p,q],int)
   b = np.ones([n,m,p,q],int)
   print(a)
   print(b)
