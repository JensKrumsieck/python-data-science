import plotly.express as px

df = px.data.gapminder().query("year==2007").query("continent=='Europe'")
df.loc[df["pop"] < 4000000, 'country'] = "Other"

fig = px.pie(df, names="country", values="pop", title="Population in Europe")

fig.show()

df2 = px.data.gapminder().query("year==2007")
df2.loc[df2["pop"] < 4000000, 'country'] = "Other"
fig2 = px.sunburst(df2, path=["continent", "country"],
                   values="pop", title="population", color="lifeExp")
fig2.show()
