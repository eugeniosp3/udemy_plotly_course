import dash
import dash_core_components as dcc
import dash_html_components as html
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

colors = {'background': '#111111', 'text': '#7fdbff'}


app.layout = html.Div(children=[
    html.H1('Hello Dash!', style={'textAlign': 'center', 'color': colors['text']}),
    dcc.Graph(id='example',
              figure={'data': [{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                               {'x': [1, 2, 3], 'y': [3, 9, 6], 'type': 'bar', 'name': 'NYC'},
                               {'x': [1, 2, 3], 'y': [8, 2, 5], 'type': 'bar', 'name': 'NOLA'}
                               ],  # data us a list
                      'layout': {
                          'plot_bgcolor': colors['background'],
                          'paper_bgcolor': colors['background'],
                          'font': {'color': colors['text']},
                          'title': 'BAR PLOTS~'
                      }})

], style={'backgroundColor':colors['background']}

)

if __name__ == '__main__':
    app.run_server()
