## objectives ##

# objective - build dashboard using 'OldFaithful.csv'
# display as a scatterplot
# D = data of recordings in month (August)
# X duration of current eruptions in minutes
# Y waiting time until the next eruption

import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/eugen/OneDrive/Main_Env/udemy_dash_course/Data/OldFaithful.csv')

colors = {'background':'#111111', 'text':'#7fdbff'}

app = dash.Dash()

app.layout = html.Div(children=
                      [html.H1('Hello Dash!',
                               style={'textAlign': 'center', 'color': colors['text']}),
                       dcc.Graph(id='example',
                                 figure={'data': [go.Scatter(x=df['X'], y=df['Y']/60, mode='markers',
                                                  marker=dict(size=df['X'], color=df['Y'],
                                                              showscale=True,colorbar=dict(title='Time to Next Eruption')))],
                                                              'layout':go.Layout(title='Old Faithful Eruptions',
                                                            xaxis={'title': 'Duration of Eruption'},
                                                            yaxis={'title': 'Interval'})})])





if __name__ == '__main__':
    app.run_server()