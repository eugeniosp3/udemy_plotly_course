# imports
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('C:/Users/eugen/OneDrive/Main_Env/udemy_dash_course/Data/2018WinterOlympics.csv')

medals = ['Gold', 'Silver', 'Bronze', 'Total']
colored = ['#FFE800', '#CECECE', '#EAAA71', '#900C3F']

countries = [x for x in df['NOC'].unique()]

data = [go.Bar(x=df['NOC'],
               y=df[m], name=m, marker={'color': colored[c]}) for c, m in enumerate(medals)]
layout = go.Layout(title='Medals', barmode='stack')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
