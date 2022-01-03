import plotly.express as px

df = px.data.iris()  # sample data
# Borsten-Schwertlilie (Iris setosa)
# Virginische Schwertlilie (Iris virginica)
# Verschiedenfarbige Schwertlilie (Iris versicolor)
print(df)

df["error"] = df["sepal_width"]/50

# sepal = Kelchblatt, petal = Blütenblatt
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 # marginal = Datenbereiche graphisch (Median, Punktverteilung, etc)
                 marginal_x="box", marginal_y="violin",
                 trendline="ols",
                 error_x="error"  # Fehlerbalken, error_y auch existent
                 )
fig.show()
