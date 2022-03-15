# main.py

from doctest import DONT_ACCEPT_BLANKLINE
from fastapi import FastAPI
from h11 import Data
from pydantic import BaseModel
from fastapi import Request
import uvicorn

app = FastAPI()
data_per_device = {'id': 1, 'fan': 15, 'ugpu': 30, 'mgpu': 35, 'temp': 68, 'power': 250, 'ip': '192.168.15.171'}
Datas = []

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
    Datas.append(data_dict)
    print(Datas)
    return { "data" : Datas }


@app.get("/api-gpu-monitor")
async def read_item():
    # data_set = list(set(Datas))
    # print(data_set)
    return {"data" : Datas}

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')