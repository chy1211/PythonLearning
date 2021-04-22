a = int(input("a邊?"))
b = int(input("b邊?"))
c = int(input("c邊?"))

if a + b > c and b + c > a and c + a > b:
    print("此為三角形")
else:
    print("這不是一個三角形")