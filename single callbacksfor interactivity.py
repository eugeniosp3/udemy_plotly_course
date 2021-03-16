import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd


df = pd.read_csv('C:/Users/eugen/OneDrive/Main_Env/udemy_dash_course/gapminderDataFiveYear.csv')
app = dash.Dash()

year_options = []
for year in df['year'].unique():
    year_options.append({'label':str(year), 'value':year})


app.layout = html.Div([dcc.Graph(id='graph'),
                       dcc.Dropdown(id='year-picker', options=year_options,
                                    value=df['year'].min())

                       ])
# output = where it will showup
# input what the input is
@app.callback(Output('graph', 'figure'),
              [Input('year-picker', 'value')])
def update_figure(selected_year):
# a function that shows the text somewhere
    filtered_df = df[df['year'] == selected_year]

    traces = []

    for continent_name in filtered_df['continents'].unique():
        df_by_continent = filtered_df[filtered_df['continent'] == continent_name]
        traces.append(go.Scatter(
            x=df_by_continent['gdpPercap'],
            y=df_by_continent['lifeExpectancy'],
            mode='markers',
            opacity=0.7,
            marker = {'size': 15},
            name = continent_name

        ))
    return {'data': traces,
            'layout': go.Layout(title = 'My Plot',
                                xaxis = {'title': 'GPD Per Cap', 'type': 'log'},
                                yaxis={'title':'Life Expectancy'})}


if __name__ == '__main__':
    app.run_server()
