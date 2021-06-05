year = input("年")
month = input("月")
day = input("日")
total = year + month + day
sum = 0
for i in total:
    sum += int(i)
print(sum)

while sum >= 10:
    sum = sum // 10 + sum % 10

print(sum)
