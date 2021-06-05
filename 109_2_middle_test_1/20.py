aList = [123, 456, 789, 321, 654]
a = int((input("輸入查詢學號:")))
b = aList.index(a)
aList[0] = ["Tom", "DTGD"]
aList[1] = ["Cat", "CSIE"]
aList[2] = ["Nana", "ASIE"]
aList[3] = ["Lim", "DBA"]
aList[4] = ["Won", "FDD"]
print("學生資料為:", a, aList[b][0], aList[b][1])
