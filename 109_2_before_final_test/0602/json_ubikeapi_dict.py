import json
import requests

data = {"lang": "tw", "type": "2"}
response = requests.get("https://apis.youbike.com.tw/api/front/station/all", data)

if response.status_code == 200:
    tmp = json.loads(response.content)
    print(tmp["retCode"])
    print(tmp["retMsg"])
    keys = [i[0] for i in tmp["retVal"][0].items()]
    print(keys)
    totalvalues = []
    for i in tmp["retVal"]:
        values = [j[1] for j in i.items()]
        totalvalues.append(values)
    print(totalvalues)
    print(len(totalvalues))
