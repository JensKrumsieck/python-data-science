import numpy as np

np.set_printoptions(suppress=True)
v = np.array([2, 4, 6])
w = np.array([1, 3, 5])

print(np.row_stack((v, w)))
#
# [[2 4 6]
# [1 3 5]]
#
print(np.column_stack((v, w)))
#
# [[2 1]
# [4 3]
# [6 5]]
#

A = np.array([
    [1, 2],
    [3, 4]
])
B = np.array([
    [6, 7],
    [8, 9]
])

print(np.row_stack((A, B)))
#
# [[1 2]
# [3 4]
# [6 7]
# [8 9]]
#

print(np.concatenate((A, B), axis=0))
#
# [[1 2]
# [3 4]
# [6 7]
# [8 9]]
#

print(np.tile(A, (2, 3)))
#
# [[1 2 1 2 1 2]
# [3 4 3 4 3 4]
# [1 2 1 2 1 2]
# [3 4 3 4 3 4]]
#

res = np.zeros((10, 10), dtype='i1')
res[:A.shape[0], :A.shape[1]] = A

print(res)
#
# [[1 2 0 0 0 0 0 0 0 0]
# [3 4 0 0 0 0 0 0 0 0]
# [0 0 0 0 0 0 0 0 0 0]
# [0 0 0 0 0 0 0 0 0 0]
# [0 0 0 0 0 0 0 0 0 0]
# [0 0 0 0 0 0 0 0 0 0]
# [0 0 0 0 0 0 0 0 0 0]
# [0 0 0 0 0 0 0 0 0 0]
# [0 0 0 0 0 0 0 0 0 0]
# [0 0 0 0 0 0 0 0 0 0]]
#
