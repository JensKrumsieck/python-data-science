import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    "A": np.random.randn(3),
    "B": np.random.randn(3),
    "C": np.random.randn(3)
}, index=[0, 1, 2])
df2 = pd.DataFrame({
    "A": np.random.randn(3),
    "B": np.random.randn(3),
    "C": np.random.randn(3)
}, index=[0, 1, 2])
df3 = pd.DataFrame({
    "A": np.random.randn(3),
    "B": np.random.randn(3),
    "C": np.random.randn(3)
}, index=[0, 1, 2])
df4 = pd.DataFrame({
    "A": np.random.randn(3),
    "B": np.random.randn(3),
    "C": np.random.randn(3)
}, index=[3, 4, 2])

print(df1)
print(df2)
print(df3)
# concatenate dataframes
# multiple identical indices, dataframes are appended below
# indices not UNIQUE!
print(pd.concat([df1, df2, df3]))

# appending as new columns on the right
# columns are not UNIQUE!
# axis 0 is default
print(pd.concat([df1, df2, df3], axis=1))

print(pd.concat([df1, df4]))
# only indices occuring in both df are printed with columns appended on the right
# with axis 0 join does not matter because columns are equal (see above)
# inner = intersection, outer = union
print(pd.concat([df1, df4], join='inner', axis=1))

# non existing values will get NaN
print(pd.concat([df1, df2, df3, df4], join='outer', axis=1))

# multiindexing with A B C for each dateframe, df4 ist not added
print(pd.concat([df1, df2, df3, df4], keys=list("ABC")))

print(df1.append(df2))  # same as pd.concat outer join

# new indexing
print(pd.concat([df1, df2, df3, df4], ignore_index=True))

# sort concatenation
print(pd.concat([df1, df2, df3, df4], sort=True))
# works with series to!
