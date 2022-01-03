import plotly.express as px

df = px.data.gapminder()
df = df[df.country == "Germany"]
print(df)
fig = px.bar(df, x="year", y="pop", color="lifeExp")
fig.show()
