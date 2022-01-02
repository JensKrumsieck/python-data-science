import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(1337, 3))
print(df)
print(df.describe())
print(df.sum())
print(df.idxmax())  # indices des maximums als ZEILENINDEX!
print(df[0][df.idxmax()[0]])
print(df.mad())  # mean absolute deviation
df = pd.Series(np.random.randint(0,42, size=1000))
print(pd.value_counts(df))