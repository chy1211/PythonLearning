aList = ['蘋果','香蕉','葡萄','藍莓','橘子']
a=(input("請輸入水果:"))
b=aList.index(a)
aList[0]=['紅色']
aList[1]=['黃色']
aList[2]=['紫色']
aList[3]=['藍色']
aList[4]=['橘色']
print(a,"是",aList[b][0])