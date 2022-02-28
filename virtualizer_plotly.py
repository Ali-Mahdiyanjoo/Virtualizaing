from dash.dependencies import Input, Output
from plotly.subplots import make_subplots
from matplotlib.pyplot import title
from plotly.offline import plot
from datetime import datetime
from time import sleep, time
from dash import dcc, html
from inspect import trace
import plotly.graph_objs as go
import numpy as np
import requests
import plotly
import dash
import time

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(
    html.Div([
        html.H1('The time is: ' + str(datetime.now())),
        html.Div(id='live-update-text'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=1*70000, # in milliseconds
            n_intervals=0
        )
    ])
)
# Multiple components can update everytime interval gets fired.
@app.callback(Output('live-update-graph', 'figure'),
              Input('interval-component', 'n_intervals'))

def update_graph_live(n):
    response = requests.get("https://panel.plusai.cloud/api-gpu-monitor")
    json_response = response.json()
    last_page = json_response["last_page"]
    for i in range(last_page):
        i += 1
        response = requests.get(f"https://panel.plusai.cloud/api-gpu-monitor?page={i}")
        json_response = response.json()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        timey = {"current_time" : current_time}
        json_response.update(timey)
        print(json_response)

        def IP_info():#

            IP_list = []
            for x in range(json_response["total"]):
                ip = json_response["data"][x]["ip"]
                IP_list.append(ip)
                
            return IP_list

        def fan_Data():#

            fan_list = []
            for x in range(json_response["total"]):
                    fan = json_response["data"][x]["fan"]
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

        def ugpu_Data():#

            ugpu_list = []
            for x in range(json_response["total"]):
                ugpu = json_response["data"][x]["ugpu"]
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

        def mgpu_Data():#

            mgpu_list = []
            for x in range(json_response["total"]):
                mgpu = json_response["data"][x]["mgpu"]
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

        def temp_Data():#

            temp_list = []
            for x in range(json_response["total"]):
                temp = json_response["data"][x]["temp"]
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
            for x in range(json_response["total"]):
                power = json_response["data"][x]["power"]
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
                            hovertemplate = "IP: %{IP} <br>fan : %{z} </br>",
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
                            hovertemplate = "IP: %{IP} <br>ugpu : %{z} </br>",
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
                                        [1.0, "rgb(170, 0, 40)"]],
                            hovertemplate = "IP: %{IP} <br>mgpu : %{z} </br>",
                            name="mgpu",
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
                                        [1.0, "rgb(170, 0, 40)"]],
                            hovertemplate = "IP: %{IP_info} <br>temp : %{z} </br>",                   
                            name="temp",
                            # hoverongaps = False,
                            ygap = 1,
                            xgap = 1,),
                            row=1, col=1)

    fig.add_trace(go.Heatmap(z=power_Data(),
                            zmin=0,
                            zmax=100,
                            colorscale='RdYlGn_r',
                            hovertemplate = "IP: %{IP} <br>power : %{z} </br>",
                            ygap = 1,
                            xgap = 1,
                            name="power",),
                            row=1, col=2)
    fig.layout.height = 900
    fig.layout.width = 1800
    # fig.update_layout(title_text="GPU Monitoring")
    # fig.update_layout(template="plotly")

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)