tmp = ord("A")
tmp1 = []
for i in range(6):
    tmp += i
    tmp1.append(chr(tmp))
print(tmp1)
z = 0
for i in range(4):
    for j in range(i):
        print(tmp1[z], end="")
        z += 1
    print()