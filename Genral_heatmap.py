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

app = dash.Dash(__name__, meta_tags=[{'name': 'viewport','content': 'width=device-width, initial-scale=1.0, maximum-scale=2, minimum-scale=0.1,'}],
                                     update_title='Updating...', external_stylesheets=[dbc.themes.CYBORG])

app.title='GPU Monitoring'
app.layout = html.Div(
    html.Div([
        html.Div(id='live-update-text'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=1*70000, # in milliseconds
            n_intervals=0
        )
    ]),
)

@app.callback(Output('live-update-graph', 'figure'),
              Input('interval-component', 'n_intervals'))

def update_graph_live(n):
    response = requests.get("http://localhost:8000/api-gpu-monitor-single/")
    json_response = response.json()
    json_data = json.loads(json_response) # save the data in json format
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    timey = {"current_time" : current_time}
    json_data.append(timey) # add the current time to the json data
    for i in range(len(json_data)):

        def IP_info():# get the IP list
            IP_list = []
            len_of_response = len(json_data) - 1
            for x in range(len_of_response):
                ip = json_data[x]["ip"]
                IP_list.append(ip)

            return IP_list

        def fan_Data():# get the fan data

            fan_list = []
            len_of_response = len(json_data) - 1
            for x in range(len_of_response):
                fan = json_data[x]["fan"]
                fan_list.append(fan)
            if len(fan_list) % 4 == 0: # if the length of the fan list is divisible by 4, then we can plot the data
                fan_data = np.array(fan_list).reshape(-1, 4)

            else: # if the length of the fan list is not divisible by 4, then we cannot plot the data so we should insert fake data
                len_old = len(fan_list)
                while len_old % 4 != 0:
                    len_old += 1
                    if len_old % 4 == 0:
                        len_new = len_old - len(fan_list)
                        for i in range(len_new):
                            fan_list.append(0)
                        fan_data = np.array(fan_list).reshape(-1, 4)

            return fan_data

        def ugpu_Data():# get the ugpu data

            ugpu_list = []
            len_of_response = len(json_data) - 1
            for x in range(len_of_response):
                ugpu = json_data[x]["ugpu"]
                ugpu_list.append(ugpu)

            if len(ugpu_list) % 4 == 0:
                ugpu_data = np.array(ugpu_list).reshape(-1, 4)

            else:
                len_old = len(ugpu_list)
                while len_old % 4 != 0:
                    len_old += 1
                    if len_old % 4 == 0:
                        len_new = len_old - len(ugpu_list)
                        for i in range(len_new):
                            ugpu_list.append(0)
                ugpu_data = np.array(ugpu_list).reshape(-1, 4)

            return ugpu_data

        def mgpu_Data():# get the mgpu data

            mgpu_list = []
            len_of_response = len(json_data) - 1
            for x in range(len_of_response):
                mgpu = json_data[x]["mgpu"]
                mgpu_list.append(mgpu)

            if len(mgpu_list) % 4 == 0:
                mgpu_data = np.array(mgpu_list).reshape(-1, 4)

            else:
                len_old = len(mgpu_list)
                while len_old % 4 != 0:
                    len_old += 1
                    if len_old % 4 == 0:
                        len_new = len_old - len(mgpu_list)
                        for i in range(len_new):
                            mgpu_list.append(0)
                mgpu_data = np.array(mgpu_list).reshape(-1, 4)

            return mgpu_data

        def temp_Data():# get the temperature data

            temp_list = []
            len_of_response = len(json_data) - 1
            for x in range(len_of_response):
                temp = json_data[x]["temp"]
                temp_list.append(temp)

            if len(temp_list) % 4 == 0:
                temp_data = np.array(temp_list).reshape(-1, 4)

            else:
                len_old = len(temp_list)
                while len_old % 4 != 0:
                    len_old += 1
                    if len_old % 4 == 0:
                        len_new = len_old - len(temp_list)
                        for i in range(len_new):
                            temp_list.append(0)        
                temp_data = np.array(temp_list).reshape(-1, 4)

            return temp_data

        def power_Data():# get the power data

            power_list = []
            len_of_response = len(json_data) - 1
            for x in range(len_of_response):
                power = json_data[x]["power"]
                power_list.append(power)

            if len(power_list) % 4 == 0:
                power_data = np.array(power_list).reshape(-1, 4)

            else:
                len_old = len(power_list)
                while len_old % 4 != 0:
                    len_old += 1
                    if len_old % 4 == 0:
                        len_new = len_old - len(power_list)
                        for i in range(len_new):
                            power_list.append(0)        
                power_data = np.array(power_list).reshape(-1, 4)

            return power_data

        def last_update():# get the last update time of the data when the data is readed
            time = json_data[-1]["current_time"]

            return time
        
    fig = make_subplots(rows=2,
                        cols=3,
                        horizontal_spacing=0.05,
                        vertical_spacing=0.075,
                        start_cell='bottom-left',
                        column_titles=['Fan', 'ugpu', 'mgpu'],
                        subplot_titles=['temp', 'power'])

    fig.add_trace(go.Heatmap(z=fan_Data(), # data it self
                            x = IP_info(), # data for hover
                            zmin=0, # min value of the data
                            zmax=100, # max value of the data
                            colorscale=[[0.0, "rgb(0, 115, 0)"],
                                        [0.1, "rgb(40, 155, 80)"],
                                        [0.2, "rgb(160, 220, 110)"],
                                        [0.25, "rgb(255, 255, 110)"],
                                        [0.3, "rgb(255, 255, 100)"],
                                        [0.4, "rgb(255, 255, 26)"],
                                        [0.5, "rgb(255, 220, 60)"],
                                        [0.6, "rgb(255,170,75)"],
                                        [0.7, "rgb(250,110,70)"],
                                        [0.8, "rgb(220,50, 40)"],
                                        [0.9, "rgb(220,50, 40)"],
                                        [1.0, "rgb(170, 0, 40)"]], # color of the data for bar
                            hovertemplate = "IP: %{x} <br>fan : %{z} </br>" + "<extra></extra>", # hover text format
                            name="fan",
                            hoverongaps = False, # if the data is missing, we should not show the hover text
                            ygap = 1, # the gap between the bar
                            xgap = 1),
                            row=2, col=1) # the position of the bar


    fig.add_trace(go.Heatmap(z=ugpu_Data(),
                            x = IP_info(),
                            zmin=0,
                            zmax=100,
                            colorscale=[[0.0, "rgb(0, 115, 0)"],
                                        [0.1, "rgb(40, 155, 80)"],
                                        [0.2, "rgb(160, 220, 110)"],
                                        [0.25, "rgb(255, 255, 110)"],
                                        [0.3, "rgb(255, 255, 100)"],
                                        [0.4, "rgb(255, 255, 26)"],
                                        [0.5, "rgb(255, 220, 60)"],
                                        [0.6, "rgb(255,170,75)"],
                                        [0.7, "rgb(250,110,70)"],
                                        [0.8, "rgb(220,50, 40)"],
                                        [0.9, "rgb(220,50, 40)"],
                                        [1.0, "rgb(170, 0, 40)"]],
                            hovertemplate = "IP: %{x} <br>ugpu : %{z} </br>" + "<extra></extra>",
                            name="ugpu",
                            hoverongaps = False,
                            ygap = 1,
                            xgap = 1,),
                            row=2, col=2)

    fig.add_trace(go.Heatmap(z=mgpu_Data(),
                            x = IP_info(),
                            zmin=0,
                            zmax=100,
                            colorscale=[[0.0, "rgb(0, 115, 0)"],
                                        [0.1, "rgb(40, 155, 80)"],
                                        [0.2, "rgb(160, 220, 110)"],
                                        [0.25, "rgb(255, 255, 110)"],
                                        [0.3, "rgb(255, 255, 100)"],
                                        [0.4, "rgb(255, 255, 26)"],
                                        [0.5, "rgb(255, 220, 60)"],
                                        [0.6, "rgb(255,170,75)"],
                                        [0.7, "rgb(250,110,70)"],
                                        [0.8, "rgb(220,50, 40)"],
                                        [0.9, "rgb(220,50, 40)"],
                                        [1.0, "rgb(170, 0, 40)"]],
                            hovertemplate = "IP: %{x} <br>mgpu : %{z} </br>" + "<extra></extra>",
                            name="mgpu",
                            hoverongaps = False,
                            ygap = 1,
                            xgap = 1,),
                            row=2, col=3)

    fig.add_trace(go.Heatmap(z=temp_Data(),
                            x = IP_info(),
                            zmin=0,
                            zmax=100,
                            colorscale=[[0.0, "rgb(0, 115, 0)"],
                                        [0.1, "rgb(40, 155, 80)"],
                                        [0.2, "rgb(160, 220, 110)"],
                                        [0.25, "rgb(255, 255, 110)"],
                                        [0.3, "rgb(255, 255, 100)"],
                                        [0.4, "rgb(255, 255, 26)"],
                                        [0.5, "rgb(255, 220, 60)"],
                                        [0.6, "rgb(255,170,75)"],
                                        [0.7, "rgb(250,110,70)"],
                                        [0.8, "rgb(220,50, 40)"],
                                        [0.9, "rgb(220,50, 40)"],
                                        [1.0, "rgb(170, 0, 40)"]],
                            hovertemplate = "IP: %{x} <br>temp : %{z} </br>" + "<extra></extra>",                   
                            name="temp",
                            hoverongaps = False,
                            ygap = 1,
                            xgap = 1,),
                            row=1, col=1)

    fig.add_trace(go.Heatmap(z=power_Data(),
                            x=IP_info(),
                            zmin=0,
                            zmax=100,
                            colorscale='RdYlGn_r',
                            hovertemplate = "IP: %{x} <br>power : %{z} </br>" + "<extra></extra>",
                            name="power",
                            hoverongaps = False,
                            ygap = 1,
                            xgap = 1,),
                            row=1, col=2)

    fig.update_layout(title_text = f"last update : {last_update()}") # title of the graph and last update time
    fig.update_layout(template="plotly_dark") # dark theme
    fig.update_xaxes(visible=False) # hide the x axis
    fig.update_yaxes(visible=False) # hide the y axis
    return fig

if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0", port = 6969) # run the server on port 8050