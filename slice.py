import numpy as np

temp = [-1.5, -1.2, 0.0, 2.1, 24.2, 17.2, 14.9, 12, 19]
np_temp = np.array(temp)

# start, end, stepsize
print(temp[1:7:2])  # [-1.2, 2.1, 17.2]
print(np_temp[1:7:2])  # [-1.2  2.1 17.2]

print(temp[::-1]) # [19, 12, 14.9, 17.2, 24.2, 2.1, 0.0, -1.2, -1.5]
print(np_temp[::-1]) # [19.  12.  14.9 17.2 24.2  2.1  0.  -1.2 -1.5]