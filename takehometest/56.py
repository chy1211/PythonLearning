total=0

a=input("請選擇主餐及升級的套餐:")
listm=[]
for i in a:
    listm.append(i)

if listm[0]=='1':
    total+=72
elif listm[0]=='2':
    total+=62
elif listm[0]=='3':
    total+=82
elif listm[0]=='4':
    total+=44
elif listm[0]=='5':
    total+=60

if listm[1]=='A':
    total+=55
elif listm[1]=='B':
    total+=68

b=input("是否升級成大杯飲料:")
if b == '是':
    total+=7
else:
    total+=0

c=input("是否換成大薯:")
if c == '是':
    total+=13
else:
    total+=0

print("總共為",total,"元")