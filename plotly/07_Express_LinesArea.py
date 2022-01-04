import plotly.express as px

df = px.data.gapminder()

fig = px.line(df, x="year", y="lifeExp",
              color="continent",
              line_group="country",
              hover_name="country",
              line_shape="spline",
              render_mode="svg"  # für spline
              )

fig.show()

df2 = px.data.gapminder().query("continent == 'Europe'")
fig2 = px.line(df2, x="year", y="lifeExp",
               color="country",
               line_group="country",
               hover_name="country",
               line_shape="spline",
               render_mode="svg"  # für spline
               )
fig2.show()

fig3 = px.area(df2, x="year", y="pop",
               color="country",
               line_group="country",
               hover_name="country"
               )
fig3.show()
