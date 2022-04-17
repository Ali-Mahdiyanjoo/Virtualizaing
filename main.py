# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Request
from pymongo import MongoClient
import time
import uvicorn
import json
from bson import ObjectId
from datetime import timedelta
from datetime import datetime
from datetime import datetime as dtt

app = FastAPI()
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

# 1 done
@app.post("/")
async def getting_data(data : GPU_DATA):
    data_dict = dict(data)
    daty = time.strftime("%Y-%m-%d")
    timy = time.strftime("%H:%M:%S")
    data_dict.update({"date": daty + " " + timy})
    x = mycol.insert_one(data_dict)
    y = JSONEncoder().encode(data_dict)
    return y

# 2 done
@app.post("/realtime")
async def getting_data(data : GPU_DATA):
    data_dict = dict(data)
    timy = datetime.now().time()
    t1 = timedelta(hours=timy.hour, minutes=timy.minute)
    data_dict.update({"time": str(t1)})
    IP = data_dict["ip"]
    IP_dict = mycol_single.find_one({"ip": IP}) # it will go to see there is a document with this IP
    for x in mycol_single.find({"ip": { "$regex" : "^192."}}):
        end = x["time"]
        tim = datetime.now().time()
        t2 = timedelta(hours=tim.hour, minutes=tim.minute)
        time_only = dtt.strptime(str(t2), "%H:%M:%S") - dtt.strptime(end, "%H:%M:%S")
        if str(time_only) == "0:10:00":
            mycol_single.delete_one({"ip": IP})
    if IP_dict is None:
        mycol_single.insert_one(data_dict)
        x = JSONEncoder().encode(data_dict)
        return x
    else:
        mycol_single.update_one({"ip": IP}, {"$set": data_dict})
        x = JSONEncoder().encode(data_dict)
        return x

# 3 done
@app.get("/api-gpu-monitor/{ip_address}")
async def read_item(ip_address):
    myquery = { "ip": { "$eq": ip_address } }
    dat = []

    for x in mycol.find(myquery):
        dat.append(x)
    adt_dict = {}
    adt_dict.update({"data" : dat})
    x = JSONEncoder().encode(adt_dict)
    return x

# 4 done
@app.get("/api-gpu-monitor-single/")
async def read_item():
    dat = []

    for x in mycol_single.find({"ip": { "$regex" : "^192."}}):
        dat.append(x)
    adt_dict = {}
    adt_dict.update({"data" : dat})
    x = JSONEncoder().encode(dat)
    return x

# 5 done
@app.get("/get_IP_list/")
async def read_item():
    IPs = []

    for x in mycol.find({ "ip": { "$regex" : "^192."} }, {"_id": 0, "date": 0, "time": 0, "fan": 0, "ugpu": 0, "mgpu": 0, "temp": 0, "power": 0}):
        IPs.append(x.get("ip"))

    adt_dict = {}
    adt_dict.update({"IPs" : list(set(IPs))})
    x = JSONEncoder().encode(adt_dict)
    return x

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')