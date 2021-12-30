import numpy as np
from sys import getsizeof

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

dic = {'Red': 255, 'Green': 255, 'Blue': 255, 'Alpha': 255}
print(dic)  # {'Red': 255, 'Green': 255, 'Blue': 255, 'Alpha': 255}
da = np.array(dic)
print(da.shape)  # ()
print(da.dtype)  # object

dt = np.dtype(('i4', [('r', 'u1'), ('g', 'u1'), ('b', 'u1'), ('a', 'u1')]))
# (numpy.int32, [('r', 'u1'), ('g', 'u1'), ('b', 'u1'), ('a', 'u1')])
print(dt)
zero = np.zeros((), dt)
print(zero)  # 0
print(zero['r'])  # 0
print(f"size of dic: {getsizeof(dic)}")  # 232
print(f"size of npdic: {getsizeof(zero)}")  # 92

complex_dt = np.dtype(
    (np.int32, {'real': (np.int16, 0), 'imag': (np.int16, 2)}))
print(complex_dt)  # (numpy.int32, [('real', '<i2'), ('imag', '<i2')])
print(f"Size of complex: {getsizeof(complex_dt)}")  # 96
print(np.zeros((500, 5000), complex_dt)['real'][0][4999])  # 0
