import numpy as np
from sys import getsizeof
import random
from timeit import Timer

temp = [-1.5, -1.2, 0.0, 2.1, 24.2]
sz = 1000000
X = [random.randint(0, 200) for _ in range(sz)]
Y = [random.randint(0, 200) for _ in range(sz)]
np_X = np.array(X, np.int16)
np_Y = np.array(Y, np.int16)


def python():
    res = [a+b for a, b in zip(X, Y)]
    return res


def numpy():
    return np_X+np_Y


timePy = Timer("python()", "from __main__ import python").timeit(10)
timeNp = Timer("numpy()", "from __main__ import numpy").timeit(10)

print(f"Size of pyList: {getsizeof(X)}")
print(f"Size of npArray: {getsizeof(np_X)}")

print(f"Time for Py was {timePy}")
print(f"Time for Np was {timeNp}")
print(f"Numpy was {timePy/timeNp} times faster and {getsizeof(X)/ getsizeof(np_X)} times less memory consuming")
