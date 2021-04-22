a = int(input("層?"))
for i in range(1, a + 1):
    print(i * '*')

for i in range(0, a + 1):
    print(' ' * (a - i) + i * '*')

for i in range(0, a + 1):
    print(' ' * (a - i) + i * '*', end='')
    for j in range(i - 1, i):
        print('*' * j)

for i in range(0, a + 1):
    print(' ' * (a - i) + i * '* ')
