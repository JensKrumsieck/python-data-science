import numpy as np

# CREATE ARRAYS AND MATRICES
arr = np.array([1, 2, 3, 4])
arr = np.ones(42)
arr = np.zeros(42)

arr = np.arange(-42, 69, 2, dtype=('i2'))  # via step
arr = np.linspace(-42, 1337.2, 5)  # via len
arr = np.full((2, 3), 69)  # fill matrix
arr = np.eye(3, dtype='i1')  # identity matrix
arr = np.random.random((2, 3))  # random float 2x3 matrix
arr = np.empty((2, 3))  # weird empty matrix

# OPERATIONS
V = np.arange(-42, 1337, 42)
M = np.eye(42)
x = np.subtract(V, V)  # add, multiply, exp, ...

x = np.sin(V)  # cos, tan, acos, ...

x = np.exp(V)  # e^V
x = np.exp2(V)  # 2^V
x = np.power(V, 2)  # V^2

x = np.log(V)  # ln(V)
x = np.log10(V)  # log(10)
x = np.log2(V)  # log2(V)

x = np.argmax(V)  # 32  = index at max
x = np.argmin(V)  # 0  = index at min
x = np.max(V)  # 1302 = max value
V = np.random.randint(0, 10, size=(10,))
x = np.argsort(V)  # sort indices by vector values ASC

idx = [x[0]] + [x[0], x[1], x[2]]
np.add.at(V, idx, 1)  # ufunc, V is modified
print(V)
print(x)
print(idx)
