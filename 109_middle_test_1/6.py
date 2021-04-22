a = list(input("輸入由0~9的數字所組成的N個數字字串"))

for j in range(len(a) - 1):
    for i in range(len(a) - j - 1):
        if a[i] > a[i + 1]:
            tmp = a[i]
            a[i] = a[i + 1]
            a[i + 1] = tmp
A = ("")
for i in a:
    A += i

b = a
for j in range(len(a) - 1):
    for i in range(len(a) - j - 1):
        if a[i] < a[i + 1]:
            tmp = a[i]
            a[i] = a[i + 1]
            a[i + 1] = tmp
B = ("")
for i in b:
    B += i

print("最大值數列", B, "與最小值數列", A, "差值為:", int(B) - int(A))
