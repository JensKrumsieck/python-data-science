import pandas as pd
df = pd.DataFrame({
    "A": [1, 2, 3],
    "B": [4, 5, 6],
},
    index=["a", "b", "c"])
print(df)
print(df.loc[["a", "b"], "B"])
print(df.loc[df.index[[1, 2]], "B"])
print(df.iloc[[1, 2], df.columns.get_loc("B")])
df.loc["d"] = [32, 42]  # appends row
df["C"] = 1337  # appends column
print(df)
print(df.at["a", "A"])  # =1
print(df.iat[2, 1])  # =6 (zeilen, spalten)

print(df)
print(df[df >= 42])  # boolean access, false = NaN
print(df[df.isin([1, 2, 3])])

s = pd.Series([1337, 42, 69])  # count = 3
print(s[s.isin([42, 1337])])  # count altered! count = 2
print(s.where(s.isin([42, 1337])))  # count =3 , index 2 = NaN

# remove NaNs in DataFrame
print(df.where(df.isin([42, 1337]), other=69))

df2 = df.where(df.isin([42, 1337]), other=-5)
print(df2)
# positives where values are not greater than 0
print(df2.where(df2 > 0, other=-df2))
# no new df is returned but saved in original var
df2.where(df2 > 0, other=-df2, inplace=True)
print(df2)
