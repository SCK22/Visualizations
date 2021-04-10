# import pandas_datareader.data as web
import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import numpy as np
import plotly.graph_objs as go
import plotly.figure_factory as ff
import plotly.tools as tls
import pandas as pd
import plotly.express as px
import numpy as np
import os

def create_options(dataset_name):
    """Creates options in the format that dash needs
    # options=[
    #     {'label': 'Categorical Columns', 'value': 'cat_col'},
    #     {'label': 'Numeric columns', 'value': 'num_col'},
    #    .
    #    .
    #     {'label': 'ideal randomness', 'value': 'ideal randomness'},
    #     {'label':'normal distribution', 'value':'normal distribution'}
    # ],
    """
    options = []
    for i in df.columns:
        options.append({'label': "{}: {}".format(str(i),df[i].dtype), 'value': str(i)})
    return options
    
app = dash.Dash()

df = pd.read_csv("./titanic/train.csv")
df.dropna(inplace = True)
df.head()

app.layout = html.Div(children=[

    html.H1(children='Titanic Dataset Univariate Visualizations'),
    html.Div(children='''
        Select a plot:
    '''),
    # this will create a dropdown in the html page, selecting a value here will pass the value to 
    # the function called below
        dcc.Dropdown(id='input',
            options = create_options(df),
        value=np.random.choice(df.columns),
        ),
    html.Div(id='output-graph',
        ),
    ])

@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)

def return_plot(input_data):
    if df[input_data].dtype in ['object']:
        vc = df[input_data.split(':')[0]].value_counts()
        return dcc.Graph(
            id = input_data,
            figure={
            'data' : [go.Bar(
            x=vc.index,
            y=vc.values,
            name = input_data.split(':')[0],
            text = vc.values,
            textposition = "auto",
            )],
            'layout' : {'title':'Distribution plot of {} column'.format(input_data.split(':')[0])}
            })
    if df[input_data].dtype in ['int64','float64']:
        return dcc.Graph(
            id =input_data,
            figure = px.histogram(df, x=input_data,opacity=0.8,
            # color_discrete_sequence=np.random.choice(px.colors.qualitative,1)[0], # choose a random color from the color palate
            title='Histogram of {}'.format(input_data)))
    
if __name__ == '__main__':
    app.run_server(debug=True)

