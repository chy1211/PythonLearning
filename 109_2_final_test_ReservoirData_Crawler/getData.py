import reservoir_sel as rqcsc
from datetime import timedelta
from datetime import datetime
import pandas as pd

day = timedelta(hours=24)
date = datetime.now().strftime("%Y-%m-%d")


def getSinCSC(date1, date2, rn):
    print(f"正在取得 {rn} {date1} 至 {date2} 的資料:")
    date1 = datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.strptime(date2, "%Y-%m-%d")
    date2 += day
    leng = 0
    value = []
    date = []
    while date1 != date2:
        date1 = datetime.strftime(date1, "%Y-%m-%d")
        date.append(date1)
        value.append(rqcsc.selsincsc(f"{date1}", f"{rn}"))
        print(f"目前進度:{date1}")
        date1 = datetime.strptime(date1, "%Y-%m-%d")
        leng += 1
        date1 += day
    DataPD = pd.DataFrame(
        columns=["date", "value"],
    )
    for i in range(leng):
        newrow = pd.DataFrame.from_dict(
            {"date": [f"{date[i]}"], "value": [f"{value[i]}"]}
        )
        DataPD = DataPD.append(newrow, ignore_index=True)
    return DataPD
