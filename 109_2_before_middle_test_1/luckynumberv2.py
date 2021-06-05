year = input("年")
month = input("月")
day = input("日")
total = year + month + day
print(total)
sum = 0

while True:
    for i in total:
        sum += int(i)
    if sum >= 10:
        total = str(sum)
    else:
        break
print(sum)
