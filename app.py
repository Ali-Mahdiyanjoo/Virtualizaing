# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from inspect import trace
from matplotlib.pyplot import title
import plotly.graph_objs as go
from plotly.offline import plot
from plotly.subplots import make_subplots
from datetime import datetime
import pandas as pd
import numpy as np
import dash
import json
import time

app = dash.Dash(__name__)
output = open("output.json")
data = json.load(output)
read_time = datetime.now()
update_time = read_time.strftime("%H:%M:%S")

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

def IP_info():

    IP_list = []
    for x in range(len(data)):
        x += 1
        ip = data[f"machin_{x}"]["ip"]
        IP_list.append(ip)
        
    return IP_list

def fan_Data():

    fan_list = []
    for x in range(len(data)):
        x += 1
        fan = int(data[f"machin_{x}"]["fan"])
        fan_list.append(fan)

    if len(fan_list) % 4 == 0:
        fan_list.sort(reverse=True)
        fan_data = np.array(fan_list).reshape(-1, 4)

    else:
        len_old = len(fan_list)
        while len_old % 4 != 0:
            len_old += 1
            if len_old % 4 == 0:
                len_new = len_old - len(fan_list)
                for i in range(len_new):
                    fan_list.append(0)
                fan_list.sort(reverse=True)
                fan_data = np.array(fan_list).reshape(-1, 4)

    return fan_data

def ugpu_Data():

    ugpu_list = []
    for x in range(len(data)):
        x += 1
        ugpu = int(data[f"machin_{x}"]["ugpu"])
        ugpu_list.append(ugpu)

    if len(ugpu_list) % 4 == 0:
        ugpu_list.sort(reverse=True)
        ugpu_data = np.array(ugpu_list).reshape(-1, 4)

    else:
        len_old = len(ugpu_list)
        while len_old % 4 != 0:
            len_old += 1
            if len_old % 4 == 0:
                len_new = len_old - len(ugpu_list)
                for i in range(len_new):
                    ugpu_list.append(0)
        ugpu_list.sort(reverse=True)
        ugpu_data = np.array(ugpu_list).reshape(-1, 4)

    return ugpu_data

def mgpu_Data():

    mgpu_list = []
    for x in range(len(data)):
        x += 1
        mgpu = int(data[f"machin_{x}"]["mgpu"])
        mgpu_list.append(mgpu)

    if len(mgpu_list) % 4 == 0:
        mgpu_list.sort(reverse=True)
        mgpu_data = np.array(mgpu_list).reshape(-1, 4)

    else:
        len_old = len(mgpu_list)
        while len_old % 4 != 0:
            len_old += 1
            if len_old % 4 == 0:
                len_new = len_old - len(mgpu_list)
                for i in range(len_new):
                    mgpu_list.append(0)
        mgpu_list.sort(reverse=True)
        mgpu_data = np.array(mgpu_list).reshape(-1, 4)

    return mgpu_data

def temp_Data():

    temp_list = []
    for x in range(len(data)):
        x += 1
        temp = int(data[f"machin_{x}"]["temp"])
        temp_list.append(temp)

    if len(temp_list) % 4 == 0:
        temp_list.sort(reverse=True)
        temp_data = np.array(temp_list).reshape(-1, 4)

    else:
        len_old = len(temp_list)
        while len_old % 4 != 0:
            len_old += 1
            if len_old % 4 == 0:
                len_new = len_old - len(temp_list)
                for i in range(len_new):
                    temp_list.append(0)        
        temp_list.sort(reverse=True)
        temp_data = np.array(temp_list).reshape(-1, 4)

    return temp_data

def power_Data():

    power_list = []
    for x in range(len(data)):
        x += 1
        power = float(data[f"machin_{x}"]["power"])
        power_list.append(power)

    if len(power_list) % 4 == 0:
        power_list.sort(reverse=True)
        power_data = np.array(power_list).reshape(-1, 4)

    else:
        len_old = len(power_list)
        while len_old % 4 != 0:
            len_old += 1
            if len_old % 4 == 0:
                len_new = len_old - len(power_list)
                for i in range(len_new):
                    power_list.append(0)        
        power_list.sort(reverse=True)
        power_data = np.array(power_list).reshape(-1, 4)

    return power_data

# template ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"]
# fig.update_layout(template="ggplot2")
# olorscale='RdYlGn_r'

fig = make_subplots(rows=2,
                    cols=5,
                    horizontal_spacing=0.05,
                    vertical_spacing=0.075,
                    start_cell='bottom-left',
                    column_titles=['Fan', 'ugpu', 'mgpu'],
                    subplot_titles=['temp', 'power'])

fig.add_trace(go.Heatmap(z=fan_Data(),
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
                        name="fan",
                        hoverongaps = False,
                        ygap = 1,
                        xgap = 1),
                        row=2, col=1)

                        # colorbar = {"title": "speed"}

fig.add_trace(go.Heatmap(z=ugpu_Data(),
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
                        name="ugpu",
                        hoverongaps = False,
                        ygap = 1,
                        xgap = 1,),
                        row=2, col=2)

fig.add_trace(go.Heatmap(z=mgpu_Data(),
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
                                    [1.0, "rgb(170, 0, 40)"]],                        name="mgpu",
                        hoverongaps = False,
                        ygap = 1,
                        xgap = 1,),
                        row=2, col=3)

fig.add_trace(go.Heatmap(z=temp_Data(),
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
                                    [1.0, "rgb(170, 0, 40)"]],                        name="temp",
                        hoverongaps = False,
                        ygap = 1,
                        xgap = 1,),
                        row=1, col=1)

fig.add_trace(go.Heatmap(z=power_Data(),
                        zmin=0,
                        zmax=100,
                        colorscale='RdYlGn_r',
                        hoverongaps = False,
                        ygap = 1,
                        xgap = 1,
                        name="power",),
                        row=1, col=2)
# fig.layout.height = 1500
# fig.layout.width = 1500
# fig.update_layout(title_text="GPU Monitoring")
# fig.update_layout(template="plotly")
fig.show()


app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[

    html.H1('Hello Dash', style={'textAlign': 'center', 'color': '#7FDBFF'}),

    html.Div(children='Dash: A web application framework for your data.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

# you can add debug to True for enabling debuging mode
if __name__ == '__main__':
    app.run_server()