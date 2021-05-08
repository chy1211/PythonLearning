#fp=open("test2.csv","r") locate
fp=open("./109_before_middle_test_2/0505/test2.csv","r")

tmp = fp.readline()

class Student:
    def __init__(self):
        self.cla = []
        self.id = []
        self.name = []
        self.git = []

theclass = Student()

while True:
    ftmp = fp.readline()
    if ftmp == "":
        break
    else:
        tmp = ftmp.replace("\n","").replace(" ","").replace("?","").split(",")
        theclass.cla.append(tmp[0])
        theclass.id.append(tmp[1])
        theclass.name.append(tmp[2])
        theclass.git.append(tmp[3])
i = 0
while True:
    if theclass.cla[i] == ",":
        break
    else:
        print(theclass.cla[i],theclass.id[i],theclass.name[i],theclass.git[i])
        i += 1
fp.close()