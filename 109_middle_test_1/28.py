A = 0
while A < 4:
    A = B = 0
    lista = list('1234')
    listb = list(input("your answer?"))
    print("your answer:", listb)
    for i in listb:
        for j in lista:
            if i == j:
                if lista.index(j) == listb.index(i):
                    A += 1
                else:
                    B += 1
    print(A, "A", B, "B")
