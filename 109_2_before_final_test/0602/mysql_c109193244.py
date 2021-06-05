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
cusor = conn.cursor(pymysql.cursors.DictCursor)
# cusor.execute("INSERT INTO `student` (`name`, `id`, `gender`, `birthday`, `hobby`) VALUES ('test', 'c109156202', '0', '1980-01-01', 'None');")
cusor.execute("SELECT * FROM `st_py`")
rows = cusor.fetchall()
data = []
for i in rows:
    print(i)
    data.append(i)
print(data)
tmp = json.dumps(data, indent=1, ensure_ascii=False)
print(tmp)
conn.commit()
cusor.close()
conn.close()
