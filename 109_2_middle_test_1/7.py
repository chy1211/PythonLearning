fee = int(input("輸入月租費"))
time = int(input("輸入通話時間"))

if fee == 186:
    fee1 = time * 0.09
    discount = fee1 / fee
    if discount > 1:
        fee1 = fee1 * 0.8
    else:
        fee1 = fee1 * 0.9
    print("通話費為:", round(fee1), "元")
elif fee == 386:
    fee1 = time * 0.08
    discount = fee1 / fee
    if discount > 1:
        fee1 = fee1 * 0.7
    else:
        fee1 = fee1 * 0.8
    print("通話費為:", round(fee1), "元")
elif fee == 586:
    fee1 = time * 0.07
    discount = fee1 / fee
    if discount > 1:
        fee1 = fee1 * 0.6
    else:
        fee1 = fee1 * 0.7
    print("通話費為:", round(fee1), "元")
elif fee == 986:
    fee1 = time * 0.06
    discount = fee1 / fee
    if discount > 1:
        fee1 = fee1 * 0.5
    else:
        fee1 = fee1 * 0.6
    print("通話費為:", round(fee1), "元")
else:
    print("錯誤!無此月租費方案")
