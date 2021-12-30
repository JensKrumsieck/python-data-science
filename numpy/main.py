import numpy as np

temp = [-1.5, -1.2, 0.0, 2.1, 24.2]
np_temp = np.array(temp)
print(np_temp.shape) # (5,)

print(3 * np_temp)
print(np.array([42, 127], np.int8))

dt = np.dtype("i4")  # i4 -> int32
print(dt.itemsize)
print(dt.name)
print(dt.type is np.int32)

print(dt.byteorder)  # = -> nativ, < -> little, > -> big endian, | -> not applicable
# big endian 1000 = 0*2^0 + 0*2^1 + 0*2^2 + 1*2^3 = 8 (vereinfacht, eigentlich bitorder)
# little endian 1000 = 1*2^0 + 0*2^1 + 0*2^2 + 0*2^3 = 1

dt = np.dtype("?")  # boolean
print(dt.type)

dt = np.dtype("f8")  # float64
print(dt.type)

dt = np.dtype("c16")  # complex128
print(dt.type)

dt = np.dtype("U")  # unicode str
print(dt.type)
print(dt.shape) # ()
