import getRequests as RS
import pymysql
from datetime import datetime


def Update():
    date = datetime.now().strftime("%Y-%m-%d")  # 時間,Time
    RSN = []  # 水庫名稱, Reservoir name
    ESC = []  # 有效蓄水量, Effective storage capacity
    CWL = []  # 目前水位, Current water level
    CSC = []  # 目前蓄水容量, Current storage capacity
    RT = []  # 記錄時間, Record time

    # 取得所有水庫資料
    data = ["北區", "中區", "南區"]
    for i in data:
        result = RS.reservoir(f"{i}")
        RSN += result[0]
        ESC += result[1]
        CWL += result[2]
        CSC += result[3]
        RT += result[4]

    # 寫入資料庫
    conn = pymysql.connect(
        host="xiaoyi1211.ddns.net",
        port=3306,
        user="chy",
        passwd="Henrychy@1211",
        db="reservoir",
        charset="utf8",
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    # 更新所有資料
    print("正在更新總資料:")
    for i in range(len(RSN)):
        sql = f"UPDATE `dam-data` SET `ESC`='{str(ESC[i])}',`CWL`='{str(CWL[i])}',`CSC`='{str(CSC[i])}',`RT`='{str(RT[i])}' WHERE `RN`='{str(RSN[i])}'"
        cursor.execute(sql)
        print(f"第{i+1}筆資料")
        conn.commit()

    # 紀錄並更新水位

    # 創建當日資料表
    sql = f"CREATE TABLE IF NOT EXISTS `{date}` (`RN` varchar(20) NOT NULL,`CSC` varchar(20) NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"
    try:
        cursor.execute(sql)
    except Exception as e:
        print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
        pass

    # 更新水位資訊
    sql = f"SELECT * FROM `{date}`"
    cursor.execute(sql)
    if cursor.fetchall() != ():
        print("正在更新水位資料:")
        for i in range(len(RSN)):
            sql = f"UPDATE `{date}` SET `CSC`='{str(CSC[i])}' WHERE `RN` = '{str(RSN[i])}'"
            cursor.execute(sql)
            print(f"第{i+1}筆資料")
            conn.commit()
    else:
        print("正在新增水位資料:")
        for i in range(len(RSN)):
            sql = f"INSERT INTO `{date}` (`RN`, `CSC`) VALUES ('{str(RSN[i])}', '{str(CSC[i])}')"
            cursor.execute(sql)
            print(f"第{i+1}筆資料")
            conn.commit()
    message = "已更新完成"
    cursor.close()
    conn.close()
    return message
