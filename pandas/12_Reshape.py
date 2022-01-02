import pandas as pd
import numpy as np

df = pd.DataFrame({
    "group": ["cat", "dog", "cat", "cat", "dog"],
    "group2": ["a", "a", "b", "c", "b"],
    "A": ["a", "b", "c", "d", "x"],
    "B": ["e", "f", "g", "h", "y"],
    "C": np.random.randn(5)
})

print(df)
# create pivot tables
print(df.pivot(
    index="group",
    columns="group2",
    values="C"
))
#
# group2         a         b         c  <---values from group 2 as column
# group
# cat    -1.185476  2.778849 -0.599333
# dog    -0.523323  1.600661       NaN
# ^
# |
# values from group as id
