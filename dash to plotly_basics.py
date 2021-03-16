import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

# create data

np.random.seed(42)

random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

app.layout = html.Div(
    [dcc.Graph(id='scatterplot',
               figure={'data': [
                   go.Scatter(
                       x=random_x,
                       y=random_y,
                       mode='markers',
                       marker={
                           'size': 12,
                           'color': 'rgb(51,204,153)',
                           'symbol': 'pentagon',
                           'line': {
                               'width': 2}})],
                            'layout': go.Layout(
                       title='My Scatterplot',
                       xaxis={
                           'title': 'Some X Title'})}

               ),
dcc.Graph(id='scatterplot2',
               figure={'data': [
                   go.Scatter(
                       x=random_x,
                       y=random_y,
                       mode='markers',
                       marker={
                           'size': 12,
                           'color': 'rgb(200,53,153)',
                           'symbol': 'pentagon',
                           'line': {
                               'width': 2}})],
                            'layout': go.Layout(
                       title='Second Plot',
                       xaxis={
                           'title': 'Some X Title'})})
     ]

)

if __name__ == '__main__':
    app.run_server()
