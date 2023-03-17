import numpy as np

x = np.array([*map(int , input().split())])
y = np.array([*map(int , input().split())])
print(np.inner(x,y))
print(np.outer(x,y))
