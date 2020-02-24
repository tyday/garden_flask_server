# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

import datetime
import pandas as pd
import sqlite3 as lite
import sys
 
conn = lite.connect('Sensor.db')
query = "SELECT *  FROM SensorReading WHERE timestamp < 158247470900;"

df = pd.read_sql_query(query,conn)
print(df)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            # 'data': [
            #     {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
            #     {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            # ],
            'data' : [
                dict(
                    x=df['timestamp'].map(lambda ts: datetime.datetime.fromtimestamp(ts)),
                    y=df['temp1'].map(lambda a: a*1.8+32),
                    name="Env Temp"
                ),
                dict(
                    x=df['timestamp'].map(lambda ts: datetime.datetime.fromtimestamp(ts)),
                    y=df['temp2'].map(lambda a: a*1.8+32),
                    name="GH Temp"
                ),
                dict(
                    x=df['timestamp'].map(lambda ts: datetime.datetime.fromtimestamp(ts)),
                    y=df['RH1'],
                    name='Env RH'
                ),
                dict(
                    x=df['timestamp'].map(lambda ts: datetime.datetime.fromtimestamp(ts)),
                    y=df['RH2'],
                    name='GH RH'
                ),
                dict(
                    x=df['timestamp'].map(lambda ts: datetime.datetime.fromtimestamp(ts)),
                    y=df['light'],
                    name='Light',
                    yaxis='y2'
                ),
            ],
            'layout': {
                'title': 'Dash Data Visualization',
                "yaxis2": dict(
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
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)