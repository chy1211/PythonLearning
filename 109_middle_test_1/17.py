a = (input("輸入五張牌:"))
listm = a.split()
total = 0

if listm[0] == 'A':
    listm[0] = 1
elif listm[0] == 'J' or listm[0] == 'j':
    listm[0] = 11
elif listm[0] == 'Q' or listm[0] == 'q':
    listm[0] = 12
elif listm[0] == 'K' or listm[0] == 'k':
    listm[0] = 13

if listm[1] == 'A':
    listm[1] = 1
elif listm[1] == 'J' or listm[1] == 'j':
    listm[1] = 11
elif listm[1] == 'Q' or listm[1] == 'q':
    listm[1] = 12
elif listm[1] == 'K' or listm[1] == 'k':
    listm[1] = 13

if listm[2] == 'A':
    listm[2] = 1
elif listm[2] == 'J' or listm[2] == 'j':
    listm[2] = 11
elif listm[2] == 'Q' or listm[2] == 'q':
    listm[2] = 12
elif listm[2] == 'K' or listm[2] == 'k':
    listm[2] = 13

if listm[3] == 'A':
    listm[3] = 1
elif listm[3] == 'J' or listm[3] == 'j':
    listm[3] = 11
elif listm[3] == 'Q' or listm[3] == 'q':
    listm[3] = 12
elif listm[3] == 'K' or listm[3] == 'k':
    listm[3] = 13

if listm[4] == 'A':
    listm[4] = 1
elif listm[4] == 'J' or listm[4] == 'j':
    listm[4] = 11
elif listm[4] == 'Q' or listm[4] == 'q':
    listm[4] = 12
elif listm[4] == 'K' or listm[4] == 'k':
    listm[4] = 13

for i in listm:
    total += int(i)
print("總點數為:", total)
