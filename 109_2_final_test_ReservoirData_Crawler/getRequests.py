import requests
from bs4 import BeautifulSoup as BS


def reservoir(area):
    # 爬取資料
    data = {"area": f"{area}"}
    response = requests.get("https://www.wra.gov.tw/common/getReservoir.ashx", data)
    soup = BS(response.text, "html.parser")
    # 區域偵測 Area detection
    currentarea = data["area"]
    print("目前" + f"{currentarea}" + "水庫:")
    # 列出目前水庫資料(有效蓄水量,目前水位,目前蓄水容量,記錄時間)
    damdata = []
    for ul in soup.find_all("ul"):
        for li in ul.find_all("li"):
            damdata.append(li.string)
    # 資料長度
    releng = len(soup.find_all("ul"))
    print("共有" + f"{releng}" + "個水庫")
    dataleng = releng * 4
    # 列出所有搜尋到的水庫
    RSN = []
    span_tags = soup.find_all("span")
    for tag in span_tags:
        RSN.append(tag.string)
    # 擷取有效蓄水量, Effective storage capacity
    ESC = []
    for i in range(0, dataleng, 4):
        ESC.append(str(damdata[i]).replace("有效蓄水量：", "").replace("(萬立方公尺)", ""))
    # 擷取目前水位, Current water level
    CWL = []
    for i in range(1, dataleng, 4):
        CWL.append(str(damdata[i]).replace("目前水位為：", "").replace("(公尺)", ""))
    # 擷取目前蓄水容量, Current storage capacity
    CSC = []
    for i in range(2, dataleng, 4):
        CSC.append(str(damdata[i]).replace("有效蓄水容量：", ""))
    # 擷取記錄時間, Record time
    RT = []
    for i in range(3, dataleng, 4):
        RT.append(str(damdata[i]).replace("記錄時間：", ""))
    # 回傳資料
    result = [RSN, ESC, CWL, CSC, RT]
    return result


def rnleng():
    area = ["北區", "中區", "南區"]
    releng = 0
    for i in area:
        data = {"area": f"{i}"}
        response = requests.get("https://www.wra.gov.tw/common/getReservoir.ashx", data)
        soup = BS(response.text, "html.parser")
        releng += len(soup.find_all("ul"))
    return releng
