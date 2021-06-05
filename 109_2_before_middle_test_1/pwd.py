import os

print(os.getcwd())

fp = open("record.txt", "r")

tmp = fp.readline()

tmp1 = tmp.replace("\n", "")
tmp2 = tmp1.split(",")
print(tmp2)

while tmp != "":
    tmp = fp.readline()
    tmp1 = tmp.replace("\n", "")
    tmp2 = tmp1.split(",")
    print(tmp2)

fp.close()
