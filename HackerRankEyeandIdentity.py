import numpy as np
m = np.eye(*map(int,input().split()))
print(str(m).replace("1"," 1").replace("0"," 0"))