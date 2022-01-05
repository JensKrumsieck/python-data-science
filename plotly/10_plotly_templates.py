from re import template
import plotly.express as px

df = px.data.tips()
fig = px.histogram(df, x="total_bill", nbins=10, y="tip", color="day")

for t in ['ggplot2', 'seaborn', 'simple_white', 'plotly',
          'plotly_white', 'plotly_dark', 'presentation', 'xgridoff',
          'ygridoff', 'gridon', 'none']:
    fig.update_layout(template=t)
    fig.show()
