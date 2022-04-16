from dash.dependencies import Input, Output
from plotly.subplots import make_subplots
from matplotlib.pyplot import title
from plotly.offline import plot
from datetime import datetime
from time import sleep, time
from dash import dcc, html
from inspect import trace
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
import numpy as np
import requests
import plotly
import dash
import json

response = requests.get("http://localhost:8000/get_IP_list/")
json_response = response.json()
json_data = json.loads(json_response)
IP_of_machins = json_data["IPs"]

app = dash.Dash(__name__, meta_tags=[{'name': 'viewport','content': 'width=device-width, initial-scale=1.0, maximum-scale=2, minimum-scale=0.1,'}], update_title='Updating...', external_stylesheets=[dbc.themes.CYBORG])

app.title='GPU Monitoring'
fig_dropdown = html.Div([
    dcc.Dropdown(options=[{'label': i, 'value': i} for i in IP_of_machins],value=IP_of_machins[1] ,id='dropdown', placeholder="Select IP")])

fig_plot = html.Div(
    html.Div([
        html.Div(id='live-update-text'),
        dcc.Graph(id='live-update-graph'),
    ]),
)
app.layout = html.Div([fig_dropdown, fig_plot])

@app.callback(Output('live-update-graph', 'figure'),
                Input('dropdown', 'value'))


def update_graph_live(fig_dropdown):
    response = requests.get(f"http://localhost:8000/api-gpu-monitor/{fig_dropdown}")
    json_response = response.json()
    json_data = json.loads(json_response)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    timey = {"current_time" : current_time}
    json_data.update(timey)
    for i in range(len(json_data["data"])):

        def IP_info():#
            IP_list = []
            for x in range(len(json_data["data"])):
                ip = json_data["data"][x]["ip"]
                IP_list.append(ip)

            return list(set(IP_list))

        def fan_Data():#

            fan_list = []
            for x in range(len(json_data["data"])):
                fan = json_data["data"][x]["fan"]
                fan_list.append(fan)
            if len(fan_list) % 4 == 0:
                fan_data = np.array(fan_list).reshape(-1, 4)

            else:
                len_old = len(fan_list)
                while len_old % 4 != 0:
                    len_old += 1
                    if len_old % 4 == 0:
                        len_new = len_old - len(fan_list)
                        for i in range(len_new):
                            fan_list.append(0)
                        fan_data = np.array(fan_list).reshape(-1, 4)

            return fan_data

        def ugpu_Data():#

            ugpu_list = []
            for x in range(len(json_data["data"])):
                ugpu = json_data["data"][x]["ugpu"]
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

        def mgpu_Data():#

            mgpu_list = []
            for x in range(len(json_data["data"])):
                mgpu = json_data["data"][x]["mgpu"]
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

        def temp_Data():#

            temp_list = []
            for x in range(len(json_data["data"])):
                temp = json_data["data"][x]["temp"]
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

        def power_Data():

            power_list = []
            for x in range(len(json_data["data"])):
                power = json_data["data"][x]["power"]
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
        def date_Data():#

            date_list = []
            for x in range(len(json_data["data"])):
                date = json_data["data"][x]["date"]
                date_list.append(date)
            if len(date_list) % 4 == 0:
                date_data = np.array(date_list).reshape(-1, 4)

            else:
                len_old = len(date_list)
                while len_old % 4 != 0:
                    len_old += 1
                    if len_old % 4 == 0:
                        len_new = len_old - len(date_list)
                        for i in range(len_new):
                            date_list.append(0)
                        date_data = np.array(date_list).reshape(-1, 4)

            return date_data

        def time_Data():#

            time_list = []
            for x in range(len(json_data["data"])):
                time = json_data["data"][x]["time"]
                time_list.append(time)
            if len(time_list) % 4 == 0:
                time_data = np.array(time_list).reshape(-1, 4)

            else:
                len_old = len(time_list)
                while len_old % 4 != 0:
                    len_old += 1
                    if len_old % 4 == 0:
                        len_new = len_old - len(time_list)
                        for i in range(len_new):
                            time_list.append(0)
                        time_data = np.array(time_list).reshape(-1, 4)

            return time_data

        def last_update():
            time = json_data["current_time"]

            return time
        
    fig = make_subplots(rows=1, cols=1, shared_xaxes=True)

    fig.add_trace(go.Scatter(y = fan_Data(),
                            x = time_Data(),
                            mode="lines",
                            hovertemplate = "Fan : %{y} <br>Time : %{x} </br><extra></extra>",
                            name="fan"),
                            row=1, col=1)
    
    fig.add_trace(go.Scatter(y = ugpu_Data(),
                            x = time_Data(),
                            mode="lines",
                            hovertemplate = "Ugpu : %{y} <br>Time : %{x} </br><extra></extra>",
                            name="ugpu"),
                            row=1, col=1)

    fig.add_trace(go.Scatter(y = mgpu_Data(),
                            x = time_Data(),
                            mode="lines",
                            hovertemplate = "Mgpu : %{y} <br>Time : %{x} </br><extra></extra>",
                            name="mgpu"),
                            row=1, col=1)

    fig.add_trace(go.Scatter(y = temp_Data(),
                            x = time_Data(),
                            mode="lines",
                            hovertemplate = "Temp : %{y} <br>Time : %{x} </br><extra></extra>",                   
                            name="temp"),
                            row=1, col=1)

    fig.add_trace(go.Scatter(y = power_Data(),
                            x = time_Data(),
                            mode="lines",
                            hovertemplate = "Power : %{y} <br>Time : %{x} </br><extra></extra>",
                            name="power"),
                            row=1, col=1)
    
    # fig.layout.height = 900
    fig.layout.width = 1900
    # fig.update_layout(yaxis=dict(range=[0, 100]))
    fig.update_layout(title_text = f"last update : {last_update()}")
    fig.update_layout(template="plotly_dark")
    fig.update_layout({"xaxis": {"title":"Time"},
                   "showlegend": False})
    return fig

if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0", port=8585)