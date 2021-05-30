a = list(input("number?"))
for j in range(len(a) - 1):
    for i in range(len(a) - j - 1):
        if a[i] > a[i + 1]:
            tmp = a[i]
            a[i] = a[i + 1]
            a[i + 1] = tmp
A = ""
for i in a:
    A += i
print(A)

b = a
for j in range(len(a) - 1):
    for i in range(len(a) - j - 1):
        if a[i] < a[i + 1]:
            tmp = a[i]
            a[i] = a[i + 1]
            a[i + 1] = tmp
B = ""
for i in b:
    B += i
print(B)

print(int(B) - int(A))
