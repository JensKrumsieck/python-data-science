import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(100000, 4))
print(df)
for col in df:  # iteration in df.columns
    print(col)

# do **NOT** use, inefficient!
# for id, row in df.iterrows(): # interation in rows
    # print(f"Id: {id}\n{row}")
    # for i in row:
    #   # print(i)

for label, series in df.items():
    print(label)
    print(series)

for row in df.itertuples():
    print(row)
    print(row[0])  # index
    print(row[1])  # 1st value
    print(row.Index)  # idx
    print(row._1)  # 1st val
    break

df2 = pd.DataFrame({
    "a": 1337,
    "b": 1338,
    "c": 1229
}, index=list("abc"))
print(df2)

for row in df2.itertuples():
    print(row)
    print(row.a)
# iteration = EVIL!

