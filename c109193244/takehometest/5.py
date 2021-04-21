N=Temp=1
M=int(input("輸入階乘值M:"))
while True:
    N+=1
    Temp=Temp*N
    if Temp<M:
        print(N)
    else:
        break
print("超過M為",M,"的最小階層N值為:",N)