# import MySQLdb
# db = MySQLdb.connect(user = "root", passwd = "Vmware@123", db = "gpu_monitoring")

# cursor = db.cursor()
# max_price=5
# cursor.execute("""SELECT * FROM users""")

# curl -X 'POST' 'http://192.168.22.140:8000/' -H 'accept: application/json' -H 'Content-Type: application/json' -d @/usr/sbin/nvidia-smi-collector-json >/dev/null 2>&1
# /usr/sbin/nvidia-smi-collector.sh

# a = [{'fan': '30', 'ugpu': '0', 'mgpu': '10', 'temp': '34', 'power': '4.77', 'ip': '192.168.15.138'},{'fan': '30', 'ugpu': '0', 'mgpu': '10', 'temp': '34', 'power': '4.77', 'ip': '192.168.15.136'},{'fan': '30', 'ugpu': '0', 'mgpu': '10', 'temp': '34', 'power': '4.77', 'ip': '192.168.15.136'}, {'fan': '30', 'ugpu': '0', 'mgpu': '10', 'temp': '34', 'power': '2.53', 'ip': '192.168.15.136'}]
# da = []
# print(len(a))
# for i in range(len(a)):
#     leny = len(a)
#     if i > leny - 1:
#         if i == leny:192.168.15.69
#             if a[i - 1]["ip"] == a[leny - 1]["ip"]:
#                 del a[i - 1]
#                 print(a)
#     else:
#         b = a[i]["ip"]
#         if b == a[i + 1]["ip"]:
#             # da.append(a[i])
#             del a[i]
#             print(a)
#         elif b == a[i + 2]["ip"]:
#             del a[i]
# from pymongo import MongoClient

# client = MongoClient(host="localhost", port=27017)
# db = client["GPU_MONITORING"]
# mycol = db["DATAS"]
# IPs = []

# for x in mycol.find({ "ip": { "$regex" : "^192."} }, {"_id": 0, "date": 0, "time": 0, "fan": 0, "ugpu": 0, "mgpu": 0, "temp": 0, "power": 0}):
#   IPs.append(x.get("ip"))
# adt_dict = {}
# adt_dict.update({"IPs" : list(set(IPs))})
# print(adt_dict)
# from fastapi import FastAPI
# import uvicorn

# app = FastAPI()
 
# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}

# if __name__ == '__main__':
#     uvicorn.run(app, port=8000, host='0.0.0.0')
# myquery = { "ip": { "$eq": '192.168.15.136' } }

# dat = []

# for x in mycol.find(myquery):
#     dat.append(x)

# print(dat)
from datetime import datetime
from time import sleep
import numpy as np
import requests
import json

# response = requests.get("http://localhost:8000/api-gpu-monitor-single/")
# json_response = response.json()
# json_data = json.loads(json_response)
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# timey = {"current_time" : current_time}
# json_data.append(timey)
# for i in range(len(json_data)):

#     def IP_info():#
#         IP_list = []
#         len_of_response = len(json_data) - 1
#         for x in range(len_of_response):
#             ip = json_data[x]["ip"]
#             IP_list.append(ip)

#         return IP_list

#     def fan_Data():#

#         fan_list = []
#         len_of_response = len(json_data) - 1
#         for x in range(len_of_response):
#             fan = json_data[x]["fan"]
#             fan_list.append(fan)
#         if len(fan_list) % 4 == 0:
#             fan_data = np.array(fan_list).reshape(-1, 4)

#         else:
#             len_old = len(fan_list)
#             while len_old % 4 != 0:
#                 len_old += 1
#                 if len_old % 4 == 0:
#                     len_new = len_old - len(fan_list)
#                     for i in range(len_new):
#                         fan_list.append(0)
#                     fan_data = np.array(fan_list).reshape(-1, 4)

#         return fan_data

#     def last_update():
#         time = json_data[-1]["current_time"]

#         return time
    
# print(last_update())
# response = requests.get("http://localhost:8000/get_IP_list/")
# json_response = response.json()
# json_data = json.loads(json_response)
# IP_of_machins = json_data["IPs"]
# print(IP_of_machins)
# for i in IP_of_machins:
# response = requests.get("http://localhost:8000/api-gpu-monitor/192.168.15.136")
# json_response = response.json()
# json_data = json.loads(json_response)
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# timey = {"current_time" : current_time}
# json_data.update(timey)
# for i in range(len(json_data["data"])):

#     def IP_info():#
#         IP_list = []
#         for x in range(len(json_data["data"])):
#             ip = json_data["data"][x]["ip"]
#             IP_list.append(ip)

#         return list(set(IP_list))

# # print(IP_info())
#     def time_Data():#

#         time_list = []
#         for x in range(len(json_data["data"])):
#             time = json_data["data"][x]["time"]
#             time_list.append(time)
#         if len(time_list) % 4 == 0:
#             time_data = np.array(time_list).reshape(-1, 4)

#         else:
#             len_old = len(time_list)
#             while len_old % 4 != 0:
#                 len_old += 1
#                 if len_old % 4 == 0:
#                     len_new = len_old - len(time_list)
#                     for i in range(len_new):
#                         time_list.append(0)
#                     time_data = np.array(time_list).reshape(-1, 4)

#         return time_data
        
#     def date_Data():#

#         date_list = []
#         for x in range(len(json_data["data"])):
#             date = json_data["data"][x]["date"]
#             date_list.append(date)
#         if len(date_list) % 4 == 0:
#             date_data = np.array(date_list).reshape(-1, 4)

#         else:
#             len_old = len(date_list)
#             while len_old % 4 != 0:
#                 len_old += 1
#                 if len_old % 4 == 0:
#                     len_new = len_old - len(date_list)
#                     for i in range(len_new):
#                         date_list.append(0)
#                     date_data = np.array(date_list).reshape(-1, 4)

#         return date_data

# print(date_Data())
# def last_update():
#     time = json_data["current_time"]

#     return time
# print(last_update())
# import plotly.graph_objects as go
# import pandas as pd

# fig = go.Figure(go.Scatter(
#     x = df['Date'],
#     y = df['mavg']
# ))
# import plotly.express as px
# import plotly.graph_objs as go
# fig = go.Figure(data=go.Scatter(x=df_month['month'].astype(dtype=str), 
#                         y=df_month['counts'],
#                         marker_color='indianred', text="counts"))

# fig.update_layout({"title": 'Tweets about Malioboro from Jan 2020 to Jan 2021',
#                    "xaxis": {"title":"Months"},
#                    "yaxis": {"title":"Total tweets"},
#                    "showlegend": False})
# fig.write_image("by-month.png",format="png", width=1000, height=600, scale=3)
# fig.show()
# from datetime import datetime as dtt
# from datetime import timedelta
# import time

# timy = datetime.now().time()
# time.sleep(2)
# tim = datetime.now().time()
# t1 = timedelta(hours=timy.hour, minutes=timy.minute, seconds=timy.second)
# t2 = timedelta(hours=tim.hour, minutes=tim.minute, seconds=tim.second)
# print(t1)
# print(t2)
# time_only = dtt.strptime(str(t2), "%H:%M:%S") - dtt.strptime(str(t1), "%H:%M:%S")

# print(time_only)