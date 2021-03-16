# obejctive - develop line chart plots 7 days worth of temp data on one graph

# imports

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


df = pd.read_csv('/udemy_dash_course/Data/2010YumaAZ.csv')

days = [x for x in df['DAY'].unique()]


# traces
data = []
for d in days:
    traces = go.Scatter(x=df['LST_TIME'],
               y=df[df['DAY']==d]['T_HR_AVG'],
               mode='lines',
               name=d,)
    data.append(traces)

# Layout design options - title, axis, etc
layout = go.Layout(title='Line Chart')

# plotting
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)

