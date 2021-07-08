import tkinter as tk  # 匯入tkinter
from tkinter import Button, ttk  # 從tkinter匯入插件
import requests  # 匯入requests
import json  # 匯入json
import pandas as pd  # 匯入pandas並以pd命名
import matplotlib.pyplot as plt  # 匯入matplotlib.pyplot並以plt命名
from datetime import datetime  # 從datetime匯入datetime


font = {"family": "DFKai-SB", "weight": "bold", "size": "12"}  # 字體設定
plt.rc("axes", unicode_minus=False)  # 字體設定
plt.rc("font", **font)  # 將字體作為kwargs導入

try:  # 嘗試 request 該網站 如果發生錯誤則列印出來
    response = requests.get(
        "https://apis.youbike.com.tw/api/front/station/all?lang=tw&type=2"  # 在ubike網站從F12的network選項翻出請求地址
    )
except Exception as e:
    print(e)

time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 取得現在時間並將其格式化
json_content = json.loads(response.content)  # 將requests的資料轉成json
df = pd.DataFrame.from_dict(json_content["retVal"])  # 將requests資料中的"retVal"轉成資料框


def jsontofile():  # 輸出json格式
    with open("ubike_api.json", "w") as f:  # 將開啟資料以f替代
        jsontext = json.dumps(
            json_content, indent=3, ensure_ascii=False
        )  # 對資料進行縮排並取消ascii編碼避免造成亂碼
        json.dump(jsontext, f)  # 寫入檔案
        tk.messagebox.showinfo(title="已導出", message="已導出所有資料至ubike_api.json")  # 訊息視窗


def arco():  # 取得area_code (根據ubike2.0api 台北市分為00台中市分為01嘉義縣分為08高雄市分為12)
    if area_combo.current() == 0:  # 台北市
        areacode = "00"
    elif area_combo.current() == 1:  # 台中市
        areacode = "01"
    elif area_combo.current() == 2:  # 嘉義縣
        areacode = "08"
    else:  # 高雄市
        areacode = "12"
    return areacode


def ar():  # 取得area
    if area_combo.current() == 0:  # 台北市
        area = "台北市"
    elif area_combo.current() == 1:  # 台中市
        area = "台中市"
    elif area_combo.current() == 2:  # 嘉義縣
        area = "嘉義縣"
    else:  # 高雄市
        area = "高雄市"
    return area


def last_time():  # 更新資料時間
    for i in json_content["retVal"]:  # 將retVal中的所有項目放入迴圈
        values = [j[1] for j in i.items()]  # 將所有資料放入j以item的型式
    ls_Text.set(
        f"資料更新時間:{str(values[22])}"
    )  # values的index22=time為資料更新時間 故將其寫入ls這個lable內


def combobox_selected(evn):  # 判斷combobox選取的值
    nowchoose_Text.set(area_combo.get())  # 取得選取的值


def export():  # 匯出ubike2.0資料到csv
    df.to_csv(
        "ubike_data.csv", encoding="utf_8_sig", index=False
    )  # 以datafram to csv寫入ubike_data.csv
    tk.messagebox.showinfo(title="已導出", message="已將所有ubike2.0資料導出成csv")  # 訊息視窗


def analysis():  # 取得區域代碼
    area_code_Text.set("區域")  # 動態設定文字
    description_Text.set("數量(站)")  # 動態設定文字
    areacode = arco()  # 以函式取得area_code
    tmp = df[df["area_code"] == areacode]  # 將資料中符合area_code的資料調出
    station_at_current_area = tmp.groupby("district_tw").count()[
        ["area_code"]
    ]  # 用groupby方法跟count統計出有多少
    result_text.set(station_at_current_area)  # 將結果寫入result_text這個lable


def export_analysis():  # 匯出該區域分析資料
    areacode = arco()  # 以函式取得area_code
    area = ar()  # 以函式取得區域
    tmp = df[df["area_code"] == areacode]  # 將資料中符合area_code的資料調出
    station_at_current_area = tmp.groupby("district_tw").count()[
        ["area_code"]
    ]  # 用groupby方法跟count統計出有多少
    station_at_current_area.to_csv(
        f"ubike_{area}.csv", encoding="utf_8_sig"
    )  # 以datafram to csv寫入ubike_{區域}.csv <---format in string
    tk.messagebox.showinfo(title="已導出", message=f"已將{area}的ubike2.0資料導出成csv")  # 訊息視窗


def plt_draw():  # 以matplotlib繪製
    areacode = arco()  # 以函式取得area_code
    area = ar()  # 以函式取得區域
    tmp = df[df["area_code"] == areacode]  # 將資料中符合area_code的資料調出
    station_at_current_area = tmp.groupby("district_tw").count()[
        ["area_code"]
    ]  # 用groupby方法跟count統計出有多少
    plt_result = station_at_current_area.sort_values(by="area_code")  # 將值傳入plt_result內
    plt_result["area_code"].plot.bar(
        title=f"{area}內 ubike站數", figsize=[10, 10]
    )  # 以條狀圖繪製
    plt.show()  # 繪圖


def status():  # 查詢狀態
    area_code_Text.set("狀態(1=正常2=異常)")  # 動態設定文字
    description_Text.set("數量(站)")  # 動態設定文字
    areacode = arco()  # 以函式取得area_code
    tmp = df[df["area_code"] == areacode]  # 將資料中符合area_code的資料調出
    station_at_current_area = tmp.groupby("status").count()[
        ["area_code"]
    ]  # 用groupby方法跟count統計出有多少
    result_text.set(station_at_current_area)  # 將結果寫入result_text這個lable


def quit():  # 關閉
    Msgbox = tk.messagebox.askquestion(title="確認", message="確定要關閉?")  # 詢問是否要關閉
    if Msgbox == "yes":  # 如果是
        tk.messagebox.showwarning(title="警告", message="程式將關閉!")  # 警告視窗
        win.destroy()  # 關閉視窗
    else:  # 如果不是
        tk.messagebox.showinfo("歡迎回來", "歡迎繼續使用")  # 訊息視窗


def readme():  # 說明
    tk.messagebox.showinfo(
        title="說明",
        message="本程式資料取自https://apis.youbike.com.tw/api/front/station/all?lang=tw&type=2",
    )  # 訊息視窗
    tk.messagebox.showinfo(title="說明", message="更新時間為開啟程式時爬取自該網站")  # 訊息視窗
    tk.messagebox.showinfo(title="說明", message="多次請求資料可能會導致程式無法正常運作!")  # 訊息視窗


def alpha(val):  # 調整透明度
    vale = scale_alpha.get() / 100  # 將值除以100
    win.attributes("-alpha", vale)  # 將結果放入並調整


def updatetime():  # 取得現在時間
    time_TEXT.set(f"現在時間是:{time}")  # 設定現在時間


win = tk.Tk()  # 將tk.Tk()指定給win

win.title("ubike分析系統")  # 標題
win.resizable(0, 0)  # 禁止改變大小
# 選取說明文字
label1 = tk.Label(win, text="請選擇分析區域")  # 文字
label1.grid(column=0, row=0)  # 以grid方式放置 文字
# 下拉選單
area_combo = ttk.Combobox(
    win, values=["台北市", "台中市", "嘉義縣", "高雄市"], state="readonly"
)  # 下拉選單
area_combo.grid(column=1, row=0)  # 以grid方式放置 combobox
area_combo.current(0)  # 預設值為台北市
area_combo.bind("<<ComboboxSelected>>", combobox_selected)  # 將選取綁定事件
# 說明
btn_readme = Button(text="說明", command=readme)  # 按鈕
btn_readme.grid(column=2, row=0)  # 以grid方式放置 按鈕
# 關閉程式
btn_quit = Button(text="關閉程式", command=quit)  # 按鈕
btn_quit.grid(column=2, row=1)  # 以grid方式放置 按鈕
# 選取說明文字
label_chooseset = tk.Label(win, text="您目前選擇的是:")  # 設置靜態文字
label_chooseset.grid(column=0, row=1)  # 以grid方式放置 文字
# 選取資料確認
nowchoose_Text = tk.StringVar()  # 設置動態文字
nowchoose_Text.set(area_combo.get())  # 其值為combobox選取值
label_nowchoose = tk.Label(win, textvariable=nowchoose_Text)  # 文字
label_nowchoose.grid(column=1, row=1)  # 以grid方式放置 文字
# 透明度調整
scale_alpha = tk.Scale(win, command=alpha, from_=100, to=10)  # 滑桿
scale_alpha.grid(column=2, row=2, rowspan=6)  # 以grid方式放置 滑桿
# 分析區域
btn_analysis = Button(text="分析該區域站數", command=analysis)  # 按鈕
btn_analysis.grid(column=0, row=2)  # 以grid方式放置 按鈕
# 導出所有資料
btn_export = Button(text="導出所有ubike2.0資料", command=export)  # 按鈕
btn_export.grid(column=1, row=2)  # 以grid方式放置 按鈕
# 顯示圖表按鈕
btn_export_analysisp = Button(text="顯示此區域分析圖表", command=plt_draw)  # 按鈕
btn_export_analysisp.grid(column=0, row=3)  # 以grid方式放置 按鈕
# 分析資料導出按鈕
btn_export_analysist = Button(text="導出此區域分析資料", command=export_analysis)  # 按鈕
btn_export_analysist.grid(column=1, row=3)  # 以grid方式放置 按鈕
# 查詢該區域狀態
btn_status = Button(text="查詢該區域的狀態", command=status)  # 按鈕
btn_status.grid(column=0, row=4)  # 以grid方式放置 按鈕
# 導出json檔案
btn_json = Button(text="導出json檔", command=jsontofile)  # 按鈕
btn_json.grid(column=1, row=4)  # 以grid方式放置 按鈕
# 資料最後更新時間
ls_Text = tk.StringVar()  # 設置動態文字
last_timet = tk.Label(win, textvariable=ls_Text)  # 文字
last_timet.grid(column=0, row=5, columnspan=2)  # 以grid方式放置 文字
last_time()  # 呼叫function last_time
# 現在時間
time_TEXT = tk.StringVar()  # 設置動態文字
time_ = tk.Label(win, textvariable=time_TEXT)  # 文字
time_.grid(column=0, row=6, columnspan=2)  # 以grid方式放置 文字
updatetime()  # 呼叫function updatetime
# 資料說明(area或status)
area_code_Text = tk.StringVar()  # 設置動態文字
area_code_description = tk.Label(win, textvariable=area_code_Text)  # 文字
area_code_description.grid(column=0, row=7)  # 以grid方式放置 文字
# 資料說明(quantity)
description_Text = tk.StringVar()  # 設置動態文字
description = tk.Label(win, textvariable=description_Text)  # 文字
description.grid(column=1, row=7)  # 以grid方式放置 文字
# 結果
result_text = tk.StringVar()  # 設置動態文字
label_result = tk.Label(win, textvariable=result_text)  # 文字
label_result.grid(column=0, row=8, columnspan=2)  # 以grid方式放置 文字
# 預設透明度
win.attributes("-alpha", 1)
# 主迴圈
win.mainloop()
