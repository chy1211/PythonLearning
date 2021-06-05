a = input("輸入一組四位數字:")
j = temp = 0
list1 = [0, 0, 0, 0]
for i in a:
    list1[j] = (int(i) + 7) % 10
    j += 1
temp = list1[0]
list1[0] = list1[2]
list1[2] = temp
temp = list1[1]
list1[1] = list1[3]
list1[3] = temp
print("加密後的數字為:", str(list1[0]) + str(list1[1]) + str(list1[2]) + str(list1[3]))
