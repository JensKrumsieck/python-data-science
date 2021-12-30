import numpy as np

# CREATE ARRAYS AND MATRICES
arr = np.array([1, 2, 3, 4])
arr = np.ones(42)
arr = np.zeros(42)

arr = np.arange(-42, 69, 2, dtype=('i2'))  # via step
#
# [-42 -40 -38 -36 -34 -32 -30 -28 -26 -24 -22 -20 -18 -16 -14 -12 -10  -8
#  -6  -4  -2   0   2   4   6   8  10  12  14  16  18  20  22  24  26  28
#  30  32  34  36  38  40  42  44  46  48  50  52  54  56  58  60  62  64
#  66  68]
#

arr = np.linspace(-42, 1337.2, 5)  # via len
# [ -42.   302.8  647.6  992.4 1337.2]

arr = np.full((2, 3), 69)  # fill matrix
#
# [[69 69 69]
# [69 69 69]]
#

arr = np.eye(3, dtype='i1')  # identity matrix
#
# [[1 0 0]
# [0 1 0]
# [0 0 1]]
#

arr = np.random.random((2, 3))  # random float 2x3 matrix

arr = np.empty((2, 3))  # weird empty matrix
print(arr)
