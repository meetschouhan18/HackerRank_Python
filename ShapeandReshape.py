import numpy as np

line = input().split()
line = [int(i) for i in line]
x = np.array(line)
x.resize(3,3)
print(x)
