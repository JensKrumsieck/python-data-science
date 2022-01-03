import plotly.express as px

df = px.data.iris()  # sample data
# Borsten-Schwertlilie (Iris setosa)
# Virginische Schwertlilie (Iris virginica)
# Verschiedenfarbige Schwertlilie (Iris versicolor)
# sepal = Kelchblatt, petal = Blütenblatt
fig = px.parallel_coordinates(df,
                              color="species_id",
                              labels={"sepal_length": "Länge Kelchblatt",
                                      "sepal_width": "Breite Kelchblatt",
                                      "petal_length": "Länge Blütenblatt",
                                      "petal_width": "Breite Blütenblatt"},
                              color_continuous_scale=px.colors.diverging.Fall,
                              color_continuous_midpoint=2
                              )
fig.show()

fig = px.parallel_categories(df,
                             color="species_id",
                             labels={"sepal_length": "Länge Kelchblatt",
                                     "sepal_width": "Breite Kelchblatt",
                                     "petal_length": "Länge Blütenblatt",
                                     "petal_width": "Breite Blütenblatt"},
                             )
fig.show()

fig = px.parallel_categories(px.data.tips(),
                             color="size"
                             )
fig.show()
