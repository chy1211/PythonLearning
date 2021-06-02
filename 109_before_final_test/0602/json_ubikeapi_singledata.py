import json
import requests

data = {"lang": "tw", "type": "2"}
response = requests.get("https://apis.youbike.com.tw/api/front/station/all", data)

if response.status_code == 200:
    tmp = json.loads(response.content)
    print(tmp["retCode"])
    print(tmp["retMsg"])
    for key, value in tmp["retVal"][49].items():
        print(key + ":" + str(value))
    print("///////////")
    for key, value in tmp["retVal"][50].items():
        print(key + ":" + str(value))
    # for i in tmp["retVal"]:
    # print(i)
