import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        "id": [0, 1, 2],
        "name": ["Cedric", "Morpheus", "Morph"],
        "age": [28, 28, 28]
    }
)

print(df)
print(df["age"].describe())
print(pd.Series([1, 2, 3], name="lol"))

var = {
    "a": [0, 1, 2, 3, 4, 5, 6, 7],
    "b": pd.Series([1, 2, 3, 4], index=["A", "B", "C", "D"]),
    "c": pd.Series([2, 3, 4, 5])
}
df2 = pd.DataFrame(var)
print(df2)

var2 = {
    "a": [0, 1, 2],
    "b": [2, 3, 4]
}
df3 = pd.DataFrame(var2, index=["a", "b", "c"])
print(df3)

var3 = np.zeros((5,), dtype=[("id", "i8"), ("age", "i4"), ("name", "a10")])
df4 = pd.DataFrame(var3)
print(df4)

var4 = {
    ("a", "b"): {"A": 0, "B": 1},
    ("a", "y"): {"A": 0, "B": 1},
    ("a", "x"): {"A": 0, "B": 1},
    ("b", "z"): {"A": 0, "B": 1},
    ("b", "y"): {"A": 0, "B": 1},
    ("b", "x"): {"A": 0, "B": 1}
}
df5 = pd.DataFrame(var4)  # a & b parent index, xyz other indices
print(df5)
print(df5["a"]["x"]["A"])  # 0
