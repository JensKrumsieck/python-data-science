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


def stack():
    idxs = list(
        zip(
            *[
                ["A", "A", "B", "B", "C", "C", "D", "D"],
                ["1", "2", "1", "2", "1", "2", "1", "2"]
            ]
        )
    )
    # [('A', '1'), ('A', '2'), ('B', '1'), ('B', '2'), ('C', '1'), ('C', '2'), ('D', '1'), ('D', '2')]
    index = pd.MultiIndex.from_tuples(idxs)
    df = pd.DataFrame(np.random.randn(8, 3), index=index,
                      columns=["X", "Y", "Z"])
    print("####DATAFRAME####")
    print(df)  # is of type DataFrame
    print("####STACK####")
    print(df.stack())  # is of type Series
    df_unstack = df.unstack()
    print("####UNSTACK####")
    print(df_unstack)  # is of type DataFrame
    print("####UNSTACK 2x####")
    print(df_unstack.unstack())  # is of type Series
    print("####RESTACK####")
    print(df_unstack.stack())  # is of type DataFrame
    print("####UNSTACK With Level Param####")
    print(df.unstack(level=[0, 1]))  # is of type DataFrame


stack()
