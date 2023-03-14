import numpy as np
line = input("")
lst = line.split()
lst = [float(i) for i in lst]
lst.reverse()
arr = np.array(lst,float)
print(arr)
