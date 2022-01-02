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
perce = pd.qcut(df[0], [0, .2, .4, .6, 1])  # 2. argument = percentile
print(perce)
print(pd.value_counts(perce))
#
# (0.289, 4.237]      4000 <- .6 bis 1 doppelt so viele werte
# (-3.5, -0.809]      2000
# (-0.809, -0.225]    2000
# (-0.225, 0.289]     2000
#
