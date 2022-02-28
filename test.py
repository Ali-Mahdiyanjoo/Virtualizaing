# import requests
# import numpy as np
import time
# from datetime import datetime

# response = requests.get("https://panel.plusai.cloud/api-gpu-monitor")
# json_response = response.json()
# last_page = json_response["last_page"]
# for i in range(last_page):
#     i += 1
#     response = requests.get(f"https://panel.plusai.cloud/api-gpu-monitor?page={i}")
#     json_response = response.json()
#     now = datetime.now()
#     current_time = now.strftime("%H:%M:%S")
#     timey = {"current_time" : current_time}
#     json_response.update(timey)
#     print(json_response)
#     def IP_info():#

#         IP_list = []
#         for x in range(json_response["total"]):
#             ip = json_response["data"][x]["ip"]
#             IP_list.append(ip)
            
#         return IP_list

#     def fan_Data():#

#         fan_list = []
#         for x in range(json_response["total"]):
#                 fan = json_response["data"][x]["fan"]
#                 fan_list.append(fan)

#         if len(fan_list) % 4 == 0:
#             fan_list.sort(reverse=True)
#             fan_data = np.array(fan_list).reshape(-1, 4)

#         else:
#             len_old = len(fan_list)
#             while len_old % 4 != 0:
#                 len_old += 1
#                 if len_old % 4 == 0:
#                     len_new = len_old - len(fan_list)
#                     for i in range(len_new):
#                         fan_list.append(0)
#                     fan_list.sort(reverse=True)
#                     fan_data = np.array(fan_list).reshape(-1, 4)

#         return fan_data

#     def ugpu_Data():#

#         ugpu_list = []
#         for x in range(json_response["total"]):
#             ugpu = json_response["data"][x]["ugpu"]
#             ugpu_list.append(ugpu)

#         if len(ugpu_list) % 4 == 0:
#             ugpu_list.sort(reverse=True)
#             ugpu_data = np.array(ugpu_list).reshape(-1, 4)

#         else:
#             len_old = len(ugpu_list)
#             while len_old % 4 != 0:
#                 len_old += 1
#                 if len_old % 4 == 0:
#                     len_new = len_old - len(ugpu_list)
#                     for i in range(len_new):
#                         ugpu_list.append(0)
#             ugpu_list.sort(reverse=True)
#             ugpu_data = np.array(ugpu_list).reshape(-1, 4)

#         return ugpu_data

#     def mgpu_Data():#

#         mgpu_list = []
#         for x in range(json_response["total"]):
#             mgpu = json_response["data"][x]["mgpu"]
#             mgpu_list.append(mgpu)

#         if len(mgpu_list) % 4 == 0:
#             mgpu_list.sort(reverse=True)
#             mgpu_data = np.array(mgpu_list).reshape(-1, 4)

#         else:
#             len_old = len(mgpu_list)
#             while len_old % 4 != 0:
#                 len_old += 1
#                 if len_old % 4 == 0:
#                     len_new = len_old - len(mgpu_list)
#                     for i in range(len_new):
#                         mgpu_list.append(0)
#             mgpu_list.sort(reverse=True)
#             mgpu_data = np.array(mgpu_list).reshape(-1, 4)

#         return mgpu_data

#     def temp_Data():#

#         temp_list = []
#         for x in range(json_response["total"]):
#             temp = json_response["data"][x]["temp"]
#             temp_list.append(temp)

#         if len(temp_list) % 4 == 0:
#             temp_list.sort(reverse=True)
#             temp_data = np.array(temp_list).reshape(-1, 4)

#         else:
#             len_old = len(temp_list)
#             while len_old % 4 != 0:
#                 len_old += 1
#                 if len_old % 4 == 0:
#                     len_new = len_old - len(temp_list)
#                     for i in range(len_new):
#                         temp_list.append(0)        
#             temp_list.sort(reverse=True)
#             temp_data = np.array(temp_list).reshape(-1, 4)

#         return temp_data

#     def power_Data():

#         power_list = []
#         for x in range(json_response["total"]):
#             power = json_response["data"][x]["power"]
#             power_list.append(power)

#         if len(power_list) % 4 == 0:
#             power_list.sort(reverse=True)
#             power_data = np.array(power_list).reshape(-1, 4)

#         else:
#             len_old = len(power_list)
#             while len_old % 4 != 0:
#                 len_old += 1
#                 if len_old % 4 == 0:
#                     len_new = len_old - len(power_list)
#                     for i in range(len_new):
#                         power_list.append(0)        
#             power_list.sort(reverse=True)
#             power_data = np.array(power_list).reshape(-1, 4)

#         return power_data

while True: print("hi"); time.sleep(3)