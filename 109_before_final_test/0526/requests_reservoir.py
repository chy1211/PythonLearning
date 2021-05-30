import requests

data = {"area": "南區"}
response = requests.get("https://www.wra.gov.tw/common/getReservoir.ashx", data)

if response.status_code == 200:
    print(response.content.decode("utf-8"))
