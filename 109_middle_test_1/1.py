def prime(x):
    if x > 2:
        for i in range(2, x - 1):
            if x % i == 0:
                return False
        return True
    elif x == 2:
        return True


in1 = "15693"
list1 = []
for i in range(5):  # 字串長度
    for j in range(i + 1, 5 + 1):
        if prime(int(in1[i:j])) is True:
            list1.append(in1[i:j])
print(len(list1))
print(list1)
if len(list1) == 0:
    print("No prime found")
else:
    print("子字串中最大的質數值為:", max(list1))
