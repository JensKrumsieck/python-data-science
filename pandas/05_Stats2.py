import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(1337, 3))
print(df)
# last column not selected, swap columns and indices
df = df.reindex(index=range(42, 0, -1), columns=[2, 0])
print(df)
print(df.index)
print(df.columns)
df.columns = [0, 2]  # rename colums
print(df)

df = pd.Series(np.random.randint(0, 42, size=1000))
hist = pd.value_counts(df)
hist = hist.reindex(range(0, 42))
print(hist)
