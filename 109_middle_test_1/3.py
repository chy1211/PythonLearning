mlist = [
    "rat", "ox", "tiger", "rabbit", "dragon", "snake", "horse", "sheep",
    "monkey", "rooster", "dog", "pig"
]
year = int((input("請輸入出生年")))
print(mlist[year % 12 - 4])
