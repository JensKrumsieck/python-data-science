import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10000, 3))
print(df[0].describe())

# 4 gleich große bins (von der range her, nicht von den elementen)
print(pd.cut(df[0], 4))
# (a,b] -> a excluded, b included

cats = pd.cut(df[0], 4)
print(cats)
print(cats[0])  # 1st element's category

print(pd.value_counts(cats))  # anzahl der einträge pro bin
# bester weg für histogramme von floats
# aber wenn man percentile braucht:
perc = pd.qcut(df[0], [0, .2, .4, .6, 1])  # 2. argument = percentile
print(perc)
print(pd.value_counts(perc))
#
# (0.289, 4.237]      4000 <- .6 bis 1 doppelt so viele werte
# (-3.5, -0.809]      2000
# (-0.809, -0.225]    2000
# (-0.225, 0.289]     2000
#
print(perc.sort_values())  # sorts perc
print(perc.cat.as_unordered())  # unsorted perc
print(perc.cat.as_ordered())  # doesn't sort!
print("----------------------------------------------------------")
cat = pd.Categorical(
    list("ABCA"), categories=list("ACD"), ordered=False
)
print(cat)
#
#['A', NaN, 'C', 'A']
# Categories (3, object): ['A', 'C', 'D']
#
cat = pd.Categorical(
    list("ABCA"), categories=list("ACD"), ordered=True
)
print(cat)
#
#['A', NaN, 'C', 'A']
# Categories (3, object): ['A' < 'C' < 'D']
#
print(cat.add_categories(["L"]))
#
#['A', NaN, 'C', 'A']
# Categories (4, object): ['A' < 'C' < 'D' < 'L']
#
print(cat.add_categories(["B"]))
#
# ['A', NaN, 'C', 'A'] <--- B still NaN, Values disposed!
# Categories (4, object): ['A' < 'C' < 'D' < 'B']
#
print(cat.remove_categories(["A"]))
#
# [NaN, NaN, 'C', NaN]
# Categories (2, object): ['C' < 'D']
#
cat = cat.add_categories(["DUMP"])
cat = cat.set_ordered(False)
cat = cat.remove_categories(["A"]).fillna("DUMP")
print(cat)
#
#['DUMP', 'DUMP', 'C', 'DUMP']
# Categories (3, object): ['C', 'D', 'DUMP']
#
cat = cat.remove_unused_categories()  # Remove D
print(cat)
#
# ['DUMP', 'DUMP', 'C', 'DUMP']
# Categories (2, object): ['C', 'DUMP']
#
cat = cat.set_ordered(True)
print(cat)
#
# ['DUMP', 'DUMP', 'C', 'DUMP']
# Categories (2, object): ['C' < 'DUMP']
#
cat.sort_values(inplace=True)
print(cat)
#
# ['C', 'DUMP', 'DUMP', 'DUMP']
# Categories (2, object): ['C' < 'DUMP']
#
print("----------------------------------------------------------")
s = pd.Series(cat)
s.sort_values(inplace=True)
print(s)
#
# 0       C
# 1    DUMP
# 2    DUMP
# 3    DUMP
#dtype: category
# Categories (2, object): ['C' < 'DUMP']
#
cat = pd.Categorical(
    list("ABCA"), categories=list("ACD"), ordered=True
)
s = pd.Series(cat)
s = s.cat.reorder_categories(list("DCA"), ordered=True)
print(s)
# Categories (3, object): ['D' < 'C' < 'A']
