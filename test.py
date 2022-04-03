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
#         if i == leny:
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
#             print(a) 