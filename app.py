# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 12:41:43 2022

@author: Admin
"""

from dash import Dash, dcc, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
     
df = pd.read_csv("D:/Plotly learning/Dash-by-Plotly-master/Dash-by-Plotly-master/Good_to_Know/Dash2.0/social_capital.csv")


app = Dash(__name__, external_stylesheets=[dbc.themes.UNITED])
server = app.server
mytitle = dcc.Markdown(children='')
mygraph = dcc.Graph(figure={})
dropdown = dcc.Dropdown(options=df.columns.values[2:],
                        value='Ceaserean delivery date',
                        clearable = False)


#Customizing the layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([mytitle], width=6)
        ], justify='center'),
    dbc.Row([
        dbc.Col([mygraph], width=12)
        ]),
    dbc.Row([
        dbc.Col([dropdown], width=6)
        ], justify='center'),  
    ], fluid = True)

@app.callback(
    Output(mygraph, component_property='figure'),
    Output(mytitle, component_property='children'),
    Input(dropdown, component_property='value')
    ) 

def update_graph(column_name):
    print(column_name)
    print(type(column_name))
    
    fig = px.choropleth(data_frame=df,
                        locations='STATE',
                        locationmode="USA-states",
                        scope='usa',
                        height=600,
                        color=column_name,
                        animation_frame='YEAR')
    
    return fig, '#' + column_name

if __name__=='__main__' :
    app.run_server(debug=True)                        
