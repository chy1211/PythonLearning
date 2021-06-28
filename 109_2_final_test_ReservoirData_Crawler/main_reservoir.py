import drawPicture as draw
import reservoir_sel as rqcsc
import reservoir_update as up
import getData as get
import tkinter as tk
from tkinter import Button, ttk

print("程式載入中...")
datecombo = rqcsc.showtable()
damcombo = rqcsc.showrn()


def verificationDate():
    d1 = date1()
    d2 = date2()
    if d1 == d2:
        status = -1
        return status
    elif d1 > d2:
        status = 0
        return status
    else:
        status = 1
        return status


def date1():
    return datecombo[date1_combo.current()]


def date2():
    return datecombo[date2_combo.current()]


def dam():
    return damcombo[dam_combo.current()]


def update():
    mes = up.Update()
    tk.messagebox.showinfo(title=mes, message=mes)


def analysis():
    if verificationDate() == -1:
        tk.messagebox.showwarning(title="警告", message="請勿選擇相同日期!")
    elif verificationDate() == 0:
        tk.messagebox.showwarning(title="警告", message="起日不得晚於迄日!")
    else:
        result_text.set(get.getSinCSC(date1(), date2(), dam()))


def show():
    if verificationDate() == -1:
        tk.messagebox.showwarning(title="警告", message="請勿選擇相同日期!")
    elif verificationDate() == 0:
        tk.messagebox.showwarning(title="警告", message="起日不得晚於迄日!")
    else:
        draw.showSinCSC(date1(), date2(), dam())


def save():
    if verificationDate() == -1:
        tk.messagebox.showwarning(title="警告", message="請勿選擇相同日期!")
    elif verificationDate() == 0:
        tk.messagebox.showwarning(title="警告", message="起日不得晚於迄日!")
    else:
        draw.saveSinCSC(date1(), date2(), dam())
        tk.messagebox.showinfo(
            title="已存", message=f"已將結果存成{dam()}-{date1()}至{date2()}容量趨勢.png"
        )


win = tk.Tk()
win.title("水庫分析系統")
win.resizable(0, 0)

label1 = tk.Label(win, text="請選擇起迄日期及水庫")
label1.grid(column=0, row=0, columnspan=4)

print("正在取得資料表")
date1_combo = ttk.Combobox(win, values=rqcsc.showtable(), state="readonly")
date1_combo.grid(column=0, row=2)
date1_combo.current(0)

label2 = tk.Label(win, text="至")
label2.grid(column=1, row=2)

date2_combo = ttk.Combobox(win, values=rqcsc.showtable(), state="readonly")
date2_combo.grid(column=2, row=2)
date2_combo.current(0)

print("正在取得資料")
dam_combo = ttk.Combobox(win, values=rqcsc.showrn(), state="readonly")
dam_combo.grid(column=3, row=2)
dam_combo.current(0)

btn_update = Button(text="將資料庫資料更新", command=update)
btn_update.grid(column=0, row=3)

btn_analysis = Button(text="分析該時間區段資料", command=analysis)
btn_analysis.grid(column=1, row=3)

btn_draw = Button(text="將資料繪製成圖", command=show)
btn_draw.grid(column=2, row=3)

btn_save = Button(text="將圖存成檔案", command=save)
btn_save.grid(column=3, row=3)

result_text = tk.StringVar()  # 設置動態文字
label_result = tk.Label(win, textvariable=result_text)  # 文字
label_result.grid(column=0, row=4, columnspan=4)  # 以grid方式放置 文字

win.mainloop()
