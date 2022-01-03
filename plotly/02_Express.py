import plotly.express as px

df = px.data.iris()  # sample data
# Borsten-Schwertlilie (Iris setosa)
# Virginische Schwertlilie (Iris virginica)
# Verschiedenfarbige Schwertlilie (Iris versicolor)
print(df)
# sepal = Kelchblatt, petal = Blütenblatt
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 marginal_x="box", marginal_y="violin",  # marginal = Datenbereiche graphisch (Median, Punktverteilung, etc)
                trendline="ols")
fig.show()
