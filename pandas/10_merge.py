import pandas as pd

l = pd.DataFrame({
    "id": ["0", "1", "2", "4"],
    "id2": ["0", "1", "2", "1"],
    "A": ["a", "b", "c", "d"],
    "B": ["e", "f", "g", "h"]
})
r = pd.DataFrame({
    "id": ["0", "1", "2", "3"],
    "id2": ["0", "1", "0", "4"],
    "C": ["i", "j", "k", "l"],
    "D": ["m", "n", "o", "p"]
})

df = l.merge(r)  # only indices from both DataFrames!!! are merged = innerjoin!
df = pd.merge(l, r)  # equivalent to l.merge(r)
print(df)
df = pd.merge(l, r, on="id")
print(df)

# Ordering differences
df = pd.merge(r, l, on="id", how="outer")  # outerjoin
print(df)
df = pd.merge(l, r, on="id", how="outer")  # outerjoin
print(df)
# id2_x and id2_y are created if not in on
# joins on boths ids, rows are appended for non-equal values
df = pd.merge(l, r, on=["id", "id2"], how="outer")
print(df)

df = pd.merge(l, r, on=["id", "id2"])
print(df)
# prints only non NaN Data
#   id id2  A  B  C  D
# 0  0   0  a  e  i  m
# 1  1   1  b  f  j  n
#

# leftouterjoin
df = pd.merge(l, r, on=["id", "id2"], how="left")  # only keys from left
print(df)
#
#   id id2  A  B    C    D
# 0  0   0  a  e    i    m
# 1  1   1  b  f    j    n
# 2  2   2  c  g  NaN  NaN
# 3  4   1  d  h  NaN  NaN
#
# rightouterjoin
df = pd.merge(l, r, on=["id", "id2"], how="right")
print(df)
#
#   id id2    A    B  C  D
# 0  0   0    a    e  i  m
# 1  1   1    b    f  j  n
# 2  2   0  NaN  NaN  k  o
# 3  3   4  NaN  NaN  l  p
#

# adds join indicator for value in both, left_only, right_only
df = pd.merge(l, r, on=["id", "id2"], how="outer", indicator="indi")
print(df)
#
#   id id2    A    B    C    D        indi
# 0  0   0    a    e    i    m        both
# 1  1   1    b    f    j    n        both
# 2  2   2    c    g  NaN  NaN   left_only
# 3  4   1    d    h  NaN  NaN   left_only
# 4  2   0  NaN  NaN    k    o  right_only
# 5  3   4  NaN  NaN    l    p  right_only
#

df = pd.merge(l, r, indicator="indi",
              left_index=True, right_index=True)

l = pd.DataFrame({
    "id": [0, 1, 2, 3],
    "A": ["a", "b", "c", "d"],
    "B": ["e", "f", "g", "h"]
})
r = pd.DataFrame({
    "id2": [0, 2, 1, 3],
    "C": ["i", "j", "k", "l"],
    "D": ["m", "n", "o", "p"]
})
df = pd.merge(l, r, left_on="id", right_on="id2")  # join id to id2
print(df)
#
#    id  A  B  id2  C  D
# 0   0  a  e    0  i  m
# 1   1  b  f    1  k  o
# 2   2  c  g    2  j  n
# 3   3  d  h    3  l  p
#
