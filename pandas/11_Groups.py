import pandas as pd
import numpy as np

df = pd.DataFrame({
    "group": ["cat", "dog", "cat", "cat", "dog"],
    "A": ["a", "b", "c", "d", "x"],
    "B": ["e", "f", "g", "h", "y"],
    "C": np.random.randn(5)
})
print(df)

group_df = df.groupby("group")
print(group_df.groups)  # {'cat': [0, 2, 3], 'dog': [1, 4]}
print(group_df.groups["cat"])  # Int64Index([0, 2, 3], dtype='int64')

for name, group in group_df:
    print(name)
    print(group)
#
# cat
#   group  A  B         C
# 0   cat  a  e -0.370417
# 2   cat  c  g -0.856473
# 3   cat  d  h -0.718394
# dog
#   group  A  B         C
# 1   dog  b  f  1.451490
# 4   dog  x  y -0.247638

print(group_df.get_group("cat"))
#
#   group  A  B         C
# 0   cat  a  e  0.612212
# 2   cat  c  g  1.611221
# 3   cat  d  h  1.678592
#
print(group_df.size())
#
# group
# cat    3
# dog    2
# dtype: int64
#
# print(group_df.cumsum())


# def foo(group):
#     print(group)
#     return pd.DataFrame({
#         'group': group,
#         'mean': group["C"].mean()  # could not convert dogdog to numeric

#     }, index=[0, 1, 2, 3, 4])


# fooo = group_df.apply(foo)
