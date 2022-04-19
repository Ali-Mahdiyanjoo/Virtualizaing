from dash.dependencies import Input, Output
from plotly.subplots import make_subplots
from matplotlib.pyplot import title
from plotly.offline import plot
from datetime import datetime
from time import sleep, time
from dash import dcc, html
from inspect import trace
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import numpy as np
import requests
import plotly
import dash
import json

response = requests.get("http://localhost:8000/get_IP_list/") # send request to server
json_response = response.json()
json_data = json.loads(json_response) # convert response to JSON
IP_of_machins = json_data["IPs"] # get IPs from JSON
app = dash.Dash(__name__, meta_tags=[{'name': 'viewport','content': 'width=device-width, initial-scale=1.0, maximum-scale=2, minimum-scale=0.1,'}],
 update_title='Updating...')

app.title='GPU Monitoring'

fig_dropdown = html.Div([ # dropdown menu
    dcc.Dropdown(options=[{'label': i, 'value': i} for i in IP_of_machins], value=IP_of_machins[0], 
    id='dropdown',
    placeholder="Select IP")])

fig_plot = html.Div(html.Div([ # plot the graph
        html.Div(id='live-update-text'),
        dcc.Graph(id='live-update-graph'),
    ]),
)
app.layout = html.Div([fig_dropdown, fig_plot]) # put dropdown menu and plot into the app

@app.callback(Output('live-update-graph', 'figure'), 
                Input('dropdown', 'value'))


def update_graph_live(fig_dropdown): # fig_dropdown is the value of dropdown menu
    response = requests.get(f"http://localhost:8000/api-gpu-monitor/{fig_dropdown}") # send request to server with selected IP
    json_response = response.json()
    json_data = json.loads(json_response)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S") # get current time in format HH:MM:SS
    timey = {"current_time" : current_time}
    json_data.update(timey)
    for i in range(len(json_data["data"])): # get length of data and loop through each element

        def fan_Data():
            fan_list = []
            for x in range(len(json_data["data"])):
                fan = json_data["data"][x]["fan"] # get fan value
                fan_list.append(fan) # append fan value to fan_list

            return fan_list

        def ugpu_Data():
            ugpu_list = []
            for x in range(len(json_data["data"])):
                ugpu = json_data["data"][x]["ugpu"] # get ugpu value
                ugpu_list.append(ugpu) # append ugpu value to ugpu_list

            return ugpu_list

        def mgpu_Data():
            mgpu_list = []
            for x in range(len(json_data["data"])):
                mgpu = json_data["data"][x]["mgpu"] # get mgpu value
                mgpu_list.append(mgpu) # append mgpu value to mgpu_list
                
            return mgpu_list

        def temp_Data():
            temp_list = []
            for x in range(len(json_data["data"])):
                temp = json_data["data"][x]["temp"] # get temp value
                temp_list.append(temp) # append temp value to temp_list

            return temp_list

        def power_Data():
            power_list = []
            for x in range(len(json_data["data"])):
                power = json_data["data"][x]["power"] # get power value
                power_list.append(float(power)) # append power value to power_list

            return power_list

        def date_Data():
            date_list = []
            for x in range(len(json_data["data"])):
                date = json_data["data"][x]["date"] # get date value
                date_list.append(date) # append date value to date_list

            return date_list

        def last_update():
            time = json_data["current_time"] # get time value for last update

            return time
        
    fig = make_subplots(rows=1, cols=1, shared_xaxes=True) # make subplots to plot graph with multiple graphs

    fig.add_trace(go.Scatter(y = power_Data(), # data to plot
                            x = date_Data(), # x axis data
                            mode="lines + markers", # mode of plot
                            hovertemplate = "Power : %{y} <br>Time : %{x} </br><extra></extra>", # hover template formate
                            name="power"), # name of the plot
                            row=1, col=1) # row and column of the plot

    fig.add_trace(go.Scatter(y = fan_Data(),
                            x = date_Data(),
                            mode="lines + markers",
                            hovertemplate = "Fan : %{y} <br>Time : %{x} </br><extra></extra>",
                            name="fan"),
                            row=1, col=1)
    
    fig.add_trace(go.Scatter(y = ugpu_Data(),
                            x = date_Data(),
                            mode="lines + markers",
                            hovertemplate = "Ugpu : %{y} <br>Time : %{x} </br><extra></extra>",
                            name="ugpu"),
                            row=1, col=1)

    fig.add_trace(go.Scatter(y = mgpu_Data(),
                            x = date_Data(),
                            mode="lines + markers",
                            hovertemplate = "Mgpu : %{y} <br>Time : %{x} </br><extra></extra>",
                            name="mgpu"),
                            row=1, col=1)

    fig.add_trace(go.Scatter(y = temp_Data(),
                            x = date_Data(),
                            mode="lines + markers",
                            hovertemplate = "Temp : %{y} <br>Time : %{x} </br><extra></extra>",                   
                            name="temp"),
                            row=1, col=1)

    fig.update_layout(height = 1080) # height of the plot
    fig.update_layout(title_text = f"last update : {last_update()}") # add title to the plot from last update time
    fig.update_layout(template="plotly_dark") # template of the plot
    fig.update_layout({"xaxis": {"title":"Time"}}) # add title to x axis

    return fig

if __name__ == '__main__': # run the app
    app.run_server(debug=True, host="0.0.0.0", port=8585)