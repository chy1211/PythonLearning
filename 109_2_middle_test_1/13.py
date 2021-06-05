a = input("請輸入連續字元:")

if not a:
    print("請不要輸入空字串!")
    a = input("請輸入連續字元:")

b = reversed(list(a))

if list(a) == list(b):
    print("YES")
else:
    print("NO")
