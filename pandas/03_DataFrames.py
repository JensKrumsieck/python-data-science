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
print(df/5)  # divide by 5
print(df.sub(2))  # subtract 2
print(df.add(df.iloc[1]))  # add first row to all
print(df.add(df.iloc[1], axis=0))  # INVALID!
print(df.head())  # 1st five rows
print(df.tail())  # last five rows
print(df.tail(1))  # last row
print(df.fillna("LOL"))  # fills NaNs
print(df.eq(df))  # true frame, if NaN = false!
print((df > 0).all())  # für ganze spalten
print((df > 0).any())
# df.combine_first(df2) -> packe alle leeren in df mit df2 werten voll
print(df.to_numpy())  # to np matrix
