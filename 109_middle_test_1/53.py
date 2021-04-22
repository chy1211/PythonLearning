import math

km = float((input("輸入路程公里數:")))
fee = 0
if km <= 1.5:
    fee = 75
else:
    fee = 75 + 5 * math.ceil((km - 1.5) / 0.25)
print("所需車資為:", fee, "元")
