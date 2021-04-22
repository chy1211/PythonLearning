a = [33, 5, 9, 100, 80, 58, 15, 51]
for j in range(len(a) - 1):
    for i in range(len(a) - j - 1):
        if a[i] > a[i + 1]:
            tmp = a[i]
            a[i] = a[i + 1]
            a[i + 1] = tmp
            print(a)