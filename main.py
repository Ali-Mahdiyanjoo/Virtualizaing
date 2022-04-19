# main.py
from datetime import datetime as dtt
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

app = FastAPI()
client = MongoClient(host="localhost", port=27017) # host and port for mongoDB connection
db = client["GPU_MONITORING"] # database name
mycol = db["DATAS"] # collection name for IP of machines with duplicate IPs
mycol_single = db["DATAS_SINGLE"] # collection name for IP of machines with single IP

class JSONEncoder(json.JSONEncoder): # this class is used to encode values for JSON
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

class GPU_DATA(BaseModel): # this class is used to create schema for data that will be resived from client
    fan : str
    ugpu : str 
    mgpu : str
    temp : str
    power : str
    ip : str

@app.post("/")
async def getting_data(data : GPU_DATA):
    data_dict = dict(data) # this line is used to create dictionary from GPU_DATA class
    daty = time.strftime("%Y-%m-%d") 
    timy = time.strftime("%H:%M:%S")
    data_dict.update({"date": daty + " " + timy}) # this line is used to add date and time to dictionary
    x = mycol.insert_one(data_dict) # this line is used to insert data to mongoDB collection
    y = JSONEncoder().encode(data_dict) # this line is used to encode data to JSON
    return y

@app.post("/realtime")
async def getting_data(data : GPU_DATA):
    data_dict = dict(data) # data_dict = {"fan": data.fan, "ugpu": data.ugpu, "mgpu": data.mgpu, "temp": data.temp, "power": data.power, "ip": data.ip}
    timy = datetime.now().time() 
    t1 = timedelta(hours=timy.hour, minutes=timy.minute)
    data_dict.update({"time": str(t1)}) # add time to data_dict
    IP = data_dict["ip"] # get ip from data_dict
    IP_dict = mycol_single.find_one({"ip": IP}) # it will go to see there is a document with this IP
    for x in mycol_single.find({"ip": { "$regex" : "^192."}}):
        end = x["time"]
        tim = datetime.now().time()
        t2 = timedelta(hours=tim.hour, minutes=tim.minute) # format the time from data_dict in database
        time_only = dtt.strptime(str(t2), "%H:%M:%S") - dtt.strptime(end, "%H:%M:%S") # calculate time difference from last record in database
        if str(time_only) == "0:10:00": # if the time is 10 minutes and not been update
            mycol_single.delete_one({"ip": IP}) # delete the document which has IP
    if IP_dict is None: # if there is no document with this IP
        mycol_single.insert_one(data_dict) # insert new document
        x = JSONEncoder().encode(data_dict) # encode it to JSON
        return x
    else:
        mycol_single.update_one({"ip": IP}, {"$set": data_dict}) # update the document which has specfic IP
        x = JSONEncoder().encode(data_dict)
        return x

@app.get("/api-gpu-monitor/{ip_address}")
async def read_item(ip_address):
    dat = []
    for x in mycol.find({"ip": { "$eq": ip_address }}): # find all documents which has IP
        dat.append(x) # append to dat
    adt_dict = {}
    adt_dict.update({"data" : dat}) # convert dat to dictionary
    x = JSONEncoder().encode(adt_dict) # encode dat to JSON
    return x

@app.get("/api-gpu-monitor-single/")
async def read_item():
    dat = []
    for x in mycol_single.find({"ip": { "$regex" : "^192."}}): # find all documents which has IP
        dat.append(x)
    adt_dict = {}
    adt_dict.update({"data" : dat}) # convert dat to dictionary
    x = JSONEncoder().encode(dat) # encode dat to JSON
    return x

@app.get("/get_IP_list/")
async def read_item():
    IPs = []
    for x in mycol.find({ "ip": { "$regex" : "^192."} }, {"_id": 0, "date": 0, "time": 0, "fan": 0, "ugpu": 0, "mgpu": 0, "temp": 0, "power": 0}): # find all documents which has IP and remove unnecesary values
        IPs.append(x.get("ip"))

    adt_dict = {}
    adt_dict.update({"IPs" : list(set(IPs))}) # convert dat to dictionary withou duplicate IPs
    x = JSONEncoder().encode(adt_dict) # encode dat to JSON
    return x

if __name__ == '__main__': # this line is used to run the server
    uvicorn.run(app, host='0.0.0.0', port=8000)