import plotly.graph_objects as go
import plotly.io as pio

graph = go.Figure(
    data=go.Bar(
        x=[0, 1, 2],
        y=[42, 1337, 69]
    ),
    layout=go.Layout(
        title=go.layout.Title(text="Beispiel")
    )
)
# graph.write_html("plot1_ignore.html", auto_open=True)
graph.show()

fig = dict({
    "layout": {
        "title": {
            "text": "Beispiel"
        },
    },
    "data": [
        {
            "type": "bar",
            "x": [0, 1, 2],
            "y": [42, 1337, 69]
        }
    ]

})
graph_fig = go.Figure(fig)
graph_fig.show()
pio.show(fig)

# all 3 figures identical! :)

print(graph.to_dict())
