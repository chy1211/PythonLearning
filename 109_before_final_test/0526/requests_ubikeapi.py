import requests

data = {'lang':'tw','type':'2'}
response = requests.get("https://apis.youbike.com.tw/api/front/station/all",data)

if response.status_code == 200:
    print(response.content.decode('utf-8'))