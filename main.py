# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Request
from pymongo import MongoClient
import time
import uvicorn
import json
from bson import ObjectId

app = FastAPI()
data_per_device = {'id': 1, 'fan': 15, 'ugpu': 30, 'mgpu': 35, 'temp': 68, 'power': 250, 'ip': '192.168.15.171'}
Datas = []
Datas_time = []
client = MongoClient(host="localhost", port=27017)
db = client["GPU_MONITORING"]
mycol = db["DATAS"]
mycol_single = db["DATAS_SINGLE"]

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

class GPU_DATA(BaseModel):
    fan : str
    ugpu : str 
    mgpu : str
    temp : str
    power : str
    ip : str

@app.post("/")
async def getting_data(data : GPU_DATA):
    data_dict = dict(data)
    daty = time.strftime("%d/%m/%Y")
    timy = time.strftime("%H:%M:%S")
    data_dict.update({"date": daty})
    data_dict.update({"time" : timy}) 
    # Datas.append(data_dict)
    x = mycol.insert_one(data_dict)
    print(x.inserted_id)
    print(data_dict)
    return { "data" : Datas }

@app.post("/realtime")
async def getting_data(data : GPU_DATA):
    data_dict = dict(data)
    IP = data_dict["ip"]
    IP_dict = mycol_single.find_one({"ip": IP})
    IP_x = IP_dict["ip"]
    if IP == IP_x:
        mycol_single.delete_one({ "ip": IP })
        mycol_single.insert_one(data_dict)
        print("fuck")
        x = JSONEncoder().encode(data_dict)
        return x
    else:
        mycol_single.insert_one(data_dict)
        print("fuck_else")
        x = JSONEncoder().encode(data_dict)
        return x

@app.get("/api-gpu-monitor/{ip_address}")
async def read_item(ip_address):
    myquery = { "ip": { "$eq": ip_address } }
    # print(myquery)
    dat = []

    for x in mycol.find(myquery):
        dat.append(x)
    adt_dict = {}
    adt_dict.update({"data" : dat})
    print(type(adt_dict))
    return adt_dict

@app.get("/api-gpu-monitor-single/")
async def read_item():
    myquery = { "ip": { "$regex" : "^192."} }
    dat = []
    for x in mycol_single.find(myquery):
        dat.append(x)
        print(x)

    # for x in mycol.find(myquery):
    #     dat.append(x)
    # adt_dict = {}
    # adt_dict.update({"data" : dat})
    # print(type(adt_dict))
    # return adt_dict

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')
