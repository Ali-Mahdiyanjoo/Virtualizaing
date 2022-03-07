from urllib import response
import requests

response = requests.get("https://panel.plusai.cloud/api-gpu-monitor")
print(response)