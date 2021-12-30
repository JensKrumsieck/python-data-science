import numpy as np

X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
Y = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# [  1   4   9  16  25  36  49  64  81 100]
print(X**2)

# [1. 1.41421356 1.73205081 2. 2.23606798 2.44948974 2.64575131 2.82842712 3. 3.16227766]
print(X**.5)

# [ 2  4  6  8 10 12 14 16 18 20]
print(X+Y)

# [ 6 12 18 24 30 36 42 48 54 60]
print(2*X+4*Y)

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
B = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [70, 8, 9]
])

print(A+B)
#
# [[ 2  4  6]
# [ 8 10 12]
# [77 16 18]]
#

print(A*B)  # elementwise multiplication
#
# [[ 1  4  9]
# [16 25 36]
# [490 64 81]]
#

print(np.dot(A, B))  # matrix multiplication
#
# [[ 219  36  42]
# [ 444  81  96]
# [669 126 150]]
#

print(A == B)
#
# [[ True  True  True]
# [ True  True  True]
# [False  True  True]]
#

F = A == B
G = np.array([
    [True, False, True],
    [False, True, False],
    [True, True, True]
])

print(np.logical_or(F, G))
#
# [[ True  True  True]
# [ True  True  True]
# [ True  True  True]]
#

print(np.logical_and(F, G))
#
# [[ True False  True]
# [False  True False]
# [False  True  True]]
#

V = np.array([1, 2, 3])
print(A*V)  # rowwise multi -> Broadcast
#
# [[ 1  4  9]
# [ 4 10 18]
# [ 7 16 27]]
#

print(np.dot(A, V))
# [14 32 50]

print(A.transpose() * V)
#
# [[ 1  8 21]
# [ 2 10 24]
# [ 3 12 27]]
#

V = np.array([V, ]*3).transpose()
print(V*A)  # usual mult
#
# [[ 1  2  3]
# [ 8 10 12]
# [21 24 27]]
#
