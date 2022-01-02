import pandas as pd

dict = {
    "a": 42,
    "c": 1337,
    "d": 69,
    "b": 420
}
var = {
    "A": [0, 1, 2, 3],
    "B": pd.Series(dict),
    "C": pd.Series([2, 3, 4, 5], index=["a", "b", "c", "d"])
}
df = pd.DataFrame(var)
print(df)
print(df.loc["a"])
print(df.iloc[3])
B = df.pop("B")  # "Wenn wir Poppen..." - Morpheus, 20.07.2021
print(df)
print(df.assign(hans=lambda x: x["A"] + x["C"]))
