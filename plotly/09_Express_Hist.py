import plotly.express as px
import numpy as np

df = px.data.tips()
fig = px.histogram(df, x="total_bill", nbins=10, y="tip", color="day")
fig = px.histogram(df, x="total_bill", nbins=10,
                   histnorm="percent")  # probability density
fig = px.histogram(df, x="total_bill", y="tip",
                   histfunc="avg", color="sex", pattern_shape="smoker")  # count, avg,
fig.update_layout(bargap=.1)
fig.show()

counts, bins = np.histogram(df.total_bill, bins=range(0, 60, 5))
bins = bins[:-1] + bins[1:]
fig2 = px.bar(x=bins, y=counts)
fig2.update_layout(bargap=.1)
fig2.show()
