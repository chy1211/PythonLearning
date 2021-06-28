import getData as get
import matplotlib.pyplot as plt
from datetime import timedelta
from datetime import datetime

font = {"family": "DFKai-SB", "weight": "bold", "size": "12"}
plt.rc("font", **font)


def showSinCSC(date1, date2, rn):
    day = timedelta(hours=24)
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    d2 += day
    leng = 0
    while d1 != d2:
        leng += 1
        d1 += day
    data = get.getSinCSC(f"{date1}", f"{date2}", f"{rn}")
    date = []
    value = []
    y_index = [i for i in range(0, 105, 5)]
    for i in range(leng):
        date.append(str(data["date"][i]))
        value.append(float(data["value"][i]))
    plt.style.use("ggplot")
    plt.figure(figsize=(12, 10), dpi=300)
    plt.plot(date, value)
    plt.xlabel("Month", fontsize=10, labelpad=5)
    plt.ylabel("Percent", fontsize=10, labelpad=10)
    plt.title(f"{rn} {date1} 至 {date2} 容量趨勢", fontsize=15, y=1)
    plt.xticks(rotation=45)
    plt.yticks(y_index)
    plt.show()


def saveSinCSC(date1, date2, rn):
    day = timedelta(hours=24)
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    d2 += day
    leng = 0
    while d1 != d2:
        leng += 1
        d1 += day
    data = get.getSinCSC(f"{date1}", f"{date2}", f"{rn}")
    date = []
    value = []
    y_index = [i for i in range(0, 105, 5)]
    for i in range(leng):
        date.append(str(data["date"][i]))
        value.append(float(data["value"][i]))
    plt.style.use("ggplot")
    plt.figure(figsize=(12, 10), dpi=300)
    plt.plot(date, value)
    plt.xlabel("Month", fontsize=20, labelpad=5)
    plt.ylabel("Percent", fontsize=20, labelpad=10)
    plt.title(f"{rn} {date1} 至 {date2} 容量趨勢", fontsize=30, y=1)
    plt.xticks(rotation=45)
    plt.yticks(y_index)
    plt.savefig(f"{rn}-{date1}至{date2}容量趨勢.png")
