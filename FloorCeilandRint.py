import numpy as np

np.set_printoptions(sign=" ")
x = np.array([*map(float,input().split())])
print(np.floor(x))
print(np.ceil(x))
print(np.rint(x))
