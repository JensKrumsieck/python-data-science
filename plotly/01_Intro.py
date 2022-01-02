import plotly.graph_objects as go

graph = go.Figure(data=go.Bar(y=[42, 1337, 69]))
graph.write_html("plot1_ignore.html", auto_open=True)
graph.show()
