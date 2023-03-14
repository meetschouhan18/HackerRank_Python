import numpy as np
n,m = map(int,input().split())
a_lst = []
b_lst = []
for i in range(0, n):
   a1 = [*map(int,input().split())]
   for j in a1:
      a_lst.append(a1)
a = np.array(a_lst)
a.resize(n,m)
for i in range(0, n):
   b1 = [*map(int,input().split())]
   for j in b1:
      b_lst.append(b1)
b = np.array(b_lst)
b.resize(n,m)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)