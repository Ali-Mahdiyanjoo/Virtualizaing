# main.py
from typing import List
from fastapi import FastAPI
from h11 import Data
from pydantic import BaseModel
from fastapi import Request
from pymongo import MongoClient
import time
import uvicorn

app = FastAPI()
data_per_device = {'id': 1, 'fan': 15, 'ugpu': 30, 'mgpu': 35, 'temp': 68, 'power': 250, 'ip': '192.168.15.171'}
Datas = []
Datas_time = []
client = MongoClient(host="192.168.15.69", port=27017)
db = client["GPU_MONITORING"]
mycol = db["DATAS"]
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
    Datas.append(data_dict)
    x = mycol.insert_one(Datas)
    print(x.inserted_id)
    print(Datas)
    return { "data" : Datas }


@app.get("/api-gpu-monitor")
async def read_item():
    return {"data" : Datas}

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')