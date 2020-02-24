import pandas as pd
import numpy as np
import datetime

import plotly.offline as pyo
import plotly.graph_objs as go

def convert_to_f(temp):
    return temp * 1.8 + 32

# Reading in CSV files. Use the read_csv command.
# More options: https://pandas.pydata.org/pandas-docs/stable/io.html
df = pd.read_csv('SensorReading.csv')
# df.set_index('timestamp', inplace=True)
df = df[df.timestamp < 158247470900]
# df = df[['temp1','temp2','RH1','RH2']]

print(df)
trace0 = go.Scatter(
    x=df['timestamp'].map(lambda ts: datetime.datetime.fromtimestamp(ts)),
    y=df['temp1'].map(lambda a: a*1.8+32),
    name="Env Temp"
)
trace1 = go.Scatter(
    x=df['timestamp'].map(lambda ts: datetime.datetime.fromtimestamp(ts)),
    y=df['temp2'].map(lambda a: a*1.8+32),
    name="GH Temp"
)
trace2 = go.Scatter(
    x=df['timestamp'].map(lambda ts: datetime.datetime.fromtimestamp(ts)),
    y=df['RH1'],
    name='Env RH'
)
trace3 = go.Scatter(
    x=df['timestamp'].map(lambda ts: datetime.datetime.fromtimestamp(ts)),
    y=df['RH2'],
    name='GH RH'
)
trace4 = go.Scatter(
    x=df['timestamp'].map(lambda ts: datetime.datetime.fromtimestamp(ts)),
    y=df['light'],
    name='Light',
    yaxis='y2'
)
data = [trace0,trace1,trace2,trace3,trace4]




layout = go.Layout(
    title="Greenhouse information",
    yaxis=dict(
        # title='yaxis title'
    ),
    yaxis2=dict(
        title='light level',
        titlefont=dict(
            color='rgb(148, 103, 189)'
        ),
        tickfont=dict(
            color='rgb(148, 103, 189)'
        ),
        overlaying='y',
        side='right'
    )
)

fig = go.Figure(data=data,layout=layout)
pyo.plot(fig, filename="greenhouse.html")