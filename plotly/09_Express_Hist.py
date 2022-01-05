import plotly.express as px

df = px.data.tips()
fig = px.histogram(df, x="total_bill", nbins=10, y="tip", color="day")
fig.update_layout(bargap=.1)
fig.show()
