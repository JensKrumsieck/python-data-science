import numpy as np

dt = np.dtype((np.int8, (4, 5)))
print(dt.shape)  # (2, 3)

arr = np.zeros((2, 3), dt)
# print(arr)
print(arr.dtype)  # int8
print(arr.shape)  # (2, 3, 4, 5)

dt2 = np.dtype(('i4, (2,3)f8, f4', (2, 3)))
arr2 = np.zeros((), dt2)
print(arr2.dtype)  # [('f0', '<i4'), ('f1', '<f8', (2, 3)), ('f2', '<f4')]
print(arr2.shape)  # (2, 3)
