import plotly.express as px

df = px.data.iris()  # sample data
# Borsten-Schwertlilie (Iris setosa)
# Virginische Schwertlilie (Iris virginica)
# Verschiedenfarbige Schwertlilie (Iris versicolor)
# sepal = Kelchblatt, petal = Blütenblatt
fig = px.scatter_matrix(df,
                        dimensions=["sepal_length", "sepal_width",
                                    "petal_length", "petal_width"],
                        color="species")

fig.show()
