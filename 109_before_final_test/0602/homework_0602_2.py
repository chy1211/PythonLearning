import pymysql
import json

conn = pymysql.connect(
    host="192.168.184.128",
    port=3306,
    user="c109193244",
    passwd="1211",
    db="c109193244",
    charset="utf8",
)
cursor = conn.cursor(pymysql.cursors.DictCursor)
cursor.execute("SELECT * FROM `ubike_api`")
rows = cursor.fetchall()
data = []
for i in rows:
    data.append(i)
tmp = json.dumps(data, indent=3, ensure_ascii=False)
print(tmp)
conn.commit()
cursor.close()
conn.close()
