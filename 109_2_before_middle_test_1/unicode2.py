tmp = ord("H")
for i in range(1, 9):
    print(tmp)
    print(chr(tmp))
    if i % 2 == 0:
        tmp -= i
    else:
        tmp += i
