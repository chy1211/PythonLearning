import pymysql


def selsincsc(date, rn):
    data = []
    conn = pymysql.connect(
        host="xiaoyi1211.ddns.net",
        port=3306,
        user="chy",
        passwd="**",
        db="reservoir",
        charset="utf8",
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(f'SELECT `CSC` FROM `{date}` WHERE RN = "{rn}"')
    row = ""
    row = cursor.fetchall()
    rows = row[0]
    value = rows["CSC"]
    data = float(value.replace("%", ""))
    conn.commit()
    cursor.close()
    conn.close()
    return data


def showtable():
    data = []
    conn = pymysql.connect(
        host="xiaoyi1211.ddns.net",
        port=3306,
        user="chy",
        passwd="**",
        db="reservoir",
        charset="utf8",
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SHOW TABLES WHERE Tables_in_reservoir !="dam-data"')
    row = ""
    row = cursor.fetchall()
    for i in row:  # 取出value
        for key, value in i.items():
            data.append(value)
    conn.commit()
    cursor.close()
    conn.close()
    return data


def showrn():
    data = []
    conn = pymysql.connect(
        host="xiaoyi1211.ddns.net",
        port=3306,
        user="chy",
        passwd="**",
        db="reservoir",
        charset="utf8",
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT `RN` FROM `dam-data`")
    row = ""
    row = cursor.fetchall()
    for i in row:  # 取出value
        for key, value in i.items():
            data.append(value)
    conn.commit()
    cursor.close()
    conn.close()
    return data
