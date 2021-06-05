import json
import requests

data = {"lang": "tw", "type": "2"}
response = requests.get("https://apis.youbike.com.tw/api/front/station/all", data)

if response.status_code == 200:
    tmp = json.loads(response.content)
    print(tmp["retCode"])
    print(tmp["retMsg"])
    totalvalues = []
    for i in tmp["retVal"]:
        values = []
        keys = []
        for key, value in i.items():
            keys.append(key)
            values.append(value)
        totalvalues.append(values)
    print(totalvalues)
    print(keys)
