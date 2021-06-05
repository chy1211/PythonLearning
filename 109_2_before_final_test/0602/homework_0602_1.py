import json
import requests
import pymysql


data = {"lang": "tw", "type": "2"}
response = requests.get("https://apis.youbike.com.tw/api/front/station/all", data)
conn = pymysql.connect(
    host="192.168.184.128",
    port=3306,
    user="c109193244",
    passwd="1211",
    db="c109193244",
    charset="utf8",
)
cursor = conn.cursor(pymysql.cursors.DictCursor)
if response.status_code == 200:
    tmp = json.loads(response.content)
    print(tmp["retCode"])
    print(tmp["retMsg"])
    # keys = [i[0] for i in tmp["retVal"][0].items()]
    # print(keys) 列出索引
    totalvalues = []
    for i in tmp["retVal"]:
        values = [j[1] for j in i.items()]
        cursor.execute(
            "INSERT INTO `ubike_api` (`country_code`, `area_code`, `type`, `status`, `station_no`, `name_tw`, `district_tw`, `address_tw`, `name_en`, `district_en`, `address_en`, `name_cn`, `district_cn`, `address_cn`, `parking_spaces`, `available_spaces`, `empty_spaces`, `forbidden_spaces`, `lat`, `lng`, `img`, `updated_at`, `time`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (
                str(values[0]),
                str(values[1]),
                str(values[2]),
                str(values[3]),
                str(values[4]),
                str(values[5]),
                str(values[6]),
                str(values[7]),
                str(values[8]),
                str(values[9]),
                str(values[10]),
                str(values[11]),
                str(values[12]),
                str(values[13]),
                str(values[14]),
                str(values[15]),
                str(values[16]),
                str(values[17]),
                str(values[18]),
                str(values[19]),
                str(values[20]),
                str(values[21]),
                str(values[22]),
            ),
        )
        totalvalues.append(values)
        print(f"正在新增資料，目前進度第:{len(totalvalues)}筆資料。 ")
        conn.commit()
    print("共新增" + f"{len(totalvalues)}" + "筆資料!")
cursor.close()
conn.close()
