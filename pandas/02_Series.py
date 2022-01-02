import pandas as pd
import numpy as np

# two lists
data = [28, 54, 218, 69]
index = ["A", "B", "C", "D"]

s = pd.Series(data, index=index, name="age")
print(s)
print(s["C"])

# dictionary
dict = {
    "A": 28,
    "B": 42,
    "C": 1337,
    "D": 69
}

# index changes sorting, F adds NaN value
s2 = pd.Series(dict,
               name="dict",
               index=["B", "C", "A", "D", "F"],
               dtype=np.int16)
print(s2)

# np
s3 = pd.Series(np.random.randn(10), dtype=np.float32)
print(s3)

print(s3.ravel())  # flattens
print(s3[1:3])  # select index 1 and 3
# s3[1:3][0] invalid!

print(s3[s3 < s3.median()])
print(np.abs(s3))
