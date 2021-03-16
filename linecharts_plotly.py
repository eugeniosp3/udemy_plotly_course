import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
np.random.seed(56)

# data
x_values = np.linspace(0,1,100)
y_values = np.random.randn(100)

# edited this to make a line chart
trace0 = go.Scatter(x=x_values, y=y_values+5,
                   mode='markers+lines',
                   name='markers')

trace1 = go.Scatter(x=x_values, y=y_values,
                   mode='lines',
                   name='lines')
# data list
data=[trace0, trace1] #needs to be a list in plotly

# Layout is optional to edit titles, axis, etc
layout = go.Layout(title='Line Chart')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
